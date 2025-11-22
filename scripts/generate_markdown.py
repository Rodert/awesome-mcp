#!/usr/bin/env python3
"""
生成英文版本的 Markdown 文件
"""
import json
from pathlib import Path
from datetime import datetime

# 场景分类名称
CATEGORY_NAMES = {
    'servers': 'MCP Servers',
    'clients': 'MCP Clients',
    'tools': 'Tools & Libraries',
    'examples': 'Examples',
    'documentation': 'Documentation'
}

# 分类描述
CATEGORY_DESCRIPTIONS = {
    'servers': 'MCP server implementations that provide protocol services',
    'clients': 'MCP client applications that connect to MCP servers',
    'tools': 'Development tools and libraries for working with MCP',
    'examples': 'Example projects demonstrating MCP usage',
    'documentation': 'Documentation, tutorials, and learning resources'
}


def format_date(date_str: str) -> str:
    """格式化日期字符串"""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except:
        return date_str[:10] if len(date_str) >= 10 else date_str


def generate_markdown(data_file: str, output_file: str, lang: str = 'en'):
    """从 JSON 数据生成 Markdown 文件"""
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    projects = data['projects']
    last_updated = format_date(data['last_updated'])
    
    # 按分类分组
    categories = {}
    for project in projects:
        cat = project['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(project)
    
    # 生成 Markdown 头部
    markdown = f"""# Awesome MCP Projects

> 🚀 Last updated: **{last_updated}** | 📦 Total projects: **{data['total']}**

A curated list of awesome [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) projects collected from GitHub.

## 📋 Table of Contents

"""
    
    # 生成目录
    for cat in sorted(categories.keys()):
        cat_name = CATEGORY_NAMES.get(cat, cat.title())
        anchor = cat.replace('_', '-')
        markdown += f"- [{cat_name}](#{anchor})\n"
    
    markdown += "\n---\n\n"
    
    # 每个分类的内容
    for cat in sorted(categories.keys()):
        cat_name = CATEGORY_NAMES.get(cat, cat.title())
        cat_desc = CATEGORY_DESCRIPTIONS.get(cat, '')
        
        markdown += f"## {cat_name}\n\n"
        
        if cat_desc:
            markdown += f"*{cat_desc}*\n\n"
        
        # 按 stars 排序
        projects_in_cat = sorted(
            categories[cat],
            key=lambda x: x['stars'],
            reverse=True
        )
        
        for idx, project in enumerate(projects_in_cat, 1):
            # 项目标题
            markdown += f"### {idx}. [{project['name']}]({project['url']})\n\n"
            
            # 项目元信息
            stars = project['stars']
            language = project['language']
            updated = format_date(project['updated_at'])
            
            markdown += f"⭐ **{stars:,}** | 🔤 **{language}** | 📅 **{updated}**\n\n"
            
            # 项目描述
            if project['description']:
                desc = project['description'].strip()
                # 移除可能存在的 Markdown 链接，避免嵌套
                if desc and not desc.startswith('['):
                    markdown += f"{desc}\n\n"
            
            # Topics/Tags
            if project.get('topics'):
                topics = project['topics'][:8]  # 限制最多显示 8 个
                if topics:
                    topics_str = ' '.join([f"`{t}`" for t in topics if t])
                    if topics_str:
                        markdown += f"**Tags:** {topics_str}\n\n"
            
            # 分隔线（最后一个项目不需要）
            if idx < len(projects_in_cat):
                markdown += "---\n\n"
            else:
                markdown += "\n"
        
        # 分类之间的分隔
        if cat != sorted(categories.keys())[-1]:
            markdown += "\n---\n\n"
    
    # Footer
    markdown += """
---

## 🤝 Contributing

Found a great MCP project that's missing? Feel free to open an issue or submit a PR!

## 📄 License

This list is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/Rodert/awesome-mcp/blob/main/LICENSE) file for details.
"""
    
    # 保存文件
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"✓ Generated {output_file}")
    print(f"  Total projects: {len(projects)}")
    print(f"  Categories: {len(categories)}")
    
    # 返回统计信息
    category_counts = {cat: len(projs) for cat, projs in categories.items()}
    for cat, count in sorted(category_counts.items()):
        print(f"    - {CATEGORY_NAMES.get(cat, cat)}: {count}")


def generate_readme_projects(data_file: str, readme_file: str):
    """生成 README 中的项目列表部分"""
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    projects = data['projects']
    last_updated = format_date(data['last_updated'])
    
    # 按分类分组
    categories = {}
    for project in projects:
        cat = project.get('category', 'tools')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(project)
    
    # 生成项目列表内容
    projects_content = f"""## 📚 Projects ({data['total']} total)

> Last updated: **{last_updated}**

"""
    
    # 显示所有分类的项目（最多前 5 个）
    for cat_key in ['servers', 'clients', 'tools', 'examples', 'documentation']:
        cat_name = CATEGORY_NAMES.get(cat_key, cat_key.title())
        cat_desc = CATEGORY_DESCRIPTIONS.get(cat_key, '')
        
        projects_content += f"### {cat_name}\n\n"
        if cat_desc:
            projects_content += f"*{cat_desc}*\n\n"
        
        if cat_key in categories:
            projects_list = sorted(categories[cat_key], key=lambda x: x['stars'], reverse=True)[:5]
            for idx, project in enumerate(projects_list, 1):
                projects_content += f"{idx}. **[{project['name']}]({project['url']})** - ⭐ {project['stars']:,}\n"
                if project.get('description'):
                    projects_content += f"   {project['description']}\n"
                projects_content += "\n"
            
            if len(categories[cat_key]) > 5:
                projects_content += f"[View all {len(categories[cat_key])} →](https://rodert.github.io/awesome-mcp/en/projects)\n\n"
        else:
            projects_content += "*Coming soon...*\n\n"
    
    projects_content += """---

**[View complete project list on GitHub Pages →](https://rodert.github.io/awesome-mcp/)**

"""
    
    # 读取现有 README，替换项目部分
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # 查找并替换项目部分（从 "## 📚 Projects" 到下一个 "## " 或文件末尾）
    import re
    pattern = r'## 📚 Projects.*?(?=\n## |\Z)'
    
    if re.search(pattern, readme_content, re.DOTALL):
        # 替换现有的项目部分
        new_readme = re.sub(pattern, projects_content.rstrip() + '\n', readme_content, flags=re.DOTALL)
    else:
        # 在 "## 🌐 Languages" 之后插入项目部分
        pattern = r'(## 🌐 Languages.*?\n.*?\n)'
        new_readme = re.sub(pattern, r'\1\n' + projects_content, readme_content, flags=re.DOTALL)
    
    # 保存更新的 README
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print(f"✓ Updated {readme_file}")


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    data_file = project_root / 'data' / 'projects.json'
    output_file = project_root / 'docs' / 'en' / 'projects.md'
    readme_file = project_root / 'README.md'
    
    if not data_file.exists():
        print(f"Error: {data_file} not found. Please run collect_projects.py first.")
        return
    
    generate_markdown(str(data_file), str(output_file))
    generate_readme_projects(str(data_file), str(readme_file))


if __name__ == '__main__':
    main()

