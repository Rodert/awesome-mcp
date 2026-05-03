# Awesome MCP

> A curated list of awesome Model Context Protocol (MCP) projects from GitHub

[![Auto Update](https://github.com/Rodert/awesome-mcp/workflows/Update%20Projects/badge.svg)](https://github.com/Rodert/awesome-mcp/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Languages / 语言 / Языки / 言語 / Langues / Idiomas:**
- [English](README.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md)

This repository automatically collects and organizes high-quality MCP projects from GitHub, presenting them in a beautiful, searchable format. The list is updated daily via GitHub Actions and hosted on GitHub Pages.

## 🌐 Languages

- [English](https://rodert.github.io/awesome-mcp/en/projects)
- [中文](https://rodert.github.io/awesome-mcp/zh/projects)
- [Русский](https://rodert.github.io/awesome-mcp/ru/projects)
- [日本語](https://rodert.github.io/awesome-mcp/ja/projects)
- [Français](https://rodert.github.io/awesome-mcp/fr/projects)
- [Español](https://rodert.github.io/awesome-mcp/es/projects)

## 🚀 Quick Start: How to Use MCP in AI Tools

The Model Context Protocol (MCP) allows AI assistants to connect to external data sources and tools. Here's how to set it up in popular AI tools:

### 📱 Claude Desktop

1. **Find the configuration file:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Edit the configuration file** and add your MCP servers:

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

3. **Restart Claude Desktop** to apply changes.

### 💻 Cursor IDE

1. **Open Settings**: `Cmd/Ctrl + ,`
2. **Navigate to**: Features → Agent → MCP Servers
3. **Click "Add Server"**
4. **Enter server details**:
   - **Name**: A friendly name for the server
   - **Command**: The command to run (e.g., `npx`)
   - **Args**: Command arguments (e.g., `["-y", "@modelcontextprotocol/server-github"]`)
   - **Env**: Environment variables (if needed)

### 🔌 Continue (VS Code Extension)

1. **Install Continue extension** from VS Code marketplace
2. **Open Continue settings**: Click the Continue icon in the sidebar
3. **Navigate to**: Settings → MCP Servers
4. **Add MCP server** in `~/.continue/config.json`:

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

5. **Reload VS Code** to apply changes.

### 🔌 Cline (VS Code Extension)

1. **Install Cline extension** from VS Code marketplace
2. **Open Command Palette**: `Cmd/Ctrl + Shift + P`
3. **Run**: `Cline: Configure MCP Servers`
4. **Edit the configuration file** that opens, or manually edit `~/.cline/mcp_config.json`:

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

5. **Restart VS Code** to apply changes.

### ⚡ Aider (Command Line)

1. **Install Aider**: `pip install aider-chat`
2. **Set environment variable** for MCP servers:

```bash
export MCP_SERVERS='{"github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"}}}'
```

3. **Or create** `~/.aider/mcp_config.json`:

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

4. **Run Aider**: `aider` (MCP servers will be automatically loaded)

### 🌊 Windsurf

1. **Open Windsurf Settings**: `Cmd/Ctrl + ,`
2. **Navigate to**: Extensions → MCP
3. **Click "Add MCP Server"**
4. **Configure server**:
   - **Name**: Server identifier
   - **Command**: Command to execute
   - **Arguments**: Command arguments
   - **Environment**: Environment variables
5. **Save and restart** Windsurf

### 🎨 Composer (Anthropic)

1. **Open Composer settings**
2. **Navigate to**: Settings → Integrations → MCP
3. **Add MCP server configuration**:

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

4. **Restart Composer** to apply changes.

### 🔍 Finding MCP Servers

Browse the [projects list](#-projects-890-total) below to discover available MCP servers. Popular options include:

- **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - Access GitHub repositories and issues
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** - Browser automation
- **[Filesystem Server](https://github.com/modelcontextprotocol/servers)** - File system access
- **[SQLite Server](https://github.com/modelcontextprotocol/servers)** - Database queries

### 📝 Example: GitHub MCP Server

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

**Get a GitHub token**: [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 🎯 What Can MCP Do?

Once configured, MCP enables AI assistants to:
- 📂 Access files and directories
- 🔍 Search code repositories
- 🌐 Browse the web
- 💾 Query databases
- 📊 Analyze data
- 🔧 Execute tools and scripts

### 📚 Learn More

- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://github.com/modelcontextprotocol/specification)
- Browse [MCP Servers Collection](https://github.com/modelcontextprotocol/servers)

---

## 📚 Projects (4558 total)

> Last updated: **2026-05-03**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 172,177
   The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

2. **[dify](https://github.com/langgenius/dify)** - ⭐ 139,901
   Production-ready platform for agentic workflow development.

3. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 135,246
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

4. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 102,992
   An open-source AI agent that brings the power of Gemini directly into your terminal.

5. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 86,132
   A collection of MCP servers.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 84,932
   Model Context Protocol Servers

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 78,943
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[netdata](https://github.com/netdata/netdata)** - ⭐ 78,678
   The fastest path to AI-powered full stack observability, even for lean teams.

9. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 75,968
   The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

10. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

11. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 59,428
   The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

12. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 57,952
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

13. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 57,605
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

14. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 56,058
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

15. **[context7](https://github.com/upstash/context7)** - ⭐ 54,317
   Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

16. **[mempalace](https://github.com/MemPalace/mempalace)** - ⭐ 50,793
   The best-benchmarked open-source AI memory system. And it's free.

17. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 46,069
   AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

18. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 41,925
   🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

19. **[mempalace](https://github.com/milla-jovovich/mempalace)** - ⭐ 40,200
   The highest-scoring AI memory system ever benchmarked. And it's free.

20. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 37,960
   Chrome DevTools for coding agents

21. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

22. **[goose](https://github.com/block/goose)** - ⭐ 37,288
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

23. **[ruflo](https://github.com/ruvnet/ruflo)** - ⭐ 37,040
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

24. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 36,473
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

25. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 36,100
   Installable GitHub library of 1,400+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows, and official/community skill collections.

26. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 34,540
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

27. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 33,477
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

28. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

29. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,905
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

30. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 31,922
   Playwright MCP server

31. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 31,197
   AI Agent Assistant that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

32. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 29,594
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

33. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 29,459
   GitHub's official MCP Server

34. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 27,996
   Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

35. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 26,835
   An autonomous agent that conducts deep research on any data using any LLM providers

36. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 26,117
   An MCP-based chatbot | 一个基于MCP的聊天机器人

37. **[fastmcp](https://github.com/PrefectHQ/fastmcp)** - ⭐ 24,963
   🚀 The fast, Pythonic way to build MCP servers and clients.

38. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,630
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

39. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 24,547
   Build and run agents you can see, understand and trust.

40. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 24,253
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

41. **[serena](https://github.com/oraios/serena)** - ⭐ 23,748
   A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent

42. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 23,493
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

43. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,902
   🚀 The fast, Pythonic way to build MCP servers and clients

44. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 22,859
   The official Python SDK for Model Context Protocol servers and clients

45. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 22,017
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

46. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 21,140

47. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 20,871
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

48. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 19,171
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

49. **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** - ⭐ 18,648
   Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

50. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 18,423
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

51. **[page-agent](https://github.com/alibaba/page-agent)** - ⭐ 17,518
   JavaScript in-page GUI agent. Control web interfaces with natural language.

52. **[nuclear](https://github.com/nukeop/nuclear)** - ⭐ 17,407
   Streaming music player that finds free music for you

53. **[openfang](https://github.com/RightNow-AI/openfang)** - ⭐ 17,122
   Open-source Agent Operating System

54. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 16,244
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

55. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 15,989
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

56. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 15,103
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

57. **[mcp-toolbox](https://github.com/googleapis/mcp-toolbox)** - ⭐ 14,913
   MCP Toolbox for Databases is an open source MCP server for databases.

58. **[code-review-graph](https://github.com/tirth8205/code-review-graph)** - ⭐ 14,901
   Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.

59. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 14,762
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

60. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 14,594
   MCP server to provide Figma layout information to AI coding agents like Cursor

61. **[electerm](https://github.com/electerm/electerm)** - ⭐ 14,024
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(linux, mac, win)

62. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 13,975
   MCP Toolbox for Databases is an open source MCP server for databases.

63. **[casdoor](https://github.com/casdoor/casdoor)** - ⭐ 13,536
   An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI supporting OpenClaw, MCP, OAuth, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD

64. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 13,516
   Memory for 24/7 proactive agents like OpenClaw.

65. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

66. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 13,245
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

67. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 13,196
   MCP for xiaohongshu.com

68. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 12,334
   The official TypeScript SDK for Model Context Protocol servers and clients

69. **[context-mode](https://github.com/mksglu/context-mode)** - ⭐ 12,062
   Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 14 platforms

70. **[kubeshark](https://github.com/kubeshark/kubeshark)** - ⭐ 11,888
   eBPF-powered network observability for Kubernetes. Indexes L4/L7 traffic with full K8s context, decrypts TLS without keys. Queryable by AI agents via MCP and humans via dashboard.

71. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,836
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

72. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 11,558
   A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

73. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,495
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

74. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 11,371
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

75. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 11,106
   Yet another WebUI for Nginx

76. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 11,028
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

77. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 10,597
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

78. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 10,322
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

79. **[superset](https://github.com/superset-sh/superset)** - ⭐ 10,248
   Code Editor for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

80. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

81. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 9,871
   The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

82. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 9,643
   Visual testing tool for MCP servers

83. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 9,431
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

84. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 9,132
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

85. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 8,934
   Official MCP Servers for AWS

86. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 8,728
   MCP Server for Ghidra

87. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,656
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

88. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 8,585
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

89. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 8,473
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

90. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,306
   Build effective agents using Model Context Protocol and simple workflow patterns

91. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 8,213
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

92. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 8,195
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, images, and structured information from PDFs, Office documents, images, and 97+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, R, C, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

93. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 8,155
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

94. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 8,010
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

95. **[webiny-js](https://github.com/webiny/webiny-js)** - ⭐ 7,971
   Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3). TypeScript framework with multi-tenancy, lifecycle hooks, GraphQL API, and AI-assisted development via MCP server. Built for developers at large organizations.

96. **[Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** - ⭐ 7,925
   ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.

97. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,838
   Build autonomous AI agents in Python.

98. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

99. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,209
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

100. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 6,981
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

101. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,762
   A community driven registry service for Model Context Protocol (MCP) servers.

102. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,723
   TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

103. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 6,443
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

104. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,406
   A collection of MCP clients.

105. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 6,202
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

106. **[ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** - ⭐ 6,180
   Learn it. Build it. Ship it for others.

107. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

108. **[open-multi-agent](https://github.com/JackChen-me/open-multi-agent)** - ⭐ 6,013
   From a goal to a task DAG, automatically. TypeScript-native multi-agent orchestration with MCP and live tracing. Three runtime dependencies.

109. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,984
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

110. **[Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** - ⭐ 5,945
   754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0

111. **[microsandbox](https://github.com/superradcompany/microsandbox)** - ⭐ 5,928
   🧱 secure, local and programmable sandboxes for AI agents

112. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,878
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

113. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,866
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

114. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,765
   A model-driven approach to building AI agents in just a few lines of code.

115. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,727
   Klavis AI:  MCP integration platforms that let AI agents use tools reliably at any scale

116. **[CodePilot](https://github.com/op7418/CodePilot)** - ⭐ 5,616
   A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your phone. Built with Electron + Next.js.

117. **[jscpd](https://github.com/kucherenko/jscpd)** - ⭐ 5,589
   Copy/paste detector for programming source code. 

118. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,570
   WhatsApp MCP server

119. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,532
   [GitHub Trending #2] A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

120. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,511
   Awesome MCP Servers - A curated list of Model Context Protocol servers

121. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,488
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

122. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 5,448
   MCP Server for Computer Use in Windows

123. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 5,435
   Learn AI and LLMs from scratch using free resources

124. **[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)** - ⭐ 5,393
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

125. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,192
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

126. **[osaurus](https://github.com/osaurus-ai/osaurus)** - ⭐ 5,179
   Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source.

127. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 5,174
   opensource secure local-first sandboxes for ai agents

128. **[stitch-skills](https://github.com/google-labs-code/stitch-skills)** - ⭐ 5,143
   A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor.

129. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 5,089
   MCP server for Atlassian tools (Confluence, Jira)

130. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 4,999
   Install, run and deploy your own decentralized AI agent service

131. **[unidbg](https://github.com/zhkl0228/unidbg)** - ⭐ 4,943
   Allows you to emulate an Android native library, and an experimental  iOS emulation

132. **[bb-browser](https://github.com/epiral/bb-browser)** - ⭐ 4,936
   Your browser is the API. CLI + MCP server for AI agents to control Chrome with your login state.

133. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,825
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

134. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,785
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

135. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 4,780
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

136. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,760
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

137. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,719
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

138. **[byterover-cli](https://github.com/campfirein/byterover-cli)** - ⭐ 4,687
   ByteRover CLI (brv) - The portable memory layer for  autonomous coding agents (formerly Cipher)

139. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,575
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

140. **[Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)** - ⭐ 4,564
   "Vibe-Trading: Your Personal Trading Agent"

141. **[mission-control](https://github.com/builderz-labs/mission-control)** - ⭐ 4,553
   Self-hosted AI agent orchestration platform: dispatch tasks, run multi-agent workflows, monitor spend, and govern operations from one mission control dashboard.

142. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 4,537
   Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

143. **[openagent](https://github.com/the-open-agent/openagent)** - ⭐ 4,527
   ⚡️next-generation personal AI assistant powered by LLM, RAG and agent loops, supporting computer-use, browser-use and coding agent, demo: https://demo.openagentai.org

144. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,507
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

145. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 4,504
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

146. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,503
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

147. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 4,490
   Tutorials, Guides and Agent Skills Directories

148. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 4,466
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

149. **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** - ⭐ 4,396
   Universal SEO skill for Claude Code. 19 sub-skills, 12 subagents, 3 extensions (DataForSEO, Firecrawl, Banana). Technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, Google APIs, and PDF/Excel reporting.

150. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 4,371
   Exa MCP for web search and web crawling!

151. **[EverOS](https://github.com/EverMind-AI/EverOS)** - ⭐ 4,348
   Build, evaluate, and integrate long-term memory for self-evolving agents.

152. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 4,287
   Official Notion MCP Server

153. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 4,283
   RikkaHub is an Android APP that supports for multiple LLM providers.

154. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,273
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

155. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 4,257
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

156. **[excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)** - ⭐ 4,256
   Fast and streamable Excalidraw MCP App

157. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 4,232
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

158. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 4,226
   An Agentic Framework for Reflective PowerPoint Generation

159. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 4,171
   A simple, secure MCP-to-OpenAPI proxy server

160. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 4,156
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

161. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

162. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 4,138

163. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 4,110
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

164. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 4,073
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks go from beginner to power user!

165. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 4,032
   A curated list of Model Context Protocol (MCP) servers

166. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 4,027
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

167. **[mcp](https://github.com/google/mcp)** - ⭐ 4,009
   Google 💚 MCP

168. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 4,008
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 130+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

169. **[directories](https://github.com/leerob/directories)** - ⭐ 3,927
   Find rules and MCP servers

170. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

171. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,879
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use. 

172. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,865
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

173. **[oh-my-pi](https://github.com/can1357/oh-my-pi)** - ⭐ 3,840
   ⌥  AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

174. **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** - ⭐ 3,838
   Never stop coding. The free AI gateway — one endpoint, 160+ providers, zero downtime. Smart 4-tier auto-fallback (Subscription → API → Cheap → Free), prompt compression (save 15-75% tokens), 3-level proxy for geo-blocks, MCP Server (29 tools), A2A Protocol, 10 multi-modal APIs, and Desktop/Android/PWA apps.

175. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 3,795
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

176. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,784
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

177. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,781
   A Model Context Protocol server for Excel file manipulation

178. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,778
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

179. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,764
   Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP Support

180. **[atmosphere](https://github.com/Atmosphere/atmosphere)** - ⭐ 3,757
   Real-time transport layer for Java AI agents. Build once with @Agent — deliver over WebSocket, SSE, gRPC, and WebTransport/HTTP3. Talk MCP, A2A and AG-UI. 

181. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,755
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

182. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,710
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

183. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,682

184. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,650
   An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins.

185. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,637
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

186. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 3,629
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

187. **[core](https://github.com/opensumi/core)** - ⭐ 3,628
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

188. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,624
   Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator

189. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 3,612
   A full-stack AI Red Teaming platform securing AI ecosystems via OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation.

190. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 3,558
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

191. **[claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** - ⭐ 3,550
   Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI across ideation, coding, experiments, writing, and publication.

192. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,548
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

193. **[EverMemOS](https://github.com/EverMind-AI/EverMemOS)** - ⭐ 3,546
   A memory OS that makes your OpenClaw agents more personal while saving tokens.

194. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,511
   LangChain 🔌 MCP

195. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,477
   Model Context Protocol(MCP) 编程极速入门

196. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 3,459
   Chrome extension to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

197. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

198. **[boost](https://github.com/laravel/boost)** - ⭐ 3,444
   Laravel-focused MCP server for augmenting your AI powered local development experience.

199. **[swarmpit](https://github.com/swarmpit/swarmpit)** - ⭐ 3,431
   Lightweight AI-friendly Docker Swarm management

200. **[drawio-mcp](https://github.com/jgraph/drawio-mcp)** - ⭐ 3,412

201. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 3,392
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

202. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,391
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

203. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 3,381
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

204. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 3,369
   The official Rust SDK for the Model Context Protocol

205. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,323
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

206. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,306
   Allow LLMs to control a browser with Browserbase and Stagehand

207. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,300
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

208. **[SimpleMem](https://github.com/aiming-lab/SimpleMem)** - ⭐ 3,267
   SimpleMem: Efficient Lifelong Memory for LLM Agents — Text & Multimodal

209. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,257
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

210. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 3,238
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

211. **[awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)** - ⭐ 3,216
   162 production-ready AI agent templates for OpenClaw. SOUL.md configs across 19 categories. Submit yours!

212. **[Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)** - ⭐ 3,162
   Multi-modal Generative Media Skills for AI Agents (Claude Code, Cursor, Gemini CLI). High-quality image, video, and audio generation powered by muapi.ai.

213. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 3,124
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

214. **[engram](https://github.com/Gentleman-Programming/engram)** - ⭐ 3,121
   Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

215. **[ouroboros](https://github.com/Q00/ouroboros)** - ⭐ 3,109
   Agent OS: Stop prompting. Start specifying.

216. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 3,089
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

217. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 3,087
   A TypeScript framework for building MCP servers.

218. **[vitemcp](https://github.com/punkpeye/vitemcp)** - ⭐ 3,056
   A TypeScript framework for building MCP servers.

219. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 3,036
   AI agent microservice

220. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 3,007
   n8n custom node for MCP

221. **[goclaw](https://github.com/nextlevelbuilder/goclaw)** - ⭐ 2,998
   GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. Deploy AI agent teams at scale without compromising on safety.

222. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,969
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

223. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,952
   MCP server for Grafana

224. **[jcode](https://github.com/1jehuang/jcode)** - ⭐ 2,922
   Coding Agent Harness

225. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 2,904
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

226. **[harbor](https://github.com/av/harbor)** - ⭐ 2,898
   One command brings a complete pre-wired LLM stack with hundreds of services to explore.

227. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 2,865
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

228. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,860
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

229. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 2,816
   This is the official website for TuriX Computer-use-Agent

230. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,758
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

231. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,680
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

232. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 2,674
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

233. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,670
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

234. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,662
   Connect Supabase to your AI assistants

235. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 2,655
   The Unofficial and Awesome Home Assistant MCP Server

236. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,644
   A Model Context Protocol server for searching and analyzing arXiv papers

237. **[moltis](https://github.com/moltis-org/moltis)** - ⭐ 2,640
   A secure persistent personal agent server in Rust. One binary, sandboxed execution, multi-provider LLMs, voice, memory, Telegram, WhatsApp, Discord, Teams, and MCP tools. Secure by design, runs on your hardware.

238. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,624
   A Model Context Protocol server for converting almost anything to Markdown

239. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,603
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

240. **[OB1](https://github.com/NateBJones-Projects/OB1)** - ⭐ 2,587
   Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS.

241. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,584
   A metasearch library that aggregates results from diverse web search services

242. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 2,580
   Next Generation Agentic Proxy for AI Agents and MCP servers

243. **[slackdump](https://github.com/rusq/slackdump)** - ⭐ 2,571
   Save or export your private and public Slack messages, threads, files, and users locally without admin privileges.

244. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

245. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,559
   A CLI tool for building Go applications.

246. **[tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** - ⭐ 2,548
   AI-assisted TradingView chart analysis — connect Claude Code to your TradingView Desktop for personal workflow automation

247. **[claude-context-mode](https://github.com/mksglu/claude-context-mode)** - ⭐ 2,522
   MCP is the protocol for tool access. We're the virtualization layer for context.

248. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 2,514
   AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free.

249. **[openpencil](https://github.com/ZSeven-W/openpencil)** - ⭐ 2,491
   The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

250. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,482
   A bridge between Streamable HTTP and stdio MCP transports

251. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,476

252. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,451
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

253. **[m_flow](https://github.com/FlowElement-ai/m_flow)** - ⭐ 2,442
   A bio-inspired cognitive memory engine — a new paradigm for Graph RAG.

254. **[FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline)** - ⭐ 2,413
   FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestration. It facilitates transparent, human-in-the-loop creation with reusable Style Skills for consistent, professional storytelling.

255. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,336
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

256. **[agent-scan](https://github.com/snyk/agent-scan)** - ⭐ 2,307
   Security scanner for AI agents, MCP servers and agent skills.

257. **[code-graph-rag](https://github.com/vitali87/code-graph-rag)** - ⭐ 2,286
   The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

258. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,280
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

259. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 2,271
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

260. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 2,271
   Real-time crypto & stock screening, advanced technical indicators, Bollinger Bands intelligence, candlestick patterns + native Claude Desktop integration. Multi-exchange (Binance, KuCoin, Bybit+). Open-source AI trading infrastructure.

261. **[agent-deck](https://github.com/asheshgoplani/agent-deck)** - ⭐ 2,265
   Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more.

262. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 2,257
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

263. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,212
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

264. **[skills](https://github.com/microsoft/skills)** - ⭐ 2,197
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

265. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,193
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

266. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 2,190
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

267. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 2,187
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

268. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 2,179
   ⭐ All-in-one AI companion! Super Agent Party = Self hosted neuro sama + openclaw! ⭐ 全能AI伴侣！超级智能体派对 = 自托管neuro sama + openclaw!

269. **[anything-analyzer](https://github.com/Mouseww/anything-analyzer)** - ⭐ 2,167
   全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

270. **[fli](https://github.com/punitarani/fli)** - ⭐ 2,154
   Google Flights MCP and Python Library

271. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 2,149
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

272. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 2,147
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

273. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 2,128
   The official MCP server implementation for the Perplexity API Platform

274. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,102
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

275. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 2,099
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

276. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

277. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,091
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

278. **[fusio](https://github.com/apioo/fusio)** - ⭐ 2,086
   Self-Hosted API Management for Builders

279. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 2,082
   425 plugins, 2,810 skills, 200 agents for Claude Code. Open-source marketplace at tonsofskills.com with the ccpi CLI package manager.

280. **[carbon](https://github.com/crbnos/carbon)** - ⭐ 2,081
   Carbon is an open source ERP, MES and QMS for manufacturing. Perfect for complex assembly, contract manufacturing, and configure to order manufacturing.

281. **[mcp2cli](https://github.com/knowsuchagency/mcp2cli)** - ⭐ 2,076
   Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen

282. **[onecli](https://github.com/onecli/onecli)** - ⭐ 2,076
   Open-source credential vault, give your AI agents access to services without exposing keys.

283. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,062
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

284. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 2,059
   An MCP server for interacting with the Financial Datasets stock market API.

285. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 2,047
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

286. **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** - ⭐ 2,017
   High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 66 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.

287. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 2,007
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

288. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 2,003
   directory for Awesome MCP Servers

289. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,989
   A Unified MCP Server Management App (MCP Manager).

290. **[beelzebub](https://github.com/beelzebub-labs/beelzebub)** - ⭐ 1,978
   A secure low code deception runtime framework, leveraging AI for System Virtualization.

291. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,977
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

292. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,975

293. **[claude-peers-mcp](https://github.com/louislva/claude-peers-mcp)** - ⭐ 1,968
   Allow all your Claude Codes to message each other ad-hoc!

294. **[witsy](https://github.com/Kochava-Studios/witsy)** - ⭐ 1,957
   Witsy: desktop AI assistant / universal MCP client

295. **[mcp-cli](https://github.com/IBM/mcp-cli)** - ⭐ 1,955

296. **[vexa](https://github.com/Vexa-ai/vexa)** - ⭐ 1,954
   Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.

297. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,941
   MCP server for interacting with the iOS simulator

298. **[rocketride-server](https://github.com/rocketride-org/rocketride-server)** - ⭐ 1,939
   High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM workflows with 13+ model providers, 8+ vector databases, and agent orchestration, all from your IDE. Includes VS Code extension, TypeScript/Python SDKs, and Docker deployment.

299. **[design-extract](https://github.com/Manavarya09/design-extract)** - ⭐ 1,932
   Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

300. **[esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** - ⭐ 1,931
   An AI-enabled NAT Router/Firewall for the ESP32

301. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,928
   Witsy: desktop AI assistant / universal MCP client

302. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,925
   Plugin for JADX to integrate MCP server

303. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,911
   Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite

304. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,907
   Development platform to debug, chat, inspect, and evaluate MCP servers, MCP apps, and ChatGPT apps.

305. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,904
   A secure low code honeypot framework, leveraging AI for System Virtualization.

306. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,901
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

307. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,891

308. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,891
   Desktop Extensions: One-click local MCP server installation in desktop apps

309. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,891
   Production ready MCP server with real-time search, extract, map & crawl.

310. **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** - ⭐ 1,866
   🦸 AI 编程超能力 · 中文增强版 — superpowers（116k+ ⭐）完整汉化 + 6 个中国原创 skills，让 Claude Code / Copilot CLI / Hermes Agent / Cursor / Windsurf / Kiro / Gemini CLI 等 16 款 AI 编程工具真正会干活

311. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 1,852
   MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

312. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,829
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

313. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

314. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,801
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

315. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,799
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

316. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,794
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

317. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,785
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

318. **[contextplus](https://github.com/forloopcodes/contextplus)** - ⭐ 1,781
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

319. **[contextplus](https://github.com/ForLoopCodes/contextplus)** - ⭐ 1,780
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

320. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,767
   Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

321. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,764
   ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP) servers.

322. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,762
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

323. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,759
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

324. **[SocratiCode](https://github.com/giancarloerra/SocratiCode)** - ⭐ 1,756
   Enterprise-grade (40m+ LOC) codebase intelligence, zero-setup, private & local Plugin/Skill or MCP: hybrid semantic search, polyglot dependency graphs, symbol-level impact analysis & call-flow, interactive HTML viewer, cross-project & branch-aware search, DB/API/infra knowledge. 61% less tokens, 84% fewer calls, 37x faster. Cloud in private beta.

325. **[plik](https://github.com/root-gg/plik)** - ⭐ 1,752
   Plik is a temporary file upload system (Wetransfer like) in Go.

326. **[dembrandt](https://github.com/dembrandt/dembrandt)** - ⭐ 1,752
   Extract any website’s design system into tokens in seconds: logo, colors, typography, borders & more. One command.

327. **[jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp)** - ⭐ 1,744
   The leading, most token-efficient MCP server for GitHub source code exploration via tree-sitter AST parsing

328. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 1,737
   Open-source MCP server for LinkedIn. Give Claude and any MCP-compatible AI assistant access to profiles, companies, jobs, and messages.

329. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 1,720
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

330. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,716
   Interactive User Feedback MCP

331. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,709
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

332. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,698
   🧡 The meta framework for code generation. Automate OpenAPI to type-safe TypeScript, Zod, and TanStack Query with a modular, plugin-based engine.

333. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,683
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

334. **[sentrux](https://github.com/sentrux/sentrux)** - ⭐ 1,682
   Real-time architectural sensor that helps AI agents close the feedback loop, enabling recursive self-improvement of code quality. Pure Rust.

335. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,676
   Make RSS 📰 great again with AI 🧠✨!! [gpt-5.5 -> https://token.glidea.app 0.2 倍率, 0.2元当1刀花，比官方便宜35倍]

336. **[pilot-shell](https://github.com/maxritter/pilot-shell)** - ⭐ 1,665
   Make Claude Code production-ready — spec-driven plans, enforced quality gates, persistent knowledge

337. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,658
   Semantic Search & Call Graphs for AI Agents (100% Local)

338. **[headroom](https://github.com/chopratejas/headroom)** - ⭐ 1,648
   The Context Optimization Layer for LLM Applications

339. **[korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)** - ⭐ 1,640
   국가법령정보MCP | 법제처 41개 API → 16개 MCP 도구. 법령·판례·조례·조약을 AI로 검색·조회·분석 + LLM 환각 방지 인용 검증 | 41 Korean legal APIs → 16 MCP tools with AI citation hallucination guard

340. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,640
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

341. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,639
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

342. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,615
   Coding assistant MCP for Claude Desktop

343. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 1,614
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

344. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,610
   MCP server that provides tools and resources for interacting with n8n API

345. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,606
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

346. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,600
   Official Microsoft Learn MCP Server and CLI tool – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

347. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,599
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

348. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,576
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

349. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

350. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,572
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

351. **[blitz-mac](https://github.com/blitzdotdev/blitz-mac)** - ⭐ 1,549
   Native macOS App Store Connect tool with MCP. Submit iOS apps to App Store with AI agents 

352. **[qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)** - ⭐ 1,530
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

353. **[mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil)** - ⭐ 1,524
   MCP Server para 70 APIs públicas brasileiras

354. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,523
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

355. **[Horizon](https://github.com/Thysrael/Horizon)** - ⭐ 1,522
   📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达

356. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 1,520
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+400,000 via SkillKit), 42 commands, 176+ plugins, 20 hooks, 15 rules, 7 templates, 14 MCP configs, 26 companion apps, 52 ecosystem entries, and more.

357. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,519
   An MCP server that installs other MCP servers for you

358. **[ai](https://github.com/stripe/ai)** - ⭐ 1,519
   One-stop shop for building AI-powered products and businesses with Stripe.

359. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,518
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

360. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,516
   Standards for building agents, better

361. **[cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)** - ⭐ 1,516
   A super light-weight embedded code search engine CLI (AST based) that just works - saves 70% token and improves speed for coding agent  🌟 Star if you like it!

362. **[claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust)** - ⭐ 1,515
   🚀 Rust 全量重构的 Claude Code - 性能提升 2.5x，体积减少 97% | High-performance Rust implementation of Claude Code with 2.5x faster startup and 97% smaller binary

363. **[NagaAgent](https://github.com/RTGS2017/NagaAgent)** - ⭐ 1,514
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

364. **[GrokSearch](https://github.com/GuDaStudio/GrokSearch)** - ⭐ 1,504
   Integrate Grok's powerful real-time search capabilities into Claude via the MCP protocol!

365. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,502
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

366. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,497
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

367. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

368. **[mcp-brasil](https://github.com/jxnxts/mcp-brasil)** - ⭐ 1,487
   MCP Server para 41 APIs públicas brasileiras

369. **[tavily-key-generator](https://github.com/skernelx/tavily-key-generator)** - ⭐ 1,480
   Multi-service toolkit for Tavily and Firecrawl signup automation, key validation, and isolated proxy pools.

370. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,473
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

371. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,469
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

372. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,458
   Security scanner for AI agents, MCP servers and agent skills.

373. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,458
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

374. **[hotpath-rs](https://github.com/pawurb/hotpath-rs)** - ⭐ 1,452
   Rust Performance Profiler & Channels Monitoring Toolkit (TUI, MCP)

375. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,449
   First gitlab mcp for you

376. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,438
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

377. **[ghost-os](https://github.com/ghostwright/ghost-os)** - ⭐ 1,433
   Full computer-use for AI agents. Self-learning workflows. Native macOS. No screenshots required.

378. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,432
   Make your own story. User-friendly software for LLM roleplaying

379. **[nixopus](https://github.com/nixopus/nixopus)** - ⭐ 1,428
   Run production apps without thinking about infrastructure. On your server or ours. Fully agentic.

380. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 1,418
   Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

381. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 1,418
   Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

382. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,402
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

383. **[phantom](https://github.com/ghostwright/phantom)** - ⭐ 1,401
   An AI co-worker with its own computer. Self-evolving, persistent memory, MCP server, secure credential collection, email identity. Built on the Claude Agent SDK.

384. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,401

385. **[jshookmcp](https://github.com/vmoranv/jshookmcp)** - ⭐ 1,394
   js hook toolkit that all you need

386. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 1,386
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

387. **[data-api-builder](https://github.com/Azure/data-api-builder)** - ⭐ 1,384
   Data API builder provides modern REST, GraphQL endpoints and MCP tools to your Azure Databases and on-prem stores.

388. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,383
   MCP Server for kubernetes management commands

389. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,382
   An official Qdrant Model Context Protocol (MCP) server implementation

390. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,377
   docker mcp CLI plugin / MCP Gateway

391. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,373
   A connector for Claude Desktop to read and search an Obsidian vault.

392. **[radar](https://github.com/skyhook-io/radar)** - ⭐ 1,372
   Modern Kubernetes visibility. Topology, event timeline, and service traffic — plus resource browsing and Helm management.

393. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,371
   告别AI提前终止烦恼，助力AI更加持久

394. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,369
   The official Swift SDK for Model Context Protocol servers and clients.

395. **[ShipSwift](https://github.com/signerlabs/ShipSwift)** - ⭐ 1,368
   AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

396. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,368
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

397. **[ai-engineering-interview-questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)** - ⭐ 1,367
   Your Cheat Sheet for AI Engineering Interview – Questions and Answers.

398. **[repowise](https://github.com/repowise-dev/repowise)** - ⭐ 1,357
   Codebase intelligence for AI-assisted engineering teams — auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.

399. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,353
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

400. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,349
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

401. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,338
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

402. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,338
   The official ElevenLabs MCP server

403. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 1,319
   A guide on how to use the Figma MCP server

404. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,315
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

405. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 1,306
   Build MCP Agents

406. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 1,303
   MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

407. **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** - ⭐ 1,301
   Humans and AI agents, building knowledge bases together. Self-hosted document annotation, version control, semantic search, and MCP.

408. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,299
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

409. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,296
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

410. **[sourcey](https://github.com/sourcey/sourcey)** - ⭐ 1,291
   Precision documentation from OpenAPI, MCP, Doxygen, and Markdown guides. Static HTML you own.

411. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,286
   Damn Vulnerable MCP Server

412. **[executor](https://github.com/RhysSullivan/executor)** - ⭐ 1,279
   The missing integration layer for AI agents. Let them call any OpenAPI / MCP / GraphQL / custom js functions in secure environment.

413. **[relaticle](https://github.com/relaticle/relaticle)** - ⭐ 1,278
   Open-source CRM with native AI agent support. 30 MCP tools, REST API, self-hosted. Built with Laravel & Filament

414. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 1,270
   Claude Code as one-shot MCP server to have an agent in your agent.

415. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,262
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

416. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 1,260
   Model Context Protocol for WinDBG

417. **[tabularis](https://github.com/TabularisDB/tabularis)** - ⭐ 1,258
   A lightweight, cross-platform database client for developers. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

418. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 1,255
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

419. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 1,251
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

420. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,248
   The TypeScript MCP framework

421. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,248
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

422. **[PrismerCloud](https://github.com/Prismer-AI/PrismerCloud)** - ⭐ 1,244
   Prismer Cloud

423. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,243
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

424. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 1,243
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

425. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,241
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

426. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,238
   An MCP server that autonomously evaluates web applications. 

427. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,234
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

428. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,232
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

429. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

430. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

431. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,216
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

432. **[antigravity-workspace-template](https://github.com/study8677/antigravity-workspace-template)** - ⭐ 1,204
   Workspace template + MCP server for Claude Code, Codex CLI, Cursor & Windsurf. Multi-agent knowledge engine (ag-refresh / ag-ask) that turns any codebase into a queryable AI assistant.

433. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,203
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

434. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,199
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

435. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 1,199
   Connect AI models like Claude & GPT with robots using MCP and ROS.

436. **[amical](https://github.com/amicalhq/amical)** - ⭐ 1,193
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

437. **[sceneview](https://github.com/sceneview/sceneview)** - ⭐ 1,190
   3D & AR SDK for Android (Jetpack Compose + Filament), iOS (SwiftUI + RealityKit), and Web. AI-first: llms.txt, MCP server, Copilot/Cursor rules. The only Compose-native 3D library.

438. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 1,188
   Draw.io Model Context Protocol (MCP) Server

439. **[mcpvault](https://github.com/bitbonsai/mcpvault)** - ⭐ 1,184
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

440. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 1,179
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

441. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,169
   A Ruby Implementation of the Model Context Protocol

442. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,169
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

443. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 1,165
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

444. **[minutes](https://github.com/silverstein/minutes)** - ⭐ 1,162
   Every meeting, every idea, every voice note — searchable by your AI. Open-source, privacy-first conversation memory layer.

445. **[aso-skills](https://github.com/Eronred/aso-skills)** - ⭐ 1,157
   AI agent skills for App Store Optimization (ASO) and app marketing. Built for indie developers, app marketers, and growth teams who want Cursor, Claude Code, or any Agent Skills-compatible AI assistant to help with keyword research, metadata optimization, competitor analysis, and app growth.

446. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,156
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

447. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 1,153
   A lightweight, cross-platform database client for developers. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

448. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

449. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,144
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

450. **[opennews-mcp](https://github.com/6551Team/opennews-mcp)** - ⭐ 1,142
   News Aggregation · AI Ratings · Trading Signals · Real-time Updates

451. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 1,141
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

452. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 1,141
   Natural (2-way) voice conversations with Claude Code

453. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 1,131
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

454. **[open-cowork](https://github.com/OpenCoworkAI/open-cowork)** - ⭐ 1,127
   Open-source AI agent desktop app for Windows & macOS. One-click install Claude Code, MCP tools, and Skills — with sandbox isolation, multi-model support, and Feishu/Slack integration.

455. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,124
   Game Boy / Game Boy Color / Super Game Boy emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

456. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 1,122
   Lighweight CLI to interact with MCP servers

457. **[agents](https://github.com/inkeep/agents)** - ⭐ 1,118
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

458. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 1,116
   Skybridge is a Full-Stack TypeScript framework for MCP Apps and ChatGPT Apps. Type-safe. React-powered. Platform-agnostic.

459. **[open-webSearch](https://github.com/Aas-ee/open-webSearch)** - ⭐ 1,115
   Multi-engine MCP server, CLI, and local daemon for agent web search and content retrieval — skill-guided workflows, no API keys.

460. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 1,112
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

461. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 1,107
   MCP integration for Google Calendar to manage events.

462. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 1,094
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

463. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,089
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

464. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,085
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

465. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 1,082
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

466. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 1,078
   A repository of servers and clients from the Model Context Protocol tutorials

467. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 1,077
   OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s. Works with Claude Code.

468. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 1,068
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

469. **[js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp)** - ⭐ 1,068
   为 AI Agent 设计的 JS 逆向 MCP Server，内置反检测，基于 chrome-devtools-mcp 重构 | JS reverse engineering MCP server with agent-first tool design and built-in anti-detection. Rebuilt from chrome-devtools-mcp.

470. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 1,067
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

471. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 1,058
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

472. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 1,056
   Bringing the power of MCP to the web

473. **[xiaoyaosearch](https://github.com/dtsola/xiaoyaosearch)** - ⭐ 1,056
   小遥搜索，听懂你的话、看懂你的图，用AI找到本地任何文件。让搜索像聊天一样简单。XiaoyaoSearch: Understands your words, reads your images, finds any local file with AI. Making search as easy as chatting.

474. **[724-office](https://github.com/wangziqi06/724-office)** - ⭐ 1,053
   7/24 Office — Self-evolving AI Agent system. 36 tools, 10,000 lines pure Python, modular architecture, MCP plugins, three-layer memory, nudge system, AI mirror, 24/7 production.

475. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,052
   MCP Python Tutorial 

476. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 1,052
   Remote MCP Servers

477. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,046
   On-premises conversational RAG with configurable containers

478. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 1,046
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

479. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 1,045
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

480. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,045
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

481. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,041
   A curated list of Model Context Protocol (MCP) servers 

482. **[keeper.sh](https://github.com/ridafkih/keeper.sh)** - ⭐ 1,041
   Calendar sync tool & universal calendar MCP server. Aggregate, sync and control calendars on Google, Outlook, Office 365, iCloud, CalDAV or ICS.

483. **[mirobody](https://github.com/thetahealth/mirobody)** - ⭐ 1,039
   Your Data, Your AI — Health, Finance & More. Open Source, Privacy-First.

484. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 1,037
   MCP server for fetch web page content using Playwright headless browser.

485. **[tools](https://github.com/strands-agents/tools)** - ⭐ 1,035
   A set of tools that gives agents powerful capabilities.

486. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,034
   Query and Summarize your chat messages.

487. **[codesight](https://github.com/Houseofmvps/codesight)** - ⭐ 1,027
   Universal AI context generator. Saves thousands of tokens per conversation in Claude Code, Cursor, Copilot, Codex, and more.

488. **[nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** - ⭐ 1,026
   A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents. Say goodbye to Vector RAG and amnesia. Empower your AI with persistent, graph-like structured memory across any model, session, or tool. Drop-in replacement for OpenClaw.

489. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

490. **[lean-ctx](https://github.com/yvgude/lean-ctx)** - ⭐ 1,024
   The context layer for AI coding agents  Reduce token waste in Cursor, Claude Code, Copilot, Windsurf, Codex, Gemini & more by 60–95% (up to 99% on cached reads) Shell Hook + MCP Server · 49 tools · 10 read modes · 90+ patterns · Single Rust binary 

491. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,021
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

492. **[LangAlpha](https://github.com/ginlix-ai/LangAlpha)** - ⭐ 1,015
   Claude Code for Finance

493. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 1,013
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

494. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 1,002
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

495. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 994
   Run all your MCP servers behind one endpoint

496. **[devops-ai-guidelines](https://github.com/VersusControl/devops-ai-guidelines)** - ⭐ 994
   First AI Journey for DevOps - with comprehensive learning paths, practical tips, and enterprise guidelines

497. **[muapi-cli](https://github.com/SamurAIGPT/muapi-cli)** - ⭐ 988
   Official CLI for muapi.ai — generate images, videos & audio from the terminal. MCP server, 14 AI models, npm + pip installable.

498. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 988
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

499. **[iwe](https://github.com/iwe-org/iwe)** - ⭐ 986
   Markdown memory system for you and your AI agent

500. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 985
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

501. **[webclaw](https://github.com/0xMassi/webclaw)** - ⭐ 983
   Fast, local-first web content extraction for LLMs. Scrape, crawl, extract structured data — all from Rust. CLI, REST API, and MCP server.

502. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 982
   Expose llms-txt to IDEs for development

503. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 980
   Skill and MCP server for searching and retrieving icons

504. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 979
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

505. **[weave](https://github.com/Ataraxy-Labs/weave)** - ⭐ 974
   Entity-level git merge driver. Resolves false conflicts git invents when independent agents edit the same file. ~95% reduction vs. line-based merge.

506. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 972
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

507. **[ai-setup](https://github.com/caliber-ai-org/ai-setup)** - ⭐ 972
   Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.

508. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 971
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

509. **[reactuse](https://github.com/childrentime/reactuse)** - ⭐ 971
   115+ production-ready React Hooks for sensors, UI, state & browser APIs. Tree-shakable, SSR-safe, TypeScript-first. Used by Shopee, PDD & Ctrip. Inspired by VueUse.

510. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 967
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

511. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 965

512. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 960
   A security scanner for your LLM agentic workflows

513. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 951
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

514. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 950
   MCP server integration for DaVinci Resolve

515. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 948
   Delegate tasks to Codex and Gemini directly from within Claude Code.

516. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 943
   OpenAPI Tool Servers

517. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 941
   Neo4j Labs Model Context Protocol servers

518. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 940
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

519. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 938
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

520. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 931
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

521. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 930
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

522. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 929

523. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 925
   A middleware to provide an openAI compatible endpoint that can call MCP tools

524. **[cs](https://github.com/boyter/cs)** - ⭐ 924
   codespelunker - CLI code search tool that understands code structure and ranks results by relevance. No indexing required with CLI, TUI, MCP and HTTP support.

525. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 921
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

526. **[MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)** - ⭐ 921
   Supports GPT Image 2, Nanobanana & ComfyUI, with a 1,400+ prompt library, carefully crafted hooks and a multi-task orchestration system

527. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 920
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

528. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 917
   The Typescript MCP Framework

529. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 910
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

530. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

531. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 908
   MCP server helping models to understand your Vite/Nuxt app better.

532. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 908
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

533. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 907
   Scan MCP servers for potential threats & security findings.

534. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 905
   A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations.

535. **[shellfirm](https://github.com/kaplanelad/shellfirm)** - ⭐ 903
   Safety guardrails for ai coding agents and human terminal commands

536. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 899
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

537. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 897

538. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 890

539. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 889
   Allow AI to wade through complex OpenAPIs using Simple Language

540. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 886
   A library for communication with a Minecraft client/server.

541. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 885

542. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 883
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility. Since 2018.

543. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 880
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

544. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 879
   A concise list for mcp servers

545. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 879
   FreeCAD MCP(Model Context Protocol) server

546. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 877
   Published in CNCF Landscape: A MCP server for Kubernetes.

547. **[kordoc](https://github.com/chrisryugj/kordoc)** - ⭐ 877
   모두 파싱해버리겠다 — HWP, HWPX, PDF, XLSX, DOCX → Markdown. CLI + MCP Server

548. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 877
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

549. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

550. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 876
   MCP Server For Turkish Legal Databases

551. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 875
   MCP Server Framework and Tool Development library for building custom capabilities into agents. 

552. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 875
   Search for the agentic web.

553. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 873
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

554. **[LetsFG](https://github.com/LetsFG/LetsFG)** - ⭐ 870
   Agent-native flight search & booking. Saved $116 across 5 routes vs Google Flights (verified). 400+ airlines in 5 seconds. Join the community - Star and spread the word

555. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 864
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

556. **[MODULAR-RAG-MCP-SERVER](https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER)** - ⭐ 853
   A modular RAG (Retrieval-Augmented Generation) system with MCP Server architecture. Using Skill to make AI follow each step of the spec and complete the code 100% by AI.

557. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 852
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

558. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 850
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

559. **[hister](https://github.com/asciimoo/hister)** - ⭐ 849
   Your own search engine

560. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 848
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

561. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 845
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

562. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 843
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

563. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 843
   原 [chatlog]项目（一个微信数据库解密读取及提供mcp服务、http服务的开源软件），现已支持通过微信clawbot接口推送消息，可以实时转发全部或指定消息到clawbot

564. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

565. **[server](https://github.com/php-mcp/server)** - ⭐ 835
   Core PHP implementation for the Model Context Protocol (MCP) server

566. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

567. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 834
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

568. **[routa](https://github.com/phodal/routa)** - ⭐ 833
   Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/   A2A support across web and desktop.

569. **[stitch-mcp](https://github.com/davideast/stitch-mcp)** - ⭐ 833
   A CLI for moving AI-generated UI designs from Google’s Stitch platform into your development workflow.

570. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 832
   Simple, modular, and observable Go framework for backend applications.

571. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 831
   A minimalistic MCP client with a good feature set.

572. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 829
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

573. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 828
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

574. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 826
   A simple, locally hosted Web Search MCP server for use with Local LLMs

575. **[nekro-agent](https://github.com/KroMiose/nekro-agent)** - ⭐ 825
   NekroAgent 是一个面向多人互动场景的跨平台 Agent 框架，集 Claude Code 沙盒执行、工作区编排、长期记忆、结构化 MCP 管理与可视化控制台于一体，兼具高扩展性、多模态交互、实时状态推送和自动化运行能力。项目支持 QQ、Discord、Telegram、Minecraft、BilibiliLive、WeChat、Email、SSE(SDK) 等多种平台接入，应用于构建高智能聊天机器人，可扩展为具备代码执行、工具调用、插件协作和复杂任务处理能力的通用 Agent 系统

576. **[claude_agent_teams_ui](https://github.com/777genius/claude_agent_teams_ui)** - ⭐ 824
   You're the CTO, agents are your team. They handle tasks on their own, message each other, and review each other's work. You just watch the kanban board and give high-level commands. Codex/Claude/OpenCode(75+ LLM providers). Build your AI company.

577. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 822
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

578. **[browser-use-mcp-server](https://github.com/kontext-security/browser-use-mcp-server)** - ⭐ 822
   Browse the web, directly from Cursor etc.

579. **[Foundry](https://github.com/promptise-com/Foundry)** - ⭐ 821
   The foundation layer for agentic intelligence.

580. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 821
   A local sandbox for your AI agents

581. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 819
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

582. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 818
   Browse the web, directly from Cursor etc.

583. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 814
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

584. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 813
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

585. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 812
   A self-hosted RSS reader and personal knowledge management tool.

586. **[gemini-skill](https://github.com/WJZ-P/gemini-skill)** - ⭐ 810
   gemini drawing MCP & skill through browser, can be used in openclaw or any agent that supports MCP. Gemini画图 MCP和sill，支持龙虾或任何agent使用٩(๑>◡<๑)۶

587. **[context-space](https://github.com/context-space/context-space)** - ⭐ 809
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

588. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

589. **[LaunchStack](https://github.com/Deodat-Lawson/LaunchStack)** - ⭐ 809
   AI-powered StartUp Accelerator Engine built with Next.js, LangChain, PostgreSQL + pgvector. Upload, organize, and chat with documents. Includes predictive missing-document detection, role-based workflows, and page-level insight extraction.

590. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 806
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

591. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 805
   一个将ACE(Augment Context Engine) 做成MCP的项目

592. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 805
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

593. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 804
   The official Ruby SDK for the Model Context Protocol.

594. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 800
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

595. **[azure-skills](https://github.com/microsoft/azure-skills)** - ⭐ 800
   Official agent plugin providing skills and MCP server configurations for Azure scenarios.

596. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 797
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

597. **[vllora](https://github.com/vllora/vllora)** - ⭐ 795
   Debug your AI agents

598. **[Context](https://github.com/indragiek/Context)** - ⭐ 795
   Native macOS client for Model Context Protocol (MCP)

599. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 793
   🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎

600. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 790
   Vibetest MCP - automated QA testing using Browser-Use agents

601. **[llmwiki](https://github.com/lucasastorian/llmwiki)** - ⭐ 783
   Open Source Implementation of Karpathy's LLM Wiki. Upload documents, connect your Claude account via MCP, and have it write your wiki ! 

602. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 780
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

603. **[work-iq](https://github.com/microsoft/work-iq)** - ⭐ 778
   MCP Server and CLI for accessing Work IQ

604. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 777
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

605. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 775
   Google Search Console Insights with Claude AI for SEOs

606. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 770
   gcloud MCP server

607. **[figma-mcp-go](https://github.com/vkhanhqui/figma-mcp-go)** - ⭐ 769
   Figma MCP for free users — no rate limits, full read/write, text to designs, designs to code

608. **[tradememory-protocol](https://github.com/mnemox-ai/tradememory-protocol)** - ⭐ 767
   Decision audit trail + persistent memory for AI trading agents. Outcome-weighted recall, SHA-256 tamper detection, 17 MCP tools.

609. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 766
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

610. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 766
   Connect ClickHouse to your AI assistants.

611. **[token-savior](https://github.com/Mibayy/token-savior)** - ⭐ 766
   The MCP server that turns Claude into the only coding agent hitting 100% on a real benchmark. -77% active tokens, -76% wall time, 0 losses across 96 tasks on Claude Opus 4.7. Structural code navigation + persistent memory. Works with every MCP client.

612. **[codedb](https://github.com/justrach/codedb)** - ⭐ 765
   Zig code intelligence server and MCP toolset for AI agents. Fast tree, outline, symbol, search, read, edit, deps, snapshot, and remote GitHub repo queries.

613. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 764
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

614. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 763
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

615. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 763
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

616. **[runno](https://github.com/taybenlor/runno)** - ⭐ 762
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

617. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 761
   A MCP server implementation for hyperbrowser

618. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 756
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

619. **[opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp)** - ⭐ 756
   Twitter/X Data · User Profiles · Tweet Search · Follower Events · KOL Tracking

620. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 754
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

621. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 753
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

622. **[tapo](https://github.com/mihai-dinculescu/tapo)** - ⭐ 753
   🦀 Rust API, 🐍 Python API, and 🤖 MCP Server for TP-Link Tapo smart devices

623. **[samples](https://github.com/strands-agents/samples)** - ⭐ 751
   Agent samples built using the Strands Agents SDK.

624. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 750
   LLDB MCP Integration + other helpful commands

625. **[xmcp](https://github.com/xdevplatform/xmcp)** - ⭐ 750
   MCP server for the X API

626. **[obot](https://github.com/obot-platform/obot)** - ⭐ 750
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

627. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 747
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

628. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 747
   Build Claude Code–style deep agents in Python: tool-calling, sandboxed execution, multi-agent teams, skills, checkpoints, and unlimited context — all on Pydantic AI.

629. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 745
   A flexible HTTP fetching Model Context Protocol server.

630. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 743
   All in one vscode plugin for mcp developer

631. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 741
   MCP Server for SearXNG

632. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 740
   An MCP server that provides control over Android devices via adb

633. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 738
   Clojure MCP

634. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 735
   MCP Server for Burp

635. **[mcp](https://github.com/laravel/mcp)** - ⭐ 735
   Rapidly build MCP servers for your Laravel applications.

636. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 735
   Next.js Development for Coding Agent

637. **[room](https://github.com/quoroom-ai/room)** - ⭐ 734
   Open-source earning-focused swarm intelligence engine. Self-governing AI collectives (queen, workers, quorum voting) running locally via MCP. Works with Claude Code, Codex, or pay-per-use APIs.

638. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 725
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

639. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 724
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

640. **[Wax](https://github.com/christopherkarani/Wax)** - ⭐ 724
   Single-file memory layer for AI agents, sub mili-second RAG on Apple Silicon. Metal Optimized On-Device. No Server. No API. One File. Pure Swift

641. **[fim-one](https://github.com/fim-ai/fim-one)** - ⭐ 723
   LLM-powered Agent Runtime with Dynamic DAG Planning & Concurrent Execution

642. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 720
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

643. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 716
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

644. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 716
   It's a plugin extension in Zotero.  Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。

645. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 715
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

646. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 714
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

647. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 713
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

648. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 713
   CUGA is an open-source generalist agent harness for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

649. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 712
   Nornicdb is a distributed low-latency, Graph+Vector, Temporal MVCC with all sub-ms HNSW search, graph traversal, and writes. Using Neo4j Bolt/Cypher and qdrant's gRPC means you can switch with no changes. Then, adding intelligent features like schemas, managed embeddings, LLM reranking+inferrence, GPU accel, Auto-TLP, Memory Decay, and MCP server.

650. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 710
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

651. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 710
   MCP server for Docker

652. **[Proxima](https://github.com/Zen4-bit/Proxima)** - ⭐ 706
   Multi-AI MCP Server - Connect ChatGPT, Claude, Gemini & Perplexity to your coding tools without any API

653. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 705
   Install, manage and develop MCP servers and skills for agents

654. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 700
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

655. **[langgraph-mcp-agents](https://github.com/braincrew-lab/langgraph-mcp-agents)** - ⭐ 700
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

656. **[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)** - ⭐ 700
   Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration.

657. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 698
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

658. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 696
   A simple MCP server for Obsidian

659. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 694
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、HITL、Skill、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

660. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 694
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

661. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 690
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

662. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 689
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

663. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 685
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

664. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 684
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

665. **[axon](https://github.com/harshkedia177/axon)** - ⭐ 683
   Graph-powered code intelligence engine — indexes codebases into a knowledge graph, exposed via MCP tools for AI agents and a CLI for developers.

666. **[MemoMind](https://github.com/24kchengYe/MemoMind)** - ⭐ 682
   Give your AI agent a brain that remembers. Local memory system for Claude Code — 100% private, GPU-accelerated, zero cloud dependency.

667. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 681
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

668. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 680
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

669. **[argo](https://github.com/xark-argo/argo)** - ⭐ 679
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

670. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 677
   飞书/Lark官方 OpenAPI MCP

671. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 676
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

672. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 674
   An MCP server for interacting with Sentry via LLMs.

673. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 673
   Laravel API for Ai Agents and humans.

674. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 673
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

675. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 672
   A simple CLI to run LLM prompt and implement MCP client.

676. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 669
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

677. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 665
   A local Apple Documentation crawler and MCP server. Written in Swift.

678. **[clihub](https://github.com/thellimist/clihub)** - ⭐ 665
   Turn any MCP server into CLI

679. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 662
   MCP configuration to connect AI agent to a Linux machine.

680. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 660
   Shell and coding agent on mcp clients

681. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 660
   Official Jina AI Remote MCP Server

682. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 660
   The open context engine for AI agents support 15+ data sources. Built on Rust and Apache DataFusion.

683. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 659
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

684. **[ship-safe](https://github.com/asamassekou10/ship-safe)** - ⭐ 658
   CLI security scanner built for the agentic era. Detects CI/CD misconfigs, agent permission risks, MCP tool injection, hardcoded secrets, and DMCA-flagged AI dependencies.

685. **[idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)** - ⭐ 657
   Pre-build reality check for AI coding agents. Scans GitHub, HN, npm, PyPI, Product Hunt. MCP server. 290+ stars.

686. **[codexia](https://github.com/milisp/codexia)** - ⭐ 656
   Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, skills management

687. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

688. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 655
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

689. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 655
   A comprehensive collection of Model Context Protocol (MCP) servers

690. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 653
   Querying local documents, powered by LLM

691. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 651

692. **[agent-kit](https://github.com/KeyID-AI/agent-kit)** - ⭐ 650
   Give Claude/Cursor email powers. 27 MCP tools — inbox, send, reply, contacts, search. Free, no signup.

693. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 646
   "AnyTool: Universal Tool-Use Layer for AI Agents"

694. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 645
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

695. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 645
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

696. **[agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator)** - ⭐ 645
   🚀 One sentence → multi-AI-role collaboration → complete plan in minutes. 211+ expert roles, zero-code YAML, 9 LLM providers (6 free). 一句话调度多个AI专家自动协作，几分钟交付完整方案。

697. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 644
   EnrichMCP is a python framework for building data driven MCP servers

698. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 643

699. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 642
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

700. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 642
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

701. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

702. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 640
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

703. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 638
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

704. **[ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero)** - ⭐ 637
    🚀 2026 最系统的 AI Agent 速成指南｜智能体实战教程 · 完整学习路径  + 实战项目 + 面试题库 · 对标大模型应用开发工程师岗位 · 覆盖LangChain / LangGraph / Coze / Dify / MCP / skills / LLM / RAG / 提示词 · 企业级部署与微调 · 从0到企业级落地 + 从学习到上线项目 + 面试准备一体化 

705. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 635
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

706. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 634
   Talk to a Cloudflare Worker from Claude Desktop!

707. **[oxideterm](https://github.com/AnalyseDeCircuit/oxideterm)** - ⭐ 634
   Local-first SSH workspace for local shells and remote machines — SSH, SFTP, trzsz, port forwarding, lightweight remote editing, file management, and BYOK AI in one native binary. Built with Tauri 2 and pure Rust SSH. Zero Electron, zero OpenSSL, zero telemetry, and no app subscription for core SSH workflows.

708. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 633
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

709. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 628
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

710. **[stash](https://github.com/alash3al/stash)** - ⭐ 628
   Stash — persistent memory layer for AI agents. Episodes, facts, and working context stored in Postgres. MCP server included. Self-hosted, single binary, no cloud required.

711. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 625
   MCP-NixOS - Model Context Protocol Server for NixOS resources

712. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

713. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

714. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 623
   mem-agent mcp server

715. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 623
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

716. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 622
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

717. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 620
   GitOps on Autopilot Mode

718. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 620
    Feishu / Lark 飞书文档与任务管理工具，支持 MCP 服务器和 CLI + Skill 两种使用方式，可无缝集成 Cursor、Claude Code、Cline 等 AI 编码工具

719. **[ScienceClaw](https://github.com/beita6969/ScienceClaw)** - ⭐ 618
   🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory.

720. **[codeg](https://github.com/xintaofei/codeg)** - ⭐ 617
   A unified workspace for local AI coding agents (Claude Code, Codex, Gemini CLI, etc.) — desktop app, standalone server, or Docker. Conversation aggregation, git worktree workflows, MCP/Skills management, chat channel integration (Telegram, Lark, iLink), and integrated terminal, all accessible from any browser.

721. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 617
   Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

722. **[k-dense-byok](https://github.com/K-Dense-AI/k-dense-byok)** - ⭐ 617
   An AI co-scientist powered by Scientific Agent Skills running on your desktop.

723. **[ThinkWatch](https://github.com/ThinkWatchProject/ThinkWatch)** - ⭐ 617
   Enterprise AI bastion host for secure AI API and MCP access, with unified proxying, RBAC, audit logs, rate limiting, and cost tracking across OpenAI, Anthropic, Gemini, and self-hosted LLMs.

724. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 616
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

725. **[Overture](https://github.com/SixHq/Overture)** - ⭐ 615
   Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. 

726. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 615
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

727. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 613
   A coding agent and general agent harness for building and orchestrating agentic applications.

728. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 613
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

729. **[tome](https://github.com/runebookai/tome)** - ⭐ 612
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

730. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 610
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

731. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 609
   A model-driven approach to building AI agents in just a few lines of code. 

732. **[google-meta-ads-ga4-mcp](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)** - ⭐ 609
   MCP server for Google Ads, Meta Ads & GA4 — works with ChatGPT, Claude, Cursor, n8n, Windsurf & more. 250+ tools for campaign management, analytics & optimization.

733. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 608
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

734. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 608
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

735. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 603
   Convert Any OpenAPI V3 API to MCP Server

736. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 602
   Daydreams is a set of tools for building agents for commerce

737. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 602
   MCP server to deploy apps to Cloud Run

738. **[JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP)** - ⭐ 602
   JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它   将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、   Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、   加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等   场景

739. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 600
   The .NET library to build AI agents with 30+ built-in connectors.

740. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 600
   Making docling agentic through MCP

741. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 597
   MCP to connect your LLM with Spotify.

742. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 596
   MCP Server for Metasploit

743. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 594
   MCP server for interacting with Neon Management API and databases

744. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 592
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

745. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 592
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

746. **[colab-mcp](https://github.com/googlecolab/colab-mcp)** - ⭐ 592
   An MCP server for interacting with Google Colab

747. **[GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)** - ⭐ 591
   An native MCP server extension for Ghidra

748. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 591

749. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 590
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

750. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 590

751. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 587
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

752. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 585
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

753. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 585
   MCP Server for interacting with Android Devices.

754. **[agentshield](https://github.com/affaan-m/agentshield)** - ⭐ 584
   AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions. Available as CLI, GitHub Action, ECC plugin, and GitHub App integration. 🛡️

755. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 583
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

756. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 583
   MCP-Universe is a comprehensive framework designed for RL training, benchmarking, and developing AI agents for general tool-use.

757. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 582
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (Claude Code, Cursor, Antigravity, etc.) to read, analyze, and modify Figma designs

758. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 582
   LangGraph solution template for MCP

759. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 578
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

760. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 578
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

761. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 578
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

762. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 577
   AI-based stock analysis and trading system

763. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 576
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

764. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 576
   A tool that converts OpenAPI specifications to MCP server

765. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 575
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

766. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 573
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript and C++.

767. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 572
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

768. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 572
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

769. **[probe](https://github.com/probelabs/probe)** - ⭐ 572
   AI-friendly semantic code search engine for large codebases. Combines ripgrep speed with tree-sitter AST parsing. Powers AI coding assistants with precise, context-aware code understanding.

770. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 572
   Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. OpenAI GPT-5, Deepseek R1, Claude Opus/Sonnet, Gemini 3, Grok 4, Alibaba Qwen, Kimi, ElevenLabs TTS, Inworld, OpenRouter, Groq, GLM, Ollama, Local, Meshy, Tripo, Hunyuan3D, Rodin, fal, Dashscope, Seedream. NPC AI, agentic, chat, 3D gen, TTS, multimodal, image gen. UnrealMCP/UnrealClaude

771. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 571
   MCP to allow AI agents to control Unreal

772. **[kraken-cli](https://github.com/krakenfx/kraken-cli)** - ⭐ 571
   The first AI-native CLI for trading crypto, stocks, forex, and derivatives.

773. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 570
   A MCP server for Home Assistant

774. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 567
   MCP Server for Turkish & American Stock Exchange and Fund Data

775. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 566
   An Mcp client inside Emacs

776. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 564
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

777. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 563
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

778. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 562
   Open Source Voice Agent Platform

779. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 560
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

780. **[zerobox](https://github.com/afshinm/zerobox)** - ⭐ 558
   Lightweight, cross-platform process sandboxing powered by OpenAI Codex's runtime. Sandbox any command with file, network, and credential controls.

781. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 557
   Token-efficient MCP adapter for Pi coding agent

782. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 556
   An MCP Multimodal AI Agent with eyes and ears!

783. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

784. **[casbin-gateway](https://github.com/casbin/casbin-gateway)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

785. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 555
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

786. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 553
   Security scanner for MCP servers

787. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 551
   A MCP (Model Context Protocol) server for interacting with dbt.

788. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 551
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

789. **[MindOS](https://github.com/GeminiLight/MindOS)** - ⭐ 550
   MindOS is a Human-AI Collaborative Mind System, where human thinks and agents act. Globally sync your mind for all agents: transparent, controllable, and evolving symbiotically.

790. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 549
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

791. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 547
   A structural code search engine for Al agents.

792. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 546
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

793. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 544
   SonarQube MCP Server

794. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 543
   A Model Context Protocol server for IDA

795. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 543
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

796. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 543
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

797. **[tda](https://github.com/irockel/tda)** - ⭐ 542
   TDA - Thread Dump Analyzer (for Java). Analyze your Thread Dumps with a GUI or use it as MCP Server.

798. **[MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio)** - ⭐ 542
   MimikaStudio - A local-first application for macOS (Apple Silicon) + Agentic MCP Support

799. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 541
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

800. **[ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw)** - ⭐ 540
   ScienceClaw is a personal research assistant built with LangChain DeepAgents and AIO Sandbox infrastructure, adopting a completely new architecture beyond OpenClaw. It offers stronger security, better transparency, and a more user-friendly experience.

801. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 539
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

802. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 537
   A universal CLI client for MCP. mcpc supports persistent sessions, stdio/HTTP, OAuth 2.1, tasks, JSON output for code mode, proxy for AI sandboxes, x402, and more.

803. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 537

804. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 537
   LLM + MCP + RAG = Magic

805. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 537
   微信读书MCP

806. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 537
   MCP server for querying Apple Health data with natural language and SQL

807. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 536

808. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 535
   Home Assistant MCP server agent. Enable Claude Code, Cursor, VS Code or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

809. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 535
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

810. **[docsagent](https://github.com/docsagent/docsagent)** - ⭐ 535
   DocsAgent is a local-first AI documents assistant that lets you securely index and chat with thousands of desktop documents with zero cloud leakage.

811. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 534
   MCP Server and CLI for accessing Work IQ

812. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 534

813. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 533
   MCP server for document format conversion using pandoc.

814. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 533
   🚀 Universal SDK for building next-gen MCP servers

815. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 531
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

816. **[ethora](https://github.com/dappros/ethora)** - ⭐ 531
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

817. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 529
   An MCP server to query any Postgres database in natural language.

818. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 527
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

819. **[rails_ai_agents](https://github.com/ThibautBaissac/rails_ai_agents)** - ⭐ 526
   Specialized AI skills, agents, rules and hooks for modern Rails AI driven-development + Spec-Driven-Development kit + MCP

820. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 523
   Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

821. **[jarvis-registry](https://github.com/ascending-llc/jarvis-registry)** - ⭐ 522
   Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with built-in identity, access control, and full observability.

822. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 520
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

823. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 518
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single) 

824. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 517

825. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 516
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

826. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 515
   A Model-Context Protocol Server for YouTube

827. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

828. **[human-skill-tree](https://github.com/24kchengYe/human-skill-tree)** - ⭐ 515
   🌳 AI-Powered Skill Tree for Lifelong Human Learning. 30+ skills from K-12 to career & social intelligence, built on cognitive science. | 人类养成记：AI 驱动的终身学习技能树

829. **[MinerU-Document-Explorer](https://github.com/opendatalab/MinerU-Document-Explorer)** - ⭐ 514
   Agent-native knowledge engine with MCP tools for document indexing, wiki organization, fast retrieval and deep reading across PDF/DOCX/PPTX/Markdown

830. **[cve-mcp-server](https://github.com/mukul975/cve-mcp-server)** - ⭐ 514
   Production-grade MCP server giving Claude 27 security intelligence tools across 21 APIs — CVE lookup, EPSS scoring, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal, and more.

831. **[desktop](https://github.com/openyak/desktop)** - ⭐ 513
   Yak is all you need

832. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 511

833. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 511
   MaverickMCP - Personal Stock Analysis MCP Server

834. **[semble](https://github.com/MinishLab/semble)** - ⭐ 511
   Fast and Accurate Code Search for Agents. Uses ~98% fewer tokens than grep+read

835. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 510
   An MCP extension for Ghidra

836. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 508
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

837. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 508
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

838. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

839. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 507
   MCP Monitoring with eBPF

840. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 506
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

841. **[resend-mcp](https://github.com/resend/resend-mcp)** - ⭐ 506
   The official MCP server to send emails and interact with Resend

842. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 505
   Yes Mcp server in bash

843. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 501
   The Ultimate Google Docs, Sheets, Drive, Gmail, & Google Calendar MCP Server. This MCP (primarily for use in Claude Desktop) gains full access to your google suite and lets claude do its thing.

844. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 499
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

845. **[everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh)** - ⭐ 499
   everything-claude-code 中文翻译项目：完整的 Claude Code 配置集合（agents, skills, hooks, commands, rules, MCPs）。源自 Anthropic 黑客松获胜者的实战配置，助力中文工程师高效理解与使用 Claude Code。

846. **[awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents)** - ⭐ 498
   ✨ A curated list of awesome GitHub instructions, prompt, skills, MCPs and agent markdown files for enhancing your GitHub Copilot AI experience.

847. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 497
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

848. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 497
   BioMCP: Biomedical Model Context Protocol

849. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 495
   Make your meetings accessible to AI Agents

850. **[open-harness](https://github.com/MaxGfeller/open-harness)** - ⭐ 494
   A code-first, composable SDK to build powerful AI agents

851. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

852. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

853. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 488
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

854. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 488
   A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI.

855. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 487
   MCP Server to interact with Google Gsuite prodcuts

856. **[OpenSail](https://github.com/TesslateAI/OpenSail)** - ⭐ 487
   OpenSail is the open-source alternative to Codex App, Claude Desktop, Cursor, and Cowork for agentic software work.

857. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 486
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

858. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 486
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

859. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 484
   MCP server for Obsidian vaults — read, write, search, and surgically edit notes, tags, and frontmatter via the Local REST API plugin.

860. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 483
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

861. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 481
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

862. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 479
   Official Docker MCP registry 

863. **[director](https://github.com/fdmtl/director)** - ⭐ 478
   MCP Playbooks for AI agents

864. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 478
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

865. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 478
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

866. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 477
   小红书MCP服务 x-s x-t js逆向

867. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 477
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

868. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 477
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

869. **[director](https://github.com/director-run/director)** - ⭐ 476
   MCP Playbooks for AI agents

870. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 476
   A docker MCP Server (modelcontextprotocol)

871. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 476
   Local MCP server for DuckDB and MotherDuck

872. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 472

873. **[docfork](https://github.com/docfork/docfork)** - ⭐ 472
   Docfork - Up-to-date Docs for AI Agents.

874. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 471
   An SDK building Laravel MCP servers

875. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 471
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

876. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 470
   Aser is a lightweight, self-assembling AI Agent frame.

877. **[cordum](https://github.com/cordum-io/cordum)** - ⭐ 470
   The open agent control plane. Govern autonomous AI agents with pre-execution policy enforcement, approval gates, and audit trails. Works with LangChain, CrewAI, MCP, and any framework.

878. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 468
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

879. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 468
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

880. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 466
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

881. **[blockrun-mcp](https://github.com/BlockRunAI/blockrun-mcp)** - ⭐ 464
   Live data for AI agents — search, research, markets, crypto, X/Twitter. Pay-per-call via x402 micropayments.

882. **[travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit)** - ⭐ 462
   AI-powered travel hacking  and search with cash, points, miles, and award flights. Drop-in skills and MCP servers for Claude, Codex, and OpenCode.

883. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 459
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

884. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 459
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

885. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 457
   Things.app MCP Server

886. **[roam-code](https://github.com/Cranot/roam-code)** - ⭐ 456
   Architectural intelligence layer for AI coding agents. Structural graph, architecture governance, multi-agent orchestration, vulnerability mapping. 139 commands, 101 MCP tools, 26 languages, 100% local.

887. **[opentabs](https://github.com/opentabs-dev/opentabs)** - ⭐ 455
   Browser automation clicks buttons. OpenTabs calls APIs.

888. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 454
   MCP server that execute applescript giving you full control of your Mac

889. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 453
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

890. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 452
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

891. **[welsonjs](https://github.com/gnh1201/welsonjs)** - ⭐ 450
   WelsonJS - Build a Windows app on the Windows built-in JavaScript engine

892. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 450
   基于.NET搭建-AI知识库智能体-现代化Saas企业级前后端分离架构：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、MCP协议服务、IOC模块化注入、自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、本地离线AI模型调用、API多版本、单元测试、RabbitMQ、Skills技能使用、AI知识库、AI联网搜索

893. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 448
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

894. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 446
   The AI-powered toolkit that grows your YouTube channel on autopilot.

895. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

896. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

897. **[claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)** - ⭐ 446
   Plugin suite + bundled MCP servers for Claude Code. Full delivery lifecycle: Agile pipeline with multi-model AI review, project bootstrap, documentation generation, codebase audits, performance optimization, community workflows. Includes hex-line (hash-verified editing), hex-graph (code knowledge graph), and hex-ssh (remote SSH) MCP servers.

898. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 445
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

899. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 444
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

900. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

901. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 444
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

902. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 443
   Search Airbnb using your AI Agent

903. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 441
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

904. **[vmlx](https://github.com/jjang-ai/vmlx)** - ⭐ 441
   vMLX - Home of JANG_Q - Cont Batch, Prefix, Paged, KV Cache Quant, VL - Powers MLX Studio. Image gen/edit, OpenAI/Anth

905. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 439
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

906. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 439
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

907. **[ZeroToken](https://github.com/AMOS144/ZeroToken)** - ⭐ 437
   ZeroToken — Record once, automate forever. A lightweight MCP for agent-driven browser automation, script recording, and scheduled execution.

908. **[claude-video-vision](https://github.com/jordanrendric/claude-video-vision)** - ⭐ 437
   Give Claude the ability to watch and understand videos — Claude Code plugin with frame extraction and multimodal audio analysis

909. **[swarmclaw](https://github.com/swarmclawai/swarmclaw)** - ⭐ 435
   Self-hosted multi-agent AI runtime with MCP server support. Build, orchestrate, and run autonomous agents with memory, skills, schedules, and 23+ LLM providers (Claude, GPT, Gemini, OpenRouter, Ollama).

910. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 433
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

911. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 431
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

912. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 431
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

913. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 431
   A CLI inspector for the Model Context Protocol

914. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 430
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

915. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 430
   Spec-Driven Development MCP Server, not just Vibe Coding

916. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 430
   An implementation of Model Context Protocol (MCP) server for Argo CD.

917. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 429
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

918. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 428
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

919. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 428
   MCP to help Defenders Detection Engineer Harder and Smarter

920. **[freee-mcp](https://github.com/freee/freee-mcp)** - ⭐ 428
   Model Context Protocol (MCP) server for freee API integration

921. **[google-ads-mcp](https://github.com/googleads/google-ads-mcp)** - ⭐ 428

922. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 427
   MCP server to access Garmin data

923. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 426
   Govern & Secure your AI

924. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 426
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

925. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 425
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

926. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 424
   Baidu Map MCP Server

927. **[mcp](https://github.com/cloudflare/mcp)** - ⭐ 424
   MCP server for the Cloudflare API

928. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 423

929. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 423
   lunar.dev: Agent native MCP Gateway for governance and security

930. **[openclaw-claude-code](https://github.com/Enderfga/openclaw-claude-code)** - ⭐ 423
   OpenClaw plugin — turn Claude Code CLI into a programmable, headless coding engine with plenty of tools, agent teams, and multi-model proxy

931. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

932. **[skylos](https://github.com/duriantaco/skylos)** - ⭐ 422
   Open-source Python, TypeScript, and Go SAST with dead code detection. Finds secrets, exploitable   flows, and AI regressions. VS Code extension, GitHub Action, and MCP server for AI agents.

933. **[n8n-claw](https://github.com/freddy-schuetz/n8n-claw)** - ⭐ 420
   OpenClaw-inspired autonomous AI agent built entirely in n8n. Adaptive RAG-powered memory, Skills via MCP templates, Expert Agents with delegated sub-agents, proactive task management, media understanding - self-hosted with one setup script

934. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 419
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

935. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 419
   Unlock 650+ MCP servers tools in your favorite agentic framework.

936. **[memorix](https://github.com/AVIDS2/memorix)** - ⭐ 419
   Open-source cross-agent memory layer for coding agents via MCP. Compatible with Cursor, Claude Code, Codex, Windsurf, Gemini CLI, GitHub Copilot, Kiro, OpenCode, Antigravity, and Trae.

937. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 418
   Memento MCP: A Knowledge Graph Memory System for LLMs

938. **[station](https://github.com/cloudshipai/station)** - ⭐ 417
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

939. **[mq](https://github.com/harehare/mq)** - ⭐ 416
   A jq-like Markdown query language for command-line processing

940. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 416
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

941. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 414
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

942. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 414
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

943. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 413
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

944. **[speakeasy](https://github.com/speakeasy-api/speakeasy)** - ⭐ 410
   Build APIs your users love ❤️ with Speakeasy. ✨ Polished and type-safe SDKs. 🌐 Terraform providers, MCP servers, CLIs and Contract Tests for your API. OpenAPI native. 

945. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 408
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands. 

946. **[robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp)** - ⭐ 408
   Create agentic AI workflows in ROBLOX Studio

947. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 407
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

948. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 407
   MCP server for JADX-AI Plugin

949. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 407
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

950. **[lsbot](https://github.com/ruilisi/lsbot)** - ⭐ 406
   Lean & Secure Bot

951. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 405
   OpenSkills: Run Claude Skills Locally using any LLM

952. **[RenderDocMCP](https://github.com/halby24/RenderDocMCP)** - ⭐ 404

953. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 404
   The safest way to make REST calls in C# with an MCP Generator

954. **[Agent](https://github.com/macOS26/Agent)** - ⭐ 404
   Any AI, replaces Claude Code, Cursor, OpenClaw. Over 18 LLM providers (Claude, OpenAI, Gemini, Ollama, Zai, HF, Qwen) wired into a native Mac app that writes code, builds Xcode projects, bumps versions, manages git, automate Safari, AppleScript 50 apps, extend w/ MCP Servers, run tasks from your iPhone via Messages, drive any Accessible app.

955. **[distributed-load-testing-on-aws](https://github.com/aws-solutions/distributed-load-testing-on-aws)** - ⭐ 403
   Distributed Load Testing on AWS automates performance testing at scale, demonstrating how systems behave under different load conditions and helping identify potential performance issues throughout their lifecycle.

956. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 402
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

957. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 401
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

958. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 399
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

959. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 399
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

960. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 398
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

961. **[memora](https://github.com/agentic-box/memora)** - ⭐ 398
   Give your AI agents persistent memory.

962. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 397
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

963. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 397
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

964. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 396

965. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 395
   基于 SSH 的 MCP 服务 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

966. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 395
   An MCP implementation for Selenium WebDriver

967. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 394
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

968. **[tentix](https://github.com/labring/tentix)** - ⭐ 394
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

969. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 393
   An experiment in software planning using MCP

970. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 393
   MCP Server for code graph analysis and visualization by CodeGPT

971. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 392
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

972. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 391
   MCP server for Todoist integration enabling natural language task management with Claude

973. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 391
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

974. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 390
   Local Groq Desktop chat app with MCP support

975. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 390
   Context-Engine MCP - Agentic Context Compression Suite

976. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 389
   MCP Server for interacting with Salesforce instances

977. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 388
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

978. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 388
   An MCP server for loading skills (shim for non-claude clients).

979. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 388
   Control your Android devices with AI using Model Context Protocol

980. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 388
   F2C MCP Server

981. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 388
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

982. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 388
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

983. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 387
   Xiaozhi MCP sample program

984. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 385
   A centralized reverse-proxy platform for MCP servers — manage, group, and export as Skills from a single endpoint.

985. **[jarvis](https://github.com/isair/jarvis)** - ⭐ 385
   A 100% private AI voice assistant that lives on your computer (works offline). Talk naturally as if Jarvis is a third person in the room, and get conversational responses. It remembers everything, knows location and time, can check the web, control Chrome, track nutrition, and more with support for unlimited MCPs / tools without context rot.

986. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 384
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

987. **[clawreins](https://github.com/pegasi-ai/clawreins)** - ⭐ 383
   Runtime security for OpenClaw agents. Scan, fix, monitor.

988. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 383
   Model Context Protocol server for GraphQL

989. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 383
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

990. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 382
   A macOS AppleScript MCP server

991. **[devopness](https://github.com/devopness/devopness)** - ⭐ 381
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

992. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 380
   Create a plan from a description in minutes

993. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 380
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

994. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 380
   MCP server for searching and retrieving Claude Agent Skills using vector search

995. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 380
   MCP Server implementation for Ableton Live OSC control

996. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 379
   MCP server connecting to Kubernetes

997. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 379
   MCP server retrieving transcripts of YouTube videos

998. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 378
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

999. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 377
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

1000. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 376
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

1001. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 376
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

1002. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 375
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

1003. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 374
   Model Context Protocol (MCP) Server for Graphlit Platform

1004. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 374
   MCP server that provides LLMs with tools for interacting with EVM networks

1005. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 374
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

1006. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 373
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

1007. **[mcp](https://github.com/IBM/mcp)** - ⭐ 373
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

1008. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 373
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

1009. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 373
   Headless IDA Pro MCP Server

1010. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 372
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

1011. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

1012. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 372
   MCP Server implementation for Xcode integration

1013. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 372
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

1014. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 372
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

1015. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 372
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

1016. **[daymon](https://github.com/daymonio/daymon)** - ⭐ 371
   Daymon puts your favorite AI to work 24/7. It schedules, remembers, and orchestrates your own virtual team. Free.

1017. **[scarf](https://github.com/awizemann/scarf)** - ⭐ 371
   Native macOS and iOS App for the Hermes AI agent — multi-window, multi-server (local + remote over SSH). Chat, dashboard, sessions, memory, cron, MCP, and more.

1018. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 370
   🐕⚡「极简至上 效率为王 秒级接入 一链即用」的 AI Bot

1019. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 370
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

1020. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 369
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

1021. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 368
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

1022. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 368
   MCP server for Bazi (八字) information

1023. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 367
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

1024. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 367
   A list of open-source AI projects you can use to generate income easily.

1025. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 366
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

1026. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 366
   Elixir Model Context Protocol (MCP) SDK

1027. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 366
   Model Context Protocol SDK for PHP

1028. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

1029. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 365
   deep, reliable and confidential coding-context

1030. **[studio](https://github.com/decocms/studio)** - ⭐ 365
   Open-source control plane for your AI agents. Connect tools, hire agents, track every token and dollar

1031. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 364
   Lean Theorem Prover MCP

1032. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 363
   Sega Master System / Game Gear / SG-1000 emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1033. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 363
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

1034. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 362
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

1035. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 362
   An MCP server for Azure DevOps

1036. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 362
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

1037. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 359
   MCP server for Claude to access Outlook data via Microsoft Graph API

1038. **[pinion-os](https://github.com/chu2bard/pinion-os)** - ⭐ 357
   Client SDK, Claude plugin and skill framework for the Pinion protocol. x402 micropayments on Base.

1039. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

1040. **[hookdeck-cli](https://github.com/hookdeck/hookdeck-cli)** - ⭐ 354
   CLI for Hookdeck: forward webhooks to localhost (ngrok alternative), manage and query Event Gateway resources (sources, connections, destinations, events), run the MCP server for AI agents. Free for dev.

1041. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 354
   MCP server to expose VS Code editing features to an LLM for AI coding

1042. **[PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor)** - ⭐ 354
   Free, open-source SQL Server performance monitoring — 32 collectors, real-time alerts, graphical plan viewer, MCP server for AI analysis. Supports SQL 2016-2025, Azure SQL, AWS RDS.

1043. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 353
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

1044. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 353
   First AI‑enabled open-source Human Capital Management system that you can start using today.

1045. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 350

1046. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 350
   MCP server for Coolify — 38 optimized tools for managing self-hosted PaaS through AI assistants

1047. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 349
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

1048. **[boltmcp](https://github.com/boltmcp/boltmcp)** - ⭐ 348

1049. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

1050. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 347
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

1051. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 347
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

1052. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 345
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

1053. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 345
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

1054. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 345
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

1055. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 345
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

1056. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 345
   Semantic code searcher and codebase utility

1057. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 344
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

1058. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 344
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

1059. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 343
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

1060. **[Aegis](https://github.com/Justin0504/Aegis)** - ⭐ 341
   Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes.                                                                         

1061. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 341
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

1062. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

1063. **[real-estate-mcp](https://github.com/tae0y/real-estate-mcp)** - ⭐ 340
   🏠 Ask Claude about Korean apartment prices — powered by 국토교통부 open API

1064. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 340
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

1065. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 340
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

1066. **[mcp](https://github.com/oracle/mcp)** - ⭐ 340
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

1067. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 340
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

1068. **[token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp)** - ⭐ 339
   Intelligent token optimization for Claude Code - achieving 95%+ token reduction through caching, compression, and smart tool intelligence

1069. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 338
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

1070. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 338
   Mapbox Model Context Protocol (MCP) server

1071. **[mesh](https://github.com/decocms/mesh)** - ⭐ 337
   One secure endpoint for every MCP server. Deploy anywhere.

1072. **[nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server)** - ⭐ 337
   AI image generation MCP server powered by Google Gemini, with smart model selection and 4K output

1073. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 336
   Example of an MCP server with custom tools that can be called directly from cursor

1074. **[moling](https://github.com/gojue/moling)** - ⭐ 336
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

1075. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 335
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

1076. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 334
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1077. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 333

1078. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 333
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1079. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 332
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

1080. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 332
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

1081. **[EDDI](https://github.com/labsai/EDDI)** - ⭐ 332
   Config-driven engine that turns JSON into production-grade AI agents. Multi-agent orchestration, 12+ LLM providers, MCP/A2A protocols, RAG, persistent memory, and enterprise compliance (EU AI Act, GDPR, HIPAA). Built on Quarkus.

1082. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 331
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

1083. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

1084. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 330
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

1085. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 330

1086. **[entroly](https://github.com/juyterman1000/entroly)** - ⭐ 329
   Entroly-Daemon: Self-Evolving Daemon. Compress 2M-token repos into a razor-sharp Principal Engineer's context. 85–99% fewer tokens, 100% accuracy retention (verified by live API benchmarks). Built for Cursor, Claude Code, Opus, Codex, GPT & Custom Providers.

1087. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 328
   A Model Context Protocol server for building an investor agent

1088. **[meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)** - ⭐ 328
   Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis.

1089. **[pipelock](https://github.com/luckyPipewrench/pipelock)** - ⭐ 327
   Firewall for AI agents. DLP scanning, SSRF protection, bidirectional MCP scanning, tool poisoning detection, and prompt injection blocking.

1090. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 327
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1091. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 326
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

1092. **[safe-mcp](https://github.com/safe-agentic-framework/safe-mcp)** - ⭐ 325
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

1093. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 325
   Model Context Protocol server for DeepSeek's advanced language models

1094. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 324
   CAD MCP Server

1095. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 324
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

1096. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 324
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

1097. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 323
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

1098. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 323
   Source code of minecraft 1.12

1099. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 323
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

1100. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 323
   Lightweight MCP server for Spotify

1101. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 323
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

1102. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

1103. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 322
   web GUI for securely managing local OpenCode configuration

1104. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 322
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

1105. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 322
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

1106. **[emcee](https://github.com/mattt/emcee)** - ⭐ 321
   MCP generator for OpenAPIs 🫳🎤💥

1107. **[cymbal-air-toolbox-demo](https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo)** - ⭐ 321
   Demo of a customer service agent (Cymbal Air) using LangGraph, Tools, and RAG to interact with Google Cloud Databases via MCP Toolbox.

1108. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 320
   Software architecture tooling for the AI age

1109. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 320

1110. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 320

1111. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 320
   An MCP server for Massive.com Financial Market Data

1112. **[generator](https://github.com/context-hub/generator)** - ⭐ 319
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

1113. **[pydantic-resolve](https://github.com/allmonday/pydantic-resolve)** - ⭐ 319
   A universal data composition tool that generates JSON RPC, GraphQL, and even MCP.

1114. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 319
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

1115. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 318
   This is a Minecraft Base Client

1116. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 318
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

1117. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 318
   Repo of skills for autogen studio using model context protocol (mcp)

1118. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 318
   MCP server for Windows OS automation

1119. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 318

1120. **[swarmvault](https://github.com/swarmclawai/swarmvault)** - ⭐ 318
   Inspired by Karpathy's LLM Wiki. Local-first RAG knowledge base compiler with MCP server (Claude Code, Codex, OpenCode, OpenClaw). Turn raw research into a persistent markdown wiki, knowledge graph, and hybrid search that compound over time.

1121. **[deep-research-mcp](https://github.com/teelaitila/deep-research-mcp)** - ⭐ 317

1122. **[DebugMCP](https://github.com/microsoft/DebugMCP)** - ⭐ 316
   Gift your VS Code agent a real debugger: breakpoints, stepping, inspection.

1123. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 316
   Agentify Desktop lets Codex/Claude/OpenCode  control your logged-in ChatGPT, Claude, AiStudio, Gemini, Grok, Perplexity web sessions via MCP, parallel hidden/visible tabs, file upload + image download

1124. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 314
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

1125. **[STS2MCP](https://github.com/Gennadiyev/STS2MCP)** - ⭐ 314
   Full agentic runs for Slay the Spire 2. A mod that exposes in-game state, and the MCP server for the mod.

1126. **[octo-terminal-releases](https://github.com/johunsang/octo-terminal-releases)** - ⭐ 313
   Octo Terminal — The ultimate vibe coding terminal. AI-powered IDE with Claude, Codex, Ollama built-in. Terminal + editor + notes + browser in one app. Tauri + React + Rust.

1127. **[codemogger](https://github.com/glommer/codemogger)** - ⭐ 312
   Codemogger is a code indexing library and MCP server for AI coding agents

1128. **[agents](https://github.com/astronomer/agents)** - ⭐ 312
   AI agent tooling for data engineering workflows.

1129. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 312
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

1130. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 311
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

1131. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

1132. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 309
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡mcphub

1133. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 309
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

1134. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 308
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.) and AI agents (Claude Desktop, OpenClaw, etc.). Supports Serper, Tavily, and SearXNG.

1135. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 308
   An MCP server providing tools for image processing operations

1136. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 308
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

1137. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 307
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

1138. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 307
   MCP stdio server for frida

1139. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 306
   api router for MCP Servers

1140. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 305
   Turn any openapi file into an mcp server, with just the tools you need.

1141. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 305
   Smithery helps AI agents access external services via a unified gateway.

1142. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 305
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1143. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 305
   Appium MCP on Steroids!

1144. **[claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager)** - ⭐ 305
   GUI app to manage MCP servers for Claude Code

1145. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 305
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

1146. **[agentic-ai-apis](https://github.com/cporter202/agentic-ai-apis)** - ⭐ 304
   The ultimate collection of APIs for building autonomous AI agents — 2,036 production-ready APIs across Agents, AI Models, and MCP Servers. Stop wasting weeks building infrastructure. Plug these in and ship your agent today.

1147. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 303
   A working pattern for SSE-based MCP clients and servers

1148. **[Lucid](https://github.com/get-Lucid/Lucid)** - ⭐ 302
   An intelligence layer grounding autonomous agents in verified, real-time knowledge at scale.

1149. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 302
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

1150. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 302
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1151. **[Dex](https://github.com/davekilleen/Dex)** - ⭐ 301
   Your AI Chief of Staff — a personal operating system starter kit that adapts to your role. No coding required.

1152. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 301
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi, Exa), AI tools (Kagi FastGPT, Exa, Linkup), and content extraction services (Firecrawl, Tavily, Kagi). Includes GitHub search. All through a single interface.

1153. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 301
   Obsidian MCP (Model Context Protocol) Server

1154. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 300
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

1155. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 300
   MCP Server for Tree-sitter

1156. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 300
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1157. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 300
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

1158. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 299
   Agentic RAG for any scenario. Customize sources, depth, and width

1159. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 299
   MCP implementation of Claude Code capabilities and more

1160. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 299
   Discover Exceptional MCP Servers

1161. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 299
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

1162. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 299
   MCP Server for Odoo

1163. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 298
   SpringAI，LLM，MCP，Embedding

1164. **[certctl](https://github.com/shankar0123/certctl)** - ⭐ 298
   Self-hosted certificate lifecycle automation platform. Any CA, any server, zero human intervention. Full REST API, web dashboard, and agent-based deployment where private keys never leave your infrastructure. Includes CLI, MCP server for AI assistants, and compliance mapping for SOC 2, PCI-DSS, and NIST.

1165. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 298
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

1166. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 298
   MCP server for TouchDesigner

1167. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 297
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

1168. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 297
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1169. **[cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** - ⭐ 296
   Cross-Code Organizer (formerly Claude Code Organizer): cross-harness config dashboard for Claude Code, Codex CLI, MCP servers, skills, memories, agents, sessions, security scanning, context budget, and backups.

1170. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 295
   Minimal MCP Server for Aider

1171. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 295
   The specification for the Universal Tool Calling Protocol

1172. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 295
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

1173. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 294
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

1174. **[consult7](https://github.com/szeider/consult7)** - ⭐ 294
   MCP server to consult a language model with large context size

1175. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 293
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

1176. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 293
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

1177. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 293
   Home Assistant MCP Server

1178. **[daan](https://github.com/pluveto/daan)** - ⭐ 292
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

1179. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 291

1180. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 291

1181. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 291
   Apache Doris MCP Server

1182. **[unifi-mcp](https://github.com/sirkirby/unifi-mcp)** - ⭐ 291
   MCP servers for the UniFi suite of applications, Network, Protect, Access, and Drive

1183. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 290
   Standardized environment infrastructure for Agentic AI development.

1184. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 289
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

1185. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 288
   MCP server for browser automation using Playwright

1186. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 288
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

1187. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 288
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1188. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 287
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

1189. **[clawdcursor](https://github.com/AmrDab/clawdcursor)** - ⭐ 287
   OS-agnostic, model-agnostic desktop automation server. Gives any AI agent eyes, hands, and ground-truth verification on Windows, macOS, and Linux.

1190. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

1191. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 286
   simple web ui to manage mcp (model context protocol) servers in the claude app

1192. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 286
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

1193. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

1194. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 285
   Code to process many kinds of content by an author into an MCP server

1195. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 285
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

1196. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 285
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

1197. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 285
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1198. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 285
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1199. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 284
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

1200. **[alfanous](https://github.com/Alfanous-team/alfanous)** - ⭐ 284
   Alfanous is an Arabic search engine API provides the simple and advanced search in Quran , more features and many interfaces...

1201. **[awesome-fintech](https://github.com/moov-io/awesome-fintech)** - ⭐ 284
   A curated collection of open source fintech libraries and resources.

1202. **[Ori-Mnemos](https://github.com/aayoawoyemi/Ori-Mnemos)** - ⭐ 284
   Local-first persistent agentic memory powered by Recursive Memory Harness (RMH). Open source must win.

1203. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 283
   Model Context Protocol server implementation for Reddit

1204. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 282
   Bringing Human Capabilities to AI Agents

1205. **[unity-cli-loop](https://github.com/hatayama/unity-cli-loop)** - ⭐ 282
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1206. **[claude-code-organizer](https://github.com/mcpware/claude-code-organizer)** - ⭐ 282
   Dashboard to manage Claude Code memories, configs, and MCP servers — security scanner for tool poisoning, context token budget tracker, duplicate cleanup, scope management. npx @mcpware/claude-code-organizer

1207. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 282
   Volcengine MCP Servers

1208. **[polymarket-paper-trader](https://github.com/agent-next/polymarket-paper-trader)** - ⭐ 282
   Paper trading simulator for Polymarket — built for AI agents. MCP server, live order books, strategy backtesting. Install: npx clawhub install polymarket-paper-trader

1209. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

1210. **[h1-brain](https://github.com/PatrikFehrenbach/h1-brain)** - ⭐ 281
   MCP server that connects AI assistants to HackerOne for bug bounty hunting

1211. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

1212. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 280
   Apollo MCP Server

1213. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 279
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

1214. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 279
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1215. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 278
   MCP integration platforms making AI-Agents developers focusing on their own tasks

1216. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 278
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

1217. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 278
   A Model Context Protocol Server for MongoDB

1218. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 278
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

1219. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 277
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

1220. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 277
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

1221. **[godot-mcp](https://github.com/tomyud1/godot-mcp)** - ⭐ 277
   MCP Server and Godot Plugin for AI-assisted game development

1222. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 276
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

1223. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

1224. **[godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** - ⭐ 276
   162 MCP tools for AI-powered Godot 4 development. Scene, animation, 3D, physics, particles, audio, shader, input simulation, runtime analysis, navigation, testing & more. $5 one-time.

1225. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 276
   Model Context Protocol (MCP) Server for dify workflows

1226. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 275
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

1227. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 275
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

1228. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 275
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

1229. **[agent-trade-kit](https://github.com/okx/agent-trade-kit)** - ⭐ 275
   OKX trading MCP server — connect AI agents to spot, swap, futures, options & grid bots via the Model Context Protocol.  

1230. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 274
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

1231. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 274
   Lightweight agent orchestration dev tool that lives in your repo

1232. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 274
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

1233. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 273
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

1234. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 272
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

1235. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

1236. **[api-agent](https://github.com/agoda-com/api-agent)** - ⭐ 271
   Universal MCP server for GraphQL/REST APIs

1237. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 271
   Lightweight C++ MCP (Model Context Protocol) SDK

1238. **[novamira](https://github.com/use-novamira/novamira)** - ⭐ 271
   MCP server that gives AI agents full access to WordPress through PHP execution and filesystem operations

1239. **[BitFun](https://github.com/GCWing/BitFun)** - ⭐ 270
   BitFun is an Agentic Development Environment (ADE，AI IDE) featuring a cutting-edge Code Agent system with four modes — Agentic, Plan, Debug, and Review. Extensible via MCP, Skills, custom Agents and Rules. Built with Rust + TypeScript for an ultra-lightweight, fluid cross-platform experience.

1240. **[vibing-steampunk](https://github.com/oisee/vibing-steampunk)** - ⭐ 270
   vs-punk: ADT to MCP bridge - Vibe code in ABAP / AMDP

1241. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 270
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

1242. **[domain-check](https://github.com/saidutt46/domain-check)** - ⭐ 270
   Fast, universal domain availability checker - 1,200+ TLDs, pattern generation, RDAP with WHOIS fallback. CLI + Rust library + MCP server for AI agents.

1243. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 269
   Bring your project into LLM context - tool and MCP server

1244. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

1245. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 269
   A collection of MCP servers

1246. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 269
   Penpot's official MCP Server

1247. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 269
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1248. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 268
   An introduction to the world of AI Agents

1249. **[flyto-core](https://github.com/flytohub/flyto-core)** - ⭐ 268
   The open-source execution engine for AI agents. 412 modules, MCP-native, triggers, queue, versioning, metering.

1250. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 267
   A MCP server for our beloved terminal multiplexer tmux.

1251. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 267
   Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1252. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 267
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1253. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 267
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1254. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 265
   小智AI客户端，目前主要用于MCP的对接

1255. **[elementor-mcp](https://github.com/msrbuilds/elementor-mcp)** - ⭐ 265
   WordPress plugin that turns Elementor into an MCP server — 97 AI-ready tools for building, editing, and managing page designs programmatically.

1256. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 264
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

1257. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 264
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

1258. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 264
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1259. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 263
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

1260. **[ctx](https://github.com/stevesolun/ctx)** - ⭐ 263
   Skill, agent, MCP and harness recommendation engine for Claude Code/custom LLMs: walks a 13,218-node LLM wiki graph (1,968 skills, 464 agents, 10,786 MCP servers, 963K edges) and suggests the right tools on the fly.

1261. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 263
   Model Context Protocol for x64dbg & x32dbg

1262. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 262
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

1263. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 261
   AWS MCP Proxy Server

1264. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 259
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

1265. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 259
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

1266. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 259
   AI-first security scanner with 76 analyzers, 9,600+ detection rules, and repo poisoning detection for AI/ML, LLM agents, and MCP servers. Scan any GitHub repo with: medusa scan --git user/repo

1267. **[corpusos](https://github.com/Corpus-OS/corpusos)** - ⭐ 258
   Open-source protocol suite standardizing LLM, Vector, Graph, and Embedding infrastructure across LangChain, LlamaIndex, AutoGen, CrewAI, Semantic Kernel, and MCP. 3,330+ conformance tests. One protocol. Any framework. Any provider.

1268. **[agentrove](https://github.com/Mng-dev-ai/agentrove)** - ⭐ 258
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1269. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 257
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

1270. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 257
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1271. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 257
   A SEC EDGAR MCP (Model Context Protocol) Server

1272. **[bernstein](https://github.com/sipyourdrink-ltd/bernstein)** - ⭐ 257
   Deterministic orchestrator for 30+ CLI AI coding agents. Git worktree isolation, HMAC audit trail, MCP server mode.

1273. **[api200](https://github.com/API-200/api200)** - ⭐ 256
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

1274. **[swiss-ai-call-agent](https://github.com/Chrissotino/swiss-ai-call-agent)** - ⭐ 256
   Enterprise-grade AI Call Agent for the Swiss market – inbound & outbound calls, multilingual (DE/FR/IT), MCP architecture, Claude AI decision engine, real-time dashboard

1275. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 256
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1276. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 255
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

1277. **[agent-craft](https://github.com/Annyfee/agent-craft)** - ⭐ 255
   AI Agent 教学仓库 | 系统化 LangChain、RAG、LangGraph、MCP 全栈实战代码 | 万字博客详解 | 开源可运行示例 | 从零构建智能体

1278. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 255
   Zerodha Kite MCP server

1279. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 255
   Tableau's official MCP Server. Helping Agents see and understand data.

1280. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 254
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

1281. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 254
   Fast-track AI innovation with a centralized, trusted, curated registry

1282. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 253
   A code reasoning MCP server, a fork of sequential-thinking

1283. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

1284. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 253
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

1285. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 253
   Korea public data portal (data.go.kr) API MCP servers

1286. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 253
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

1287. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 252
   hydra-ai

1288. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 252
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1289. **[AgentRecall-MCP](https://github.com/Goldentrii/AgentRecall-MCP)** - ⭐ 251
   AI Session Memory with Think-Execute-Reflect Quality Loops — give your agent a brain that survives every session. Built on the Intelligent Distance principle.

1290. **[AgentRecall](https://github.com/Goldentrii/AgentRecall)** - ⭐ 250
   AI Session Memory with Think-Execute-Reflect Quality Loops — give your agent a brain that survives every session. Built on the Intelligent Distance principle.

1291. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 250
   MCP Server for ServiceNow

1292. **[vurb.ts](https://github.com/vinkius-labs/vurb.ts)** - ⭐ 250
   The TypeScript MCP framework where every AI agent finds its first action — and every action after.

1293. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 249
   MCP server implementation for Google's Gemini API

1294. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 249
   Opensource Memory for Agents

1295. **[call.md](https://github.com/video-db/call.md)** - ⭐ 249
   Turn meetings into live agent loops. Record, transcribe, and analyze meetings with real-time AI intelligence — before, during, and after calls.

1296. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 249
   Turn any MCP server into a Python module

1297. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 249
   Operating System for your personal AI Agents with Security-first approach. Multi-channel (WhatsApp, Telegram, Discord, Slack, iMessage), multi-provider (Claude, GPT, Gemini, Ollama), fully self-hosted.

1298. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 249
   pctx is the execution layer for agentic tool calls. It auto-converts agent tools and MCP servers into code that runs in secure sandboxes for token-efficient workflows.

1299. **[purple](https://github.com/erickochen/purple)** - ⭐ 249
   Open-source terminal SSH manager and SSH config editor in Rust. Fuzzy search hundreds of hosts, sync from 16 clouds, transfer files, manage Docker and Podman over SSH, sign short-lived Vault SSH certs and expose an MCP server for AI agents.

1300. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 248
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

1301. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 248
   MCP server(s) for Aipolabs ACI.dev

1302. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 248
   MCP Interface for Video Jungle

1303. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 248
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

1304. **[JoySafeter](https://github.com/jd-opensource/JoySafeter)** - ⭐ 248
   🚀 JoySafeter: An enterprise AI Agent Platform—Not just chatting. building、running、testing, and tracing autonomous Agent Teams with visual orchestration...

1305. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 248
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1306. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

1307. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

1308. **[dat](https://github.com/hexinfo/dat)** - ⭐ 247
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

1309. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 246
   An experimental MCP Server for foundry built for Solidity devs

1310. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 246
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1311. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 245
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

1312. **[mcp-dev-latam](https://github.com/codespar/mcp-dev-latam)** - ⭐ 245
   MCP servers for Brazilian services — payments, fiscal, banking, communication. Generated by CodeSpar.

1313. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 245
   The evaluation benchmark on MCP servers

1314. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1315. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 244
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

1316. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 244
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

1317. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 244
   MCP Server for Telegram

1318. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 244
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

1319. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 244
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

1320. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 244
   🔥 Model Context Protocol (MCP) server for Firebase.

1321. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 244
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1322. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 244
   Local-first RAG server for developers. Semantic + keyword search for code and technical docs. Works with MCP or CLI. Fully private, zero setup.

1323. **[embodied-claude](https://github.com/lifemate-ai/embodied-claude)** - ⭐ 243
   Claudeに身体性を与えるMCP群

1324. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 243
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1325. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 243
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1326. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 242
   Code Runner MCP Server

1327. **[lokka](https://github.com/merill/lokka)** - ⭐ 242
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1328. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 241
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

1329. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 241
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1330. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 240
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

1331. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 240
   Simplified Gemini for Claude Code. 

1332. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

1333. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 239
   Playwright MCP fork that works with Cloudflare Browser Rendering

1334. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

1335. **[Google-Research-MCP](https://github.com/mixelpixx/Google-Research-MCP)** - ⭐ 239
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1336. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 239
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1337. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 239
   Sketchup Model Context Protocol

1338. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 238

1339. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 238
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1340. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 238
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

1341. **[beever-atlas](https://github.com/Beever-AI/beever-atlas)** - ⭐ 238
   Your First LLM-Wiki Conversation Knowledge Base

1342. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 237
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1343. **[LycheeMem](https://github.com/LycheeMem/LycheeMem)** - ⭐ 237
   Lightweight Long-Term Memory for LLM Agents.

1344. **[Octopoda-OS](https://github.com/RyjoxTechnologies/Octopoda-OS)** - ⭐ 237
   The open-source memory operating system for AI agents. Persistent memory, semantic search, loop detection, agent messaging, crash recovery, and real-time observability.

1345. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 237
   MCP server for Anki via AnkiConnect

1346. **[copilot-plugins](https://github.com/github/copilot-plugins)** - ⭐ 237
   The official GitHub Copilot plugins collection — MCP servers, skills, hooks, and other extensibility tools for GitHub Copilot.

1347. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 236
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

1348. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 236
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1349. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 236
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1350. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

1351. **[claude-in-mobile](https://github.com/AlexGladkov/claude-in-mobile)** - ⭐ 235
   MCP server for mobile and desktop automation — Android (via ADB), iOS Simulator (via simctl), and Desktop (Compose Multiplatform). Like Claude in Chrome but for mobile devices and desktop apps

1352. **[agentseal](https://github.com/getagentseal/agentseal)** - ⭐ 235
   Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for supply chain attacks, test prompt injection resistance, and audit live MCP servers for tool poisoning.

1353. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 235
   💻 Give AI models complete control of your computer (probably a bad idea)

1354. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 235
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1355. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 234
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

1356. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 234
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

1357. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 233
   Securely scale AI usage across your organization.  Control plane for building, securing and monitoring your agents, mcp and skills.

1358. **[mcp-engine-public](https://github.com/maxanatsko/mcp-engine-public)** - ⭐ 233
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1359. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 233
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1360. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 233
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1361. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 232
   A Model Context Protocol (MCP) server that enables natural language queries to databases

1362. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 232
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

1363. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 232
   Creates a simple MCP tool server with "streaming" HTTP.

1364. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 232
   Autonomous SWE agent working in the cloud!

1365. **[jebmcp](https://github.com/flankerhqd/jebmcp)** - ⭐ 232

1366. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 231
   A Model Context Protocol (MCP) server for interacting with Twitter.

1367. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 230
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1368. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 230
   🧰 All-in-one domain name intelligence as a service

1369. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 230
   Model Context Protocol Servers for Milvus

1370. **[mcp-todoist](https://github.com/greirson/mcp-todoist)** - ⭐ 230
   MCP server that connects Claude to Todoist for natural language task and project   management with bulk operations

1371. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 230
   Homeassistant MCP server for 小智AI

1372. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1373. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 229
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

1374. **[sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** - ⭐ 229
   A complete list of SAP MCP Servers and SAP AI Skills

1375. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 229
   Hugging Face MCP Server

1376. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 228
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1377. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 228
   mindmap, mcp server, artifact

1378. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 228
   Penpot MCP server

1379. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 228
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1380. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 228
   Connect your AI to your APIs on Postman

1381. **[claudit-sec](https://github.com/HarmonicSecurity/claudit-sec)** - ⭐ 228
   Security audit tool for Claude Desktop and Claude Code on macOS — single-command visibility into MCP servers, extensions, plugins, connectors, scheduled tasks, and permissions.

1382. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1383. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

1384. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 227
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1385. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 226
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1386. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 226
   IMAP and SMTP via MCP Server

1387. **[agent-skills](https://github.com/jdrhyne/agent-skills)** - ⭐ 225
   A collection of AI agent skills for Clawdbot, Claude Code, Codex

1388. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 225
   Model Context Protocol server to run commands (tool: `runProcess`)

1389. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 225
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1390. **[flutter-skill](https://github.com/ai-dashboad/flutter-skill)** - ⭐ 225
   AI-powered E2E testing for 10 platforms. 253 MCP tools. Zero config. Works with Claude, Cursor, Windsurf, Copilot. Test Flutter, React Native, iOS, Android, Web, Electron, Tauri, KMP, .NET MAUI — all from natural language.

1391. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 224
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1392. **[pasal](https://github.com/ilhamfp/pasal)** - ⭐ 224
   Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + REST API + web app giving AI grounded access Indonesian laws.

1393. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 224
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1394. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 223
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1395. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 223
   A tool for autonomous agents like OpenClaw to discover and learn skills autonomously

1396. **[AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem)** - ⭐ 223
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1397. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 223

1398. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 223
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1399. **[arcticdb_mcp](https://github.com/YMuskrat/arcticdb_mcp)** - ⭐ 222
   MCP server for ArcticDB

1400. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

1401. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

1402. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

1403. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 222
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1404. **[ATaC](https://github.com/ATaC-team/ATaC)** - ⭐ 222
   Record and Replay AI Agent Trajectories.

1405. **[scrumboy](https://github.com/markrai/scrumboy)** - ⭐ 221
   Self-hosted kanban & project management with shareable boards, voice commands, sticky-notes and MCP support

1406. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

1407. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 221
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1408. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 221
   MCP stdio server for radare2

1409. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 221
   MCP server for AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends, focus-free dispatch, undo/redo, P&ID symbols, and robust IPC with ESC prefix and UTF-8 fallback. Companion agent skill: puran-water/autocad-drafting

1410. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 220
   Neo4j official MCP Server

1411. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

1412. **[mcp-dev-brasil](https://github.com/codespar/mcp-dev-brasil)** - ⭐ 219
   MCP servers for Brazilian services — payments, fiscal, banking, communication. Generated by CodeSpar.

1413. **[registry-broker-skills](https://github.com/hashgraph-online/registry-broker-skills)** - ⭐ 219
   AI agent skills for the Universal Registry - search, chat, and register 72,000+ agents across 14+ protocols. Works with Claude, Codex, Cursor, OpenClaw, and any AI assistant.

1414. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 219
   A curated list of OSINT MCP servers. Pull requests are welcomed!

1415. **[STS2-Agent](https://github.com/CharTyr/STS2-Agent)** - ⭐ 219
   杀戮尖塔2的MOD，将杀戮尖塔2的游戏状态与操作暴露为本地 HTTP API 包装成 MCP Server，供支持 MCP 的AI客户端直接调用

1416. **[solomd](https://github.com/zhitongblog/solomd)** - ⭐ 219
   A markdown editor — and the bridge to your LLM. Local-first, MIT, ~15 MB. Bundled MCP server lets Claude Code / Codex / Cursor drive your vault directly. 14 AI providers BYOK.

1417. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 218
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1418. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 218
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1419. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 217
   Razorpay's Official MCP Server

1420. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 217
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1421. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 216

1422. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 216
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1423. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 216
   🔎 A MCP server for Unsplash image search.

1424. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 216
   Tools to allow LLM clients to interact with Linux systems remotely

1425. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 215
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1426. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 215
   HeyClaude (formerly Claude Pro Directory) is a searchable collection of pre-built AI skills, agents, MCP servers, guides, hooks, statuslines, and other custom configs, designed to enhance Claude, Codex, Cursor, OpenClaw, and various other agentic workflows/platforms.

1427. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1428. **[airbroke](https://github.com/icoretech/airbroke)** - ⭐ 214
   🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher

1429. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 214
   Run and monitor MCP servers locally

1430. **[ai-code-interface.el](https://github.com/tninja/ai-code-interface.el)** - ⭐ 214
   Unified Emacs interface supporting OpenAI Codex, GitHub Copilot CLI, Claude Code, Gemini CLI, Opencode, and more

1431. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 214
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1432. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 214
   A Model Context Protocol (MCP) server providing access to Google Search Console

1433. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 214
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1434. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 213
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1435. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1436. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 213
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1437. **[harnss](https://github.com/OpenSource03/harnss)** - ⭐ 213
   Open-source, desktop client/UI build to harness Claude Code, Codex and any other Agent accepting Agent Client Protocol. Run multiple AI coding agents side by side with rich tool visualization, MCP integrations, built-in terminal, git, browser and just about anything else you may need.

1438. **[Claude-Code-AI-Design](https://github.com/Julpygo/Claude-Code-AI-Design)** - ⭐ 212
   Claude Design Anthropic Tool Download April 2026 Figma to Code AI Agent Research Preview Claude Code CLI Integration React 19 Tailwind v4 Support Model Context Protocol MCP Server Setup Design Systems Automation UI UX Prototyping Next.js Component Generation Best Developer Tools 2026 Free Tutorial

1439. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 211
   Pure Rust implementation of MCP server for headless terminal 

1440. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 211
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1441. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 211
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1442. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 211
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1443. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 211
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1444. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 210
   An MCP server to use Sora video generation APIs

1445. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1446. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1447. **[Claude-code-ChatInWindows](https://github.com/LKbaba/Claude-code-ChatInWindows)** - ⭐ 210
   Full-featured GUI for Claude Code CLI in VS Code — Windows (no WSL) & macOS. Third-party API, MCP plugins, Skills, Hooks, real-time token tracking. Actively maintained.

1448. **[open-webui-plugins](https://github.com/Classic298/open-webui-plugins)** - ⭐ 210
   A curated collection of Open WebUI plugins - tools, skills, filters, pipes, and actions that extend your AI chat experience.

1449. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 210
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1450. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 210

1451. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 210
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1452. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 210
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1453. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1454. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 209
   A ReAct-Based Highly Robust Autonomous Agent (Harness) Framework.

1455. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 209
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1456. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 208
   interactive programming of melodies, producing MIDI 

1457. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 208
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1458. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 208
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1459. **[agent-skills-hub](https://github.com/zhuyansen/agent-skills-hub)** - ⭐ 208
   Discover and compare open-source Agent Skills, tools & MCP servers — with quality scoring, trending analysis, and automated GitHub sync

1460. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 208
   Nextcloud MCP Server

1461. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 207
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1462. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 207
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1463. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 207
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1464. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 207
   Self-hosted AI RAG + MCP Platform

1465. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 207
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1466. **[facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp)** - ⭐ 207
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1467. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 207
   Supercharge AI Agents, Safely

1468. **[readwise-skills](https://github.com/readwiseio/readwise-skills)** - ⭐ 207
   Agent skills for your Readwise and Reader data, powered by the Readwise MCP server/CLI.  Triage your inbox, quiz yourself on what you've read, build a personalized now-reading page, and more.

1469. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1470. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 206
   MCP server for Dynatrace Observability

1471. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 206
   Enterprise AI Red Team Platform | 企业级AI红队平台 | 132 MCP Tools | Pure Python Engines | SDK+CLI+MCP | Auto-Download sqlmap/nuclei/ffuf | Production C2 | LLM Enhanced | Docker Sandbox | SARIF CI/CD | 1980 Tests

1472. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 206
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1473. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 206
   Google Analytics 4 data to AI agents, agentic workflows, and MCP clients. Give agents analysis-ready access to website traffic, user behavior, and performance data with schema discovery, server-side aggregation, and safe defaults that reduce data wrangling.

1474. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1475. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1476. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1477. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1478. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 205
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1479. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 205
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1480. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 205
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1481. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 205
   这是一个专为开发企业级MCP server而设计的通用开发框架

1482. **[OpenCode-Everything-You-Need-to-Know](https://github.com/wesammustafa/OpenCode-Everything-You-Need-to-Know)** - ⭐ 205
   The ultimate all-in-one guide to mastering OpenCode. From installation, Zen model router setup, TUI mastery, commands, skills, agents, workflows, automation, and integrations, to MCP servers, plugins, packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for OpenCode mastery.

1483. **[mcp-fusion](https://github.com/vinkius-labs/mcp-fusion)** - ⭐ 204
   MCP Fusion - The framework for AI-native MCP servers. 

1484. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 204
   A MCP Server for the RAG Web Browser Actor

1485. **[sap-skills](https://github.com/secondsky/sap-skills)** - ⭐ 204
   Production-ready Claude Code skills for SAP development - 35 skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more

1486. **[Corbell](https://github.com/Corbell-AI/Corbell)** - ⭐ 204
   AI-powered spec generation and review using multi-repo code graph intelligence for backend teams that ship to production.

1487. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 203
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

1488. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 202
   MCP Server for Wazuh SIEM

1489. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1490. **[CrowdSentinels-AI-MCP](https://github.com/thomasxm/CrowdSentinels-AI-MCP)** - ⭐ 202
   AI-powered threat hunting and incident response MCP server for Elasticsearch/OpenSearch

1491. **[ai-skills](https://github.com/sanjay3290/ai-skills)** - ⭐ 202
   Collection of agent skills for AI coding assistants

1492. **[designing-real-world-ai-agents-workshop](https://github.com/iusztinpaul/designing-real-world-ai-agents-workshop)** - ⭐ 202
   Hands-on workshop: Build a multi-agent AI system from scratch — Deep Research Agent + Writing Workflow served as MCP servers. Includes code, slides, and video

1493. **[cryptocurrency.cv](https://github.com/nirholas/cryptocurrency.cv)** - ⭐ 202
   Free crypto news API - real-time aggregator for Bitcoin, Ethereum, DeFi, Solana & altcoins. No API key required. RSS/Atom feeds, JSON REST API, historical archive with market context, embeddable widgets, ChatGPT plugin, Claude MCP server, SDKs (Python, TypeScript, Go, React, PHP). AI/LLM ready. Vibe coding friendly. Open source.

1494. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 201
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1495. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 201
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1496. **[shodh-memory](https://github.com/varun29ankuS/shodh-memory)** - ⭐ 201
   Cognitive memory for AI agents — learns from use, forgets what's irrelevant, strengthens what matters. Single binary, fully offline.

1497. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 201
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1498. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 201
   R MCP Server

1499. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 201
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1500. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1501. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 200
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1502. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 200
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1503. **[codefire-app](https://github.com/websitebutlers/codefire-app)** - ⭐ 200
   CodeFire gives AI coding tools persistent memory, task tracking, and project intelligence. A desktop companion for the AI-native workflow.

1504. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 200
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1505. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 199
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1506. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 199
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1507. **[ClaudeR](https://github.com/IMNMV/ClaudeR)** - ⭐ 199
   Connect RStudio to Claude Code, Codex, Gemini, and other LLM agents via MCP. Multi-agent orchestration, automated manuscript   auditing, and zero-config setup with uvx

1508. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 198
   Discord MCP Server for Claude Integration

1509. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 198
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1510. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 198
   Manage / Proxy / Secure your MCP Servers

1511. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 198
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1512. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 198
   Learn how to use MCP Servers with GitHub Copilot

1513. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 197
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1514. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 197
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1515. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 197
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1516. **[live-coding-music-mcp](https://github.com/williamzujkowski/live-coding-music-mcp)** - ⭐ 197
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1517. **[binary-ninja-headless-mcp](https://github.com/mrphrazer/binary-ninja-headless-mcp)** - ⭐ 197
   Headless Binary Ninja MCP server — giving AI agents deep reverse-engineering capabilities via 180 tools.

1518. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1519. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 196
   MCP server implementation for the UniFi network application

1520. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 196
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1521. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 196
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1522. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 196
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1523. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1524. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 195
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1525. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 195
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

1526. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 195
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1527. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 194
   Index the world's undocumented APIs

1528. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 194
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1529. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 194
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1530. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 194

1531. **[agent-graph](https://github.com/keta1930/agent-graph)** - ⭐ 194
   Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1532. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 194
   Absurdly easy Model Context Protocol Servers in Typescript

1533. **[memex](https://github.com/iamtouchskyer/memex)** - ⭐ 194
   Zettelkasten-based persistent memory for AI coding agents. Works with Claude Code, Cursor, VS Code Copilot, Codex, Windsurf & any MCP client. No vector DB — just markdown + git sync.

1534. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 194
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1535. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 193
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1536. **[Charles-mcp](https://github.com/heizaheiza/Charles-mcp)** - ⭐ 193
   Charles Proxy MCP server for AI agents with live capture, structured traffic analysis, and agent-friendly tool contracts

1537. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 193
   MCP Server for Searching Turkish Legislation

1538. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 192
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1539. **[security-investigator](https://github.com/SCStelz/security-investigator)** - ⭐ 192
   Automated security investigation tool using Microsoft MCP Servers, GitHub Copilot, Python Modules and custom copilot-instructions.

1540. **[omem](https://github.com/ourmem/omem)** - ⭐ 192
   Shared Memory That Never Forgets — persistent memory for AI agents with Space-based sharing across agents and teams. Plugins for OpenCode, Claude Code, OpenClaw, MCP Server.

1541. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 192
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1542. **[agentseal](https://github.com/AgentSeal/agentseal)** - ⭐ 191
   Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for supply chain attacks, test prompt injection resistance, and audit live MCP servers for tool poisoning.

1543. **[ida-multi-mcp](https://github.com/MeroZemory/ida-multi-mcp)** - ⭐ 191
   Multi-instance IDA Pro MCP server — analyze multiple binaries simultaneously through a single MCP endpoint.

1544. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 191
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1545. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1546. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 190
   Supabase MCP server created in Python.

1547. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 190
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1548. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 190
   This extension enables developers to implement the MCP server features easily.

1549. **[openchrome](https://github.com/shaun0927/openchrome)** - ⭐ 190
   Open-source browser automation MCP server. Control your real Chrome from any AI agent.

1550. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 190

1551. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 190
   MCP Server that enables Claude code to interact with Gemini

1552. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 190
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1553. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 189
   Chat application with multi-agents system supports multi-models and MCP

1554. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 189
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1555. **[gigabrain](https://github.com/legendaryvibecoder/gigabrain)** - ⭐ 189
   Local-first memory layer for OpenClaw, Codex App, and Codex CLI: capture, recall, dedupe, and native sync.

1556. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 189
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1557. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 189
   Official Railway MCP Server for interacting with your Railway account

1558. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 188
   Model Context Protocol Servers in Quarkus

1559. **[bear-notes-mcp](https://github.com/vasylenko/bear-notes-mcp)** - ⭐ 188
   MCP Server for Bear note taking app available as Claude Desktop extension or standalone server for any other AI tool

1560. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 188
   An MCP server to search for flights.

1561. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 188
   Skill + MCP server to turn your agent into an RLM. Load context, iterate with search/code/think tools, converge on answers.

1562. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 188
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1563. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 187
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1564. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1565. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1566. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1567. **[memov](https://github.com/memovai/memov)** - ⭐ 187
   Give git-like & traceable memory to OpenClaw and any coding agents. By https://memov.ai/ aka Entire CLI for every coding agents by MCP.

1568. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 187
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1569. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 187
   DataForSEO API modelcontextprotocol server 

1570. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 187
   MCP Server for use with Monarch Money

1571. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1572. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 186
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1573. **[notebooklm-skill](https://github.com/claude-world/notebooklm-skill)** - ⭐ 186
   NotebookLM does the research, Claude writes the content. Research → Synthesis → Content Creation → Publishing. Claude Code Skill + MCP Server.

1574. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 185
   Official Magic UI MCP server.

1575. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1576. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 185
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1577. **[docs](https://github.com/strands-agents/docs)** - ⭐ 185
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1578. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 185
   MCP for calling Siri Shorcuts from LLMs

1579. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 184
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1580. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1581. **[siconos](https://github.com/siconos/siconos)** - ⭐ 184
   Simulation framework for nonsmooth dynamical systems

1582. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 184
   MCP Server for the Bilibili API, supporting various operations.

1583. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 184
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1584. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 184
   Typescript SDK to build MCP servers in an agnostic way

1585. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 183
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1586. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 183
   Server-enforced workflow discipline for AI agents. An MCP server providing persistent work items, dependency graphs, quality gates, and actor attribution. Schemas define what agents must produce — the server blocks the call if they don't. Works with any MCP-compatible client.

1587. **[aelf-skills](https://github.com/AElfProject/aelf-skills)** - ⭐ 182
   Unified aelf skills hub for discovery, routing, bootstrap, and health checks across OpenClaw, Codex, Cursor, and Claude Code.

1588. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1589. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1590. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 182
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1591. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 182
   Examples of using Pipedream's MCP server in your app or AI agent.

1592. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 182
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1593. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 182
   A simple CLI to install MCP servers into any client - auth included!

1594. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 182

1595. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 182
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1596. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 182
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

1597. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 181
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1598. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 181
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1599. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 180
   Official MCP server for Tripo

1600. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 180
   Safe local execution layer for AI agent tools. Build, validate, and publish MCP tools with a no-pass-no-run workflow — cross-platform desktop app powered by Spring AI.

1601. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 180
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1602. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 180
   An MCP server for Anki

1603. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 180
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1604. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 180
   Python SDK for interacting with the MCP Toolbox for Databases. 

1605. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 180
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1606. **[comfy-pilot](https://github.com/ConstantineB6/comfy-pilot)** - ⭐ 180
   MCP server + embedded terminal that lets Claude Code see and edit your ComfyUI workflows

1607. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 180
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1608. **[dario](https://github.com/askalf/dario)** - ⭐ 180
   Local LLM router. One endpoint for Claude Max/Pro, OpenAI, OpenRouter, Groq, Ollama, LiteLLM, any OpenAI-compat URL — your tools don't need to change. OAuth for Claude subscriptions, multi-account pool, MCP server. Zero runtime deps.

1609. **[cachebro](https://github.com/glommer/cachebro)** - ⭐ 179
   File cache with diff tracking for AI coding agents. Drop-in MCP server that cuts token usage by 26%.

1610. **[xiaoi](https://github.com/xvhuan/xiaoi)** - ⭐ 179
   小爱音箱语音通知工具：提供 CLI/TUI/MCP/Webhook 一键播报与控制音量，支持 PM2 常驻部署，支持docker部署。

1611. **[icm](https://github.com/rtk-ai/icm)** - ⭐ 179
   Permanent memory for AI agents. Single binary, zero dependencies, MCP native.

1612. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 179
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1613. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 179
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1614. **[figma-mcp-bridge](https://github.com/gethopp/figma-mcp-bridge)** - ⭐ 179
   Figma Plugin & MCP server to bypass API limits

1615. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 179
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1616. **[lumen](https://github.com/ory/lumen)** - ⭐ 179
   Reduce Claude Code, Codex, OpenCode wall clock and token use by 50% with open source, local semantic search. Works for small and large codebases and monorepos! Enterprise-ready and fully compliant via Ollama and SQLite-vec.

1617. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1618. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1619. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 178
   A MCP server to search for accurate academic articles.

1620. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 178
   Revornix is an open-source, local-first AI information/markdown workspace. It helps you collect fragmented inputs, turn them into structured knowledge, generate reports with images and podcast audio, and deliver the output through automated notifications.

1621. **[bernstein](https://github.com/chernistry/bernstein)** - ⭐ 178
   Deterministic orchestrator for 30+ CLI AI coding agents. Git worktree isolation, HMAC audit trail, MCP server mode.

1622. **[android-skills-mcp](https://github.com/skydoves/android-skills-mcp)** - ⭐ 178
   An MCP server and CLI packager for official Android skills.

1623. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 177

1624. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 177
   A redmine MCP server covering close to 100% of redmines API

1625. **[PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio)** - ⭐ 177
   Free, open-source SQL Server execution plan analyzer — cross-platform GUI + CLI with 30 analysis rules, missing index detection, SSMS extension. Built-in MCP server for AI-assisted plan review.

1626. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 177
   📜 An MCP server for conversation history search and retrieval in Claude Code

1627. **[LeanKG](https://github.com/FreePeak/LeanKG)** - ⭐ 177
   LeanKG: Stop Burning Tokens. Start Coding Lean.

1628. **[dataseo-mcp](https://github.com/egebese/dataseo-mcp)** - ⭐ 177
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1629. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 176
   MCP Server for Google Slides

1630. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 176
   MCP Server for Postgres

1631. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 176
   MCP Salesforce connector

1632. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 175
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1633. **[Companion](https://github.com/mattt/Companion)** - ⭐ 175
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1634. **[aghub](https://github.com/AkaraChen/aghub)** - ⭐ 175
   One hub for every AI coding agent. Unified configuration management for 22+ assistants.

1635. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 175
   MCP server to work with Telegram through MTProto

1636. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 175
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1637. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 175
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1638. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 175
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1639. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 175
   Open source version of Claude Managed Agents. Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent.

1640. **[renderdoc-mcp](https://github.com/JiaboLi-GitHub/renderdoc-mcp)** - ⭐ 175
   An MCP server for RenderDoc: Empowering AI assistants to analyze GPU frame captures and debug graphics pipelines.

1641. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 174
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1642. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 174
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1643. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 174
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1644. **[command](https://github.com/scopecraft/command)** - ⭐ 174
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1645. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 173
   Turn any website or doc into an MCP server

1646. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 173

1647. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 173
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1648. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 172
   A mongo db server for the model context protocol (MCP)

1649. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 172
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1650. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 172
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1651. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 172
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1652. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 172
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1653. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 172
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1654. **[clix](https://github.com/spideystreet/clix)** - ⭐ 171
   X from terminal. No API keys needed. Just plug your AI Agent.

1655. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 171
   One MCP Server, All Your Apps, Privacy First

1656. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 171
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1657. **[PolyMCP](https://github.com/poly-mcp/PolyMCP)** - ⭐ 171
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1658. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 171
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1659. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 171
   Codex Mcp Server 

1660. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 170
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1661. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1662. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 170
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1663. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 170
   Turn a web server into an MCP server in one click without making any code changes.

1664. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 170
   Model Context Protocol For R

1665. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 170
   MCPSDK.dev(ToolSDK.ai)'s Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1666. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 170
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

1667. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 170
   The AI Operating System for Delphi. 100% native framework with RAG 2.0, autonomous agents, MCP protocol, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Delphi 10.4+ (limited), full support from Delphi 12 Athens.

1668. **[godot-ai](https://github.com/hi-godot/godot-ai)** - ⭐ 170
   Production-grade MCP server and AI tools for the Godot engine. Community project, not affiliated with the Godot Foundation.

1669. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 169
   AI-powered security operations for Wazuh SIEM—use any MCP-compatible client to ask security questions in plain English. Faster threat detection, incident triage, and compliance checks with real-time monitoring and anomaly spotting. Production-ready MCP server for conversational SOC workflows.

1670. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 169
   A Tiny Web Chat App for AI Models with MCP Client Support

1671. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 169
   Local-first MCP App framework for ChatGPT Apps, Claude, and more.

1672. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 169
   Command line interface for MCP clients with secure execution and customizable security policies

1673. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 169
   StarRocks MCP (Model Context Protocol) Server

1674. **[sibyl-research-system](https://github.com/Sibyl-Research-Team/sibyl-research-system)** - ⭐ 168
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1675. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 168
   c4 GenAI Suite

1676. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 168
   WeChat-MCP: let Openclaw/Claude/ChatGPT and other AI assistants read and reply to WeChat for you

1677. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 168
    QMT-MCP 模块化量化交易助手

1678. **[refref](https://github.com/amicalhq/refref)** - ⭐ 167
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1679. **[agnix](https://github.com/agent-sh/agnix)** - ⭐ 167
   The missing linter and lsp for AI coding assistants. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP. Plugin for all major IDEs included, with autofixes.

1680. **[ironcurtain](https://github.com/provos/ironcurtain)** - ⭐ 167
   A secure* runtime for autonomous AI agents. Policy from plain-English constitutions. (*https://ironcurtain.dev)

1681. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 166
   A desktop application that adds powerful tools to Claude and AI platforms

1682. **[CyberStrike](https://github.com/CyberStrikeus/CyberStrike)** - ⭐ 166
   AI-powered offensive security agent. Autonomous pentesting with 13+ specialized agents, 120+ OWASP test cases, 15+ LLM providers, and Bolt remote tool servers. Your AI red team.

1683. **[data-verify-mcp](https://github.com/CCCpan/data-verify-mcp)** - ⭐ 166
   中国数据核验 MCP Server | 身份核验/企业查询/车辆信息/OCR识别/风险评估 | 10个Tool覆盖5大类 | 微信: chenganp | 邮箱: 345048305@qq.com

1684. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 166
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1685. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 166
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1686. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 166
   MariaDB MCP (Model Context Protocol) server implementation

1687. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 166
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1688. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 166
   Persistent Intelligence Infrastructure for AI Agents

1689. **[knowledge-base-server](https://github.com/willynikes2/knowledge-base-server)** - ⭐ 166
   Make every AI agent you use smarter. Persistent memory with SQLite FTS5, MCP server, Obsidian sync, and self-learning intelligence pipeline.

1690. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 165
   MCP server for searching and querying PubMed medical papers/research database

1691. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 165
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1692. **[ai-polymarket-agent](https://github.com/kaktusesquire6rmu/ai-polymarket-agent)** - ⭐ 165
   Enable Claude, ChatGPT, and other AI agents to analyze markets, fetch real-time odds, and execute trades on Polymarket using the Model Context Protocol (MCP).

1693. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 164
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1694. **[recall](https://github.com/joseairosa/recall)** - ⭐ 164
   Persistent cross-session memory for Claude & AI agents. Self-host on Redis/Valkey, or use the managed SaaS at recallmcp.com.

1695. **[Axon.MCP.Server](https://github.com/ali-kamali/Axon.MCP.Server)** - ⭐ 164
   Transform your codebase into an intelligent knowledge base for AI-powered development with Cursor IDE, Google AntiGravity, and MCP-enabled assistants

1696. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 164
   MCP server for Mikrotik

1697. **[domscribe](https://github.com/patchorbit/domscribe)** - ⭐ 164
   Domscribe is a pixel-to-code development tool that bridges the gap between running web applications and their source code.

1698. **[mcp-codex-dev](https://github.com/FYZAFH/mcp-codex-dev)** - ⭐ 163
   MCP Server for Codex CLI integration - stateful code writing and review workflows

1699. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 163

1700. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 163
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1701. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 163
   MCP Server and CLI for Apache Spark History Server. Debug Spark applications from AI agents, scripts, or the terminal.

1702. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 163
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1703. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 162
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1704. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 162
   Model Context Protocol (MCP) server for constraint optimization and solving"

1705. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 162
   Vector-search powered agent memory MCP server

1706. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 162
   小红书MCP服务器 | 秒级工具调用执行，笔记用户搜索、通知消息监控等；打造2026最简单、最快速、最精准、最好用的小红书MCPServer！

1707. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 162
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1708. **[turbo-flow](https://github.com/marcuspat/turbo-flow)** - ⭐ 162
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI subagents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1709. **[mengram](https://github.com/alibaizhanov/mengram)** - ⭐ 162
   Human-like memory for AI agents — semantic, episodic & procedural. Experience-driven procedures that learn from failures. Free API, Python & JS SDKs, LangChain, CrewAI & OpenClaw integrations.

1710. **[jdocmunch-mcp](https://github.com/jgravelle/jdocmunch-mcp)** - ⭐ 162
   The leading, most token-efficient MCP server for documentation exploration and retrieval via structured section indexing

1711. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1712. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 161
   MCP Server for AI Summarization

1713. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 161
   Instagram Direct messages MCP

1714. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 161
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1715. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 161

1716. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 161
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1717. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 161
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1718. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 160
   Scrapeless Mcp Server

1719. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 160
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1720. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 160
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1721. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 160
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1722. **[awesome-ai-for-economists](https://github.com/hanlulong/awesome-ai-for-economists)** - ⭐ 160
   A curated list of AI tools, libraries, and resources for economics research, teaching, and policy analysis. Maintained by the OpenEcon team.

1723. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 160
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1724. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 160
   Simple Slackbot MCP Client

1725. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 160
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1726. **[mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** - ⭐ 160
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1727. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 160
   MCP Server for connecting to the Meta Marketing API

1728. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 160
   Isaac Simulation MCP Extension and Server

1729. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 160

1730. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 159
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1731. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 159
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1732. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 159
   A Model Context Protocol server for Hopper Disassembler

1733. **[affine-mcp-server](https://github.com/DAWNCR0W/affine-mcp-server)** - ⭐ 159
   Model Context Protocol server for AFFiNE. Connect AI assistants to AFFiNE workspaces, documents, databases, and collaboration APIs over stdio or HTTP.

1734. **[claude-code-open](https://github.com/kill136/claude-code-open)** - ⭐ 158
   Open source AI coding platform with Web IDE, multi-agent system, 37+ tools, MCP protocol. MIT licensed.

1735. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 158
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1736. **[QuickDesk](https://github.com/barry-ran/QuickDesk)** - ⭐ 158
   QuickDesk is the first AI-native remote desktop — an open-source, free application with a built-in MCP (Model Context Protocol) Server that lets any AI agent see and control remote computers.

1737. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 158
   MCP server that provides access to Chinese stock market data using akshare-one

1738. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 157
   A Model Context Protocol server for MySQL database operations

1739. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 157
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1740. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 157
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1741. **[bocha-search-mcp](https://github.com/BochaAI/bocha-search-mcp)** - ⭐ 157
   Bocha Search MCP Server.

1742. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 156
   An MCP server for fetching URLs / Youtube video transcript.

1743. **[refref](https://github.com/refrefhq/refref)** - ⭐ 156
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1744. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 156

1745. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 156
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1746. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 156
   Make MCP Server

1747. **[mcp-bridge](https://github.com/firekula/mcp-bridge)** - ⭐ 156
   这是一个为 Cocos Creator 设计的 MCP (Model Context Protocol) 桥接插件，用于连接外部 AI 工具与 Cocos Creator 编辑器，实现对场景、节点等资源的自动化操作。

1748. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 155
   ChatGPT Copilot Extension for Visual Studio Code

1749. **[payram-mcp](https://github.com/PayRam/payram-mcp)** - ⭐ 155
   Connect to hosted payram helper at: https://mcp.payram.com

1750. **[AI-company](https://github.com/CronusL-1141/AI-company)** - ⭐ 155
   AI Team OS — Multi-Agent Team Operating System for Claude Code. 40+ MCP tools, 22 agent templates, task wall, meeting system, dashboard.

1751. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 155
   Deep Research for crypto - free & fully local

1752. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 155
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1753. **[hanzi-browse](https://github.com/hanzili/hanzi-browse)** - ⭐ 155
   let any ai agent use the local browser

1754. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 155
   Salesforce MCP Server

1755. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 154
   A simple MCP server to search for documentation (tutorial)

1756. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 154
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1757. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 154
   A simple and performant Model Context Protocol framework for Python.

1758. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 154
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1759. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 153
   :octocat: GitHub Emoji for C#, dotnet and beyond

1760. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 153
   Manage Your Kubernetes Cluster with k8s mcp-server

1761. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 153
   An MCP Server for Ollama

1762. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 153
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1763. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 152
   A gateway demo for MCP SSE Server

1764. **[agentanycast](https://github.com/AgentAnycast/agentanycast)** - ⭐ 152
   Connect AI agents across any network — zero config, encrypted, skill-based routing

1765. **[claude-code-karma](https://github.com/JayantDevkar/claude-code-karma)** - ⭐ 152
   Dashboard for monitoring claude code sessions. 

1766. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 152
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1767. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 152
   Dynamically expose tools from proxied servers based on an Agent Persona

1768. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 152
   MCP server for discord bot

1769. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 151
   MCP server for Unreal Engine 5

1770. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 151
   Toolkit for Coding Agents to work reliably with repo of any size.

1771. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 151
   MCP Server for using any LLM as a Tool

1772. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 151
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1773. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 151
   Catch MCP server issues before your agents do.

1774. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 151
   Serper MCP Server supporting search and webpage scraping

1775. **[eion](https://github.com/eiondb/eion)** - ⭐ 151
   Shared Memory Storage for Multi-Agent Systems

1776. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 151
   Model Context Protocol (MCP) with TikTok integration

1777. **[relay](https://github.com/prism-php/relay)** - ⭐ 150
   An MCP client tool for Prism

1778. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1779. **[aai-gateway](https://github.com/gybob/aai-gateway)** - ⭐ 150
   Install MCP servers and skills once, share across all your AI agents — with 90% less context overhead.

1780. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 150
   MCP server to download entire websites

1781. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 150
   Let LLMs control embedded devices via the Model Context Protocol.

1782. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 150
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1783. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 150
   Connect any Open Data to any LLM with Model Context Protocol.

1784. **[ProxmoxMCP-Plus](https://github.com/RekklesNA/ProxmoxMCP-Plus)** - ⭐ 150
   Use MCP and OpenAPI to safely control Proxmox VE VMs, LXCs, backups, and snapshots from LLMs and AI agents.

1785. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 150
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1786. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 149
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1787. **[Express-REST-API-and-MCP-Server-Framework](https://github.com/iolufemi/Express-REST-API-and-MCP-Server-Framework)** - ⭐ 149
   Express REST API and MCP Server Framework is a comprehensive development framework for building RESTful APIs and MCP servers with Express.js. It provides a complete template for creating production-ready APIs using Node.js, Express, Mongoose (MongoDB), and Sequelize (SQL databases).

1788. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 149
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1789. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 149
   Enable AI Agents to Control Unity

1790. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 149
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1791. **[regenerator2000](https://github.com/ricardoquesada/regenerator2000)** - ⭐ 149
   An interactive disassembler for the CPU 6502, focused mostly on Commodore 8-bit computers. Features a TUI with modern features like x-ref, undo/redo, arrows, keyboard-driven, mcp server, VICE debugger and more!

1792. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 149
   MCP server for interaction with Bitwarden.

1793. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 149
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1794. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 149
   A Model Context Protocol server for calculating.

1795. **[Gopeak-godot-mcp](https://github.com/HaD0Yun/Gopeak-godot-mcp)** - ⭐ 149
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

1796. **[eclipse-chatgpt-plugin](https://github.com/gradusnikov/eclipse-chatgpt-plugin)** - ⭐ 149
   Eclipse IDE as an MCP Server for AI Agents

1797. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 149
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1798. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 148
   Desktop APP for Discover and Install MCP Servers

1799. **[plan-cascade](https://github.com/Taoidle/plan-cascade)** - ⭐ 148
   AI-powered cascading development framework. Decompose complex projects into parallel executable tasks with auto-generated PRDs, design docs, and multi-agent collaboration (Claude Code, Codex, Aider).

1800. **[kom](https://github.com/weibaohui/kom)** - ⭐ 148
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1801. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 148
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1802. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 148
   Raindrop MCP Server

1803. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 148
   MCP Server connecting to Perplexity Comet browser

1804. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 148
   A PubMed MCP server.

1805. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 148
   Model Context Protocol server implementation for Figma API

1806. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 148
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1807. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 148
   Model Context Protocol (MCP) server for the Zotero API, in Python

1808. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 148
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1809. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 148
   Async Python client for the Model Context Protocol with interactive CLI and reactive Web UI, connecting AI models to MCP servers via stdio and SSE

1810. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 148
   Model Context Protocol Server for Swift

1811. **[meta_skill](https://github.com/Dicklesworthstone/meta_skill)** - ⭐ 147
   Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic search, bandit-optimized suggestions, and MCP integration

1812. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 147
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1813. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 147
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1814. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 146
   An MCP server that provides access to Postman.

1815. **[openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions)** - ⭐ 146
   A collection of enhancements, plugins, and prompts for Open WebUI, developed and curated for personal use to extend functionality and improve experience.

1816. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 146
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1817. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 146
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1818. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust 

1819. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 145
   MSSQL Server MCP implementation written in C#

1820. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 145
   Comprehensive MCP server exposing dozens of capabilities to AI agents: multi-provider LLM delegation, browser automation, document processing, vector ops, and cognitive memory systems

1821. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 145
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12+.

1822. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 145
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1823. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 144
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1824. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 144
   A MCP Server for creating Powerpoint Presentations

1825. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

1826. **[godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** - ⭐ 144
   MCP server for full Godot 4.x engine control — 149 tools for AI-driven game development

1827. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 143
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1828. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 143
   MCP server implementation for Google's Gemini API

1829. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

1830. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 143
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1831. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 143
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1832. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 143
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1833. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 142
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1834. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 142
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1835. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1836. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 142
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1837. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 142
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1838. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1839. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 141
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1840. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 141
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1841. **[antigravity-link-extension](https://github.com/cafeTechne/antigravity-link-extension)** - ⭐ 141
   Mobile companion for Google's Antigravity IDE. Mirror AI sessions on your phone, send messages, stop generation, automate via 9 MCP tools or OpenAPI.

1842. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 141
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1843. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 141
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, Slides and Calendar. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

1844. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 141
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1845. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 140
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1846. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 140

1847. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 140
   MCP server for Israel Government Data

1848. **[linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server)** - ⭐ 140
   🔗 A Model Context Protocol (MCP) server for LinkedIn — search people, companies, and jobs, scrape profiles, and get structured data via any MCP-compatible AI client.

1849. **[unity-mcp-server](https://github.com/AnkleBreaker-Studio/unity-mcp-server)** - ⭐ 140
   Unity MCP Server — 268 tools for AI-assisted game development. Connect Claude, Cursor, or any MCP client to Unity Editor & Unity Hub. Scene management, GameObjects, components, builds, profiling, Shader Graph, Amplify, terrain, physics, NavMesh, animation, MPPM multiplayer & more. Free & open source by AnkleBreaker Studio.

1850. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 139
   Graphiti MCP Server

1851. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 139
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1852. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 139
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1853. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 139
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

1854. **[forgemax](https://github.com/postrv/forgemax)** - ⭐ 139
   Code Mode inspired local sandboxed MCP Gateway - collapses N servers x M tools into 2 tools (~1,000 tokens)

1855. **[reddit-mcp-server](https://github.com/eliasbiondo/reddit-mcp-server)** - ⭐ 139
   🔗 A zero-config Model Context Protocol (MCP) server for Reddit — search posts, browse subreddits, scrape user activity, and get structured data via any MCP-compatible AI client. No API keys or authentication needed.

1856. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 138
   Simple MCP Server Implementation

1857. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 138
   MCP server for seamless document format conversion and processing

1858. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 138
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1859. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 138
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1860. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 138
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1861. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 138
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1862. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 138
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1863. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 137
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1864. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 137
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1865. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 137
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1866. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 137
   mcp server for gitingest

1867. **[resolve-mcp](https://github.com/barckley75/resolve-mcp)** - ⭐ 137
   Connect DaVinci Resolve Studio to Claude AI through the Model Context Protocol (MCP)

1868. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 136
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

1869. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 136
      Convert any MCP server into a Claude Skill with 90% context savings

1870. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 136
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

1871. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 136
   Excel MCP Server & CLI - 23 tools, 214 operations for AI-powered Excel automation via COM API

1872. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 135
   Simple API & React framework, fully type safe, OpenAPI, RSC, MCP, type safe client, streaming with SSE

1873. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 135
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1874. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 135
   MCP server for interacting with the Aseprite API

1875. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 135
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1876. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 135
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1877. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 134
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1878. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1879. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 134
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1880. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 134
   A powerful MCP server for intelligently reading Java source code (For Jar and local project).

1881. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 134
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1882. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 134
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1883. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1884. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1885. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 133
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1886. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 133
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1887. **[charlotte](https://github.com/TickTockBent/charlotte)** - ⭐ 133
   Token-efficient browser MCP server — structured web pages for AI agents, not raw accessibility dumps

1888. **[claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** - ⭐ 133
   Claudeus WordPress MCP Server

1889. **[VibeUE](https://github.com/kevinpbuckley/VibeUE)** - ⭐ 133
   Unreal Engine Vibe Coding tool

1890. **[magg](https://github.com/sitbon/magg)** - ⭐ 133
   Magg: The MCP Aggregator

1891. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 133
   Model Context Protocol for Actual Budget API

1892. **[firefox-devtools-mcp](https://github.com/mozilla/firefox-devtools-mcp)** - ⭐ 133
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

1893. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 132
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1894. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 132
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1895. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 132
   Docker Hub MCP Server

1896. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 132
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

1897. **[orchestkit](https://github.com/yonatangross/orchestkit)** - ⭐ 132
   The Complete AI Development Toolkit for Claude Code — 89 skills, 31 agents, 99 hooks. Production-ready patterns for full-stack development.

1898. **[mcp-ts-core](https://github.com/cyanheads/mcp-ts-core)** - ⭐ 132
   Agent-native TypeScript framework for building MCP servers. Declarative definitions with auth, multi-backend storage, OpenTelemetry, and first-class support for Bun/Node/Cloudflare Workers.

1899. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 132
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1900. **[yuque-mcp-server](https://github.com/yuque/yuque-mcp-server)** - ⭐ 132
   Yuque MCP Server - Model Context Protocol server for Yuque API

1901. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 132
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1902. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 131

1903. **[ClawMem](https://github.com/yoloshii/ClawMem)** - ⭐ 131
   On-device memory layer for AI agents. Claude Code, Hermes and OpenClaw. Hooks + MCP server + hybrid RAG search.

1904. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 131
   blazigly fast gRPC/MCP client & server implementation in zig

1905. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 131
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1906. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 130
   BrowserStack's Official MCP Server

1907. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 130
   High-performance CCXT MCP server for cryptocurrency exchange integration

1908. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 130
   It's time to push beyond MCP Servers... Right?

1909. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 130
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1910. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 130
   A Google Tasks Model Context Protocol Server for Claude

1911. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 129
   A modular MCP server that provides commonly used developer tools for AI coding agents

1912. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 129
   A collection of crypto MCP servers.

1913. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 129
   Conversion from Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines, and autonomous Excel reading and writing by AI agents through MCP integration.

1914. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 129
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

1915. **[indonesia-gov-apis](https://github.com/suryast/indonesia-gov-apis)** - ⭐ 129
   🇮🇩 50+ Indonesian Government APIs & Data Sources — BPS, OJK, BPJPH, BPOM, Bank Indonesia, IDX, BMKG + MCP servers. Python examples, scraping patterns, and practical gotchas.

1916. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 129
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1917. **[prism-mcp](https://github.com/dcostenco/prism-mcp)** - ⭐ 129
   The Mind Palace for AI Agents - HIPAA-hardened Cognitive Architecture with on-device LLM (prism-coder:7b), Hebbian learning, ACT-R spreading activation, adversarial evaluation, persistent memory, multi-agent Hivemind and visual dashboard. Zero API keys required.

1918. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 128
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1919. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1920. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 128
   Intelligent spec workflow management MCP server

1921. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 128
   a private MCP server for accessing Linear

1922. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 128
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1923. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1924. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 128
   A Model Context Protocol (MCP) for Jupyter Notebook

1925. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 128
   Buttplug.io Model Context Protocol (MCP) Server

1926. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 128
   A Model Context Protocol Server to manipulate *.xcodeproj

1927. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 128
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1928. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 128
   Model Context Protocol (MCP) server for the Webflow Data API.

1929. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1930. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

1931. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 127
   Portainer MCP server

1932. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 127
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

1933. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 127
   MCP server for understanding AWS spend

1934. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 127
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1935. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 126
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1936. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 126
   Dart AI Model Context Protocol (MCP) server

1937. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1938. **[sysplant](https://github.com/x42en/sysplant)** - ⭐ 126
   Your Windows syscall hooking factory - feat Canterlot's Gate - All accessible over MCP

1939. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 126
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1940. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 126
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1941. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 126
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1942. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1943. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 125
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1944. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 125
   unofficial mcp server for cloudflare api

1945. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 125
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

1946. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 125
   A Model Context Protocol server that provides access to BigQuery

1947. **[rails-ai-context](https://github.com/crisnahine/rails-ai-context)** - ⭐ 125
   38 MCP tools that give AI agents live access to your Rails schema, models, routes & conventions. Works with Claude Code, Cursor, Copilot, OpenCode, Codex CLI. Zero config.

1948. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 125
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1949. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 125
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1950. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1951. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 124
   🐉 The fast, PHP way to build MCP servers

1952. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 124
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1953. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 124
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1954. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 124
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under  MIT License.

1955. **[gm-exec](https://github.com/AnEntrypoint/gm-exec)** - ⭐ 123
   wanna develop an app ❓

1956. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 123
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1957. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 123
   wanna develop an app ❓

1958. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 123
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1959. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 123
   MCP server for Google Tag Manager

1960. **[ASI](https://github.com/vNeeL-code/ASI)** - ⭐ 123
   Android ✧ Gemma Integration into Android System Intelligence

1961. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 123
   MCP server for Shodan — search internet-connected devices, IP reconnaissance, DNS lookups, and CVE/CPE vulnerability intelligence. Works with Claude Code, Codex, Gemini CLI, and Claude Desktop.

1962. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 123
   MCP server for token-efficient large document analysis via the use of REPL state

1963. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 123
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1964. **[mcp-gm](https://github.com/AnEntrypoint/mcp-gm)** - ⭐ 122
   wanna develop an app ❓

1965. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 122
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

1966. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 122
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1967. **[env-doctor](https://github.com/mitulgarg/env-doctor)** - ⭐ 122
   Debug your GPU, CUDA, and AI stacks across local, Docker, and CI/CD (CLI and MCP server)

1968. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 122
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1969. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 122
   An MCP server that provides LLMs with the latest stable package versions when coding

1970. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 122
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1971. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 122
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1972. **[mcp](https://github.com/taskade/mcp)** - ⭐ 122
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1973. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 122
   MCP server for *arr media management suite

1974. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 121
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1975. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1976. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 121
   MCP server implementation for n8n workflow automation

1977. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 121

1978. **[mcp-hubspot](https://github.com/baryhuang/mcp-hubspot)** - ⭐ 121
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1979. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 121
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via CLI wrappers

1980. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

1981. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 120
   Google Sheets MCP Server 📊🤖

1982. **[mcp](https://github.com/frappe/mcp)** - ⭐ 120
   Frappe MCP allows Frappe apps to function as MCP servers

1983. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 120
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1984. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 120
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1985. **[Pare](https://github.com/Dave-London/Pare)** - ⭐ 120
   Dev tools, optimized for agents. Structured, token-efficient MCP servers for git, test runners, npm, Docker, and more.

1986. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 120
   A proxy to use HTTP/SSE MCPs from STDIO clients

1987. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 120
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1988. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 119

1989. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 119
   TypeScript template for building Model Context Protocol (MCP) servers. Ships with declarative tools/resources, pluggable auth, multi-backend storage, OpenTelemetry observability, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1990. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 119
   MCP server for VirusTotal API — analyze URLs, files, IPs, and domains with comprehensive security reports, relationship analysis, and pagination support.

1991. **[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)** - ⭐ 119
   Curated awesome list for OpenClaw (formerly Moltbot/Clawdbot): skills, plugins, memory systems, MCP tools, deployment stacks, ecosystem platforms, and developer tooling.

1992. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 119
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1993. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 119
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1994. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

1995. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 118
   MCP Server for PolyMarket API

1996. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 118
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

1997. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 118
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1998. **[nitrostack](https://github.com/nitrocloudofficial/nitrostack)** - ⭐ 118
   The full-stack TypeScript framework to build, test, and deploy production-ready MCP servers and AI-native apps.

1999. **[MiniClaw](https://github.com/8421bit/MiniClaw)** - ⭐ 118
   🦞 A Digital Life Embryo for your MCP Client. An intelligent micro-kernel with Nociception, Memory Apoptosis, and a Curiosity Drive. Evolve your AI Copilot into a sentient partner for Claude Desktop, Qoderwork, Cursor, and beyond.

2000. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 117
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

2001. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 117
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

2002. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 117
   An MCP server for InterviewReady

2003. **[kodit](https://github.com/helixml/kodit)** - ⭐ 117
   👩‍💻 MCP server to index external repositories

2004. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 117
   It's an MCP server... for Outline (the documentation platform!)

2005. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 117
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

2006. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 117
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

2007. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 117
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

2008. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 116
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

2009. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 116
   MCP for 1C:EDT

2010. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 115
   Fast and super efficient Minecraft Server written in C++

2011. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 115
   Azure API Management as AI Gateway to Remote MCP servers.

2012. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 115
   MCP Server for working with large Oracle databases

2013. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 115
   Getting Started with Remote MCP Servers using Azure Functions (Python)

2014. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 115
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search, News Search and LLM Context Search capabilities

2015. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 115
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

2016. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 115
   From Java Dev to AI Engineer: Spring AI Fast Track

2017. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 114
   Swagger to MCP server

2018. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 114
   Foxy contexts is a library for building context servers supporting Model Context Protocol

2019. **[modex](https://github.com/theronic/modex)** - ⭐ 114
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

2020. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 114
   Native Delphi Server implementation of the Model Context Protocol (MCP)

2021. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 113
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

2022. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

2023. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

2024. **[AgenticGoKit](https://github.com/AgenticGoKit/AgenticGoKit)** - ⭐ 113
   Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent agents. LLM-agnostic, event-driven, with multi-agent workflows, MCP tool discovery, and production-grade observability.

2025. **[mcp-armor](https://github.com/aira-security/mcp-armor)** - ⭐ 113
   MCP Armor continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

2026. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 113
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

2027. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 113
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

2028. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

2029. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 112
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

2030. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 112

2031. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 112
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

2032. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 112
   Rails Engine with MCP compliant Spec.

2033. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 112
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

2034. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

2035. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

2036. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

2037. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

2038. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

2039. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 111

2040. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 111
   Open Source MCP Servers for Scientific Research

2041. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 111
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

2042. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 111
   MCP for semantic code search & navigation that reduces token waste

2043. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 111
   Headless IDA Pro binary analysis via Model Context Protocol

2044. **[mcp-dock](https://github.com/OldJii/mcp-dock)** - ⭐ 110
   A cross-platform MCP Server manager for Cursor, Claude, Windsurf, Zed & TRAE. Features one-click installation, multi-client sync, and a curated registry of Official & Smithery servers.

2045. **[MySearch-Proxy](https://github.com/skernelx/MySearch-Proxy)** - ⭐ 110
   Unified search MCP, proxy console, and skill for Tavily, Firecrawl, and Social / X.

2046. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 110
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

2047. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

2048. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

2049. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 110
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

2050. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 110
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

2051. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 110
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

2052. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 110
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

2053. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 110
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

2054. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 109
   MCP Client Implementation using Python, LangGraph and Gemini

2055. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

2056. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

2057. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 109
   The coding agent for professionals

2058. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 109
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

2059. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 109
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

2060. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 109
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

2061. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 109
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2062. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 109
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

2063. **[adloop](https://github.com/kLOsk/adloop)** - ⭐ 109
   An MCP server that gives your AI assistant read + write access to Google Ads and GA4 — with safety guardrails that prevent accidental spend.

2064. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 109
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

2065. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 109
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

2066. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

2067. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

2068. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

2069. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 108
   An MCP client for Node.js.

2070. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 108
   Payload CMS MCP Server

2071. **[forge-orchestrator](https://github.com/nxtg-ai/forge-orchestrator)** - ⭐ 108
   Forge Orchestrator: Multi-AI task orchestration. File locking, knowledge capture, drift detection. Rust.

2072. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 108
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

2073. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 108
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

2074. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 108
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

2075. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 108
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

2076. **[Alicization-Town](https://github.com/ceresOPA/Alicization-Town)** - ⭐ 108
    **⚔️ Alicization Town** is a decentralized, multi-agent pixel sandbox world powered by the **Model Context Protocol (MCP)**.    **⚔️ Alicization Town** 是一个基于 **MCP (Model Context Protocol)** 架构的去中心化多智能体像素沙盒世界。

2077. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 108
   Safe local execution layer for AI agent tools. Build, validate, and publish MCP tools with a no-pass-no-run workflow — cross-platform desktop app powered by Spring AI.

2078. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 107
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

2079. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

2080. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

2081. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 107
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

2082. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 107
   fast, secure c# runner

2083. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 107
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

2084. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 107
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

2085. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 107
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

2086. **[winremote-mcp](https://github.com/dddabtc/winremote-mcp)** - ⭐ 107
   Windows Remote MCP Server — 40+ tools for desktop automation, process management, file operations via FastMCP

2087. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 107
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

2088. **[obsidian-web-mcp](https://github.com/jimprosser/obsidian-web-mcp)** - ⭐ 107
   Secure remote MCP server for Obsidian vaults -- access your notes from Claude, your phone, or any MCP client, anywhere. OAuth 2.0 auth, Cloudflare Tunnel, atomic writes safe for Obsidian Sync.

2089. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 106
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

2090. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 106
   MCP server for natural language interaction with Power BI datasets

2091. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 106
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

2092. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 106
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

2093. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 106
   Model Context Protocol for YNAB (you need a budget)

2094. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 105
   An md file as a chat interface and editable history in one.

2095. **[claude-emporium](https://github.com/Vvkmnn/claude-emporium)** - ⭐ 105
   🏛 [UNDER CONSTRUCTION] A (roman) claude plugin marketplace 

2096. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

2097. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

2098. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

2099. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 105
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

2100. **[linggen-memory](https://github.com/linggen/linggen-memory)** - ⭐ 105
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

2101. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 105
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref. 

2102. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

2103. **[deep-code-reasoning-mcp](https://github.com/evalops/deep-code-reasoning-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

2104. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 105
   first gemini based desktop client for MCP

2105. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 105
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

2106. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

2107. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

2108. **[linggen](https://github.com/linggen/linggen)** - ⭐ 104
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

2109. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 104
   Official Vectorize MCP Server

2110. **[agent-bridge](https://github.com/raysonmeng/agent-bridge)** - ⭐ 104
   A local bridge for bidirectional collaboration between Claude Code and Codex. 连接 Claude Code 与 Codex 的本地实时协作桥接工具。

2111. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 104
   A Model Context Protocol server that provides knowledge graph management capabilities. 

2112. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 103
   simple web ui to manage mcp (model context protocol) servers in the claude app

2113. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

2114. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

2115. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

2116. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

2117. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

2118. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 103
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

2119. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 103
   AlibabaCloud CloudOps MCP Server

2120. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 103
   Wanaku MCP Router

2121. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 103
    Official Go implementation of the UTCP 

2122. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 103
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

2123. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 103
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

2124. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 103
   This is a Ruby implementation of MCP (Model Context Protocol) client

2125. **[omega-memory](https://github.com/omega-memory/omega-memory)** - ⭐ 103
   Persistent memory for AI coding agents

2126. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 103
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

2127. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 103
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

2128. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 103
   xiaohongshu-mcp-python 是一个基于现代 Python 技术栈开发的小红书内容自动化发布工具，通过 Model Context Protocol（MCP）协议为 AI 客户端提供强大的小红书操作能力。项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持 HTTP/HTTPS 链接，为用户提供灵活的内容发布方案。  该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的 MCP 接口，用户可以轻松地将小红书操作能力集成到各种 AI 工作流中，实现智能化的内容管理

2129. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

2130. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 102
   go doc mcp server

2131. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 102
   Quickly screenshots webpages and converts to an LLM friendly size

2132. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 102
   Node.js Client Implementation for Model Context Protocol (MCP)

2133. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 102
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

2134. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 102
   MCP server for AI image generation and editing with automatic prompt optimization and quality presets (fast/balanced/quality). Powered by Gemini (Nano Banana 2 & Pro).

2135. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 102
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

2136. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

2137. **[agenticmail](https://github.com/agenticmail/agenticmail)** - ⭐ 102
   Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically

2138. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

2139. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 101
   Collection of examples of how to use Model Context Protocol with AWS.

2140. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

2141. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 101
   Memory and context manager just works.

2142. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 101
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

2143. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 101
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

2144. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 101
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

2145. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

2146. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

2147. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

2148. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

2149. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

2150. **[mpm-vibe-coding](https://github.com/halflifezyf2680/mpm-vibe-coding)** - ⭐ 100
   MPM is an MCP context-engineering layer for Vibe Coding, focused on three delivery bottlenecks: context loss, uncontrolled changes, and non-verifiable outcomes.

2151. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 100
   LangGraph AI Repository

2152. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 100
   MCP server for persistent context management in AI coding assistants

2153. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 100
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

2154. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 100
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

2155. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

2156. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

2157. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

2158. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

2159. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 99
   lapras.com 公式MCP Server

2160. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 99
   Your AI Coding Assistant's Long-Term Memory

2161. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 99
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

2162. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 99
   A Model Context Protocol (MCP) server for square

2163. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 99
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

2164. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 99
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

2165. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 99
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

2166. **[ETOS-LLM-Studio](https://github.com/Eric-Terminal/ETOS-LLM-Studio)** - ⭐ 99
   A powerful native LLM client for iOS & Apple Watch. Supports OpenAI/Claude/Gemini, featuring local RAG memory, Model Context Protocol (MCP) tools, Siri Shortcuts, and cross-device sync. Built with Swift.

2167. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 98
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

2168. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 98
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

2169. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

2170. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 98
   MCP Server for AI automation of the PlayCanvas Editor

2171. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 98
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

2172. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

2173. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 98
   Context7 MCP Server for Zed

2174. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 98
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

2175. **[mcp_on_ruby](https://github.com/nagstler/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

2176. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

2177. **[cesium-mcp](https://github.com/gaopengbin/cesium-mcp)** - ⭐ 98
   AI-powered CesiumJS 3D globe control  49 tools for camera, entities, layers, animation & spatial analysis via Model Context Protocol (MCP). Natural language to 3D GIS.

2178. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 97
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

2179. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 97
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

2180. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 97
   claude mcp sse demo with server and client(cli、web)

2181. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 97
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

2182. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 97
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

2183. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server for querying the CVE-Search API

2184. **[deterministic-agent-control-protocol](https://github.com/elliot35/deterministic-agent-control-protocol)** - ⭐ 96
   Governance gateway for AI agents — bounded, auditable, session-aware control with MCP proxy, shell proxy & HTTP API. Works with Cursor, Claude Code, Codex, and any MCP-compatible agent.

2185. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 96
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

2186. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 96
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

2187. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 96
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

2188. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 96
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

2189. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 96
   Portable , scalable , secure AI Agents

2190. **[NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform)** - ⭐ 96
   AI-powered network automation via Netbox and Model Context Protocol (MCP). 178 tools for multi-vendor infrastructure   management, self-healing agents, drift detection, and a real-time web dashboard.

2191. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 96
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

2192. **[ogham-mcp](https://github.com/ogham-mcp/ogham-mcp)** - ⭐ 96
   Shared memory MCP server — persistent, searchable, cross-client Claude, Opencode

2193. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 95
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

2194. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 95
   MCP Server for Linux Scheduler Management and Auto optimization

2195. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 95
   Collection of resources to help AI agents build better with Sanity.

2196. **[mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events)** - ⭐ 95
   MCP server providing native macOS integration with Apple Reminders and Calendar via EventKit

2197. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 95
   A Model Context Protocol (MCP) server for working with TradingView PineScript

2198. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 94
   Sandbox for Agents 

2199. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 94
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

2200. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 94
   Interact with all three types of generative UI, all in one interface

2201. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 94
   Model Context Protocol server for Replicate's API

2202. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 94
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

2203. **[us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp)** - ⭐ 94
   MCP server + TypeScript SDK for 40+ U.S. government data APIs — 250+ tools. Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, and many more. Works with VS Code Copilot, Claude Desktop, Cursor.

2204. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 94
   Official Oxylabs MCP integration

2205. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 94
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

2206. **[Embody](https://github.com/dylanroscover/Embody)** - ⭐ 94
   MCP server for TouchDesigner — build, wire, and debug networks with AI. Plus git-diffable externalization.

2207. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

2208. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

2209. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

2210. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 93
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

2211. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 93
   Octopus Deploy Official MCP Server

2212. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 93
   MCPcat is an analytics platform for MCP server owners 🐱.

2213. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 93
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

2214. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 93
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

2215. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 93
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

2216. **[askimo](https://github.com/haiphucnguyen/askimo)** - ⭐ 93
   Local-first AI agent platform for desktop and CLI. Chat, RAG search, multi-step Plans workflows, MCP tools, and script runner. Supports OpenAI, Claude, Gemini, Grok, Ollama, LM Studio and more

2217. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 93
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2218. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

2219. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 92
   Open Models MCP for Blender Using Ollama

2220. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 92
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

2221. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 92
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

2222. **[identity](https://github.com/agntcy/identity)** - ⭐ 91
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2223. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

2224. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

2225. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 91
   A Model Context Protocol server that provides knowledge graph management capabilities.

2226. **[photon](https://github.com/portel-dev/photon)** - ⭐ 91
   Define intent once. Photon turns a single TypeScript file into CLI tools, MCP servers, and web interfaces.

2227. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 91
   A model-context-protocol server for molecules.

2228. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 91
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

2229. **[kicad-mcp-pro](https://github.com/oaslananka/kicad-mcp-pro)** - ⭐ 91
   Professional Model Context Protocol server for KiCad: project setup, schematic/PCB tooling, validation, and manufacturing exports.

2230. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 91
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

2231. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 90
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

2232. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 90
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2233. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 89
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

2234. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 89
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

2235. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 89
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

2236. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 89
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

2237. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 89
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

2238. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 89
   The official MCP server for SurrealDB

2239. **[tradingview-chart-mcp](https://github.com/ertugrul59/tradingview-chart-mcp)** - ⭐ 89
   MCP server that captures TradingView chart images via Selenium — supports any ticker/interval with browser pooling for concurrent performance

2240. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 89
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

2241. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 89
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2242. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

2243. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 88
   高德地图MCP Server，支持stdio, sse和streamable-http

2244. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 88
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

2245. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 88
   CLI & API for MCP management

2246. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 88
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

2247. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

2248. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

2249. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

2250. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 87
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

2251. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 87
   Ragie Model Context Protocol Server

2252. **[sdl-mcp](https://github.com/GlitterKill/sdl-mcp)** - ⭐ 87
   SDL-MCP (Symbol Delta Ledger MCP Server) is a cards-first context system for coding agents that saves tokens and improves context.

2253. **[mcpmu](https://github.com/Bigsy/mcpmu)** - ⭐ 87
   TUI-based MCP server multiplexer, configure all your MCP's in a single MCP with profiles

2254. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 87
   MCP server for Slither static analysis of Solidity smart contracts

2255. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 87
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2256. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 87
   MCP server for the NCBI E-utilities API. Search PubMed, fetch article metadata and full text, generate citations, explore MeSH terms, and discover related research. STDIO or Streamable HTTP.

2257. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 87
   A WooCommerce (MCP) Model Context Protocol server

2258. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 86
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

2259. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

2260. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

2261. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

2262. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

2263. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

2264. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 86
   MCP server for AI-assisted development of CAP applications

2265. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 86
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

2266. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 86
   A Model Context Protocol server for Zendesk

2267. **[mcp-server](https://github.com/bitDive/mcp-server)** - ⭐ 86
   BitDive Model Context Protocol (MCP) server. The Autonomous Quality Loop for AI agents. Provides real runtime context, before/after trace comparison, and integration testing workflows.

2268. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 86
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2269. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 86
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

2270. **[zabbix-mcp-server](https://github.com/initMAX/zabbix-mcp-server)** - ⭐ 86
   MCP server for the complete Zabbix API — 231 tools, multi-server support, bearer auth, systemd ready. Works with ChatGPT, Claude, VS Code, Codex, JetBrains and any MCP client.

2271. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 85
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

2272. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

2273. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

2274. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 85
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

2275. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 85
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

2276. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 85
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

2277. **[aivectormemory](https://github.com/Edlineas/aivectormemory)** - ⭐ 85
   aivectormemory 是一款基于 Model Context Protocol (MCP) 开发的OpenClaw、OpenCode、ClaudeCodeAI记忆管理工具。它专门为 Claude、OpenCode、Cursor 和 主流IDE 编程工具设计，通过向量数据库技术解决 AI 在不同对话会话中「健忘」的问题。aivectormemory: A lightweight MCP Server enabling persistent, cross-session memory for AI-powered IDEs via vector search.

2278. **[AutoGenesis](https://github.com/microsoft/AutoGenesis)** - ⭐ 85
   AutoGenesis is an AI-powered automated testing framework based on Model Context Protocol (MCP), supporting multiple platforms including desktop applications (Windows/macOS) and mobile applications (iOS/Android).

2279. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

2280. **[spiceflow-framework](https://github.com/remorses/spiceflow-framework)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

2281. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 84
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

2282. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 84
   a mcp server to manage github project's functionality 

2283. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 84
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

2284. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 84
   Model Context Protocol (MCP) Server for the Keboola Platform

2285. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 84
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

2286. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 84
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

2287. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 84
   Open-source FRED MCP Server (Federal Reserve Economic Data)

2288. **[mcp-1c](https://github.com/feenlace/mcp-1c)** - ⭐ 84
   MCP server for 1C:Enterprise — AI assistant sees your configuration and generates accurate BSL code. One binary, zero dependencies, 9 tools.

2289. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 84
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

2290. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 84
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2291. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 84
   [Community Supported] Perforce P4 MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2292. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 84
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

2293. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 84
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

2294. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 84
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2295. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 84
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

2296. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 84
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2297. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 84
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

2298. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 83
   Streams are the future of AI powered by unlimited free tokens.

2299. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

2300. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

2301. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

2302. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

2303. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 83
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

2304. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 83
   The EMBL-EBI Ontology Lookup Service (OLS)

2305. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 83
   A GitHub MCP Server extension for Zed

2306. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 83
   A complete MCP server template that include vitamins (oauth authentication included)

2307. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 83
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

2308. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 83
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2309. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 83
   An extension of MCP for SillyTavern.

2310. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 83
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2311. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 83
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

2312. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 82
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

2313. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

2314. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 82
   Model Context Protocol (MCP) CLI server template for Rust

2315. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 82
   MCP Server to previewing mermaid diagrams with live reload

2316. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 82
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

2317. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 82
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

2318. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 82
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

2319. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 82
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2320. **[formanator](https://github.com/timrogers/formanator)** - ⭐ 82
   Submit and manage Forma (https://joinforma.com) claims from the command line and Model Context Protocol (MCP) clients

2321. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 82
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

2322. **[line-desktop-mcp](https://github.com/dtwang/line-desktop-mcp)** - ⭐ 82
   透過 MCP（Model Context Protocol），使 AI 工具能夠與 LINE Desktop 整合，並執行訊息的讀取與發送操作。Through the MCP (Model Context Protocol), AI tools can be integrated with LINE Desktop to perform message reading and sending operations.

2323. **[ComIDP-MCP-Server](https://github.com/ComPDFKit/ComIDP-MCP-Server)** - ⭐ 82
   A lightweight MCP (Model Context Protocol) server designed for seamless integrating ComIDP with Claude Desktop.

2324. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 82
   A Model Context Protocol (MCP) server for Microsoft Clarity

2325. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

2326. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

2327. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

2328. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 81
   OpenAPI specification MCP server.

2329. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 81
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

2330. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

2331. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 81
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

2332. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 81
   A full featured, enterprise grade rust MCP SDK

2333. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 81
   Model Context Protocol server for OpenStreetMap data

2334. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 80
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

2335. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

2336. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 80
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

2337. **[ophis](https://github.com/njayp/ophis)** - ⭐ 80
   Transform any Cobra CLI into an MCP server

2338. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 80
   Build agentic-MCP servers by composing existing MCP tools.

2339. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 80
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

2340. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 80
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

2341. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 80
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

2342. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 80
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

2343. **[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp)** - ⭐ 80
   MCP server for controlling a real iPhone via macOS iPhone Mirroring...and any MacOs app. Screenshot, tap, swipe, type — from any MCP client.

2344. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 79
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

2345. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 79
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

2346. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

2347. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

2348. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

2349. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 79
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

2350. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 79
   MCP server that can execute terminal commands

2351. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 79
   A MCP server for Django applications, inspired by Laravel Boost.

2352. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 79
   Model Context Protocol implementation for retrieving codebases using RepoMix

2353. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 79
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

2354. **[modular-context-obsidian-plugin](https://github.com/klemensgc/modular-context-obsidian-plugin)** - ⭐ 79
   Modular Context | Karpathy LLM Knowledge Base + Gmail & G-Cal — multi-account MCP server for Claude Code, encrypted local-first

2355. **[Ludus-FastMCP](https://github.com/tjnull/Ludus-FastMCP)** - ⭐ 79
   A Model Context Protocol (MCP) server for automating Ludus v1 and v2 cyber range environments through AI assistants. 190+ tools for range management, blueprints, groups, templates, scenarios, and SIEM integration.

2356. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 79
   Deterministic research MCP server on FastMCP 3 — 5-engine web search, 9-platform social search, 6 academic DBs, news aggregation, entity profiles, conflict detection, document analysis. No API keys. No in-server LLM. Structured outputs for agent chaining.

2357. **[gno](https://github.com/gmickel/gno)** - ⭐ 79
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2358. **[transit-agent](https://github.com/ruby-verma/transit-agent)** - ⭐ 78
   This guide demonstrates how to build an Agentic AI system using Google's Agent Development Kit (ADK) and the Model Context Protocol (MCP).

2359. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 78
   MCP Server for Bing Search API

2360. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 78
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

2361. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 78
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

2362. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 78
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

2363. **[hulunote](https://github.com/hulunote/hulunote)** - ⭐ 78
   AI + Note Hippocampus — Your second brain, powered by AI

2364. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 78
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2365. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 78
   Build MCP servers with WebAssembly components

2366. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 78
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2367. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 78
   Model Context Protocol server for CODESYS automation platform

2368. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 77
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

2369. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 77
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

2370. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

2371. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

2372. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

2373. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

2374. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2375. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 77
    An MCP server that provides LLMs access to other LLMs

2376. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 77
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

2377. **[agent-security-scanner-mcp](https://github.com/sinewaveai/agent-security-scanner-mcp)** - ⭐ 77
   Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

2378. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 77
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

2379. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 77
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

2380. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 77
   A Model Context Protocol Server to perform Kafka client operations

2381. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 77
   MCP server for computer use & browser automation  - screenshot, OCR, click, type, find_text, Chrome/Electron CDP, template matching. macOS, Windows & Android. Works with Claude, Cursor, and any MCP client.

2382. **[windbg-mcp](https://github.com/gengstah/windbg-mcp)** - ⭐ 77
   An MCP (Model Context Protocol) server that turns all pybag Windows debugger functions into native MCP tools. It lets MCP-compatible clients (Claude Desktop, Claude Code, Cowork, OpenAI Codex CLI, Cursor, and custom agents) control user-mode processes, kernel sessions, and crash dump analysis via structured JSON calls.

2383. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 77
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2384. **[qgis-mcp](https://github.com/nkarasiak/qgis-mcp)** - ⭐ 77
   Connect QGIS to Claude AI through the Model Context Protocol (MCP)

2385. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 77
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

2386. **[houtini-lm](https://github.com/houtini-ai/houtini-lm)** - ⭐ 77
   MCP server that saves Claude Code tokens by delegating bounded tasks to local or cloud LLMs. Works with LM Studio, Ollama, vLLM, DeepSeek, Groq, Cerebras.

2387. **[glade-mcp-unity](https://github.com/Glade-tool/glade-mcp-unity)** - ⭐ 77
   Connect any MCP-compatible AI client (Claude Code, Cursor) to your Unity Editor. 222+ granular tools, a full Unity-aware system prompt, game design document project context, script semantic search, and skill calibration - all free and local.

2388. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 76
   MCP server for Google Search integration using Gemini's built-in search capabilities

2389. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

2390. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 76
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

2391. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 76
   MCP web search using perplexity without any API KEYS 

2392. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 76
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

2393. **[apitap](https://github.com/n1byn1kt/apitap)** - ⭐ 76
   The MCP server that turns any website into an API — no docs, no SDK, no browser. npm: @apitap/core

2394. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 76
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2395. **[Sephera](https://github.com/Reim-developer/Sephera)** - ⭐ 76
   Fast local-first Rust CLI for codebase metrics, AST-compressed LLM context bundles, and built-in MCP server.

2396. **[altk-evolve](https://github.com/AgentToolkit/altk-evolve)** - ⭐ 76
   Self improving agents through iterations

2397. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 76
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

2398. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 76
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

2399. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 76
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

2400. **[perplexity-webui-scraper](https://github.com/henrique-coder/perplexity-webui-scraper)** - ⭐ 76
   An advanced, high-performance Python client, MCP server, and REST API for reverse-engineering Perplexity AI's WebUI.

2401. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 76
   Index of all Model Context Protocol (MCP) clients and their capabilities

2402. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 76
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

2403. **[Meting-Agent](https://github.com/ELDment/Meting-Agent)** - ⭐ 75
   🪐 面向 AI 的多音乐平台的 API 代理 • 网易云 • QQ音乐 • 酷狗 • 酷我 🎻 Multi-platform music API agent for AI • NetEase • QQ Music • KuGou • Kuwo

2404. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

2405. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 75
   MCP to explore websites with llms.txt files

2406. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 75
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

2407. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 75
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

2408. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 75
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

2409. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 75
   Interactive Brokers MCP Server

2410. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 75
   The Privacy Firewall for LLMs

2411. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 75
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2412. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 75
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2413. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 75
   Zero-dependency MCP server implementation.

2414. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 75
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2415. **[MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP)** - ⭐ 75
   Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered search and vision analysis APIs optimized for code development workflows

2416. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 74
   A task management system designed for AI development

2417. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 74
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

2418. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 74
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2419. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 74
   Unified execution environment for Python code, shell commands, and programmatic MCP tool calls.

2420. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 74
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2421. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 74
   AniList MCP server for accessing anime and manga data

2422. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 74
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2423. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 74
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

2424. **[reddit-mcp-server](https://github.com/jordanburke/reddit-mcp-server)** - ⭐ 74
   ⚙️ A Model Context Protocol (MCP) that provides tools for fetching and creating Reddit content

2425. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 73
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

2426. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

2427. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 73
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

2428. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 73
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

2429. **[firefox-devtools-mcp](https://github.com/globau/firefox-devtools-mcp)** - ⭐ 73
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2430. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 73
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

2431. **[youtube-connector-mcp](https://github.com/ShellyDeng08/youtube-connector-mcp)** - ⭐ 73
   MCP server for YouTube — search videos, channels, playlists, and transcripts. Works with Claude, Cursor, Windsurf, and any MCP client.

2432. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 73
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

2433. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 73
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2434. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 73
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2435. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 72
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

2436. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 72
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

2437. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 72
   An experimental GitHub MCP server with local database.

2438. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 72
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

2439. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 72
   MCP server for the Joplin note taking app

2440. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 72
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2441. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 72
   An unofficial and community-built MCP server for integrating with https://railway.app

2442. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 72
   Model Context Protocol (MCP) server for Gmail

2443. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 72
   Persistent memory for AI coding agents. Cross-session context, global knowledge, and autonomous task execution.

2444. **[ainativelang](https://github.com/sbhooley/ainativelang)** - ⭐ 72
   AINL helps turn AI from "a smart conversation" into "a structured worker."  It is designed for teams building AI workflows that need multiple steps, state and memory, tool use, repeatable execution, validation and control, and lower dependence on long prompt loops.  AINL is a compact, graph-canonical, AI-native programming system for (READ: README)

2445. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 72
   可视化的配置和管理，给xiaozhi接入mcp

2446. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 72
   Python 实现 MCP client / service

2447. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 72
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2448. **[drawio-mcp-server](https://github.com/simonkurtz-MSFT/drawio-mcp-server)** - ⭐ 72
   A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server generates Draw.io XML directly — no browser extension or Draw.io instance required.

2449. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 72
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

2450. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 71
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

2451. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 71
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

2452. **[adb-tui](https://github.com/alanisme/adb-tui)** - ⭐ 71
   🤖 Full-featured Android Debug Bridge TUI and MCP server. Control any device by keystroke or AI.

2453. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 71
   MCP server to fetch YouTube transcripts

2454. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

2455. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server 

2456. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 71
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

2457. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 71
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2458. **[trading-mcp](https://github.com/netanelavr/trading-mcp)** - ⭐ 71
   The MCP server that will help you trade smarter (or at least try)

2459. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 71
   Javascript SDK for interacting with the MCP Toolbox for Databases.

2460. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 71
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

2461. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 71
   MCP client for local ollama models

2462. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 71
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

2463. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 71
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

2464. **[mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs)** - ⭐ 71
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2465. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 71
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2466. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 71
   Altium Model Context Protocol server and Altium API script

2467. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 71
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2468. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 71
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2469. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 70
   Convert LangChain tools to FastMCP tools

2470. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 70
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

2471. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 70
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

2472. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 70
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

2473. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 70
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2474. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 70
   McDonald's China MCP Server Integration Guide

2475. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 70
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

2476. **[MCP-server-Deepseek_R1](https://github.com/kamelirzouni/MCP-server-Deepseek_R1)** - ⭐ 70
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2477. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 70
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

2478. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 70
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

2479. **[aguara](https://github.com/garagon/aguara)** - ⭐ 70
   Security scanner for AI agent skills and MCP servers. Static analysis, incident response, no LLM. One binary.   Detection engine behind oktsec.

2480. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 70
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2481. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 69
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2482. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2483. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 69
   A simple MCP server for the SO-ARM100 control

2484. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 69
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

2485. **[unity-mcp-plugin](https://github.com/AnkleBreaker-Studio/unity-mcp-plugin)** - ⭐ 69
   Unity MCP Plugin (UPM) — Editor bridge for AI-assisted game development. Enables Claude, Cursor & MCP-compatible AI to control Unity Editor with 268 tools: scenes, GameObjects, components, builds, profiling, Shader Graph, Amplify Shader Editor, terrain, physics, NavMesh & more. Free & open source.

2486. **[claude-code-source-all-in-one](https://github.com/wuwangzhang1216/claude-code-source-all-in-one)** - ⭐ 69
   Always up-to-date open-source mirror of Claude Code with GPT-5.4 support. Run Claude Code from source with Claude or GPT models via ChatGPT subscription. 18 deep-dive architecture articles included. For educational and reference purposes only.

2487. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 69
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2488. **[Skills-ContextManager](https://github.com/One-Man-Company/Skills-ContextManager)** - ⭐ 69
   A self-hosted web application for managing AI skills, workflows, and contexts with full MCP (Model Context Protocol) integration. Organize, manage, and dynamically load specialized knowledge bases into any AI Agent just by toggling your Skills On/Off in simple local hosted WEB UI.

2489. **[buddy](https://github.com/fiorastudio/buddy)** - ⭐ 69
   A virtual pet companion for your AI — Designed to provide in-context code review feedback with personality. Grow with your buddy and level up together. Works with Claude Code, Codex, CursorCLI, Github CopilotCLI, OpenClaw, and any MCP compatible clients

2490. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 68
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

2491. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 68
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

2492. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 68
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

2493. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

2494. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 68

2495. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

2496. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 68
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

2497. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 68
   MCP Deep Research Server using Gemini creating a Research AI Agent

2498. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 68
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

2499. **[vesta-mac-dist](https://github.com/scouzi1966/vesta-mac-dist)** - ⭐ 68
   Vesta macOS Distribution - Official releases and downloads.Vesta AI Chat Assistant for macOS - Built with SwiftUI, Swift MLX  and Apple Intelligence using Apple's on device model on MacOs Tahoe (MacOS 26). Now with side-by-side Qwen3-VL for vison

2500. **[hyperterse](https://github.com/hyperterse/hyperterse)** - ⭐ 68
   The MCP framework. Connect your data to your agents.

2501. **[nothumanallowed](https://github.com/adoslabsproject-gif/nothumanallowed)** - ⭐ 68
   Epistemic dataset generation engine. 38 AI agents deliberate through multi-round Geth Consensus — producing auditable reasoning traces for AI training. Parliament System, Knowledge Grounding, zero-trust security.

2502. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 68
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

2503. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 68
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2504. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 68
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2505. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 68
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2506. **[gdal-mcp](https://github.com/JordanGunn/gdal-mcp)** - ⭐ 68
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2507. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

2508. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

2509. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

2510. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 67
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

2511. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 67
   MCP server that provides tools and resources to control and monitor robots using Nav2.

2512. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 67
   A MCP server for interacting with Bear note-taking software.

2513. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 67
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

2514. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 67
   Attio Model Context Protocol (MCP) server implementation

2515. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 67
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2516. **[monolith](https://github.com/tumourlove/monolith)** - ⭐ 67
   MCP plugin for Unreal Engine 5.7 — gives AI assistants full read/write access to Blueprints, Materials, Niagara VFX, Animation, Mesh, AI (BT/ST/EQS/SO), GAS, Logic Driver, ComboGraph, UI, Audio (Sound Cues + MetaSounds), and more. 1,226 actions across 16 modules. Zero Python dependency.

2517. **[compass](https://github.com/raystack/compass)** - ⭐ 67
   Compass is a context engine that builds a knowledge graph of your organization's metadata, capturing   entities, relationships, and lineage across systems and time, making it discoverable and queryable for   both humans and AI agents.

2518. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 67
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

2519. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 67
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2520. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 67
   ABAP MCP - Model Context Protocol - Server SDK

2521. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 67
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

2522. **[wp-mcp-ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)** - ⭐ 67
   WordPress MCP Ultimate — Full MCP server with 58 WordPress abilities. Connect WordPress to any AI via Model Context Protocol.

2523. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 67
   Compiler-driven MCP framework for Kotlin Multiplatform

2524. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 67
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2525. **[join.cloud](https://github.com/kushneryk/join.cloud)** - ⭐ 66
   Join.cloud lets AI agents work together in real-time rooms. Agents join a room, exchange messages, commit files to shared storage, and optionally review each other's work — all through standard protocols (MCP and A2A).

2526. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 66
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

2527. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 66
   [MCP Server] The Security Agent for AI assisted coding

2528. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 66
   Amazon MCP server to search & buy products using the L402

2529. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 66
   Model Context Protocol(MCP) 中文教程讲解

2530. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 66
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2531. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 66
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

2532. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 66
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

2533. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 66
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2534. **[cesium-ai-integrations](https://github.com/CesiumGS/cesium-ai-integrations)** - ⭐ 66
   Cesium AI Integrations is a collection of reference integrations and experiments connecting the Cesium ecosystem with AI systems including Model Context Protocol (MCP) tools, retrieval pipelines, and agent skills.

2535. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 66
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2536. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 66
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2537. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 65
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

2538. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 65
   FHIR MCP Server for handling medical data standard.

2539. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 65
   Academia MCP server: Tools for automatic scientific research

2540. **[ClaudeHistoryMCP](https://github.com/jhammant/ClaudeHistoryMCP)** - ⭐ 65
   MCP server for searching and surfacing Claude Code conversation history

2541. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 65
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

2542. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 65
   LSD Model Context Protocol

2543. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 65
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2544. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 65
   MCP server for the ClinicalTrials.gov v2 API. Search trials, retrieve study details and results, and match patients to eligible trials.

2545. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 65
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2546. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 65
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2547. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 65
   🗓️ A CalDAV Model Context Protocol (MCP) server to expose calendar operations as tools for AI assistants.

2548. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 65
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2549. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 65
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2550. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 65
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

2551. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 65
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2552. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 65
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2553. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 65
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2554. **[agenti](https://github.com/nirholas/agenti)** - ⭐ 65
   Give any AI agent a crypto wallet. Agents deserve access to money.  Pay x402 APIs, receive USDC, check balances — autonomously. Works with Claude, LangChain, AutoGen, CrewAI, and any MCP client. EVM + Solana.

2555. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 64
   A Model Context Protocol implementation for FHIR

2556. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

2557. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

2558. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

2559. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 64
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2560. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 64
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2561. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 64
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2562. **[estonia-ai-kit](https://github.com/stefanoamorelli/estonia-ai-kit)** - ⭐ 64
   🇪🇪 Open-source AI SDK for Estonian government and private services. MCP servers and skills. Connect Claude, GPT, agents and models, to Estonia's digital infrastructure.

2563. **[pitlane-mcp](https://github.com/eresende/pitlane-mcp)** - ⭐ 64
   Token-efficient navigation substrate for AI coding agents. Index code once and retrieve only the symbols you need.

2564. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 64
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2565. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 64
   Miro integration for Model Context Protocol

2566. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 64
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2567. **[CornMCP](https://github.com/yuki-20/CornMCP)** - ⭐ 64
   CornMCP is an open-source mono repo that gives AI coding agents (Antigravity, Cursor, Claude Code, Codex), token-saving access to your codebase through the Model Context Protocol (MCP).

2568. **[SageFs](https://github.com/WillEhrendreich/SageFs)** - ⭐ 64
   Sage Mode for F# development — REPL with solution or project loading, Live Testing for FREE, Hot Reload, and session management.

2569. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

2570. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 63
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

2571. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 63
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

2572. **[cortex-scout](https://github.com/cortex-works/cortex-scout)** - ⭐ 63
   A unified web extraction and stateful automation engine for AI. Replaces heavy testing frameworks with token-optimized browser control, deep research, and HITL.

2573. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 63
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2574. **[1c-mcp](https://github.com/Untru/1c-mcp)** - ⭐ 63
   Curated list of MCP servers for 1C:Enterprise ecosystem | Каталог MCP-серверов для экосистемы 1С:Предприятие

2575. **[unreal-api-mcp](https://github.com/Codeturion/unreal-api-mcp)** - ⭐ 63
   Instant, accurate Unreal Engine API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations.

2576. **[home-memory](https://github.com/impactjo/home-memory)** - ⭐ 63
   MCP server that lets your AI assistant remember everything about your home.

2577. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 63
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2578. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 63
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2579. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 62
   A Model Context Protocol (MCP) server for Rember.

2580. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 62
   Cryptocurrency Market Data MCP Server

2581. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

2582. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 62
   Advanced MCP server for seamless access to Israeli Government Open Data

2583. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 62
   Model Context Protocol server and client for R

2584. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 62
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2585. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 62
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

2586. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 62
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2587. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 62
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2588. **[agent-architecture-review-sample](https://github.com/Azure-Samples/agent-architecture-review-sample)** - ⭐ 62
   The Architecture Review Agent is an open-source AI agent sample that reviews software architectures and generates interactive diagrams automatically. 

2589. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 62
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2590. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 62
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2591. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 62
   Model Context Protocol server for ActivityWatch time tracking data

2592. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 62
   A Model Context Protocol server for Go developers

2593. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 61
   Universal MCP Server Configuration Manager

2594. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services. 

2595. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 61
   nocodb mcp server

2596. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 61
   A Clojure SDK to create MCP servers (and eventually clients)

2597. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 61
   A curated list of awesome Model Context Protocol (MCP) servers.

2598. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 61
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2599. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 61
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2600. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 61
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2601. **[mcp-bridgekit](https://github.com/mkbhardwas12/mcp-bridgekit)** - ⭐ 61
   Embeddable MCP stdio → HTTP bridge with background jobs & live dashboard. Survives Vercel/Cloudflare 30s timeouts. Now scales to 100+ users.

2602. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 61
   A Model Context Protocol server for Ashra

2603. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2604. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 61
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2605. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 61
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2606. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 60
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

2607. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 60
   MCP (Model Context Protocol) server for the Contentful Management API

2608. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

2609. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

2610. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 60
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

2611. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 60
   Adds MCP server to Blockbench

2612. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

2613. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 60
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2614. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 60
   Unblock, scrape, and search tools for MCP clients

2615. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 60
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2616. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 60
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2617. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 60
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2618. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 60
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2619. **[pentestMCP](https://github.com/RamKansal/pentestMCP)** - ⭐ 60
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2620. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 59
   MCP Server for IBKR Client

2621. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 59
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2622. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 59
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

2623. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

2624. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

2625. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

2626. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 59
   MCP Server to expose the GDB debugging capabilities

2627. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 59
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2628. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 59
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2629. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 59
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

2630. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 59
   A powerful Model Context Protocol server for LinkedIn API integration

2631. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 58
   MCP router and Web Based MCP client

2632. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2633. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2634. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 58
   ScapeGraph MCP Server

2635. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 58
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2636. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 58
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2637. **[better-bear](https://github.com/KuvopLLC/better-bear)** - ⭐ 58

2638. **[reaper-mcp](https://github.com/bonfire-audio/reaper-mcp)** - ⭐ 58
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2639. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 58
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2640. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 58
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2641. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2642. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 57
   Model Context Protocol server for Daipendency

2643. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2644. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2645. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 57
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2646. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 57
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2647. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 57
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2648. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 57
   OCaml implementation of the Model Context Protocol (MCP)

2649. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 57
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

2650. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 57
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2651. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2652. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 57
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2653. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 57
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2654. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 57
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2655. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 57
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2656. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 57
   Go SDK for interacting with the MCP Toolbox for Databases.

2657. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 57
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2658. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 57
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2659. **[aitour26-WRK542-prototype-agents-with-Foundry-toolkit-and-model-context-protocol](https://github.com/microsoft/aitour26-WRK542-prototype-agents-with-Foundry-toolkit-and-model-context-protocol)** - ⭐ 57

2660. **[python](https://github.com/mcp-auth/python)** - ⭐ 57
   🔐 Plug-and-play auth for Python MCP servers.

2661. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 56
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2662. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2663. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2664. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2665. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 56
   Generate an MCP for any web app

2666. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 56
   Write notes to Flomo

2667. **[MegaMemory](https://github.com/0xK3vin/MegaMemory)** - ⭐ 56
   Persistent project knowledge graph for coding agents. MCP server with semantic search, in-process embeddings, and web explorer.

2668. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 56
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2669. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 56
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2670. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 56
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2671. **[mcpshim](https://github.com/mcpshim/mcpshim)** - ⭐ 56
   Turn remote MCP servers into local command workflows.

2672. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2673. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 56
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2674. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 56
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2675. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 56
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2676. **[client](https://github.com/php-mcp/client)** - ⭐ 56
   Core PHP implementation for the Model Context Protocol (MCP) Client

2677. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 56
   MCP server to support Astro project development

2678. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 55
   Build multi-model chatbots and agents from intent.

2679. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 55
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2680. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 55
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2681. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 55
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2682. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 55
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2683. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 55
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2684. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 55
   Multiplatform system monitoring tool using Cosmopolitan Libc

2685. **[AfdianToMarkdown](https://github.com/PhiFever/AfdianToMarkdown)** - ⭐ 55
   爱发电爬虫(afdian.com)

2686. **[go-crx3](https://github.com/mmadfox/go-crx3)** - ⭐ 55
   Chrome browser extension tools with MCP integration. Pack, unpack, zip, unzip, download, and manage CRX3 extensions – now AI-compatible via Model Context Protocol.

2687. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 55
   MCP Memory Server with DuckDB backend

2688. **[unraid-mcp](https://github.com/jmagar/unraid-mcp)** - ⭐ 55
   Query, monitor, and manage Unraid servers via GraphQL API through MCP tools. Supports system info, Docker, VMs, array/parity, notifications, plugins, rclone, and live telemetry.

2689. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 55
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2690. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 55
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2691. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 55
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2692. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 55
   Implementation of Model Context Protocol server for Mailgun APIs

2693. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 55
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2694. **[mcp-stata](https://github.com/tmonk/mcp-stata)** - ⭐ 55
    A lightweight Model Context Protocol (MCP) server for Stata. Execute commands, inspect data, retrieve stored results (r()/e()), and view graphs in your chat interface. Built for economists who want to integrate LLM assistance into their Stata workflow. 

2695. **[npm-packages](https://github.com/WebMCP-org/npm-packages)** - ⭐ 55
   NPM packages for MCP-B: Transport layers, React hooks, and browser tools for the Model Context Protocol

2696. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 55
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2697. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 54
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2698. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 54
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2699. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2700. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2701. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2702. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2703. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 54
   A MCP server for symbolic manipulation of mathematical expressions

2704. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 54
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2705. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 54
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2706. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 54
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2707. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 54
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2708. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 54
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2709. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 54
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2710. **[brainstorm-mcp](https://github.com/spranab/brainstorm-mcp)** - ⭐ 54
   MCP server for multi-round AI brainstorming debates between multiple models (GPT, DeepSeek, Groq, Ollama, etc.)

2711. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 54
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2712. **[unity-mcp-pro-plugin](https://github.com/youichi-uda/unity-mcp-pro-plugin)** - ⭐ 54
   147 AI tools for Unity game development via MCP (Model Context Protocol). Connect Claude, Cursor, and AI assistants to your Unity editor.

2713. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 54
   MCP client for Discourse sites

2714. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 54
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2715. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 54
   Amadeus MCP(Model Context Protocol) Server

2716. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 53
   Model Context Protocol Servers for Azure AI Search

2717. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

2718. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2719. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2720. **[Multi-Agent-System-A2A-ADK-MCP](https://github.com/RubensZimbres/Multi-Agent-System-A2A-ADK-MCP)** - ⭐ 53
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2721. **[skrills](https://github.com/athola/skrills)** - ⭐ 53
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2722. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 53
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2723. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 53
   MCP Guard secures your MCP client from prompt injection attacks and more.

2724. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 53
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2725. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 53
   Thoughtbox is an intention ledger for agents. Evaluate AI's decisions against its decision-making.

2726. **[fossil-mcp](https://github.com/yfedoseev/fossil-mcp)** - ⭐ 53
   The code quality toolkit for the agentic AI era. Find dead code, clones, and scaffolding across 15 languages. MCP server + CLI.

2727. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 53
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2728. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 53
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2729. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 53
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

2730. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 53
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2731. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 53
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2732. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

2733. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2734. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2735. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 52
   Claude  et al. play the brilliant puzzle title "Baba is You"

2736. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 52
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

2737. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 52
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2738. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 52
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

2739. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 52
   Inkdrop Model Context Protocol Server

2740. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 52
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2741. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 52
   Official Rust implementation of the UTCP

2742. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 52
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2743. **[unity-api-mcp](https://github.com/Codeturion/unity-api-mcp)** - ⭐ 52
   Instant, accurate Unity API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations

2744. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 52
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2745. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 52
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2746. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

2747. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 52
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2748. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 52
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2749. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 52
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2750. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 52
   MCP (Model Context Protocol) server for the Contentful Management API

2751. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

2752. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 52
   IMAP Model Context Protocol server for interactive email processing

2753. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 52
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

2754. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 51
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

2755. **[gdal-mcp](https://github.com/Wayfinder-Foundry/gdal-mcp)** - ⭐ 51
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2756. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 51
   MCP Server for whois lookups.

2757. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 51
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

2758. **[ShadowCrawl](https://github.com/DevsHero/ShadowCrawl)** - ⭐ 51
   🥷 The FREE, Sovereign alternative to Firecrawl & Tavily. Pure Rust Stealth Scraper + Built-in God-Tier Meta-Search for AI Agents. Bypass Cloudflare & DataDome via HITL. Zero-bloat, ultra-clean LLM data. 99.99% Success Rate. 🦀

2759. **[hmr](https://github.com/promplate/hmr)** - ⭐ 51
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

2760. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 51
   Matlab MCP Server in python

2761. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 51
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2762. **[tokio-prompt-orchestrator](https://github.com/Mattbusel/tokio-prompt-orchestrator)** - ⭐ 51
   Multi-core, Tokio-native orchestration for LLM pipelines.

2763. **[mcp](https://github.com/40ants/mcp)** - ⭐ 51
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2764. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 51
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 17 security hardening layers

2765. **[ctxvault](https://github.com/Filippo-Venturini/ctxvault)** - ⭐ 51
   Local memory infrastructure for AI agents. Store knowledge and skills in isolated vaults you compose, control and query.

2766. **[Zikkaron](https://github.com/amanhij/Zikkaron)** - ⭐ 51
   Biologically-inspired persistent memory engine for Claude Code. 26 cognitive subsystems, Hopfield networks, predictive coding, causal discovery, successor representations, all running locally over SQLite.

2767. **[template-mcp-server](https://github.com/redhat-data-and-ai/template-mcp-server)** - ⭐ 51
   Production-ready Python template for building MCP servers with FastMCP, FastAPI, OAuth, and OpenShift deployment.

2768. **[openclaw-superpowers](https://github.com/ArchieIndian/openclaw-superpowers)** - ⭐ 51
   44 plug-and-play skills for OpenClaw — self-modifying AI agent with cron scheduling, security guardrails, persistent memory, knowledge graphs, and MCP health monitoring. Your agent teaches itself new behaviors during conversation.

2769. **[notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)** - ⭐ 51
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

2770. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 51
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

2771. **[omnifocus-mcp-enhanced](https://github.com/jqlts1/omnifocus-mcp-enhanced)** - ⭐ 51
   Enhanced Model Context Protocol (MCP) server for OmniFocus with complete subtask support, perspective views (Inbox/Flagged/Forecast/Tags), ultimate   task filtering, and direct access to custom perspectives. Seamlessly integrate OmniFocus with Claude AI for intelligent task management.

2772. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 51
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2773. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 51
   SAP HANA MCP server — Enterprise Model Context Protocol server for SAP HANA. Use with Claude Code, VS Code. npm: hana-mcp-server

2774. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 51
   A Model-Context-Protocol (MCP) Server for Active Directory

2775. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 51
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2776. **[ferris-search](https://github.com/lispking/ferris-search)** - ⭐ 51
   A blazing-fast MCP (Model Context Protocol) server for multi-engine web search, written in Rust.

2777. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

2778. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 51
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2779. **[ontosphere](https://github.com/ThHanke/ontosphere)** - ⭐ 51
   Browser-based RDF/ontology knowledge graph editor — load RDF from files, URLs or SPARQL endpoints; author nodes and edges on the canvas; run OWL-RL reasoning; apply multi-algorithm layout and clustering. AI-native via MCP tool surface and relay bridge. Fully client-side, no backend required.

2780. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 50
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

2781. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 50

2782. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

2783. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

2784. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

2785. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

2786. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

2787. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 50
   An implementation of the Model Context Protocol in Ruby.

2788. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 50
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2789. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 50
   GIMP MCP server

2790. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 50
   MCP Server for Text to Speech

2791. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 50
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

2792. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 50
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

2793. **[civyk-winwright](https://github.com/civyk-official/civyk-winwright)** - ⭐ 50
   Playwright-style MCP server for Windows desktop, system, and browser automation. 59 tools for WPF, WinForms, Win32, Chrome/Edge via Model Context Protocol.

2794. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 50
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

2795. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 50
   Anthropic’s Model Context Protocol implementation for Oat++

2796. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2797. **[ApkMCP-Auto](https://github.com/kggzs/ApkMCP-Auto)** - ⭐ 50
   本项目是一个 Android 逆向工程工具集合，通过 MCP (Model Context Protocol) 协议将 AI 助手（如 Claude）与专业的 Android 反编译工具连接起来，实现智能化的 APK 分析与修改。

2798. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 50
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

2799. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 49
   vMCP - Virtual Model Context Protocol

2800. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

2801. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

2802. **[agent-os](https://github.com/imran-siddique/agent-os)** - ⭐ 49
   A Safety-First Kernel for Autonomous AI Agents - POSIX-inspired primitives with 0% policy violation guarantee

2803. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 49
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

2804. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 49
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

2805. **[mcp](https://github.com/goplus/mcp)** - ⭐ 49
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

2806. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 49
   Send system notification when Agent task is done.

2807. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 49

2808. **[MCPwner](https://github.com/Pigyon/MCPwner)** - ⭐ 49
   Model Context Protocol server for autonomous vulnerability discovery

2809. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 49
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

2810. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 49
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

2811. **[gtm-mcp](https://github.com/impecablemee/gtm-mcp)** - ⭐ 49
   MCP server for B2B cold outreach — find companies via Apollo, verify with AI, push to SmartLead & GetSales. 49    tools. Works with Claude Code or any MCP client

2812. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 49
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2813. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2814. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 49
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

2815. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 49
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

2816. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2817. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 49
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

2818. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 49
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

2819. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2820. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2821. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2822. **[shadowgit-mcp](https://github.com/aflsolutions/shadowgit-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2823. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 48
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2824. **[mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index)** - ⭐ 48
   17 MCP query tools for codebase navigation — functions, classes, imports, dependency graphs, change impact. Zero dependencies. 87% token reduction.

2825. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 48
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

2826. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

2827. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

2828. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

2829. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 48
   Official MCP Server for Buildkite.

2830. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 48
   A comprehensive MCP server for Metabase with 70+ tools.

2831. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 48
   Remote MCP server that gives LLMs access to run network commands

2832. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 48
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

2833. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 48
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

2834. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

2835. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2836. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 48
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

2837. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 48
   Model Context Protocol to fetch youtube transcript

2838. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 48
   mcp server to run scripts on adobe illustrator

2839. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 48
   Un-official Serper Google search server for Cline and other MCP clients

2840. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

2841. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

2842. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 48
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2843. **[claude-plugins](https://github.com/2389-research/claude-plugins)** - ⭐ 48
   28 plugins and MCP servers for Claude Code — TDD, multi-agent orchestration, iterative refinement, binary RE, structured decisions. Install any skill in one command.

2844. **[Kaimon.jl](https://github.com/kahliburke/Kaimon.jl)** - ⭐ 48
   MCP server giving AI agents full access to Julia's runtime via a live Gate — code execution, introspection, debugging, testing, and semantic search

2845. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 48
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2846. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 48
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

2847. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2848. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 48
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

2849. **[devswarm](https://github.com/justrach/devswarm)** - ⭐ 48
   High-performance MCP server, code graph engine & evolutionary algorithm platform in Zig. 33 tools: GitHub project management, agent swarm orchestration, iterative review-fix loops, blast radius analysis, and code navigation via Model Context Protocol.

2850. **[js](https://github.com/mcp-auth/js)** - ⭐ 48
   🔐 Plug-and-play auth for Node.js MCP servers.

2851. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 48
   Enhanced MCP server for GitLab: group projects listing and activity tracking

2852. **[slack-mcp-plugin](https://github.com/slackapi/slack-mcp-plugin)** - ⭐ 48
   Repo containing the configuration information for the Slack MCP to be added to other clients

2853. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 47
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2854. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 47
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

2855. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

2856. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

2857. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

2858. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 47
   Grant the AI octopus access to a portion of your desktop

2859. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 47
   Dremio MCP server

2860. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 47
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

2861. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 47
   OpenAPI Schema Model Context Protocol Server

2862. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 47
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2863. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 47
   Enhanced Zen MCP Server with 'zen' default tool and improvements

2864. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 47
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

2865. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 47
   Sample MCP Server and MCP client with Aspire

2866. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 47
   A production-ready Model Context Protocol (MCP) server for semantic memory management

2867. **[oh-my-codex](https://github.com/scalarian/oh-my-codex)** - ⭐ 47
   oh-my-codex (omx) — Orchestration layer for OpenAI Codex CLI. Async Claude Code delegation (no timeouts), structured workflows (autopilot, TDD, code review, planning), persistent state & memory. Like oh-my-zsh but for Codex.

2868. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 47
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2869. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 47
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

2870. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 47
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2871. **[sharedcontext](https://github.com/Eversmile12/sharedcontext)** - ⭐ 47
   MCP server that gives AI coding assistants persistent cross-client memory. Facts and conversations stored in SQLite, encrypted with AES-256-GCM, synced to Arweave. No server, no account, recoverable with a 12-word phrase.

2872. **[mcp-workspace](https://github.com/MarcusJellinghaus/mcp-workspace)** - ⭐ 47
   MCP Workspace Server: A secure Model Context Protocol server providing file, git, and GitHub tools for AI assistants within a sandboxed project directory.

2873. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 47
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2874. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 47
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

2875. **[roblox-executor-mcp](https://github.com/notpoiu/roblox-executor-mcp)** - ⭐ 47
   A MCP Server which allows for direct access to the roblox game client

2876. **[synapse-ai](https://github.com/naveenraj-17/synapse-ai)** - ⭐ 47
   Build AI agents that actually do things. Synapse is an open-source platform for creating, connecting, and orchestrating AI agents powered by any LLM — local, cloud or CLIs.

2877. **[MCP-Trust-Kit](https://github.com/aak204/MCP-Trust-Kit)** - ⭐ 46
   Deterministic CI scanner and surface-risk scoring for MCP (Model Context Protocol) servers.

2878. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 46
   共学《MCP极简开发》项目代码

2879. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

2880. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

2881. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 46
   Model Context Protocol server for Flight Tracking

2882. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 46
   MCPcat is an analytics platform for MCP server owners 🐱.

2883. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 46
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

2884. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 46
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

2885. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 46
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

2886. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 46
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2887. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

2888. **[claude-additional-models-mcp](https://github.com/Arkya-AI/claude-additional-models-mcp)** - ⭐ 46
   Reduce Claude Desktop consumption by 10x - Integrate Google's Gemini or Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

2889. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

2890. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 46
   An implementation of the Model Context Protocol for the World Bank open data API

2891. **[Generative-UI-MCP](https://github.com/op7418/Generative-UI-MCP)** - ⭐ 46
   MCP server that teaches AI models to generate interactive visualizations — charts, diagrams, mockups, and more.

2892. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 46
   An opinionated starter template for making Model Context Protocol (MCP) servers

2893. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 46
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2894. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2895. **[tomtom-maps-mcp](https://github.com/tomtom-international/tomtom-maps-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2896. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 46
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2897. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 46
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

2898. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 46
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

2899. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 46
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2900. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 46
   The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2901. **[dataworkers-claw-community](https://github.com/DataWorkersProject/dataworkers-claw-community)** - ⭐ 45
   We’re build a swarm of agents for all data tasks. That anyone can use for free, open-source community version.  

2902. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 45
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

2903. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 45
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

2904. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 45
   ElizaOS plugin allowing agents to connect to MCP servers

2905. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

2906. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

2907. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

2908. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 45
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

2909. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 45
   Create the prompts you need to write your Novel using AI

2910. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 45
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

2911. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 45
   MCP server for golang projects development: Expand AI Code Agent ability boundary to have a semantic understanding and determinisic information for golang projects.

2912. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 45
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

2913. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

2914. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 45
   GraphQL Schema Model Context Protocol Server

2915. **[bonnard-cli](https://github.com/bonnard-data/bonnard-cli)** - ⭐ 45
   Open-source agentic schema CLI. Optimised for claude code, gemini, codex and co-pilot. Skills included.

2916. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 45
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

2917. **[aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol](https://github.com/microsoft/aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol)** - ⭐ 45

2918. **[mcpx](https://github.com/lydakis/mcpx)** - ⭐ 45
   Turn MCP servers into composable CLIs.

2919. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 45
   A Model Context Protocol (MCP) server for NATS messaging system integration

2920. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 45
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2921. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 45
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

2922. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 45
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

2923. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 45
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

2924. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 45
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

2925. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 45
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

2926. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 45
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2927. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 45
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2928. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 44
   Model Context Protocol server for Salesforce REST API integration

2929. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 44
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

2930. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 44
   Moondream MCP Server in Python

2931. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

2932. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

2933. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

2934. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

2935. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 44
   An MCP server to allow you to debug webpages using LLMs

2936. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 44
   Yandex Tracker MCP Server with OAuth2 support

2937. **[adal-cli](https://github.com/SylphAI-Inc/adal-cli)** - ⭐ 44
   The self-evolving coding agent that learns from your entire team and codebase. Less syncing. Less waiting. Deliver at the speed of thought.

2938. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 44
   Model Context Protocol Platform，统一管理你的MCP服务

2939. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 44
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

2940. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 44
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

2941. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

2942. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 44
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

2943. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 44
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2944. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 44
   Open source local MCP server providing AI assistants with comprehensive access to eBay's Sell APIs. Includes 325 tools for inventory management, order fulfillment, marketing campaigns, analytics, developer tools, and more.

2945. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 44
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

2946. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

2947. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 44
   A curated list of excellent Model Context Protocol (MCP) servers.

2948. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 44
   Algorand Local Model Context Protocol (Server & Client)

2949. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 44
   A Model Context Protocol server implementation for Kagi's API

2950. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 44
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

2951. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 44
   Model Context Protocol (MCP) server for LinkedIn API integration

2952. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 44
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2953. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 44
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

2954. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 44
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2955. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 44
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2956. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 44
   Command-line interface for any Model Context Protocol (MCP) server.

2957. **[Dragon-Brain](https://github.com/iikarus/Dragon-Brain)** - ⭐ 44
   Dragon Brain — persistent long-term memory for AI agents via MCP (Model Context Protocol). Knowledge graph (FalkorDB) + vector search (Qdrant) + CUDA GPU embeddings. Works with Claude, Gemini CLI, Cursor, Windsurf, VS Code Copilot. 30 tools, 1121 tests.

2958. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 44
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2959. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 44
   Bluesky MCP (Model Context Protocol) Server

2960. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 44
   Arch Linux MCP (Model Context Protocol) Server

2961. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 43
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2962. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 43
   Quantum-proof MCP Server and Client Interactions

2963. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 43
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

2964. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

2965. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

2966. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

2967. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

2968. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

2969. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

2970. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 43
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

2971. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 43
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows, Linux, Claude App etc

2972. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 43
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

2973. **[lastsaas](https://github.com/jonradoff/lastsaas)** - ⭐ 43
   SaaS boilerplate/starter-kit in Go+React with Stripe integration, multi-tenant support, comprehensive features and AI-agent ready

2974. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 43
   Solana Model Context Protocol (MCP) Demo

2975. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 43
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2976. **[AgentTools](https://github.com/WolframResearch/AgentTools)** - ⭐ 43
   Implements a model context protocol server using Wolfram Language

2977. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 43
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2978. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 43
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2979. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 43
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2980. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 43
   Sync MCP (Model Context Protocol) configurations across AI tools

2981. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 43
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

2982. **[mcp-musescore](https://github.com/ghchen99/mcp-musescore)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides programmatic control over MuseScore!

2983. **[music-composer-webmcp](https://github.com/Leanmcp-Community/music-composer-webmcp)** - ⭐ 43
   This WebMCP Music Composer project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with local browser contexts (tools) to achieve complex workflows autonomously.

2984. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 43
   model context protocol for Autodesk Revit

2985. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 43
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2986. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

2987. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

2988. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

2989. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 42
   WhatsApp Unofficial MCP Server

2990. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 42
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

2991. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 42
   台灣證交所OpenAPI 的 MCP Server

2992. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 42
   Rimworld Coding RAG MCP server

2993. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 42
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

2994. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 42
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

2995. **[getnote-mcp](https://github.com/iswalle/getnote-mcp)** - ⭐ 42
   GetNote For MCP

2996. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 42
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2997. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 42
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2998. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 42
   A generic, modular server for implementing the Model Context Protocol (MCP). 

2999. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 42
   Claude Unified Model Context Interaction Protocol

3000. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 42
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

3001. **[mie](https://github.com/kraklabs/mie)** - ⭐ 42
   Persistent memory graph for AI agents. Facts, decisions, entities, and relationships that survive across sessions, tools, and providers. MCP server — works with Claude, Cursor, ChatGPT, and any MCP client.

3002. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 42
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

3003. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 42
   Model Context Protocol server for Sitecore

3004. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 42
   Emacs Lisp implementation of the Model Context Protocol

3005. **[amazon_ads_mcp](https://github.com/KuudoAI/amazon_ads_mcp)** - ⭐ 42
   Amazon Ads MCP - Model Context Protocol server for Amazon Advertising API

3006. **[arifos](https://github.com/ariffazil/arifos)** - ⭐ 42
   ArifOS — Constitutional MCP kernel for governed AI execution. AAA architecture: Architect · Auditor · Agent. Built for the open-source agentic era.

3007. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 42
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

3008. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 42
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

3009. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 41
   Model Context Protocol (MCP) implementation for iOS simulators

3010. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   MCP server that exposes YepCode processes as callable tools for AI platforms. Securely connect AI assistants to your YepCode workflows, APIs, and automations.

3011. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

3012. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

3013. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

3014. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

3015. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

3016. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

3017. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 41
   MCP server for Obsidian (TypeScript + Bun)

3018. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 41
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

3019. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 41
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

3020. **[processhacker-mcp](https://github.com/illegal-instruction-co/processhacker-mcp)** - ⭐ 41
   your ai debugger, vibe hacking tool

3021. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 41

3022. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 41
   A hackable Model Context Protocol (MCP) gateway

3023. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 41
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

3024. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 41
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

3025. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 41
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

3026. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 41
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

3027. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 41
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

3028. **[arifOS](https://github.com/ariffazil/arifOS)** - ⭐ 41
   ArifOS — Constitutional MCP kernel for governed AI execution. AAA architecture: Architect · Auditor · Agent. Built for the open-source agentic era.

3029. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 41
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

3030. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 41
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

3031. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 41
   Learn Model Context Protocol with Python, published by Packt

3032. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 41
   A Model Context Protocol server that provides access to Shodan API functionality

3033. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 41
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

3034. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 41
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

3035. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 41
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

3036. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 41
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

3037. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 41
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

3038. **[TalkToFigmaDesktop](https://github.com/grab/TalkToFigmaDesktop)** - ⭐ 41
   A powerful desktop application bridging Figma and AI tools via Model Context Protocol Seamless integration between Figma designs and AI assistants

3039. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 41
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

3040. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 41
   ElysiaJS plugin for Model Context Protocol with HTTP transport

3041. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

3042. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 40
   a mcp server for polymarket

3043. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

3044. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

3045. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

3046. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

3047. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 40
   Write detections, investigate alerts, and query logs from your favorite AI agents

3048. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 40
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

3049. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 40
   PDF RAG server for cursor.

3050. **[bonnard-cli](https://github.com/meal-inc/bonnard-cli)** - ⭐ 40
   Agent-native analytics. MCP server, dashboards, SDK, and semantic layer CLI.

3051. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 40
   Apple Books MCP Server

3052. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 40
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

3053. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 40
   It shows how to use model-context-protocol. 

3054. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 40
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

3055. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 40
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

3056. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 40
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

3057. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 40
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

3058. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 40
   An MCP server for querying Solana transactions using natural language with Solscan API

3059. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 40
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

3060. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 40
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

3061. **[rustchain-mcp](https://github.com/Scottcjn/rustchain-mcp)** - ⭐ 40
   MCP server for RustChain blockchain and BoTTube video platform — AI agent tools for earning RTC tokens. Built on createkr's RustChain SDK.

3062. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 40
   http4k MCP Desktop Client

3063. **[agent-trace](https://github.com/Siddhant-K-code/agent-trace)** - ⭐ 40
   strace for AI agents. Capture and replay every tool call, prompt, and response from Claude Code, Cursor, Gemini CLI or any MCP client

3064. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 40
   Tools for building modern & secure MCP integrations across the client and server side

3065. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 40
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

3066. **[NepseAPI-Unofficial](https://github.com/surajrimal07/NepseAPI-Unofficial)** - ⭐ 40
   Unlock Nepal Stock Exchange (NEPSE) data with this powerful unofficial API. Features REST, WebSocket, and a first-of-its-kind Model Context Protocol (MCP) server, enabling AI models like Claude to perform live market analysis with over 20 specialized tools. Strictly for educational and non-commercial use.

3067. **[RedTeam-Agent](https://github.com/ktol1/RedTeam-Agent)** - ⭐ 40
    RedTeam-Agent: AI-Powered Autonomous Red Team Framework via Model Context Protocol. AI红队与内网渗透自动化框架，支持 gogo, fscan, httpx, nuclei, impacket, playwright 等 15+ 渗透工具，让 LLM 直接化身安全审计黑客。

3068. **[iota-agent-mcp](https://github.com/Scottcjn/iota-agent-mcp)** - ⭐ 40
   MCP server for IOTA blockchain — 20 tools for AI agent integration (wallet, Move CLI, on-chain queries via Model Context Protocol)

3069. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 39
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

3070. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 39
   MCP server for anki

3071. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

3072. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

3073. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

3074. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

3075. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

3076. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

3077. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 39
   Self-hosted Stealth Scraping & Federated Search for AI Agents. A 100% private, free alternative to Firecrawl, Jina Reader, and Tavily. Featuring Universal Anti-bot Bypass + Semantic Research Memory, Copy-Paste setup

3078. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 39
   Enable AI assistants to explore and query your Steampipe data!

3079. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 39
   A MCP server for Storybook.

3080. **[best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** - ⭐ 39
   🏆  A ranked list of MCP servers. Updated weekly.

3081. **[arifosmcp](https://github.com/ariffazil/arifosmcp)** - ⭐ 39
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

3082. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

3083. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 39
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

3084. **[mcp-server](https://github.com/Aayush9029/mcp-server)** - ⭐ 39
   MCP SERVER

3085. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 39
   Model Context Protocol Minecraft Server

3086. **[roampal-core](https://github.com/roampal-ai/roampal-core)** - ⭐ 39
   Outcome-based persistent memory MCP server for Claude Code and OpenCode. Good advice promoted, bad advice demoted. pip install roampal.

3087. **[camofox-mcp](https://github.com/redf0x1/camofox-mcp)** - ⭐ 39
   Anti-detection browser MCP server for AI agents — navigate, interact, and automate the web without getting blocked

3088. **[golemcore-bot](https://github.com/alexk-dev/golemcore-bot)** - ⭐ 39
   AI-native runtime for the GolemCore ecosystem with skills, plugins, MCP, memory, and Hive.

3089. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 39
   Generate a map of your codebaseto help AI Agents understand your architecture, coding conventions and patterns. Discoverable with Semantic Search

3090. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 39
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

3091. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 39
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

3092. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 39
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

3093. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 39
   Telegram MCP server with HTTP-MTProto Bridge — direct API/curl access, multi-user Bearer auth, Docker, MTProto proxy, file attachments, voice transcription, context-optimized

3094. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

3095. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 39
   A Chat Client for LLMs, written in Compose Multiplatform.

3096. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 39
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

3097. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 39

3098. **[pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp)** - ⭐ 39
   Model Context Protocol (MCP) server for AI-powered reservoir engineering calculations. Integrates pyResToolbox with Claude AI for PVT analysis, well   performance, simulation support, and more. 47 production-ready tools using industry-standard correlations.

3099. **[email-mcp](https://github.com/codefuturist/email-mcp)** - ⭐ 39
   Email MCP server with full IMAP + SMTP support — read, search, send, manage, and organize email from any AI assistant via the Model Context Protocol

3100. **[SpecialAgentPlugin](https://github.com/ArtisanGameworks/SpecialAgentPlugin)** - ⭐ 39
   SpecialAgent is an Unreal Engine 5 plugin that implements a Model Context Protocol (MCP)  server, allowing Large Language Models like Claude to programmatically interact with UE5  projects. With 71+ tool endpoints across 14 service categories, LLMs gain comprehensive control for building complex 3D environments.

3101. **[fusion360-claude-ultimate](https://github.com/Misterbra/fusion360-claude-ultimate)** - ⭐ 39
   🤖 Control Fusion 360 with natural language through Claude Desktop using MCP (Model Context Protocol). Create, manipulate and modify 3D objects by simply describing what you want to do. French-localized adaptation of Kanbara Tomonori's original concept.

3102. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 38
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

3103. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 38
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

3104. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 38
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

3105. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 38
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

3106. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 38
   A package manager to manage all your mcp servers across platforms

3107. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 38
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

3108. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

3109. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

3110. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

3111. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

3112. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

3113. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 38
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

3114. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 38
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

3115. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 38
   Highly configurable autonomous efficient-first agentic AI framework for CLI

3116. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 38
   awesome-lists now available as MCP server for you agent.

3117. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 38
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

3118. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 38
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

3119. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 38
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

3120. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 38
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

3121. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 38
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

3122. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 38
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

3123. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 38
   Model Context Protocol server to let LLMs write and execute matlab scripts 

3124. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 38
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

3125. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 38
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

3126. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 38
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

3127. **[trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp)** - ⭐ 38
   TrainingPeaks MCP server for Claude Desktop, Code and Cowork. No API approval needed - works with any account. Query workouts, CTL/ATL/TSB fitness data, power PRs via natural language.

3128. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 38
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

3129. **[xero-agent-toolkit](https://github.com/XeroAPI/xero-agent-toolkit)** - ⭐ 38
   A collection of examples demonstrating how to build AI agents that integrate with the Xero API using various agentic frameworks and the Xero MCP (Model Context Protocol) Server.

3130. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 38
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

3131. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 38
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

3132. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 38
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

3133. **[mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp)** - ⭐ 38
   A Model-Context Protocol server for the MITRE ATT&CK knowledge base

3134. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 38
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

3135. **[OpenInsider-MCP](https://github.com/btopn/OpenInsider-MCP)** - ⭐ 38
   MCP server that exposes openinsider.com to any MCP compatible client.

3136. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 38
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

3137. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 38
   Zillow MCP Server for real estate data access via the Model Context Protocol

3138. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 38
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

3139. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 38
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

3140. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 38
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

3141. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 38
   Build Model Context Protocol (MCP) servers in Go

3142. **[zapier-mcp](https://github.com/zapier/zapier-mcp)** - ⭐ 38
   Connect your AI to thousands of apps with the Model Context Protocol.

3143. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 38
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3144. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 37
   Trivy plugin for starting an MCP server

3145. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

3146. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 37
   MCP server tailored to connecting web crawler data and archives

3147. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 37
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

3148. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

3149. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

3150. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

3151. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

3152. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 37
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

3153. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 37
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

3154. **[google-workspace-mcp](https://github.com/dguido/google-workspace-mcp)** - ⭐ 37
   MCP server for Google Drive, Docs, Sheets, Slides, Calendar, Gmail, and Contacts

3155. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 37
   An MCP server for Android's Tasker automation app.

3156. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 37
   A simple note-taking MCP server for recording and managing notes with AI models.

3157. **[godot-mcp](https://github.com/HaD0Yun/godot-mcp)** - ⭐ 37
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

3158. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 37
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

3159. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 37
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

3160. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 37
   Model Context Protocol (MCP) server that interacts with a Debugger

3161. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 37
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

3162. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

3163. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 37
   Demonstrate how to implement MCP Client in Flutter application with AI.

3164. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 37
   a lib to build MCP clients and MCP servers in Clojure(script)

3165. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 37
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

3166. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 37
   List of Awesome MCP Servers and Clients for building Agentic Devops 

3167. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 37
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

3168. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 37
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

3169. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 37
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

3170. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 37
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

3171. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 37
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

3172. **[vulnerablemcp](https://github.com/vineethsai/vulnerablemcp)** - ⭐ 37
   A comprehensive database of Model Context Protocol vulnerabilities, security research, and exploits

3173. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 37
   Model Context Protocol (MCP) Server for Mistral OCR API

3174. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 37
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

3175. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 37
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

3176. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 37
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

3177. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server and app for creating Datawrapper charts using AI assistants.

3178. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

3179. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

3180. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

3181. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

3182. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

3183. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

3184. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 36
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

3185. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 36
   A2A Protocol client and developer toolkit.

3186. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 36
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

3187. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 36
   Python sandboxes for llms

3188. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 36
   A curated collection of persona-based mcp server & tool groupings.

3189. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 36
   Vapi MCP Server

3190. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 36
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

3191. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 36
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

3192. **[apple-mail-mcp](https://github.com/patrickfreyer/apple-mail-mcp)** - ⭐ 36
   MCP server giving AI assistants full access to Apple Mail - read, search, compose, organize & analyze emails via natural language

3193. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 36
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

3194. **[ronykit](https://github.com/clubpay/ronykit)** - ⭐ 36
   API Framework supporting REST and RPC.

3195. **[agience-core](https://github.com/Agience/agience-core)** - ⭐ 36
   An open, extensible runtime for agentic AI. Shared artifacts, structured state, and provenance by default.

3196. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

3197. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 36
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

3198. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 36
   A super simple Starter to build your own MCP Server

3199. **[kimi-code-mcp](https://github.com/howardpen9/kimi-code-mcp)** - ⭐ 36
   MCP server for Claude Code × Kimi K2.5 (256K context) — delegate bulk codebase analysis to Kimi, save 90% on token costs. Session caching, parallel agents, TypeScript.

3200. **[ckan-mcp-server](https://github.com/ondata/ckan-mcp-server)** - ⭐ 36
   MCP server for querying CKAN open data portals (package search, DataStore SQL, organizations, groups, tags)

3201. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 36
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

3202. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 36
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

3203. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 36
   Model Context Protocol (MCP) server for openBIM

3204. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 36
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

3205. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 36
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

3206. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 36
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

3207. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

3208. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 36
   esa の Model Context Protocol サーバー実装

3209. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 36
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

3210. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 36
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

3211. **[CE-MCP-Plugin](https://github.com/Eruditi/CE-MCP-Plugin)** - ⭐ 36
   CE MCP Plugin是一个Cheat Engine插件，它实现了Model Context Protocol (MCP)，允许AI模型与Cheat Engine进行交互。通过这个插件，AI可以使用Cheat Engine的各种功能，如内存读写、进程管理等。

3212. **[levante](https://github.com/levante-hub/levante)** - ⭐ 36
   Levante - Personal, Secure, Free, Local AI, MCP Client

3213. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 36
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

3214. **[mcp-dblp](https://github.com/szeider/mcp-dblp)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides access to the DBLP computer science bibliography database for Large Language Models.

3215. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 36
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

3216. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 36
   Wwise-MCP is a Model Context Protocol (MCP) server that enables large language models (LLMs) to interact with the Wwise Authoring application. It exposes a set of tools built on a custom Python WAAPI library, allowing MCP clients such as Claude or Cursor to automate and compose complex, multi-step Wwise workflows.

3217. **[claude-image-gen](https://github.com/guinacio/claude-image-gen)** - ⭐ 36
   AI-powered image generation using Google Gemini, integrated with Claude Code via Skills or Claude.ai via MCP (Model Context Protocol).

3218. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 36
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

3219. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 35
   OpenAI Code Assistant Model Context Protocol (MCP) Server

3220. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

3221. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

3222. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

3223. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

3224. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

3225. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 35
   An open source implementation of the Claude built-in text editor tool

3226. **[daisyui-mcp](https://github.com/birdseyevue/daisyui-mcp)** - ⭐ 35
   🌼 A token-friendly local MCP server for DaisyUI component documentation using their public llms.txt.

3227. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 35
   Turn any MCP Client into a "multi-agent" system (via prompting)

3228. **[awesome-mcp-servers](https://github.com/ever-works/awesome-mcp-servers)** - ⭐ 35
   A curated list of the best MCP Servers, featuring top solutions, libraries, tools, and more. - https://mcpserver.works

3229. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 35
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

3230. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 35
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3231. **[mcp](https://github.com/fastly/mcp)** - ⭐ 35
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

3232. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 35
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

3233. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 35
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

3234. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 35
   About A Model Context Protocol server that executes commands in the current WezTerm session

3235. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 35
   Model Context Protocol extension for Azure Functions.

3236. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 35
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

3237. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 35
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

3238. **[chabeau](https://github.com/permacommons/chabeau)** - ⭐ 35
   OpenAI-API compatible terminal chatbot and MCP client in Rust

3239. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 35
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

3240. **[inkmcp](https://github.com/Shriinivas/inkmcp)** - ⭐ 35
   Inkscape MCP Server - Control Inkscape through AI assistants via Model Context Protocol

3241. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

3242. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 35
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

3243. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 35
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

3244. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 35
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

3245. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

3246. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

3247. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

3248. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

3249. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 34
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

3250. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform. 

3251. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

3252. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

3253. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

3254. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 34
   Model Context Protocol server written in Scala

3255. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 34
   Apache IoTDB MCP Server

3256. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 34
   Let your agent write code and execute code directly in the browser with WASM

3257. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 34
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

3258. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 34
   An MCP server that allows users to dynamically add custom tools/functions at runtime

3259. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 34
   A MCP implementation for sending notifications via Pushover

3260. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 34
   Capacities×MCP

3261. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 34
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

3262. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 34
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

3263. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

3264. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 34
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

3265. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 34
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

3266. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 34
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

3267. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 34
   Implements a model context protocol server using Wolfram Language

3268. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 34
   A generic mcp server fuzzer

3269. **[review-flow](https://github.com/DGouron/review-flow)** - ⭐ 34
   Automated AI code reviews powered — webhook-driven, real-time dashboard, MCP integration, smart queue with deduplication, multi-agent audits, and iterative follow-up reviews for GitLab MRs and GitHub PRs

3270. **[context-harness](https://github.com/parallax-labs/context-harness)** - ⭐ 34
   Local-first context ingestion and retrieval for AI tools. SQLite + embeddings + MCP server for Cursor & Claude.

3271. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 34
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

3272. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 34
   Minimal Metals stand alone client that allows running the metals mcp server

3273. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 34
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

3274. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 34
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

3275. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

3276. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 34
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

3277. **[pentester-mcp](https://github.com/halilkirazkaya/pentester-mcp)** - ⭐ 34
   Elevate your AI assistants (like Claude & Cursor) into autonomous cybersecurity experts. Pentester-MCP integrates 200+ pentesting tools via the Model Context Protocol (MCP) using a secure Docker sandbox.

3278. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

3279. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 34
   Awesome list of MCP servers for interacting with hardware and the physical world.

3280. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3281. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 34
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

3282. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 34
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

3283. **[onec-client-mcp-devkit](https://github.com/1c-neurofish/onec-client-mcp-devkit)** - ⭐ 34
   Реализация MCP сервера, который запускается в клиенте 1С:Предприятие

3284. **[Mira](https://github.com/vwww-droid/Mira)** - ⭐ 34
   🔬 Mobile runtime detection workbench (iOS and Android)

3285. **[mTarsier](https://github.com/mcp360/mTarsier)** - ⭐ 33
   mTarsier - The Open Source MCP & Skill Manager for Claude, Cursor, VS Code & any AI client.

3286. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 33
   MCP Server connects with claude code local command.

3287. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 33
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

3288. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

3289. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

3290. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

3291. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

3292. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 33
   MCP Server for Membrane

3293. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 33
   Minimalist AI agent that fixes itself when things break.

3294. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 33
   AI-Powered Threat Intelligence MCP tool

3295. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 33
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

3296. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 33
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi. 

3297. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 33
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

3298. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 33
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

3299. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 33
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

3300. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 33
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

3301. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 33
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

3302. **[awesome-finance-mcp](https://github.com/BlockRunAI/awesome-finance-mcp)** - ⭐ 33
   A curated list of MCP servers for AI finance agents

3303. **[ue5-mcp-bridge](https://github.com/Natfii/ue5-mcp-bridge)** - ⭐ 33
   MCP server bridging AI assistants to Unreal Engine 5 editor

3304. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 33
   Query model running with Ollama from within Claude Desktop or other MCP clients

3305. **[apipost-mcp](https://github.com/jlcodes99/apipost-mcp)** - ⭐ 33
   ApiPost API management tool based on MCP (Model Context Protocol), supporting complete interface documentation management and team collaboration. Features intelligent search, batch operations, and security management.

3306. **[mcp-gateway](https://github.com/openziti/mcp-gateway)** - ⭐ 33
   Zero trust gateway for MCP servers. Aggregate, filter, and securely access MCP tools from anywhere without VPNs, open ports, or exposed           endpoints. Built on OpenZiti and zrok with cryptographic identity, mTLS, per-client isolation, and tool-level permission control.                    

3307. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 33
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

3308. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 33
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

3309. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 33
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

3310. **[lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server exposing Lucide icons as resources and tools for LLMs and agentic applications. Built with Bun and the MCP TypeScript SDK.

3311. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 33
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with OpenAI and 🌐 web browser control via Playwright.

3312. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 33
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

3313. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 33
   Asterisk Model Context Protocol (MCP) server.

3314. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 33
   A Curated List of MCP Servers, Clients and Toolkits

3315. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 33
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

3316. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 33
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

3317. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 33
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

3318. **[tally-mcp-server](https://github.com/dhananjay1405/tally-mcp-server)** - ⭐ 33
   Tally Prime MCP (Model Context Protocol) Server implementation to feed Tally ERP data to popular LLM like Claude, ChatGPT supporting MCP

3319. **[mcp_xpp](https://github.com/ccampora/mcp_xpp)** - ⭐ 33
   Experimental MCP server for Dynamics 365 F&O X++ development. Provides object creation, modification, and codebase navigation through the Model Context Protocol. Includes VS2022 service integration for D365 object handling.

3320. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 33
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3321. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 33
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3322. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 33
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

3323. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 33
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + Java + TypeScript

3324. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 33
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

3325. **[SSH-MCP](https://github.com/mixelpixx/SSH-MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides SSH access to remote servers, allowing AI tools like Claude Desktop or VS Code to securely connect to your VPS.

3326. **[screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp)** - ⭐ 33
   MCP server for Screaming Frog SEO Spider – crawl sites, export data, and manage crawl storage via Claude or any MCP-compatible client

3327. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 32
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

3328. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 32
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

3329. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

3330. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

3331. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

3332. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

3333. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

3334. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

3335. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 32
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

3336. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 32
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

3337. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 32
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

3338. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 32
   A Model Context Protocol server starter template

3339. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 32
   A collection of MCP server examples developed by various Java SDKs

3340. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 32
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

3341. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

3342. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 32
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

3343. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 32
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

3344. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 32
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

3345. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 32
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3346. **[hop](https://github.com/danmartuszewski/hop)** - ⭐ 32
   Fast, elegant SSH connection manager with a TUI dashboard and MCP server

3347. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 32
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

3348. **[orionbelt-semantic-layer](https://github.com/ralfbecher/orionbelt-semantic-layer)** - ⭐ 32
   API-first semantic engine and query planner for AI agents that compiles declarative YAML models into optimized, dialect-specific SQL across BigQuery, PostgreSQL, Snowflake, ClickHouse, Dremio, Databricks, DuckDB, and MySQL.

3349. **[dassian-adt](https://github.com/DassianInc/dassian-adt)** - ⭐ 32
   MCP server for SAP ABAP development via ADT API. Connect AI assistants to SAP: read, write, test, and deploy ABAP code without SAP GUI.

3350. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 32
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

3351. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 32
   Model Context Protocol Server of Rod

3352. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 32
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

3353. **[unplugin-devpilot](https://github.com/zcf0508/unplugin-devpilot)** - ⭐ 32
   A universal plugin framework for development tools that enables seamless browser-server communication and MCP (Model Context Protocol) integration with AI/LLM systems.

3354. **[douyin-mcp-server](https://github.com/lancelin111/douyin-mcp-server)** - ⭐ 32
   🎥 Douyin (TikTok China) MCP Server - Automated video upload service via Model Context Protocol for AI integration

3355. **[drafts-mcp-server](https://github.com/agiletortoise/drafts-mcp-server)** - ⭐ 32
   Model Context Protocol for Drafts

3356. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 32
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

3357. **[google-researcher-mcp](https://github.com/zoharbabin/google-researcher-mcp)** - ⭐ 32
   This is a Model Context Protocol (MCP) server that enables AI assistants like Claude, GPT, and other LLMs to:  Search the web via Google (general, images, news) Read any webpage including JavaScript-rendered sites Extract YouTube transcripts automatically Parse documents (PDF, DOCX, PPTX)

3358. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

3359. **[myBrAIn](https://github.com/lilium360/myBrAIn)** - ⭐ 31
   myBrAIn is an MCP (Model Context Protocol) server designed to provide persistent and contextual memory to language models (like Google Antigravity). It acts as a "second brain" for your development environment, allowing the AI to remember project rules, architectural decisions, and technical insights across different chat sessions

3360. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

3361. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 31
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

3362. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

3363. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

3364. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

3365. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32. 

3366. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 31
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

3367. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

3368. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 31
   一個簡單易用的網頁工具，用於管理 GitHub Copilot Coding Agent 的 MCP (Model Context Protocol) 設定

3369. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 31
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

3370. **[rss-mcp](https://github.com/veithly/rss-mcp)** - ⭐ 31
   This is a Model Context Protocol (MCP) server built with TypeScript. It provides a versatile tool to fetch and parse any standard RSS/Atom feed, and also includes special support for RSSHub feeds. 

3371. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 31
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

3372. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 31
   MCP (Model Context Protocol) server for biothings

3373. **[mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm)** - ⭐ 31
   MCP server for Klever blockchain smart contract development

3374. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 31
   Convert source code to LLM ready knowledge base

3375. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 31
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

3376. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 31
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

3377. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 31
   PowerPlatform Model Context Protocol server

3378. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 31
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

3379. **[mcp-marketplace](https://github.com/aiagenta2z/mcp-marketplace)** - ⭐ 31
   OpenSource MCP Marketplace | MCP Servers Tools Meta Dataset | Web API | Web Client Integration

3380. **[stitch-mcp-auto](https://github.com/GreenSheep01201/stitch-mcp-auto)** - ⭐ 31
   Automated installer for Stitch MCP - The easiest way to set up your Universal MCP server for Google Stitch.

3381. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 31
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

3382. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 31
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

3383. **[pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server)** - ⭐ 31
   PubNub MCP Model Context Protocol Server for use in Cursor, Windsurf, Claude Desktop, Claude Code and OpenAI Codex and more!

3384. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 31
   A Model Context Protocol server for 3D Slicer integration

3385. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 31
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

3386. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 31
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

3387. **[listmonk-mcp](https://github.com/rhnvrm/listmonk-mcp)** - ⭐ 31
   MCP (Model Context Protocol) server for Listmonk newsletter management

3388. **[minimal-godot-mcp](https://github.com/ryanmazzolini/minimal-godot-mcp)** - ⭐ 31
   Lightweight MCP server bridging Godot LSP to MCP clients for GDScript validation

3389. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 30
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

3390. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 30
   MCP (Model Context Protocol) Server for postgres Database

3391. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 30
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

3392. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 30
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

3393. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 30
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

3394. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

3395. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

3396. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

3397. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

3398. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

3399. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

3400. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

3401. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

3402. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 30
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

3403. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 30
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

3404. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 30
   A simple Model Context Protocol (MCP) server for Clay.

3405. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

3406. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 30
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

3407. **[mcp-loxone](https://github.com/avrabe/mcp-loxone)** - ⭐ 30
   An opinionated Model Context Protocol (MCP) server for controlling Loxone home automation systems.

3408. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 30
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

3409. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 30
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

3410. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 30
   ESPN Fantasy API with LLMs!

3411. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 30
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

3412. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 30
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3413. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 30
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

3414. **[fcpxml-mcp-server](https://github.com/DareDev256/fcpxml-mcp-server)** - ⭐ 30
   🎬 The first AI-powered MCP server for Final Cut Pro XML. Control your edits with natural language.

3415. **[ads-mcp](https://github.com/amekala/ads-mcp)** - ⭐ 30
   MCP server for managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. 100+ tools for campaign creation, performance analysis, keyword research, and budget optimization. Works with ChatGPT, Claude, Gemini CLI, Cursor, Codex, and Windsurf.

3416. **[aura](https://github.com/mezmo/aura)** - ⭐ 30
   A production-ready framework for composing AI agents from declarative TOML configuration, with MCP tool integration, RAG pipelines, and an OpenAI-compatible web API.

3417. **[OmniClip-RAG](https://github.com/msjsc001/OmniClip-RAG)** - ⭐ 30
   Local-first RAG desktop app & official MCP Server. Let any AI instantly search your private Markdown, PDF, and 1290+ document formats. (本地优先的 RAG 桌面端与官方 MCP 服务器。让任意 AI 瞬间检索你的私有 Markdown、PDF 及 1290+ 种文档格式。)

3418. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 30
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

3419. **[binance-mcp-server](https://github.com/ethancod1ng/binance-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server for integrating AI assistants with Binance cryptocurrency exchange APIs, enabling automated trading, market data access, and account management.

3420. **[OmnifocusMCP](https://github.com/vitalyrodnenko/OmnifocusMCP)** - ⭐ 30
   Model Context Protocol (MCP) server for OmniFocus on macOS, with Rust, Python, and TypeScript implementations

3421. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 30
   MCP (Model Context Protocol) server for Dumpling AI

3422. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 30
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

3423. **[mdk-mcp-server](https://github.com/SAP/mdk-mcp-server)** - ⭐ 30
   Model Context Protocol (MCP) server for AI-assisted development ("vibe coding") of MDK applications.

3424. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 30
   Fast rust MCP proxy between stdio and SSE

3425. **[VS-MCPServer](https://github.com/CodingWithCalvin/VS-MCPServer)** - ⭐ 30
   VS MCP Server exposes Visual Studio features through the Model Context Protocol (MCP), enabling AI assistants like Claude to interact with your IDE programmatically. Open files, read code, build projects, and more - all through natural conversation!

3426. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 30
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

3427. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

3428. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 30
   Yandex Cloud MCP Servers

3429. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 30
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

3430. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 30
   A Model Context Protocol (MCP) library for the Zig ecosystem.

3431. **[meshy-ai-mcp-server](https://github.com/pasie15/meshy-ai-mcp-server)** - ⭐ 30
   This is a Model Context Protocol (MCP) server for interacting with the Meshy AI API. It provides tools for generating 3D models from text and images, applying textures, and remeshing models.

3432. **[MCP-Scorecard](https://github.com/aak204/MCP-Scorecard)** - ⭐ 29
   Deterministic CI scanner and surface-risk scoring for MCP (Model Context Protocol) servers.

3433. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 29
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

3434. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 29
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

3435. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

3436. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

3437. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

3438. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

3439. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

3440. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

3441. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

3442. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

3443. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

3444. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

3445. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

3446. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

3447. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

3448. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 29
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

3449. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 29
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

3450. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 29
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

3451. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 29
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

3452. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 29
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

3453. **[izan.io](https://github.com/ekingunoncu/izan.io)** - ⭐ 29
   Turn Any Browser Action & Data Extraction into an AI Tool in 60 Seconds

3454. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 29
   Testing framework for Model Context Protocol (MCP)

3455. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 29
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

3456. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 29
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

3457. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 29
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

3458. **[drawio-mcp-extension](https://github.com/lgazo/drawio-mcp-extension)** - ⭐ 29
   Draw.io Model Context Protocol (MCP) Browser Extension

3459. **[emcp](https://github.com/PJUllrich/emcp)** - ⭐ 29
   A Model Context Protocol (MCP) Server for Elixir

3460. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 29
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

3461. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 29
   Azure AI Foundry - Agents related sample code

3462. **[autotask-mcp](https://github.com/wyre-technology/autotask-mcp)** - ⭐ 29
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3463. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 29
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

3464. **[Go-High-Level-MCP-2026-Complete](https://github.com/BusyBee3333/Go-High-Level-MCP-2026-Complete)** - ⭐ 29
   GoHighLevel MCP Server — 520+ tools across 40 categories. Voice AI, Proposals, Contacts, Calendars, Conversations, Opportunities, Invoices, Payments, Workflows, Social Media, and more. MCP SDK 1.26, Streamable HTTP, tool annotations.

3465. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

3466. **[claude-mcp-trello](https://github.com/hrs-asano/claude-mcp-trello)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

3467. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 29
   Antrophics Model context protocol to edit powerpoint files

3468. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 29
   An implementation of Giphy integration with Model Context Protocol

3469. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 29
   a web logging proxy for MCP client-server communication

3470. **[engram-memory-community](https://github.com/EngramMemory/engram-memory-community)** - ⭐ 29
   The highest-scoring AI memory system ever benchmarked that isn't reliant on LLM reranking. And it's free & burns less tokens.

3471. **[DecisionNode](https://github.com/decisionnode/DecisionNode)** - ⭐ 29
   CLI + Local MCP - A shared structured memory store across Claude Code, Cursor, Windsurf, Antigravity, and every MCP client. Semantically queryable.

3472. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 29
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

3473. **[opencode-mcp](https://github.com/AlaeddineMessadi/opencode-mcp)** - ⭐ 29
   MCP server for OpenCode AI — 70 tools, 10 resources, 5 prompts. Use npx opencode-mcp with Claude Desktop, Claude Code, Cursor, Windsurf, or any MCP client.

3474. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 29
   An MCP Server and client for communicating with Nifi (v1.28)

3475. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 29
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3476. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 29
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

3477. **[rootcause](https://github.com/yindia/rootcause)** - ⭐ 29
   RootCause is a local-first MCP server that turns natural-language requests into evidence-backed incident analysis, Kubernetes diagnostics, and safer operations.

3478. **[coworker](https://github.com/Array-Ventures/coworker)** - ⭐ 29
   Open-source AI agent with MCP UI, app builder, A2A protocol, skills marketplace, and multi-provider chat. Built with Mastra. Alternative to OpenClaw.

3479. **[Palmos](https://github.com/ClayPulse/Palmos)** - ⭐ 28
   The Runtime Where AI Agents Build, Ship, and Evolve. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

3480. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 28
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

3481. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 28
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

3482. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 28
   A library for declaratively building Model Context Protocol servers.

3483. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 28
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

3484. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

3485. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

3486. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

3487. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

3488. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

3489. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

3490. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 28
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

3491. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 28
   Model Context Protocol to bridge in Substack writings to Claude.

3492. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 28
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

3493. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 28
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

3494. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 28
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

3495. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 28
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

3496. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 28
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

3497. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 28
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

3498. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

3499. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3500. **[chat](https://github.com/repaera/chat)** - ⭐ 28
   Chat Client for Your Service's MCP Server

3501. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 28
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

3502. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 28
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

3503. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 28
   Simple MCP to give Claude ability to check current time as well as know when holidays are, what is the time distance between dates etc.

3504. **[computeruseprotocol](https://github.com/computeruseprotocol/computeruseprotocol)** - ⭐ 28
   Computer Use Protocol is a universal schema for AI agents to perceive and interact with any desktop UI.

3505. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 28
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3506. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 28
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3507. **[Unity-AI-ParticleSystem](https://github.com/IvanMurzak/Unity-AI-ParticleSystem)** - ⭐ 28
   AI-powered tools for Unity Particle System. Create and modify Particle System directly through natural language commands.

3508. **[mcp-anything](https://github.com/Type-MCP/mcp-anything)** - ⭐ 28
   One command to turn any codebase into an MCP server

3509. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 28
   MCP to LangChain Tools Conversion Utility / Python

3510. **[raybridge](https://github.com/jlokos/raybridge)** - ⭐ 28
   MCP server that bridges Raycast extensions to any MCP-compatible client

3511. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 28
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3512. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 28
   The Runtime Where AI Agents Build, Ship, and Evolve. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

3513. **[stata-workbench](https://github.com/tmonk/stata-workbench)** - ⭐ 28
   A VS Code compatible extension (Cursor, Windsurf, Antigravity etc.) that allows Stata code to be run directly from the editor. Enables AI agents to directly interact with Stata. Powered by mcp-stata, https://github.com/tmonk/mcp-stata.

3514. **[overleaf-mcp-server](https://github.com/YounesBensafia/overleaf-mcp-server)** - ⭐ 28
   MCP server for Overleaf projects. Syncs LaTeX files via Git, parses sections, equations, and citations, and exposes them to AI clients for assisted paper review, LaTeX fixes, and content generation.

3515. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 28
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3516. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 27
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

3517. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 27
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

3518. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

3519. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

3520. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

3521. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

3522. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

3523. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

3524. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

3525. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

3526. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 27
   Model Context Protocol Server for NebulaGraph 3.x

3527. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 27
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

3528. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

3529. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 27
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

3530. **[janee](https://github.com/rsdouglas/janee)** - ⭐ 27
   Secrets management for AI agents via MCP • @janeesecure

3531. **[openzeppelin-mcp](https://github.com/OpenZeppelin/openzeppelin-mcp)** - ⭐ 27
   Model Context Protocol Servers Repository for OpenZeppelin products

3532. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 27
   Educational repo for MCP streamable HTTP servers and clients

3533. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 27
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

3534. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

3535. **[novyx-mcp](https://github.com/novyxlabs/novyx-mcp)** - ⭐ 27
   Persistent memory for AI agents. 107 MCP tools for remember, recall, rollback, audit, knowledge graph, eval, cortex, replay, governed actions, threat intel, auto-defense, Runtime v2 agents/missions, and more. Works locally (zero config) or with Novyx Cloud.

3536. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 27
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

3537. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 27
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets. 

3538. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 27
   🧬 Analyze spatial transcriptomics data through natural language conversation. Stop writing code, start having conversations with your data. MCP server for Claude Code and Codex.

3539. **[codex-claude-bridge](https://github.com/abhishekgahlot2/codex-claude-bridge)** - ⭐ 27
   Bidirectional bridge between Claude Code and OpenAI Codex CLI. Built on Claude Code Channels. Two AI agents, one conversation, real-time web UI.

3540. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 27
   Simple MCP SDK in Java

3541. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 27
   An MCP server and client for LLMs to interact with Unity Projects

3542. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 27
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3543. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 27
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

3544. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 27
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

3545. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 27
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3546. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 26
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

3547. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

3548. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

3549. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

3550. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

3551. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

3552. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy 

3553. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for GreptimeDB

3554. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 26
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

3555. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 26
   Model Context Protocol server for Github Repo // Reading Github Repo

3556. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 26
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

3557. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 26
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

3558. **[markview](https://github.com/paulhkang94/markview)** - ⭐ 26
   Native macOS markdown preview + MCP server for Claude Code. Swift/SwiftUI, GFM, Mermaid, syntax highlighting. No Electron.

3559. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 26
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

3560. **[MCPHammer](https://github.com/praetorian-inc/MCPHammer)** - ⭐ 26
   MCP security testing framework for evaluating Model Context Protocol server vulnerabilities

3561. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 26
   Local FAISS vector store as an MCP server – Agent Memory, drop-in local semantic search for Claude / Copilot / Agents.

3562. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 26
   MCP server to expose local zotero repository to MCP clients 

3563. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 26
   A Fastify plugin to run Model Context Protocol (MCP) servers

3564. **[ue5-mcp](https://github.com/mirno-ehf/ue5-mcp)** - ⭐ 26
   Let AI edit your Unreal Engine Blueprints. MCP server plugin for Claude Code — describe what you want in plain English.

3565. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 26
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

3566. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

3567. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 26
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

3568. **[Unreal-MCP](https://github.com/aadeshrao123/Unreal-MCP)** - ⭐ 26
   AI bridge for Unreal Engine 5. Control the editor from Claude Code, Cursor, Windsurf, and any MCP client. 238 commands across materials, blueprints, Niagara VFX, StateTree, data tables, Mass Entity, Enhanced Input, UMG widgets, and performance profiling.

3569. **[plux](https://github.com/milisp/plux)** - ⭐ 26
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

3570. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 26
   Contemplative reasoning MCP server — Lotus Sutra wisdom framework with interactive ext-apps journey visualization.

3571. **[mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp)** - ⭐ 26
   MCP Server that wraps mitmproxy and exposes it as a tool to any MCP client, allows your AI agents to inspect traffic, filter traffic, intercept & modify traffic, request reply, set global headers, and start/stop mitmproxy as needed.

3572. **[webmcp-bridge](https://github.com/holon-run/webmcp-bridge)** - ⭐ 25
   Bridge local MCP clients to browser WebMCP tools through Playwright, using native WebMCP when available and injected adapters when not.

3573. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

3574. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

3575. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

3576. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

3577. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

3578. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

3579. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

3580. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

3581. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

3582. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

3583. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

3584. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 25
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

3585. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 25
   Message Communication Protocol server for json2video API integration

3586. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 25
   Simple MCP Client for remote MCP Servers 🌐

3587. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 25
   An MCP server enabling CFBD API queries within Claude Desktop.

3588. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 25
   MCP server wrapping around the Fabric Rest API

3589. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 25
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

3590. **[gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp)** - ⭐ 25
   MCP server for Google Gemini — free image generation, editing & chat via browser cookies. No API keys needed.

3591. **[Screenhand](https://github.com/manushi4/Screenhand)** - ⭐ 25
   Give AI eyes and hands on your desktop. Open-source MCP server for desktop automation — screenshots, UI control, browser automation, OCR. Works with Claude, Cursor, and any MCP client. macOS + Windows.

3592. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 25
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

3593. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 25
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3594. **[Intercept](https://github.com/PolicyLayer/Intercept)** - ⭐ 25
   The control layer for AI agents. Intercept enforces hard limits on every MCP tool call before execution. Rate limits, spend caps, access controls. Open source.

3595. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 25
   Model Context Protocol server for Rollbar

3596. **[twincat-validator-mcp](https://github.com/agenticcontrolio/twincat-validator-mcp)** - ⭐ 25
   An MCP server that validates, auto-fixes, and scaffolds TwinCAT 3 XML files. Connect it to any LLM client to give your AI assistant reliable, deterministic TwinCAT code quality tooling — structural checks, 21 IEC 61131-3 OOP checks, auto-fix pipelines, and canonical skeleton generation.

3597. **[mcp-server](https://github.com/Decodo/mcp-server)** - ⭐ 25
   The Decodo MCP server which enables MCP clients to interface with services.

3598. **[asc-mcp](https://github.com/zelentsov-dev/asc-mcp)** - ⭐ 25
   MCP server for App Store Connect API — 208 tools for managing apps, builds, TestFlight, subscriptions, and more from Claude, Cursor, VS Code, or any MCP client

3599. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

3600. **[MCP-OpenStack-Ops](https://github.com/call518/MCP-OpenStack-Ops)** - ⭐ 25
   90+ production-safe OpenStack tools for AI agents via MCP. Project-scoped & read-only by default. Works with Claude, Open WebUI & any MCP client. FastMCP + OpenStack SDK. Available on PyPI, Docker Hub & Smithery.

3601. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 24
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

3602. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 24
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

3603. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

3604. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

3605. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

3606. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

3607. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3608. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

3609. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

3610. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

3611. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

3612. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

3613. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

3614. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

3615. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

3616. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

3617. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

3618. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

3619. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

3620. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

3621. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

3622. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

3623. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 24
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

3624. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 24
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

3625. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 24
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3626. **[agentgate](https://github.com/agentkitai/agentgate)** - ⭐ 24
   Approval workflows for AI agents

3627. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 24
   Memory Cache Server for use with supported MCP API Clients.

3628. **[WikidataMCP](https://github.com/philippesaade-wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3629. **[WikidataMCP](https://github.com/wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3630. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 24
   CLI for calling successive MCP Server tools

3631. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/cortexaiofficial/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3632. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/Cortex-AI-Software/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3633. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 24
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

3634. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 24
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

3635. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 24
   Tanzu Platform Chat

3636. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 24
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

3637. **[MCP-DB-Client](https://github.com/DitriXNew/MCP-DB-Client)** - ⭐ 24
   MCP layer for 1C

3638. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 24
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API)

3639. **[mcp-server-zotero-dev](https://github.com/introfini/mcp-server-zotero-dev)** - ⭐ 24
   Give your AI assistant superpowers for Zotero plugin development. 25 tools for screenshots, DOM inspection, JavaScript execution, build integration, and debugging via Model Context Protocol.

3640. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 24
   MCP server and client for running Linux commands

3641. **[atxp](https://github.com/atxp-dev/atxp)** - ⭐ 24
   Give your AI agent a wallet, email, phone number, and instant access to paid MCP tools — web search, image/video/music gen, X search, SMS, voice calls, code execution, and more. Works with Gemini CLI, Claude, and any MCP client.

3642. **[plumcp](https://github.com/plumce/plumcp)** - ⭐ 24
   Clojure/ClojureScript library for making MCP server and client

3643. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

3644. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 23
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

3645. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 23
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

3646. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

3647. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

3648. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

3649. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3650. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

3651. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

3652. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

3653. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

3654. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

3655. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

3656. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

3657. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

3658. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 23
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3659. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 23
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

3660. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 23
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3661. **[agent-studio-starter](https://github.com/nsphung/agent-studio-starter)** - ⭐ 23
   Stop building AI agents from scratch. Bootstrap starter Agent app with LangGraph, CopilotKit, and beautiful Generative UIs.

3662. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 23
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3663. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 23
   MCP to LangChain Tools Conversion Utility / TypeScript

3664. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 23
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3665. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 23
   The Decodo MCP server which enables MCP clients to interface with services.

3666. **[mcp-scan](https://github.com/rodolfboctor/mcp-scan)** - ⭐ 23
   Security scanner for MCP server configurations. Detects secrets, CVEs, permission issues, and exfiltration vectors across 10 AI tool clients.

3667. **[awesome-agent-skills-mcp](https://github.com/shadowrootdev/awesome-agent-skills-mcp)** - ⭐ 23
   MCP server providing 100+ AI agent skills from Anthropic, Vercel, Trail of Bits, Hugging Face & more. Works with Claude, GitHub Copilot, and any MCP client.

3668. **[manceps](https://github.com/zarpay/manceps)** - ⭐ 23
   Ruby client for the Model Context Protocol (MCP). Latin: one who takes in hand.

3669. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 23
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

3670. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 23
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3671. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 23

3672. **[askr](https://github.com/Sweatent/askr)** - ⭐ 23
   MCP Q&A Assistant - Async Q&A capabilities for AI clients via MCP protocol

3673. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 23
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3674. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 23
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

3675. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 23
   MCP server to integrate AWS S3 and LLM

3676. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 22
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

3677. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 22
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

3678. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

3679. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

3680. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

3681. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

3682. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

3683. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

3684. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

3685. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

3686. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

3687. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

3688. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

3689. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

3690. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

3691. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

3692. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 22
   Rust MCP framework for building AI agents

3693. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 22
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

3694. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 22
   A collection of mcp servers/client/sdks

3695. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 22
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

3696. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 22
   MCP agent/client/server implementation for private knowledge base

3697. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 22
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

3698. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 22
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3699. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 22
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3700. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 22
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

3701. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 22
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3702. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 22
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

3703. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 22
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

3704. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 22
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

3705. **[spectrawl](https://github.com/Pyx-Corp/spectrawl)** - ⭐ 22
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

3706. **[mcp-superset](https://github.com/bintocher/mcp-superset)** - ⭐ 22
   MCP server for managing Apache Superset — 128+ tools for dashboards, charts, datasets, SQL Lab, access control

3707. **[Jiva](https://github.com/KarmaloopAI/Jiva)** - ⭐ 22
   Jiva is a CLI-first, open source autonomous AI agent and open alternative to Claude. Built in TypeScript with a three-agent architecture (Manager, Worker, Client), it autonomously plans and executes tasks from your terminal. Supports MCP servers, a built-in Skills system, and Jiva Personas - a plugin framework fully compatible with Claude Plugins.

3708. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 22
   Session-based Slack MCP for Claude and MCP clients: local-first workflows, secure-default HTTP.

3709. **[csv-editor](https://github.com/santoshray02/csv-editor)** - ⭐ 22
   Stateful CSV editing MCP server for AI assistants — sessions, undo/redo, auto-save, and 39 pandas-powered tools. Works    with Claude, ChatGPT, Cursor, Windsurf, Claude Code, and any MCP-compatible client. Built on FastMCP 3

3710. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 22
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3711. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 22
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3712. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation for Gumroad API

3713. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 21
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

3714. **[pixelpanda-mcp](https://github.com/RyanKramer/pixelpanda-mcp)** - ⭐ 21
   MCP server for PixelPanda — 31 AI image processing tools for Claude Desktop, Cursor & other MCP clients

3715. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 21
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

3716. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 21
   Supabase MCP client react app with Tambo

3717. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

3718. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

3719. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

3720. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

3721. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

3722. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

3723. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

3724. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

3725. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

3726. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

3727. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

3728. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

3729. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 21
   Haskell server/client for MCP (Model Context Protocol)

3730. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 21
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

3731. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 21
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

3732. **[heuristic-mcp](https://github.com/softerist/heuristic-mcp)** - ⭐ 21
   Enhanced MCP server for semantic code search with call-graph proximity, recency ranking, and find-similar-code. Built for AI coding assistants.

3733. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 21
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

3734. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

3735. **[codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool)** - ⭐ 21

3736. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 21
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

3737. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 21
   The BioContextAI Registry for biomedical MCP servers

3738. **[archmcp](https://github.com/dejo1307/archmcp)** - ⭐ 21
   archmcp - MCP Architectural Snapshot Server and Knowledge Graph

3739. **[agentidentityprotocol](https://github.com/openagentidentityprotocol/agentidentityprotocol)** - ⭐ 21
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3740. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 21
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

3741. **[codeTree](https://github.com/ThinkyMiner/codeTree)** - ⭐ 21
   MCP server with 23 tools for structured code understanding via tree-sitter. 10 languages. 999 tests. One-command install.

3742. **[turn-mcp](https://github.com/shiahonb777/turn-mcp)** - ⭐ 21
   Achieve infinite conversation turns in a single API request via turn-mcp.             Self-hosted MCP server with browser console for human-in-the-loop AI agents.

3743. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 21
   BioContextAI Knowledgebase MCP server for biomedical agentic AI 

3744. **[mcp-kling](https://github.com/199-mcp/mcp-kling)** - ⭐ 21
   🎬 The FIRST MCP server for Kling AI video generation! Generate stunning AI videos directly from Claude.

3745. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 21
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

3746. **[dsers-mcp-product](https://github.com/lofder/dsers-mcp-product)** - ⭐ 21
   An open-source MCP server to automate DSers product import, bulk edit variants, and push to Shopify/Wix/WooCommerce using AI. Supports AliExpress, Alibaba, 1688.

3747. **[agentic-tools](https://github.com/meta-quest/agentic-tools)** - ⭐ 21
   Agent Tool and Skills for VR Development on Meta Quest 

3748. **[ARBuilder](https://github.com/Quantum3-Labs/ARBuilder)** - ⭐ 21
   AI-powered code generator for Arbitrum Stylus, SDK bridging, dApps & Orbit chains — 19 MCP tools with RAG

3749. **[MicrosoftGraph_Transcript_MCP](https://github.com/ITSpecialist111/MicrosoftGraph_Transcript_MCP)** - ⭐ 21
   A remote Model Context Protocol (MCP) server that retrieves Microsoft Teams meeting transcripts via the Microsoft Graph API, using delegated **OAuth 2.0 On-Behalf-Of (OBO)** authentication.  Designed for integration with Microsoft Copilot Studio (via the MCP Wizard), though any MCP-compatible client can connect.

3750. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 21
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

3751. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 21
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3752. **[swift-mcp](https://github.com/DePasqualeOrg/swift-mcp)** - ⭐ 21
   Full-featured Swift SDK for Model Context Protocol servers and clients

3753. **[muster](https://github.com/giantswarm/muster)** - ⭐ 21
   MCP tool management and workflow proxy

3754. **[bruno-mcp](https://github.com/macarthy/bruno-mcp)** - ⭐ 21
   🚀 MCP server for generating Bruno API testing files programmatically. Create collections, environments, requests, and test scripts using AI clients like Claude Desktop.

3755. **[zebbern-kali-mcp](https://github.com/zebbern/zebbern-kali-mcp)** - ⭐ 21
   MCP server for Kali Linux penetration testing - 130 tools for AI-assisted security testing - Giving Agents access to full pentesting tools

3756. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

3757. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 21
   A fetch API based TypeScript SDK for MCP

3758. **[open-code-review](https://github.com/raye-deng/open-code-review)** - ⭐ 21
   🤖 AI code quality gate for AI-generated code. Detects hallucinated packages, phantom dependencies, stale APIs, and more. MCP Server + CLI + CI/CD Action.

3759. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 21
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

3760. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 20
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

3761. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

3762. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

3763. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

3764. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 20
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

3765. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 20
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3766. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 20
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

3767. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 20
   Connect to any MCP servers using agents

3768. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 20
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

3769. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 20
   HasMCP Community Edition

3770. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 20
   A GitHub CLI extension that seamlessly runs the github-mcp-server using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

3771. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 20
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

3772. **[starbase](https://github.com/metorial/starbase)** - ⭐ 20
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

3773. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 20
   a Nushell cross.stream extension to interact with LLMs and MCP servers

3774. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 20
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

3775. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 20

3776. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 20
   苹果 MCP 工具 ✅

3777. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 20
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

3778. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 20
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3779. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 19
   MCP Server for fething yfinance financial data into Claude Desktop

3780. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 19
   A high performance MCP client sdk for python

3781. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

3782. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

3783. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 19
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

3784. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

3785. **[termlink](https://github.com/chu2bard/termlink)** - ⭐ 19
   MCP server for shell and terminal operations

3786. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

3787. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 19
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

3788. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 19
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

3789. **[bonnard](https://github.com/bonnard-data/bonnard)** - ⭐ 19
   Open-source agentic schema for reliable data outputs. Query data through MCP and via our SDK. Create apps, embed data or just simply explore through your preferred agent.

3790. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 19
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

3791. **[spectrawl](https://github.com/FayAndXan/spectrawl)** - ⭐ 19
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

3792. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 19
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

3793. **[unified-gateway-mcp](https://github.com/mcp360/unified-gateway-mcp)** - ⭐ 19
   Unified MCP Gateway Platform, Marketplace & Custom MCPs

3794. **[subcog](https://github.com/zircote/subcog)** - ⭐ 19
   Persistent memory system for AI coding assistants. Captures decisions, learnings, and context from coding sessions. Features hybrid search (semantic + BM25), MCP server integration, SQLite persistence with knowledge graph, and proactive memory surfacing. Written in Rust.

3795. **[builtwith-api](https://github.com/zcaceres/builtwith-api)** - ⭐ 19
   TypeScript library, MCP, and agent-friendly CLI for the BuiltWith API.

3796. **[better-notion-mcp](https://github.com/n24q02m/better-notion-mcp)** - ⭐ 19
   Markdown-first MCP server for Notion API - composite tools optimized for AI agents

3797. **[mcp-anything](https://github.com/gabrielekarra/mcp-anything)** - ⭐ 19
   One command to turn any codebase into an MCP server

3798. **[nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp)** - ⭐ 19
   Gemini Vision & Image Generation MCP for Claude Desktop and Claude Code

3799. **[awesome-mcp-security](https://github.com/AgentSeal/awesome-mcp-security)** - ⭐ 19
   Security scores for 800+ MCP servers. 9 analyzers scan for prompt injection, toxic flows, and attack surface risks. Updated daily. 🛡️

3800. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 19
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

3801. **[resonant](https://github.com/codependentai/resonant)** - ⭐ 19
   Open-source relational AI framework with identity persistence, memory, and MCP integration. Build relationship-aware AI agents that remember, grow, and maintain continuity. Built on Claude Agent SDK.

3802. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 19
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

3803. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 19
   MCP server to manage Spotify from MCP clients

3804. **[strategy-mcp](https://github.com/sohaibt/strategy-mcp)** - ⭐ 19
   strategy-mcp is an open source MCP server that exposes professional-grade product strategy frameworks as structured tools. Any MCP-compatible AI assistant (Claude, Cursor, Cline) can install it and immediately get access to structured strategy analysis, RICE, JTBD, competitive positioning, assumption mapping, and more.

3805. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 19
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

3806. **[brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server)** - ⭐ 19
   MCP server for Brightspace (D2L). Check grades, due dates, assignments, announcements, rosters, syllabus & course content via Claude, ChatGPT, Cursor, Windsurf, or any MCP client. Works with any school. npm: npx brightspace-mcp-server@latest

3807. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database. 

3808. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 19
   MCP server for graph representation of a codebase

3809. **[bambu-printer-mcp](https://github.com/DMontgomery40/bambu-printer-mcp)** - ⭐ 19
   MCP server for Bambu Lab 3D printers — STL manipulation, BambuStudio slicing, and direct printer control

3810. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 19
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

3811. **[ProxmoxMCP-advance](https://github.com/Markermav/ProxmoxMCP-advance)** - ⭐ 19
   ProxmoxMCP (advance): MCP for Proxmox integration in Claude, Goose, Cline, any client.

3812. **[localwp-agent-tools](https://github.com/10up/localwp-agent-tools)** - ⭐ 19
   A Local add-on that provides an MCP server, skills, and project context for AI-powered WordPress development. Works with Claude Code, Cursor, Windsurf, VS Code Copilot, and any MCP client.

3813. **[llmqore](https://github.com/Palm1r/llmqore)** - ⭐ 19
   Qt C++ library for working with AI/LLM Providers and MCP

3814. **[daiv](https://github.com/srtab/daiv)** - ⭐ 18
   Your AI-powered SWE teammate, built into your git workflow

3815. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

3816. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

3817. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

3818. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

3819. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

3820. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

3821. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

3822. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 18
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

3823. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 18
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

3824. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 18
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

3825. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 18
   A command-line utility for interacting with MCP servers.

3826. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 18
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

3827. **[toolhive-catalog](https://github.com/stacklok/toolhive-catalog)** - ⭐ 18
   ToolHive's registry catalog of MCP servers

3828. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 18
   The immune system for AI coding agents

3829. **[robotmem](https://github.com/robotmem/robotmem)** - ⭐ 18
   Robot Memory - Persistent memory system for AI robots. MCP Server + hybrid search + spatial retrieval.

3830. **[speclock](https://github.com/sgroy10/speclock)** - ⭐ 18
   AI Constraint Engine by Sandeep Roy — stops AI from breaking what you locked. 100/100 on Claude's adversarial test suite. 42 MCP tools. Works with Bolt.new, Lovable, Claude Code, Cursor. Free & open source.

3831. **[agentify](https://github.com/koriyoshi2041/agentify)** - ⭐ 18
   Agent Interface Compiler — One command. Every agent speaks your product. Transform OpenAPI specs into MCP Servers, Skills, CLAUDE.md, AGENTS.md, and more.

3832. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 18
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

3833. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 18
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

3834. **[scopus-mcp](https://github.com/qwe4559999/scopus-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server for Elsevier Scopus. Allows AI assistants like Claude to search academic papers, retrieve abstracts, and analyze author profiles directly.

3835. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 18
   simple mcp server for interacting with local obsidian notes

3836. **[ContextOS](https://github.com/itallstartedwithaidea/ContextOS)** - ⭐ 18
   Unified MCP context intelligence platform — pip-installable CLI that absorbed 6 foundational repos. Context engineering for AI agents.

3837. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 18
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

3838. **[openrouter-mcp-multimodal](https://github.com/stabgan/openrouter-mcp-multimodal)** - ⭐ 18
   MCP server for OpenRouter providing text chat and image analysis tools

3839. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 18

3840. **[XcodeMCPWrapper](https://github.com/SoundBlaster/XcodeMCPWrapper)** - ⭐ 18
   MCP that makes Xcode 26.3's MCP compatible with Cursor and other strict MCP-spec-compliant clients

3841. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 18
   An MCP client that uses signal for sending and receiving messages.

3842. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 18
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

3843. **[ida-codex-mcp](https://github.com/Iamgublin/ida-codex-mcp)** - ⭐ 18
   IDA Codex MCP bridges IDA Pro 9.2 with the MCP ecosystem. It provides an IDA plugin and a stdio MCP server that expose   function lists, call graphs, Hex‑Rays pseudocode, disassembly, imports/exports, xrefs, strings, and memory reads to   MCP clients.

3844. **[mendeley-mcp](https://github.com/pallaprolus/mendeley-mcp)** - ⭐ 18
   MCP server for Mendeley reference manager - search, retrieve, and manage your academic library from Claude and other MCP clients

3845. **[webclaw](https://github.com/kuroko1t/webclaw)** - ⭐ 18
   A WebMCP-native browser agent that runs inside your real Chrome — control it from Claude, Cursor, and any MCP client

3846. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 18
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

3847. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 17
   Model Context Protocol (MCP)

3848. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 17
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

3849. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 17
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

3850. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

3851. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

3852. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

3853. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

3854. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

3855. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

3856. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

3857. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

3858. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

3859. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 17
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

3860. **[mcpforge](https://github.com/lorenzosaraiva/mcpforge)** - ⭐ 17

3861. **[mcp-ecosystem](https://github.com/SynkraAI/mcp-ecosystem)** - ⭐ 17
   MCP Ecosystem: Docker MCP Toolkit, IDE Configs & Presets for AIOS

3862. **[lightdash_mcp](https://github.com/poddubnyoleg/lightdash_mcp)** - ⭐ 17
   mcp server for lightdash

3863. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 17
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

3864. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 17
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

3865. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 17
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

3866. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 17
   A model-agnostic MCP Client-Server for .Net and Unity

3867. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 17
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

3868. **[FocusRelayMCP](https://github.com/deverman/FocusRelayMCP)** - ⭐ 17
   Talk to your OmniFocus tasks. An OmniFocus MCP server that lets AI assistants query your tasks, projects, and tags using natural language—no more clicking through endless lists.

3869. **[extract-llms-docs](https://github.com/nirholas/extract-llms-docs)** - ⭐ 17
   Extract documentation for AI agents from any site with llms.txt support. Features MCP server, REST API, batch processing, and multiple export formats.

3870. **[video-research-mcp](https://github.com/Galbaz1/video-research-mcp)** - ⭐ 17
   Give Claude Code 41 research & video tools with one command. Video analysis, deep research, content extraction, explainer video creation, and Weaviate vector search — powered by Gemini 3.1 Pro.

3871. **[opencode-browser](https://github.com/michaljach/opencode-browser)** - ⭐ 17
   Browser automation plugin for OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via MCP integration

3872. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 17
   MCP server and client for Frontapp

3873. **[nasa](https://github.com/peteretelej/nasa)** - ⭐ 17
   Go client library for NASA APIs: APOD, NeoWs, DONKI, NASA Image Library, SSD/CNEOS, EONET. Supports built-in rate-limiting, a CLI & MCP Server

3874. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 17

3875. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 17
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

3876. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 17
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

3877. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 17
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

3878. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 17
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

3879. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 17
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

3880. **[slm-mesh](https://github.com/qualixar/slm-mesh)** - ⭐ 17
   Peer-to-peer communication for AI coding agents. 8 MCP tools, full CLI, Python client. Part of the Qualixar research initiative by Varun Pratap Bhardwaj.

3881. **[obsidian-http-mcp](https://github.com/NasAndNora/obsidian-http-mcp)** - ⭐ 17
   First HTTP-native MCP server for Obsidian - Compatible with any MCP client (Claude Code, Codex, Gemini, etc.) without stdio bugs

3882. **[mcp-client-cli](https://github.com/addity3/mcp-client-cli)** - ⭐ 16
   cli-based program to run llm prompt and mcp

3883. **[claude-vigil-mcp](https://github.com/Vvkmnn/claude-vigil-mcp)** - ⭐ 16
   🏺 An MCP server for checkpointing and file recovery in Claude Code

3884. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

3885. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

3886. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

3887. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

3888. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

3889. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

3890. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

3891. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3892. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

3893. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

3894. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 16
   Language to Maps

3895. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 16
   MCP server for xAI Grok — read and serve .faf project context. npm: grok-faf-mcp

3896. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 16
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

3897. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 16
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

3898. **[penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** - ⭐ 16
   MCP server for Penpot - Connect AI assistants to Penpot design platform via Model Context Protocol

3899. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 16
   MCP server for penetration testing

3900. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 16
   An MCP server to read MCP logs to debug directly inside the client

3901. **[drf-mcp-docs](https://github.com/Abdulkhalek-1/drf-mcp-docs)** - ⭐ 16
   API documentation via MCP for AI coding agents

3902. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 16
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

3903. **[LSP4J-MCP](https://github.com/stephanj/LSP4J-MCP)** - ⭐ 16
   A Java MCP (Model Context Protocol) server that wraps JDTLS (Eclipse JDT Language Server) using LSP4J to provide Java IDE features to AI assistants like Claude.

3904. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 16
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

3905. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 16
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

3906. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 16
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

3907. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 16
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

3908. **[shodan-mcp](https://github.com/Vorota-ai/shodan-mcp)** - ⭐ 16
   Shodan MCP server for Claude, Cursor & VS Code. 20 tools for passive reconnaissance, CVE/CPE intelligence, DNS analysis, and device search. 4 tools work free without an API key. OSINT and vulnerability research from your IDE.

3909. **[webmcp-react](https://github.com/MCPCat/webmcp-react)** - ⭐ 16
   React hooks for exposing your app's functionality as WebMCP tools - transport-agnostic, SSR-safe, Strict Mode safe, W3C spec-aligned

3910. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 16
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

3911. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 16
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

3912. **[openapi-to-mcp](https://github.com/EvilFreelancer/openapi-to-mcp)** - ⭐ 16
   Turns any OpenAPI/Swagger API into an MCP server. One MCP tool per endpoint, Streamable HTTP - for AI clients calling your REST API.

3913. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 16
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

3914. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 16
   A web-based client for connecting to MCP servers with OAuth support

3915. **[mcp-dashboards](https://github.com/KyuRish/mcp-dashboards)** - ⭐ 16
   Turn your data into interactive dashboards inside any AI client - MCP Apps powered

3916. **[reporelay](https://github.com/chwoerz/reporelay)** - ⭐ 16
   A self-hosted code context engine for MCP.

3917. **[vibeshell](https://github.com/veithly/vibeshell)** - ⭐ 16
   The first SSH client built for AI agents. Let Claude Code, Codex, and other CLI agents manage your servers through MCP skills. Beautiful UI, native performance.

3918. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 16
   Unity Catalog AI Model Context Protocol Server

3919. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 16
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

3920. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 16
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3921. **[conductor](https://github.com/aryabyte21/conductor)** - ⭐ 16
   Manage MCP server configs across AI coding clients

3922. **[atm](https://github.com/sfox38/atm)** - ⭐ 16
   Create secure and scoped Home Assistant API tokens for AI assistants and other MCP clients

3923. **[kiro-professional-toolkit](https://github.com/gkhantyln/kiro-professional-toolkit)** - ⭐ 16
   ⚡ The most complete Kiro IDE toolkit — 34 AI Agents, 32 Expert Hooks, 50 Skills, 22 Steering Rules & 44 MCP Integrations. From React to Rust, Spring to GraphQL — production-grade workflows, one install.

3924. **[nexo](https://github.com/wazionapps/nexo)** - ⭐ 16
   NEXO Brain — Shared brain for AI agents. Persistent memory, semantic RAG, natural forgetting, metacognitive guard, trust scoring, 150+ MCP tools. Works with Claude Code, Codex, Claude Desktop & any MCP client. 100% local, open source, free.

3925. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 15
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

3926. **[faf](https://github.com/Wolfe-Jam/faf)** - ⭐ 15
   FAF specification — IANA-registered AI context format (application/vnd.faf+yaml)

3927. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

3928. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

3929. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

3930. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data 

3931. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

3932. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

3933. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 15
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

3934. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 15
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

3935. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 15
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

3936. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 15
   A Socratic dialogue engine for AI agents. 

3937. **[mcp](https://github.com/local-falcon/mcp)** - ⭐ 15
   MCP server for Local Falcon's local SEO and AI visibility platform: geo-grid rank tracking, campaign management, and competitor analysis via Model Context Protocol

3938. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 15
   MCP server for Open Targets Data

3939. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 15
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

3940. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 15
   Markdown To PDF Conversion MCP

3941. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 15
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

3942. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 15
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

3943. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 15
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics 

3944. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 15
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

3945. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 15
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

3946. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 15
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

3947. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 15
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

3948. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 15
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

3949. **[agent-board](https://github.com/quentintou/agent-board)** - ⭐ 15
   Open-source multi-agent task board for OpenClaw. Kanban + DAG dependencies + MCP server + auto-retry + audit trail. Built for autonomous AI agent teams.

3950. **[cuba-memorys](https://github.com/LeandroPG19/cuba-memorys)** - ⭐ 15
   🧠 Persistent memory MCP for AI agents — Knowledge graph + Hebbian learning + Anti-hallucination. 12 tools, 1 dependency, zero manual setup.

3951. **[opentrace](https://github.com/adham90/opentrace)** - ⭐ 15
   Self-hosted observability server with 75+ MCP tools. Ingest logs, connect Postgres, monitor servers — then debug it all from Claude, Cursor, or any MCP client.

3952. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 15
   MCP Client for Gemma-3

3953. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 15
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

3954. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 15
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

3955. **[seats.aero-mcp-server](https://github.com/gavgrego/seats.aero-mcp-server)** - ⭐ 15
   MCP server allowing clients to interface with the seats.aero API

3956. **[memoryOSS](https://github.com/memoryOSScom/memoryOSS)** - ⭐ 15
   Persistent long-term memory for AI agents. Local proxy + MCP memory layer for Claude, Codex, and OpenAI-compatible clients.

3957. **[webmcp-sh](https://github.com/WebMCP-org/webmcp-sh)** - ⭐ 15
   A modern web-based Model Context Protocol (MCP) playground for testing and developing MCP servers and clients

3958. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 15
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

3959. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 15
   Universal cli to add an MCP server to a variety of clients

3960. **[originlab-mcp](https://github.com/garethbeaumo/originlab-mcp)** - ⭐ 15
    MCP Server for OriginLab  Control OriginLab with natural language through AI clients via the Model Context Protocol.

3961. **[Ai-doctor](https://github.com/Jevon-Zhong/Ai-doctor)** - ⭐ 15
   🧑‍⚕️ Ai智能医生聊天助手-这是一个前端基于Vue3、TS、后端基于Nest.js、MongoDB、Redis、Milvus并结合大模型、RAG等技术实现的医疗库智能问答系统，能结合大模型的生成能力和上传的专业医疗领域知识库针对提问给出专业回答。同时具备工具调用能力，可使用MCP集成网页爬取能力让大模型根据网址对应的医疗领域文章进行分析和输出。

3962. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 15
   Official ConfigCat Model Context Protocol (MCP) Server 

3963. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 15
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

3964. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

3965. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

3966. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

3967. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

3968. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

3969. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server 

3970. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

3971. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

3972. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 14
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

3973. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 14
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

3974. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 14
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

3975. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

3976. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 14
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

3977. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 14
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

3978. **[webfetch-mcp](https://github.com/manooll/webfetch-mcp)** - ⭐ 14
   Live Web Access for Your Local AI — Tunable Search & Clean Content Extraction

3979. **[domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp)** - ⭐ 14
   Zero-config domain availability MCP for Claude & ChatGPT. AI suggestions, premium/auction detection via GoDaddy, RDAP/WHOIS fallback. Stdio + HTTP.

3980. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 14
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

3981. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 14
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

3982. **[phabricator-mcp](https://github.com/freelancer/phabricator-mcp)** - ⭐ 14
   MCP server for Phabricator

3983. **[openalex-research-mcp](https://github.com/oksure/openalex-research-mcp)** - ⭐ 14
   MCP server for the OpenAlex API — search 240M+ scholarly works, analyze citations, track research trends, and map collaboration networks

3984. **[claude-praetorian-mcp](https://github.com/Vvkmnn/claude-praetorian-mcp)** - ⭐ 14
   ⚜️ An MCP server for context compaction and recycling in Claude Code

3985. **[servicenow-mcp](https://github.com/aartiq/servicenow-mcp)** - ⭐ 14
   Production-ready Model Context Protocol server for ServiceNow platform integration - ITOM, ITSM, CMDB with OAuth, natural language queries, and enterprise security controls

3986. **[swift-skeleton](https://github.com/1amageek/swift-skeleton)** - ⭐ 14
   Swift source code structural indexer. Extracts type declarations, properties, method signatures, and source locations. MCP server for Claude Code.

3987. **[arxiv-mcp-server](https://github.com/1Dark134/arxiv-mcp-server)** - ⭐ 14
   arXiv MCP Server Client 🐙 enables AI assistants to search, retrieve, analyze, and summarize arXiv papers with features like author/category browsing, trends, and citation insights.

3988. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 14
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3989. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 14
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

3990. **[WAIaaS](https://github.com/minhoyoo-iotrust/WAIaaS)** - ⭐ 14
   Wallet-as-a-Service for all AI agents in the world

3991. **[x402-deploy](https://github.com/nirholas/x402-deploy)** - ⭐ 14
   Turn any API or MCP server into a paid service with x402 

3992. **[ai-mate](https://github.com/symfony/ai-mate)** - ⭐ 14
   AI development assistant MCP server for Symfony projects

3993. **[mcp-security-checklist](https://github.com/Helixar-AI/mcp-security-checklist)** - ⭐ 14
   MCP is being adopted rapidly. Security guidance is lagging behind. This checklist gives security engineers, platform teams, and technical leaders a clear, actionable baseline for securing MCP deployments , whether you're shipping an internal tool or a customer-facing AI agent.

3994. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 14
   The ultimate AI-powered generator for llms.txt and llms-full.txt files. 

3995. **[mcp-graph-workflow](https://github.com/DiegoNogueiraDev/mcp-graph-workflow)** - ⭐ 14
   MCP local-first CLI tool that converts PRD text files into persistent execution graphs (SQLite) for structured agentic workflows

3996. **[MCPScan](https://github.com/sahiloj/MCPScan)** - ⭐ 14
   Offensive MCP server auditor — detects tool poisoning, credential leaks, RCE vectors, SSRF, session hijacking, and supply chain vulnerabilities across stdio, HTTP, and SSE transports.

3997. **[toolhive-registry-server](https://github.com/stacklok/toolhive-registry-server)** - ⭐ 14
   An API server that implements the official MCP Registry API, providing standardised access to MCP servers from multiple backends, including file-based and other API-compliant registries.

3998. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 14
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

3999. **[KunAvatar](https://github.com/KunLabAI/KunAvatar)** - ⭐ 14
   基于ollama推理框架本地部署的Agent应用，实现MCP工具调用，短长期记忆等功能。||  A locally deployed agent application built on the Ollama, featuring MCP tool integration along with both short-term and long-term memory support.

4000. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 14
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

4001. **[Rube](https://github.com/dorucioclea/Rube)** - ⭐ 14
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

4002. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 14
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

4003. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

4004. **[java-xiaohongshu-mcp](https://github.com/bzlrj/java-xiaohongshu-mcp)** - ⭐ 14
   Java 实现的小红书 Model Context Protocol (MCP) 工具服务  为 AI Agent / MCP Client 提供标准化接口，实现： 登录、发图文、发视频、搜索、评论、推荐内容、用户主页 等核心功能

4005. **[SRE-agent](https://github.com/martinimarcello00/SRE-agent)** - ⭐ 14
   Autonomous agent for Kubernetes incident detection, diagnosis, and mitigation using LLMs and modular workflows. Integrates LangChain, LangGraph, and MCP servers to enable automated SRE tasks in cloud-native environments.

4006. **[istat_mcp_server](https://github.com/ondata/istat_mcp_server)** - ⭐ 14
   MCP server to query Italian statistics (ISTAT) via SDMX API — compatible with any MCP client

4007. **[ex_mcp](https://github.com/azmaveth/ex_mcp)** - ⭐ 14
   Model Context Protocol (MCP) and Agent Client Protocol (ACP) client/server library for Elixir

4008. **[salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib)** - ⭐ 14
   Salesforce MCP Library is a local stdio bridge for Salesforce MCP endpoints using OAuth client credentials, featuring a reusable Apex MCP library and JSON-RPC 2.0 core.

4009. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

4010. **[obsidian-cli-rest](https://github.com/dsebastien/obsidian-cli-rest)** - ⭐ 14
   Control your Obsidian vault programmatically. This plugin turns all Obsidian CLI commands into a local HTTP API and MCP server, letting you automate your workflow from scripts, tools, and AI assistants.

4011. **[mcp-toggl](https://github.com/verygoodplugins/mcp-toggl)** - ⭐ 14
   MCP server for Toggl Track integration with intelligent caching and reporting tools

4012. **[mcpskills-cli](https://github.com/dhanababum/mcpskills-cli)** - ⭐ 13
   Generate Agent Skills from MCP server tools. Connects via Streamable HTTP, discovers tools, and outputs a skill with schema docs and a call script in the language of your choice.

4013. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 13

4014. **[nest-mcp](https://github.com/btwld/nest-mcp)** - ⭐ 13
   Build Model Context Protocol (MCP) servers, clients, and gateways using the NestJS ecosystem you already know.

4015. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

4016. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

4017. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

4018. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

4019. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

4020. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

4021. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

4022. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

4023. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

4024. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

4025. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

4026. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

4027. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

4028. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

4029. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

4030. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

4031. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 13
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

4032. **[devtap](https://github.com/killme2008/devtap)** - ⭐ 13
   Bridge build/dev process output to AI coding sessions via MCP — supports Claude Code, Codex, OpenCode, Gemini CLI, and aider

4033. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 13
   A server implementation for the Model Context Protocol (MCP) in Ruby.

4034. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 13
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

4035. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 13
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

4036. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 13
   Taiga UI MCP server providing documentation search and scaffolding tools.

4037. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 13
   MCP server for OWL applications

4038. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 13
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

4039. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 13
   Simple Weather MCP Server Example

4040. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 13
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

4041. **[istek](https://github.com/istekapp/istek)** - ⭐ 13
   The API client built for AI agents. HTTP, GraphQL, gRPC, WebSocket, MQTT + MCP."

4042. **[mcp-server-template](https://github.com/BearHuddleston/mcp-server-template)** - ⭐ 13
   Spec-driven Go MCP server template for building domain MCPs with AI-agent onboarding.

4043. **[obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** - ⭐ 13
   MCP server for Obsidian vault management - enables Claude and other AI assistants to read, write, search, and organize your notes

4044. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 13
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

4045. **[claude-tools-mcp](https://github.com/mathematic-inc/claude-tools-mcp)** - ⭐ 13
   MCP server that exposes Claude Code's file and shell tools (bash, read, write, edit, glob, grep) over HTTP for remote use by any MCP client

4046. **[sift-gateway](https://github.com/lourencomaciel/sift-gateway)** - ⭐ 13
   Reliability gateway for AI tool output: schema-stable, secret-safe, pagination-complete JSON for MCP and CLI agents.

4047. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 13
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

4048. **[lm](https://github.com/houtini-ai/lm)** - ⭐ 13
   Offload Tasks from Claude to your Local LLM With Houtini-LM - uses OpenAPI for LM Studio and Ollama Compatibility. Save tokens by offloading some grunt work for your API - our tool description helps claude decide what work to assign and why.

4049. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 13
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

4050. **[cie](https://github.com/kraklabs/cie)** - ⭐ 13
   Code Intelligence Engine — indexes your codebase and gives AI assistants deep understanding via MCP (semantic search, call graphs, 20+ tools)

4051. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 13
   Anthropic MCP server for .faf — 33 tools, IANA-registered format. npm: claude-faf-mcp. MCP Registry #2759

4052. **[credit-optimizer-v5](https://github.com/rafsilva85/credit-optimizer-v5)** - ⭐ 13
   Credit Optimizer v5 for Manus AI - Save 30-75% on credits. Free MCP Server (PyPI) + $9 Manus Skill. Audited across 53 scenarios. Zero quality loss.

4053. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 13
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

4054. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

4055. **[GitLab-CICD-Agent](https://github.com/shalwin04/GitLab-CICD-Agent)** - ⭐ 13
   agentic-cicd is an AI-powered multi-agent system that automates GitLab CI/CD workflows using natural language. Built with LangGraphJS, it connects to GitLab via OAuth, interprets user intent, generates pipelines, and executes deployments — all orchestrated by autonomous AI agents and backed by a GitLab MCP server.

4056. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 13
   Documentation

4057. **[agent-hub](https://github.com/nathangtg/agent-hub)** - ⭐ 13
   Agent Hub is an AI orchestration platform that transforms how developers and DevOps engineers interact with their toolchain. Built on the cutting-edge Model Context Protocol (MCP), it provides intelligent automation through specialized AI agents, seamlessly integrating with GitHub, Azure, security tools, and data processing

4058. **[Cortex](https://github.com/cdeust/Cortex)** - ⭐ 13
   C.O.R.T.E.X. — Cognitive profiling system for Claude Code

4059. **[docdex](https://github.com/bekirdag/docdex)** - ⭐ 13
   A document index with MCP, http and client support. https://docdex.org/ 

4060. **[claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp)** - ⭐ 13
   Local-first TypeScript MCP server for Qdrant with client isolation, LM Studio integration, and scalable document workflows.

4061. **[magento-coding-standard-mcp](https://github.com/Midhun-edv/magento-coding-standard-mcp)** - ⭐ 13
   MCP server that teaches AI assistants Magento 2 coding standards — validate code, look up correct patterns, check security, and apply theme-specific rules (Hyva, Luma, Breeze, Porto). Works with Claude, Cursor, Gemini CLI, VS Code Copilot, and any MCP-compatible client.

4062. **[XcodeMCPKit](https://github.com/lynnswap/XcodeMCPKit)** - ⭐ 13
   Xcode MCP proxy with multi-client sessions

4063. **[pentest-mcp-server](https://github.com/exjskdjsdfks/pentest-mcp-server)** - ⭐ 13
   ⚙️ Enable AI agents to conduct autonomous penetration testing on any Linux distribution with a persistent and robust Model Context Protocol server.

4064. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 13
   DataAnalysis Agent using LangGraph & MCP server and client

4065. **[mcpmate](https://github.com/loocor/mcpmate)** - ⭐ 13
   MCPMate is a comprehensive Model Context Protocol (MCP) management center designed to address configuration complexity, resource consumption, security risks, and other issues in the MCP ecosystem, providing users with a unified management platform.

4066. **[locus](https://github.com/Magnifico4625/locus)** - ⭐ 13
   Persistent project-aware memory for AI coding tools. Built on MCP. Works with Codex, Claude Code, and other MCP-compatible clients.

4067. **[ai-memory-mcp](https://github.com/alphaonedev/ai-memory-mcp)** - ⭐ 13
   Persistent memory for any AI — MCP server, HTTP API, CLI. Works with Claude, ChatGPT, Grok, Gemini, Codex, Cursor, OpenClaw, and any MCP client. 97.8% R@5 on LongMemEval. Pure SQLite FTS5, zero cloud dependencies.

4068. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 13
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

4069. **[bookmark-manager-mcp](https://github.com/infinitepi-io/bookmark-manager-mcp)** - ⭐ 13
   A lightweight Model Context Protocol (MCP) server that provides persistent bookmark management for Claude and other MCP-compatible clients. Features categorized storage, resource discovery, and seamless integration with your AI workflow.

4070. **[vault-sync](https://github.com/alexjbarnes/vault-sync)** - ⭐ 13
   Headless Obsidian Sync client with MCP server for AI assistants

4071. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 12
   talk to sarvam APIs directly, without code.

4072. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

4073. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

4074. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

4075. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

4076. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

4077. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

4078. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

4079. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

4080. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

4081. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

4082. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

4083. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

4084. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 12
   🥾 _b00t_:  state of the art agentic harness tooling & dynamic context initialization

4085. **[jenkins-mcp-server](https://github.com/AshwiniGhuge3012/jenkins-mcp-server)** - ⭐ 12
   An MCP server for interacting with a Jenkins server. Allows you to trigger jobs, check build statuses, and manage your Jenkins instance through MCP.

4086. **[openagentidentityprotocol](https://github.com/openagentidentityprotocol/openagentidentityprotocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

4087. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 12
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

4088. **[MCPGateway](https://github.com/abdullah1854/MCPGateway)** - ⭐ 12
   Open-source MCP server — progressive tool discovery, code execution, intelligent routing & token optimization across 50+ tools

4089. **[mcp-interactive-terminal](https://github.com/amol21p/mcp-interactive-terminal)** - ⭐ 12
   MCP server that gives AI agents (Claude Code, Cursor, Windsurf) real interactive terminal sessions — REPLs, SSH, databases, Docker, and any interactive CLI with clean output and smart completion detection

4090. **[kiro-powers](https://github.com/praveenc/kiro-powers)** - ⭐ 12
   Repository of custom kiro powers. https://kiro.dev/docs/powers/

4091. **[guildbridge](https://github.com/dend/guildbridge)** - ⭐ 12
   🏰 Remotely hosted MCP server for Discord

4092. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 12
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

4093. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 12
   MCP server for accessing VS Code/Cursor's Local History

4094. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 12
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

4095. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 12
   Connecting AI agent to biomedical data

4096. **[nodebench-ai](https://github.com/HomenShum/nodebench-ai)** - ⭐ 12
   NodeBench MCP - 260-tool Model Context Protocol server with progressive discovery, agent-as-a-graph embeddings, research optimization, and adaptive web scraping. Monorepo: MCP server + Convex backend + React frontend.

4097. **[mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** - ⭐ 12
   WooCommerce MCP Server — WordPress community plugin implementing the Model Context Protocol (MCP) for WooCommerce. Supports STDIO and HTTP streamable transport, with optional JWT authentication. Based on Automattic’s official WordPress MCP.  This plugin is not affiliated with Automattic.

4098. **[asap-protocol](https://github.com/adriannoes/asap-protocol)** - ⭐ 12
   Standard protocol for agent-to-agent communication with stateful orchestration, MCP-compatible and a public marketplace to discover and register agents.

4099. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 12
   MCP for Scorable Evaluation Platform

4100. **[Hoofy](https://github.com/HendryAvila/Hoofy)** - ⭐ 12
   Hoofy — AI development companion MCP server. Persistent memory, spec-driven development, adaptive change pipeline, Clarity Gate. 32 tools, single Go binary, zero deps.

4101. **[wamcp](https://github.com/delltrak/wamcp)** - ⭐ 12
   WhatsApp MCP Server — Connect AI agents to WhatsApp via Model Context Protocol. 61 tools, 10 resources, 12 real-time events. Supports Baileys (WhatsApp Web) and Cloud API. Built with TypeScript, BullMQ, and Docker.

4102. **[actual-mcp-server](https://github.com/agigante80/actual-mcp-server)** - ⭐ 12
   Docker MCP server connecting MCP clients (tested with LibreChat/LobeChat) to Actual Budget for natural-language budgeting, transaction management, and financial insights.

4103. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 12
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

4104. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

4105. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 12
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

4106. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 12
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

4107. **[mcpup](https://github.com/mohammedsamin/mcpup)** - ⭐ 12
   MCP configuration manager — enable, disable, and sync MCP servers across AI clients from one place

4108. **[Opencollab-mcp](https://github.com/prakhar1605/Opencollab-mcp)** - ⭐ 12
   AI-powered open source contribution matchmaker — finds perfect "good first issues" matched to YOUR skills

4109. **[openclaw-mcp-server](https://github.com/Helms-AI/openclaw-mcp-server)** - ⭐ 12
   MCP server exposing OpenClaw Gateway tools to Claude Code and other MCP-compatible clients

4110. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 12
   A TUI to probe the calls between MCP client and server

4111. **[openclaw-mcp-bridge](https://github.com/AIWerk/openclaw-mcp-bridge)** - ⭐ 12
   OpenClaw MCP Client Plugin - bridges MCP servers into OpenClaw via registerTool

4112. **[ux-mcp-server](https://github.com/elsahafy/ux-mcp-server)** - ⭐ 12
   MCP server providing 28 UX knowledge resources, 23 analysis tools & 4 workflow prompts. Works with Claude, Cursor, Continue.dev, Cline, Zed & any MCP client. WCAG, Nielsen heuristics, design systems, e-commerce, PWA, AI/ML & more.

4113. **[DevoChat](https://github.com/gws8820/DevoChat)** - ⭐ 12
   Unified Web AI Chat UI & MCP Client

4114. **[league-client-mcp](https://github.com/rumi-chan/league-client-mcp)** - ⭐ 12
   Connect Claude, Antigravity to League Client via MCP & Pengu Loader.

4115. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 12

4116. **[bexio-mcp-server](https://github.com/PromptPartner/bexio-mcp-server)** - ⭐ 12
   Complete Swiss accounting integration for Bexio via MCP. Works with Claude Desktop, n8n, and any MCP client. 310 tools for invoices, contacts, projects & more. Created by Lukas Hertig.

4117. **[godot-dotnet-mcp](https://github.com/LuoxuanLove/godot-dotnet-mcp)** - ⭐ 12
   A Godot 4.6+ editor plugin that gives AI agents a real MCP interface to the live Godot editor: project state, scene editing, script analysis, runtime control, screenshots, logs, and client setup from inside the editor itself.

4118. **[ai-cli-mcp](https://github.com/mkXultra/ai-cli-mcp)** - ⭐ 12
   MCP server to run Claude, Codex, and Gemini CLI agents in the background from any MCP client.

4119. **[robotmcp_client](https://github.com/robotmcp/robotmcp_client)** - ⭐ 12
   Connect AI models like Claude & GPT with robots using MCP and ROS.

4120. **[mcp-unifi-applications](https://github.com/KallistoX/mcp-unifi-applications)** - ⭐ 12
   An MCP server that exposes UniFi application API documentation (Network, Protect, Site Manager) as queryable tools for Claude Desktop, Claude Code (VS Code / JetBrains), or any MCP-compatible client.

4121. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 11
   An opinionated MCP module for NestJS

4122. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 11
   MCP server for kintone

4123. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 11
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

4124. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 11
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

4125. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

4126. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

4127. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

4128. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

4129. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

4130. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

4131. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

4132. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

4133. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

4134. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

4135. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

4136. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

4137. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

4138. **[polaris](https://github.com/octu0/polaris)** - ⭐ 11
   Distributed AI Agent Framework

4139. **[glm5-mcp](https://github.com/Arkya-AI/glm5-mcp)** - ⭐ 11
   Reduce Claude Desktop consumption by 10x - Integrate Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

4140. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 11
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

4141. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 11
   Example Spring AI Model Context Protocol (MCP)

4142. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 11
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

4143. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 11
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

4144. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 11
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

4145. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 11
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

4146. **[gtm-mcp](https://github.com/pouyanafisi/gtm-mcp)** - ⭐ 11
   MCP server for Google Tag Manager: read tags/triggers/variables, publish containers, and audit changes via Claude/Gemini.

4147. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 11
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

4148. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 11
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

4149. **[mcp-coroot](https://github.com/jamesbrink/mcp-coroot)** - ⭐ 11
   MCP server for Coroot observability platform - integrate monitoring, troubleshooting, and configuration tools with AI agents

4150. **[chromadb-remote-mcp](https://github.com/meloncafe/chromadb-remote-mcp)** - ⭐ 11
   Remote MCP server for ChromaDB

4151. **[msty-admin-mcp](https://github.com/M-Pineapple/msty-admin-mcp)** - ⭐ 11
   AI-powered administration for Msty Studio Desktop. 24 MCP tools for database insights, config sync, local model orchestration, and Claude handoff workflows.

4152. **[miro-mcp-server](https://github.com/olgasafonova/miro-mcp-server)** - ⭐ 11
   MCP server for controlling Miro whiteboards with AI assistants

4153. **[qurio](https://github.com/irahardianto/qurio)** - ⭐ 11
   Self-hosted RAG engine for AI coding assistants. Ingests technical docs & code repositories locally with structure-aware chunking. Serves grounded context via MCP to prevent hallucinations in software development workflows.

4154. **[fathom-mcp](https://github.com/Dot-Fun/fathom-mcp)** - ⭐ 11
   Model Context Protocol server for Fathom AI - access meeting recordings, transcripts, summaries, teams, and webhooks

4155. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 11
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

4156. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 11
   Simple template project for controlling Unity via MCP

4157. **[keycloak-mcp](https://github.com/HaithamOumerzoug/keycloak-mcp)** - ⭐ 11
   MCP server that integrates with Keycloak, allowing you to manage Keycloak users and realms through a standardized protocol. It uses the official Keycloak Admin Client to interact with Keycloak's API.

4158. **[AMS](https://github.com/LastEld/AMS)** - ⭐ 11
   Audit Memory System (AMS): Durable orchestration and memory layer for MCP clients.

4159. **[mcp-oidc-provider](https://github.com/tigrisdata/mcp-oidc-provider)** - ⭐ 11
   Open-sourced mcp-oidc-provider: a minimal, vendor-neutral OIDC layer that sits between MCP clients and your upstream IdP (Auth0/Clerk/Okta).

4160. **[openmessage](https://github.com/MaxGhenis/openmessage)** - ⭐ 11
   Open-source Google Messages client with AI tools (MCP). SMS + RCS from your desktop.

4161. **[lol-client-mcp](https://github.com/johnnyinlee/lol-client-mcp)** - ⭐ 11
   League of Legends Game Client API MCP Server

4162. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 11
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

4163. **[llmcore](https://github.com/Palm1r/llmcore)** - ⭐ 11
   Qt C++ library for working with AI/LLM Providers and MCP

4164. **[mcp-shopline](https://github.com/asgard-ai-platform/mcp-shopline)** - ⭐ 11
   MCP server wrapping the Shopline Open API into 143 AI-callable tools (75 read + 68 write) for e-commerce operations. Built for Claude Code, Claude Desktop, and any MCP-compatible AI client.

4165. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 11
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

4166. **[mcp-bibliotheque_nationale_de_France](https://github.com/Kryzo/mcp-bibliotheque_nationale_de_France)** - ⭐ 11
   Un serveur MCP (Model-Client-Protocol) pour accéder à l'API Gallica de la Bibliothèque nationale de France (BnF) et générer des rapports de recherche séquentiels.

4167. **[GitIntel-MCP-Server](https://github.com/hoangsonww/GitIntel-MCP-Server)** - ⭐ 11
   A Git intelligence MCP server built with Node.js and TypeScript that analyzes local Git repositories to surface insights like hotspots, churn, temporal coupling, knowledge maps, and risk scoring. Designed for AI agents, it exposes repository analytics tools through the Model Context Protocol (MCP) while keeping all data local and read-only.

4168. **[mcp-auth-helper](https://github.com/sdaoudi/mcp-auth-helper)** - ⭐ 11
   Standalone OAuth helper for MCP servers with client allowlists (Figma, etc.) - works with OpenCode without forking

4169. **[bio-agents-mcp](https://github.com/dogeplusplus/bio-agents-mcp)** - ⭐ 11
   MCP servers for Protein Data Bank, ChemBL, and other life science data (WIP), with Ollama client for local testing.

4170. **[alexa-mcp-server](https://github.com/sijan2/alexa-mcp-server)** - ⭐ 11
   amazon alexa mcp server for poke🌴 and other mcp client

4171. **[mcpHTTPClient](https://github.com/matlab-deep-learning/mcpHTTPClient)** - ⭐ 11
   An MCP client in pure MATLAB code

4172. **[openchatwidget](https://github.com/Open-Chat-Widget/openchatwidget)** - ⭐ 11
   AI chat widget in your web app. Supports MCP as a client. 

4173. **[pycentauri](https://github.com/bjan/pycentauri)** - ⭐ 11
   Python client, CLI, and MCP server for the Elegoo Centauri Carbon 3D printer

4174. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 11
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

4175. **[commvault-mcp-server](https://github.com/Commvault/commvault-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server for interacting with Commvault software.

4176. **[streamdeck-mcp](https://github.com/verygoodplugins/streamdeck-mcp)** - ⭐ 11
   MCP server for Elgato Stream Deck control — set buttons, manage pages, wire actions

4177. **[pipulate](https://github.com/pipulate/pipulate)** - ⭐ 10
   Local First AI SEO Software on Nix, FastHTML & HTMX

4178. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 10
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

4179. **[kroki-mcp](https://github.com/utain/kroki-mcp)** - ⭐ 10
   Kroki-MCP is a Go-based Model Context Protocol tool that converts textual diagram definitions (PlantUML, Mermaid, and more) into images via a Kroki backend. Designed for simplicity and flexibility, it supports both local and remote Kroki servers, offers configurable settings, and outputs multiple formats – making it ideal for developers building AI

4180. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 10
   MCP server to give client the ability to access Wikipedia pages

4181. **[taskboard](https://github.com/tcarac/taskboard)** - ⭐ 10
   Local project management with Kanban UI, CLI, and MCP server for AI assistants. SQLite-backed, single binary, installable via Homebrew.

4182. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

4183. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

4184. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

4185. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

4186. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

4187. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

4188. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

4189. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

4190. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

4191. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

4192. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

4193. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

4194. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

4195. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

4196. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

4197. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

4198. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

4199. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

4200. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault 

4201. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

4202. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

4203. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

4204. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

4205. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

4206. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

4207. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

4208. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

4209. **[Simple_MCP_Client](https://github.com/Avento/Simple_MCP_Client)** - ⭐ 10
   Simple MCP Client for OpenAI/Deepseek R1/V3

4210. **[awesome-mcp](https://github.com/gauravfs-14/awesome-mcp)** - ⭐ 10
   A carefully curated collection of high-quality tools, libraries, research papers, projects, and tutorials centered around Model Context Protocol (MCP) — a novel paradigm designed to enable modular, adaptive coordination between large language models (LLMs) and external tools or data contexts.

4211. **[openapi-mcp-swagger](https://github.com/salacoste/openapi-mcp-swagger)** - ⭐ 10
   Solve AI context window limits for API docs | Convert any Swagger/OpenAPI to searchable MCP server | AI-powered endpoint discovery & code generation | Works with Cursor, Claude, VS Code

4212. **[mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig)** - ⭐ 10
   A local MCP server that breaks on demand. Test your client against auth failures, disappearing tools, flaky responses, and token expiry, all from a web UI.

4213. **[notification-mcp](https://github.com/pinkpixel-dev/notification-mcp)** - ⭐ 10
   A Model Context Protocol server that allows AI agents to play a notification sound via a tool when a task is completed.

4214. **[adonis-mcp](https://github.com/7nohe/adonis-mcp)** - ⭐ 10
   An AdonisJS package for building remote MCP servers

4215. **[genkit-mcp-client-blender](https://github.com/xprilion/genkit-mcp-client-blender)** - ⭐ 10
   An MCP Client for interfacing with the Blender MCP Server built with Firebase Genkit and Gemini

4216. **[esp32-mcpserver](https://github.com/solnera/esp32-mcpserver)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server framework for ESP32. Seamlessly connect embedded devices to LLMs.

4217. **[youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server providing real-time YouTube Data API access for AI assistants. Features 14 functions including intelligent content evaluation with technology freshness scoring for knowledge base curation.

4218. **[Azure-Foundry-Webinar](https://github.com/ShivamGoyal03/Azure-Foundry-Webinar)** - ⭐ 10
   This repository is the official companion for the Azure AI Foundry Agent Service Webinar Series. It provides hands-on code samples, modular use cases, and practical guides for building, deploying, and scaling AI agents on Azure.

4219. **[Cognio](https://github.com/0xReLogic/Cognio)** - ⭐ 10
   Persistent semantic memory server for MCP - Give your AI long-term memory that survives across conversations. Lightweight Python server with SQLite storage and semantic search.

4220. **[systemprompt-template](https://github.com/systempromptio/systemprompt-template)** - ⭐ 10
   Production AI agent mesh in 3 commands. MCP servers, playbooks, and multi-agent orchestration built on systemprompt-core.

4221. **[cheatengine-mcp-bridge](https://github.com/beamstar/cheatengine-mcp-bridge)** - ⭐ 10
   🔗 Connect AI to Cheat Engine for fast memory analysis, enabling quick mods and audits without the tedious manual work.

4222. **[toolhive-cloud-ui](https://github.com/stacklok/toolhive-cloud-ui)** - ⭐ 10
   ToolHive Cloud UI surfaces MCP servers running in your infrastructure, highlighting metadata, tool capabilities, and copy-ready endpoints for fast AI agent integrations.

4223. **[mcpd](https://github.com/pouriya/mcpd)** - ⭐ 10
   A ~3MB MCP daemon that exposes any script as a tool for Claude, Cursor & AI assistants

4224. **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** - ⭐ 10
   Extended WhatsApp MCP server with 41 tools - reactions, group management, polls, presence, newsletters & more. Fork of lharries/whatsapp-mcp

4225. **[chessmata](https://github.com/jonradoff/chessmata)** - ⭐ 10
   Chessmata: chess game for humans and AI agents

4226. **[storybook-mcp-server](https://github.com/stefanoamorelli/storybook-mcp-server)** - ⭐ 10
   MCP server for Storybook - provides AI assistants access to components, stories, properties and screenshots. Built with TypeScript and Model Context Protocol SDK.

4227. **[dbt-core-mcp](https://github.com/NiclasOlofsson/dbt-core-mcp)** - ⭐ 10
   dbt Core MCP Server: Interact with dbt projects via Model Context Protocol

4228. **[chatgpt2md](https://github.com/NextStat/chatgpt2md)** - ⭐ 10
   Convert ChatGPT export to Markdown with full-text search and MCP server for Claude

4229. **[mini_claude](https://github.com/20alexl/mini_claude)** - ⭐ 10
   Give Claude Code persistent memory across sessions. Track habits, log mistakes, prevent death spirals. Runs locally with Ollama.

4230. **[statelessagent](https://github.com/sgx-labs/statelessagent)** - ⭐ 10
   Your AI forgets everything between sessions. SAME fixes that. Local-first, no API keys, single binary.

4231. **[MCP-Penetration-testing](https://github.com/Mr-Infect/MCP-Penetration-testing)** - ⭐ 10
   The ultimate OWASP MCP Top 10 security checklist and pentesting framework for Model Context Protocol (MCP), AI agents, and LLM-powered systems.

4232. **[caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for Caltrain schedules. Get real-time train departures using GTFS data, designed for Claude Desktop and other MCP clients.

4233. **[shellguard](https://github.com/fawdyinc/shellguard)** - ⭐ 10
   MCP server that gives LLM agents read-only shell access over SSH

4234. **[PsMCP-MCP-Server-for-Photoshop](https://github.com/Chandrahas455/PsMCP-MCP-Server-for-Photoshop)** - ⭐ 10
   An Extensive MCP server and a Gradio MCP client ( with Gemini ) with several tools made using win32com to intereact with Photoshop. Designing with Photoshop has never been more fun!

4235. **[ollama-mcp-example](https://github.com/kirillsaidov/ollama-mcp-example)** - ⭐ 10
   Ollama MCP example for dummies. 

4236. **[civitai-mcp-server](https://github.com/Cicatriiz/civitai-mcp-server)** - ⭐ 10
   A Model Context Protocol server for browsing and discovering AI models on Civitai

4237. **[openapi-to-mcp](https://github.com/agentic-community/openapi-to-mcp)** - ⭐ 10
   Transform OpenAPI specifications into production-ready MCP servers   with AI-powered evaluation and enhancement. Leverages LLMs to   analyze, improve, and generate Model Context Protocol   implementations from your existing API documentation.

4238. **[world-intel-mcp](https://github.com/marc-shade/world-intel-mcp)** - ⭐ 10
   100+ tool MCP server for real-time global intelligence — markets, FX, bonds, earnings, SEC filings, conflict, military, cyber, climate, news, company enrichment, and 30+ domains. Live Leaflet dashboard with 20 map layers, SSE streaming, and AI situation briefs.

4239. **[ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp)** - ⭐ 10
   🔓 UNLEASH ILSpy'S POWER. Reverse-engineer DOTNET code at GOD SPEED. AI-assisted debugging that THINKS with you. Decompile ANYTHING. 🚀

4240. **[aichat](https://github.com/Hayashi-Yudai/aichat)** - ⭐ 10
   A customizable AI chat application powered by Flet.

4241. **[mcp-document-converter](https://github.com/xt765/mcp-document-converter)** - ⭐ 10
   MCP Document Converter - A powerful MCP tool for converting documents between multiple formats, enabling AI agents to easily transform documents.

4242. **[simple-mcp-server](https://github.com/dataworkshop/simple-mcp-server)** - ⭐ 10
   Simple MCP Server — Educational Example This repository contains a minimal MCP (Model Context Protocol) server built for educational purposes. Its goal is to help developers understand how the MCP protocol works and how to manage decision-making processes based on model–client communication.

4243. **[cubbi](https://github.com/Monadical-SAS/cubbi)** - ⭐ 10
   Monadical container CLI tool for running sandboxed MCP clients & servers

4244. **[team-memory-mcp](https://github.com/gustavolira/team-memory-mcp)** - ⭐ 10
   Shared team memory for AI coding agents. Bayesian confidence scoring with temporal decay. Works with Claude Code, Devin, Cursor, and any MCP-compatible client.

4245. **[ai-assistant-vui](https://github.com/mgoltzsche/ai-assistant-vui)** - ⭐ 10
   Experimental voice user interface (VUI) to interact with an agentic AI assistant

4246. **[mcp-client](https://github.com/CopilotKit/mcp-client)** - ⭐ 10

4247. **[tupac](https://github.com/tkellogg/tupac)** - ⭐ 10
   A terminal MCP client based on the OpenAI responses API.

4248. **[ai-mcp-bridge](https://github.com/xiaozhug/ai-mcp-bridge)** - ⭐ 10
   rest to mcp & mcp Registry & mcp Loadbalancer & ai mcp & Multiple Registries & 多注册中心 

4249. **[cli](https://github.com/inboxapi/cli)** - ⭐ 10
   🤖 Your Agents' personal email 📧  

4250. **[mcp-shell](https://github.com/Prat011/mcp-shell)** - ⭐ 10
   terminal based MCP Client 

4251. **[mcp-google-calendar](https://github.com/guinacio/mcp-google-calendar)** - ⭐ 10
   A MCP server that allows Claude and other MCP clients to interact with Google Calendar. This server enables AI assistants to manage your calendar events, check availability, and handle scheduling tasks.

4252. **[discogs-mcp](https://github.com/rianvdm/discogs-mcp)** - ⭐ 10
   A Discogs MCP Server with OAuth, to use with your favorite LLM client. Ask for recommendations, stats about your collection, details about releases you own, and more!

4253. **[capacities-mcp-bridge-unofficial](https://github.com/natkitten/capacities-mcp-bridge-unofficial)** - ⭐ 10
   Unofficial MCP tools and bridges for Capacities.io, for use with Claude Desktop, Genspark, and other clients.

4254. **[local-voice-mcp](https://github.com/CodeCraftersLLC/local-voice-mcp)** - ⭐ 10
   Give your MCP clients the ability to speak by running local voice models

4255. **[ctx-sys](https://github.com/david-franz/ctx-sys)** - ⭐ 10
   Intelligent context management for AI coding assistants. Indexes your codebase with tree-sitter, builds a semantic knowledge graph, and serves 12 tools over MCP. Hybrid RAG combines keyword search, vector embeddings, and graph traversal for precise retrieval. Works with Claude Desktop, Cursor, and any MCP client. Fully local with Ollama.

4256. **[auxilia](https://github.com/keurcien/auxilia)** - ⭐ 10
   A lightweight web MCP client designed to host your MCP-powered AI assistants. auxilia is designed to only support remote MCP servers.

4257. **[laravel-release-changelog-generator](https://github.com/lightszentip/laravel-release-changelog-generator)** - ⭐ 10
   Generate a changelog and releases with version management with artisan

4258. **[mistral-ai-docs-mcp-server](https://github.com/nikhilbhima/mistral-ai-docs-mcp-server)** - ⭐ 10
   Unofficial MCP server for Mistral AI developer docs and API reference. One public URL, no auth, works in every MCP client.

4259. **[flipper-mcp](https://github.com/roostercoopllc/flipper-mcp)** - ⭐ 10
   AI-powered MCP server for Flipper Zero. Control SubGHz, NFC, RFID, IR, BLE, GPIO, and more over WiFi using Claude or any MCP client.

4260. **[mcp-server](https://github.com/finmap-org/mcp-server)** - ⭐ 10
   The finmap.org MCP server provides comprehensive historical data from the US, UK, Russian and Turkish stock exchanges. Access sectors, tickers, company profiles, market cap, volume, value, and trade counts, as well as treemap and histogram visualizations

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 46,013
   LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

2. **[CowAgent](https://github.com/zhayujie/CowAgent)** - ⭐ 43,977
   CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

3. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 42,983
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 10,537
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[evolver](https://github.com/EvoMap/evolver)** - ⭐ 7,181
   The GEP-powered self-evolving engine for AI agents. Auditable evolution with Genes, Capsules, and Events. | evomap.ai

6. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,766
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

7. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,803
   Magicrew. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

8. **[koog](https://github.com/JetBrains/koog)** - ⭐ 4,143
   Koog is a JVM (Java and Kotlin) framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

9. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,356
   extendable code review and QA agent 🚢

10. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,323
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.1, Claude, DeepSeek V4, Grok, OpenRouter, Kimi 2.5, GLM 5, SiliconFlow, GPT-oss, Gemma 4, Qwen 3.5

11. **[nono](https://github.com/always-further/nono)** - ⭐ 2,204
   nono - a capability-based, multiplexing sandbox tool, built for developers - lift'n'shift seamless path to prod. Run agents securely without needing any additional infra, zero setup, zero latency. 

12. **[ragent](https://github.com/nageoffer/ragent)** - ⭐ 1,860
   企业级 Agentic RAG 智能体 - 全链路覆盖文档解析、多路检索、意图识别、问题重写、会话记忆、MCP 工具调用与深度思考。面向真实业务场景，从 0 到 1 完整工程实现。

13. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,682
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

14. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,642

15. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 949
   OpenTelemetry Instrumentation for AI Observability

16. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 855
   A code repository indexing tool to supercharge your LLM experience.

17. **[openyak](https://github.com/openyak/openyak)** - ⭐ 806
   OpenYak — open-source local AI agent for Windows, macOS, and Linux. A private, BYOK alternative to Claude Code, Claude for Work, and OpenAI Codex with 20+ tools, 100+ models via OpenRouter, MCP, and Ollama. Free, MIT-licensed, no telemetry.

18. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 712
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

19. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 581
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

20. **[aimock](https://github.com/CopilotKit/aimock)** - ⭐ 570
   Mock everything your AI app talks to — LLM APIs, MCP, A2A, AG-UI, vector DBs, search. One package, one port, zero dependencies.

21. **[comunica](https://github.com/comunica/comunica)** - ⭐ 560
   📬 A knowledge graph querying framework for JavaScript

22. **[casbin-gateway](https://github.com/apache/casbin-gateway)** - ⭐ 559
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

23. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 534
   The easiest way to discover and install MCPs

24. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 485
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

25. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 435
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

26. **[pwno-mcp](https://github.com/pwno-io/pwno-mcp)** - ⭐ 252
   MCP for Pwn

27. **[openclaw.net](https://github.com/clawdotnet/openclaw.net)** - ⭐ 243
   Self-hosted OpenClaw gateway + agent runtime in .NET (NativeAOT-friendly)

28. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 219
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

29. **[ai](https://github.com/WordPress/ai)** - ⭐ 177
   AI features and experiments for WordPress. Modular framework for testing AI capabilities.

30. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 159
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

31. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

32. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 109
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

33. **[uxc](https://github.com/holon-run/uxc)** - ⭐ 104
   A unified CLI for discovering and invoking tools across OpenAPI, MCP, GraphQL, gRPC, and JSON-RPC

34. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

35. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 95
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

36. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 94
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

37. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 91
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

38. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

39. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 58

40. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 50
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

41. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

42. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

43. **[ziya](https://github.com/ziya-ai/ziya)** - ⭐ 35
   Self-hosted AI technical workbench. Visual, persistent, multi-stream. Development, architecture, and operational analytics without losing context.

44. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

45. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 28
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

46. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 27
   MCP Web Client project

47. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

48. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

49. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

50. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

51. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 21
   Powered by Ray (video) and Photon (image) models by Luma AI

52. **[ai](https://github.com/JoakimCarlsson/ai)** - ⭐ 20
   A Go toolkit for building AI agents and applications across multiple providers. Unified LLM client, agent framework with handoffs, tool calling, streaming, structured output, MCP integration, and cost tracking.

53. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 19
   A desktop client with MCP support for Mistral LLMs

54. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

55. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 11

56. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 11
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

57. **[ArcaMCP](https://github.com/Yoryoboy/ArcaMCP)** - ⭐ 10
   Servidor MCP para AFIP/ARCA: automatiza certificados, autorización de Web Services, emisión/consulta de comprobantes y generación de PDF con QR.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 186,504
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[goose](https://github.com/aaif-goose/goose)** - ⭐ 43,690
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

3. **[kong](https://github.com/Kong/kong)** - ⭐ 43,303
   🦍 The API and AI Gateway

4. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 39,094
   AI Data Vault - A query engine for AI Agents to securely query data from any datasource

5. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 27,889
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

6. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,650
   Your ultimate Go microservices framework for the cloud-native era.

7. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,544
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

8. **[plate](https://github.com/udecode/plate)** - ⭐ 16,221
   Rich-text editor with AI and shadcn/ui

9. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

10. **[hyperframes](https://github.com/heygen-com/hyperframes)** - ⭐ 13,931
   Write HTML. Render video. Built for agents.

11. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 13,778
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

12. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 11,837
   LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including MCP support), agents and RAG easy. It integrates seamlessly with enterprise Java frameworks like Quarkus and Spring Boot.

14. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,834
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

15. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 11,730
   A cross-platform Markdown AI note-taking software.

16. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,844
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,769
    The most powerful Android RPA agent framework, next generation mobile automation.

18. **[adk-go](https://github.com/google/adk-go)** - ⭐ 7,735
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

19. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 7,467
   💻 vibe coding 2026 | Your first modern programming course for beginners to master step by step.

20. **[codefather](https://github.com/liyupi/codefather)** - ⭐ 7,240
   程序员鱼皮的编程宝典 ⭐️ 2026年最全编程学习路线图！包含Java学习路线、前端学习路线、Python学习路线、C++学习路线、算法学习路线、计算机基础学习路线、AI应用开发学习路线、AI Agent开发学习路线等。提供编程入门教程、AI大模型应用开发教程、RAG开发实战、MCP开发教程、Prompt工程指南、LLM应用开发、技术知识分享、学习资源推荐、项目实战教程、热门面试题、求职经验、简历优化、编程自学指南等内容，适用于所有零基础学编程、学习AI开发、转行程序员、计算机专业学生、求职找工作的同学 💎 编程学习，就来编程导航！

21. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 5,687
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

22. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 5,213
   面向企业级市场的一站式AI应用开发框架，支持多厂商大模型统一接入与管理，具备安全可控的企业知识库与高精度检索优化能力，提供可视化流程编排、自主决策智能体与多智能体协同调度，兼容主流 Agent Skill 协议，帮助企业与开发者零门槛快速构建安全、高效、可落地的AI智能体应用与行业解决方案。

23. **[Yuxi](https://github.com/xerrors/Yuxi)** - ⭐ 5,069
   结合知识库管理的 多租户 Agent Harness 平台。 An agent harness that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

24. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 5,039
   Adversary simulation and Red teaming platform with AI

25. **[API-mega-list](https://github.com/cporter202/API-mega-list)** - ⭐ 4,917
   This GitHub repo is a powerhouse collection of APIs you can start using immediately to build everything from simple automations to full-scale applications. One of the most valuable API lists on GitHub—period. 💪

26. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,667
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

27. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,467
   AG2 (formerly AutoGen): The Open-Source AgentOS.Join us at: https://discord.gg/sNGSwQME3x

28. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,384
   Nexent is a zero-code platform for auto-generating production-grade AI agents using Harness Engineering principles — unified tools, skills, memory, and orchestration with built-in constraints, feedback loops, and control planes.

29. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,369
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

30. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,093
   Bulk port forwarding Kubernetes services for local development.

31. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 4,049
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

32. **[holaOS](https://github.com/holaboss-ai/holaOS)** - ⭐ 3,882
   An Open Agent Computer for ANY digital work.

33. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,309
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

34. **[claude-code-book](https://github.com/lintsinghua/claude-code-book)** - ⭐ 3,065
   《御舆：解码 Agent Harness》42万字拆解 AI Agent 的Harness骨架与神经 —— Claude Code 架构深度剖析，15 章从对话循环到构建你自己的 Agent Harness。在线阅读网站：

35. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,916
   A highly opinionated, zero-configuration linter and formatter.

36. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,724
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

37. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 2,253
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

38. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 2,070
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流

39. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,946
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

40. **[DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner)** - ⭐ 1,771
   🎨 NeMo Data Designer: Generate high-quality synthetic data from scratch or from seed data.

41. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,741
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

42. **[Klee](https://github.com/signerlabs/Klee)** - ⭐ 1,731
   A native macOS AI chat app powered by MLX. 100% local inference on Apple Silicon, no cloud required. Built with ShipSwift.

43. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,660
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

44. **[Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills)** - ⭐ 1,627
   VibeSkills is a new kind of super skill that organizes 340+ governed skills into one stable AI work system.

45. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,588
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

46. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,512
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

47. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,449
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

48. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

49. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,332
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

50. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,330
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

51. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

52. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,324
   Korea Investment & Securities Open API Github

53. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,263
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

54. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 1,263
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

55. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 1,244
   Local first codebase intelligence

56. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

57. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,227
   [Acquired by The Guild] The Grafbase GraphQL Federation Gateway

58. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,188
   Search, understand, reproduce, and improve an idea with ease

59. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,158
   A single interface to use and evaluate different agent frameworks 

60. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,081
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

61. **[rulesync](https://github.com/dyoshikawa/rulesync)** - ⭐ 1,063
   A Utility CLI for AI Coding Agents

62. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 1,021
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

63. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 990
   Arduino MCP2515 CAN interface library

64. **[cursor2api-go](https://github.com/libaxuan/cursor2api-go)** - ⭐ 934
   Free claude-sonnet-4.6  | cursor不倒我不倒🙏 ❌ 不支持 tools / function calling / MCP

65. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 922
   LightAgent: Lightweight AI agent framework with memory, mcp & skill. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

66. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 905
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps. I mainly use it as an xcodebuild wrapper to save context.

67. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 826
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

68. **[eDBG](https://github.com/ShinoLeah/eDBG)** - ⭐ 805
   eBPF-based lightweight debugger for Android with MCP support

69. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 780
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

70. **[axi](https://github.com/kunchenguid/axi)** - ⭐ 778
   Design principles for agent ergonomics. Higher accuracy with lower token cost than both MCP and regular CLI.

71. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 766
   Solidity Static Analyzer that easily integrates into your editor

72. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 754
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

73. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 737
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

74. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 713
   JiwuChat 🍂 - A lightweight cross-platform instant messaging app with integrated AI assistants (DeepSeek/Gemini/Kimi). Features real-time messaging, audio/video calls, multi-device sync, and customizable themes. Built with Vue3 & Tauri2 🍒

75. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 679
   A personal AI assistant for everyone

76. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 666
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

77. **[how-to-vibecoding](https://github.com/1EchA/how-to-vibecoding)** - ⭐ 656
   Vibecoding 系列教程：从环境搭建到多智能体协作，涵盖 MCP、Skills、Agent 分工治理

78. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 656
   UI components for AI interfaces

79. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 631
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

80. **[vocotype-cli](https://github.com/233stone/vocotype-cli)** - ⭐ 623
   VocoType 是一款运行在本地端侧的隐私安全语音输入工具，通过快捷键即可将语音实时转换为文字并自动输入到当前应用。支持语音转文字MCP、AI 优化文本、自定义替换词典、录音视频转文字等功能，让语音输入更高效、更安全。

81. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 603
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

82. **[claude-code-cli](https://github.com/huangserva/claude-code-cli)** - ⭐ 571
   这是 Claude Code 的 CLI 客户端主体（src/ 目录），即整个终端交互层的源码。具体包含： 1. CLI 入口与命令解析 — main.tsx（4684行）、entrypoints/（CLI 模式、SDK 模式、MCP 模式） 2. 终端 UI 渲染 — components/（144 个组件，用 React + Ink 渲染终端界面） 3. 工具系统 — tools/（43 个工具，Bash、文件读写编辑、Grep、Glob、Web 搜索等） 4. API 通信层 — services/api/（与 Anthropic 后端通信） 5. MCP 协议  6. 多 Agent/Team 协作 l 7. 认证与策略 8. 辅助服务 等

83. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 559
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

84. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 558
   🚀 告别多个App！本项目主要基于Python+React+TypeScript+Hono+SQLite3+Redis，打造“All in One”智能工具集。免会员破解爱奇艺、腾讯视频、优酷、抖音、B站、小红书等20+平台视频，支持4K在线解析与无水印高速下载。集成Cloudflare Turnstile防机器人和爬虫、Google、GitHub授权登录及OpenAI SDK、埋点SDK、MCP服务和Agent等，支持ChatGPT对话、AI绘画、论文降重、Hugging Face论文爬取、在线Latex编写；更有实时黄金K线、AI思维导图、闲鱼助手等效率黑科技。内置海量动漫漫画资源，畅享阅读！轻量高效，配置即用，完美适配PC与移动端，快来ChattyPlay开启奇妙之旅吧～

85. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 540
   Marmot is an open-source data catalog designed for teams who want powerful data discovery without enterprise complexity. Catalog every data asset, enrich it with the context that matters and make it accessible to your team and your AI tools.

86. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 482
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

87. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 476
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

88. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

89. **[machi](https://github.com/qntx/machi)** - ⭐ 446
   Agent behavior that compiles.

90. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 438
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

91. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

92. **[spool](https://github.com/spool-lab/spool)** - ⭐ 427
   Search your Claude Code sessions, Codex history, GitHub stars, and 50+ sources — locally, instantly. Your AI agents can search too.

93. **[bridle](https://github.com/neiii/bridle)** - ⭐ 419
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

94. **[reins](https://github.com/pegasi-ai/reins)** - ⭐ 410
   Stop AI agents from doing things you didn't ask for.

95. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 400
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

96. **[agent-desktop](https://github.com/lahfir/agent-desktop)** - ⭐ 397
   Native desktop automation CLI for AI agents. Control any application through OS accessibility trees with structured JSON output and deterministic element refs.

97. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 394
   Python toolkit for building graph-enhanced GenAI applications

98. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 393
   MCP for Unreal Engine 5

99. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 393
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

100. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 391
   Minecraft: Pi Edition API Python Library

101. **[volcano-agent-sdk](https://github.com/Kong/volcano-agent-sdk)** - ⭐ 390
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

102. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

103. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 381
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

104. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 378
   Arduino Library for Adafruit MCP23017

105. **[ai4paper](https://github.com/wdcpclover/ai4paper)** - ⭐ 376
   AI一键文献综述 · AI一键搜文献 · AI笔记管理 · 原生GPT直连 · MCP协议 · 支持Zotero 7/8/9 | AI4Paper.pro

106. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 355
   Blender python addon to increase workflow for creating minecraft renders and animations

107. **[exograph](https://github.com/exograph/exograph)** - ⭐ 345
   Build production-ready backends in minutes

108. **[depyler](https://github.com/paiml/depyler)** - ⭐ 344
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

109. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 340
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

110. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

111. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 317
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

112. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

113. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 304
   An in-depth book and reference on building agentic systems like Claude Code

114. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 304
   小红书创作中心

115. **[skene](https://github.com/SkeneTechnologies/skene)** - ⭐ 290
   Product-Led Growth (PLG) analysis toolkit that detects tech stacks, plans growth loops and builds the loop iteratively.

116. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 282
   AI for Ethical Hacking - Workshop

117. **[genie](https://github.com/automagik-dev/genie)** - ⭐ 280
   Wishes in, PRs out. CLI agent that interviews you, plans the work, dispatches parallel agents in isolated worktrees, and reviews code before you see it.

118. **[scribe.js](https://github.com/scribeocr/scribe.js)** - ⭐ 271
   JavaScript OCR and text extraction for images and PDFs.

119. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 269
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

120. **[talkio](https://github.com/llt22/talkio)** - ⭐ 268
   Local-first multi-AI group chat desktop app — pull gpt, Claude, Gemini, DeepSeek into one conversation. Tauri 2 + React 19.

121. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

122. **[PSAI](https://github.com/dfinke/PSAI)** - ⭐ 256
   High-agency PowerShell AI framework for multi-agent orchestration and autonomous systems engineering

123. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 253
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

124. **[agentica](https://github.com/shibing624/agentica)** - ⭐ 246
   Agentica: Lightweight async-first Python framework for AI agents. 轻量级异步优先的AI Agent框架，支持工具调用、RAG、多智能体和MCP。

125. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 244
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

126. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 244
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

127. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 240
   Public facing repo for MCP SRG mappings.

128. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 240
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

129. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 238
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

130. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 233
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

131. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

132. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 228
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

133. **[LAP](https://github.com/Lap-Platform/LAP)** - ⭐ 223
   Your agents are guessing at APIs. Give them the actual Agent-Native spec. 1500+ API's Ready To-Use skills,  Compile any API spec into a lean, agent-native format. 10× smaller. OpenAPI, GraphQL, AsyncAPI, Protobuf, Postman.

134. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

135. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

136. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

137. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

138. **[weam](https://github.com/weam-ai/weam)** - ⭐ 214
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

139. **[claudemap](https://github.com/QuinnAho/claudemap)** - ⭐ 213
   google maps for vibecoders.

140. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

141. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 201
   Re-usable multi part components built on React Aria and TailwindCSS. 

142. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

143. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

144. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 178
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

145. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

146. **[OnionClaw](https://github.com/christinminor459/OnionClaw)** - ⭐ 168
   Provide AI agents with full Tor network access and dark web data through a zero-config OpenClaw skill or standalone tool.

147. **[selene](https://github.com/tercumantanumut/selene)** - ⭐ 166
   Selene is a desktop app that runs AI agents on your machine. Connect them to your WhatsApp, Telegram, Slack, or Discord. Write code, generate images, build personal assistants. All from one place. Your data stays on your device.

148. **[structurizr](https://github.com/structurizr/structurizr)** - ⭐ 165
   Structurizr is a "models as code" tool designed for the C4 model.

149. **[claude-android-skill](https://github.com/dpconde/claude-android-skill)** - ⭐ 164
   Claude Code skill for building modern Android apps following best practices.

150. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 160
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

151. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 155
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

152. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 148
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

153. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 143
   Seline is a local-first AI desktop application that brings together conversational AI, visual generation tools, vector search, and multi-channel connectivity in one place.

154. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 142
   ☕ Community-driven Java implementation of TOON

155. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

156. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

157. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 134
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

158. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 128
   A curated list of open source repositories for AI Engineers

159. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 127
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

160. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 119
   5-Day Gen AI Intensive Course with Google

161. **[agentic-ai](https://github.com/mahmoudrabie/agentic-ai)** - ⭐ 118
   This repository serves as a comprehensive knowledge hub, curating cutting-edge research papers and developments across 24 specialized domains

162. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 117
   Unity plugin for Coplay

163. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 116
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

164. **[roampal](https://github.com/roampal-ai/roampal)** - ⭐ 116
   Memory that learns what works.

165. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 115
   Solid Tumor Associative Modeling in Pathology

166. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 115
   One-click launch URL generator for protocol-based apps

167. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 114
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

168. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 111
   Scalable and extensible reinforcement learning for LM agents.

169. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 110
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

170. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 109
   谷歌5天AI Agents强化课程

171. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 106
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

172. **[GenAI-AgenticAI-From-Zero-to-Production](https://github.com/bansalkanav/GenAI-AgenticAI-From-Zero-to-Production)** - ⭐ 103
   Learn GenAI and Agentic AI from Zero to Production

173. **[Manifold](https://github.com/Garume/Manifold)** - ⭐ 102
   Operation-first .NET foundation for generating fast CLI and MCP surfaces from a single definition.

174. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 92
   ai memory for coding

175. **[yes-ue-mcp](https://github.com/softdaddy-o/yes-ue-mcp)** - ⭐ 83
   Native C++ Model Context Protocol (MCP) plugin for Unreal Engine 5.4+

176. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP 

177. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 79
   A lightweight, open, and extensible multi-LLM interaction studio.

178. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

179. **[open-skills](https://github.com/besoeasy/open-skills)** - ⭐ 78
   Battle-tested skill library for AI agents. Save 98% of API costs with ready-to-use code for crypto, PDFs, search, web scraping & more. No trial-and-error, no expensive APIs.

180. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 77
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

181. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 75
   Quarkus Langchain4J Workshop

182. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 75
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

183. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 74
   OneMCP feature requests, bugs and improvements 

184. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 69
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

185. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 65
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

186. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 64
   MeMesh Plugin — Searchable project memory plugin for Claude Code.

187. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 62
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

188. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 61
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

189. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 56
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

190. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 53
   Houdini integration through the Model Context Protocol

191. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 51
   chm to markdown and vectorDB

192. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 48
   Backported Model Context Protocol SDK for Java 8

193. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 48
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

194. **[velocity](https://github.com/OptimiLabs/velocity)** - ⭐ 41
   Local-first workspace for Claude Code, Codex CLI, and Gemini CLI with sessions, analytics, workflows, and tools

195. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

196. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 37
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

197. **[Agience](https://github.com/Agience/Agience)** - ⭐ 36
   MCP-native workspace for turning live work into durable knowledge.

198. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 35
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

199. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 35
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

200. **[mini-coder](https://github.com/sacenox/mini-coder)** - ⭐ 34
   A good idea 👾

201. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

202. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 32
   Prompt-driven automation platform - Transform natural language into executable workflows

203. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 32
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

204. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 30
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

205. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

206. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 27
   Build AI Agent using Google ADK , MCP and Gemma 3 model

207. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

208. **[codai](https://github.com/codai-agent/codai)** - ⭐ 25
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

209. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 21
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

210. **[codectx](https://github.com/hey-granth/codectx)** - ⭐ 17
   Codebase context compiler for AI agents. Graph-ranked, token-budgeted, tier-compressed output. Smarter than the existing ones.

211. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

212. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 17
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

213. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

214. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

215. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 15
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

216. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 14
   Multi-agent system for software development

217. **[pic-standard](https://github.com/madeinplutofabio/pic-standard)** - ⭐ 14
   The industry standard for Provenance & Intent Contracts (PIC) in Agentic AI. Bridging the Causal Gap in autonomous systems.

218. **[Tapnow-Studio--](https://github.com/Menaelz/Tapnow-Studio--)** - ⭐ 14
   🎨 Create visual AI workflows with Tapnow Studio, a browser-based tool that combines powerful AI capabilities in a single, interactive node editor.

219. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

220. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

221. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 12
   Unity MCP Tool template project

222. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

223. **[claude-colony](https://github.com/MakingJamie/claude-colony)** - ⭐ 10
   Multi-agent Claude Code you can actually control. Spawn specialist teams in tmux, watch them work side-by-side, steer when needed. Built on native Claude Code agents. No black boxes.

224. **[Ai_agents](https://github.com/jenasuraj/Ai_agents)** - ⭐ 10
   This is a repository of collection of many agents build on top of Langchain , Langgraph, MCP and so many amazing tools

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,626
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

3. **[claude-mcp-examples](https://github.com/charIesding/claude-mcp-examples)** - ⭐ 151
   examples of claude with mcp integration

4. **[End-to-End-Agentic-Ai-Automation-Lab](https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab)** - ⭐ 50
   This repository contains hands-on projects, code examples, and deployment workflows. Explore multi-agent systems, LangChain, LangGraph, AutoGen, CrewAI, RAG, MCP, automation with n8n, and scalable agent deployment using Docker, AWS, and BentoML.

5. **[claude-mcp](https://github.com/thinkbigcd/claude-mcp)** - ⭐ 16
   claude and mcp integration examples and tutorials

6. **[agent-examples](https://github.com/kagenti/agent-examples)** - ⭐ 12
   Sample Agents and Tools for Kagenti platform

### Documentation

*Documentation, tutorials, and learning resources*

1. **[JavaGuide](https://github.com/Snailclimb/JavaGuide)** - ⭐ 155,368
   Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

2. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 12,945
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档，已升级为鱼皮 AI 导航网站

3. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 7,986
   Specification and documentation for the Model Context Protocol

4. **[wechatDownload](https://github.com/qiye45/wechatDownload)** - ⭐ 7,472
   微信公众号文章批量下载工具，支持评论、合集下载，支持保存html/mhtml/md/pdf/docx/csv文件，保存文章内图片、视频、音频文件，支持MCP/Skill调用

5. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 514
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

6. **[platform-engineering](https://github.com/codetocloudorg/platform-engineering)** - ⭐ 94
   A centralized hub for platform engineering teams, providing resources, best practices, and automation tools. Includes IaC templates, blueprints, and operational guides to help build scalable, secure, and efficient platforms for cloud-native environments and DevSecOps workflows.

7. **[forksilly.doc](https://github.com/fatsnk/forksilly.doc)** - ⭐ 94
   Documents repo of ForkSilly. ForkSilly：兼容sillytavern（酒馆）角色卡、世界书、正则、预设、聊天记录的安卓移动端应用；同时也可作为stable diffusion客户端使用。

8. **[pew-pew-plaza-packs](https://github.com/appboypov/pew-pew-plaza-packs)** - ⭐ 83
   AI-powered project management framework based on an opinionated view on effective prompts and a highly modular approach to building effective agents, workflows, templates, prompts and context documents.

9. **[Agent-Fusion](https://github.com/krokozyab/Agent-Fusion)** - ⭐ 57
    Agent Fusion is a local RAG semantic search engine that gives AI agents instant access to your code, documentation (Markdown, Word, PDF). Query    your codebase from code agents without hallucinations. Runs 100% locally, includes a lightweight embedding model, and optional multi-agent task    orchestration. Deploy with a single JAR

10. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 27
    A powerful system for crawling documentation websites, extracting code snippets, and providing fast search capabilities via MCP (Model Context Protocol) integration.

11. **[Q4_learning](https://github.com/DanielHashmi/Q4_learning)** - ⭐ 15
   This repository serves as the comprehensive workspace for Quarter 4 academic endeavors, encompassing assignments, technical documentation, experimental implementations, and applied projects.

---

## 📋 Project Criteria

- ⭐ At least 10 stars
- 📝 Must have a README file
- 🔍 Discovered through keywords, topics, and tags related to MCP

## 🤖 Automation

This repository uses automated scripts that:

1. **Collect** projects daily via GitHub Search API
2. **Categorize** projects by use case (servers, clients, tools, examples, documentation)
3. **Translate** content into multiple languages using AI translation
4. **Update** the website automatically

## 🏗️ Structure

```
awesome-mcp/
├── .github/workflows/    # GitHub Actions automation
├── scripts/              # Python collection and translation scripts
├── data/                 # JSON data files
└── docs/                 # VitePress site source
```

## 📝 License

Licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👥 Maintainers

This project is maintained by AI coding assistants:

- **Cursor** - AI-powered code editor
- **Claude Code** - Anthropic's AI coding assistant
- **DeepSeek** - DeepSeek AI coding assistant
- **Gemini** - Google's AI coding assistant

These AI assistants collaborate to keep the project up-to-date, collect new MCP projects, and maintain the quality of the curated list.

## 🙏 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

