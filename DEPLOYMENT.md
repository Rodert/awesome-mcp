# GitHub Pages 部署说明

## ✅ 部署状态

GitHub Pages 已完全配置完成，包含以下功能：

### 1. 可搜索的 Web UI
- ✅ Vue 组件实现的交互式搜索界面
- ✅ 实时搜索项目名称、描述、标签
- ✅ 多维度筛选（分类、语言、标签）
- ✅ 灵活排序（按星标、更新时间、名称）
- ✅ 响应式设计，支持移动端

### 2. 多语言支持
- ✅ 6 种语言界面（English, 中文, Русский, 日本語, Français, Español）
- ✅ 项目列表保留原始语言（不翻译）
- ✅ README 文件多语言版本

### 3. 自动化工作流

#### update-projects.yml
- ✅ 每天 UTC 0 点自动运行
- ✅ 从 GitHub 采集 MCP 项目
- ✅ 保留已有项目，只添加新项目
- ✅ 更新已有项目的最新信息
- ✅ 生成搜索页面和数据文件
- ✅ 自动提交更新

#### deploy.yml
- ✅ 当 docs/ 目录有变更时自动触发
- ✅ 构建 VitePress 网站
- ✅ 部署到 GitHub Pages

## 📁 文件结构

```
docs/
├── .vitepress/
│   ├── components/
│   │   └── ProjectSearch.vue    # Vue 搜索组件
│   └── config.js                 # VitePress 配置
├── data/
│   └── projects.json             # 项目数据（自动生成）
├── en/projects.md                 # 英文搜索页面
├── zh/projects.md                 # 中文搜索页面
├── ru/projects.md                 # 俄语搜索页面
├── ja/projects.md                 # 日语搜索页面
├── fr/projects.md                 # 法语搜索页面
└── es/projects.md                 # 西班牙语搜索页面
```

## 🚀 部署流程

1. **自动更新项目**（每天 UTC 0 点）
   - 运行 `collect_projects.py` 采集项目
   - 运行 `generate_markdown.py` 生成页面和数据文件
   - 提交更改到仓库

2. **自动部署**（docs/ 目录变更时）
   - 构建 VitePress 网站
   - 部署到 GitHub Pages

## 🔧 配置要求

### GitHub Pages 设置
1. 进入仓库 Settings -> Pages
2. Source: 选择 "GitHub Actions"
3. 确保有 `pages: write` 权限

### 环境变量
- `GITHUB_TOKEN`: 自动提供（无需手动配置）
- `DEBUG_MODE`: 可选，通过仓库变量控制

## 📊 数据文件

- **位置**: `docs/data/projects.json`
- **生成**: 由 `generate_markdown.py` 自动复制
- **访问**: 前端通过 `/awesome-mcp/data/projects.json` 访问

## 🌐 访问地址

部署后的访问地址：
- 主页: `https://rodert.github.io/awesome-mcp/`
- 英文: `https://rodert.github.io/awesome-mcp/en/projects`
- 中文: `https://rodert.github.io/awesome-mcp/zh/projects`
- 俄语: `https://rodert.github.io/awesome-mcp/ru/projects`
- 日语: `https://rodert.github.io/awesome-mcp/ja/projects`
- 法语: `https://rodert.github.io/awesome-mcp/fr/projects`
- 西班牙语: `https://rodert.github.io/awesome-mcp/es/projects`

## ✨ 功能特性

- 🔍 **实时搜索**: 输入即时过滤项目
- 🏷️ **标签筛选**: 点击标签快速筛选
- 📊 **分类浏览**: 按 MCP Servers、Clients、Tools 等分类
- 🌍 **多语言**: 6 种语言界面
- 📱 **响应式**: 完美适配各种设备
- ⚡ **快速加载**: 优化的数据加载和渲染

## 🐛 故障排除

### 数据文件未加载
- 检查 `docs/data/projects.json` 是否存在
- 检查浏览器控制台的错误信息
- 确认数据文件路径是否正确

### 部署失败
- 检查 GitHub Actions 日志
- 确认 Node.js 版本（需要 18+）
- 确认 VitePress 依赖已安装

### 搜索不工作
- 检查浏览器控制台是否有 JavaScript 错误
- 确认 Vue 组件是否正确加载
- 检查数据文件格式是否正确

## 📝 更新说明

所有更新都是自动的：
- 项目采集：每天自动运行
- 网站部署：docs/ 目录变更时自动部署
- 无需手动操作

