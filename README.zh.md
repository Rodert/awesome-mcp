# Awesome MCP

> 来自 GitHub 的精选 Model Context Protocol (MCP) 项目列表

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

本仓库自动收集并整理来自 GitHub 的高质量 MCP 项目，以美观、可搜索的格式呈现。列表通过 GitHub Actions 每日更新，并托管在 GitHub Pages 上。

## 🌐 语言

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 快速开始：如何在 AI 工具中使用 MCP

Model Context Protocol (MCP) 允许 AI 助手连接到外部数据源和工具。以下是在主流 AI 工具中设置 MCP 的方法：

### 📱 Claude Desktop

1. **找到配置文件：**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **编辑配置文件**并添加 MCP 服务器：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  }
}
```

3. **重启 Claude Desktop** 以应用更改。

### 💻 Cursor IDE

1. **打开设置**：`Cmd/Ctrl + ,`
2. **导航到**：Features → Agent → MCP Servers
3. **点击 "Add Server"**
4. **输入服务器详情**：
   - **名称**：服务器的友好名称
   - **命令**：要运行的命令（例如 `npx`）
   - **参数**：命令参数（例如 `["-y", "@modelcontextprotocol/server-github"]`）
   - **环境变量**：环境变量（如需要）

### 🔌 Continue (VS Code 扩展)

1. **安装 Continue 扩展**：从 VS Code 市场安装
2. **打开 Continue 设置**：点击侧边栏中的 Continue 图标
3. **导航到**：Settings → MCP Servers
4. **在 `~/.continue/config.json` 中添加 MCP 服务器**：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

5. **重新加载 VS Code** 以应用更改。

### 🔌 Cline (VS Code 扩展)

1. **安装 Cline 扩展**：从 VS Code 市场安装
2. **打开命令面板**：`Cmd/Ctrl + Shift + P`
3. **运行**：`Cline: Configure MCP Servers`
4. **编辑打开的配置文件**，或手动编辑 `~/.cline/mcp_config.json`：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

5. **重启 VS Code** 以应用更改。

### ⚡ Aider (命令行工具)

1. **安装 Aider**：`pip install aider-chat`
2. **设置环境变量**用于 MCP 服务器：

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **或创建** `~/.aider/mcp_config.json`：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

4. **运行 Aider**：`aider`（MCP 服务器将自动加载）

### 🌊 Windsurf

1. **打开 Windsurf 设置**：`Cmd/Ctrl + ,`
2. **导航到**：Extensions → MCP
3. **点击 "Add MCP Server"**
4. **配置服务器**：
   - **名称**：服务器标识符
   - **命令**：要执行的命令
   - **参数**：命令参数
   - **环境变量**：环境变量
5. **保存并重启** Windsurf

### 🎨 Composer (Anthropic)

1. **打开 Composer 设置**
2. **导航到**：Settings → Integrations → MCP
3. **添加 MCP 服务器配置**：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

4. **重启 Composer** 以应用更改。

### 🔍 查找 MCP 服务器

浏览下面的[项目列表](#-项目共-890-个)以发现可用的 MCP 服务器。热门选项包括：

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - 访问 GitHub 仓库和问题
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - 浏览器自动化
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - 文件系统访问
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - 数据库查询

### 📝 示例：GitHub MCP Server

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**获取 GitHub token**：[GitHub 设置 → 开发者设置 → 个人访问令牌](https://github.com/settings/tokens)

### 🎯 MCP 能做什么？

配置完成后，MCP 使 AI 助手能够：
- 📂 访问文件和目录
- 🔍 搜索代码仓库
- 🌐 浏览网页
- 💾 查询数据库
- 📊 分析数据
- 🔧 执行工具和脚本

### 📚 了解更多

- [官方 MCP 文档](https://modelcontextprotocol.io/)
- [MCP 规范](https://github.com/modelcontextprotocol/specification)
- 浏览 [MCP 服务器集合](https://github.com/modelcontextprotocol/servers)

---

## 📚 项目（共 9 个）

> 最后更新：**2025-11-22**

### MCP 服务器

*提供协议服务的 MCP 服务器实现*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 119,501
   生产就绪的智能体工作流开发平台。

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 115,900
   用户友好的 AI 界面（支持 Ollama、OpenAI API 等）

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,770
   通往 AI 驱动的全栈可观测性的最快路径，即使是精简团队也能使用。

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 75,146
   MCP 服务器集合。

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 73,079
   Model Context Protocol 服务器

[查看全部 8 个 →](https://rodert.github.io/awesome-mcp/zh/projects)

### MCP 客户端

*连接到 MCP 服务器的 MCP 客户端应用程序*

*即将推出...*

### 工具和库

*用于处理 MCP 的开发工具和库*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 157,879
   具有原生 AI 功能的公平代码工作流自动化平台。将可视化构建与自定义代码相结合，可自托管或云端部署，支持 400+ 集成。

### 示例

*演示 MCP 用法的示例项目*

*即将推出...*

### 文档

*文档、教程和学习资源*

*即将推出...*

---

**[在 GitHub Pages 查看完整项目列表 →](https://rodert.github.io/awesome-mcp/)**

## 📋 项目标准

- ⭐ 至少 10 个星标
- 📝 必须有 README 文件
- 🔍 通过 MCP 相关的关键词、话题和标签发现

## 🤖 自动化

本仓库使用自动化脚本，实现：

1. **收集** - 通过 GitHub Search API 每日收集项目
2. **分类** - 按用例对项目进行分类（服务器、客户端、工具、示例、文档）
3. **翻译** - 使用 AI 翻译将内容翻译成多种语言
4. **更新** - 自动更新网站

## 🏗️ 结构

```
awesome-mcp/
├── .github/workflows/    # GitHub Actions 自动化
├── scripts/              # Python 收集和翻译脚本
├── data/                 # JSON 数据文件
└── docs/                 # VitePress 网站源文件
```

## 📝 许可证

根据 Apache License 2.0 许可 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 👥 维护者

本项目由以下 AI 编程助手维护：

- **Cursor** - AI 驱动的代码编辑器
- **Claude Code** - Anthropic 的 AI 编程助手
- **DeepSeek** - DeepSeek AI 编程助手
- **Gemini** - Google 的 AI 编程助手

这些 AI 助手协作维护项目，收集新的 MCP 项目，并保持精选列表的质量。

## 🙏 贡献

欢迎贡献！请随时提交 Pull Request。

