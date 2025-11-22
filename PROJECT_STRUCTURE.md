# 项目结构说明

## 📁 完整目录结构

```
awesome-mcp/
├── .github/
│   └── workflows/
│       ├── update-projects.yml    # 自动采集和更新项目的工作流
│       └── deploy.yml              # 自动部署到 GitHub Pages 的工作流
│
├── scripts/                        # Python 自动化脚本
│   ├── collect_projects.py        # 从 GitHub 采集 MCP 项目
│   ├── generate_markdown.py       # 生成英文 Markdown 文件
│   ├── translate_content.py       # 翻译内容到其他语言
│   └── requirements.txt            # Python 依赖包
│
├── data/                           # 数据文件目录
│   ├── .gitkeep                   # 保持目录存在
│   └── projects.json              # 采集的项目数据（自动生成）
│
├── docs/                           # VitePress 网站源文件
│   ├── .vitepress/
│   │   └── config.js              # VitePress 配置文件
│   │
│   ├── index.md                   # 首页
│   │
│   ├── en/                        # 英文文档
│   │   └── projects.md           # 项目列表（英文）
│   │
│   ├── zh/                        # 中文文档
│   │   └── projects.md           # 项目列表（中文）
│   │
│   ├── ru/                        # 俄语文档
│   │   └── projects.md           # 项目列表（俄语）
│   │
│   ├── ja/                        # 日语文档
│   │   └── projects.md           # 项目列表（日语）
│   │
│   ├── fr/                        # 法语文档
│   │   └── projects.md           # 项目列表（法语）
│   │
│   └── es/                        # 西班牙语文档
│       └── projects.md           # 项目列表（西班牙语）
│
├── .gitignore                     # Git 忽略文件配置
├── CONTRIBUTING.md                # 贡献指南
├── LICENSE                        # Apache 2.0 许可证
├── package.json                   # Node.js 项目配置
├── PROJECT_STRUCTURE.md           # 本文件
├── README.md                      # 项目说明文档
└── SETUP.md                       # 设置指南
```

## 🔄 工作流程

### 1. 自动采集流程（update-projects.yml）

```
GitHub Actions 触发（每天 UTC 0 点）
    ↓
运行 collect_projects.py
    ↓
从 GitHub API 采集项目数据
    ↓
保存到 data/projects.json
    ↓
运行 generate_markdown.py
    ↓
生成 docs/en/projects.md
    ↓
运行 translate_content.py
    ↓
生成其他语言的 projects.md 文件
    ↓
提交更改到仓库
```

### 2. 部署流程（deploy.yml）

```
推送到 main 分支（docs/ 目录变更）
    ↓
GitHub Actions 触发构建
    ↓
安装 Node.js 依赖
    ↓
构建 VitePress 网站
    ↓
部署到 GitHub Pages
```

## 📊 数据格式

### projects.json 结构

```json
{
  "last_updated": "2024-01-01T00:00:00",
  "total": 100,
  "projects": [
    {
      "name": "项目名称",
      "full_name": "owner/repo",
      "description": "项目描述",
      "url": "https://github.com/owner/repo",
      "stars": 100,
      "language": "Python",
      "updated_at": "2024-01-01T00:00:00",
      "created_at": "2023-01-01T00:00:00",
      "topics": ["mcp", "model-context-protocol"],
      "category": "servers",
      "owner": "owner",
      "archived": false
    }
  ]
}
```

### 项目分类

- `servers`: MCP 服务器实现
- `clients`: MCP 客户端应用
- `tools`: 工具和库
- `examples`: 示例项目
- `documentation`: 文档和教程

## 🛠️ 核心脚本说明

### collect_projects.py

**功能**: 从 GitHub 采集符合条件的 MCP 项目

**筛选条件**:
- ⭐ Stars ≥ 10
- 📝 必须有 README 文件
- 🔍 通过关键词、话题、标签搜索

**搜索方式**:
- 关键词: `MCP`, `Model Context Protocol`, `mcp-server`, `mcp-client`
- 话题: `mcp`, `model-context-protocol`, `mcp-server`, `mcp-client`

### generate_markdown.py

**功能**: 从 JSON 数据生成英文 Markdown 文件

**输出**: `docs/en/projects.md`

**内容**:
- 项目总数和最后更新时间
- 按分类组织的项目列表
- 每个项目的详细信息（stars, 语言, 更新时间, 标签）

### translate_content.py

**功能**: 将英文内容翻译到其他语言

**支持语言**:
- 中文 (zh)
- 俄语 (ru)
- 日语 (ja)
- 法语 (fr)
- 西班牙语 (es)

**翻译服务**: 使用 `googletrans` 库（免费但可能不稳定）

## 🌐 网站结构

### VitePress 配置

- **主题**: VitePress 默认主题
- **搜索**: 本地搜索功能
- **多语言**: 通过目录结构实现
- **部署**: GitHub Pages

### 页面路由

- `/` - 首页
- `/en/projects` - 英文项目列表
- `/zh/projects` - 中文项目列表
- `/ru/projects` - 俄语项目列表
- `/ja/projects` - 日语项目列表
- `/fr/projects` - 法语项目列表
- `/es/projects` - 西班牙语项目列表

## 📝 维护说明

### 手动更新

```bash
# 1. 采集项目
python scripts/collect_projects.py

# 2. 生成 Markdown
python scripts/generate_markdown.py

# 3. 翻译（可选）
python scripts/translate_content.py
```

### 自动更新

项目通过 GitHub Actions 每天自动更新，无需手动操作。

### 自定义配置

- **搜索关键词**: 修改 `scripts/collect_projects.py` 中的 `SEARCH_QUERIES`
- **分类规则**: 修改 `scripts/collect_projects.py` 中的 `categorize_project()` 函数
- **网站样式**: 修改 `docs/.vitepress/config.js`
- **更新频率**: 修改 `.github/workflows/update-projects.yml` 中的 cron 表达式

## 🔗 相关资源

- [Model Context Protocol 官网](https://modelcontextprotocol.io/)
- [VitePress 文档](https://vitepress.dev/)
- [GitHub API 文档](https://docs.github.com/en/rest)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

