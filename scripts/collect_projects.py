#!/usr/bin/env python3
"""
收集 GitHub 上的 MCP 项目
自动搜索、筛选并整理 MCP 相关项目
"""
import os
import json
import time
from datetime import datetime
from github import Github
from typing import List, Dict, Set
from pathlib import Path

# 场景分类
CATEGORIES = {
    'servers': 'MCP Servers',
    'clients': 'MCP Clients',
    'tools': 'Tools & Libraries',
    'examples': 'Examples',
    'documentation': 'Documentation'
}

# 搜索关键词
SEARCH_QUERIES = [
    'MCP',
    'Model Context Protocol',
    'mcp-server',
    'mcp-client',
    'model-context-protocol'
]

# GitHub Topics
TOPICS = [
    'mcp',
    'model-context-protocol',
    'mcp-server',
    'mcp-client',
    'modelcontextprotocol'
]

# 最小 Stars 数量
MIN_STARS = 10

# API 请求延迟（避免速率限制）
REQUEST_DELAY = 0.5

# 调试模式：通过环境变量控制，调试时只采集少量项目
DEBUG_MODE = os.environ.get('DEBUG_MODE', 'false').lower() == 'true'
MAX_PROJECTS_PER_QUERY = 3 if DEBUG_MODE else 30  # 调试模式：每个查询最多3个，正常模式：30个
MAX_SEARCH_QUERIES = 2 if DEBUG_MODE else len(SEARCH_QUERIES)  # 调试模式：只使用前2个查询
MAX_TOPICS = 1 if DEBUG_MODE else len(TOPICS)  # 调试模式：只使用前1个话题


def categorize_project(repo) -> str:
    """根据仓库信息分类项目"""
    name_lower = repo.name.lower()
    desc_lower = (repo.description or '').lower()
    readme_content = ''
    
    # 尝试获取 README 内容
    try:
        readme = repo.get_readme()
        readme_content = readme.decoded_content.decode('utf-8').lower()
    except:
        pass
    
    # 检查 topics
    topics = [t.lower() for t in repo.get_topics()]
    
    # 分类逻辑
    if any(keyword in name_lower or keyword in desc_lower or keyword in readme_content 
           for keyword in ['server', 'mcp-server']):
        return 'servers'
    elif any(keyword in name_lower or keyword in desc_lower or keyword in readme_content 
             for keyword in ['client', 'mcp-client']):
        return 'clients'
    elif any(keyword in name_lower or keyword in desc_lower 
             for keyword in ['example', 'demo', 'sample']):
        return 'examples'
    elif any(keyword in name_lower or keyword in desc_lower 
             for keyword in ['doc', 'documentation', 'wiki', 'guide']):
        return 'documentation'
    else:
        return 'tools'


def load_existing_projects(data_file: Path) -> Dict[str, Dict]:
    """加载已有的项目数据"""
    existing_projects = {}
    if data_file.exists():
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'projects' in data:
                    for project in data['projects']:
                        existing_projects[project['full_name']] = project
                    print(f"📂 加载了 {len(existing_projects)} 个已有项目")
        except Exception as e:
            print(f"⚠️  读取已有项目时出错: {str(e)}")
    return existing_projects


