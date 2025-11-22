# 项目设置指南

本指南将帮助您完成 Awesome MCP 项目的初始设置。

## 📋 前置要求

- Python 3.11+
- Node.js 18+
- npm 或 yarn
- GitHub 账号（用于 API 访问）

## 🚀 快速开始

### 1. 安装依赖

```bash
# 安装 Python 依赖
cd scripts
pip install -r requirements.txt
cd ..

# 安装 Node.js 依赖
npm install
```

### 2. 配置 GitHub Token

为了使用 GitHub API 采集项目，您需要配置 GitHub Token：

#### 创建 Personal Access Token

1. 访问 GitHub Settings: https://github.com/settings/tokens
2. 点击 "Generate new token" -> "Generate new token (classic)"
3. 设置权限：
   - ✅ `public_repo` - 访问公开仓库信息
   - ✅ `repo` - 如果需要访问私有仓库（通常不需要）
4. 生成 Token 并复制

#### 配置 Token

**方式 1: 环境变量（推荐用于本地开发）**

```bash
export GITHUB_TOKEN=your_token_here
```

**方式 2: GitHub Actions Secrets（用于自动化）**

1. 访问仓库设置: `Settings` -> `Secrets and variables` -> `Actions`
2. 点击 "New repository secret"
3. 名称: `GITHUB_TOKEN`
4. 值: 粘贴您的 Token
5. 点击 "Add secret"

> **注意**: GitHub Actions 会自动提供 `GITHUB_TOKEN`，但如果您需要使用更高的速率限制，可以添加自定义 Token。

### 3. 首次运行

```bash
# 1. 采集项目
python scripts/collect_projects.py

# 2. 生成英文 Markdown
python scripts/generate_markdown.py

# 3. 翻译到其他语言（可选，需要较长时间）
python scripts/translate_content.py
```

### 4. 本地预览

```bash
# 启动开发服务器
npm run dev

# 在浏览器中打开 http://localhost:5173
```

### 5. 构建和部署

```bash
# 构建静态网站
npm run build

# 预览构建结果
npm run preview
```

## 🔧 GitHub Pages 设置

### 方式 1: 使用 GitHub Actions（推荐）

1. 仓库设置 -> `Settings` -> `Pages`
2. Source: 选择 "GitHub Actions"
3. 每次推送代码时，`deploy.yml` 工作流会自动构建并部署

### 方式 2: 手动部署

1. 构建网站: `npm run build`
2. 将 `docs/.vitepress/dist` 目录推送到 `gh-pages` 分支

## 🤖 自动化配置

### GitHub Actions 工作流

项目包含两个主要工作流：

1. **update-projects.yml**
   - 每天 UTC 0 点自动运行
   - 采集 GitHub 项目
   - 生成和翻译 Markdown 文件
   - 自动提交更新

2. **deploy.yml**
   - 当 `docs/` 目录有变更时触发
   - 构建 VitePress 网站
   - 部署到 GitHub Pages

### 手动触发

您可以在 GitHub Actions 页面手动触发工作流：

1. 访问仓库的 `Actions` 标签
2. 选择工作流
3. 点击 "Run workflow"

## 📝 文件结构说明

```
awesome-mcp/
├── .github/
│   └── workflows/          # GitHub Actions 工作流
│       ├── update-projects.yml  # 自动采集和更新
│       └── deploy.yml           # 自动部署
├── scripts/                # Python 脚本
│   ├── collect_projects.py      # 采集 GitHub 项目
│   ├── generate_markdown.py     # 生成 Markdown
│   ├── translate_content.py     # 翻译内容
│   └── requirements.txt          # Python 依赖
├── data/                   # 数据文件
│   └── projects.json            # 采集的项目数据（JSON）
├── docs/                   # VitePress 网站源文件
│   ├── .vitepress/
│   │   └── config.js            # VitePress 配置
│   ├── en/                 # 英文文档
│   ├── zh/                 # 中文文档
│   ├── ru/                 # 俄语文档
│   ├── ja/                 # 日语文档
│   ├── fr/                 # 法语文档
│   └── es/                 # 西班牙语文档
├── package.json            # Node.js 依赖配置
└── README.md               # 项目说明
```

## ⚠️ 常见问题

### 1. GitHub API 速率限制

如果遇到速率限制错误：
- 使用 GitHub Personal Access Token（而不是默认的 GITHUB_TOKEN）
- 在脚本中添加更长的延迟
- 减少每次采集的项目数量

### 2. 翻译 API 失败

翻译脚本使用 `googletrans` 库（非官方），可能不稳定：
- 可以添加重试机制（脚本已包含）
- 如果持续失败，考虑使用其他翻译服务
- 可以跳过翻译步骤，手动翻译

### 3. VitePress 构建失败

确保：
- Node.js 版本 ≥ 18
- 所有依赖已正确安装
- `docs/.vitepress/config.js` 配置正确

### 4. GitHub Pages 404

检查：
- `base` 路径是否正确设置（`/awesome-mcp/`）
- GitHub Pages 设置是否正确
- 构建是否成功

## 🔗 相关链接

- [VitePress 文档](https://vitepress.dev/)
- [GitHub API 文档](https://docs.github.com/en/rest)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 💡 下一步

1. 配置 GitHub Token
2. 运行首次采集
3. 检查生成的文件
4. 预览网站
5. 推送到 GitHub 并触发自动部署

祝您使用愉快！🎉