def collect_projects(github_token: str, existing_projects: Dict[str, Dict] = None) -> List[Dict]:
    """收集符合条件的 MCP 项目，保留已有项目并更新其信息"""
    g = Github(github_token)
    projects: Dict[str, Dict] = existing_projects.copy() if existing_projects else {}
    
    if DEBUG_MODE:
        print("🔧 调试模式：只采集少量项目以加快调试速度")
    
    print("开始收集 MCP 项目...")
    new_count = 0
    updated_projects = set()  # 记录被更新的项目，避免重复计数
    
    # 通过关键词搜索
    for query in SEARCH_QUERIES[:MAX_SEARCH_QUERIES]:
        print(f"搜索关键词: {query}")
        try:
            repos = g.search_repositories(
                query=f'{query} stars:>={MIN_STARS}',
                sort='stars',
                order='desc'
            )
            
            count = 0
            for repo in repos:
                try:
                    # 如果项目已存在，更新其信息
                    if repo.full_name in projects:
                        existing = projects[repo.full_name]
                        # 更新可能变化的信息
                        existing['stars'] = repo.stargazers_count
                        existing['updated_at'] = repo.updated_at.isoformat()
                        existing['language'] = repo.language or 'N/A'
                        existing['topics'] = repo.get_topics()
                        existing['archived'] = repo.archived
                        existing['description'] = repo.description or existing.get('description', '')
                        # 重新分类（可能分类规则变化）
                        existing['category'] = categorize_project(repo)
                        updated_projects.add(repo.full_name)
                        print(f"  ↻ 更新: {repo.full_name} ({repo.stargazers_count} ⭐)")
                        time.sleep(REQUEST_DELAY)
                        continue
                    
                    # 检查是否有 README
                    try:
                        repo.get_readme()
                    except:
                        print(f"  跳过 {repo.full_name}: 没有 README")
                        continue
                    
                    # 检查 Stars 数量
                    if repo.stargazers_count < MIN_STARS:
                        continue
                    
                    # 检查是否真的与 MCP 相关
                    desc_lower = (repo.description or '').lower()
                    name_lower = repo.name.lower()
                    topics = [t.lower() for t in repo.get_topics()]
                    
                    # 简单的相关性检查
                    mcp_keywords = ['mcp', 'model context protocol', 'model-context-protocol']
                    if not any(kw in desc_lower or kw in name_lower or kw in ' '.join(topics) 
                               for kw in mcp_keywords):
                        # 检查 topics
                        if not any(topic in topics for topic in TOPICS):
                            continue
                    
                    project = {
                        'name': repo.name,
                        'full_name': repo.full_name,
                        'description': repo.description or '',
                        'url': repo.html_url,
                        'stars': repo.stargazers_count,
                        'language': repo.language or 'N/A',
                        'updated_at': repo.updated_at.isoformat(),
                        'created_at': repo.created_at.isoformat(),
                        'topics': repo.get_topics(),
                        'category': categorize_project(repo),
                        'owner': repo.owner.login,
                        'archived': repo.archived
                    }
                    
                    projects[repo.full_name] = project
                    count += 1
                    print(f"  ✓ 收集: {repo.full_name} ({repo.stargazers_count} ⭐)")
                    
                    time.sleep(REQUEST_DELAY)
                    
                    # 限制每个查询最多收集的项目数
                    if count >= MAX_PROJECTS_PER_QUERY:
                        break
                        
                except Exception as e:
                    print(f"  错误处理 {repo.full_name}: {str(e)}")
                    continue
                    
        except Exception as e:
            print(f"搜索 '{query}' 时出错: {str(e)}")
            continue
    
    # 通过话题搜索
    for topic in TOPICS[:MAX_TOPICS]:
        print(f"搜索话题: {topic}")
        try:
            repos = g.search_repositories(
                query=f'topic:{topic} stars:>={MIN_STARS}',
                sort='stars',
                order='desc'
            )
            
            count = 0
            for repo in repos:
                try:
                    # 如果项目已存在，更新其信息
                    if repo.full_name in projects:
                        existing = projects[repo.full_name]
                        # 更新可能变化的信息
                        existing['stars'] = repo.stargazers_count
                        existing['updated_at'] = repo.updated_at.isoformat()
                        existing['language'] = repo.language or 'N/A'
                        existing['topics'] = repo.get_topics()
                        existing['archived'] = repo.archived
                        existing['description'] = repo.description or existing.get('description', '')
                        # 重新分类（可能分类规则变化）
                        existing['category'] = categorize_project(repo)
                        updated_projects.add(repo.full_name)
                        print(f"  ↻ 更新: {repo.full_name} ({repo.stargazers_count} ⭐)")
                        time.sleep(REQUEST_DELAY)
                        continue
                    
                    try:
                        repo.get_readme()
                    except:
                        continue
                    
                    if repo.stargazers_count < MIN_STARS:
                        continue
                    
                    project = {
                        'name': repo.name,
                        'full_name': repo.full_name,
                        'description': repo.description or '',
                        'url': repo.html_url,
                        'stars': repo.stargazers_count,
                        'language': repo.language or 'N/A',
                        'updated_at': repo.updated_at.isoformat(),
                        'created_at': repo.created_at.isoformat(),
                        'topics': repo.get_topics(),
                        'category': categorize_project(repo),
                        'owner': repo.owner.login,
                        'archived': repo.archived
                    }
                    
                    projects[repo.full_name] = project
                    count += 1
                    new_count += 1
                    print(f"  ✓ 新增: {repo.full_name} ({repo.stargazers_count} ⭐)")
                    
                    time.sleep(REQUEST_DELAY)
                    
                    if count >= MAX_PROJECTS_PER_QUERY:
                        break
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"搜索话题 '{topic}' 时出错: {str(e)}")
            continue
    
    # 过滤掉已归档的项目
    active_projects = [p for p in projects.values() if not p['archived']]
    
    # 按 stars 排序
    active_projects.sort(key=lambda x: x['stars'], reverse=True)
    
    print(f"\n📊 采集统计:")
    print(f"  - 新增项目: {new_count}")
    print(f"  - 更新项目: {len(updated_projects)}")
    if existing_projects:
        preserved_count = len(existing_projects) - len(updated_projects)
        print(f"  - 保留已有: {preserved_count}")
    print(f"  - 总计: {len(active_projects)} 个项目")
    
    return active_projects


def main():
    """主函数"""
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        raise ValueError('GITHUB_TOKEN environment variable is required')
    
    # 确保 data 目录存在
    data_dir = Path(__file__).parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    data_file = data_dir / 'projects.json'
    
    # 加载已有项目
    existing_projects = load_existing_projects(data_file)
    
    # 收集项目（保留已有项目，只添加新的）
    projects = collect_projects(github_token, existing_projects)
    
    # 保存到 JSON 文件
    output = {
        'last_updated': datetime.now().isoformat(),
        'total': len(projects),
        'projects': projects
    }
    
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已保存到 {data_file}")
    print(f"共保存 {len(projects)} 个项目")
    
    # 按分类统计
    categories_count = {}
    for project in projects:
        cat = project['category']
        categories_count[cat] = categories_count.get(cat, 0) + 1
    
    print("\n按分类统计:")
    for cat, count in sorted(categories_count.items()):
        print(f"  {CATEGORIES.get(cat, cat)}: {count}")


if __name__ == '__main__':
    main()

