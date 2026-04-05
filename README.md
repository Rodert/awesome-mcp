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

## 📚 Projects (4320 total)

> Last updated: **2026-04-05**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 138,364
   The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

2. **[dify](https://github.com/langgenius/dify)** - ⭐ 136,008
   Production-ready platform for agentic workflow development.

3. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 130,082
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

4. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 100,240
   An open-source AI agent that brings the power of Gemini directly into your terminal.

5. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 84,231
   A collection of MCP servers.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 82,981
   Model Context Protocol Servers

7. **[netdata](https://github.com/netdata/netdata)** - ⭐ 78,313
   The fastest path to AI-powered full stack observability, even for lean teams.

8. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 77,139
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

9. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 74,746
   The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

10. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

11. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 57,662
   The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

12. **[context7](https://github.com/upstash/context7)** - ⭐ 51,642
   Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

13. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 51,169
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

14. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 50,874
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

15. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 45,729
   一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

16. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 38,953
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

17. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

18. **[goose](https://github.com/block/goose)** - ⭐ 35,819
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

19. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 35,233
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

20. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 34,649
   🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

21. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 33,200
   Chrome DevTools for coding agents

22. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 33,162
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

23. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

24. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,791
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

25. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 32,704
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

26. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 30,681
   Installable GitHub library of 1,340+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows, and official/community skill collections.

27. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 30,284
   Playwright MCP server

28. **[ruflo](https://github.com/ruvnet/ruflo)** - ⭐ 29,823
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

29. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 29,255
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

30. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 28,970
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

31. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 28,558
   GitHub's official MCP Server

32. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 27,637
   Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

33. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 26,238
   An autonomous agent that conducts deep research on any data using any LLM providers

34. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 25,372
   An MCP-based chatbot | 一个基于MCP的聊天机器人

35. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,529
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

36. **[fastmcp](https://github.com/PrefectHQ/fastmcp)** - ⭐ 24,298
   🚀 The fast, Pythonic way to build MCP servers and clients.

37. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 23,049
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

38. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 22,978
   Build and run agents you can see, understand and trust.

39. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,902
   🚀 The fast, Pythonic way to build MCP servers and clients

40. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 22,692
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

41. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 22,510
   The official Python SDK for Model Context Protocol servers and clients

42. **[serena](https://github.com/oraios/serena)** - ⭐ 22,480
   A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent

43. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 21,574
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

44. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 20,643
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

45. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 18,381

46. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 17,523
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

47. **[openfang](https://github.com/RightNow-AI/openfang)** - ⭐ 16,252
   Open-source Agent Operating System

48. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 15,999
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

49. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 15,896
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

50. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 15,796
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

51. **[page-agent](https://github.com/alibaba/page-agent)** - ⭐ 15,157
   JavaScript in-page GUI agent. Control web interfaces with natural language.

52. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 15,103
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

53. **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** - ⭐ 15,099
   Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

54. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 14,368
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

55. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 14,150
   MCP server to provide Figma layout information to AI coding agents like Cursor

56. **[electerm](https://github.com/electerm/electerm)** - ⭐ 13,833
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(linux, mac, win)

57. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 13,737
   MCP Toolbox for Databases is an open source MCP server for databases.

58. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

59. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 13,300
   Memory for 24/7 proactive agents like openclaw (moltbot, clawdbot).

60. **[casdoor](https://github.com/casdoor/casdoor)** - ⭐ 13,284
   An open-source AI-first Identity and Access Management (IAM) /AI MCP & agent gateway and auth server with web UI supporting MCP, A2A, OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD

61. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 12,595
   MCP for xiaohongshu.com

62. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 12,332
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

63. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 12,095
   The official TypeScript SDK for Model Context Protocol servers and clients

64. **[kubeshark](https://github.com/kubeshark/kubeshark)** - ⭐ 11,853
   eBPF-powered network observability for Kubernetes. Indexes L4/L7 traffic with full K8s context, decrypts TLS without keys. Queryable by AI agents via MCP and humans via dashboard.

65. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,776
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

66. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,369
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

67. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 11,202
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

68. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 11,095
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

69. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,965
   Yet another WebUI for Nginx

70. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 10,659
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

71. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

72. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 9,677
   The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

73. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 9,498
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

74. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 9,332
   Visual testing tool for MCP servers

75. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 9,133
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

76. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 8,682
   Official MCP Servers for AWS

77. **[superset](https://github.com/superset-sh/superset)** - ⭐ 8,628
   Code Editor for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

78. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,537
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

79. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,201
   Build effective agents using Model Context Protocol and simple workflow patterns

80. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 8,151
   MCP Server for Ghidra

81. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 8,096
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

82. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 8,005
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

83. **[webiny-js](https://github.com/webiny/webiny-js)** - ⭐ 7,955
   Open-source, self-hosted CMS platform on AWS serverless (Lambda, DynamoDB, S3). TypeScript framework with multi-tenancy, lifecycle hooks, GraphQL API, and AI-assisted development via MCP server. Built for developers at large organizations.

84. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,875
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

85. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 7,875
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

86. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 7,381
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

87. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

88. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 7,286
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, images, and structured information from PDFs, Office documents, images, and 91+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, R, C, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

89. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 7,247
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

90. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,165
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

91. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 7,116
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

92. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 6,782
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

93. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,635
   A community driven registry service for Model Context Protocol (MCP) servers.

94. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,611
   TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

95. **[context-mode](https://github.com/mksglu/context-mode)** - ⭐ 6,503
   Privacy-first. MCP is the protocol for tool access. We're the virtualization layer for context.

96. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,377
   A collection of MCP clients.

97. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 6,232
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

98. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

99. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,949
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

100. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,848
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

101. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,842
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

102. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,756
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

103. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,701
   Klavis AI:  MCP integration platforms that let AI agents use tools reliably at any scale

104. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,542
   A model-driven approach to building AI agents in just a few lines of code.

105. **[Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** - ⭐ 5,492
   ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.

106. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,485
   WhatsApp MCP server

107. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,465
   A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

108. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,391
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

109. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,368
   Awesome MCP Servers - A curated list of Model Context Protocol servers

110. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 5,297
   Learn AI and LLMs from scratch using free resources

111. **[microsandbox](https://github.com/superradcompany/microsandbox)** - ⭐ 5,251
   local-first and programmable sandboxes for AI agents

112. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 5,174
   opensource secure local-first sandboxes for ai agents

113. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,141
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

114. **[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)** - ⭐ 5,029
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

115. **[CodePilot](https://github.com/op7418/CodePilot)** - ⭐ 5,024
   A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your phone. Built with Electron + Next.js.

116. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 5,006
   MCP Server for Computer Use in Windows

117. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,004
   Install, run and deploy your own decentralized AI agent service

118. **[unidbg](https://github.com/zhkl0228/unidbg)** - ⭐ 4,882
   Allows you to emulate an Android native library, and an experimental  iOS emulation

119. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 4,817
   MCP server for Atlassian tools (Confluence, Jira)

120. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,750
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

121. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,732
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

122. **[code-review-graph](https://github.com/tirth8205/code-review-graph)** - ⭐ 4,669
   Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.

123. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,639
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

124. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,596
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

125. **[osaurus](https://github.com/osaurus-ai/osaurus)** - ⭐ 4,593
   Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source.

126. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,552
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

127. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,496
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

128. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 4,350
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

129. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,325
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

130. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 4,299
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

131. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,269
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

132. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 4,244
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

133. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 4,169
   Official Notion MCP Server

134. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 4,168
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

135. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 4,150
   Exa MCP for web search and web crawling!

136. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

137. **[byterover-cli](https://github.com/campfirein/byterover-cli)** - ⭐ 4,111
   ByteRover CLI (brv) - The portable memory layer for  autonomous coding agents (formerly Cipher)

138. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 4,102
   A simple, secure MCP-to-OpenAPI proxy server

139. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 4,091
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

140. **[bb-browser](https://github.com/epiral/bb-browser)** - ⭐ 4,090
   Your browser is the API. CLI + MCP server for AI agents to control Chrome with your login state.

141. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 4,066
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

142. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 4,050
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

143. **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** - ⭐ 3,981
   Universal SEO skill for Claude Code. 19 sub-skills, 12 subagents, 3 extensions (DataForSEO, Firecrawl, Banana). Technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, maps intelligence, Google APIs, and PDF/Excel reporting.

144. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,931
   An Agentic Framework for Reflective PowerPoint Generation

145. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,921
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

146. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,918
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 130+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

147. **[directories](https://github.com/leerob/directories)** - ⭐ 3,916
   Find rules and MCP servers

148. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

149. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,860
   A curated list of Model Context Protocol (MCP) servers

150. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,850
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

151. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 3,842
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks go from beginner to power user!

152. **[mission-control](https://github.com/builderz-labs/mission-control)** - ⭐ 3,790
   Self-hosted AI agent orchestration platform: dispatch tasks, run multi-agent workflows, monitor spend, and govern operations from one mission control dashboard.

153. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 3,781
   RikkaHub is an Android APP that supports for multiple LLM providers.

154. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 3,751
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

155. **[atmosphere](https://github.com/Atmosphere/atmosphere)** - ⭐ 3,749
   Real-time transport layer for Java AI agents. Build once with @Agent — deliver over WebSocket, SSE, gRPC, MCP, A2A, AG-UI, or any transport. Works with Spring AI, LangChain4j, Google ADK, Embabel, Koog or the built-in OpenAI-compatible client.

156. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,737
   Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP Support

157. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,729
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use. 

158. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,710
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

159. **[excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)** - ⭐ 3,707
   Fast and streamable Excalidraw MCP App

160. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,705
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

161. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,695
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

162. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,668
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

163. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,637
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

164. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,637
   A Model Context Protocol server for Excel file manipulation

165. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 3,633
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Antigravity, Copilot, VS Code)

166. **[core](https://github.com/opensumi/core)** - ⭐ 3,617
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

167. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,586

168. **[EverOS](https://github.com/EverMind-AI/EverOS)** - ⭐ 3,572
   A memory OS that makes your OpenClaw agents more personal while saving tokens.

169. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,548
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

170. **[EverMemOS](https://github.com/EverMind-AI/EverMemOS)** - ⭐ 3,546
   A memory OS that makes your OpenClaw agents more personal while saving tokens.

171. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,534
   Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator

172. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,523
   An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins.

173. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 3,510
   Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

174. **[mcp](https://github.com/google/mcp)** - ⭐ 3,495
   Google 💚 MCP

175. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,461
   LangChain 🔌 MCP

176. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

177. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,435
   Model Context Protocol(MCP) 编程极速入门

178. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 3,395
   A full-stack AI Red Teaming platform securing AI ecosystems via OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation.

179. **[boost](https://github.com/laravel/boost)** - ⭐ 3,383
   Laravel-focused MCP server for augmenting your AI powered local development experience.

180. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,333
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

181. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,312
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

182. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 3,310
   Chrome extension to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

183. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 3,274
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

184. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,259
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

185. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 3,254

186. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 3,252
   The official Rust SDK for the Model Context Protocol

187. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,243
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

188. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,224
   Allow LLMs to control a browser with Browserbase and Stagehand

189. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 3,208
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

190. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 3,201
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

191. **[SimpleMem](https://github.com/aiming-lab/SimpleMem)** - ⭐ 3,180
   SimpleMem: Efficient Lifelong Memory for LLM Agents — Text & Multimodal

192. **[claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** - ⭐ 3,114
   Semi-automated research assistant for academic research and software development. Supports Claude Code, OpenCode, and Codex CLI across ideation, coding, experiments, writing, and publication.

193. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 3,069
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

194. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 3,028
   A TypeScript framework for building MCP servers.

195. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 3,012
   AI agent microservice

196. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 3,005
   n8n custom node for MCP

197. **[Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)** - ⭐ 2,997
   Multi-modal Generative Media Skills for AI Agents (Claude Code, Cursor, Gemini CLI). High-quality image, video, and audio generation powered by muapi.ai.

198. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,911
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

199. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 2,873
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

200. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 2,856
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

201. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,767
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

202. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 2,754
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

203. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,746
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

204. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,716
   MCP server for Grafana

205. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,696
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

206. **[oh-my-pi](https://github.com/can1357/oh-my-pi)** - ⭐ 2,657
   ⌥  AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

207. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,581
   Connect Supabase to your AI assistants

208. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

209. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,555
   A CLI tool for building Go applications.

210. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,545
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

211. **[awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)** - ⭐ 2,544
   162 production-ready AI agent templates for OpenClaw. SOUL.md configs across 19 categories. Submit yours!

212. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,543
   A Model Context Protocol server for converting almost anything to Markdown

213. **[claude-context-mode](https://github.com/mksglu/claude-context-mode)** - ⭐ 2,522
   MCP is the protocol for tool access. We're the virtualization layer for context.

214. **[slackdump](https://github.com/rusq/slackdump)** - ⭐ 2,514
   Save or export your private and public Slack messages, threads, files, and users locally without admin privileges.

215. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,512
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

216. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,495
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

217. **[moltis](https://github.com/moltis-org/moltis)** - ⭐ 2,493
   A Rust-native claw you can trust. One binary — sandboxed, secure, auditable. Voice, memory, MCP tools, and multi-channel access built-in.

218. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 2,477
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

219. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,476
   A Model Context Protocol server for searching and analyzing arXiv papers

220. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,396
   A bridge between Streamable HTTP and stdio MCP transports

221. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,393
   A metasearch library that aggregates results from diverse web search services

222. **[drawio-mcp](https://github.com/jgraph/drawio-mcp)** - ⭐ 2,390

223. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,387
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

224. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,378

225. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 2,293
   Next Generation Agentic Proxy for AI Agents and MCP servers

226. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 2,288
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

227. **[code-graph-rag](https://github.com/vitali87/code-graph-rag)** - ⭐ 2,286
   The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

228. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,264
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

229. **[engram](https://github.com/Gentleman-Programming/engram)** - ⭐ 2,249
   Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

230. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,223
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.1, Claude, Grok, DeepSeek, OpenRouter, Kimi 2.5, GLM 5, SiliconFlow, GPT-oss, Gemma 4, Qwen 3.5

231. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,190
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

232. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,183
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

233. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,162
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

234. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 2,133
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

235. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 2,129
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

236. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

237. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 2,082
   This is the official website for TuriX Computer-use-Agent

238. **[fusio](https://github.com/apioo/fusio)** - ⭐ 2,081
   Self-Hosted API Management for Builders

239. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 2,077
   The official MCP server implementation for the Perplexity API Platform

240. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,075
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

241. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,073
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

242. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 2,059
   ⭐ All-in-one AI companion! Super Agent Party = Self hosted neuro sama + openclaw! ⭐ 全能AI伴侣！超级智能体派对 = 自托管neuro sama + openclaw!

243. **[agent-scan](https://github.com/snyk/agent-scan)** - ⭐ 2,056
   Security scanner for AI agents, MCP servers and agent skills.

244. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,053
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

245. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 2,035
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

246. **[ouroboros](https://github.com/Q00/ouroboros)** - ⭐ 2,033
   Stop prompting. Start specifying.

247. **[openpencil](https://github.com/ZSeven-W/openpencil)** - ⭐ 2,028
   The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

248. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 2,026
   The Unofficial and Awesome Home Assistant MCP Server

249. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 2,024
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

250. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 2,009
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

251. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,999
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

252. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,989
   directory for Awesome MCP Servers

253. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 1,988
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

254. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,974
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

255. **[skills](https://github.com/microsoft/skills)** - ⭐ 1,953
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

256. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,940
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

257. **[beelzebub](https://github.com/beelzebub-labs/beelzebub)** - ⭐ 1,939
   A secure low code honeypot framework, leveraging AI for System Virtualization.

258. **[mcp-cli](https://github.com/IBM/mcp-cli)** - ⭐ 1,936

259. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 1,934
   AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free.

260. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,925
   Witsy: desktop AI assistant / universal MCP client

261. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,925
   A Unified MCP Server Management App (MCP Manager).

262. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,904
   A secure low code honeypot framework, leveraging AI for System Virtualization.

263. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,896
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

264. **[agent-deck](https://github.com/asheshgoplani/agent-deck)** - ⭐ 1,895
   Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more.

265. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,891

266. **[esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** - ⭐ 1,881
   An AI-enabled NAT Router/Firewall for the ESP32

267. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,867
   Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite

268. **[mcp2cli](https://github.com/knowsuchagency/mcp2cli)** - ⭐ 1,867
   Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen

269. **[vexa](https://github.com/Vexa-ai/vexa)** - ⭐ 1,847
   Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.

270. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 1,845
   340 plugins + 1367 agent skills for Claude Code. Open-source marketplace with CCPI package manager, interactive tutorials, and production orchestration patterns.

271. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,836
   Test, Evaluate, and Ship MCP servers, ChatGPT apps, and MCP Apps (ext-apps)

272. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,823
   Desktop Extensions: One-click local MCP server installation in desktop apps

273. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,822
   MCP server for interacting with the iOS simulator

274. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

275. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,790
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

276. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,790
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

277. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 1,776
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

278. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,767
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

279. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,761
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

280. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,758
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

281. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 1,743
   An MCP server for interacting with the Financial Datasets stock market API.

282. **[claude-peers-mcp](https://github.com/louislva/claude-peers-mcp)** - ⭐ 1,735
   Allow all your Claude Codes to message each other ad-hoc!

283. **[plik](https://github.com/root-gg/plik)** - ⭐ 1,734
   Plik is a temporary file upload system (Wetransfer like) in Go.

284. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,726

285. **[contextplus](https://github.com/ForLoopCodes/contextplus)** - ⭐ 1,721
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

286. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,720
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

287. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,714
   Interactive User Feedback MCP

288. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,705
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

289. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,697
   ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP) servers.

290. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,677
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

291. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,674
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

292. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,667
   Make RSS 📰 great again with AI 🧠✨!! 【29元500次sonnet，下方wx扫码联系】

293. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,658
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

294. **[FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline)** - ⭐ 1,653
   FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestration. It facilitates transparent, human-in-the-loop creation with reusable Style Skills for consistent, professional storytelling.

295. **[onecli](https://github.com/onecli/onecli)** - ⭐ 1,646
   Open-source credential vault, give your AI agents access to services without exposing keys.

296. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,641
   Plugin for JADX to integrate MCP server

297. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,638
   Production ready MCP server with real-time search, extract, map & crawl.

298. **[nono](https://github.com/always-further/nono)** - ⭐ 1,633
   Kernel-enforced agent sandbox. Capability-based isolation with secure key management, atomic rollback, cryptographic immutable audit chain of provenance. Run your agents in a zero-trust environment.

299. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 1,625
   MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

300. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,615
   Coding assistant MCP for Claude Desktop

301. **[pilot-shell](https://github.com/maxritter/pilot-shell)** - ⭐ 1,609
   The professional development environment for Claude Code

302. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,605
   Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

303. **[dembrandt](https://github.com/dembrandt/dembrandt)** - ⭐ 1,604
   Extract any website’s design system into tokens in seconds: logo, colors, typography, borders & more. One command.

304. **[ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** - ⭐ 1,599
   Learn it. Build it. Ship it for others.

305. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,592
   MCP server that provides tools and resources for interacting with n8n API

306. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,592
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

307. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

308. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,562
   Semantic Search & Call Graphs for AI Agents (100% Local)

309. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,556
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

310. **[goclaw](https://github.com/nextlevelbuilder/goclaw)** - ⭐ 1,555
   GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. Deploy AI agent teams at scale without compromising on safety.

311. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,543
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

312. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 1,533
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

313. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,522
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

314. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,519
   Official Microsoft Learn MCP Server and CLI tool – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

315. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,518
   An MCP server that installs other MCP servers for you

316. **[NagaAgent](https://github.com/RTGS2017/NagaAgent)** - ⭐ 1,509
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

317. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,508
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

318. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,506
   Standards for building agents, better

319. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,505
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

320. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

321. **[rocketride-server](https://github.com/rocketride-org/rocketride-server)** - ⭐ 1,491
   High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM workflows with 13+ model providers, 8+ vector databases, and agent orchestration, all from your IDE. Includes VS Code extension, TypeScript/Python SDKs, and Docker deployment.

322. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,484
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

323. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,473
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

324. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,467
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

325. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,458
   Security scanner for AI agents, MCP servers and agent skills.

326. **[jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp)** - ⭐ 1,447
   The leading, most token-efficient MCP server for GitHub source code exploration via tree-sitter AST parsing

327. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,438
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

328. **[fli](https://github.com/punitarani/fli)** - ⭐ 1,437
   Google Flights MCP and Python Library

329. **[ai](https://github.com/stripe/ai)** - ⭐ 1,434
   One-stop shop for building AI-powered products and businesses with Stripe.

330. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,433
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

331. **[tavily-key-generator](https://github.com/skernelx/tavily-key-generator)** - ⭐ 1,429
   Multi-service toolkit for Tavily and Firecrawl signup automation, key validation, and isolated proxy pools.

332. **[hotpath-rs](https://github.com/pawurb/hotpath-rs)** - ⭐ 1,421
   Rust Performance Profiler & Channels Monitoring Toolkit (TUI, MCP)

333. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 1,418
   Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

334. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,416
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

335. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 1,389
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

336. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,387
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

337. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,386
   Make your own story. User-friendly software for LLM roleplaying

338. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,382
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

339. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,373
   A connector for Claude Desktop to read and search an Obsidian vault.

340. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,371
   MCP Server for kubernetes management commands

341. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,355

342. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,353
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

343. **[data-api-builder](https://github.com/Azure/data-api-builder)** - ⭐ 1,349
   Data API builder provides modern REST, GraphQL endpoints and MCP tools to your Azure Databases and on-prem stores.

344. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,338
   docker mcp CLI plugin / MCP Gateway

345. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,337
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

346. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,333
   The official Swift SDK for Model Context Protocol servers and clients.

347. **[ShipSwift](https://github.com/signerlabs/ShipSwift)** - ⭐ 1,329
   AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

348. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,321
   An official Qdrant Model Context Protocol (MCP) server implementation

349. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,320
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

350. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,319
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

351. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,310
   First gitlab mcp for you

352. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,308
   告别AI提前终止烦恼，助力AI更加持久

353. **[ghost-os](https://github.com/ghostwright/ghost-os)** - ⭐ 1,304
   Full computer-use for AI agents. Self-learning workflows. Native macOS. No screenshots required.

354. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,302
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

355. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,294
   The official ElevenLabs MCP server

356. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 1,286
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

357. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,278
   Damn Vulnerable MCP Server

358. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,274
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

359. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 1,269
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and manage your inbox.

360. **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** - ⭐ 1,261
   Humans and AI agents, building knowledge bases together. Self-hosted document annotation, version control, semantic search, and MCP.

361. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 1,253
   Build MCP Agents

362. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,248
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

363. **[GrokSearch](https://github.com/GuDaStudio/GrokSearch)** - ⭐ 1,242
   Integrate Grok's powerful real-time search capabilities into Claude via the MCP protocol!

364. **[cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)** - ⭐ 1,239
   A super light-weight embedded code search engine CLI (AST based) that just works - saves 70% token and improves speed for coding agent  🌟 Star if you like it!

365. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,236
   An MCP server that autonomously evaluates web applications. 

366. **[relaticle](https://github.com/relaticle/relaticle)** - ⭐ 1,228
   Open-source CRM with native AI agent support. 30 MCP tools, REST API, self-hosted. Built with Laravel & Filament

367. **[mcp-brasil](https://github.com/jxnxts/mcp-brasil)** - ⭐ 1,227
   MCP Server para 41 APIs públicas brasileiras

368. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

369. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,225
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

370. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,225
   The TypeScript MCP framework

371. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,224
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

372. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 1,223
   Claude Code as one-shot MCP server to have an agent in your agent.

373. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,222
   The Grafbase GraphQL Federation Gateway

374. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

375. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,213
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

376. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,210
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

377. **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** - ⭐ 1,207
   High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 66 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies.

378. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

379. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 1,201
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

380. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,200
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

381. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,199
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

382. **[OB1](https://github.com/NateBJones-Projects/OB1)** - ⭐ 1,198
   Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plugs in. No middleware, no SaaS.

383. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,195
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

384. **[phantom](https://github.com/ghostwright/phantom)** - ⭐ 1,189
   An AI co-worker with its own computer. Self-evolving, persistent memory, MCP server, secure credential collection, email identity. Built on the Claude Agent SDK.

385. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 1,188
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

386. **[xiaoyaosearch](https://github.com/dtsola/xiaoyaosearch)** - ⭐ 1,181
   小遥搜索，听懂你的话、看懂你的图，用AI找到本地任何文件。让搜索像聊天一样简单。XiaoyaoSearch: Understands your words, reads your images, finds any local file with AI. Making search as easy as chatting.

387. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 1,178
   Model Context Protocol for WinDBG

388. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,174
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

389. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 1,160
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

390. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,159
   A Ruby Implementation of the Model Context Protocol

391. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,151
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

392. **[headroom](https://github.com/chopratejas/headroom)** - ⭐ 1,151
   The Context Optimization Layer for LLM Applications

393. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

394. **[724-office](https://github.com/wangziqi06/724-office)** - ⭐ 1,147
   7/24 Office — Self-evolving AI Agent system. 26 tools, 3500 lines pure Python, MCP/Skill plugins, three-layer memory, self-repair, 24/7 production.

395. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,144
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

396. **[sceneview](https://github.com/sceneview/sceneview)** - ⭐ 1,144
   3D & AR SDK for Android, iOS, Web, Desktop, TV, Flutter, React Native — Jetpack Compose, SwiftUI, Filament, RealityKit, WebXR

397. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 1,141
   Connect AI models like Claude & GPT with robots using MCP and ROS.

398. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,137
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

399. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,135
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

400. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,128
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

401. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 1,121
   Draw.io Model Context Protocol (MCP) Server

402. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,111
   Game Boy / Game Boy Color / Super Game Boy emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

403. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 1,108
   Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

404. **[korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)** - ⭐ 1,103
   89 tools for Korean law — statutes, precedents, ordinances, interpretations | MCP Server · CLI · npm

405. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,086
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

406. **[amical](https://github.com/amicalhq/amical)** - ⭐ 1,081
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

407. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 1,078
   Lighweight CLI to interact with MCP servers

408. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 1,076
   MCP integration for Google Calendar to manage events.

409. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,063
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

410. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 1,063
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+400,000 via SkillKit), 42 commands, 150+ plugins, 19 hooks, 15 rules, 7 templates, 8 MCP configs, and more.

411. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 1,062
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

412. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 1,058
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

413. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 1,055
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

414. **[blitz-mac](https://github.com/blitzdotdev/blitz-mac)** - ⭐ 1,055
   Native macOS App Store Connect tool with MCP. Submit iOS apps to App Store with AI agents 

415. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 1,054
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

416. **[agents](https://github.com/inkeep/agents)** - ⭐ 1,053
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

417. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 1,052
   A repository of servers and clients from the Model Context Protocol tutorials

418. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 1,048
   Bringing the power of MCP to the web

419. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,047
   MCP Python Tutorial 

420. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,040
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

421. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,040
   On-premises conversational RAG with configurable containers

422. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,038
   A curated list of Model Context Protocol (MCP) servers 

423. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 1,037
   Remote MCP Servers

424. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,035
   Query and Summarize your chat messages.

425. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 1,032
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

426. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

427. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 1,025
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

428. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 1,022
   MCP server for fetch web page content using Playwright headless browser.

429. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 1,018
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

430. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,017
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

431. **[tools](https://github.com/strands-agents/tools)** - ⭐ 1,003
   A set of tools that gives agents powerful capabilities.

432. **[mcpvault](https://github.com/bitbonsai/mcpvault)** - ⭐ 1,002
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

433. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 989
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

434. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 987
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

435. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 985
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

436. **[muapi-cli](https://github.com/SamurAIGPT/muapi-cli)** - ⭐ 975
   Official CLI for muapi.ai — generate images, videos & audio from the terminal. MCP server, 14 AI models, npm + pip installable.

437. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 970
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

438. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 970
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

439. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 970
   A guide on how to use the Figma MCP server

440. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 968
   Expose llms-txt to IDEs for development

441. **[reactuse](https://github.com/childrentime/reactuse)** - ⭐ 966
   115+ production-ready React Hooks for sensors, UI, state & browser APIs. Tree-shakable, SSR-safe, TypeScript-first. Used by Shopee, PDD & Ctrip. Inspired by VueUse.

442. **[tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** - ⭐ 966
   AI-assisted TradingView chart analysis — connect Claude Code to your TradingView Desktop for personal workflow automation

443. **[keeper.sh](https://github.com/ridafkih/keeper.sh)** - ⭐ 962
   Open-source calendar sync tool & universal calendar MCP server. Aggregate, sync and control calendars on Google, Outlook, Office 365, iCloud, CalDAV or ICS.

444. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 958
   MCP, CLI, Skills for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

445. **[devops-ai-guidelines](https://github.com/VersusControl/devops-ai-guidelines)** - ⭐ 957
   First AI Journey for DevOps - with comprehensive learning paths, practical tips, and enterprise guidelines

446. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 956
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

447. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 949
   Self-hosted MCP Gateway for AI agents

448. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 945
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

449. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 945
   A lightweight, cross-platform database client for developers. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

450. **[Horizon](https://github.com/Thysrael/Horizon)** - ⭐ 945
   Automated AI news aggregator & summarizer. Generates daily briefings in English & Chinese. | 全自动 AI 科技新闻聚合与摘要生成器。

451. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 942
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

452. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 941
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

453. **[ai-engineering-interview-questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)** - ⭐ 941
   Your Cheat Sheet for AI Engineering Interview – Questions and Answers.

454. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 940
   A security scanner for your LLM agentic workflows

455. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 935
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

456. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 933
   Delegate tasks to Codex and Gemini directly from within Claude Code.

457. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 931
   Neo4j Labs Model Context Protocol servers

458. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 923
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

459. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 920
   A middleware to provide an openAI compatible endpoint that can call MCP tools

460. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 918

461. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 918
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

462. **[cs](https://github.com/boyter/cs)** - ⭐ 914
   codespelunker - CLI code search tool that understands code structure and ranks results by relevance. No indexing required with CLI, TUI, MCP and HTTP support.

463. **[nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** - ⭐ 913
   A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents. Say goodbye to Vector RAG and amnesia. Empower your AI with persistent, graph-like structured memory across any model, session, or tool. Drop-in replacement for OpenClaw.

464. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 911
   The Typescript MCP Framework

465. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

466. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 909
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

467. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 908
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

468. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 906
   OpenAPI Tool Servers

469. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 905
   MCP server helping models to understand your Vite/Nuxt app better.

470. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 899
   Skybridge is a framework for building ChatGPT & MCP Apps

471. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 897
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

472. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 897
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

473. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 890
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

474. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 889
   Allow AI to wade through complex OpenAPIs using Simple Language

475. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 888
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

476. **[shellfirm](https://github.com/kaplanelad/shellfirm)** - ⭐ 887
   Safety guardrails for ai coding agents and human terminal commands

477. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 884
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility. Since 2018.

478. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 884
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

479. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 883

480. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 881
   A concise list for mcp servers

481. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 880
   A library for communication with a Minecraft client/server.

482. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 879
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

483. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 877
   Skill and MCP server for searching and retrieving icons

484. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

485. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 875

486. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 872
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

487. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 871
   Scan MCP servers for potential threats & security findings.

488. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 871
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

489. **[minutes](https://github.com/silverstein/minutes)** - ⭐ 871
   Every meeting, every idea, every voice note — searchable by your AI. Open-source, privacy-first conversation memory layer.

490. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 869

491. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 868

492. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 864
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

493. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 861
   Database APIs for AI agents

494. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 859
   A Model Context Protocol (MCP) server for Kubernetes. Install: npx kubectl-mcp-server or pip install kubectl-mcp-server

495. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 857
   A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations.

496. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 845
   The best way to create, deploy, and share MCP Servers

497. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 838
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

498. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

499. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

500. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 831
   A minimalistic MCP client with a good feature set.

501. **[server](https://github.com/php-mcp/server)** - ⭐ 828
   Core PHP implementation for the Model Context Protocol (MCP) server

502. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 827
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

503. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 826
   Simple, modular, and observable Go framework for backend applications.

504. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 825
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

505. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 821
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

506. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 817
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

507. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 816
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

508. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 815
   Browse the web, directly from Cursor etc.

509. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 813
   A local sandbox for your AI agents

510. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 812
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

511. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 811
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

512. **[context-space](https://github.com/context-space/context-space)** - ⭐ 810
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

513. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

514. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 805
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

515. **[sentrux](https://github.com/sentrux/sentrux)** - ⭐ 802
   Real-time architectural sensor that helps AI agents close the feedback loop, enabling recursive self-improvement of code quality. Pure Rust.

516. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 800
   一个将ACE(Augment Context Engine) 做成MCP的项目

517. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 800
   A self-hosted RSS reader and personal knowledge management tool.

518. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 798
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

519. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 791
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

520. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 790
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

521. **[vllora](https://github.com/vllora/vllora)** - ⭐ 788
   Debug your AI agents

522. **[Context](https://github.com/indragiek/Context)** - ⭐ 786
   Native macOS client for Model Context Protocol (MCP)

523. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 784
   Vibetest MCP - automated QA testing using Browser-Use agents

524. **[secpipe](https://github.com/FuzzingLabs/secpipe)** - ⭐ 783
   MCP server for AI-driven security pipelines

525. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 775
   🤖 Automatically collected AI repos, tools, websites, papers & tutorials. 实用AI百宝箱 💎

526. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 773
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

527. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 770
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

528. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 768
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

529. **[runno](https://github.com/taybenlor/runno)** - ⭐ 764
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

530. **[nekro-agent](https://github.com/KroMiose/nekro-agent)** - ⭐ 764
   NekroAgent 是一个面向多人互动场景的跨平台 Agent 框架，集 Claude Code 沙盒执行、工作区编排、长期记忆、结构化 MCP 管理与可视化控制台于一体，兼具高扩展性、多模态交互、实时状态推送和自动化运行能力。项目支持 QQ、Discord、Telegram、Minecraft、BilibiliLive、WeChat、Email、SSE(SDK) 等多种平台接入，应用于构建高智能聊天机器人，可扩展为具备代码执行、工具调用、插件协作和复杂任务处理能力的通用 Agent 系统

531. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 762
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

532. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 761
   The official Ruby SDK for the Model Context Protocol.

533. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 760
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

534. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 755
   A MCP server implementation for hyperbrowser

535. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 754
   MCP server integration for DaVinci Resolve

536. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 754
   OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s. Works with Claude Code.

537. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 750
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

538. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 746
   MCP Server For Turkish Legal Databases

539. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 745
   Connect ClickHouse to your AI assistants.

540. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 745
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

541. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 743
   LLDB MCP Integration + other helpful commands

542. **[opennews-mcp](https://github.com/6551Team/opennews-mcp)** - ⭐ 738
   Crypto News Aggregation · AI Ratings · Trading Signals · Real-time Updates

543. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 737
   A flexible HTTP fetching Model Context Protocol server.

544. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 737
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

545. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 736
   All in one vscode plugin for mcp developer

546. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 736
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

547. **[SocratiCode](https://github.com/giancarloerra/SocratiCode)** - ⭐ 735
   Enterprise-grade (40m+ lines) codebase intelligence in a zero-setup, private and local Claude Plugin or MCP: managed indexing, hybrid semantic search, polyglot code dependency graphs, and DB/API/infra knowledge. Benchmark: 61% less tokens, 84% fewer calls, 37x faster than standard AI grep.

548. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 730
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

549. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 729
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

550. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 725
   gcloud MCP server

551. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 723
   Clojure MCP

552. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 720
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

553. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 719
   An MCP server that provides control over Android devices via adb

554. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 719
   A simple, locally hosted Web Search MCP server for use with Local LLMs

555. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 718
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

556. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 717
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

557. **[mcp](https://github.com/laravel/mcp)** - ⭐ 717
   Rapidly build MCP servers for your Laravel applications.

558. **[stitch-mcp](https://github.com/davideast/stitch-mcp)** - ⭐ 716
   A CLI for moving AI-generated UI designs from Google’s Stitch platform into your development workflow.

559. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 713
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

560. **[samples](https://github.com/strands-agents/samples)** - ⭐ 710
   Agent samples built using the Strands Agents SDK.

561. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 709
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

562. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 708
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

563. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 708
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

564. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 706
   Next.js Development for Coding Agent

565. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 705
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

566. **[MODULAR-RAG-MCP-SERVER](https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER)** - ⭐ 704
   A modular RAG (Retrieval-Augmented Generation) system with MCP Server architecture. Using Skill to make AI follow each step of the spec and complete the code 100% by AI.

567. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 697
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

568. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 696
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

569. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 695
   MCP server for Docker

570. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 693
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

571. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 693
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

572. **[Wax](https://github.com/christopherkarani/Wax)** - ⭐ 690
   Single-file memory layer for AI agents, sub mili-second RAG on Apple Silicon. Metal Optimized On-Device. No Server. No API. One File. Pure Swift

573. **[obot](https://github.com/obot-platform/obot)** - ⭐ 690
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

574. **[aso-skills](https://github.com/Eronred/aso-skills)** - ⭐ 689
   AI agent skills for App Store Optimization (ASO) and app marketing. Built for indie developers, app marketers, and growth teams who want Cursor, Claude Code, or any Agent Skills-compatible AI assistant to help with keyword research, metadata optimization, competitor analysis, and app growth.

575. **[gemini-skill](https://github.com/WJZ-P/gemini-skill)** - ⭐ 684
   gemini drawing MCP & skill through browser, can be used in openclaw or any agent that supports MCP. Gemini画图 MCP和sill，支持龙虾或任何agent使用٩(๑>◡<๑)۶

576. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 681
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

577. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 677
   FreeCAD MCP(Model Context Protocol) server

578. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 677
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

579. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 676
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

580. **[room](https://github.com/quoroom-ai/room)** - ⭐ 675
   Open-source earning-focused swarm intelligence engine. Self-governing AI collectives (queen, workers, quorum voting) running locally via MCP. Works with Claude Code, Codex, or pay-per-use APIs.

581. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 674
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

582. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 672
   A simple MCP server for Obsidian

583. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 672
   A simple CLI to run LLM prompt and implement MCP client.

584. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 669
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

585. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 668
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

586. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 666
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

587. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 663
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

588. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 656
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

589. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

590. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 655
   Shell and coding agent on mcp clients

591. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 652
   Laravel API for Ai Agents and humans.

592. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 650
   Querying local documents, powered by LLM

593. **[clihub](https://github.com/thellimist/clihub)** - ⭐ 650
   Turn any MCP server into CLI

594. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 650
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

595. **[work-iq](https://github.com/microsoft/work-iq)** - ⭐ 647
   MCP Server and CLI for accessing Work IQ

596. **[js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp)** - ⭐ 646
   为 AI Agent 设计的 JS 逆向 MCP Server，内置反检测，基于 chrome-devtools-mcp 重构 | JS reverse engineering MCP server with agent-first tool design and built-in anti-detection. Rebuilt from chrome-devtools-mcp.

597. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 644
   EnrichMCP is a python framework for building data driven MCP servers

598. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

599. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 640
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

600. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 640
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

601. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 639

602. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 639
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

603. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 637

604. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 636
   "AnyTool: Universal Tool-Use Layer for AI Agents"

605. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 634
   飞书/Lark官方 OpenAPI MCP

606. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 634
   Install, manage and develop MCP servers and skills for agents

607. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 633
   Talk to a Cloudflare Worker from Claude Desktop!

608. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 633
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

609. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 633
   A local Apple Documentation crawler and MCP server. Written in Swift.

610. **[axon](https://github.com/harshkedia177/axon)** - ⭐ 633
   Graph-powered code intelligence engine — indexes codebases into a knowledge graph, exposed via MCP tools for AI agents and a CLI for developers.

611. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 631
   The open context engine for AI agents support 15+ data sources. Built on Rust and Apache DataFusion.

612. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 631
   MCP Server for Burp

613. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 629
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

614. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 624
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

615. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

616. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

617. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 623
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

618. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 621
   mem-agent mcp server

619. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 621
   An MCP server for interacting with Sentry via LLMs.

620. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 619
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

621. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 619
   Python Deep Agent framework built on top of Pydantic-AI, designed to help you quickly build production-grade autonomous AI agents with planning, filesystem operations, subagent delegation, skills, and structured outputs—in just 10 lines of code.

622. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 617
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

623. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 614
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

624. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 613
   Google Search Console Insights with Claude AI for SEOs

625. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 611
   MCP configuration to connect AI agent to a Linux machine.

626. **[tome](https://github.com/runebookai/tome)** - ⭐ 610
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

627. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 608
   Official Jina AI Remote MCP Server

628. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 608
   A coding agent and general agent harness for building and orchestrating agentic applications.

629. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 608
   MCP Server for SearXNG

630. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 606
   Convert Any OpenAPI V3 API to MCP Server

631. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 606
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

632. **[Overture](https://github.com/SixHq/Overture)** - ⭐ 605
   Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. 

633. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 605
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

634. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 604
   Daydreams is a set of tools for building agents for commerce

635. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 603
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

636. **[agent-kit](https://github.com/KeyID-AI/agent-kit)** - ⭐ 603
   Give Claude/Cursor email powers. 27 MCP tools — inbox, send, reply, contacts, search. Free, no signup.

637. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 600
   A comprehensive collection of Model Context Protocol (MCP) servers

638. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 598
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

639. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 597
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

640. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 595
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

641. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 594
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

642. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 593
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

643. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 593
   MCP to connect your LLM with Spotify.

644. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 590
   The .NET library to build AI agents with 30+ built-in connectors.

645. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 589
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

646. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 589
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

647. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 589
   GitOps on Autopilot Mode

648. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 588
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

649. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 586
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

650. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 584
   MCP server to deploy apps to Cloud Run

651. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 582
    Feishu / Lark 飞书文档与任务管理工具，支持 MCP 服务器和 CLI + Skill 两种使用方式，可无缝集成 Cursor、Claude Code、Cline 等 AI 编码工具

652. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 582
   It's a plugin extension in Zotero.  Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。

653. **[codeg](https://github.com/xintaofei/codeg)** - ⭐ 582
   A unified workspace for local AI coding agents (Claude Code, Codex, Gemini CLI, etc.) — desktop app, standalone server, or Docker. Conversation aggregation, git worktree workflows, MCP/Skills management, chat channel integration (Telegram, Lark, iLink), and integrated terminal, all accessible from any browser.

654. **[azure-skills](https://github.com/microsoft/azure-skills)** - ⭐ 581
   Official agent plugin providing skills and MCP server configurations for Azure scenarios.

655. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 578
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

656. **[kordoc](https://github.com/chrisryugj/kordoc)** - ⭐ 578
   모두 파싱해버리겠다 — HWP, HWPX, PDF, XLSX, DOCX → Markdown. CLI + MCP Server

657. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 577
   LangGraph solution template for MCP

658. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 577
   MCP-Universe is a comprehensive framework designed for RL training, benchmarking, and developing AI agents for general tool-use.

659. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 575

660. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 574
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

661. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 574
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

662. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 573
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

663. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 572
   MCP server for interacting with Neon Management API and databases

664. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 572
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

665. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 571
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

666. **[ai-setup](https://github.com/caliber-ai-org/ai-setup)** - ⭐ 571
   Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.

667. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 570
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

668. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 569
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

669. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 563
   MCP Server for Metasploit

670. **[ScienceClaw](https://github.com/beita6969/ScienceClaw)** - ⭐ 563
   🔬🦞 A self-evolving AI research colleague for scientists. 285 skills, zero hallucination, persistent memory.

671. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 562
   A MCP server for Home Assistant

672. **[GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)** - ⭐ 562
   An MCP extension for Ghidra

673. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 561
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

674. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 559
   A model-driven approach to building AI agents in just a few lines of code. 

675. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 559
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (Claude Code, Cursor, Antigravity, etc.) to read, analyze, and modify Figma designs

676. **[MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)** - ⭐ 558
   MeiGen-AI-Design-MCP — Turn Claude Code / OpenClaw into your local Lovart. Local ComfyUI, 1,400+ prompt library, multi-direction parallel generation.

677. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 557
   MCP to allow AI agents to control Unreal

678. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 556
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

679. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

680. **[casbin-gateway](https://github.com/casbin/casbin-gateway)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

681. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 555
   An Mcp client inside Emacs

682. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 555
   Open Source Voice Agent Platform

683. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 554
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

684. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 554
   A tool that converts OpenAPI specifications to MCP server

685. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 552
   An MCP Multimodal AI Agent with eyes and ears!

686. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 552
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

687. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 552
   Making docling agentic through MCP

688. **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** - ⭐ 552
   🦸 AI 编程超能力 · 中文增强版 — superpowers（99k+ ⭐）完整汉化 + 6 个中国原创 skills，让 OpenClaw / Claude Code / Cursor / Windsurf / Kiro / Gemini CLI 等 14 款 AI 编程工具真正会干活

689. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 551
   Security scanner for MCP servers

690. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 550
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

691. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 543
   A structural code search engine for Al agents.

692. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 543
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

693. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 543

694. **[tda](https://github.com/irockel/tda)** - ⭐ 540
   TDA - Thread Dump Analyzer (for Java). Analyze your Thread Dumps with a GUI or use it as MCP Server.

695. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 540
   MCP Server for Turkish & American Stock Exchange and Fund Data

696. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 539
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

697. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 538
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

698. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 537

699. **[codexia](https://github.com/milisp/codexia)** - ⭐ 537
   Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, skills management

700. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 536
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

701. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 536
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

702. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 536
   MCP-NixOS - Model Context Protocol Server for NixOS resources

703. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 534
   MCP Server and CLI for accessing Work IQ

704. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 534
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

705. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 533

706. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 532
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

707. **[idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)** - ⭐ 532
   Pre-build reality check for AI coding agents. Scans GitHub, HN, npm, PyPI, Product Hunt. MCP server. 290+ stars.

708. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 531
   A Model Context Protocol server for IDA

709. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 531
   微信读书MCP

710. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 529
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

711. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 529

712. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 529
   A MCP (Model Context Protocol) server for interacting with dbt.

713. **[ethora](https://github.com/dappros/ethora)** - ⭐ 527
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

714. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 527
   AI-based stock analysis and trading system

715. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 527
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

716. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 527
   An MCP server to query any Postgres database in natural language.

717. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 525
   MCP server for querying Apple Health data with natural language and SQL

718. **[probe](https://github.com/probelabs/probe)** - ⭐ 525
   AI-friendly semantic code search engine for large codebases. Combines ripgrep speed with tree-sitter AST parsing. Powers AI coding assistants with precise, context-aware code understanding.

719. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 522
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

720. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 522
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

721. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 520
   MCP server for document format conversion using pandoc.

722. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 520
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

723. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 519
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

724. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 519
   LLM + MCP + RAG = Magic

725. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 517

726. **[claude_agent_teams_ui](https://github.com/777genius/claude_agent_teams_ui)** - ⭐ 517
   You're the CTO, agents are your team. They handle tasks themselves, message each other, review each other's code. You just look at the kanban board and drink coffee.

727. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

728. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 514
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single) 

729. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 514
   Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT, Deepseek, Claude Sonnet/Opus APIs, Google Gemini 3, Alibaba Qwen, Kimi, and Grok 4.1, with plans to add TTS, Elevenlabs, Inworld, OpenRouter, Groq, GLM, seedream hunyuan3d, fal, Dashscope, Rodin, Meshy, Tripo, UnrealClaude soon. UnrealMCP is also here!!

730. **[desktop](https://github.com/openyak/desktop)** - ⭐ 513
   Yak is all you need

731. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 512
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

732. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 510
   An MCP extension for Ghidra

733. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 510
   A Model-Context Protocol Server for YouTube

734. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 510
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

735. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 509
   MCP Server for interacting with Android Devices.

736. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 508
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

737. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

738. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 507

739. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 507
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

740. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 506
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

741. **[MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio)** - ⭐ 506
   MimikaStudio - A local-first application for macOS (Apple Silicon) + Agentic MCP Support

742. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 505
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

743. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 504
   MCP Monitoring with eBPF

744. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 504
   Yes Mcp server in bash

745. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 503
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

746. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 496
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

747. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

748. **[argo](https://github.com/xark-argo/argo)** - ⭐ 493
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

749. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

750. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 490
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

751. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 487
   Govern & Secure your AI

752. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 487
   🚀 Universal SDK for building next-gen MCP servers

753. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 486
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

754. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 485
   MCP Server to interact with Google Gsuite prodcuts

755. **[resend-mcp](https://github.com/resend/resend-mcp)** - ⭐ 485
   The official MCP server to send emails and interact with Resend

756. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 484
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

757. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 482
   A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI.

758. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 480
   BioMCP: Biomedical Model Context Protocol

759. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 480
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

760. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 479
   Make your meetings accessible to AI Agents

761. **[rails_ai_agents](https://github.com/ThibautBaissac/rails_ai_agents)** - ⭐ 478
   Specialized AI skills, agents, rules and hooks for modern Rails AI driven-development + Spec-Driven-Development kit + MCP

762. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 477
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

763. **[director](https://github.com/director-run/director)** - ⭐ 476
   MCP Playbooks for AI agents

764. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 475
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

765. **[PrismerCloud](https://github.com/Prismer-AI/PrismerCloud)** - ⭐ 474
   Prismer Cloud

766. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 473
   Connect Cursor, Copilot & Claude AI directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

767. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 473
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

768. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 472
   An SDK building Laravel MCP servers

769. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 472
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

770. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 471
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

771. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 470
   Aser is a lightweight, self-assembling AI Agent frame.

772. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 470
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

773. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 470
   MaverickMCP - Personal Stock Analysis MCP Server

774. **[awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents)** - ⭐ 470
   ✨ A curated list of awesome GitHub instructions, prompt, skills, MCPs and agent markdown files for enhancing your GitHub Copilot AI experience.

775. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 469
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

776. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 468
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript and C++.

777. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 467
   小红书MCP服务 x-s x-t js逆向

778. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 466
   A docker MCP Server (modelcontextprotocol)

779. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 465
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

780. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 465
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

781. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 465
   Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

782. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 462
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

783. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 461
   Official Docker MCP registry 

784. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 458
   Local MCP server for DuckDB and MotherDuck

785. **[lean-ctx](https://github.com/yvgude/lean-ctx)** - ⭐ 458
   Hybrid Context Optimizer — Shell Hook + MCP Server. Reduces LLM token consumption by 89-99%. Single Rust binary, zero dependencies.

786. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 457

787. **[cordum](https://github.com/cordum-io/cordum)** - ⭐ 457
   The open agent control plane. Govern autonomous AI agents with pre-execution policy enforcement, approval gates, and audit trails. Works with LangChain, CrewAI, MCP, and any framework.

788. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 456
   SonarQube MCP Server

789. **[docfork](https://github.com/docfork/docfork)** - ⭐ 455
   Docfork - Up-to-date Docs for AI Agents.

790. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 454
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

791. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 451
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

792. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 447
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

793. **[roam-code](https://github.com/Cranot/roam-code)** - ⭐ 447
   Architectural intelligence layer for AI coding agents. Structural graph, architecture governance, multi-agent orchestration, vulnerability mapping. 139 commands, 101 MCP tools, 26 languages, 100% local.

794. **[opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp)** - ⭐ 447
   Twitter/X Data · User Profiles · Tweet Search · Follower Events · KOL Tracking

795. **[colab-mcp](https://github.com/googlecolab/colab-mcp)** - ⭐ 447
   An MCP server for interacting with Google Colab

796. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

797. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

798. **[tradememory-protocol](https://github.com/mnemox-ai/tradememory-protocol)** - ⭐ 445
   Decision audit trail + persistent memory for AI trading agents. Outcome-weighted recall, SHA-256 tamper detection, 17 MCP tools.

799. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

800. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 444
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

801. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 444
   MCP server that execute applescript giving you full control of your Mac

802. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 442
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

803. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 441
   基于NET搭建-AI知识库智能体-现代化Saas企业级前后端分离架构：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR识别、API多版本、单元测试、RabbitMQ、Skills技能使用、AI知识库、AI联网搜索

804. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 438
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

805. **[webclaw](https://github.com/0xMassi/webclaw)** - ⭐ 438
   Fast, local-first web content extraction for LLMs. Scrape, crawl, extract structured data — all from Rust. CLI, REST API, and MCP server.

806. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 434
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to do its thing.

807. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 432
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

808. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 430
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

809. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 429
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

810. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 429
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

811. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 429
   A CLI inspector for the Model Context Protocol

812. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 428
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

813. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 427
   Spec-Driven Development MCP Server, not just Vibe Coding

814. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 427
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

815. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 426
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

816. **[ZeroToken](https://github.com/AMOS144/ZeroToken)** - ⭐ 426
   ZeroToken — Record once, automate forever. A lightweight MCP for agent-driven browser automation, script recording, and scheduled execution.

817. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 425
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

818. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 424

819. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

820. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 421
   Unlock 650+ MCP servers tools in your favorite agentic framework.

821. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 420
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

822. **[ScienceClaw](https://github.com/AgentTeam-TaichuAI/ScienceClaw)** - ⭐ 419
   ScienceClaw is a personal research assistant built with LangChain DeepAgents and AIO Sandbox infrastructure, adopting a completely new architecture beyond OpenClaw. It offers stronger security, better transparency, and a more user-friendly experience.

823. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 417
   The AI-powered toolkit that grows your YouTube channel on autopilot.

824. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 417
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

825. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 416
   Baidu Map MCP Server

826. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 414
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

827. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 413
   Memento MCP: A Knowledge Graph Memory System for LLMs

828. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 413
   lunar.dev: Agent native MCP Gateway for governance and security

829. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 413
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

830. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 413
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

831. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 413
   Search Airbnb using your AI Agent

832. **[MemoMind](https://github.com/24kchengYe/MemoMind)** - ⭐ 412
   Give your AI agent a brain that remembers. Local memory system for Claude Code — 100% private, GPU-accelerated, zero cloud dependency.

833. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 409
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

834. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 407
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

835. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 407
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

836. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 407
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

837. **[speakeasy](https://github.com/speakeasy-api/speakeasy)** - ⭐ 406
   Build APIs your users love ❤️ with Speakeasy. ✨ Polished and type-safe SDKs. 🌐 Terraform providers, MCP servers, CLIs and Contract Tests for your API. OpenAPI native. 

838. **[human-skill-tree](https://github.com/24kchengYe/human-skill-tree)** - ⭐ 406
   🌳 AI-Powered Skill Tree for Lifelong Human Learning. 30+ skills from K-12 to career & social intelligence, built on cognitive science. | 人类养成记：AI 驱动的终身学习技能树

839. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 405
   The safest way to make REST calls in C# with an MCP Generator

840. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 405
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

841. **[routa](https://github.com/phodal/routa)** - ⭐ 403
   Build Your Agent Team for Real-World AI Development - Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/   A2A support across web and desktop.

842. **[distributed-load-testing-on-aws](https://github.com/aws-solutions/distributed-load-testing-on-aws)** - ⭐ 402
   Distributed Load Testing on AWS automates performance testing at scale, demonstrating how systems behave under different load conditions and helping identify potential performance issues throughout their lifecycle.

843. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 401
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

844. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 400
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

845. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 400
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

846. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 398
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

847. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 398
   Things.app MCP Server

848. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 397
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

849. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 395
   An experiment in software planning using MCP

850. **[freee-mcp](https://github.com/freee/freee-mcp)** - ⭐ 395
   Model Context Protocol (MCP) server for freee API integration

851. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 394
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

852. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 393
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

853. **[station](https://github.com/cloudshipai/station)** - ⭐ 391
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

854. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 391
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

855. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 391
   OpenSkills: Run Claude Skills Locally using any LLM

856. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 391
   MCP Server for code graph analysis and visualization by CodeGPT

857. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 391
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

858. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 391
   An implementation of Model Context Protocol (MCP) server for Argo CD.

859. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 390
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

860. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 386
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

861. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 386
   Local Groq Desktop chat app with MCP support

862. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 386
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

863. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 386
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

864. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 384
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

865. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 384
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

866. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 384
   MCP server for Todoist integration enabling natural language task management with Claude

867. **[JSReverser-MCP](https://github.com/NoOne-hub/JSReverser-MCP)** - ⭐ 383
   JSReverser-MCP 是一个面向 JavaScript 逆向分析的 MCP 工具，专门用于帮助开发者在真实浏览器环境中高效定位前端核心逻辑。它   将脚本检索、断点调试、函数 Hook、网络请求追踪、调用链分析、混淆还原和风险评估整合为统一能力，可直接接入 Claude、   Codex、Cursor 等支持 MCP 的客户端。你可以连接已开启的 Chrome，在登录态页面下持续采样请求参数与返回数据，快速定位签名、   加密、鉴权和关键业务流程。工具同时支持自动化页面操作与结构化报告导出，适合用于接口分析、安全研究、前端调试与工程排障等   场景

868. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 382
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

869. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 382
   An MCP server for loading skills (shim for non-claude clients).

870. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 382
   Nornicdb is a low-latency, Graph + Vector, Temporal MVCC with all sub-ms HNSW search, graph traversal, and writes. Uses Neo4j Bolt/Cypher and qdrant's gRPC drivers so you can switch with no changes. Then, adding intelligent features like schemas, managed embeddings, LLM reranking+inferrence, GPU acceleration, Auto-TLP, Memory Decay, and MCP server.

871. **[lsbot](https://github.com/ruilisi/lsbot)** - ⭐ 381
   Lean & Secure Bot

872. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 380
   An MCP implementation for Selenium WebDriver

873. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 380
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

874. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 379
   F2C MCP Server

875. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 378
   MCP server connecting to Kubernetes

876. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 378
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

877. **[memora](https://github.com/agentic-box/memora)** - ⭐ 378
   Give your AI agents persistent memory.

878. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 378
   A centralized reverse-proxy platform for MCP servers — manage, group, and export as Skills from a single endpoint.

879. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 377
   Model Context Protocol server for GraphQL

880. **[daymon](https://github.com/daymonio/daymon)** - ⭐ 377
   Daymon puts your favorite AI to work 24/7. It schedules, remembers, and orchestrates your own virtual team. Free.

881. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 376
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

882. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 376
   Control your Android devices with AI using Model Context Protocol

883. **[repowise](https://github.com/repowise-dev/repowise)** - ⭐ 376
   Codebase intelligence for AI-assisted engineering teams — auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.

884. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 374
   Model Context Protocol (MCP) Server for Graphlit Platform

885. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 374
   A macOS AppleScript MCP server

886. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 374
   Context-Engine MCP - Agentic Context Compression Suite

887. **[mq](https://github.com/harehare/mq)** - ⭐ 374
   A jq-like Markdown query language for command-line processing

888. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 373
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

889. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 373

890. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

891. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 372
   MCP server that provides LLMs with tools for interacting with EVM networks

892. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 372
   Xiaozhi MCP sample program

893. **[zerobox](https://github.com/afshinm/zerobox)** - ⭐ 372
   Lightweight, cross-platform process sandboxing powered by OpenAI Codex's runtime. Sandbox any command with file, network, and credential controls.

894. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 371
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

895. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 371
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

896. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 371
   MCP Server implementation for Ableton Live OSC control

897. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 371
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

898. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 370
   🐕⚡「极简至上 效率为王 秒级接入 一链即用」的 AI Bot

899. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 370
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

900. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 369
   MCP Server implementation for Xcode integration

901. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 369
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

902. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 368
   MCP server for JADX-AI Plugin

903. **[devopness](https://github.com/devopness/devopness)** - ⭐ 368
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

904. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 368
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

905. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 367
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

906. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

907. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 365
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

908. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 365
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

909. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 364
   Create a plan from a description in minutes

910. **[RenderDocMCP](https://github.com/halby24/RenderDocMCP)** - ⭐ 364

911. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 363
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

912. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 363
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

913. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 363
   MCP server for searching and retrieving Claude Agent Skills using vector search

914. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 362
   Model Context Protocol SDK for PHP

915. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 362
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

916. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 362
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

917. **[skylos](https://github.com/duriantaco/skylos)** - ⭐ 362
   Open-source Python, TypeScript, and Go SAST with dead code detection. Finds secrets, exploitable   flows, and AI regressions. VS Code extension, GitHub Action, and MCP server for AI agents.

918. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 362
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

919. **[tentix](https://github.com/labring/tentix)** - ⭐ 361
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

920. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 361
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

921. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 360
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

922. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 360
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

923. **[mcp](https://github.com/IBM/mcp)** - ⭐ 359
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

924. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 359
   MCP server retrieving transcripts of YouTube videos

925. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 358
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

926. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 358
   Elixir Model Context Protocol (MCP) SDK

927. **[pinion-os](https://github.com/chu2bard/pinion-os)** - ⭐ 357
   Client SDK, Claude plugin and skill framework for the Pinion protocol. x402 micropayments on Base.

928. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 356
   An MCP server for Azure DevOps

929. **[studio](https://github.com/decocms/studio)** - ⭐ 356
   Open-source control plane for your AI agents. Connect tools, hire agents, track every token and dollar

930. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

931. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 355
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

932. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 355
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

933. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 355
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands. 

934. **[hookdeck-cli](https://github.com/hookdeck/hookdeck-cli)** - ⭐ 353
   CLI for Hookdeck: forward webhooks to localhost (ngrok alternative), manage and query Event Gateway resources (sources, connections, destinations, events), run the MCP server for AI agents. Free for dev.

935. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 353
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

936. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 352
   MCP server for Bazi (八字) information

937. **[memorix](https://github.com/AVIDS2/memorix)** - ⭐ 352
   Open-source cross-agent memory layer for coding agents via MCP. Compatible with Cursor, Claude Code, Codex, Windsurf, Gemini CLI, GitHub Copilot, Kiro, OpenCode, Antigravity, and Trae.

938. **[google-ads-mcp](https://github.com/googleads/google-ads-mcp)** - ⭐ 351

939. **[n8n-claw](https://github.com/freddy-schuetz/n8n-claw)** - ⭐ 351
   OpenClaw-inspired autonomous AI agent built entirely in n8n. Adaptive RAG-powered memory, Skills via MCP templates, Expert Agents with delegated sub-agents, proactive task management, media understanding - self-hosted with one setup script

940. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 350

941. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 350
   Sega Master System / Game Gear / SG-1000 emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

942. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 350
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

943. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 348
   MCP to help Defenders Detection Engineer Harder and Smarter

944. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 348
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

945. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

946. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 347
   deep, reliable and confidential coding-context

947. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 346
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

948. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 346
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

949. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 345
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

950. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 344
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

951. **[figma-mcp-go](https://github.com/vkhanhqui/figma-mcp-go)** - ⭐ 344
   Figma MCP for free users — no rate limits, full read/write, text to designs, designs to code

952. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 343
   MCP server to expose VS Code editing features to an LLM for AI coding

953. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 343
   Lean Theorem Prover MCP

954. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 342
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

955. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 342
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

956. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 342
   MCP Server for interacting with Salesforce instances

957. **[boltmcp](https://github.com/boltmcp/boltmcp)** - ⭐ 341

958. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 341
   First AI‑enabled open-source Human Capital Management system that you can start using today.

959. **[Aegis](https://github.com/Justin0504/Aegis)** - ⭐ 341
   Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes.                                                                         

960. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 340
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

961. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

962. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 340
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

963. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 340
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

964. **[open-harness](https://github.com/MaxGfeller/open-harness)** - ⭐ 339
   A code-first, composable SDK to build powerful AI agents

965. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 338
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

966. **[mesh](https://github.com/decocms/mesh)** - ⭐ 337
   One secure endpoint for every MCP server. Deploy anywhere.

967. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 337
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

968. **[real-estate-mcp](https://github.com/tae0y/real-estate-mcp)** - ⭐ 337
   🏠 Ask Claude about Korean apartment prices — powered by 국토교통부 open API

969. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 336
   Example of an MCP server with custom tools that can be called directly from cursor

970. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 336
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

971. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 336
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

972. **[ship-safe](https://github.com/asamassekou10/ship-safe)** - ⭐ 336
   CLI security scanner built for the agentic era. Detects CI/CD misconfigs, agent permission risks, MCP tool injection, hardcoded secrets, and DMCA-flagged AI dependencies.

973. **[robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp)** - ⭐ 335
   Create agentic AI workflows in ROBLOX Studio

974. **[moling](https://github.com/gojue/moling)** - ⭐ 334
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

975. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 334
   MCP server to access Garmin data

976. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 333

977. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 333
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

978. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 331
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

979. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

980. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 331
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

981. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 330
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

982. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 330

983. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 329
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

984. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 328
   Mapbox Model Context Protocol (MCP) server

985. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 328
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

986. **[daan](https://github.com/pluveto/daan)** - ⭐ 325
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

987. **[safe-mcp](https://github.com/safe-agentic-framework/safe-mcp)** - ⭐ 325
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

988. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 325
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

989. **[everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh)** - ⭐ 325
   everything-claude-code 中文翻译项目：完整的 Claude Code 配置集合（agents, skills, hooks, commands, rules, MCPs）。源自 Anthropic 黑客松获胜者的实战配置，助力中文工程师高效理解与使用 Claude Code。

990. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 324
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

991. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 323
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

992. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 323
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

993. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 323
   Source code of minecraft 1.12

994. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

995. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 322
   MCP server for Claude to access Outlook data via Microsoft Graph API

996. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 322
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

997. **[emcee](https://github.com/mattt/emcee)** - ⭐ 321
   MCP generator for OpenAPIs 🫳🎤💥

998. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 321
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

999. **[cymbal-air-toolbox-demo](https://github.com/GoogleCloudPlatform/cymbal-air-toolbox-demo)** - ⭐ 321
   Demo of a customer service agent (Cymbal Air) using LangGraph, Tools, and RAG to interact with Google Cloud Databases via MCP Toolbox.

1000. **[pipelock](https://github.com/luckyPipewrench/pipelock)** - ⭐ 321
   Firewall for AI agents. DLP scanning, SSRF protection, bidirectional MCP scanning, tool poisoning detection, and prompt injection blocking.

1001. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 320

1002. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 320
   A Model Context Protocol server for building an investor agent

1003. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 319
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

1004. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 318
   This is a Minecraft Base Client

1005. **[pydantic-resolve](https://github.com/allmonday/pydantic-resolve)** - ⭐ 318
   A tool for building domain layer modeling and use case assembly.

1006. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 318
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

1007. **[mcp](https://github.com/oracle/mcp)** - ⭐ 318
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

1008. **[deep-research-mcp](https://github.com/teelaitila/deep-research-mcp)** - ⭐ 317

1009. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 317
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

1010. **[mcp](https://github.com/cloudflare/mcp)** - ⭐ 317
   MCP server for the Cloudflare API

1011. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 315
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

1012. **[generator](https://github.com/context-hub/generator)** - ⭐ 315
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

1013. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 315
   Repo of skills for autogen studio using model context protocol (mcp)

1014. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 313
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

1015. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 313
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

1016. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 312

1017. **[octo-terminal-releases](https://github.com/johunsang/octo-terminal-releases)** - ⭐ 312
   Octo Terminal — The ultimate vibe coding terminal. AI-powered IDE with Claude, Codex, Ollama built-in. Terminal + editor + notes + browser in one app. Tauri + React + Rust.

1018. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 312
   Model Context Protocol server for DeepSeek's advanced language models

1019. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 310
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

1020. **[claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)** - ⭐ 310
   Plugin suite + bundled MCP servers for Claude Code. Full delivery lifecycle: Agile pipeline with multi-model AI review, project bootstrap, documentation generation, codebase audits, performance optimization, community workflows. Includes hex-line (hash-verified editing), hex-graph (code knowledge graph), and hex-ssh (remote SSH) MCP servers.

1021. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

1022. **[agentshield](https://github.com/affaan-m/agentshield)** - ⭐ 309
   AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions. Available as CLI, GitHub Action, ECC plugin, and GitHub App integration. 🛡️

1023. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 308
   MCP server for Windows OS automation

1024. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 307
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

1025. **[travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit)** - ⭐ 307
   AI-powered travel hacking with points, miles, and award flights. Drop-in skills and MCP servers for OpenCode and Claude Code.

1026. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 306
   Token-efficient MCP adapter for Pi coding agent

1027. **[fim-one](https://github.com/fim-ai/fim-one)** - ⭐ 306
   LLM-powered Agent Runtime with Dynamic DAG Planning & Concurrent Execution

1028. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 305
   api router for MCP Servers

1029. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 305
   Smithery helps AI agents access external services via a unified gateway.

1030. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 305
   Turn any openapi file into an mcp server, with just the tools you need.

1031. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 305
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

1032. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 305
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

1033. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 305
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

1034. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 304
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

1035. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 303
   A working pattern for SSE-based MCP clients and servers

1036. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 303
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

1037. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 303
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

1038. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 303
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

1039. **[Lucid](https://github.com/get-Lucid/Lucid)** - ⭐ 302
   An intelligence layer grounding autonomous agents in verified, real-time knowledge at scale.

1040. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

1041. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 301
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

1042. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 301
   An MCP server providing tools for image processing operations

1043. **[PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor)** - ⭐ 300
   Free, open-source SQL Server performance monitoring — 32 collectors, real-time alerts, graphical plan viewer, MCP server for AI analysis. Supports SQL 2016-2025, Azure SQL, AWS RDS.

1044. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 299
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡mcphub

1045. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 299
   Obsidian MCP (Model Context Protocol) Server

1046. **[agents](https://github.com/astronomer/agents)** - ⭐ 299
   AI agent tooling for data engineering workflows.

1047. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 298
   Agentic RAG for any scenario. Customize sources, depth, and width

1048. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 298
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1049. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 298
   MCP Server for Odoo

1050. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 297
   MCP implementation of Claude Code capabilities and more

1051. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 297
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

1052. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 297
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

1053. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 296
   Discover Exceptional MCP Servers

1054. **[codemogger](https://github.com/glommer/codemogger)** - ⭐ 296
   Codemogger is a code indexing library and MCP server for AI coding agents

1055. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 296
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

1056. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 295
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

1057. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 295
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1058. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 295
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

1059. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 294
   The specification for the Universal Tool Calling Protocol

1060. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 294
   Minimal MCP Server for Aider

1061. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 294
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

1062. **[consult7](https://github.com/szeider/consult7)** - ⭐ 292
   MCP server to consult a language model with large context size

1063. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 292
   CAD MCP Server

1064. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 292
   Appium MCP on Steroids!

1065. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 291

1066. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 291

1067. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 291
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

1068. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 291
   An MCP server for Massive.com Financial Market Data

1069. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 291
   web GUI for securely managing local OpenCode configuration

1070. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 290
   Standardized environment infrastructure for Agentic AI development.

1071. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 290
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

1072. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 290
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

1073. **[EDDI](https://github.com/labsai/EDDI)** - ⭐ 290
   Multi-agent orchestration middleware that coordinates between users, AI agents (LLMs), and business systems. It provides intelligent routing, conversation management, and API orchestration for building sophisticated AI-powered applications.

1074. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 290
   基于 SSH 的 MCP 服务 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1075. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 290
   SpringAI，LLM，MCP，Embedding

1076. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 289
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

1077. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 289
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1078. **[meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)** - ⭐ 288
   Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis.

1079. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 287
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

1080. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 287
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

1081. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 287
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1082. **[Dex](https://github.com/davekilleen/Dex)** - ⭐ 287
   Your AI Chief of Staff — a personal operating system starter kit that adapts to your role. No coding required.

1083. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

1084. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 286
   simple web ui to manage mcp (model context protocol) servers in the claude app

1085. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

1086. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 285
   Code to process many kinds of content by an author into an MCP server

1087. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 285
   MCP server for Coolify — 38 optimized tools for managing self-hosted PaaS through AI assistants

1088. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 284
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

1089. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 283
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

1090. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 283
   Home Assistant MCP Server

1091. **[alfanous](https://github.com/Alfanous-team/alfanous)** - ⭐ 283
   Alfanous is an Arabic search engine API provides the simple and advanced search in Quran , more features and many interfaces...

1092. **[certctl](https://github.com/shankar0123/certctl)** - ⭐ 283
   Self-hosted certificate lifecycle automation platform. Any CA, any server, zero human intervention. Full REST API, web dashboard, and agent-based deployment where private keys never leave your infrastructure. Includes CLI, MCP server for AI assistants, and compliance mapping for SOC 2, PCI-DSS, and NIST.

1093. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 282
   MCP server for browser automation using Playwright

1094. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 281
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

1095. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

1096. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 281
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

1097. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 281
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

1098. **[DebugMCP](https://github.com/microsoft/DebugMCP)** - ⭐ 281
   Gift your VS Code agent a real debugger: breakpoints, stepping, inspection.

1099. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 281
   Bringing Human Capabilities to AI Agents

1100. **[awesome-fintech](https://github.com/moov-io/awesome-fintech)** - ⭐ 281
   A curated collection of open source fintech libraries and resources.

1101. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

1102. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 280
   MCP Server for Tree-sitter

1103. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 278
   MCP integration platforms making AI-Agents developers focusing on their own tasks

1104. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 278
   Apollo MCP Server

1105. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 277
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

1106. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 277
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

1107. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 277
   A Model Context Protocol Server for MongoDB

1108. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 277
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

1109. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 277
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1110. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

1111. **[opentabs](https://github.com/opentabs-dev/opentabs)** - ⭐ 276
   Browser automation clicks buttons. OpenTabs calls APIs.

1112. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 275
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

1113. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 275
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

1114. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 274
   Model Context Protocol server implementation for Reddit

1115. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 274
   Model Context Protocol (MCP) Server for dify workflows

1116. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 274
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

1117. **[claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager)** - ⭐ 274
   GUI app to manage MCP servers for Claude Code

1118. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 274
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1119. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 274
   Lightweight MCP server for Spotify

1120. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 273
   Apache Doris MCP Server

1121. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 273
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

1122. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 272
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

1123. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 272
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

1124. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 272
   MCP stdio server for frida

1125. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

1126. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 271
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

1127. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 271
   Volcengine MCP Servers

1128. **[nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server)** - ⭐ 271

1129. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

1130. **[BitFun](https://github.com/GCWing/BitFun)** - ⭐ 270
   BitFun is an Agentic Development Environment (ADE，AI IDE) featuring a cutting-edge Code Agent system with four modes — Agentic, Plan, Debug, and Review. Extensible via MCP, Skills, custom Agents and Rules. Built with Rust + TypeScript for an ultra-lightweight, fluid cross-platform experience.

1131. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 270
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

1132. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

1133. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 268
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

1134. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 268
   A list of open-source AI projects you can use to generate income easily.

1135. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 268
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

1136. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 268
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1137. **[api-agent](https://github.com/agoda-com/api-agent)** - ⭐ 267
   Universal MCP server for GraphQL/REST APIs

1138. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 266
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

1139. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 265
   小智AI客户端，目前主要用于MCP的对接

1140. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 265
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

1141. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 265
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

1142. **[unity-cli-loop](https://github.com/hatayama/unity-cli-loop)** - ⭐ 265
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1143. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 264

1144. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 264
   Lightweight agent orchestration dev tool that lives in your repo

1145. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 264
   An introduction to the world of AI Agents

1146. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 263
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

1147. **[flyto-core](https://github.com/flytohub/flyto-core)** - ⭐ 263
   The open-source execution engine for AI agents. 412 modules, MCP-native, triggers, queue, versioning, metering.

1148. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 263
   Semantic code searcher and codebase utility

1149. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 262
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

1150. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 262
   A collection of MCP servers

1151. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 262
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.) and AI agents (Claude Desktop, OpenClaw, etc.). Supports Serper, Tavily, and SearXNG.

1152. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 261
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

1153. **[codedb](https://github.com/justrach/codedb)** - ⭐ 261
   Zig code intelligence server and MCP toolset for AI agents. Fast tree, outline, symbol, search, read, edit, deps, snapshot, and remote GitHub repo queries.

1154. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 260
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

1155. **[corpusos](https://github.com/Corpus-OS/corpusos)** - ⭐ 259
   Open-source protocol suite standardizing LLM, Vector, Graph, and Embedding infrastructure across LangChain, LlamaIndex, AutoGen, CrewAI, Semantic Kernel, and MCP. 3,330+ conformance tests. One protocol. Any framework. Any provider.

1156. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 259
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1157. **[api200](https://github.com/API-200/api200)** - ⭐ 258
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

1158. **[domain-check](https://github.com/saidutt46/domain-check)** - ⭐ 258
   Fast, universal domain availability checker - 1,200+ TLDs, pattern generation, RDAP with WHOIS fallback. CLI + Rust library + MCP server for AI agents.

1159. **[jcode](https://github.com/1jehuang/jcode)** - ⭐ 258
   Coding Agent Harness

1160. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 257
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

1161. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 257
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

1162. **[swiss-ai-call-agent](https://github.com/Chrissotino/swiss-ai-call-agent)** - ⭐ 256
   Enterprise-grade AI Call Agent for the Swiss market – inbound & outbound calls, multilingual (DE/FR/IT), MCP architecture, Claude AI decision engine, real-time dashboard

1163. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 256
   A code reasoning MCP server, a fork of sequential-thinking

1164. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 256
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1165. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 255
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

1166. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 254
   Headless IDA Pro MCP Server

1167. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 254
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

1168. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 254
   AWS MCP Proxy Server

1169. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

1170. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 253
   MCP server for TouchDesigner

1171. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 252
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1172. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 252
   hydra-ai

1173. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 252
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

1174. **[agentrove](https://github.com/Mng-dev-ai/agentrove)** - ⭐ 252
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1175. **[vibing-steampunk](https://github.com/oisee/vibing-steampunk)** - ⭐ 251
   vs-punk: ADT to MCP bridge - Vibe code in ABAP / AMDP

1176. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 250
   A MCP server for our beloved terminal multiplexer tmux.

1177. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 250
   AI-first security scanner with 76 analyzers, 9,600+ detection rules, and repo poisoning detection for AI/ML, LLM agents, and MCP servers. Scan any GitHub repo with: medusa scan --git user/repo

1178. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 249
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1179. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 249
   Agentify Desktop lets Codex/Claude/OpenCode  control your logged-in ChatGPT, Claude, AiStudio, Gemini, Grok, Perplexity web sessions via MCP, parallel hidden/visible tabs, file upload + image download

1180. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 248
   MCP server(s) for Aipolabs ACI.dev

1181. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 248
   MCP server implementation for Google's Gemini API

1182. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 248
   MCP Interface for Video Jungle

1183. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 248
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

1184. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 248
   Zerodha Kite MCP server

1185. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

1186. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

1187. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 247
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1188. **[h1-brain](https://github.com/PatrikFehrenbach/h1-brain)** - ⭐ 247
   MCP server that connects AI assistants to HackerOne for bug bounty hunting

1189. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 246
   Turn any MCP server into a Python module

1190. **[dat](https://github.com/hexinfo/dat)** - ⭐ 245
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

1191. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 245
   A SEC EDGAR MCP (Model Context Protocol) Server

1192. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 245
   Fast-track AI innovation with a centralized, trusted, curated registry

1193. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 245
   Lightweight C++ MCP (Model Context Protocol) SDK

1194. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1195. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 244
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

1196. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 244
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

1197. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 244
   pctx is the execution layer for agentic tool calls. It auto-converts agent tools and MCP servers into code that runs in secure sandboxes for token-efficient workflows.

1198. **[embodied-claude](https://github.com/lifemate-ai/embodied-claude)** - ⭐ 243
   Claudeに身体性を与えるMCP群

1199. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 243
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

1200. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 243
   The evaluation benchmark on MCP servers

1201. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 243
   🔥 Model Context Protocol (MCP) server for Firebase.

1202. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 243
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1203. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 242
   An experimental MCP Server for foundry built for Solidity devs

1204. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 242
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

1205. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 242
   Penpot's official MCP Server

1206. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 241
   Code Runner MCP Server

1207. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 241
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

1208. **[vurb.ts](https://github.com/vinkius-labs/vurb.ts)** - ⭐ 241
   Vurb.ts - The TypeScript Framework for MCP Servers. Type-safe tools, structured AI perception, and built-in security. Deploy once — every AI assistant connects instantly.

1209. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 240
   Simplified Gemini for Claude Code. 

1210. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

1211. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 240
   Playwright MCP fork that works with Cloudflare Browser Rendering

1212. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 240
   MCP Server for Telegram

1213. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 240
   Opensource Memory for Agents

1214. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 240
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1215. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 239
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

1216. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

1217. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 239
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1218. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 239
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1219. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 238

1220. **[JoySafeter](https://github.com/jd-opensource/JoySafeter)** - ⭐ 238
   🚀 JoySafeter: An enterprise AI Agent Platform—Not just chatting. building、running、testing, and tracing autonomous Agent Teams with visual orchestration...

1221. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 238
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1222. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 237
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1223. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 236
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1224. **[call.md](https://github.com/video-db/call.md)** - ⭐ 236
   Turn meetings into live agent loops. Record, transcribe, and analyze meetings with real-time AI intelligence — before, during, and after calls.

1225. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

1226. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 235
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1227. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 235
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

1228. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 235
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1229. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 234
   Korea public data portal (data.go.kr) API MCP servers

1230. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 233
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1231. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 233
   MCP server for Anki via AnkiConnect

1232. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 232
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

1233. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 232
   A Model Context Protocol (MCP) server that enables natural language queries to databases

1234. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 232
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

1235. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 232
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1236. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 232
   MCP Server for ServiceNow

1237. **[lokka](https://github.com/merill/lokka)** - ⭐ 232
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1238. **[Ori-Mnemos](https://github.com/aayoawoyemi/Ori-Mnemos)** - ⭐ 232
   Local-first persistent agentic memory powered by Recursive Memory Harness (RMH). Open source must win.

1239. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 231
   Creates a simple MCP tool server with "streaming" HTTP.

1240. **[unifi-mcp](https://github.com/sirkirby/unifi-mcp)** - ⭐ 231
   MCP servers for the UniFi suite of applications, Network, Protect, Access, and Drive

1241. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 230
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

1242. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 230
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

1243. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 230
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

1244. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 230
   A Model Context Protocol (MCP) server for interacting with Twitter.

1245. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 230
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1246. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 229
   🧰 All-in-one domain name intelligence as a service

1247. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 229
   Autonomous SWE agent working in the cloud!

1248. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1249. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 229
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1250. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 227
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

1251. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1252. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

1253. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 227
   Penpot MCP server

1254. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 227
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1255. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 226
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1256. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 225
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1257. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 225
   Model Context Protocol server to run commands (tool: `runProcess`)

1258. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 225
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1259. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 225
   Securely scale AI usage across your organization.  Control plane for building, securing and monitoring your agents, mcp and skills.

1260. **[claude-code-organizer](https://github.com/mcpware/claude-code-organizer)** - ⭐ 225
   Dashboard to manage Claude Code memories, configs, and MCP servers — security scanner for tool poisoning, context token budget tracker, duplicate cleanup, scope management. npx @mcpware/claude-code-organizer

1261. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 224
   Model Context Protocol Servers for Milvus

1262. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 224
   mindmap, mcp server, artifact

1263. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 224
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1264. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 224
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1265. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 223
   Tableau's official MCP Server. Helping Agents see and understand data.

1266. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

1267. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

1268. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

1269. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 222
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1270. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 222
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1271. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 222
   A tool for autonomous agents like OpenClaw to discover and learn skills autonomously

1272. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 222
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1273. **[agent-craft](https://github.com/Annyfee/agent-craft)** - ⭐ 222
   AI Agent 教学仓库 | 系统化 LangChain、RAG、LangGraph、MCP 全栈实战代码 | 万字博客详解 | 开源可运行示例 | 从零构建智能体

1274. **[jebmcp](https://github.com/flankerhqd/jebmcp)** - ⭐ 222

1275. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 222
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1276. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

1277. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 221
   Homeassistant MCP server for 小智AI

1278. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 221
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1279. **[agent-skills](https://github.com/jdrhyne/agent-skills)** - ⭐ 221
   A collection of AI agent skills for Clawdbot, Claude Code, Codex

1280. **[STS2MCP](https://github.com/Gennadiyev/STS2MCP)** - ⭐ 221
   Full agentic runs for Slay the Spire 2. A mod that exposes in-game state, and the MCP server for the mod.

1281. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 220
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1282. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 220
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1283. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 219
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1284. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

1285. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 219
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1286. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 218
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1287. **[ATaC](https://github.com/ATaC-team/ATaC)** - ⭐ 217
   Record and Replay AI Agent Trajectories.

1288. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 217

1289. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 216

1290. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 216
   Razorpay's Official MCP Server

1291. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 216
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1292. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 215
   Hugging Face MCP Server

1293. **[AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem)** - ⭐ 215
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1294. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 214
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1295. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1296. **[airbroke](https://github.com/icoretech/airbroke)** - ⭐ 213
   🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher

1297. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1298. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 212
   Run and monitor MCP servers locally

1299. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 212
   Pure Rust implementation of MCP server for headless terminal 

1300. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 212
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1301. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 211
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1302. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 210
   🔎 A MCP server for Unsplash image search.

1303. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 210
   An MCP server to use Sora video generation APIs

1304. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1305. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 210
   A Multi-modal MCP client for voice powered agentic workflows

1306. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1307. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 210

1308. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 210
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1309. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 210
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1310. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 209
   📜 An MCP server for conversation history search and retrieval in Claude Code

1311. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 209
   A ReAct-Based Highly Robust Autonomous Agent (Harness) Framework.

1312. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1313. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 209
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

1314. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 209
   IMAP and SMTP via MCP Server

1315. **[Claude-code-ChatInWindows](https://github.com/LKbaba/Claude-code-ChatInWindows)** - ⭐ 208
   Full-featured GUI for Claude Code CLI in VS Code — Windows (no WSL) & macOS. Third-party API, MCP plugins, Skills, Hooks, real-time token tracking. Actively maintained.

1316. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 208
   Connect your AI to your APIs on Postman

1317. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 207
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1318. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 207
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1319. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 207
   interactive programming of melodies, producing MIDI 

1320. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 207
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1321. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 207
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1322. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1323. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 206
   MCP server for Dynatrace Observability

1324. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 206
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1325. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 206
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1326. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 206
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1327. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 206
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1328. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 206
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1329. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 206
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1330. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1331. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1332. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 205
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1333. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 205
   Self-hosted AI RAG + MCP Platform

1334. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1335. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 205
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1336. **[mcp-fusion](https://github.com/vinkius-labs/mcp-fusion)** - ⭐ 204
   MCP Fusion - The framework for AI-native MCP servers. 

1337. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 204
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

1338. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 204
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1339. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 203
   Neo4j official MCP Server

1340. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 203
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1341. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 203
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1342. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 203
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1343. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 203
   Model Context Protocol for x64dbg & x32dbg

1344. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1345. **[CrowdSentinels-AI-MCP](https://github.com/thomasxm/CrowdSentinels-AI-MCP)** - ⭐ 202
   AI-powered threat hunting and incident response MCP server for Elasticsearch/OpenSearch

1346. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 202
   Sketchup Model Context Protocol

1347. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 202
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1348. **[novamira](https://github.com/use-novamira/novamira)** - ⭐ 202
   MCP server that gives AI agents full access to WordPress through PHP execution and filesystem operations

1349. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 201
   R MCP Server

1350. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 201
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1351. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 201
   A MCP Server for the RAG Web Browser Actor

1352. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 201
   Local-first RAG server for developers. Semantic + keyword search for code and technical docs. Works with MCP or CLI. Fully private, zero setup.

1353. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 201
   💻 Give AI models complete control of your computer (probably a bad idea)

1354. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1355. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 200
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1356. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 200
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1357. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 200
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1358. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 200
   AI-Driven Automated Red Team Orchestration Framework | AI驱动的自动化红队编排框架 | 101 MCP Tools | 2000+ Payloads | Full ATT&CK Coverage | MCTS Attack Planner | Knowledge Graph | Cross-platform

1359. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 199
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1360. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 199
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1361. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 199
   这是一个专为开发企业级MCP server而设计的通用开发框架

1362. **[facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp)** - ⭐ 199
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1363. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 199
   A Model Context Protocol (MCP) server providing access to Google Search Console

1364. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 199
   Tools to allow LLM clients to interact with Linux systems remotely

1365. **[pasal](https://github.com/ilhamfp/pasal)** - ⭐ 198
   Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + REST API + web app giving AI grounded access Indonesian laws.

1366. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 198
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1367. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 198
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1368. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 198
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1369. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 197
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1370. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 197
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1371. **[mcp-todoist](https://github.com/greirson/mcp-todoist)** - ⭐ 197
   MCP server that connects Claude to Todoist for natural language task and project   management with bulk operations

1372. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 196
   Google Analytics 4 data to AI agents, agentic workflows, and MCP clients. Give agents analysis-ready access to website traffic, user behavior, and performance data with schema discovery, server-side aggregation, and safe defaults that reduce data wrangling.

1373. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 196
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

1374. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1375. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 196
   MCP server implementation for the UniFi network application

1376. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 196
   Index the world's undocumented APIs

1377. **[codefire-app](https://github.com/websitebutlers/codefire-app)** - ⭐ 196
   CodeFire gives AI coding tools persistent memory, task tracking, and project intelligence. A desktop companion for the AI-native workflow.

1378. **[open-webui-plugins](https://github.com/Classic298/open-webui-plugins)** - ⭐ 196
   A curated collection of Open WebUI plugins - tools, skills, filters, pipes, and actions that extend your AI chat experience.

1379. **[registry-broker-skills](https://github.com/hashgraph-online/registry-broker-skills)** - ⭐ 196
   AI agent skills for the Universal Registry - search, chat, and register 72,000+ agents across 14+ protocols. Works with Claude, Codex, Cursor, OpenClaw, and any AI assistant.

1380. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 196
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1381. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 195
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1382. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1383. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 195
   Manage / Proxy / Secure your MCP Servers

1384. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 195
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1385. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 194
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1386. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 194
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1387. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 194
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1388. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 194
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1389. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 194
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1390. **[openclaw-claude-code](https://github.com/Enderfga/openclaw-claude-code)** - ⭐ 194
   OpenClaw plugin — turn Claude Code CLI into a programmable, headless coding engine with plenty of tools, agent teams, and multi-model proxy

1391. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 193

1392. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 193
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1393. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 193
   Absurdly easy Model Context Protocol Servers in Typescript

1394. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 192
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1395. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 192
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1396. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 192
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1397. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 192
   Learn how to use MCP Servers with GitHub Copilot

1398. **[LycheeMem](https://github.com/LycheeMem/LycheeMem)** - ⭐ 192
   Compact, efficient, and extensible long-term memory for LLM agents.

1399. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 191
   Discord MCP Server for Claude Integration

1400. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 191
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1401. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 191
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1402. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 191
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1403. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 191
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1404. **[ai-skills](https://github.com/sanjay3290/ai-skills)** - ⭐ 191
   Collection of agent skills for AI coding assistants

1405. **[ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero)** - ⭐ 191
    🚀 2026 最系统的 AI Agent 速成指南｜智能体实战教程 · 完整学习路径  + 实战项目 + 面试题库 · 对标大模型应用开发工程师岗位 · 覆盖LangChain / LangGraph / Coze / Dify / MCP / skills / LLM / RAG / 提示词 · 企业级部署与微调 · 从0到企业级落地 + 从学习到上线项目 + 面试准备一体化 

1406. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1407. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 190
   Supabase MCP server created in Python.

1408. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 190
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1409. **[gigabrain](https://github.com/legendaryvibecoder/gigabrain)** - ⭐ 190
   Local-first memory layer for OpenClaw, Codex App, and Codex CLI: capture, recall, dedupe, and native sync.

1410. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 190
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1411. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 189
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1412. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 189
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1413. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 189
   MCP Server for Wazuh SIEM

1414. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 189
   Operating System for your personal AI Agents with Security-first approach. Multi-channel (WhatsApp, Telegram, Discord, Slack, iMessage), multi-provider (Claude, GPT, Gemini, Ollama), fully self-hosted.

1415. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 188
   MCP server for AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends, focus-free dispatch, undo/redo, P&ID symbols, and robust IPC with ESC prefix and UTF-8 fallback. Companion agent skill: puran-water/autocad-drafting

1416. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 188

1417. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1418. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1419. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1420. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 187
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1421. **[aelf-skills](https://github.com/AElfProject/aelf-skills)** - ⭐ 187
   Unified aelf skills hub for discovery, routing, bootstrap, and health checks across OpenClaw, Codex, Cursor, and Claude Code.

1422. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 187
   This extension enables developers to implement the MCP server features easily.

1423. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 187
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1424. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1425. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 186
   Model Context Protocol Servers in Quarkus

1426. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1427. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 185
   Official Magic UI MCP server.

1428. **[shodh-memory](https://github.com/varun29ankuS/shodh-memory)** - ⭐ 185
   Cognitive memory for AI agents — learns from use, forgets what's irrelevant, strengthens what matters. Single binary, fully offline.

1429. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 185
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1430. **[claude-in-mobile](https://github.com/AlexGladkov/claude-in-mobile)** - ⭐ 185
   MCP server for mobile and desktop automation — Android (via ADB), iOS Simulator (via simctl), and Desktop (Compose Multiplatform). Like Claude in Chrome but for mobile devices and desktop apps

1431. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1432. **[omem](https://github.com/ourmem/omem)** - ⭐ 184
   Shared Memory That Never Forgets — persistent memory for AI agents with Space-based sharing across agents and teams. Plugins for OpenCode, Claude Code, OpenClaw, MCP Server.

1433. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 184
   MCP stdio server for radare2

1434. **[sap-skills](https://github.com/secondsky/sap-skills)** - ⭐ 184
   Production-ready Claude Code skills for SAP development - 35 skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more

1435. **[LetsFG](https://github.com/LetsFG/LetsFG)** - ⭐ 184
   Agent-native flight search & booking. Saved $116 across 5 routes vs Google Flights (verified). 400+ airlines in 5 seconds. Star = free forever for first 1,000 stargazers.

1436. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 183
   MCP for calling Siri Shorcuts from LLMs

1437. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 183
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1438. **[siconos](https://github.com/siconos/siconos)** - ⭐ 183
   Simulation framework for nonsmooth dynamical systems

1439. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1440. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1441. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 182
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1442. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 182
   A simple CLI to install MCP servers into any client - auth included!

1443. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 182
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1444. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 182
   MCP Server for the Bilibili API, supporting various operations.

1445. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 182
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1446. **[binary-ninja-headless-mcp](https://github.com/mrphrazer/binary-ninja-headless-mcp)** - ⭐ 182
   Headless Binary Ninja MCP server — giving AI agents deep reverse-engineering capabilities via 180 tools.

1447. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 182
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1448. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 181
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1449. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 181
   Typescript SDK to build MCP servers in an agnostic way

1450. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 181
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1451. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 181
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1452. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 181
   Skill + MCP server to turn your agent into an RLM. Load context, iterate with search/code/think tools, converge on answers.

1453. **[docs](https://github.com/strands-agents/docs)** - ⭐ 181
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1454. **[mcp-dev-brasil](https://github.com/codespar/mcp-dev-brasil)** - ⭐ 181
   MCP servers for Brazilian services — payments, fiscal, banking, communication. Generated by CodeSpar.

1455. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 180
   A self-hosted web UI that simplifies AI experimentation and testing for Java developers. It provides playgrounds for all major vector databases and MCP tools, supports intuitive interaction with LLMs, and enables rapid development and testing of RAG workflows, MCP integrations, and unified chat experiences.

1456. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 180

1457. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 180
   Official MCP server for Tripo

1458. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 180
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1459. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 180
   An MCP server to search for flights.

1460. **[token-savior](https://github.com/Mibayy/token-savior)** - ⭐ 180
   Token-efficient structural codebase MCP server for AI-assisted development

1461. **[godot-mcp](https://github.com/tomyud1/godot-mcp)** - ⭐ 180
   MCP Server and Godot Plugin for AI-assisted game development

1462. **[memov](https://github.com/memovai/memov)** - ⭐ 180
   Give git-like & traceable memory to OpenClaw and any coding agents. By https://memov.ai/ aka Entire CLI for every coding agents by MCP.

1463. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 179
   An MCP server for Anki

1464. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 179
   Examples of using Pipedream's MCP server in your app or AI agent.

1465. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 179
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1466. **[xiaoi](https://github.com/xvhuan/xiaoi)** - ⭐ 179
   小爱音箱语音通知工具：提供 CLI/TUI/MCP/Webhook 一键播报与控制音量，支持 PM2 常驻部署，支持docker部署。

1467. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 178
   MCP Server for Searching Turkish Legislation

1468. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1469. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1470. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 178
   Chat application with multi-agents system supports multi-models and MCP

1471. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 178
   Official Railway MCP Server for interacting with your Railway account

1472. **[copilot-plugins](https://github.com/github/copilot-plugins)** - ⭐ 178
   The official GitHub Copilot plugins collection — MCP servers, skills, hooks, and other extensibility tools for GitHub Copilot.

1473. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 178
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1474. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 177
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1475. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 177
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1476. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 177
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1477. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 176
   Revornix is an open-source, local-first AI information/markdown workspace. It helps you collect fragmented inputs, turn them into structured knowledge, generate reports with images and podcast audio, and deliver the output through automated notifications.

1478. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 176
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1479. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 176
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1480. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 176
   A light touch MCP task orchestration server for AI agents. Persistent work tracking and context storage across sessions and agents.  Defines planning floors through composable notes with optional gating transitions.   Coordinates multi-agent execution without prescribing how agents do their work.

1481. **[Corbell](https://github.com/Corbell-AI/Corbell)** - ⭐ 176
   AI-powered spec generation and review using multi-repo code graph intelligence for backend teams that ship to production.

1482. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 176
   Nextcloud MCP Server

1483. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 175
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1484. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 175
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1485. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 175
   MCP Server that enables Claude code to interact with Gemini

1486. **[Companion](https://github.com/mattt/Companion)** - ⭐ 175
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1487. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 174
   Turn any website or doc into an MCP server

1488. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1489. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 174
   MCP server to work with Telegram through MTProto

1490. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 174
   A MCP server to search for accurate academic articles.

1491. **[agent-skills-hub](https://github.com/zhuyansen/agent-skills-hub)** - ⭐ 174
   Discover and compare open-source Agent Skills, tools & MCP servers — with quality scoring, trending analysis, and automated GitHub sync

1492. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 174
   Supercharge AI Agents, Safely

1493. **[command](https://github.com/scopecraft/command)** - ⭐ 173
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1494. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 173
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1495. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 173
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1496. **[openchrome](https://github.com/shaun0927/openchrome)** - ⭐ 173
   Open-source browser automation MCP server. Control your real Chrome from any AI agent.

1497. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 172
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1498. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 172
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1499. **[STS2-Agent](https://github.com/CharTyr/STS2-Agent)** - ⭐ 172
   杀戮尖塔2的MOD，将杀戮尖塔2的游戏状态与操作暴露为本地 HTTP API 包装成 MCP Server，供支持 MCP 的AI客户端直接调用

1500. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 172

1501. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 171
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1502. **[clix](https://github.com/spideystreet/clix)** - ⭐ 171
   X from terminal. No API keys needed. Just plug your AI Agent.

1503. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 171
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1504. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 171

1505. **[sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** - ⭐ 171
   A complete list of SAP MCP Servers and SAP AI Skills

1506. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 171
   MCP Server for Postgres

1507. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 170
   One MCP Server, All Your Apps, Privacy First

1508. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1509. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 170
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1510. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 170
   Turn a web server into an MCP server in one click without making any code changes.

1511. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 170
   DataForSEO API modelcontextprotocol server 

1512. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 170
   MCP Salesforce connector

1513. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 169
   A Tiny Web Chat App for AI Models with MCP Client Support

1514. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 169
   MCPSDK.dev(ToolSDK.ai)'s Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1515. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 169
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1516. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 169
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1517. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 169
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1518. **[cachebro](https://github.com/glommer/cachebro)** - ⭐ 169
   File cache with diff tracking for AI coding agents. Drop-in MCP server that cuts token usage by 26%.

1519. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 169
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1520. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 169
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1521. **[arcticdb_mcp](https://github.com/YMuskrat/arcticdb_mcp)** - ⭐ 169
   MCP server for ArcticDB

1522. **[sibyl-research-system](https://github.com/Sibyl-Research-Team/sibyl-research-system)** - ⭐ 168
   Fully Autonomous AI Research System with Self-Evolution, built natively on Claude Code

1523. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 168
   Python SDK for interacting with the MCP Toolbox for Databases. 

1524. **[ClaudeR](https://github.com/IMNMV/ClaudeR)** - ⭐ 168
   Connect RStudio to Claude Code, Codex, Gemini, and other LLM agents via MCP. Multi-agent orchestration, automated manuscript   auditing, and zero-config setup with uvx

1525. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 168
   MCP Server for Google Slides

1526. **[oxideterm](https://github.com/AnalyseDeCircuit/oxideterm)** - ⭐ 168
   All-in-one terminal workspace — local shells, SSH, SFTP, remote IDE, AI agent, and file manager in a single native binary. Built with Tauri 2 and pure Rust SSH (no OpenSSL). Smart reconnect, MCP, RAG, plugins, 30+ themes, 11 languages.

1527. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 167
   Command line interface for MCP clients with secure execution and customizable security policies

1528. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 167
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1529. **[godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro)** - ⭐ 167
   162 MCP tools for AI-powered Godot 4 development. Scene, animation, 3D, physics, particles, audio, shader, input simulation, runtime analysis, navigation, testing & more. $5 one-time.

1530. **[kraken-cli](https://github.com/krakenfx/kraken-cli)** - ⭐ 167
   The first AI-native CLI for trading crypto, stocks, forex, and derivatives.

1531. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 166
   A desktop application that adds powerful tools to Claude and AI platforms

1532. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 166
   c4 GenAI Suite

1533. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 166
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1534. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 166
   Model Context Protocol For R

1535. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 166
   Local-first MCP App framework for ChatGPT Apps, Claude, and more.

1536. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 165
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1537. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 165
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1538. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 165
   Persistent Intelligence Infrastructure for AI Agents

1539. **[PolyMCP](https://github.com/poly-mcp/PolyMCP)** - ⭐ 165
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1540. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 165
   A curated list of OSINT MCP servers. Pull requests are welcomed!

1541. **[data-verify-mcp](https://github.com/CCCpan/data-verify-mcp)** - ⭐ 164
   中国数据核验 MCP Server | 身份核验/企业查询/车辆信息/OCR识别/风险评估 | 10个Tool覆盖5大类 | 微信: chenganp | 邮箱: 345048305@qq.com

1542. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 164
   Codex Mcp Server 

1543. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 163
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1544. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 163
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1545. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 163
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1546. **[mcp-codex-dev](https://github.com/FYZAFH/mcp-codex-dev)** - ⭐ 163
   MCP Server for Codex CLI integration - stateful code writing and review workflows

1547. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 163
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1548. **[recall](https://github.com/joseairosa/recall)** - ⭐ 163
   Persistent cross-session memory for Claude & AI agents. Self-host on Redis/Valkey, or use the managed SaaS at recallmcp.com.

1549. **[harnss](https://github.com/OpenSource03/harnss)** - ⭐ 163
   Open-source, desktop client/UI build to harness Claude Code, Codex and any other Agent accepting Agent Client Protocol. Run multiple AI coding agents side by side with rich tool visualization, MCP integrations, built-in terminal, git, browser and just about anything else you may need.

1550. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 162
   MCP server for searching and querying PubMed medical papers/research database

1551. **[Axon.MCP.Server](https://github.com/ali-kamali/Axon.MCP.Server)** - ⭐ 162
   Transform your codebase into an intelligent knowledge base for AI-powered development with Cursor IDE, Google AntiGravity, and MCP-enabled assistants

1552. **[flutter-skill](https://github.com/ai-dashboad/flutter-skill)** - ⭐ 162
   AI-powered E2E testing for 10 platforms. 253 MCP tools. Zero config. Works with Claude, Cursor, Windsurf, Copilot. Test Flutter, React Native, iOS, Android, Web, Electron, Tauri, KMP, .NET MAUI — all from natural language.

1553. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 161
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1554. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 161
   StarRocks MCP (Model Context Protocol) Server

1555. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 161
   A redmine MCP server covering close to 100% of redmines API

1556. **[refref](https://github.com/amicalhq/refref)** - ⭐ 161
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1557. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 160
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1558. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 160
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1559. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 160
   MCP (Model Context Protocol) server for Weaviate

1560. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 160
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1561. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 160
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1562. **[comfy-pilot](https://github.com/ConstantineB6/comfy-pilot)** - ⭐ 160
   MCP server + embedded terminal that lets Claude Code see and edit your ComfyUI workflows

1563. **[bear-notes-mcp](https://github.com/vasylenko/bear-notes-mcp)** - ⭐ 160
   MCP Server for Bear note taking app available as Claude Desktop extension or standalone server for any other AI tool

1564. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 159
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1565. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 159
   MCP Server for AI Summarization

1566. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 159
   Model Context Protocol (MCP) server for constraint optimization and solving"

1567. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 159
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1568. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 159
   MariaDB MCP (Model Context Protocol) server implementation

1569. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 159
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1570. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1571. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 158
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1572. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 158
   Simple Slackbot MCP Client

1573. **[claude-code-open](https://github.com/kill136/claude-code-open)** - ⭐ 158
   Open source AI coding platform with Web IDE, multi-agent system, 37+ tools, MCP protocol. MIT licensed.

1574. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 158
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1575. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 158
   Scrapeless Mcp Server

1576. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 158
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1577. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 158
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1578. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 158
   Vector-search powered agent memory MCP server

1579. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 158

1580. **[notebooklm-skill](https://github.com/claude-world/notebooklm-skill)** - ⭐ 158
   NotebookLM does the research, Claude writes the content. Research → Synthesis → Content Creation → Publishing. Claude Code Skill + MCP Server.

1581. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 157
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1582. **[agentseal](https://github.com/AgentSeal/agentseal)** - ⭐ 157
   Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for supply chain attacks, test prompt injection resistance, and audit live MCP servers for tool poisoning.

1583. **[OpenCode-Everything-You-Need-to-Know](https://github.com/wesammustafa/OpenCode-Everything-You-Need-to-Know)** - ⭐ 157
   The ultimate all-in-one guide to mastering OpenCode. From installation, Zen model router setup, TUI mastery, commands, skills, agents, workflows, automation, and integrations, to MCP servers, plugins, packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for OpenCode mastery.

1584. **[CyberStrike](https://github.com/CyberStrikeus/CyberStrike)** - ⭐ 157
   AI-powered offensive security agent. Autonomous pentesting with 13+ specialized agents, 120+ OWASP test cases, 15+ LLM providers, and Bolt remote tool servers. Your AI red team.

1585. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 156
   An MCP server for fetching URLs / Youtube video transcript.

1586. **[refref](https://github.com/refrefhq/refref)** - ⭐ 156
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1587. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 156
   A Model Context Protocol server for MySQL database operations

1588. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 156
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1589. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 155
   Instagram Direct messages MCP

1590. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 155

1591. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 155
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1592. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 155
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1593. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 155
   AI-powered security operations for Wazuh SIEM—use any MCP-compatible client to ask security questions in plain English. Faster threat detection, incident triage, and compliance checks with real-time monitoring and anomaly spotting. Production-ready MCP server for conversational SOC workflows.

1594. **[ironcurtain](https://github.com/provos/ironcurtain)** - ⭐ 155
   A secure* runtime for autonomous AI agents. Policy from plain-English constitutions. (*https://ironcurtain.dev)

1595. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 155

1596. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 155
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1597. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 154
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1598. **[bocha-search-mcp](https://github.com/BochaAI/bocha-search-mcp)** - ⭐ 154
   Bocha Search MCP Server.

1599. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 154
   ChatGPT Copilot Extension for Visual Studio Code

1600. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 154
   A simple and performant Model Context Protocol framework for Python.

1601. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 154
   Deep Research for crypto - free & fully local

1602. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 154
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1603. **[turbo-flow](https://github.com/marcuspat/turbo-flow)** - ⭐ 154
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI subagents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1604. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 154
   A simple MCP server to search for documentation (tutorial)

1605. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 154
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1606. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 154
   MCP server for Unreal Engine 5

1607. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 153
   :octocat: GitHub Emoji for C#, dotnet and beyond

1608. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 153
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1609. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 153
   Manage Your Kubernetes Cluster with k8s mcp-server

1610. **[elementor-mcp](https://github.com/msrbuilds/elementor-mcp)** - ⭐ 153
   WordPress plugin that turns Elementor into an MCP server — 97 AI-ready tools for building, editing, and managing page designs programmatically.

1611. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 153
   小红书MCP服务器 | 秒级工具调用执行，笔记用户搜索、通知消息监控等；打造2026最简单、最快速、最精准、最好用的小红书MCPServer！

1612. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 152
   Make MCP Server

1613. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 152
   A gateway demo for MCP SSE Server

1614. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 152
   MCP Server for using any LLM as a Tool

1615. **[agentanycast](https://github.com/AgentAnycast/agentanycast)** - ⭐ 152
   Connect AI agents across any network — zero config, encrypted, skill-based routing

1616. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 152

1617. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 152
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1618. **[relay](https://github.com/prism-php/relay)** - ⭐ 152
   An MCP client tool for Prism

1619. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 152
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1620. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 151
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1621. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 151
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1622. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 151
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1623. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 151
    QMT-MCP 模块化量化交易助手

1624. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 151
   A Model Context Protocol server for Hopper Disassembler

1625. **[agent-trade-kit](https://github.com/okx/agent-trade-kit)** - ⭐ 151
   OKX trading MCP server — connect AI agents to spot, swap, futures, options & grid bots via the Model Context Protocol.  

1626. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 150
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1627. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1628. **[eion](https://github.com/eiondb/eion)** - ⭐ 150
   Shared Memory Storage for Multi-Agent Systems

1629. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 150
   Toolkit for Coding Agents to work reliably with repo of any size.

1630. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 150
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1631. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 150
   Serper MCP Server supporting search and webpage scraping

1632. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 149
   Dynamically expose tools from proxied servers based on an Agent Persona

1633. **[Express-REST-API-and-MCP-Server-Framework](https://github.com/iolufemi/Express-REST-API-and-MCP-Server-Framework)** - ⭐ 149
   Express REST API and MCP Server Framework is a comprehensive development framework for building RESTful APIs and MCP servers with Express.js. It provides a complete template for creating production-ready APIs using Node.js, Express, Mongoose (MongoDB), and Sequelize (SQL databases).

1634. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 149
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1635. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1636. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 149
   MCP server to download entire websites

1637. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 149
   Catch MCP server issues before your agents do.

1638. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 149
   Desktop APP for Discover and Install MCP Servers

1639. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 149
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1640. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 149
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1641. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 149
   Salesforce MCP Server

1642. **[PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio)** - ⭐ 149
   Free, open-source SQL Server execution plan analyzer — cross-platform GUI + CLI with 30 analysis rules, missing index detection, SSMS extension. Built-in MCP server for AI-assisted plan review.

1643. **[scrumboy](https://github.com/markrai/scrumboy)** - ⭐ 149
   a self-hosted project management & Kanban solution + Instant shareable boards

1644. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 148
   MCP server for discord bot

1645. **[plan-cascade](https://github.com/Taoidle/plan-cascade)** - ⭐ 148
   AI-powered cascading development framework. Decompose complex projects into parallel executable tasks with auto-generated PRDs, design docs, and multi-agent collaboration (Claude Code, Codex, Aider).

1646. **[kom](https://github.com/weibaohui/kom)** - ⭐ 148
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1647. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 148
   A Model Context Protocol server for calculating.

1648. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 148
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1649. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 148
   An MCP Server for Ollama

1650. **[Charles-mcp](https://github.com/heizaheiza/Charles-mcp)** - ⭐ 148
   Charles Proxy MCP server with live capture and structured traffic analysis

1651. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 148
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1652. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 148
   MCP server for Mikrotik

1653. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 147
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1654. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 147
   Async Python client for the Model Context Protocol with interactive CLI and reactive Web UI, connecting AI models to MCP servers via stdio and SSE

1655. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 147
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1656. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 147
   Enable AI Agents to Control Unity

1657. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 147
   A PubMed MCP server.

1658. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 147
   Connect any Open Data to any LLM with Model Context Protocol.

1659. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 147
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1660. **[regenerator2000](https://github.com/ricardoquesada/regenerator2000)** - ⭐ 147
   An interactive disassembler for the CPU 6502, focused mostly on Commodore 8-bit computers. Features a TUI with modern features like x-ref, undo/redo, arrows, keyboard-driven, mcp server, VICE debugger and more!

1661. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 146
   Model Context Protocol server implementation for Figma API

1662. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 146
   An MCP server that provides access to Postman.

1663. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 146
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1664. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 146
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1665. **[aai-gateway](https://github.com/gybob/aai-gateway)** - ⭐ 145
   Install MCP servers and skills once, share across all your AI agents — with 90% less context overhead.

1666. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust 

1667. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 145
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1668. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 145
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1669. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 145
   MCP Server connecting to Perplexity Comet browser

1670. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 145
   MSSQL Server MCP implementation written in C#

1671. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 145
   MCP server that provides access to Chinese stock market data using akshare-one

1672. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 145
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1673. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 145
   MCP server for interaction with Bitwarden.

1674. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 145
   Raindrop MCP Server

1675. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 145
   Comprehensive MCP server exposing dozens of capabilities to AI agents: multi-provider LLM delegation, browser automation, document processing, vector ops, and cognitive memory systems

1676. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 145
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12+.

1677. **[mengram](https://github.com/alibaizhanov/mengram)** - ⭐ 145
   Human-like memory for AI agents — semantic, episodic & procedural. Experience-driven procedures that learn from failures. Free API, Python & JS SDKs, LangChain & CrewAI integrations.

1678. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 144
   A MCP Server for creating Powerpoint Presentations

1679. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

1680. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 144
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1681. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 144
   Isaac Simulation MCP Extension and Server

1682. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 144
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1683. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 144
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1684. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 143
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1685. **[deterministic-agent-control-protocol](https://github.com/elliot35/deterministic-agent-control-protocol)** - ⭐ 143
   Governance gateway for AI agents — bounded, auditable, session-aware control with MCP proxy, shell proxy & HTTP API. Works with Cursor, Claude Code, Codex, and any MCP-compatible agent.

1686. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 143
   MCP server implementation for Google's Gemini API

1687. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

1688. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 143
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1689. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 143
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1690. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 142
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1691. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1692. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 142
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1693. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 142
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1694. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 142
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1695. **[mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** - ⭐ 142
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1696. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 142
   Model Context Protocol (MCP) with TikTok integration

1697. **[domscribe](https://github.com/patchorbit/domscribe)** - ⭐ 142
   Domscribe is a pixel-to-code development tool that bridges the gap between running web applications and their source code.

1698. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1699. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1700. **[meta_skill](https://github.com/Dicklesworthstone/meta_skill)** - ⭐ 141
   Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic search, bandit-optimized suggestions, and MCP integration

1701. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 141
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1702. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 141
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1703. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 140
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1704. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 140

1705. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 140
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1706. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 140
   MCP server for Israel Government Data

1707. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 140
   Model Context Protocol (MCP) server for the Zotero API, in Python

1708. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 140
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1709. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 140
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1710. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 140
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1711. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 139
   Graphiti MCP Server

1712. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 139
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1713. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 139
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1714. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 139
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

1715. **[forgemax](https://github.com/postrv/forgemax)** - ⭐ 139
   Code Mode inspired local sandboxed MCP Gateway - collapses N servers x M tools into 2 tools (~1,000 tokens)

1716. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 138
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1717. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 138
   Simple MCP Server Implementation

1718. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 138
   MCP server for seamless document format conversion and processing

1719. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 138
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1720. **[AI-company](https://github.com/CronusL-1141/AI-company)** - ⭐ 138
   AI Team OS — Multi-Agent Team Operating System for Claude Code. 40+ MCP tools, 22 agent templates, task wall, meeting system, dashboard.

1721. **[claude-code-karma](https://github.com/JayantDevkar/claude-code-karma)** - ⭐ 138
   Dashboard for monitoring claude code sessions. 

1722. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 138
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1723. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 138
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1724. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 138
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1725. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 137
   Model Context Protocol Server for Swift

1726. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 137
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1727. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 137
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1728. **[QuickDesk](https://github.com/barry-ran/QuickDesk)** - ⭐ 137
   QuickDesk is the first AI-native remote desktop — an open-source, free application with a built-in MCP (Model Context Protocol) Server that lets any AI agent see and control remote computers.

1729. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 136
   mcp server for gitingest

1730. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 136
      Convert any MCP server into a Claude Skill with 90% context savings

1731. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 136
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

1732. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 136
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1733. **[antigravity-link-extension](https://github.com/cafeTechne/antigravity-link-extension)** - ⭐ 136
   Mobile companion for Google's Antigravity IDE. Mirror AI sessions on your phone, send messages, stop generation, automate via 9 MCP tools or OpenAPI.

1734. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 136
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1735. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 135
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1736. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 135
   MCP server for interacting with the Aseprite API

1737. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 135
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1738. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 135
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1739. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 135
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1740. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 135
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1741. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 135
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1742. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 134
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1743. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1744. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 134
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1745. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 134
   A powerful MCP server for intelligently reading Java source code (For Jar and local project).

1746. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1747. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1748. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 133
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1749. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 132
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1750. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 132
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1751. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 132
   Docker Hub MCP Server

1752. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 132
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

1753. **[orchestkit](https://github.com/yonatangross/orchestkit)** - ⭐ 132
   The Complete AI Development Toolkit for Claude Code — 89 skills, 31 agents, 99 hooks. Production-ready patterns for full-stack development.

1754. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 132
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1755. **[mcp-bridge](https://github.com/firekula/mcp-bridge)** - ⭐ 132
   这是一个为 Cocos Creator 设计的 MCP (Model Context Protocol) 桥接插件，用于连接外部 AI 工具与 Cocos Creator 编辑器，实现对场景、节点等资源的自动化操作。

1756. **[magg](https://github.com/sitbon/magg)** - ⭐ 131
   Magg: The MCP Aggregator

1757. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 131

1758. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 131
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1759. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 131
   Simple API & React framework, fully type safe, OpenAPI, RSC, MCP, type safe client, streaming with SSE

1760. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 130
   BrowserStack's Official MCP Server

1761. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 130
   High-performance CCXT MCP server for cryptocurrency exchange integration

1762. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 130
   It's time to push beyond MCP Servers... Right?

1763. **[openwebui-extensions](https://github.com/Fu-Jie/openwebui-extensions)** - ⭐ 130
   A collection of enhancements, plugins, and prompts for Open WebUI, developed and curated for personal use to extend functionality and improve experience.

1764. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 130
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1765. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 129
   A modular MCP server that provides commonly used developer tools for AI coding agents

1766. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 129
   A collection of crypto MCP servers.

1767. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 129
   Conversion from Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines, and autonomous Excel reading and writing by AI agents through MCP integration.

1768. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 129
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

1769. **[indonesia-gov-apis](https://github.com/suryast/indonesia-gov-apis)** - ⭐ 129
   🇮🇩 50+ Indonesian Government APIs & Data Sources — BPS, OJK, BPJPH, BPOM, Bank Indonesia, IDX, BMKG + MCP servers. Python examples, scraping patterns, and practical gotchas.

1770. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 129
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1771. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1772. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1773. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 128
   Intelligent spec workflow management MCP server

1774. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 128
   a private MCP server for accessing Linear

1775. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 128
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1776. **[linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server)** - ⭐ 128
   🔗 A Model Context Protocol (MCP) server for LinkedIn — search people, companies, and jobs, scrape profiles, and get structured data via any MCP-compatible AI client.

1777. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 128
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1778. **[mcp-ts-core](https://github.com/cyanheads/mcp-ts-core)** - ⭐ 128
   Agent-native TypeScript framework for building MCP servers. Build tools, not infrastructure.

1779. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 127
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1780. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1781. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 127
   MCP server for understanding AWS spend

1782. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

1783. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 127
   Portainer MCP server

1784. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 127
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1785. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 127
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

1786. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 127
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1787. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 127
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1788. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 127
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

1789. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1790. **[sysplant](https://github.com/x42en/sysplant)** - ⭐ 126
   Your Windows syscall hooking factory - feat Canterlot's Gate - All accessible over MCP

1791. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 126
   Buttplug.io Model Context Protocol (MCP) Server

1792. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 126
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1793. **[reddit-mcp-server](https://github.com/eliasbiondo/reddit-mcp-server)** - ⭐ 126
   🔗 A zero-config Model Context Protocol (MCP) server for Reddit — search posts, browse subreddits, scrape user activity, and get structured data via any MCP-compatible AI client. No API keys or authentication needed.

1794. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 126
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1795. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 125
   Dart AI Model Context Protocol (MCP) server

1796. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1797. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 125
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1798. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 125
   unofficial mcp server for cloudflare api

1799. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 125
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

1800. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 125
   A Model Context Protocol (MCP) for Jupyter Notebook

1801. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 125
   A Model Context Protocol Server to manipulate *.xcodeproj

1802. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 125
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1803. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 125
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1804. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1805. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 124
   🐉 The fast, PHP way to build MCP servers

1806. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 124
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1807. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 124
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1808. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 124
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1809. **[gm-exec](https://github.com/AnEntrypoint/gm-exec)** - ⭐ 124
   wanna develop an app ❓

1810. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 123
   wanna develop an app ❓

1811. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 123
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1812. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 123
   MCP server for Google Tag Manager

1813. **[ASI](https://github.com/vNeeL-code/ASI)** - ⭐ 123
   Android ✧ Gemma Integration into Android System Intelligence

1814. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 123
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1815. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 123
   A Model Context Protocol server that provides access to BigQuery

1816. **[mcp-gm](https://github.com/AnEntrypoint/mcp-gm)** - ⭐ 122
   wanna develop an app ❓

1817. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 122
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

1818. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 122
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1819. **[env-doctor](https://github.com/mitulgarg/env-doctor)** - ⭐ 122
   Debug your GPU, CUDA, and AI stacks across local, Docker, and CI/CD (CLI and MCP server)

1820. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 122
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1821. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 122
   An MCP server that provides LLMs with the latest stable package versions when coding

1822. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 122
   blazigly fast gRPC/MCP client & server implementation in zig

1823. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1824. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 121
   MCP server implementation for n8n workflow automation

1825. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 121

1826. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 121
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1827. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 121
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1828. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 121
   Model Context Protocol for Actual Budget API

1829. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 121
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1830. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

1831. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 120
   Google Sheets MCP Server 📊🤖

1832. **[mcp](https://github.com/frappe/mcp)** - ⭐ 120
   Frappe MCP allows Frappe apps to function as MCP servers

1833. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 120
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1834. **[mcp](https://github.com/taskade/mcp)** - ⭐ 120
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1835. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 120
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1836. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 120
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1837. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 119
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1838. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 119

1839. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 119
   TypeScript template for building Model Context Protocol (MCP) servers. Ships with declarative tools/resources, pluggable auth, multi-backend storage, OpenTelemetry observability, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1840. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 119
   MCP server for Shodan — search internet-connected devices, IP reconnaissance, DNS lookups, and CVE/CPE vulnerability intelligence. Works with Claude Code, Codex, Gemini CLI, and Claude Desktop.

1841. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 118
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1842. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

1843. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 118
   MCP Server for PolyMarket API

1844. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 118
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

1845. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 118
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1846. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 118
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via CLI wrappers

1847. **[claudeus-wp-mcp](https://github.com/deus-h/claudeus-wp-mcp)** - ⭐ 118
   Claudeus WordPress MCP Server

1848. **[claude-emporium](https://github.com/Vvkmnn/claude-emporium)** - ⭐ 117
   🏛 [UNDER CONSTRUCTION] A (roman) claude plugin marketplace 

1849. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 117
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1850. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 117
   An MCP server for InterviewReady

1851. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 117
   A proxy to use HTTP/SSE MCPs from STDIO clients

1852. **[kodit](https://github.com/helixml/kodit)** - ⭐ 117
   👩‍💻 MCP server to index external repositories

1853. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 117
   It's an MCP server... for Outline (the documentation platform!)

1854. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 117
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

1855. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 117
   MCP server for token-efficient large document analysis via the use of REPL state

1856. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 117
   A Google Tasks Model Context Protocol Server for Claude

1857. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 116
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

1858. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 116
   MCP for 1C:EDT

1859. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 116
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1860. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 116
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under  MIT License.

1861. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 116
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1862. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 116
   MCP server for VirusTotal API — analyze URLs, files, IPs, and domains with comprehensive security reports, relationship analysis, and pagination support.

1863. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 116
   Model Context Protocol (MCP) server for the Webflow Data API.

1864. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 115
   Fast and super efficient Minecraft Server written in C++

1865. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 115
   Azure API Management as AI Gateway to Remote MCP servers.

1866. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 115
   MCP Server for working with large Oracle databases

1867. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 115
   Getting Started with Remote MCP Servers using Azure Functions (Python)

1868. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1869. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 114
   Swagger to MCP server

1870. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 114
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1871. **[nitrostack](https://github.com/nitrocloudofficial/nitrostack)** - ⭐ 114
   The full-stack TypeScript framework to build, test, and deploy production-ready MCP servers and AI-native apps.

1872. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 114
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1873. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 114
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1874. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1875. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

1876. **[AgenticGoKit](https://github.com/AgenticGoKit/AgenticGoKit)** - ⭐ 113
   Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent agents. LLM-agnostic, event-driven, with multi-agent workflows, MCP tool discovery, and production-grade observability.

1877. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 113
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search, News Search and LLM Context Search capabilities

1878. **[modex](https://github.com/theronic/modex)** - ⭐ 113
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1879. **[mcp-armor](https://github.com/aira-security/mcp-armor)** - ⭐ 113
   MCP Armor continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1880. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1881. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 112
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1882. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 112

1883. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 112
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1884. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 112
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1885. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 112
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1886. **[charlotte](https://github.com/TickTockBent/charlotte)** - ⭐ 112
   Token-efficient browser MCP server — structured web pages for AI agents, not raw accessibility dumps

1887. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1888. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

1889. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1890. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1891. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

1892. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 111

1893. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 111
   Open Source MCP Servers for Scientific Research

1894. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 111
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

1895. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 111
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1896. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 110
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1897. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 110
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1898. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1899. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

1900. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 110
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1901. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 110
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

1902. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 110
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1903. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1904. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 110
   MCP for semantic code search & navigation that reduces token waste

1905. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 110
   MCP Client Implementation using Python, LangGraph and Gemini

1906. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

1907. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1908. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 109
   The coding agent for professionals

1909. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 109
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

1910. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 109
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

1911. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 109
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

1912. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 109
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1913. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 109
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1914. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 109
   MCP server for *arr media management suite

1915. **[Pare](https://github.com/Dave-London/Pare)** - ⭐ 109
   Dev tools, optimized for agents. Structured, token-efficient MCP servers for git, test runners, npm, Docker, and more.

1916. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1917. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1918. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

1919. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 108
   An MCP client for Node.js.

1920. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 108
   Payload CMS MCP Server

1921. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 108
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1922. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 108
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1923. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 108
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1924. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 107
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1925. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

1926. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

1927. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 107
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

1928. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 107
   fast, secure c# runner

1929. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 107
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

1930. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 107
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1931. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 107
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1932. **[prism-mcp](https://github.com/dcostenco/prism-mcp)** - ⭐ 107
   The Mind Palace for AI Agents — a Cognitive Architecture with Hebbian learning, ACT-R spreading activation, multi-hop causal reasoning, uncertainty-aware rejection gates, adversarial evaluation, Dark Factory pipelines, persistent memory & visual dashboard.

1933. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 107
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1934. **[forge-orchestrator](https://github.com/nxtg-ai/forge-orchestrator)** - ⭐ 106
   Forge Orchestrator: Multi-AI task orchestration. File locking, knowledge capture, drift detection. Rust.

1935. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 106
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

1936. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 106
   An md file as a chat interface and editable history in one.

1937. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 106
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1938. **[VibeUE](https://github.com/kevinpbuckley/VibeUE)** - ⭐ 106
   Unreal Engine Vibe Coding tool

1939. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 105
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1940. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

1941. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

1942. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

1943. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 105
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

1944. **[linggen-memory](https://github.com/linggen/linggen-memory)** - ⭐ 105
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1945. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 105
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref. 

1946. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 105
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1947. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 105
   MCP server for natural language interaction with Power BI datasets

1948. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 105
   From Java Dev to AI Engineer: Spring AI Fast Track

1949. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 105
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1950. **[MiniClaw](https://github.com/8421bit/MiniClaw)** - ⭐ 105
   🦞 A Digital Life Embryo for your MCP Client. An intelligent micro-kernel with Nociception, Memory Apoptosis, and a Curiosity Drive. Evolve your AI Copilot into a sentient partner for Claude Desktop, Qoderwork, Cursor, and beyond.

1951. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1952. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 105
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1953. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1954. **[yuque-mcp-server](https://github.com/yuque/yuque-mcp-server)** - ⭐ 105
   Yuque MCP Server - Model Context Protocol server for Yuque API

1955. **[rails-ai-context](https://github.com/crisnahine/rails-ai-context)** - ⭐ 105
   Auto-introspect your Rails app and expose it to AI assistants via MCP. 39 tools, zero config, works with Claude, Cursor, Copilot, and any MCP client.

1956. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

1957. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1958. **[linggen](https://github.com/linggen/linggen)** - ⭐ 104
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1959. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1960. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 104
   Official Vectorize MCP Server

1961. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 104
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1962. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 104
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1963. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 104
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1964. **[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)** - ⭐ 104
   Curated awesome list for OpenClaw (formerly Moltbot/Clawdbot): skills, plugins, memory systems, MCP tools, deployment stacks, ecosystem platforms, and developer tooling.

1965. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1966. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1967. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

1968. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1969. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1970. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 103
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

1971. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 103
   AlibabaCloud CloudOps MCP Server

1972. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 103
   Wanaku MCP Router

1973. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 103
   Excel MCP Server & CLI - 23 tools, 214 operations for AI-powered Excel automation via COM API

1974. **[Gopeak-godot-mcp](https://github.com/HaD0Yun/Gopeak-godot-mcp)** - ⭐ 103
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

1975. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1976. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 102
   go doc mcp server

1977. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 102
   Quickly screenshots webpages and converts to an LLM friendly size

1978. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 102
   Collection of examples of how to use Model Context Protocol with AWS.

1979. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 102
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1980. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 102
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1981. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 102
    Official Go implementation of the UTCP 

1982. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 102
   This is a Ruby implementation of MCP (Model Context Protocol) client

1983. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 102
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1984. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 102
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1985. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 102
   Rails Engine with MCP compliant Spec.

1986. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1987. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 101
   Memory and context manager just works.

1988. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 101
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

1989. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 101
   Node.js Client Implementation for Model Context Protocol (MCP)

1990. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 101
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, Slides and Calendar. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

1991. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1992. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1993. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1994. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1995. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1996. **[mpm-vibe-coding](https://github.com/halflifezyf2680/mpm-vibe-coding)** - ⭐ 100
   MPM is an MCP context-engineering layer for Vibe Coding, focused on three delivery bottlenecks: context loss, uncontrolled changes, and non-verifiable outcomes.

1997. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 100
   LangGraph AI Repository

1998. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 100
   MCP server for persistent context management in AI coding assistants

1999. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 100
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

2000. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 100
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

2001. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 100
   first gemini based desktop client for MCP

2002. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 100
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

2003. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 99
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

2004. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

2005. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

2006. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

2007. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

2008. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 99
   lapras.com 公式MCP Server

2009. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 99
   Your AI Coding Assistant's Long-Term Memory

2010. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 99
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

2011. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 99
   MCP Server for use with Monarch Money

2012. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 99
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

2013. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 99
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

2014. **[MySearch-Proxy](https://github.com/skernelx/MySearch-Proxy)** - ⭐ 99
   Unified search MCP, proxy console, and skill for Tavily, Firecrawl, and Social / X.

2015. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 99
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

2016. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 98
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

2017. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

2018. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 98
   MCP Server for AI automation of the PlayCanvas Editor

2019. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 98
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

2020. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

2021. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 98
   Context7 MCP Server for Zed

2022. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 98
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

2023. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 98
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

2024. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 98
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

2025. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 97
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

2026. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 97
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

2027. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 97
   claude mcp sse demo with server and client(cli、web)

2028. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 97
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

2029. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 97
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

2030. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 97
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

2031. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 97
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

2032. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

2033. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 96
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

2034. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 96
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

2035. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 96
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

2036. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 96
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

2037. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 96
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

2038. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 96
   Portable , scalable , secure AI Agents

2039. **[NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform)** - ⭐ 96
   AI-powered network automation via Netbox and Model Context Protocol (MCP). 178 tools for multi-vendor infrastructure   management, self-healing agents, drift detection, and a real-time web dashboard.

2040. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 96
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

2041. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 95
   xiaohongshu-mcp-python 是一个基于现代 Python 技术栈开发的小红书内容自动化发布工具，通过 Model Context Protocol（MCP）协议为 AI 客户端提供强大的小红书操作能力。项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持 HTTP/HTTPS 链接，为用户提供灵活的内容发布方案。  该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的 MCP 接口，用户可以轻松地将小红书操作能力集成到各种 AI 工作流中，实现智能化的内容管理

2042. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 95
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

2043. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 95
   MCP Server for Linux Scheduler Management and Auto optimization

2044. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 95
   Collection of resources to help AI agents build better with Sanity.

2045. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 95
   MCP Server for connecting to the Meta Marketing API

2046. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 95
   A Model Context Protocol (MCP) server for square

2047. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 95
   MCP server for AI image generation and editing with automatic prompt optimization and quality presets (fast/balanced/quality). Powered by Gemini (Nano Banana 2 & Pro).

2048. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 95
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

2049. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 94
   Sandbox for Agents 

2050. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 94
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

2051. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 94
   Interact with all three types of generative UI, all in one interface

2052. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 94
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

2053. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 94
   A Model Context Protocol (MCP) server for working with TradingView PineScript

2054. **[firefox-devtools-mcp](https://github.com/mozilla/firefox-devtools-mcp)** - ⭐ 94
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2055. **[us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp)** - ⭐ 93
   MCP server + TypeScript SDK for 40+ U.S. government data APIs — 250+ tools. Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, and many more. Works with VS Code Copilot, Claude Desktop, Cursor.

2056. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

2057. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

2058. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 93
   Model Context Protocol server for Replicate's API

2059. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

2060. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 93
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

2061. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 93
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

2062. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 93
   Octopus Deploy Official MCP Server

2063. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 93
   MCPcat is an analytics platform for MCP server owners 🐱.

2064. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 93
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

2065. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 93
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

2066. **[obsidian-web-mcp](https://github.com/jimprosser/obsidian-web-mcp)** - ⭐ 93
   Secure remote MCP server for Obsidian vaults -- access your notes from Claude, your phone, or any MCP client, anywhere. OAuth 2.0 auth, Cloudflare Tunnel, atomic writes safe for Obsidian Sync.

2067. **[winremote-mcp](https://github.com/dddabtc/winremote-mcp)** - ⭐ 93
   Windows Remote MCP Server — 40+ tools for desktop automation, process management, file operations via FastMCP

2068. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 92
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

2069. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

2070. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 92
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

2071. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 92
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

2072. **[agent-bridge](https://github.com/raysonmeng/agent-bridge)** - ⭐ 92
   A local bridge for bidirectional collaboration between Claude Code and Codex. 连接 Claude Code 与 Codex 的本地实时协作桥接工具。

2073. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

2074. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

2075. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 91
   A Model Context Protocol (MCP) server for querying the CVE-Search API

2076. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 91
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

2077. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 91
   Headless IDA Pro binary analysis via Model Context Protocol

2078. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 91
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

2079. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 90
   A model-context-protocol server for molecules.

2080. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 90
   A Model Context Protocol server that provides knowledge graph management capabilities.

2081. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 90
   Official Oxylabs MCP integration

2082. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 90
   Model Context Protocol for YNAB (you need a budget)

2083. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 90
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

2084. **[purple](https://github.com/erickochen/purple)** - ⭐ 90
   Terminal SSH client with MCP support for AI agent integration, instant search, cloud sync from 16 providers, Docker/Podman container management, visual file transfer and password management. Edits ~/.ssh/config with round-trip fidelity.

2085. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 90
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

2086. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 89
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

2087. **[identity](https://github.com/agntcy/identity)** - ⭐ 89
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2088. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 88
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

2089. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

2090. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 88
   高德地图MCP Server，支持stdio, sse和streamable-http

2091. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 88
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

2092. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 88
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

2093. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 88
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

2094. **[mcp-dock](https://github.com/OldJii/mcp-dock)** - ⭐ 88
   A cross-platform MCP Server manager for Cursor, Claude, Windsurf, Zed & TRAE. Features one-click installation, multi-client sync, and a curated registry of Official & Smithery servers.

2095. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

2096. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

2097. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

2098. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 87
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

2099. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 87
   Ragie Model Context Protocol Server

2100. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 87
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

2101. **[sdl-mcp](https://github.com/GlitterKill/sdl-mcp)** - ⭐ 87
   SDL-MCP (Symbol Delta Ledger MCP Server) is a cards-first context system for coding agents that saves tokens and improves context.

2102. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 87
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

2103. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 87
   The official MCP server for SurrealDB

2104. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 87
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

2105. **[ogham-mcp](https://github.com/ogham-mcp/ogham-mcp)** - ⭐ 87
   Shared memory MCP server — persistent, searchable, cross-client

2106. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 86
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

2107. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

2108. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

2109. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

2110. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

2111. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 86
   CLI & API for MCP management

2112. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

2113. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 86
   MCP server for AI-assisted development of CAP applications

2114. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 86
   WeChat-MCP: let Claude/ChatGPT and other AI assistants read and reply to WeChat for you

2115. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 86
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

2116. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 86
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

2117. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 86
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

2118. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 85
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

2119. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

2120. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

2121. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 85
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

2122. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 85
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

2123. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 85
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

2124. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 85
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

2125. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 85
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

2126. **[unity-mcp-server](https://github.com/AnkleBreaker-Studio/unity-mcp-server)** - ⭐ 85
   Unity MCP Server — 268 tools for AI-assisted game development. Connect Claude, Cursor, or any MCP client to Unity Editor & Unity Hub. Scene management, GameObjects, components, builds, profiling, Shader Graph, Amplify, terrain, physics, NavMesh, animation, MPPM multiplayer & more. Free & open source by AnkleBreaker Studio.

2127. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

2128. **[spiceflow-framework](https://github.com/remorses/spiceflow-framework)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

2129. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 84
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

2130. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 84
   a mcp server to manage github project's functionality 

2131. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 84
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

2132. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 84
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

2133. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 84
   A WooCommerce (MCP) Model Context Protocol server

2134. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 84
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

2135. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

2136. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

2137. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

2138. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

2139. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 83
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

2140. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 83
   The EMBL-EBI Ontology Lookup Service (OLS)

2141. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 83
   A GitHub MCP Server extension for Zed

2142. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 83
   A complete MCP server template that include vitamins (oauth authentication included)

2143. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 83
   Model Context Protocol (MCP) Server for the Keboola Platform

2144. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 83
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

2145. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 83
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

2146. **[tradingview-chart-mcp](https://github.com/ertugrul59/tradingview-chart-mcp)** - ⭐ 83
   MCP server that captures TradingView chart images via Selenium — supports any ticker/interval with browser pooling for concurrent performance

2147. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 82
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

2148. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 82
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

2149. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

2150. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 82
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

2151. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 82
   Model Context Protocol (MCP) CLI server template for Rust

2152. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 82
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

2153. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 82
   MCP Server to previewing mermaid diagrams with live reload

2154. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 82
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

2155. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 82
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

2156. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 82
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

2157. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 82
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

2158. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 82
   Open Models MCP for Blender Using Ollama

2159. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 82
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

2160. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 82
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2161. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

2162. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

2163. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

2164. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 81
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

2165. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 81
   OpenAPI specification MCP server.

2166. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 81
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

2167. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 81
   MCP server for Slither static analysis of Solidity smart contracts

2168. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 81
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

2169. **[agenticmail](https://github.com/agenticmail/agenticmail)** - ⭐ 81
   Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically

2170. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

2171. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 80
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

2172. **[ophis](https://github.com/njayp/ophis)** - ⭐ 80
   Transform any Cobra CLI into an MCP server

2173. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 80
   Build agentic-MCP servers by composing existing MCP tools.

2174. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 80
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

2175. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 80
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

2176. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 80
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

2177. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 79
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

2178. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

2179. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

2180. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

2181. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 79
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

2182. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 79
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

2183. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 79
   MCP server that can execute terminal commands

2184. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 79
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

2185. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 79
   A MCP server for Django applications, inspired by Laravel Boost.

2186. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 79
   Model Context Protocol server for OpenStreetMap data

2187. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 79
   A Model Context Protocol server for Zendesk

2188. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 79
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

2189. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 79
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

2190. **[aivectormemory](https://github.com/Edlineas/aivectormemory)** - ⭐ 79
   aivectormemory 是一款基于 Model Context Protocol (MCP) 开发的OpenClaw、OpenCode、ClaudeCodeAI记忆管理工具。它专门为 Claude、OpenCode、Cursor 和 主流IDE 编程工具设计，通过向量数据库技术解决 AI 在不同对话会话中「健忘」的问题。aivectormemory: A lightweight MCP Server enabling persistent, cross-session memory for AI-powered IDEs via vector search.

2191. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 79
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2192. **[godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** - ⭐ 79
   MCP server for full Godot 4.x engine control — 149 tools for AI-driven game development

2193. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 78
   MCP Server for Bing Search API

2194. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 78
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

2195. **[transit-agent](https://github.com/ruby-verma/transit-agent)** - ⭐ 78
   This guide demonstrates how to build an Agentic AI system using Google's Agent Development Kit (ADK) and the Model Context Protocol (MCP).

2196. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 78
   An extension of MCP for SillyTavern.

2197. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 78
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2198. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 78
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

2199. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 78
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

2200. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 77
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2201. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 77
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

2202. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

2203. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

2204. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

2205. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

2206. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2207. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 77
    An MCP server that provides LLMs access to other LLMs

2208. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 77
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

2209. **[agent-security-scanner-mcp](https://github.com/sinewaveai/agent-security-scanner-mcp)** - ⭐ 77
   Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

2210. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 77
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

2211. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 77
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

2212. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 77
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

2213. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 77
   Model Context Protocol implementation for retrieving codebases using RepoMix

2214. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 77
   Open-source FRED MCP Server (Federal Reserve Economic Data)

2215. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 76
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

2216. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 76
   MCP server for Google Search integration using Gemini's built-in search capabilities

2217. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

2218. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 76
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

2219. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 76
   MCP web search using perplexity without any API KEYS 

2220. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 76
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

2221. **[apitap](https://github.com/n1byn1kt/apitap)** - ⭐ 76
   The MCP server that turns any website into an API — no docs, no SDK, no browser. npm: @apitap/core

2222. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 76
   A full featured, enterprise grade rust MCP SDK

2223. **[Ludus-FastMCP](https://github.com/tjnull/Ludus-FastMCP)** - ⭐ 76
   A Model Context Protocol (MCP) server for automating Ludus v1 and v2 cyber range environments through AI assistants. 190+ tools for range management, blueprints, groups, templates, scenarios, and SIEM integration.

2224. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 76
   [Community Supported] Perforce P4 MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2225. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 76
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2226. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 76
   A Model Context Protocol Server to perform Kafka client operations

2227. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 76
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2228. **[ClawMem](https://github.com/yoloshii/ClawMem)** - ⭐ 76
   On-device context engine and memory for AI agents. Claude Code, Hermes and OpenClaw. Hooks + MCP server + hybrid RAG search.

2229. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

2230. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 75
   MCP to explore websites with llms.txt files

2231. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 75
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

2232. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 75
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

2233. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 75
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

2234. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 75
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

2235. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 75
   Interactive Brokers MCP Server

2236. **[hulunote](https://github.com/hulunote/hulunote)** - ⭐ 75
   AI + Note Hippocampus — Your second brain, powered by AI

2237. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 75
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

2238. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 75
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

2239. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 75
   The Privacy Firewall for LLMs

2240. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 75
   A Model Context Protocol (MCP) server for Microsoft Clarity

2241. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 74
   A task management system designed for AI development

2242. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 74
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

2243. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 74
   Index of all Model Context Protocol (MCP) clients and their capabilities

2244. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 74
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

2245. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 74
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2246. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 74
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

2247. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 74
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2248. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 74
   Unified execution environment for Python code, shell commands, and programmatic MCP tool calls.

2249. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 74
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

2250. **[photon](https://github.com/portel-dev/photon)** - ⭐ 74
   Define intent once. Photon turns a single TypeScript file into CLI tools, MCP servers, and web interfaces.

2251. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

2252. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 73
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

2253. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 73
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

2254. **[firefox-devtools-mcp](https://github.com/globau/firefox-devtools-mcp)** - ⭐ 73
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2255. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 73
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

2256. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 73
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2257. **[Sephera](https://github.com/Reim-developer/Sephera)** - ⭐ 73
   Fast local-first Rust CLI for codebase metrics, AST-compressed LLM context bundles, and built-in MCP server.

2258. **[mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events)** - ⭐ 73
   MCP server providing native macOS integration with Apple Reminders and Calendar via EventKit

2259. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 72
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2260. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 72
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

2261. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 72
   An experimental GitHub MCP server with local database.

2262. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 72
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

2263. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 72
   MCP server for the Joplin note taking app

2264. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 72
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

2265. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 72
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2266. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 72
   An unofficial and community-built MCP server for integrating with https://railway.app

2267. **[youtube-connector-mcp](https://github.com/ShellyDeng08/youtube-connector-mcp)** - ⭐ 72
   MCP server for YouTube — search videos, channels, playlists, and transcripts. Works with Claude, Cursor, Windsurf, and any MCP client.

2268. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 72
   AniList MCP server for accessing anime and manga data

2269. **[Meting-Agent](https://github.com/ELDment/Meting-Agent)** - ⭐ 72
   🪐 面向 AI 的多音乐平台的 API 代理 • 网易云 • QQ音乐 • 酷狗 • 酷我 🎻 Multi-platform music API agent for AI • NetEase • QQ Music • KuGou • Kuwo

2270. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 72
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2271. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 72
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2272. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 72
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2273. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 72
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

2274. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 72
   MCP server for the NCBI E-utilities API. Search PubMed, fetch article metadata and full text, generate citations, explore MeSH terms, and discover related research. STDIO or Streamable HTTP.

2275. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 71
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

2276. **[adb-tui](https://github.com/alanisme/adb-tui)** - ⭐ 71
   🤖 Full-featured Android Debug Bridge TUI and MCP server. Control any device by keystroke or AI.

2277. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 71
   MCP server to fetch YouTube transcripts

2278. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

2279. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server 

2280. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 71
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

2281. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 71
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2282. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 71
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

2283. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 71
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2284. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 71
   Model Context Protocol (MCP) server for Gmail

2285. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 71
   Convert LangChain tools to FastMCP tools

2286. **[trading-mcp](https://github.com/netanelavr/trading-mcp)** - ⭐ 71
   The MCP server that will help you trade smarter (or at least try)

2287. **[join.cloud](https://github.com/kushneryk/join.cloud)** - ⭐ 71
   Join.cloud lets AI agents work together in real-time rooms. Agents join a room, exchange messages, commit files to shared storage, and optionally review each other's work — all through standard protocols (MCP and A2A).

2288. **[adloop](https://github.com/kLOsk/adloop)** - ⭐ 71
   An MCP server that gives your AI assistant read + write access to Google Ads and GA4 — with safety guardrails that prevent accidental spend.

2289. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 70
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

2290. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 70
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

2291. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 70
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

2292. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 70
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2293. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 70
   McDonald's China MCP Server Integration Guide

2294. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 70
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2295. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 70
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

2296. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 70
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

2297. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 70
   Javascript SDK for interacting with the MCP Toolbox for Databases.

2298. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 70
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

2299. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 70
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2300. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 70
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2301. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 70
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2302. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2303. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 69
   MCP client for local ollama models

2304. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 69
   Build MCP servers with WebAssembly components

2305. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 69
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

2306. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 69
   A simple MCP server for the SO-ARM100 control

2307. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 69
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

2308. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 69
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

2309. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 69
   Python 实现 MCP client / service

2310. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 69
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

2311. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 69
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

2312. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 69
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

2313. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 69
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

2314. **[askimo](https://github.com/haiphucnguyen/askimo)** - ⭐ 69
   Open-source AI desktop app with built-in knowledge base, MCP support, and multi-provider models like OpenAI, Gemini, Grok, and Ollama.

2315. **[Alicization-Town](https://github.com/ceresOPA/Alicization-Town)** - ⭐ 69
    **⚔️ Alicization Town** is a decentralized, multi-agent pixel sandbox world powered by the **Model Context Protocol (MCP)**.    **⚔️ Alicization Town** 是一个基于 **MCP (Model Context Protocol)** 架构的去中心化多智能体像素沙盒世界。

2316. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

2317. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 68

2318. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 68
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

2319. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 68
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

2320. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

2321. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 68
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

2322. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 68
   MCP Deep Research Server using Gemini creating a Research AI Agent

2323. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 68
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

2324. **[vesta-mac-dist](https://github.com/scouzi1966/vesta-mac-dist)** - ⭐ 68
   Vesta macOS Distribution - Official releases and downloads.Vesta AI Chat Assistant for macOS - Built with SwiftUI, Swift MLX  and Apple Intelligence using Apple's on device model on MacOs Tahoe (MacOS 26). Now with side-by-side Qwen3-VL for vison

2325. **[hyperterse](https://github.com/hyperterse/hyperterse)** - ⭐ 68
   The MCP framework. Connect your data to your agents.

2326. **[nothumanallowed](https://github.com/adoslabsproject-gif/nothumanallowed)** - ⭐ 68
   Epistemic dataset generation engine. 38 AI agents deliberate through multi-round Geth Consensus — producing auditable reasoning traces for AI training. Parliament System, Knowledge Grounding, zero-trust security.

2327. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 68
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

2328. **[windbg-mcp](https://github.com/gengstah/windbg-mcp)** - ⭐ 68
   An MCP (Model Context Protocol) server that turns all pybag Windows debugger functions into native MCP tools. It lets MCP-compatible clients (Claude Desktop, Claude Code, Cowork, OpenAI Codex CLI, Cursor, and custom agents) control user-mode processes, kernel sessions, and crash dump analysis via structured JSON calls.

2329. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

2330. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

2331. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

2332. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 67
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

2333. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 67
   MCP server that provides tools and resources to control and monitor robots using Nav2.

2334. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 67
   A MCP server for interacting with Bear note-taking software.

2335. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 67
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

2336. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 67
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

2337. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 67
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2338. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 67
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

2339. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2340. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 67
   可视化的配置和管理，给xiaozhi接入mcp

2341. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 66
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

2342. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 66
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

2343. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 66
   [MCP Server] The Security Agent for AI assisted coding

2344. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 66
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

2345. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 66
   Amazon MCP server to search & buy products using the L402

2346. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 66
   Model Context Protocol(MCP) 中文教程讲解

2347. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 66
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

2348. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 66
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

2349. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 66
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2350. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 66
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2351. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 66
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2352. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 65
   Compiler-driven MCP framework for Kotlin Multiplatform

2353. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 65
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

2354. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 65
   A Model Context Protocol implementation for FHIR

2355. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 65
   FHIR MCP Server for handling medical data standard.

2356. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 65
   Academia MCP server: Tools for automatic scientific research

2357. **[ClaudeHistoryMCP](https://github.com/jhammant/ClaudeHistoryMCP)** - ⭐ 65
   MCP server for searching and surfacing Claude Code conversation history

2358. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 65
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

2359. **[Skills-ContextManager](https://github.com/One-Man-Company/Skills-ContextManager)** - ⭐ 65
   A self-hosted web application for managing AI skills, workflows, and contexts with full MCP (Model Context Protocol) integration. Organize, manage, and dynamically load specialized knowledge bases into any AI Agent just by toggling your Skills On/Off in simple local hosted WEB UI.

2360. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 65
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

2361. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 65
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2362. **[mcp-1c](https://github.com/feenlace/mcp-1c)** - ⭐ 65
   MCP server for 1C:Enterprise — AI assistant sees your configuration and generates accurate BSL code. One binary, zero dependencies, 9 tools.

2363. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 65
   LSD Model Context Protocol

2364. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 65
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2365. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 65
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2366. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 65
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2367. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 65
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2368. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 65
   Persistent memory for AI coding agents. Cross-session context, global knowledge, and autonomous task execution.

2369. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

2370. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

2371. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 64
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2372. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 64
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

2373. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 64
   MCP server for the ClinicalTrials.gov v2 API. Search trials, retrieve study details and results, and match patients to eligible trials.

2374. **[ainativelang](https://github.com/sbhooley/ainativelang)** - ⭐ 64
   AINL helps turn AI from "a smart conversation" into "a structured worker."  It is designed for teams building AI workflows that need multiple steps, state and memory, tool use, repeatable execution, validation and control, and lower dependence on long prompt loops.  AINL is a compact, graph-canonical, AI-native programming system for (READ: README)

2375. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

2376. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 63
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

2377. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 63
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

2378. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 63
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

2379. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 63
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2380. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 63
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2381. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 63
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2382. **[mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs)** - ⭐ 63
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2383. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 63
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2384. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 63
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2385. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 62
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2386. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 62
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

2387. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 62
   Miro integration for Model Context Protocol

2388. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 62
   Cryptocurrency Market Data MCP Server

2389. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

2390. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 62
   Advanced MCP server for seamless access to Israeli Government Open Data

2391. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 62
   Model Context Protocol server and client for R

2392. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 62
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2393. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 62
   Universal MCP Server Configuration Manager

2394. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 62
   A Model Context Protocol (MCP) server for Rember.

2395. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 62
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2396. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 62
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2397. **[Embody](https://github.com/dylanroscover/Embody)** - ⭐ 62
   Have a conversation with TouchDesigner

2398. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

2399. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services. 

2400. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 61
   nocodb mcp server

2401. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 61
   A Clojure SDK to create MCP servers (and eventually clients)

2402. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 61
   Zero-dependency MCP server implementation.

2403. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 61
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2404. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 61
   A curated list of awesome Model Context Protocol (MCP) servers.

2405. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 61
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2406. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 61
   A Model Context Protocol server for Go developers

2407. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

2408. **[gdal-mcp](https://github.com/JordanGunn/gdal-mcp)** - ⭐ 61
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2409. **[CornMCP](https://github.com/yuki-20/CornMCP)** - ⭐ 61
   CornMCP is an open-source mono repo that gives AI coding agents (Antigravity, Cursor, Claude Code, Codex), token-saving access to your codebase through the Model Context Protocol (MCP).

2410. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 60
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

2411. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

2412. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

2413. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 60
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

2414. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 60
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2415. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 60
   Adds MCP server to Blockbench

2416. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 60
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2417. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 60
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2418. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 60
   ABAP MCP - Model Context Protocol - Server SDK

2419. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 60
   Attio Model Context Protocol (MCP) server implementation

2420. **[cortex-scout](https://github.com/cortex-works/cortex-scout)** - ⭐ 60
   A unified web extraction and stateful automation engine for AI. Replaces heavy testing frameworks with token-optimized browser control, deep research, and HITL.

2421. **[mcp-bridgekit](https://github.com/mkbhardwas12/mcp-bridgekit)** - ⭐ 60
   Embeddable MCP stdio → HTTP bridge with background jobs & live dashboard. Survives Vercel/Cloudflare 30s timeouts. Now scales to 100+ users.

2422. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

2423. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 60
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2424. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 60
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2425. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 60
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2426. **[aguara](https://github.com/garagon/aguara)** - ⭐ 60
   Security scanner for AI agent skills and MCP servers. Static analysis, incident response, no LLM. One binary.   Detection engine behind oktsec.

2427. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 60
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2428. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 60
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2429. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 60
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2430. **[drawio-mcp-server](https://github.com/simonkurtz-MSFT/drawio-mcp-server)** - ⭐ 60
   A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server generates Draw.io XML directly — no browser extension or Draw.io instance required.

2431. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 60
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

2432. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 60
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2433. **[gno](https://github.com/gmickel/gno)** - ⭐ 60
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2434. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 60
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2435. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2436. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 59
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

2437. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

2438. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

2439. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

2440. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 59
   MCP Server to expose the GDB debugging capabilities

2441. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 59
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2442. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 59
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2443. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 59
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2444. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 59
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

2445. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 59
   A Model Context Protocol server for Ashra

2446. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 59
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2447. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 59
   Unblock, scrape, and search tools for MCP clients

2448. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 59
   Altium Model Context Protocol server and Altium API script

2449. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2450. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 59
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2451. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 59
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2452. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 58
   MCP router and Web Based MCP client

2453. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2454. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2455. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 58
   ScapeGraph MCP Server

2456. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 58
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2457. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 58
   MCP Server for IBKR Client

2458. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 58
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2459. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 58
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2460. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 58
   Model Context Protocol server for ActivityWatch time tracking data

2461. **[1c-mcp](https://github.com/Untru/1c-mcp)** - ⭐ 58
   Curated list of MCP servers for 1C:Enterprise ecosystem | Каталог MCP-серверов для экосистемы 1С:Предприятие

2462. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 58
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2463. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 58
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2464. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 58
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2465. **[omega-memory](https://github.com/omega-memory/omega-memory)** - ⭐ 57
   Persistent memory for AI coding agents

2466. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2467. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 57
   Model Context Protocol server for Daipendency

2468. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2469. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2470. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 57
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2471. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 57
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2472. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 57
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2473. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 57
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2474. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 57
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2475. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 57
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2476. **[SageFs](https://github.com/WillEhrendreich/SageFs)** - ⭐ 57
   Sage Mode for F# development — REPL with solution or project loading, Live Testing for FREE, Hot Reload, and session management.

2477. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2478. **[cesium-mcp](https://github.com/gaopengbin/cesium-mcp)** - ⭐ 57
   AI-powered CesiumJS 3D globe control  49 tools for camera, entities, layers, animation & spatial analysis via Model Context Protocol (MCP). Natural language to 3D GIS.

2479. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 57
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2480. **[estonia-ai-kit](https://github.com/stefanoamorelli/estonia-ai-kit)** - ⭐ 57
   🇪🇪 Open-source AI SDK for Estonian government and private services. MCP servers and skills. Connect Claude, GPT, agents and models, to Estonia's digital infrastructure.

2481. **[agent-architecture-review-sample](https://github.com/Azure-Samples/agent-architecture-review-sample)** - ⭐ 57
   The Architecture Review Agent is an open-source AI agent sample that reviews software architectures and generates interactive diagrams automatically. 

2482. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 56
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2483. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2484. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

2485. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2486. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

2487. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2488. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 56
   Generate an MCP for any web app

2489. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 56
   Write notes to Flomo

2490. **[MegaMemory](https://github.com/0xK3vin/MegaMemory)** - ⭐ 56
   Persistent project knowledge graph for coding agents. MCP server with semantic search, in-process embeddings, and web explorer.

2491. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 56
   OCaml implementation of the Model Context Protocol (MCP)

2492. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 56
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2493. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 56
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2494. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 56
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2495. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 56
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2496. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 56
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2497. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2498. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 56
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2499. **[AutoGenesis](https://github.com/microsoft/AutoGenesis)** - ⭐ 56
   AutoGenesis is an AI-powered automated testing framework based on Model Context Protocol (MCP), supporting multiple platforms including desktop applications (Windows/macOS) and mobile applications (iOS/Android).

2500. **[MCP-Trust-Kit](https://github.com/aak204/MCP-Trust-Kit)** - ⭐ 55
   Deterministic CI scanner and surface-risk scoring for MCP (Model Context Protocol) servers.

2501. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 55
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2502. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 55
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2503. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 55
   MCP server to support Astro project development

2504. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 55
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2505. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 55
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2506. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 55
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2507. **[python](https://github.com/mcp-auth/python)** - ⭐ 55
   🔐 Plug-and-play auth for Python MCP servers.

2508. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 55
   Multiplatform system monitoring tool using Cosmopolitan Libc

2509. **[AfdianToMarkdown](https://github.com/PhiFever/AfdianToMarkdown)** - ⭐ 55
   爱发电爬虫(afdian.com)

2510. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 55
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2511. **[go-crx3](https://github.com/mmadfox/go-crx3)** - ⭐ 55
   Chrome browser extension tools with MCP integration. Pack, unpack, zip, unzip, download, and manage CRX3 extensions – now AI-compatible via Model Context Protocol.

2512. **[client](https://github.com/php-mcp/client)** - ⭐ 55
   Core PHP implementation for the Model Context Protocol (MCP) Client

2513. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 55
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2514. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 55
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2515. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 55
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2516. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 55
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2517. **[pentestMCP](https://github.com/RamKansal/pentestMCP)** - ⭐ 55
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2518. **[unreal-api-mcp](https://github.com/Codeturion/unreal-api-mcp)** - ⭐ 55
   Instant, accurate Unreal Engine API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations.

2519. **[memex](https://github.com/iamtouchskyer/memex)** - ⭐ 55
   Zettelkasten-based persistent memory for AI coding agents. Works with Claude Code, Cursor, VS Code Copilot, Codex, Windsurf & any MCP client. No vector DB — just markdown + git sync.

2520. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 55
   MCP Memory Server with DuckDB backend

2521. **[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp)** - ⭐ 55
   MCP server for controlling a real iPhone via macOS iPhone Mirroring...and any MacOs app. Screenshot, tap, swipe, type — from any MCP client.

2522. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 54
   A powerful Model Context Protocol server for LinkedIn API integration

2523. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2524. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2525. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2526. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 54
   A MCP server for symbolic manipulation of mathematical expressions

2527. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 54
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2528. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 54
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2529. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 54
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2530. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 54
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2531. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 54
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2532. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 54
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2533. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 54
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2534. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 54
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2535. **[mcpshim](https://github.com/mcpshim/mcpshim)** - ⭐ 54
   Turn remote MCP servers into local command workflows.

2536. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 54
   Go SDK for interacting with the MCP Toolbox for Databases.

2537. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 54
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2538. **[MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP)** - ⭐ 54
   Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered search and vision analysis APIs optimized for code development workflows

2539. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 54
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2540. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 54
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

2541. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 53
   Model Context Protocol Servers for Azure AI Search

2542. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

2543. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2544. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 53
   Unofficial Golang SDK for Anthropic Model Context Protocol

2545. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2546. **[Multi-Agent-System-A2A-ADK-MCP](https://github.com/RubensZimbres/Multi-Agent-System-A2A-ADK-MCP)** - ⭐ 53
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2547. **[skrills](https://github.com/athola/skrills)** - ⭐ 53
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2548. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 53
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2549. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 53
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2550. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 53
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2551. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 53
   MCP Guard secures your MCP client from prompt injection attacks and more.

2552. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 53
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2553. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 53
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2554. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 53
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2555. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 53
   Thoughtbox is an intention ledger for agents. Evaluate AI's decisions against its decision-making.

2556. **[civyk-winwright](https://github.com/civyk-official/civyk-winwright)** - ⭐ 53
   Playwright-style MCP server for Windows desktop, system, and browser automation. 59 tools for WPF, WinForms, Win32, Chrome/Edge via Model Context Protocol.

2557. **[dataworkers-claw-community](https://github.com/DataWorkersProject/dataworkers-claw-community)** - ⭐ 53
   We’re build a swarm of agents for all data tasks. That anyone can use for free, open-source community version.  

2558. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 53
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2559. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 53
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2560. **[unraid-mcp](https://github.com/jmagar/unraid-mcp)** - ⭐ 53
   Query, monitor, and manage Unraid servers via GraphQL API through MCP tools. Supports system info, Docker, VMs, array/parity, notifications, plugins, rclone, and live telemetry.

2561. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 52
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

2562. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2563. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 52
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2564. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2565. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 52
   Claude  et al. play the brilliant puzzle title "Baba is You"

2566. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 52
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

2567. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 52
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2568. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 52
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

2569. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 52
   Inkdrop Model Context Protocol Server

2570. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 52
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2571. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 52
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2572. **[fossil-mcp](https://github.com/yfedoseev/fossil-mcp)** - ⭐ 52
   The code quality toolkit for the agentic AI era. Find dead code, clones, and scaffolding across 15 languages. MCP server + CLI.

2573. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 52
   Official Rust implementation of the UTCP

2574. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 52
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2575. **[unity-mcp-plugin](https://github.com/AnkleBreaker-Studio/unity-mcp-plugin)** - ⭐ 52
   Unity MCP Plugin (UPM) — Editor bridge for AI-assisted game development. Enables Claude, Cursor & MCP-compatible AI to control Unity Editor with 268 tools: scenes, GameObjects, components, builds, profiling, Shader Graph, Amplify Shader Editor, terrain, physics, NavMesh & more. Free & open source.

2576. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 51
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

2577. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 51
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

2578. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 51
   Quantum-proof MCP Server and Client Interactions

2579. **[gdal-mcp](https://github.com/Wayfinder-Foundry/gdal-mcp)** - ⭐ 51
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2580. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 51
   MCP Server for whois lookups.

2581. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 51
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

2582. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 51
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2583. **[ShadowCrawl](https://github.com/DevsHero/ShadowCrawl)** - ⭐ 51
   🥷 The FREE, Sovereign alternative to Firecrawl & Tavily. Pure Rust Stealth Scraper + Built-in God-Tier Meta-Search for AI Agents. Bypass Cloudflare & DataDome via HITL. Zero-bloat, ultra-clean LLM data. 99.99% Success Rate. 🦀

2584. **[hmr](https://github.com/promplate/hmr)** - ⭐ 51
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

2585. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 51
   Matlab MCP Server in python

2586. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 51
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

2587. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 51
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2588. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 51
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2589. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 51
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2590. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 51
   Implementation of Model Context Protocol server for Mailgun APIs

2591. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 51
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2592. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 51
   MCP client for Discourse sites

2593. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 51
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2594. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 51
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2595. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 51
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2596. **[brainstorm-mcp](https://github.com/spranab/brainstorm-mcp)** - ⭐ 51
   MCP server for multi-round AI brainstorming debates between multiple models (GPT, DeepSeek, Groq, Ollama, etc.)

2597. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2598. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 50

2599. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

2600. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

2601. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

2602. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

2603. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

2604. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 50
   An implementation of the Model Context Protocol in Ruby.

2605. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 50
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2606. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 50
   GIMP MCP server

2607. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 50
   vMCP - Virtual Model Context Protocol

2608. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

2609. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 50
   MCP Server for Text to Speech

2610. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 50
   Amadeus MCP(Model Context Protocol) Server

2611. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 50
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

2612. **[mcp](https://github.com/40ants/mcp)** - ⭐ 50
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2613. **[tokio-prompt-orchestrator](https://github.com/Mattbusel/tokio-prompt-orchestrator)** - ⭐ 50
   Multi-core, Tokio-native orchestration for LLM pipelines.

2614. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 50
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2615. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 50
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2616. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 50
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

2617. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2618. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 50
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2619. **[unity-api-mcp](https://github.com/Codeturion/unity-api-mcp)** - ⭐ 50
   Instant, accurate Unity API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations

2620. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 50
   MCP (Model Context Protocol) server for the Contentful Management API

2621. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 50
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2622. **[bernstein](https://github.com/chernistry/bernstein)** - ⭐ 50
   Declarative Agent Orchestration.  Ship while you sleep.

2623. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

2624. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 49
   Anthropic’s Model Context Protocol implementation for Oat++

2625. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

2626. **[agent-os](https://github.com/imran-siddique/agent-os)** - ⭐ 49
   A Safety-First Kernel for Autonomous AI Agents - POSIX-inspired primitives with 0% policy violation guarantee

2627. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 49
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

2628. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 49
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

2629. **[mcp](https://github.com/goplus/mcp)** - ⭐ 49
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

2630. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 49
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

2631. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 49
   Send system notification when Agent task is done.

2632. **[template-mcp-server](https://github.com/redhat-data-and-ai/template-mcp-server)** - ⭐ 49
   Production-ready Python template for building MCP servers with FastMCP, FastAPI, OAuth, and OpenShift deployment.

2633. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

2634. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

2635. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 49
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2636. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 49

2637. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 49
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

2638. **[mcp-stata](https://github.com/tmonk/mcp-stata)** - ⭐ 49
    A lightweight Model Context Protocol (MCP) server for Stata. Execute commands, inspect data, retrieve stored results (r()/e()), and view graphs in your chat interface. Built for economists who want to integrate LLM assistance into their Stata workflow. 

2639. **[MCPwner](https://github.com/Pigyon/MCPwner)** - ⭐ 49
   Model Context Protocol server for autonomous vulnerability discovery

2640. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 49
   IMAP Model Context Protocol server for interactive email processing

2641. **[mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index)** - ⭐ 49
   17 MCP query tools for codebase navigation — functions, classes, imports, dependency graphs, change impact. Zero dependencies. 87% token reduction.

2642. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 48
   A Model-Context-Protocol (MCP) Server for Active Directory

2643. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 48
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

2644. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

2645. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

2646. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

2647. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 48
   Official MCP Server for Buildkite.

2648. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 48
   A comprehensive MCP server for Metabase with 70+ tools.

2649. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 48
   Remote MCP server that gives LLMs access to run network commands

2650. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 48
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

2651. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 48
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

2652. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

2653. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2654. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 48
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

2655. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 48
   Model Context Protocol to fetch youtube transcript

2656. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 48
   mcp server to run scripts on adobe illustrator

2657. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 48
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

2658. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2659. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 48
   Un-official Serper Google search server for Cline and other MCP clients

2660. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 48
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2661. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 48
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

2662. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

2663. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

2664. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 48
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2665. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 48
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

2666. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2667. **[reaper-mcp](https://github.com/bonfire-audio/reaper-mcp)** - ⭐ 48
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2668. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 47
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2669. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 47
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

2670. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

2671. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

2672. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

2673. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

2674. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 47
   Grant the AI octopus access to a portion of your desktop

2675. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 47
   Dremio MCP server

2676. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 47
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

2677. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 47
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

2678. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 47
   OpenAPI Schema Model Context Protocol Server

2679. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 47
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2680. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 47
   Enhanced Zen MCP Server with 'zen' default tool and improvements

2681. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 47
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

2682. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 47
   Deep Research & Competitor Analysis MCP for Claude & Cursor. No API Keys. Features: Web Search, Social Media (Reddit/HN), Trends & OCR.

2683. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 47
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

2684. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 47
   共学《MCP极简开发》项目代码

2685. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 47
   Sample MCP Server and MCP client with Aspire

2686. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 47
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

2687. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 47
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2688. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 47
   A production-ready Model Context Protocol (MCP) server for semantic memory management

2689. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 47
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2690. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 47
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2691. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 47
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 17 security hardening layers

2692. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 47
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2693. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2694. **[openclaw-superpowers](https://github.com/ArchieIndian/openclaw-superpowers)** - ⭐ 46
   44 plug-and-play skills for OpenClaw — self-modifying AI agent with cron scheduling, security guardrails, persistent memory, knowledge graphs, and MCP health monitoring. Your agent teaches itself new behaviors during conversation.

2695. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

2696. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

2697. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 46
   Model Context Protocol server for Flight Tracking

2698. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 46
   MCPcat is an analytics platform for MCP server owners 🐱.

2699. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 46
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

2700. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 46
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

2701. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 46
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

2702. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 46
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2703. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

2704. **[sharedcontext](https://github.com/Eversmile12/sharedcontext)** - ⭐ 46
   MCP server that gives AI coding assistants persistent cross-client memory. Facts and conversations stored in SQLite, encrypted with AES-256-GCM, synced to Arweave. No server, no account, recoverable with a 12-word phrase.

2705. **[claude-additional-models-mcp](https://github.com/Arkya-AI/claude-additional-models-mcp)** - ⭐ 46
   Reduce Claude Desktop consumption by 10x - Integrate Google's Gemini or Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

2706. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2707. **[ctxvault](https://github.com/Filippo-Venturini/ctxvault)** - ⭐ 46
   Local memory infrastructure for AI agents. Store knowledge and skills in isolated vaults you compose, control and query — entirely local.

2708. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 46
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2709. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2710. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

2711. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 46
   An implementation of the Model Context Protocol for the World Bank open data API

2712. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 46
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

2713. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2714. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 46
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

2715. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 46
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

2716. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 46
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2717. **[Generative-UI-MCP](https://github.com/op7418/Generative-UI-MCP)** - ⭐ 46
   MCP server that teaches AI models to generate interactive visualizations — charts, diagrams, mockups, and more.

2718. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 45
   ElizaOS plugin allowing agents to connect to MCP servers

2719. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 45
   An opinionated starter template for making Model Context Protocol (MCP) servers

2720. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

2721. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

2722. **[js](https://github.com/mcp-auth/js)** - ⭐ 45
   🔐 Plug-and-play auth for Node.js MCP servers.

2723. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

2724. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 45
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

2725. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 45
   Create the prompts you need to write your Novel using AI

2726. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 45
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

2727. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 45
   MCP server for golang projects development: Expand AI Code Agent ability boundary to have a semantic understanding and determinisic information for golang projects.

2728. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 45
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

2729. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

2730. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 45
   Model Context Protocol server for Salesforce REST API integration

2731. **[mcp-workspace](https://github.com/MarcusJellinghaus/mcp-workspace)** - ⭐ 45
   MCP Workspace Server: A secure Model Context Protocol server providing file, git, and GitHub tools for AI assistants within a sandboxed project directory.

2732. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 45
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

2733. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 45
   GraphQL Schema Model Context Protocol Server

2734. **[bonnard-cli](https://github.com/bonnard-data/bonnard-cli)** - ⭐ 45
   Open-source agentic schema CLI. Optimised for claude code, gemini, codex and co-pilot. Skills included.

2735. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 45
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

2736. **[notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)** - ⭐ 45
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

2737. **[Zikkaron](https://github.com/amanhij/Zikkaron)** - ⭐ 45
   Biologically-inspired persistent memory engine for Claude Code. 26 cognitive subsystems, Hopfield networks, predictive coding, causal discovery, successor representations, all running locally over SQLite.

2738. **[npm-packages](https://github.com/WebMCP-org/npm-packages)** - ⭐ 45
   NPM packages for MCP-B: Transport layers, React hooks, and browser tools for the Model Context Protocol

2739. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 45
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

2740. **[cesium-ai-integrations](https://github.com/CesiumGS/cesium-ai-integrations)** - ⭐ 45
   Cesium AI Integrations is a collection of reference integrations and experiments connecting the Cesium ecosystem with AI systems including Model Context Protocol (MCP) tools, retrieval pipelines, and agent skills.

2741. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 44
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2742. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 44
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

2743. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 44
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

2744. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 44
   Moondream MCP Server in Python

2745. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

2746. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

2747. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

2748. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 44
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

2749. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

2750. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 44
   An MCP server to allow you to debug webpages using LLMs

2751. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 44
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

2752. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 44
   Yandex Tracker MCP Server with OAuth2 support

2753. **[adal-cli](https://github.com/SylphAI-Inc/adal-cli)** - ⭐ 44
   The self-evolving coding agent that learns from your entire team and codebase. Less syncing. Less waiting. Deliver at the speed of thought.

2754. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 44
   Model Context Protocol Platform，统一管理你的MCP服务

2755. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 44
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2756. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 44
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

2757. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 44
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

2758. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

2759. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 44
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

2760. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2761. **[mcpx](https://github.com/lydakis/mcpx)** - ⭐ 44
   Turn MCP servers into composable CLIs.

2762. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 44
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2763. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 44
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

2764. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 44
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2765. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 44
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

2766. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2767. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 44
   A Model Context Protocol (MCP) server for NATS messaging system integration

2768. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 43
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

2769. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 43
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

2770. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

2771. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

2772. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

2773. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

2774. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

2775. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 43
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

2776. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

2777. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

2778. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 43
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

2779. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 43
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

2780. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 43
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

2781. **[lastsaas](https://github.com/jonradoff/lastsaas)** - ⭐ 43
   SaaS boilerplate/starter-kit in Go+React with Stripe integration, multi-tenant support, comprehensive features and AI-agent ready

2782. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 43
   A curated list of excellent Model Context Protocol (MCP) servers.

2783. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 43
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

2784. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2785. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 43
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

2786. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 43
   Solana Model Context Protocol (MCP) Demo

2787. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 43
   MCP server for native app testing & browser automation — screenshot, OCR, click, type, find_text, Chrome/Electron CDP, template matching. macOS, Windows & Android. Works with Claude, Cursor, and any MCP client.

2788. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 43
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2789. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 43
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

2790. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 43
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

2791. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 42
   Model Context Protocol (MCP) server for LinkedIn API integration

2792. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

2793. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

2794. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

2795. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

2796. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 42
   WhatsApp Unofficial MCP Server

2797. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 42
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

2798. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 42
   台灣證交所OpenAPI 的 MCP Server

2799. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 42
   Bluesky MCP (Model Context Protocol) Server

2800. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 42
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2801. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 42
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2802. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 42
   Rimworld Coding RAG MCP server

2803. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 42
   SAP HANA MCP server — Enterprise Model Context Protocol server for SAP HANA. Use with Claude Code, VS Code. npm: hana-mcp-server

2804. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2805. **[omnifocus-mcp-enhanced](https://github.com/jqlts1/omnifocus-mcp-enhanced)** - ⭐ 42
   Enhanced Model Context Protocol (MCP) server for OmniFocus with complete subtask support, perspective views (Inbox/Flagged/Forecast/Tags), ultimate   task filtering, and direct access to custom perspectives. Seamlessly integrate OmniFocus with Claude AI for intelligent task management.

2806. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 42
   Algorand Local Model Context Protocol (Server & Client)

2807. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 42
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

2808. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 42
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2809. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 42
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2810. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 42
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2811. **[wp-mcp-ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)** - ⭐ 42
   WordPress MCP Ultimate — Full MCP server with 58 WordPress abilities. Connect WordPress to any AI via Model Context Protocol.

2812. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 41
   Model Context Protocol (MCP) implementation for iOS simulators

2813. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   MCP server that exposes YepCode processes as callable tools for AI platforms. Securely connect AI assistants to your YepCode workflows, APIs, and automations.

2814. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

2815. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

2816. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

2817. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

2818. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

2819. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

2820. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 41
   MCP server for Obsidian (TypeScript + Bun)

2821. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 41
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

2822. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 41
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

2823. **[processhacker-mcp](https://github.com/illegal-instruction-co/processhacker-mcp)** - ⭐ 41
   your ai debugger, vibe hacking tool

2824. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 41

2825. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 41
   A hackable Model Context Protocol (MCP) gateway

2826. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 41
   Model Context Protocol server for Sitecore

2827. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 41
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

2828. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 41
   Command-line interface for any Model Context Protocol (MCP) server.

2829. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 41
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

2830. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 41
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2831. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 41
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

2832. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 41
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2833. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 41
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2834. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 41
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2835. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 41
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

2836. **[Dragon-Brain](https://github.com/iikarus/Dragon-Brain)** - ⭐ 41
   Dragon Brain — persistent long-term memory for AI agents via MCP (Model Context Protocol). Knowledge graph (FalkorDB) + vector search (Qdrant) + CUDA GPU embeddings. Works with Claude, Gemini CLI, Cursor, Windsurf, VS Code Copilot. 31 tools, 1116 tests.

2837. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 41
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2838. **[aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol](https://github.com/microsoft/aitour26-WRK542-prototype-agents-with-the-ai-toolkit-and-model-context-protocol)** - ⭐ 41

2839. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

2840. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2841. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 40
   A Model Context Protocol server that provides access to Shodan API functionality

2842. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 40
   a mcp server for polymarket

2843. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 40
   A generic, modular server for implementing the Model Context Protocol (MCP). 

2844. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

2845. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

2846. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

2847. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

2848. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 40
   Write detections, investigate alerts, and query logs from your favorite AI agents

2849. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 40
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

2850. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 40
   PDF RAG server for cursor.

2851. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 40
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

2852. **[bonnard-cli](https://github.com/meal-inc/bonnard-cli)** - ⭐ 40
   Agent-native analytics. MCP server, dashboards, SDK, and semantic layer CLI.

2853. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 40
   Apple Books MCP Server

2854. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 40
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2855. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 40
   It shows how to use model-context-protocol. 

2856. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 40
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2857. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 40
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

2858. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 40
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2859. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 40
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

2860. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 40
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

2861. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

2862. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 40
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

2863. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 40
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2864. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 40
   Claude Unified Model Context Interaction Protocol

2865. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 40
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2866. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

2867. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 40
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

2868. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 40
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2869. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 40
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

2870. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 40
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

2871. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 40
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

2872. **[mie](https://github.com/kraklabs/mie)** - ⭐ 40
   Persistent memory graph for AI agents. Facts, decisions, entities, and relationships that survive across sessions, tools, and providers. MCP server — works with Claude, Cursor, ChatGPT, and any MCP client.

2873. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 40
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

2874. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 40
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2875. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 40
   An MCP server for querying Solana transactions using natural language with Solscan API

2876. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 40
   Learn Model Context Protocol with Python, published by Packt

2877. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 39
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2878. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 39
   MCP server for anki

2879. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

2880. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

2881. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

2882. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

2883. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

2884. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

2885. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 39
   Self-hosted Stealth Scraping & Federated Search for AI Agents. A 100% private, free alternative to Firecrawl, Jina Reader, and Tavily. Featuring Universal Anti-bot Bypass + Semantic Research Memory, Copy-Paste setup

2886. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 39
   Enable AI assistants to explore and query your Steampipe data!

2887. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 39
   A MCP server for Storybook.

2888. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 39
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

2889. **[music-composer-webmcp](https://github.com/Leanmcp-Community/music-composer-webmcp)** - ⭐ 39
   This WebMCP Music Composer project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with local browser contexts (tools) to achieve complex workflows autonomously.

2890. **[best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** - ⭐ 39
   🏆  A ranked list of MCP servers. Updated weekly.

2891. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

2892. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 39
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2893. **[arifosmcp](https://github.com/ariffazil/arifosmcp)** - ⭐ 39
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

2894. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

2895. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 39
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

2896. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 39
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

2897. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 39
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

2898. **[mcp-server](https://github.com/Aayush9029/mcp-server)** - ⭐ 39
   MCP SERVER

2899. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 39
   Model Context Protocol Minecraft Server

2900. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 39
   The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2901. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 39
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2902. **[arifOS](https://github.com/ariffazil/arifOS)** - ⭐ 39
   ArifOS — Constitutional MCP kernel for governed AI execution. AAA architecture: Architect · Auditor · Agent. Built for the open-source agentic era.

2903. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 39
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

2904. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 39
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2905. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 39
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2906. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 39
   Sync MCP (Model Context Protocol) configurations across AI tools

2907. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 39
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2908. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 39
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2909. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 39
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2910. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 39
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2911. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 39
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2912. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 38
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

2913. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 38
   A package manager to manage all your mcp servers across platforms

2914. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 38
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

2915. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

2916. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

2917. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 38
   A Chat Client for LLMs, written in Compose Multiplatform.

2918. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

2919. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

2920. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

2921. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

2922. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 38
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

2923. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 38
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

2924. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 38
   Highly configurable autonomous efficient-first agentic AI framework for CLI

2925. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 38
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

2926. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 38
   Enhanced MCP server for GitLab: group projects listing and activity tracking

2927. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 38
   awesome-lists now available as MCP server for you agent.

2928. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 38
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

2929. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 38
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

2930. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 38
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

2931. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 38
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

2932. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 38
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

2933. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 38
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

2934. **[roampal-core](https://github.com/roampal-ai/roampal-core)** - ⭐ 38
   Outcome-based persistent memory MCP server for Claude Code and OpenCode. Good advice promoted, bad advice demoted. pip install roampal.

2935. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 38
   Model Context Protocol server to let LLMs write and execute matlab scripts 

2936. **[camofox-mcp](https://github.com/redf0x1/camofox-mcp)** - ⭐ 38
   Anti-detection browser MCP server for AI agents — navigate, interact, and automate the web without getting blocked

2937. **[golemcore-bot](https://github.com/alexk-dev/golemcore-bot)** - ⭐ 38
   AI agent framework for Java — skill-based architecture with MCP support, tool calling, RAG, and Telegram integration. Built on Spring Boot and  LangChain4j

2938. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 38
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

2939. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 38
   Open source local MCP server providing AI assistants with comprehensive access to eBay's Sell APIs. Includes 325 tools for inventory management, order fulfillment, marketing campaigns, analytics, developer tools, and more.

2940. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 38
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2941. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 38
   Model Context Protocol server for CODESYS automation platform

2942. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 38
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

2943. **[zabbix-mcp-server](https://github.com/initMAX/zabbix-mcp-server)** - ⭐ 38
   MCP server for the complete Zabbix API — 220 tools, multi-server support, bearer auth, systemd ready. Works with ChatGPT, Claude, VS Code, Codex, JetBrains and any MCP client.

2944. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 37
   Trivy plugin for starting an MCP server

2945. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 37
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

2946. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

2947. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 37
   MCP server tailored to connecting web crawler data and archives

2948. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 37
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

2949. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 37
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

2950. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

2951. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

2952. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2953. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 37
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

2954. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2955. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 37
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

2956. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 37
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

2957. **[google-workspace-mcp](https://github.com/dguido/google-workspace-mcp)** - ⭐ 37
   MCP server for Google Drive, Docs, Sheets, Slides, Calendar, Gmail, and Contacts

2958. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 37
   An MCP server for Android's Tasker automation app.

2959. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 37
   A simple note-taking MCP server for recording and managing notes with AI models.

2960. **[godot-mcp](https://github.com/HaD0Yun/godot-mcp)** - ⭐ 37
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

2961. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 37
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2962. **[pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp)** - ⭐ 37
   Model Context Protocol (MCP) server for AI-powered reservoir engineering calculations. Integrates pyResToolbox with Claude AI for PVT analysis, well   performance, simulation support, and more. 47 production-ready tools using industry-standard correlations.

2963. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

2964. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 37
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

2965. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 37
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

2966. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 37
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2967. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 37
   model context protocol for Autodesk Revit

2968. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 37
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

2969. **[devswarm](https://github.com/justrach/devswarm)** - ⭐ 37
   High-performance MCP server, code graph engine & evolutionary algorithm platform in Zig. 33 tools: GitHub project management, agent swarm orchestration, iterative review-fix loops, blast radius analysis, and code navigation via Model Context Protocol.

2970. **[TalkToFigmaDesktop](https://github.com/grab/TalkToFigmaDesktop)** - ⭐ 37
   A powerful desktop application bridging Figma and AI tools via Model Context Protocol Seamless integration between Figma designs and AI assistants

2971. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2972. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 37
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2973. **[amazon_ads_mcp](https://github.com/KuudoAI/amazon_ads_mcp)** - ⭐ 37
   Amazon Ads MCP - Model Context Protocol server for Amazon Advertising API

2974. **[reddit-mcp-server](https://github.com/jordanburke/reddit-mcp-server)** - ⭐ 37
   ⚙️ A Model Context Protocol (MCP) that provides tools for fetching and creating Reddit content

2975. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 36
   Model Context Protocol (MCP) Server for Mistral OCR API

2976. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

2977. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

2978. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

2979. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

2980. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

2981. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

2982. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

2983. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 36
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

2984. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 36
   A2A Protocol client and developer toolkit.

2985. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 36
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

2986. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 36
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

2987. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 36
   Python sandboxes for llms

2988. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 36
   A curated collection of persona-based mcp server & tool groupings.

2989. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 36
   Vapi MCP Server

2990. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 36
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

2991. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 36
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

2992. **[apple-mail-mcp](https://github.com/patrickfreyer/apple-mail-mcp)** - ⭐ 36
   MCP server giving AI assistants full access to Apple Mail - read, search, compose, organize & analyze emails via natural language

2993. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 36
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

2994. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 36
   Emacs Lisp implementation of the Model Context Protocol

2995. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 36
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2996. **[mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp)** - ⭐ 36
   A Model-Context Protocol server for the MITRE ATT&CK knowledge base

2997. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 36
   Model Context Protocol (MCP) server that interacts with a Debugger

2998. **[ronykit](https://github.com/clubpay/ronykit)** - ⭐ 36
   API Framework supporting REST and RPC.

2999. **[agience-core](https://github.com/Agience/agience-core)** - ⭐ 36
   An open, extensible runtime for agentic AI. Shared artifacts, structured state, and provenance by default.

3000. **[vulnerablemcp](https://github.com/vineethsai/vulnerablemcp)** - ⭐ 36
   A comprehensive database of Model Context Protocol vulnerabilities, security research, and exploits

3001. **[Kaimon.jl](https://github.com/kahliburke/Kaimon.jl)** - ⭐ 36
   MCP server giving AI agents full access to Julia's runtime via a live Gate — code execution, introspection, debugging, testing, and semantic search

3002. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 36
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

3003. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

3004. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 36
   List of Awesome MCP Servers and Clients for building Agentic Devops 

3005. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 36
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

3006. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 36
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

3007. **[ziya](https://github.com/ziya-ai/ziya)** - ⭐ 36
   Self-hosted AI workbench for code, architecture, and operations. Not an IDE. Rich visualizations, diff application, parallel AI agents, enterprise plugin system.

3008. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 36
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

3009. **[ferris-search](https://github.com/lispking/ferris-search)** - ⭐ 36
   A blazing-fast MCP (Model Context Protocol) server for multi-engine web search, written in Rust.

3010. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 36
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

3011. **[slack-mcp-plugin](https://github.com/slackapi/slack-mcp-plugin)** - ⭐ 36
   Repo containing the configuration information for the Slack MCP to be added to other clients

3012. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 35
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

3013. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 35
   OpenAI Code Assistant Model Context Protocol (MCP) Server

3014. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

3015. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

3016. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

3017. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

3018. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

3019. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

3020. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 35
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

3021. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 35
   An open source implementation of the Claude built-in text editor tool

3022. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 35
   A super simple Starter to build your own MCP Server

3023. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

3024. **[daisyui-mcp](https://github.com/birdseyevue/daisyui-mcp)** - ⭐ 35
   🌼 A token-friendly local MCP server for DaisyUI component documentation using their public llms.txt.

3025. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 35
   Turn any MCP Client into a "multi-agent" system (via prompting)

3026. **[awesome-mcp-servers](https://github.com/ever-works/awesome-mcp-servers)** - ⭐ 35
   A curated list of the best MCP Servers, featuring top solutions, libraries, tools, and more. - https://mcpserver.works

3027. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 35
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

3028. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 35
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

3029. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 35
   An MCP for AI Agents that detects your team coding conventions and patterns, brings in persistent memory, edit preflight checks, and hybrid search with evidence scoring. Exposed through CLI and MCP server.

3030. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 35
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

3031. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 35
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

3032. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 35
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

3033. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 35
   Arch Linux MCP (Model Context Protocol) Server

3034. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 35
   Tools for building modern & secure MCP integrations across the client and server side

3035. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 35
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

3036. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 35
   Zillow MCP Server for real estate data access via the Model Context Protocol

3037. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 35
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

3038. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 35
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

3039. **[AgentTools](https://github.com/WolframResearch/AgentTools)** - ⭐ 35
   Implements a model context protocol server using Wolfram Language

3040. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 34
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

3041. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 34
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

3042. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

3043. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

3044. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

3045. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 34
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

3046. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

3047. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 34
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

3048. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform. 

3049. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

3050. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

3051. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

3052. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 34
   MCP Server connects with claude code local command.

3053. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 34
   Model Context Protocol server written in Scala

3054. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 34
   Apache IoTDB MCP Server

3055. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 34
   Let your agent write code and execute code directly in the browser with WASM

3056. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 34
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

3057. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

3058. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 34
   An MCP server that allows users to dynamically add custom tools/functions at runtime

3059. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 34
   A MCP implementation for sending notifications via Pushover

3060. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 34
   Capacities×MCP

3061. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 34
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

3062. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 34
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

3063. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 34
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

3064. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

3065. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 34
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

3066. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 34
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

3067. **[mcp](https://github.com/fastly/mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

3068. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 34
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

3069. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 34
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

3070. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 34
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

3071. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 34
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

3072. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for openBIM

3073. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 34
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

3074. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 34
   Implements a model context protocol server using Wolfram Language

3075. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 34
   A generic mcp server fuzzer

3076. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 34
   Model Context Protocol extension for Azure Functions.

3077. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 34
   About A Model Context Protocol server that executes commands in the current WezTerm session

3078. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 34
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

3079. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

3080. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

3081. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 33
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

3082. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

3083. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

3084. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

3085. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

3086. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 33
   MCP Server for Membrane

3087. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 33
   Minimalist AI agent that fixes itself when things break.

3088. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 33
   AI-Powered Threat Intelligence MCP tool

3089. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 33
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

3090. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 33
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

3091. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 33
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi. 

3092. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 33
   Minimal Metals stand alone client that allows running the metals mcp server

3093. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 33
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

3094. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 33
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

3095. **[review-flow](https://github.com/DGouron/review-flow)** - ⭐ 33
   Automated AI code reviews powered — webhook-driven, real-time dashboard, MCP integration, smart queue with deduplication, multi-agent audits, and iterative follow-up reviews for GitLab MRs and GitHub PRs

3096. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 33

3097. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 33
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

3098. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 33
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

3099. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 33
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

3100. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

3101. **[kimi-code-mcp](https://github.com/howardpen9/kimi-code-mcp)** - ⭐ 33
   MCP server for Claude Code × Kimi K2.5 (256K context) — delegate bulk codebase analysis to Kimi, save 90% on token costs. Session caching, parallel agents, TypeScript.

3102. **[mini-coder](https://github.com/sacenox/mini-coder)** - ⭐ 33
   A good idea 👾

3103. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 33
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

3104. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 33
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

3105. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

3106. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 33
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

3107. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 33
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

3108. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 33
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

3109. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server and app for creating Datawrapper charts using AI assistants.

3110. **[xero-agent-toolkit](https://github.com/XeroAPI/xero-agent-toolkit)** - ⭐ 33
   A collection of examples demonstrating how to build AI agents that integrate with the Xero API using various agentic frameworks and the Xero MCP (Model Context Protocol) Server.

3111. **[levante](https://github.com/levante-hub/levante)** - ⭐ 33
   Levante - Personal, Secure, Free, Local AI, MCP Client

3112. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 33
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

3113. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 33
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

3114. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 32
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

3115. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

3116. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

3117. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

3118. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

3119. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 32
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

3120. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

3121. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

3122. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

3123. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 32
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

3124. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 32
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

3125. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 32
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

3126. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 32
   A Model Context Protocol server starter template

3127. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 32
   A collection of MCP server examples developed by various Java SDKs

3128. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 32
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

3129. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 32
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

3130. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 32
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

3131. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 32
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

3132. **[chabeau](https://github.com/permacommons/chabeau)** - ⭐ 32
   OpenAI-API compatible terminal chatbot and MCP client in Rust

3133. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 32
   Asterisk Model Context Protocol (MCP) server.

3134. **[myBrAIn](https://github.com/lilium360/myBrAIn)** - ⭐ 32
   myBrAIn is an MCP (Model Context Protocol) server designed to provide persistent and contextual memory to language models (like Google Antigravity). It acts as a "second brain" for your development environment, allowing the AI to remember project rules, architectural decisions, and technical insights across different chat sessions

3135. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 32
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

3136. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

3137. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 32
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

3138. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 32
   Query model running with Ollama from within Claude Desktop or other MCP clients

3139. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

3140. **[context-harness](https://github.com/parallax-labs/context-harness)** - ⭐ 32
   Local-first context ingestion and retrieval for AI tools. SQLite + embeddings + MCP server for Cursor & Claude.

3141. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 32
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

3142. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 32
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

3143. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

3144. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 32
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

3145. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 32
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

3146. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 32
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

3147. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 32
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

3148. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 32
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

3149. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 32
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

3150. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 32
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

3151. **[iota-agent-mcp](https://github.com/Scottcjn/iota-agent-mcp)** - ⭐ 32
   MCP server for IOTA blockchain — 20 tools for AI agent integration (wallet, Move CLI, on-chain queries via Model Context Protocol)

3152. **[jdwp-mcp](https://github.com/navicore/jdwp-mcp)** - ⭐ 32
   Java debugging for LLMs via JDWP and Model Context Protocol

3153. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 32
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

3154. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 32
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

3155. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 31
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

3156. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 31
   Model Context Protocol Server of Rod

3157. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

3158. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

3159. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

3160. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32. 

3161. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

3162. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 31
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

3163. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 31
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

3164. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

3165. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 31
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

3166. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

3167. **[ckan-mcp-server](https://github.com/ondata/ckan-mcp-server)** - ⭐ 31
   MCP server for querying CKAN open data portals (package search, DataStore SQL, organizations, groups, tags)

3168. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 31
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

3169. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 31
   MCP (Model Context Protocol) Server for postgres Database

3170. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 31
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

3171. **[rss-mcp](https://github.com/veithly/rss-mcp)** - ⭐ 31
   This is a Model Context Protocol (MCP) server built with TypeScript. It provides a versatile tool to fetch and parse any standard RSS/Atom feed, and also includes special support for RSSHub feeds. 

3172. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 31
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

3173. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 31
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

3174. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 31
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

3175. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 31
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

3176. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 31
   MCP (Model Context Protocol) server for biothings

3177. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 31
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

3178. **[lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server exposing Lucide icons as resources and tools for LLMs and agentic applications. Built with Bun and the MCP TypeScript SDK.

3179. **[mcp-musescore](https://github.com/ghchen99/mcp-musescore)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides programmatic control over MuseScore!

3180. **[mTarsier](https://github.com/mcp360/mTarsier)** - ⭐ 31
   mTarsier - The Open Source MCP Manager for Claude, Cursor, VS Code & any AI client.

3181. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 30
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

3182. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 30
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

3183. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

3184. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

3185. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

3186. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

3187. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

3188. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

3189. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

3190. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

3191. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

3192. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

3193. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 30
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

3194. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 30
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

3195. **[pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server)** - ⭐ 30
   PubNub MCP Model Context Protocol Server for use in Cursor, Windsurf, Claude Desktop, Claude Code and OpenAI Codex and more!

3196. **[mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm)** - ⭐ 30
   MCP server for Klever blockchain smart contract development

3197. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 30
   PowerPlatform Model Context Protocol server

3198. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 30
   A simple Model Context Protocol (MCP) server for Clay.

3199. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 30
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3200. **[hop](https://github.com/danmartuszewski/hop)** - ⭐ 30
   Fast, elegant SSH connection manager with a TUI dashboard and MCP server

3201. **[apipost-mcp](https://github.com/jlcodes99/apipost-mcp)** - ⭐ 30
   ApiPost API management tool based on MCP (Model Context Protocol), supporting complete interface documentation management and team collaboration. Features intelligent search, batch operations, and security management.

3202. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

3203. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

3204. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 30
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

3205. **[SpecialAgentPlugin](https://github.com/ArtisanGameworks/SpecialAgentPlugin)** - ⭐ 30
   SpecialAgent is an Unreal Engine 5 plugin that implements a Model Context Protocol (MCP)  server, allowing Large Language Models like Claude to programmatically interact with UE5  projects. With 71+ tool endpoints across 14 service categories, LLMs gain comprehensive control for building complex 3D environments.

3206. **[mcp-dblp](https://github.com/szeider/mcp-dblp)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides access to the DBLP computer science bibliography database for Large Language Models.

3207. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 30
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

3208. **[mcp-loxone](https://github.com/avrabe/mcp-loxone)** - ⭐ 30
   An opinionated Model Context Protocol (MCP) server for controlling Loxone home automation systems.

3209. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 30
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3210. **[unplugin-devpilot](https://github.com/zcf0508/unplugin-devpilot)** - ⭐ 30
   A universal plugin framework for development tools that enables seamless browser-server communication and MCP (Model Context Protocol) integration with AI/LLM systems.

3211. **[mcp_xpp](https://github.com/ccampora/mcp_xpp)** - ⭐ 30
   Experimental MCP server for Dynamics 365 F&O X++ development. Provides object creation, modification, and codebase navigation through the Model Context Protocol. Includes VS2022 service integration for D365 object handling.

3212. **[qgis-mcp](https://github.com/nkarasiak/qgis-mcp)** - ⭐ 30
   Connect QGIS to Claude AI through the Model Context Protocol (MCP)

3213. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 30
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

3214. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 29
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

3215. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 29
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

3216. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

3217. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

3218. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

3219. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 29
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

3220. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

3221. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 29
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

3222. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

3223. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

3224. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

3225. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

3226. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

3227. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

3228. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

3229. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

3230. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

3231. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 29
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

3232. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 29
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

3233. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

3234. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 29
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

3235. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 29
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

3236. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 29
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

3237. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 29
   Convert source code to LLM ready knowledge base

3238. **[izan.io](https://github.com/ekingunoncu/izan.io)** - ⭐ 29
   Turn Any Browser Action & Data Extraction into an AI Tool in 60 Seconds

3239. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 29
   Testing framework for Model Context Protocol (MCP)

3240. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 29
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

3241. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 29
   ESPN Fantasy API with LLMs!

3242. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 29
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

3243. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 29
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

3244. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 29
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

3245. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 29
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

3246. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 29
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

3247. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 29
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3248. **[drawio-mcp-extension](https://github.com/lgazo/drawio-mcp-extension)** - ⭐ 29
   Draw.io Model Context Protocol (MCP) Browser Extension

3249. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 29
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

3250. **[binance-mcp-server](https://github.com/ethancod1ng/binance-mcp-server)** - ⭐ 29
   A Model Context Protocol (MCP) server for integrating AI assistants with Binance cryptocurrency exchange APIs, enabling automated trading, market data access, and account management.

3251. **[emcp](https://github.com/PJUllrich/emcp)** - ⭐ 29
   A Model Context Protocol (MCP) Server for Elixir

3252. **[douyin-mcp-server](https://github.com/lancelin111/douyin-mcp-server)** - ⭐ 29
   🎥 Douyin (TikTok China) MCP Server - Automated video upload service via Model Context Protocol for AI integration

3253. **[tally-mcp-server](https://github.com/dhananjay1405/tally-mcp-server)** - ⭐ 29
   Tally Prime MCP (Model Context Protocol) Server implementation to feed Tally ERP data to popular LLM like Claude, ChatGPT supporting MCP

3254. **[inkmcp](https://github.com/Shriinivas/inkmcp)** - ⭐ 29
   Inkscape MCP Server - Control Inkscape through AI assistants via Model Context Protocol

3255. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 29
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

3256. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 28
   MCP (Model Context Protocol) server for Dumpling AI

3257. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 28
   A library for declaratively building Model Context Protocol servers.

3258. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 28
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

3259. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

3260. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

3261. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

3262. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

3263. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

3264. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 28
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

3265. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

3266. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 28
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

3267. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 28
   a web logging proxy for MCP client-server communication

3268. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 28
   Model Context Protocol to bridge in Substack writings to Claude.

3269. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 28
   Azure AI Foundry - Agents related sample code

3270. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 28
   Fast rust MCP proxy between stdio and SSE

3271. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 28
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

3272. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 28
   An implementation of Giphy integration with Model Context Protocol

3273. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 28
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

3274. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 28
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

3275. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 28
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

3276. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 28
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

3277. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 28
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

3278. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 28
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

3279. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 28
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

3280. **[autotask-mcp](https://github.com/wyre-technology/autotask-mcp)** - ⭐ 28
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3281. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 28
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

3282. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 28
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

3283. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 28
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

3284. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 28
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3285. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 28
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

3286. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 28
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

3287. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 28
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

3288. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 28
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

3289. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

3290. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 28
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

3291. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3292. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 28
   Antrophics Model context protocol to edit powerpoint files

3293. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 28
   A Model Context Protocol server for 3D Slicer integration

3294. **[chat](https://github.com/repaera/chat)** - ⭐ 28
   Chat Client for Your Service's MCP Server

3295. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 27
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

3296. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 27
   MCP to LangChain Tools Conversion Utility / Python

3297. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

3298. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

3299. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

3300. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

3301. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

3302. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

3303. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

3304. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 27
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

3305. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

3306. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 27
   The Runtime Where AI Agents Build, Ship, and Evolve. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

3307. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

3308. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 27
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

3309. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 27
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

3310. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 27
   Model Context Protocol Server for NebulaGraph 3.x

3311. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 27
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

3312. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 27
   Simple MCP to give Claude ability to check current time as well as know when holidays are, what is the time distance between dates etc.

3313. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

3314. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 27
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

3315. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 27
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

3316. **[computeruseprotocol](https://github.com/computeruseprotocol/computeruseprotocol)** - ⭐ 27
   Computer Use Protocol is a universal schema for AI agents to perceive and interact with any desktop UI.

3317. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 27
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

3318. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 27
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

3319. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 27
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3320. **[janee](https://github.com/rsdouglas/janee)** - ⭐ 27
   Secrets management for AI agents via MCP • @janeesecure

3321. **[rustchain-mcp](https://github.com/Scottcjn/rustchain-mcp)** - ⭐ 27
   MCP server for RustChain blockchain and BoTTube video platform — AI agent tools for earning RTC tokens. Built on createkr's RustChain SDK.

3322. **[openzeppelin-mcp](https://github.com/OpenZeppelin/openzeppelin-mcp)** - ⭐ 27
   Model Context Protocol Servers Repository for OpenZeppelin products

3323. **[raybridge](https://github.com/jlokos/raybridge)** - ⭐ 27
   MCP server that bridges Raycast extensions to any MCP-compatible client

3324. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 27
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3325. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 27
   Educational repo for MCP streamable HTTP servers and clients

3326. **[agent-trace](https://github.com/Siddhant-K-code/agent-trace)** - ⭐ 27
   strace for AI agents. Capture and replay every tool call, prompt, and response from Claude Code, Cursor, or any MCP client

3327. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

3328. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

3329. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

3330. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

3331. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

3332. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 26
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

3333. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy 

3334. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 26
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

3335. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for GreptimeDB

3336. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 26
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

3337. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 26
   Model Context Protocol server for Github Repo // Reading Github Repo

3338. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 26
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

3339. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 26
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

3340. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 26
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

3341. **[markview](https://github.com/paulhkang94/markview)** - ⭐ 26
   Native macOS markdown preview app. Swift/SwiftUI, GitHub Flavored Markdown, syntax highlighting, linting, plugins. No Electron.

3342. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

3343. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 26
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

3344. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 26
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

3345. **[MCPHammer](https://github.com/praetorian-inc/MCPHammer)** - ⭐ 26
   MCP security testing framework for evaluating Model Context Protocol server vulnerabilities

3346. **[awesome-finance-mcp](https://github.com/BlockRunAI/awesome-finance-mcp)** - ⭐ 26
   A curated list of MCP servers for AI finance agents

3347. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 26
   Local FAISS vector store as an MCP server – Agent Memory, drop-in local semantic search for Claude / Copilot / Agents.

3348. **[novyx-mcp](https://github.com/novyxlabs/novyx-mcp)** - ⭐ 26
   Persistent memory for AI agents. 91 MCP tools for remember, recall, rollback, audit, knowledge graph, eval, cortex, replay, governed actions, threat intel, auto-defense, and more. Works locally (zero config) or with Novyx Cloud.

3349. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 26
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

3350. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 26
   MCP server to expose local zotero repository to MCP clients 

3351. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 26
   An MCP Server and client for communicating with Nifi (v1.28)

3352. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

3353. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

3354. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

3355. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

3356. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

3357. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

3358. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

3359. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3360. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

3361. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

3362. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

3363. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

3364. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 25
   A Curated List of MCP Servers, Clients and Toolkits

3365. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

3366. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 25
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

3367. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 25
   Message Communication Protocol server for json2video API integration

3368. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 25
   Simple MCP Client for remote MCP Servers 🌐

3369. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 25
   Simple MCP SDK in Java

3370. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 25
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

3371. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 25
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

3372. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 25
   A Fastify plugin to run Model Context Protocol (MCP) servers

3373. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

3374. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 25
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

3375. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 25
   An MCP server enabling CFBD API queries within Claude Desktop.

3376. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 25
   MCP server wrapping around the Fabric Rest API

3377. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 25
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

3378. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 25
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets. 

3379. **[gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp)** - ⭐ 25
   MCP server for Google Gemini — free image generation, editing & chat via browser cookies. No API keys needed.

3380. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 25
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3381. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3382. **[Screenhand](https://github.com/manushi4/Screenhand)** - ⭐ 25
   Give AI eyes and hands on your desktop. Open-source MCP server for desktop automation — screenshots, UI control, browser automation, OCR. Works with Claude, Cursor, and any MCP client. macOS + Windows.

3383. **[stitch-mcp-auto](https://github.com/GreenSheep01201/stitch-mcp-auto)** - ⭐ 25
   Automated installer for Stitch MCP - The easiest way to set up your Universal MCP server for Google Stitch.

3384. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

3385. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 25
   An MCP server and client for LLMs to interact with Unity Projects

3386. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 24
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

3387. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

3388. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

3389. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

3390. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

3391. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

3392. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3393. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

3394. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

3395. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

3396. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

3397. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

3398. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

3399. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

3400. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

3401. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

3402. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

3403. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

3404. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

3405. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

3406. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

3407. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

3408. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

3409. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 24
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

3410. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 24
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + Java + TypeScript

3411. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 24
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

3412. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 24
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

3413. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 24
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3414. **[agentgate](https://github.com/agentkitai/agentgate)** - ⭐ 24
   Approval workflows for AI agents

3415. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 24
   Memory Cache Server for use with supported MCP API Clients.

3416. **[WikidataMCP](https://github.com/philippesaade-wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3417. **[WikidataMCP](https://github.com/wmde/WikidataMCP)** - ⭐ 24
   Model Context Protocol for Wikidata

3418. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 24
   CLI for calling successive MCP Server tools

3419. **[minimal-godot-mcp](https://github.com/ryanmazzolini/minimal-godot-mcp)** - ⭐ 24
   Lightweight MCP server bridging Godot LSP to MCP clients for GDScript validation

3420. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/cortexaiofficial/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3421. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 24
   🧬 Analyze spatial transcriptomics data through natural language conversation. Stop writing code, start having conversations with your data. MCP server for Claude Code and Codex.

3422. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 24
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

3423. **[Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine](https://github.com/Cortex-AI-Software/Autonomous-AI-Trading-Agent-MCP-Flash-Arb-Engine)** - ⭐ 24
   🧠 Autonomous AI Trading Agent & Multi-Chain Flash-Arb Engine (v2.0 Beta). Powered by MCP-Protocol & LLM reasoning. High-frequency arbitrage on Solana, Base, and EVM L2s. Built by Cortex Software Labs.

3424. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 24
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

3425. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 24
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

3426. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 24
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

3427. **[trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp)** - ⭐ 24
   TrainingPeaks MCP server for Claude Desktop, Code and Cowork. No API approval needed - works with any account. Query workouts, CTL/ATL/TSB fitness data, power PRs via natural language.

3428. **[webmcp-bridge](https://github.com/holon-run/webmcp-bridge)** - ⭐ 24
   Bridge local MCP clients to browser WebMCP tools through Playwright, using native WebMCP when available and injected adapters when not.

3429. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 24
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3430. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 23
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

3431. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

3432. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

3433. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

3434. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3435. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

3436. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

3437. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

3438. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

3439. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

3440. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

3441. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

3442. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

3443. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

3444. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

3445. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 23
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

3446. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 23
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

3447. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 23
   Tanzu Platform Chat

3448. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 23
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3449. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 23
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

3450. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 23
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3451. **[agent-studio-starter](https://github.com/nsphung/agent-studio-starter)** - ⭐ 23
   Stop building AI agents from scratch. Bootstrap starter Agent app with LangGraph, CopilotKit, and beautiful Generative UIs.

3452. **[orionbelt-semantic-layer](https://github.com/ralfbecher/orionbelt-semantic-layer)** - ⭐ 23
   API-first semantic engine and query planner for AI agents that compiles declarative YAML models into optimized, dialect-specific SQL across BigQuery, PostgreSQL, Snowflake, ClickHouse, Dremio, Databricks, DuckDB, and MySQL.

3453. **[fcpxml-mcp-server](https://github.com/DareDev256/fcpxml-mcp-server)** - ⭐ 23
   🎬 The first AI-powered MCP server for Final Cut Pro XML. Control your edits with natural language.

3454. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 23
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3455. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 23
   MCP to LangChain Tools Conversion Utility / TypeScript

3456. **[coworker](https://github.com/Array-Ventures/coworker)** - ⭐ 23
   Open-source AI agent with MCP UI, app builder, A2A protocol, skills marketplace, and multi-provider chat. Built with Mastra. Alternative to OpenClaw.

3457. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 23
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3458. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 23
   Pre-release - Model Context Protocol server for Rollbar

3459. **[stata-workbench](https://github.com/tmonk/stata-workbench)** - ⭐ 23
   A VS Code compatible extension (Cursor, Windsurf, Antigravity etc.) that allows Stata code to be run directly from the editor. Enables AI agents to directly interact with Stata. Powered by mcp-stata, https://github.com/tmonk/mcp-stata.

3460. **[roblox-executor-mcp](https://github.com/notpoiu/roblox-executor-mcp)** - ⭐ 23
   A MCP Server which allows for direct access to the roblox game client

3461. **[twincat-validator-mcp](https://github.com/agenticcontrolio/twincat-validator-mcp)** - ⭐ 23
   An MCP server that validates, auto-fixes, and scaffolds TwinCAT 3 XML files. Connect it to any LLM client to give your AI assistant reliable, deterministic TwinCAT code quality tooling — structural checks, 21 IEC 61131-3 OOP checks, auto-fix pipelines, and canonical skeleton generation.

3462. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

3463. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

3464. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

3465. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

3466. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

3467. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

3468. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

3469. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

3470. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

3471. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

3472. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

3473. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

3474. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

3475. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

3476. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 22
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

3477. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 22
   Rust MCP framework for building AI agents

3478. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 22
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

3479. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 22
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3480. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 22
   A collection of mcp servers/client/sdks

3481. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 22
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

3482. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 22
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3483. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 22
   MCP agent/client/server implementation for private knowledge base

3484. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 22
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

3485. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 22
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3486. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 22
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3487. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 22
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

3488. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 22
   The Decodo MCP server which enables MCP clients to interface with services.

3489. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 22
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3490. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 22
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

3491. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 22
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

3492. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 22
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

3493. **[ads-mcp](https://github.com/amekala/ads-mcp)** - ⭐ 22
   MCP server for managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. 100+ tools for campaign creation, performance analysis, keyword research, and budget optimization. Works with Claude Code, Cursor, Codex, ChatGPT, Windsurf, and Cline.

3494. **[Unity-AI-ParticleSystem](https://github.com/IvanMurzak/Unity-AI-ParticleSystem)** - ⭐ 22
   AI-powered tools for Unity Particle System. Create and modify Particle System directly through natural language commands.

3495. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 22
   A comprehensive Model Context Protocol (MCP) library for Zig — bringing MCP support to the Zig ecosystem.

3496. **[spectrawl](https://github.com/Pyx-Corp/spectrawl)** - ⭐ 22
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

3497. **[mcp-superset](https://github.com/bintocher/mcp-superset)** - ⭐ 22
   MCP server for managing Apache Superset — 128+ tools for dashboards, charts, datasets, SQL Lab, access control

3498. **[Jiva](https://github.com/KarmaloopAI/Jiva)** - ⭐ 22
   Jiva is a CLI-first, open source autonomous AI agent and open alternative to Claude. Built in TypeScript with a three-agent architecture (Manager, Worker, Client), it autonomously plans and executes tasks from your terminal. Supports MCP servers, a built-in Skills system, and Jiva Personas - a plugin framework fully compatible with Claude Plugins.

3499. **[pixelpanda-mcp](https://github.com/RyanKramer/pixelpanda-mcp)** - ⭐ 22
   MCP server for PixelPanda — 31 AI image processing tools for Claude Desktop, Cursor & other MCP clients

3500. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 21
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

3501. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 21
   Supabase MCP client react app with Tambo

3502. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

3503. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

3504. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

3505. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

3506. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

3507. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

3508. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

3509. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

3510. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

3511. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

3512. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

3513. **[plux](https://github.com/milisp/plux)** - ⭐ 21
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

3514. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

3515. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 21
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

3516. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 21
   Haskell server/client for MCP (Model Context Protocol)

3517. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 21
   MCP server to integrate AWS S3 and LLM

3518. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 21
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

3519. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 21
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

3520. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 21
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

3521. **[heuristic-mcp](https://github.com/softerist/heuristic-mcp)** - ⭐ 21
   Enhanced MCP server for semantic code search with call-graph proximity, recency ranking, and find-similar-code. Built for AI coding assistants.

3522. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 21
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

3523. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 21
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

3524. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

3525. **[codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool)** - ⭐ 21

3526. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 21

3527. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 21
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

3528. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 21
   The BioContextAI Registry for biomedical MCP servers

3529. **[archmcp](https://github.com/dejo1307/archmcp)** - ⭐ 21
   archmcp - MCP Architectural Snapshot Server and Knowledge Graph

3530. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 21
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3531. **[email-mcp](https://github.com/codefuturist/email-mcp)** - ⭐ 21
   Email MCP server with full IMAP + SMTP support — read, search, send, manage, and organize email from any AI assistant via the Model Context Protocol

3532. **[agentidentityprotocol](https://github.com/openagentidentityprotocol/agentidentityprotocol)** - ⭐ 21
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3533. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 21
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

3534. **[codeTree](https://github.com/ThinkyMiner/codeTree)** - ⭐ 21
   MCP server with 23 tools for structured code understanding via tree-sitter. 10 languages. 999 tests. One-command install.

3535. **[turn-mcp](https://github.com/shiahonb777/turn-mcp)** - ⭐ 21
   Achieve infinite conversation turns in a single API request via turn-mcp.             Self-hosted MCP server with browser console for human-in-the-loop AI agents.

3536. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 21
   BioContextAI Knowledgebase MCP server for biomedical agentic AI 

3537. **[mcp-kling](https://github.com/199-mcp/mcp-kling)** - ⭐ 21
   🎬 The FIRST MCP server for Kling AI video generation! Generate stunning AI videos directly from Claude.

3538. **[mcp-anything](https://github.com/Type-MCP/mcp-anything)** - ⭐ 21
   One command to turn any codebase into an MCP server

3539. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 21
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

3540. **[dsers-mcp-product](https://github.com/lofder/dsers-mcp-product)** - ⭐ 21
   An open-source MCP server to automate DSers product import, bulk edit variants, and push to Shopify/Wix/WooCommerce using AI. Supports AliExpress, Alibaba, 1688.

3541. **[agentic-tools](https://github.com/meta-quest/agentic-tools)** - ⭐ 21
   Agent Tool and Skills for VR Development on Meta Quest 

3542. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 21
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3543. **[ue5-mcp-bridge](https://github.com/Natfii/ue5-mcp-bridge)** - ⭐ 21
   MCP server bridging AI assistants to Unreal Engine 5 editor

3544. **[ARBuilder](https://github.com/Quantum3-Labs/ARBuilder)** - ⭐ 21
   AI-powered code generator for Arbitrum Stylus, SDK bridging, dApps & Orbit chains — 19 MCP tools with RAG

3545. **[aura](https://github.com/mezmo/aura)** - ⭐ 21
   A production-ready framework for composing AI agents from declarative TOML configuration, with MCP tool integration, RAG pipelines, and an OpenAI-compatible web API.

3546. **[mcp-scan](https://github.com/rodolfboctor/mcp-scan)** - ⭐ 21
   Security scanner for MCP server configurations. Detects secrets, CVEs, permission issues, and exfiltration vectors across 10 AI tool clients.

3547. **[onec-client-mcp-devkit](https://github.com/1c-neurofish/onec-client-mcp-devkit)** - ⭐ 21
   Реализация MCP сервера, который запускается в клиенте 1С:Предприятие

3548. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 21
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

3549. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 21
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3550. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 21
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3551. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 21
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3552. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 21
   MCP server and client for running Linux commands

3553. **[MCP-DB-Client](https://github.com/DitriXNew/MCP-DB-Client)** - ⭐ 21
   MCP layer for 1C

3554. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

3555. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

3556. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

3557. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

3558. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

3559. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 20
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

3560. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 20
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3561. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 20
   MCP Server for fething yfinance financial data into Claude Desktop

3562. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 20
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

3563. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 20
   Connect to any MCP servers using agents

3564. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 20
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3565. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 20
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

3566. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 20
   HasMCP Community Edition

3567. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 20
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

3568. **[muster](https://github.com/giantswarm/muster)** - ⭐ 20
   MCP tool management and workflow proxy

3569. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 20
   A GitHub CLI extension that seamlessly runs the github-mcp-server using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

3570. **[Intercept](https://github.com/PolicyLayer/Intercept)** - ⭐ 20
   The control layer for AI agents. Intercept enforces hard limits on every MCP tool call before execution. Rate limits, spend caps, access controls. Open source.

3571. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 20
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

3572. **[starbase](https://github.com/metorial/starbase)** - ⭐ 20
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

3573. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 20
   a Nushell cross.stream extension to interact with LLMs and MCP servers

3574. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 20
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

3575. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 20
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3576. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 20

3577. **[monolith](https://github.com/tumourlove/monolith)** - ⭐ 20
   MCP plugin for Unreal Engine 5.7 — gives AI assistants full read/write access to Blueprints, Materials, Niagara VFX, Animation, IKRig, Control Rig, and more. 290 actions across 9 modules.

3578. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 19
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

3579. **[opencode-mcp](https://github.com/AlaeddineMessadi/opencode-mcp)** - ⭐ 19
   MCP server for OpenCode AI — 70 tools, 10 resources, 5 prompts. Use npx opencode-mcp with Claude Desktop, Claude Code, Cursor, Windsurf, or any MCP client.

3580. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

3581. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

3582. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 19
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

3583. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

3584. **[termlink](https://github.com/chu2bard/termlink)** - ⭐ 19
   MCP server for shell and terminal operations

3585. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

3586. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 19
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

3587. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 19
   Yandex Cloud MCP Servers

3588. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 19
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

3589. **[bonnard](https://github.com/bonnard-data/bonnard)** - ⭐ 19
   Open-source agentic schema for reliable data outputs. Query data through MCP and via our SDK. Create apps, embed data or just simply explore through your preferred agent.

3590. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 19
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3591. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 19
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

3592. **[spectrawl](https://github.com/FayAndXan/spectrawl)** - ⭐ 19
   The unified web layer for AI agents. Search (8 engines), stealth browse, auth, and act on 24 platforms. One npm install, self-hosted.

3593. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 19
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

3594. **[unified-gateway-mcp](https://github.com/mcp360/unified-gateway-mcp)** - ⭐ 19
   Unified MCP Gateway Platform, Marketplace & Custom MCPs

3595. **[subcog](https://github.com/zircote/subcog)** - ⭐ 19
   Persistent memory system for AI coding assistants. Captures decisions, learnings, and context from coding sessions. Features hybrid search (semantic + BM25), MCP server integration, SQLite persistence with knowledge graph, and proactive memory surfacing. Written in Rust.

3596. **[builtwith-api](https://github.com/zcaceres/builtwith-api)** - ⭐ 19
   TypeScript library, MCP, and agent-friendly CLI for the BuiltWith API.

3597. **[better-notion-mcp](https://github.com/n24q02m/better-notion-mcp)** - ⭐ 19
   Markdown-first MCP server for Notion API - composite tools optimized for AI agents

3598. **[mcp-anything](https://github.com/gabrielekarra/mcp-anything)** - ⭐ 19
   One command to turn any codebase into an MCP server

3599. **[nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp)** - ⭐ 19
   Gemini Vision & Image Generation MCP for Claude Desktop and Claude Code

3600. **[awesome-mcp-security](https://github.com/AgentSeal/awesome-mcp-security)** - ⭐ 19
   Security scores for 800+ MCP servers. 9 analyzers scan for prompt injection, toxic flows, and attack surface risks. Updated daily. 🛡️

3601. **[ue5-mcp](https://github.com/mirno-ehf/ue5-mcp)** - ⭐ 19
   Let AI edit your Unreal Engine Blueprints. MCP server plugin for Claude Code — describe what you want in plain English.

3602. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 19
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

3603. **[resonant](https://github.com/codependentai/resonant)** - ⭐ 19
   Open-source relational AI framework with identity persistence, memory, and MCP integration. Build relationship-aware AI agents that remember, grow, and maintain continuity. Built on Claude Agent SDK.

3604. **[overleaf-mcp-server](https://github.com/YounesBensafia/overleaf-mcp-server)** - ⭐ 19
   MCP server for Overleaf projects. Syncs LaTeX files via Git, parses sections, equations, and citations, and exposes them to AI clients for assisted paper review, LaTeX fixes, and content generation.

3605. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 19
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

3606. **[daiv](https://github.com/srtab/daiv)** - ⭐ 18
   Your AI-powered SWE teammate, built into your git workflow

3607. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 18
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

3608. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 18
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database. 

3609. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 18
   A fetch API based TypeScript SDK for MCP

3610. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

3611. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

3612. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

3613. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

3614. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

3615. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

3616. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

3617. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

3618. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 18
   Model Context Protocol (MCP)

3619. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 18
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

3620. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 18
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

3621. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 18
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

3622. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 18
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

3623. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server implementation for Gumroad API

3624. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 18
   A command-line utility for interacting with MCP servers.

3625. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 18
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

3626. **[toolhive-catalog](https://github.com/stacklok/toolhive-catalog)** - ⭐ 18
   ToolHive's registry catalog of MCP servers

3627. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 18
   The immune system for AI coding agents

3628. **[robotmem](https://github.com/robotmem/robotmem)** - ⭐ 18
   Robot Memory - Persistent memory system for AI robots. MCP Server + hybrid search + spatial retrieval.

3629. **[speclock](https://github.com/sgroy10/speclock)** - ⭐ 18
   AI Constraint Engine by Sandeep Roy — stops AI from breaking what you locked. 100/100 on Claude's adversarial test suite. 42 MCP tools. Works with Bolt.new, Lovable, Claude Code, Cursor. Free & open source.

3630. **[agentify](https://github.com/koriyoshi2041/agentify)** - ⭐ 18
   Agent Interface Compiler — One command. Every agent speaks your product. Transform OpenAPI specs into MCP Servers, Skills, CLAUDE.md, AGENTS.md, and more.

3631. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 18
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

3632. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 18
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

3633. **[scopus-mcp](https://github.com/qwe4559999/scopus-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server for Elsevier Scopus. Allows AI assistants like Claude to search academic papers, retrieve abstracts, and analyze author profiles directly.

3634. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 18
   simple mcp server for interacting with local obsidian notes

3635. **[ContextOS](https://github.com/itallstartedwithaidea/ContextOS)** - ⭐ 18
   Unified MCP context intelligence platform — pip-installable CLI that absorbed 6 foundational repos. Context engineering for AI agents.

3636. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 18
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

3637. **[openrouter-mcp-multimodal](https://github.com/stabgan/openrouter-mcp-multimodal)** - ⭐ 18
   MCP server for OpenRouter providing text chat and image analysis tools

3638. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 18
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

3639. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 18

3640. **[awesome-agent-skills-mcp](https://github.com/shadowrootdev/awesome-agent-skills-mcp)** - ⭐ 18
   MCP server providing 100+ AI agent skills from Anthropic, Vercel, Trail of Bits, Hugging Face & more. Works with Claude, GitHub Copilot, and any MCP client.

3641. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 18
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

3642. **[MicrosoftGraph_Transcript_MCP](https://github.com/ITSpecialist111/MicrosoftGraph_Transcript_MCP)** - ⭐ 18
   A remote Model Context Protocol (MCP) server that retrieves Microsoft Teams meeting transcripts via the Microsoft Graph API, using delegated **OAuth 2.0 On-Behalf-Of (OBO)** authentication.  Designed for integration with Microsoft Copilot Studio (via the MCP Wizard), though any MCP-compatible client can connect.

3643. **[houtini-lm](https://github.com/houtini-ai/houtini-lm)** - ⭐ 18
   MCP server that saves Claude Code tokens by delegating bounded tasks to local or cloud LLMs. 93% token savings benchmarked. Works with LM Studio, Ollama, vLLM, DeepSeek, Groq, Cerebras.

3644. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 18
   An extensible AI agents framework

3645. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

3646. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

3647. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

3648. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

3649. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

3650. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

3651. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

3652. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

3653. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

3654. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 17
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

3655. **[rpc-nodes-mcp](https://github.com/chainstacklabs/rpc-nodes-mcp)** - ⭐ 17
   Minimal, fast, and extensible MCP server for interactions with JSON-RPC blockchain nodes

3656. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 17
   MCP server for graph representation of a codebase

3657. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 17
   An MCP client that uses signal for sending and receiving messages.

3658. **[mcpforge](https://github.com/lorenzosaraiva/mcpforge)** - ⭐ 17

3659. **[mcp-ecosystem](https://github.com/SynkraAI/mcp-ecosystem)** - ⭐ 17
   MCP Ecosystem: Docker MCP Toolkit, IDE Configs & Presets for AIOS

3660. **[lightdash_mcp](https://github.com/poddubnyoleg/lightdash_mcp)** - ⭐ 17
   mcp server for lightdash

3661. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 17
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

3662. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 17
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

3663. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 17
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

3664. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 17
   A model-agnostic MCP Client-Server for .Net and Unity

3665. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 17
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

3666. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 17
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

3667. **[FocusRelayMCP](https://github.com/deverman/FocusRelayMCP)** - ⭐ 17
   Talk to your OmniFocus tasks. An OmniFocus MCP server that lets AI assistants query your tasks, projects, and tags using natural language—no more clicking through endless lists.

3668. **[extract-llms-docs](https://github.com/nirholas/extract-llms-docs)** - ⭐ 17
   Extract documentation for AI agents from any site with llms.txt support. Features MCP server, REST API, batch processing, and multiple export formats.

3669. **[OmniClip-RAG](https://github.com/msjsc001/OmniClip-RAG)** - ⭐ 17
   Local-first RAG desktop app & official MCP Server. Let any AI instantly search your private Markdown, PDF, and 1290+ document formats. (本地优先的 RAG 桌面端与官方 MCP 服务器。让任意 AI 瞬间检索你的私有 Markdown、PDF 及 1290+ 种文档格式。)

3670. **[video-research-mcp](https://github.com/Galbaz1/video-research-mcp)** - ⭐ 17
   Give Claude Code 41 research & video tools with one command. Video analysis, deep research, content extraction, explainer video creation, and Weaviate vector search — powered by Gemini 3.1 Pro.

3671. **[opencode-browser](https://github.com/michaljach/opencode-browser)** - ⭐ 17
   Browser automation plugin for OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via MCP integration

3672. **[Go-High-Level-MCP-2026-Complete](https://github.com/BusyBee3333/Go-High-Level-MCP-2026-Complete)** - ⭐ 17
   GoHighLevel MCP Server — 520+ tools across 40 categories. Voice AI, Proposals, Contacts, Calendars, Conversations, Opportunities, Invoices, Payments, Workflows, Social Media, and more. MCP SDK 1.26, Streamable HTTP, tool annotations.

3673. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 17
   MCP server and client for Frontapp

3674. **[XcodeMCPWrapper](https://github.com/SoundBlaster/XcodeMCPWrapper)** - ⭐ 17
   MCP that makes Xcode 26.3's MCP compatible with Cursor and other strict MCP-spec-compliant clients

3675. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 17
   MCP server to manage Spotify from MCP clients

3676. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 17
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

3677. **[swift-mcp](https://github.com/DePasqualeOrg/swift-mcp)** - ⭐ 17
   Full-featured Swift SDK for Model Context Protocol servers and clients

3678. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 17
   Session-based Slack MCP for Claude and MCP clients: local-first workflows, secure-default HTTP.

3679. **[nasa](https://github.com/peteretelej/nasa)** - ⭐ 17
   Go client library for NASA APIs: APOD, NeoWs, DONKI, NASA Image Library, SSD/CNEOS, EONET. Supports built-in rate-limiting, a CLI & MCP Server

3680. **[localwp-agent-tools](https://github.com/10up/localwp-agent-tools)** - ⭐ 17
   A Local add-on that provides an MCP server, skills, and project context for AI-powered WordPress development. Works with Claude Code, Cursor, Windsurf, VS Code Copilot, and any MCP client.

3681. **[askr](https://github.com/Sweatent/askr)** - ⭐ 17
   MCP Q&A Assistant - Async Q&A capabilities for AI clients via MCP protocol

3682. **[mcp-client-cli](https://github.com/addity3/mcp-client-cli)** - ⭐ 16
   cli-based program to run llm prompt and mcp

3683. **[claude-vigil-mcp](https://github.com/Vvkmnn/claude-vigil-mcp)** - ⭐ 16
   🏺 An MCP server for checkpointing and file recovery in Claude Code

3684. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

3685. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

3686. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

3687. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

3688. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

3689. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

3690. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

3691. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3692. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 16
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

3693. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

3694. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

3695. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 16
   Language to Maps

3696. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 16
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

3697. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 16
   MCP server for xAI Grok — read and serve .faf project context. npm: grok-faf-mcp

3698. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 16
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

3699. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 16
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

3700. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 16
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

3701. **[penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** - ⭐ 16
   MCP server for Penpot - Connect AI assistants to Penpot design platform via Model Context Protocol

3702. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 16

3703. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 16
   MCP server for penetration testing

3704. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 16
   An MCP server to read MCP logs to debug directly inside the client

3705. **[drf-mcp-docs](https://github.com/Abdulkhalek-1/drf-mcp-docs)** - ⭐ 16
   API documentation via MCP for AI coding agents

3706. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 16
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

3707. **[LSP4J-MCP](https://github.com/stephanj/LSP4J-MCP)** - ⭐ 16
   A Java MCP (Model Context Protocol) server that wraps JDTLS (Eclipse JDT Language Server) using LSP4J to provide Java IDE features to AI assistants like Claude.

3708. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 16
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

3709. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 16
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

3710. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 16
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

3711. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 16
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

3712. **[shodan-mcp](https://github.com/Vorota-ai/shodan-mcp)** - ⭐ 16
   Shodan MCP server for Claude, Cursor & VS Code. 20 tools for passive reconnaissance, CVE/CPE intelligence, DNS analysis, and device search. 4 tools work free without an API key. OSINT and vulnerability research from your IDE.

3713. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 16
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

3714. **[webmcp-react](https://github.com/MCPCat/webmcp-react)** - ⭐ 16
   React hooks for exposing your app's functionality as WebMCP tools - transport-agnostic, SSR-safe, Strict Mode safe, W3C spec-aligned

3715. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 16
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3716. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 16
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

3717. **[mcp-server-zotero-dev](https://github.com/introfini/mcp-server-zotero-dev)** - ⭐ 16
   Give your AI assistant superpowers for Zotero plugin development. 25 tools for screenshots, DOM inspection, JavaScript execution, build integration, and debugging via Model Context Protocol.

3718. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 16
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

3719. **[ProxmoxMCP-advance](https://github.com/Markermav/ProxmoxMCP-advance)** - ⭐ 16
   ProxmoxMCP (advance): MCP for Proxmox integration in Claude, Goose, Cline, any client.

3720. **[ida-codex-mcp](https://github.com/Iamgublin/ida-codex-mcp)** - ⭐ 16
   IDA Codex MCP bridges IDA Pro 9.2 with the MCP ecosystem. It provides an IDA plugin and a stdio MCP server that expose   function lists, call graphs, Hex‑Rays pseudocode, disassembly, imports/exports, xrefs, strings, and memory reads to   MCP clients.

3721. **[screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp)** - ⭐ 16
   MCP server for Screaming Frog SEO Spider – crawl sites, export data, and manage crawl storage via Claude or any MCP-compatible client

3722. **[bruno-mcp](https://github.com/macarthy/bruno-mcp)** - ⭐ 16
   🚀 MCP server for generating Bruno API testing files programmatically. Create collections, environments, requests, and test scripts using AI clients like Claude Desktop.

3723. **[faf](https://github.com/Wolfe-Jam/faf)** - ⭐ 15
   FAF specification — IANA-registered AI context format (application/vnd.faf+yaml)

3724. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

3725. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

3726. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

3727. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data 

3728. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

3729. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 15
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

3730. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

3731. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 15
   Unity Catalog AI Model Context Protocol Server

3732. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 15
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

3733. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 15
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

3734. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 15
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

3735. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 15
   A web-based client for connecting to MCP servers with OAuth support

3736. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 15
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

3737. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 15
   A Socratic dialogue engine for AI agents. 

3738. **[mcp](https://github.com/local-falcon/mcp)** - ⭐ 15
   MCP server for Local Falcon's local SEO and AI visibility platform: geo-grid rank tracking, campaign management, and competitor analysis via Model Context Protocol

3739. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 15
   MCP server for Open Targets Data

3740. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 15
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

3741. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 15
   Markdown To PDF Conversion MCP

3742. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 15
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

3743. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 15
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

3744. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 15
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

3745. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 15
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics 

3746. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 15
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

3747. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 15
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

3748. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 15
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

3749. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 15
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

3750. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 15
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

3751. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 15
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

3752. **[agent-board](https://github.com/quentintou/agent-board)** - ⭐ 15
   Open-source multi-agent task board for OpenClaw. Kanban + DAG dependencies + MCP server + auto-retry + audit trail. Built for autonomous AI agent teams.

3753. **[cuba-memorys](https://github.com/LeandroPG19/cuba-memorys)** - ⭐ 15
   🧠 Persistent memory MCP for AI agents — Knowledge graph + Hebbian learning + Anti-hallucination. 12 tools, 1 dependency, zero manual setup.

3754. **[mcpskills-cli](https://github.com/dhanababum/mcpskills-cli)** - ⭐ 15
   Generate Agent Skills from MCP server tools. Connects via Streamable HTTP, discovers tools, and outputs a skill with schema docs and a call script in the language of your choice.

3755. **[opentrace](https://github.com/adham90/opentrace)** - ⭐ 15
   Self-hosted observability server with 75+ MCP tools. Ingest logs, connect Postgres, monitor servers — then debug it all from Claude, Cursor, or any MCP client.

3756. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 15
   Awesome list of MCP servers for interacting with hardware and the physical world.

3757. **[atxp](https://github.com/atxp-dev/atxp)** - ⭐ 15
   Give your AI agent a wallet, email, phone number, and instant access to paid MCP tools — web search, image/video/music gen, X search, SMS, voice calls, code execution, and more. Works with Gemini CLI, Claude, and any MCP client.

3758. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 15
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

3759. **[asc-mcp](https://github.com/zelentsov-dev/asc-mcp)** - ⭐ 15
   MCP server for App Store Connect API — 208 tools for managing apps, builds, TestFlight, subscriptions, and more from Claude, Cursor, VS Code, or any MCP client

3760. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 15
   MCP Client for Gemma-3

3761. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 15
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

3762. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

3763. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

3764. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

3765. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

3766. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

3767. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

3768. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server 

3769. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3770. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

3771. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

3772. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 14
   Official ConfigCat Model Context Protocol (MCP) Server 

3773. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 14
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

3774. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 14
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

3775. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 14

3776. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 14
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

3777. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 14
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

3778. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

3779. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 14
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

3780. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 14
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

3781. **[webfetch-mcp](https://github.com/manooll/webfetch-mcp)** - ⭐ 14
   Live Web Access for Your Local AI — Tunable Search & Clean Content Extraction

3782. **[domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp)** - ⭐ 14
   Zero-config domain availability MCP for Claude & ChatGPT. AI suggestions, premium/auction detection via GoDaddy, RDAP/WHOIS fallback. Stdio + HTTP.

3783. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 14
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

3784. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 14
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

3785. **[phabricator-mcp](https://github.com/freelancer/phabricator-mcp)** - ⭐ 14
   MCP server for Phabricator

3786. **[openalex-research-mcp](https://github.com/oksure/openalex-research-mcp)** - ⭐ 14
   MCP server for the OpenAlex API — search 240M+ scholarly works, analyze citations, track research trends, and map collaboration networks

3787. **[claude-praetorian-mcp](https://github.com/Vvkmnn/claude-praetorian-mcp)** - ⭐ 14
   ⚜️ An MCP server for context compaction and recycling in Claude Code

3788. **[servicenow-mcp](https://github.com/aartiq/servicenow-mcp)** - ⭐ 14
   Production-ready Model Context Protocol server for ServiceNow platform integration - ITOM, ITSM, CMDB with OAuth, natural language queries, and enterprise security controls

3789. **[swift-skeleton](https://github.com/1amageek/swift-skeleton)** - ⭐ 14
   Swift source code structural indexer. Extracts type declarations, properties, method signatures, and source locations. MCP server for Claude Code.

3790. **[arxiv-mcp-server](https://github.com/1Dark134/arxiv-mcp-server)** - ⭐ 14
   arXiv MCP Server Client 🐙 enables AI assistants to search, retrieve, analyze, and summarize arXiv papers with features like author/category browsing, trends, and citation insights.

3791. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 14
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3792. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 14
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

3793. **[WAIaaS](https://github.com/minhoyoo-iotrust/WAIaaS)** - ⭐ 14
   Wallet-as-a-Service for all AI agents in the world

3794. **[x402-deploy](https://github.com/nirholas/x402-deploy)** - ⭐ 14
   Turn any API or MCP server into a paid service with x402 

3795. **[ai-mate](https://github.com/symfony/ai-mate)** - ⭐ 14
   AI development assistant MCP server for Symfony projects

3796. **[mcp-security-checklist](https://github.com/Helixar-AI/mcp-security-checklist)** - ⭐ 14
   MCP is being adopted rapidly. Security guidance is lagging behind. This checklist gives security engineers, platform teams, and technical leaders a clear, actionable baseline for securing MCP deployments , whether you're shipping an internal tool or a customer-facing AI agent.

3797. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 14
   The ultimate AI-powered generator for llms.txt and llms-full.txt files. 

3798. **[mcp-graph-workflow](https://github.com/DiegoNogueiraDev/mcp-graph-workflow)** - ⭐ 14
   MCP local-first CLI tool that converts PRD text files into persistent execution graphs (SQLite) for structured agentic workflows

3799. **[MCPScan](https://github.com/sahiloj/MCPScan)** - ⭐ 14
   Offensive MCP server auditor — detects tool poisoning, credential leaks, RCE vectors, SSRF, session hijacking, and supply chain vulnerabilities across stdio, HTTP, and SSE transports.

3800. **[toolhive-registry-server](https://github.com/stacklok/toolhive-registry-server)** - ⭐ 14
   An API server that implements the official MCP Registry API, providing standardised access to MCP servers from multiple backends, including file-based and other API-compliant registries.

3801. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 14
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

3802. **[openapi-to-mcp](https://github.com/EvilFreelancer/openapi-to-mcp)** - ⭐ 14
   Turns any OpenAPI/Swagger API into an MCP server. One MCP tool per endpoint, Streamable HTTP - for AI clients calling your REST API.

3803. **[KunAvatar](https://github.com/KunLabAI/KunAvatar)** - ⭐ 14
   基于ollama推理框架本地部署的Agent应用，实现MCP工具调用，短长期记忆等功能。||  A locally deployed agent application built on the Ollama, featuring MCP tool integration along with both short-term and long-term memory support.

3804. **[webclaw](https://github.com/kuroko1t/webclaw)** - ⭐ 14
   A WebMCP-native browser agent that runs inside your real Chrome — control it from Claude, Cursor, and any MCP client

3805. **[conductor](https://github.com/aryabyte21/conductor)** - ⭐ 14
   Manage MCP server configs across AI coding clients

3806. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 14
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

3807. **[Rube](https://github.com/dorucioclea/Rube)** - ⭐ 13
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

3808. **[nest-mcp](https://github.com/btwld/nest-mcp)** - ⭐ 13
   Build Model Context Protocol (MCP) servers, clients, and gateways using the NestJS ecosystem you already know.

3809. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

3810. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

3811. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

3812. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

3813. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

3814. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

3815. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

3816. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

3817. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

3818. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

3819. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

3820. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

3821. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

3822. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 13
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3823. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

3824. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

3825. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

3826. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

3827. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

3828. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 13
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

3829. **[devtap](https://github.com/killme2008/devtap)** - ⭐ 13
   Bridge build/dev process output to AI coding sessions via MCP — supports Claude Code, Codex, OpenCode, Gemini CLI, and aider

3830. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 13
   talk to sarvam APIs directly, without code.

3831. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 13
   A server implementation for the Model Context Protocol (MCP) in Ruby.

3832. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 13
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

3833. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 13
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

3834. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 13
   Taiga UI MCP server providing documentation search and scaffolding tools.

3835. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 13
   MCP server for OWL applications

3836. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 13
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

3837. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 13
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

3838. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 13
   Simple Weather MCP Server Example

3839. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 13
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

3840. **[istek](https://github.com/istekapp/istek)** - ⭐ 13
   The API client built for AI agents. HTTP, GraphQL, gRPC, WebSocket, MQTT + MCP."

3841. **[mcp-server-template](https://github.com/BearHuddleston/mcp-server-template)** - ⭐ 13
   Spec-driven Go MCP server template for building domain MCPs with AI-agent onboarding.

3842. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

3843. **[obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** - ⭐ 13
   MCP server for Obsidian vault management - enables Claude and other AI assistants to read, write, search, and organize your notes

3844. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 13
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

3845. **[claude-tools-mcp](https://github.com/mathematic-inc/claude-tools-mcp)** - ⭐ 13
   MCP server that exposes Claude Code's file and shell tools (bash, read, write, edit, glob, grep) over HTTP for remote use by any MCP client

3846. **[sift-gateway](https://github.com/lourencomaciel/sift-gateway)** - ⭐ 13
   Reliability gateway for AI tool output: schema-stable, secret-safe, pagination-complete JSON for MCP and CLI agents.

3847. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 13
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

3848. **[lm](https://github.com/houtini-ai/lm)** - ⭐ 13
   Offload Tasks from Claude to your Local LLM With Houtini-LM - uses OpenAPI for LM Studio and Ollama Compatibility. Save tokens by offloading some grunt work for your API - our tool description helps claude decide what work to assign and why.

3849. **[plumcp](https://github.com/plumce/plumcp)** - ⭐ 13
   Clojure/ClojureScript library for making MCP server and client

3850. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 13
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

3851. **[cie](https://github.com/kraklabs/cie)** - ⭐ 13
   Code Intelligence Engine — indexes your codebase and gives AI assistants deep understanding via MCP (semantic search, call graphs, 20+ tools)

3852. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 13
   Anthropic MCP server for .faf — 33 tools, IANA-registered format. npm: claude-faf-mcp. MCP Registry #2759

3853. **[credit-optimizer-v5](https://github.com/rafsilva85/credit-optimizer-v5)** - ⭐ 13
   Credit Optimizer v5 for Manus AI - Save 30-75% on credits. Free MCP Server (PyPI) + $9 Manus Skill. Audited across 53 scenarios. Zero quality loss.

3854. **[SRE-agent](https://github.com/martinimarcello00/SRE-agent)** - ⭐ 13
   Autonomous agent for Kubernetes incident detection, diagnosis, and mitigation using LLMs and modular workflows. Integrates LangChain, LangGraph, and MCP servers to enable automated SRE tasks in cloud-native environments.

3855. **[java-xiaohongshu-mcp](https://github.com/bzlrj/java-xiaohongshu-mcp)** - ⭐ 13
   Java 实现的小红书 Model Context Protocol (MCP) 工具服务  为 AI Agent / MCP Client 提供标准化接口，实现： 登录、发图文、发视频、搜索、评论、推荐内容、用户主页 等核心功能

3856. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 13
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

3857. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

3858. **[GitLab-CICD-Agent](https://github.com/shalwin04/GitLab-CICD-Agent)** - ⭐ 13
   agentic-cicd is an AI-powered multi-agent system that automates GitLab CI/CD workflows using natural language. Built with LangGraphJS, it connects to GitLab via OAuth, interprets user intent, generates pipelines, and executes deployments — all orchestrated by autonomous AI agents and backed by a GitLab MCP server.

3859. **[ex_mcp](https://github.com/azmaveth/ex_mcp)** - ⭐ 13
   Model Context Protocol (MCP) and Agent Client Protocol (ACP) client/server library for Elixir

3860. **[webmcp-sh](https://github.com/WebMCP-org/webmcp-sh)** - ⭐ 13
   A modern web-based Model Context Protocol (MCP) playground for testing and developing MCP servers and clients

3861. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 13
   Documentation

3862. **[zebbern-kali-mcp](https://github.com/zebbern/zebbern-kali-mcp)** - ⭐ 13
   MCP server for Kali Linux penetration testing - 149 tools for AI-assisted security testing - Giving Agents access to full pentesting tools

3863. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

3864. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

3865. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

3866. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

3867. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

3868. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

3869. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

3870. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

3871. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

3872. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 12
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

3873. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 12
   An opinionated MCP module for NestJS

3874. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

3875. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 12
   MCP server for kintone

3876. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

3877. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3878. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 12
   🥾 _b00t_:  brians dotfiles aka state of the art agentic tooling & context initialization

3879. **[jenkins-mcp-server](https://github.com/AshwiniGhuge3012/jenkins-mcp-server)** - ⭐ 12
   An MCP server for interacting with a Jenkins server. Allows you to trigger jobs, check build statuses, and manage your Jenkins instance through MCP.

3880. **[openagentidentityprotocol](https://github.com/openagentidentityprotocol/openagentidentityprotocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3881. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 12
   Universal cli to add an MCP server to a variety of clients

3882. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 12
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

3883. **[MCPGateway](https://github.com/abdullah1854/MCPGateway)** - ⭐ 12
   Open-source MCP server — progressive tool discovery, code execution, intelligent routing & token optimization across 50+ tools

3884. **[mcp-interactive-terminal](https://github.com/amol21p/mcp-interactive-terminal)** - ⭐ 12
   MCP server that gives AI agents (Claude Code, Cursor, Windsurf) real interactive terminal sessions — REPLs, SSH, databases, Docker, and any interactive CLI with clean output and smart completion detection

3885. **[kiro-powers](https://github.com/praveenc/kiro-powers)** - ⭐ 12
   Repository of custom kiro powers. https://kiro.dev/docs/powers/

3886. **[guildbridge](https://github.com/dend/guildbridge)** - ⭐ 12
   🏰 Remotely hosted MCP server for Discord

3887. **[docdex](https://github.com/bekirdag/docdex)** - ⭐ 12
   A document index with MCP, http and client support. https://docdex.org/ 

3888. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 12
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

3889. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 12
   MCP server for accessing VS Code/Cursor's Local History

3890. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 12
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

3891. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 12
   Connecting AI agent to biomedical data

3892. **[nodebench-ai](https://github.com/HomenShum/nodebench-ai)** - ⭐ 12
   NodeBench MCP - 260-tool Model Context Protocol server with progressive discovery, agent-as-a-graph embeddings, research optimization, and adaptive web scraping. Monorepo: MCP server + Convex backend + React frontend.

3893. **[mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** - ⭐ 12
   WooCommerce MCP Server — WordPress community plugin implementing the Model Context Protocol (MCP) for WooCommerce. Supports STDIO and HTTP streamable transport, with optional JWT authentication. Based on Automattic’s official WordPress MCP.  This plugin is not affiliated with Automattic.

3894. **[asap-protocol](https://github.com/adriannoes/asap-protocol)** - ⭐ 12
   Standard protocol for agent-to-agent communication with stateful orchestration, MCP-compatible and a public marketplace to discover and register agents.

3895. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 12
   MCP for Scorable Evaluation Platform

3896. **[Hoofy](https://github.com/HendryAvila/Hoofy)** - ⭐ 12
   Hoofy — AI development companion MCP server. Persistent memory, spec-driven development, adaptive change pipeline, Clarity Gate. 32 tools, single Go binary, zero deps.

3897. **[wamcp](https://github.com/delltrak/wamcp)** - ⭐ 12
   WhatsApp MCP Server — Connect AI agents to WhatsApp via Model Context Protocol. 61 tools, 10 resources, 12 real-time events. Supports Baileys (WhatsApp Web) and Cloud API. Built with TypeScript, BullMQ, and Docker.

3898. **[magento-coding-standard-mcp](https://github.com/Midhun-edv/magento-coding-standard-mcp)** - ⭐ 12
   MCP server that teaches AI assistants Magento 2 coding standards — validate code, look up correct patterns, check security, and apply theme-specific rules (Hyva, Luma, Breeze, Porto). Works with Claude, Cursor, Gemini CLI, VS Code Copilot, and any MCP-compatible client.

3899. **[claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp)** - ⭐ 12
   Local-first TypeScript MCP server for Qdrant with client isolation, LM Studio integration, and scalable document workflows.

3900. **[actual-mcp-server](https://github.com/agigante80/actual-mcp-server)** - ⭐ 12
   Docker MCP server connecting MCP clients (tested with LibreChat/LobeChat) to Actual Budget for natural-language budgeting, transaction management, and financial insights.

3901. **[mendeley-mcp](https://github.com/pallaprolus/mendeley-mcp)** - ⭐ 12
   MCP server for Mendeley reference manager - search, retrieve, and manage your academic library from Claude and other MCP clients

3902. **[bookmark-manager-mcp](https://github.com/infinitepi-io/bookmark-manager-mcp)** - ⭐ 12
   A lightweight Model Context Protocol (MCP) server that provides persistent bookmark management for Claude and other MCP-compatible clients. Features categorized storage, resource discovery, and seamless integration with your AI workflow.

3903. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 12
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

3904. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

3905. **[seats.aero-mcp-server](https://github.com/gavgrego/seats.aero-mcp-server)** - ⭐ 12
   MCP server allowing clients to interface with the seats.aero API

3906. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 12
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

3907. **[agent-hub](https://github.com/nathangtg/agent-hub)** - ⭐ 12
   Agent Hub is an AI orchestration platform that transforms how developers and DevOps engineers interact with their toolchain. Built on the cutting-edge Model Context Protocol (MCP), it provides intelligent automation through specialized AI agents, seamlessly integrating with GitHub, Azure, security tools, and data processing

3908. **[mitmproxy-mcp](https://github.com/snapspecter/mitmproxy-mcp)** - ⭐ 12
   MCP Server that wraps mitmproxy and exposes it as a tool to any MCP client, allows your AI agents to inspect traffic, filter traffic, intercept & modify traffic, request reply, set global headers, and start/stop mitmproxy as needed.

3909. **[openclaw-mcp-server](https://github.com/Helms-AI/openclaw-mcp-server)** - ⭐ 11
   MCP server exposing OpenClaw Gateway tools to Claude Code and other MCP-compatible clients

3910. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 11
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

3911. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 11
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

3912. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

3913. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

3914. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

3915. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

3916. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

3917. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

3918. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

3919. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

3920. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

3921. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

3922. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

3923. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

3924. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

3925. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

3926. **[polaris](https://github.com/octu0/polaris)** - ⭐ 11
   Distributed AI Agent Framework

3927. **[glm5-mcp](https://github.com/Arkya-AI/glm5-mcp)** - ⭐ 11
   Reduce Claude Desktop consumption by 10x - Integrate Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

3928. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 11
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

3929. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 11
   Example Spring AI Model Context Protocol (MCP)

3930. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 11
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

3931. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 11
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

3932. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 11
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

3933. **[robotmcp_client](https://github.com/robotmcp/robotmcp_client)** - ⭐ 11
   Connect AI models like Claude & GPT with robots using MCP and ROS.

3934. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 11
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

3935. **[gtm-mcp](https://github.com/pouyanafisi/gtm-mcp)** - ⭐ 11
   MCP server for Google Tag Manager: read tags/triggers/variables, publish containers, and audit changes via Claude/Gemini.

3936. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 11
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

3937. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 11
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

3938. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 11
   DataAnalysis Agent using LangGraph & MCP server and client

3939. **[mcp-coroot](https://github.com/jamesbrink/mcp-coroot)** - ⭐ 11
   MCP server for Coroot observability platform - integrate monitoring, troubleshooting, and configuration tools with AI agents

3940. **[chromadb-remote-mcp](https://github.com/meloncafe/chromadb-remote-mcp)** - ⭐ 11
   Remote MCP server for ChromaDB

3941. **[msty-admin-mcp](https://github.com/M-Pineapple/msty-admin-mcp)** - ⭐ 11
   AI-powered administration for Msty Studio Desktop. 24 MCP tools for database insights, config sync, local model orchestration, and Claude handoff workflows.

3942. **[miro-mcp-server](https://github.com/olgasafonova/miro-mcp-server)** - ⭐ 11
   MCP server for controlling Miro whiteboards with AI assistants

3943. **[qurio](https://github.com/irahardianto/qurio)** - ⭐ 11
   Self-hosted RAG engine for AI coding assistants. Ingests technical docs & code repositories locally with structure-aware chunking. Serves grounded context via MCP to prevent hallucinations in software development workflows.

3944. **[fathom-mcp](https://github.com/Dot-Fun/fathom-mcp)** - ⭐ 11
   Model Context Protocol server for Fathom AI - access meeting recordings, transcripts, summaries, teams, and webhooks

3945. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 11
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

3946. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 11
   Simple template project for controlling Unity via MCP

3947. **[XcodeMCPKit](https://github.com/lynnswap/XcodeMCPKit)** - ⭐ 11
   Xcode MCP proxy with multi-client sessions

3948. **[keycloak-mcp](https://github.com/HaithamOumerzoug/keycloak-mcp)** - ⭐ 11
   MCP server that integrates with Keycloak, allowing you to manage Keycloak users and realms through a standardized protocol. It uses the official Keycloak Admin Client to interact with Keycloak's API.

3949. **[AMS](https://github.com/LastEld/AMS)** - ⭐ 11
   Audit Memory System (AMS): Durable orchestration and memory layer for MCP clients.

3950. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 11
   A TUI to probe the calls between MCP client and server

3951. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

3952. **[mcp-oidc-provider](https://github.com/tigrisdata/mcp-oidc-provider)** - ⭐ 11
   Open-sourced mcp-oidc-provider: a minimal, vendor-neutral OIDC layer that sits between MCP clients and your upstream IdP (Auth0/Clerk/Okta).

3953. **[openmessage](https://github.com/MaxGhenis/openmessage)** - ⭐ 11
   Open-source Google Messages client with AI tools (MCP). SMS + RCS from your desktop.

3954. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 10
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

3955. **[kroki-mcp](https://github.com/utain/kroki-mcp)** - ⭐ 10
   Kroki-MCP is a Go-based Model Context Protocol tool that converts textual diagram definitions (PlantUML, Mermaid, and more) into images via a Kroki backend. Designed for simplicity and flexibility, it supports both local and remote Kroki servers, offers configurable settings, and outputs multiple formats – making it ideal for developers building AI

3956. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 10
   MCP server to give client the ability to access Wikipedia pages

3957. **[taskboard](https://github.com/tcarac/taskboard)** - ⭐ 10
   Local project management with Kanban UI, CLI, and MCP server for AI assistants. SQLite-backed, single binary, installable via Homebrew.

3958. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

3959. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

3960. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

3961. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

3962. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

3963. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

3964. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

3965. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

3966. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3967. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

3968. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

3969. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

3970. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

3971. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

3972. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

3973. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

3974. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

3975. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

3976. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

3977. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault 

3978. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

3979. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

3980. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

3981. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

3982. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

3983. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

3984. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

3985. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

3986. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 10
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

3987. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

3988. **[Simple_MCP_Client](https://github.com/Avento/Simple_MCP_Client)** - ⭐ 10
   Simple MCP Client for OpenAI/Deepseek R1/V3

3989. **[awesome-mcp](https://github.com/gauravfs-14/awesome-mcp)** - ⭐ 10
   A carefully curated collection of high-quality tools, libraries, research papers, projects, and tutorials centered around Model Context Protocol (MCP) — a novel paradigm designed to enable modular, adaptive coordination between large language models (LLMs) and external tools or data contexts.

3990. **[openapi-mcp-swagger](https://github.com/salacoste/openapi-mcp-swagger)** - ⭐ 10
   Solve AI context window limits for API docs | Convert any Swagger/OpenAPI to searchable MCP server | AI-powered endpoint discovery & code generation | Works with Cursor, Claude, VS Code

3991. **[mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig)** - ⭐ 10
   A local MCP server that breaks on demand. Test your client against auth failures, disappearing tools, flaky responses, and token expiry, all from a web UI.

3992. **[notification-mcp](https://github.com/pinkpixel-dev/notification-mcp)** - ⭐ 10
   A Model Context Protocol server that allows AI agents to play a notification sound via a tool when a task is completed.

3993. **[adonis-mcp](https://github.com/7nohe/adonis-mcp)** - ⭐ 10
   An AdonisJS package for building remote MCP servers

3994. **[genkit-mcp-client-blender](https://github.com/xprilion/genkit-mcp-client-blender)** - ⭐ 10
   An MCP Client for interfacing with the Blender MCP Server built with Firebase Genkit and Gemini

3995. **[esp32-mcpserver](https://github.com/solnera/esp32-mcpserver)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server framework for ESP32. Seamlessly connect embedded devices to LLMs.

3996. **[youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server providing real-time YouTube Data API access for AI assistants. Features 14 functions including intelligent content evaluation with technology freshness scoring for knowledge base curation.

3997. **[Azure-Foundry-Webinar](https://github.com/ShivamGoyal03/Azure-Foundry-Webinar)** - ⭐ 10
   This repository is the official companion for the Azure AI Foundry Agent Service Webinar Series. It provides hands-on code samples, modular use cases, and practical guides for building, deploying, and scaling AI agents on Azure.

3998. **[Cognio](https://github.com/0xReLogic/Cognio)** - ⭐ 10
   Persistent semantic memory server for MCP - Give your AI long-term memory that survives across conversations. Lightweight Python server with SQLite storage and semantic search.

3999. **[systemprompt-template](https://github.com/systempromptio/systemprompt-template)** - ⭐ 10
   Production AI agent mesh in 3 commands. MCP servers, playbooks, and multi-agent orchestration built on systemprompt-core.

4000. **[cheatengine-mcp-bridge](https://github.com/beamstar/cheatengine-mcp-bridge)** - ⭐ 10
   🔗 Connect AI to Cheat Engine for fast memory analysis, enabling quick mods and audits without the tedious manual work.

4001. **[toolhive-cloud-ui](https://github.com/stacklok/toolhive-cloud-ui)** - ⭐ 10
   ToolHive Cloud UI surfaces MCP servers running in your infrastructure, highlighting metadata, tool capabilities, and copy-ready endpoints for fast AI agent integrations.

4002. **[mcpd](https://github.com/pouriya/mcpd)** - ⭐ 10
   A ~3MB MCP daemon that exposes any script as a tool for Claude, Cursor & AI assistants

4003. **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** - ⭐ 10
   Extended WhatsApp MCP server with 41 tools - reactions, group management, polls, presence, newsletters & more. Fork of lharries/whatsapp-mcp

4004. **[chessmata](https://github.com/jonradoff/chessmata)** - ⭐ 10
   Chessmata: chess game for humans and AI agents

4005. **[storybook-mcp-server](https://github.com/stefanoamorelli/storybook-mcp-server)** - ⭐ 10
   MCP server for Storybook - provides AI assistants access to components, stories, properties and screenshots. Built with TypeScript and Model Context Protocol SDK.

4006. **[dbt-core-mcp](https://github.com/NiclasOlofsson/dbt-core-mcp)** - ⭐ 10
   dbt Core MCP Server: Interact with dbt projects via Model Context Protocol

4007. **[chatgpt2md](https://github.com/NextStat/chatgpt2md)** - ⭐ 10
   Convert ChatGPT export to Markdown with full-text search and MCP server for Claude

4008. **[mini_claude](https://github.com/20alexl/mini_claude)** - ⭐ 10
   Give Claude Code persistent memory across sessions. Track habits, log mistakes, prevent death spirals. Runs locally with Ollama.

4009. **[statelessagent](https://github.com/sgx-labs/statelessagent)** - ⭐ 10
   Your AI forgets everything between sessions. SAME fixes that. Local-first, no API keys, single binary.

4010. **[MCP-Penetration-testing](https://github.com/Mr-Infect/MCP-Penetration-testing)** - ⭐ 10
   The ultimate OWASP MCP Top 10 security checklist and pentesting framework for Model Context Protocol (MCP), AI agents, and LLM-powered systems.

4011. **[caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for Caltrain schedules. Get real-time train departures using GTFS data, designed for Claude Desktop and other MCP clients.

4012. **[shellguard](https://github.com/fawdyinc/shellguard)** - ⭐ 10
   MCP server that gives LLM agents read-only shell access over SSH

4013. **[PsMCP-MCP-Server-for-Photoshop](https://github.com/Chandrahas455/PsMCP-MCP-Server-for-Photoshop)** - ⭐ 10
   An Extensive MCP server and a Gradio MCP client ( with Gemini ) with several tools made using win32com to intereact with Photoshop. Designing with Photoshop has never been more fun!

4014. **[ollama-mcp-example](https://github.com/kirillsaidov/ollama-mcp-example)** - ⭐ 10
   Ollama MCP example for dummies. 

4015. **[civitai-mcp-server](https://github.com/Cicatriiz/civitai-mcp-server)** - ⭐ 10
   A Model Context Protocol server for browsing and discovering AI models on Civitai

4016. **[openapi-to-mcp](https://github.com/agentic-community/openapi-to-mcp)** - ⭐ 10
   Transform OpenAPI specifications into production-ready MCP servers   with AI-powered evaluation and enhancement. Leverages LLMs to   analyze, improve, and generate Model Context Protocol   implementations from your existing API documentation.

4017. **[world-intel-mcp](https://github.com/marc-shade/world-intel-mcp)** - ⭐ 10
   100+ tool MCP server for real-time global intelligence — markets, FX, bonds, earnings, SEC filings, conflict, military, cyber, climate, news, company enrichment, and 30+ domains. Live Leaflet dashboard with 20 map layers, SSE streaming, and AI situation briefs.

4018. **[ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp)** - ⭐ 10
   🔓 UNLEASH ILSpy'S POWER. Reverse-engineer DOTNET code at GOD SPEED. AI-assisted debugging that THINKS with you. Decompile ANYTHING. 🚀

4019. **[aichat](https://github.com/Hayashi-Yudai/aichat)** - ⭐ 10
   A customizable AI chat application powered by Flet.

4020. **[mcp-document-converter](https://github.com/xt765/mcp-document-converter)** - ⭐ 10
   MCP Document Converter - A powerful MCP tool for converting documents between multiple formats, enabling AI agents to easily transform documents.

4021. **[pentest-mcp-server](https://github.com/exjskdjsdfks/pentest-mcp-server)** - ⭐ 10
   ⚙️ Enable AI agents to conduct autonomous penetration testing on any Linux distribution with a persistent and robust Model Context Protocol server.

4022. **[mcpHTTPClient](https://github.com/matlab-deep-learning/mcpHTTPClient)** - ⭐ 10
   An MCP client in pure MATLAB code

4023. **[DevoChat](https://github.com/gws8820/DevoChat)** - ⭐ 10
   Unified Web AI Chat UI & MCP Client

4024. **[simple-mcp-server](https://github.com/dataworkshop/simple-mcp-server)** - ⭐ 10
   Simple MCP Server — Educational Example This repository contains a minimal MCP (Model Context Protocol) server built for educational purposes. Its goal is to help developers understand how the MCP protocol works and how to manage decision-making processes based on model–client communication.

4025. **[openclaw-mcp-bridge](https://github.com/AIWerk/openclaw-mcp-bridge)** - ⭐ 10
   OpenClaw MCP Client Plugin - bridges MCP servers into OpenClaw via registerTool

4026. **[cubbi](https://github.com/Monadical-SAS/cubbi)** - ⭐ 10
   Monadical container CLI tool for running sandboxed MCP clients & servers

4027. **[team-memory-mcp](https://github.com/gustavolira/team-memory-mcp)** - ⭐ 10
   Shared team memory for AI coding agents. Bayesian confidence scoring with temporal decay. Works with Claude Code, Devin, Cursor, and any MCP-compatible client.

4028. **[ai-assistant-vui](https://github.com/mgoltzsche/ai-assistant-vui)** - ⭐ 10
   Experimental voice user interface (VUI) to interact with an agentic AI assistant

4029. **[mcp-client](https://github.com/CopilotKit/mcp-client)** - ⭐ 10

4030. **[tupac](https://github.com/tkellogg/tupac)** - ⭐ 10
   A terminal MCP client based on the OpenAI responses API.

4031. **[vault-sync](https://github.com/alexjbarnes/vault-sync)** - ⭐ 10
   Headless Obsidian Sync client with MCP server for AI assistants

4032. **[bio-agents-mcp](https://github.com/dogeplusplus/bio-agents-mcp)** - ⭐ 10
   MCP servers for Protein Data Bank, ChemBL, and other life science data (WIP), with Ollama client for local testing.

4033. **[lol-client-mcp](https://github.com/johnnyinlee/lol-client-mcp)** - ⭐ 10
   League of Legends Game Client API MCP Server

4034. **[ai-mcp-bridge](https://github.com/xiaozhug/ai-mcp-bridge)** - ⭐ 10
   rest to mcp & mcp Registry & mcp Loadbalancer & ai mcp & Multiple Registries & 多注册中心 

4035. **[cli](https://github.com/inboxapi/cli)** - ⭐ 10
   🤖 Your Agents' personal email 📧  

4036. **[Ai-doctor](https://github.com/Jevon-Zhong/Ai-doctor)** - ⭐ 10
   🧑‍⚕️ Ai智能医生聊天助手-这是一个前端基于Vue3、TS、后端基于Nest.js、MongoDB、Redis、Milvus并结合大模型、RAG等技术实现的医疗库智能问答系统，能结合大模型的生成能力和上传的专业医疗领域知识库针对提问给出专业回答。同时具备工具调用能力，可使用MCP集成网页爬取能力让大模型根据网址对应的医疗领域文章进行分析和输出。

4037. **[ux-mcp-server](https://github.com/elsahafy/ux-mcp-server)** - ⭐ 10
   MCP server providing 28 UX knowledge resources, 23 analysis tools & 4 workflow prompts. Works with Claude, Cursor, Continue.dev, Cline, Zed & any MCP client. WCAG, Nielsen heuristics, design systems, e-commerce, PWA, AI/ML & more.

4038. **[league-client-mcp](https://github.com/rumi-chan/league-client-mcp)** - ⭐ 10
   Connect Claude, Antigravity to League Client via MCP & Pengu Loader.

4039. **[Cortex](https://github.com/cdeust/Cortex)** - ⭐ 10
   C.O.R.T.E.X. — Cognitive profiling system for Claude Code

3890. **[operant-mcp](https://github.com/operantlabs/operant-mcp)** - ⭐ 0
   Security testing MCP server with 51 tools for penetration testing, network forensics, memory analysis, and vulnerability assessment.

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 44,895
   LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

2. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 42,760
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

3. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 10,210
   ValueCell is a community-driven, multi-agent platform for financial applications.

4. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,640
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

5. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,725
   Magicrew. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

6. **[koog](https://github.com/JetBrains/koog)** - ⭐ 4,038
   Koog is a JVM (Java and Kotlin) framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

7. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,345
   extendable code review and QA agent 🚢

8. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,673
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

9. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,641

10. **[ragent](https://github.com/nageoffer/ragent)** - ⭐ 1,268
   企业级 Agentic RAG 智能体 - 全链路覆盖文档解析、多路检索、意图识别、问题重写、会话记忆、MCP 工具调用与深度思考。面向真实业务场景，从 0 到 1 完整工程实现。

11. **[Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills)** - ⭐ 1,054
   Wherever your AI supports skills, VibeSkills works. 340+ governed skills spanning coding, research, automation & creative work.

12. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 908
   OpenTelemetry Instrumentation for AI Observability

13. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 842
   A code repository indexing tool to supercharge your LLM experience.

14. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 710
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

15. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 582
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

16. **[casbin-gateway](https://github.com/apache/casbin-gateway)** - ⭐ 556
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

17. **[comunica](https://github.com/comunica/comunica)** - ⭐ 548
   📬 A knowledge graph querying framework for JavaScript

18. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 535
   The easiest way to discover and install MCPs

19. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 485
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

20. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 389
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

21. **[pwno-mcp](https://github.com/pwno-io/pwno-mcp)** - ⭐ 241
   MCP for Pwn

22. **[openclaw.net](https://github.com/clawdotnet/openclaw.net)** - ⭐ 192
   Self-hosted OpenClaw gateway + agent runtime in .NET (NativeAOT-friendly)

23. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 189
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

24. **[ai](https://github.com/WordPress/ai)** - ⭐ 168
   AI features and experiments for WordPress. Modular framework for testing AI capabilities.

25. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 157
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

26. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

27. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 109
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

28. **[uxc](https://github.com/holon-run/uxc)** - ⭐ 99
   A unified CLI for discovering and invoking tools across OpenAPI, MCP, GraphQL, gRPC, and JSON-RPC

29. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

30. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 96
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

31. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 95
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

32. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 85
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

33. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

34. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 55

35. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

36. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 46
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

37. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

38. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

39. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

40. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 27
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

41. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

42. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

43. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

44. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

45. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 21
   Powered by Ray (video) and Photon (image) models by Luma AI

46. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 19
   A desktop client with MCP support for Mistral LLMs

47. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

48. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 11

49. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

50. **[ArcaMCP](https://github.com/Yoryoboy/ArcaMCP)** - ⭐ 10
   Servidor MCP para AFIP/ARCA: automatiza certificados, autorización de Web Services, emisión/consulta de comprobantes y generación de PDF con QR.

51. **[ai](https://github.com/JoakimCarlsson/ai)** - ⭐ 10
   A Go toolkit for building AI agents and applications across multiple providers. Unified LLM client, agent framework with handoffs, tool calling, streaming, structured output, MCP integration, and cost tracking.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 182,474
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 43,108
   🦍 The API and AI Gateway

3. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,907
   Query Engine for AI Analytics: Build self-reasoning agents across all your live data

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 27,614
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,585
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,442
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 16,109
   Rich-text editor with AI and shadcn/ui

8. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

9. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

10. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,799
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

11. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 11,461
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 11,191
   A cross-platform Markdown AI note-taking software.

13. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 10,880
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

14. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 9,662
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

15. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 8,764
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,819
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,705
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[adk-go](https://github.com/google/adk-go)** - ⭐ 7,425
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

19. **[codefather](https://github.com/liyupi/codefather)** - ⭐ 6,945
   程序员鱼皮的编程宝典 ⭐️ 2026年最全编程学习路线图！包含Java学习路线、前端学习路线、Python学习路线、C++学习路线、算法学习路线、计算机基础学习路线、AI应用开发学习路线、AI Agent开发学习路线等。提供编程入门教程、AI大模型应用开发教程、RAG开发实战、MCP开发教程、Prompt工程指南、LLM应用开发、技术知识分享、学习资源推荐、项目实战教程、热门面试题、求职经验、简历优化、编程自学指南等内容，适用于所有零基础学编程、学习AI开发、转行程序员、计算机专业学生、求职找工作的同学 💎 编程学习，就来编程导航！

20. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 5,047
   面向企业级市场的一站式AI应用开发框架，支持多厂商大模型统一接入与管理，具备安全可控的企业知识库与高精度检索优化能力，提供可视化流程编排、自主决策智能体与多智能体协同调度，兼容主流 Agent Skill 协议，帮助企业与开发者零门槛快速构建安全、高效、可落地的AI智能体应用与行业解决方案。

21. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 5,036
   💻 vibe coding 2026 | Your first modern programming course for beginners to master step by step.

22. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 5,018
   Adversary simulation and Red teaming platform with AI

23. **[Yuxi](https://github.com/xerrors/Yuxi)** - ⭐ 4,806
   结合知识库管理的 Agent Harness 平台。 An agent harness that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

24. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,667
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

25. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,412
   Nexent is a zero-code platform for auto-generating production-grade AI agents using Harness Engineering principles — unified tools, skills, memory, and orchestration with built-in constraints, feedback loops, and control planes.

26. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,359
   AG2 (formerly AutoGen): The Open-Source AgentOS.Join us at: https://discord.gg/sNGSwQME3x

27. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,305
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

28. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,082
   Bulk port forwarding Kubernetes services for local development.

29. **[Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** - ⭐ 4,044
   753+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

30. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 3,610
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

31. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,309
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

32. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,778
   A highly opinionated, zero-configuration linter and formatter.

33. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,713
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

34. **[harbor](https://github.com/av/harbor)** - ⭐ 2,698
   One command brings a complete pre-wired LLM stack with hundreds of services to explore.

35. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 2,180
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

36. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 2,038
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流

37. **[claude-code-book](https://github.com/lintsinghua/claude-code-book)** - ⭐ 2,004
   《御舆：解码 Agent Harness》42万字拆解 AI Agent 的Harness骨架与神经 —— Claude Code 架构深度剖析，15 章从对话循环到构建你自己的 Agent Harness。在线阅读网站：

38. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,922
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

39. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,729
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

40. **[Klee](https://github.com/signerlabs/Klee)** - ⭐ 1,719
   A native macOS AI chat app powered by MLX. 100% local inference on Apple Silicon, no cloud required. Built with ShipSwift.

41. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,625
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

42. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,520
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

43. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,490
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

44. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,434
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

45. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

46. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,332
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

47. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

48. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,311
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

49. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

50. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,228
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

51. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,203
   Korea Investment & Securities Open API Github

52. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 1,194
   Local first codebase intelligence

53. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,171
   Search, understand, reproduce, and improve an idea with ease

54. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,137
   A single interface to use and evaluate different agent frameworks 

55. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,071
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

56. **[claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust)** - ⭐ 1,067
   🚀 Rust 全量重构的 Claude Code - 性能提升 2.5x，体积减少 97% | High-performance Rust implementation of Claude Code with 2.5x faster startup and 97% smaller binary

57. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 1,024
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

58. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 1,011
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

59. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 981
   Arduino MCP2515 CAN interface library

60. **[rulesync](https://github.com/dyoshikawa/rulesync)** - ⭐ 971
   A Utility CLI for AI Coding Agents

61. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 955
   Natural (2-way) voice conversations with Claude Code

62. **[DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner)** - ⭐ 948
   🎨 NeMo Data Designer: Generate high-quality synthetic data from scratch or from seed data.

63. **[cursor2api-go](https://github.com/libaxuan/cursor2api-go)** - ⭐ 934
   Free claude-sonnet-4.6  | cursor不倒我不倒🙏 ❌ 不支持 tools / function calling / MCP

64. **[weave](https://github.com/Ataraxy-Labs/weave)** - ⭐ 824
   Entity-level semantic merge driver for Git. Resolves conflicts that git can't by understanding code structure via tree-sitter. 31/31 clean merges vs git's 15/31.

65. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 804
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

66. **[eDBG](https://github.com/ShinoLeah/eDBG)** - ⭐ 790
   eBPF-based lightweight debugger for Android with MCP support

67. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 776
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

68. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 761
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

69. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 754
   Solidity Static Analyzer that easily integrates into your editor

70. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 749
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

71. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 741
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

72. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 737
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

73. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 735
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

74. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 711
   JiwuChat 🍂 - A lightweight cross-platform instant messaging app with integrated AI assistants (DeepSeek/Gemini/Kimi). Features real-time messaging, audio/video calls, multi-device sync, and customizable themes. Built with Vue3 & Tauri2 🍒

75. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 677
   A personal AI assistant for everyone

76. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 651
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

77. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 610
   UI components for AI interfaces

78. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 601
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

79. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 586
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

80. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 550
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

81. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 531
   Marmot is an open-source data catalog designed for teams who want powerful data discovery without enterprise complexity. Catalog every data asset, enrich it with the context that matters and make it accessible to your team and your AI tools.

82. **[vocotype-cli](https://github.com/233stone/vocotype-cli)** - ⭐ 512
   VocoType 是一款运行在本地端侧的隐私安全语音输入工具，通过快捷键即可将语音实时转换为文字并自动输入到当前应用。支持语音转文字MCP、AI 优化文本、自定义替换词典、录音视频转文字等功能，让语音输入更高效、更安全。

83. **[claude-code-cli](https://github.com/huangserva/claude-code-cli)** - ⭐ 505
   这是 Claude Code 的 CLI 客户端主体（src/ 目录），即整个终端交互层的源码。具体包含： 1. CLI 入口与命令解析 — main.tsx（4684行）、entrypoints/（CLI 模式、SDK 模式、MCP 模式） 2. 终端 UI 渲染 — components/（144 个组件，用 React + Ink 渲染终端界面） 3. 工具系统 — tools/（43 个工具，Bash、文件读写编辑、Grep、Glob、Web 搜索等） 4. API 通信层 — services/api/（与 Anthropic 后端通信） 5. MCP 协议  6. 多 Agent/Team 协作 l 7. 认证与策略 8. 辅助服务 等

84. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 476
   🚀 告别多个App！本项目基于Python+React+TypeScript+Hono+SQLite3+Redis，打造“All in One”智能工具集。免会员破解爱奇艺、腾讯视频、优酷、抖音、B站、小红书等20+平台视频，支持4K在线解析与无水印高速下载。集成Google、GitHub授权登录及OpenAI SDK、MCP服务和Agent，支持ChatGPT对话、AI绘画、论文降重、Hugging Face论文爬取；更有实时黄金K线、AI思维导图、闲鱼助手等效率黑科技。内置海量动漫漫画资源，畅享阅读！轻量高效，配置即用，完美适配PC与移动端，快来ChattyPlay开启奇妙之旅吧～✨

85. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 471
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

86. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

87. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

88. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 429
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

89. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 418
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

90. **[bridle](https://github.com/neiii/bridle)** - ⭐ 409
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

91. **[how-to-vibecoding](https://github.com/1EchA/how-to-vibecoding)** - ⭐ 407
   Vibecoding 系列教程：从环境搭建到多智能体协作，涵盖 MCP、Skills、Agent 分工治理

92. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 398
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

93. **[volcano-agent-sdk](https://github.com/Kong/volcano-agent-sdk)** - ⭐ 390
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

94. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 390
   Minecraft: Pi Edition API Python Library

95. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

96. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 384
   MCP for Unreal Engine 5

97. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 382
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

98. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 380
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

99. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 379
   Python toolkit for building graph-enhanced GenAI applications

100. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 378
   Arduino Library for Adafruit MCP23017

101. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 353
   Blender python addon to increase workflow for creating minecraft renders and animations

102. **[exograph](https://github.com/exograph/exograph)** - ⭐ 345
   Build production-ready backends in minutes

103. **[depyler](https://github.com/paiml/depyler)** - ⭐ 344
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

104. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 336
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

105. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

106. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 319
   Software architecture tooling for the AI age

107. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 315
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

108. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

109. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 303
   An in-depth book and reference on building agentic systems like Claude Code

110. **[machi](https://github.com/qntx/machi)** - ⭐ 289
   A Web4.0-native AI Agent Framework.

111. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 286
   小红书创作中心

112. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 282
   AI for Ethical Hacking - Workshop

113. **[genie](https://github.com/automagik-dev/genie)** - ⭐ 274
   Wishes in, PRs out. CLI agent that interviews you, plans the work, dispatches parallel agents in isolated worktrees, and reviews code before you see it.

114. **[scribe.js](https://github.com/scribeocr/scribe.js)** - ⭐ 266
   JavaScript OCR and text extraction for images and PDFs.

115. **[talkio](https://github.com/llt22/talkio)** - ⭐ 263
   Local-first multi-AI group chat desktop app — pull gpt, Claude, Gemini, DeepSeek into one conversation. Tauri 2 + React 19.

116. **[spool](https://github.com/spool-lab/spool)** - ⭐ 261
   Search your Claude Code sessions, Codex history, GitHub stars, and 50+ sources — locally, instantly. Your AI agents can search too.

117. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

118. **[PSAI](https://github.com/dfinke/PSAI)** - ⭐ 255
   High-agency PowerShell AI framework for multi-agent orchestration and autonomous systems engineering

119. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 255
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

120. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 251
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

121. **[agentica](https://github.com/shibing624/agentica)** - ⭐ 246
   Agentica: Lightweight async-first Python framework for AI agents. 轻量级异步优先的AI Agent框架，支持工具调用、RAG、多智能体和MCP。

122. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 244
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

123. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 241
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

124. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 240
   Public facing repo for MCP SRG mappings.

125. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 236
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

126. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 234
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

127. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 233
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

128. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

129. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 229
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

130. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 228
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

131. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

132. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

133. **[LAP](https://github.com/Lap-Platform/LAP)** - ⭐ 216
   Your agents are guessing at APIs. Give them the actual Agent-Native spec. 1500+ API's Ready To-Use skills,  Compile any API spec into a lean, agent-native format. 10× smaller. OpenAPI, GraphQL, AsyncAPI, Protobuf, Postman.

134. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

135. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

136. **[weam](https://github.com/weam-ai/weam)** - ⭐ 214
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

137. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

138. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 202
   Re-usable multi part components built on React Aria and TailwindCSS. 

139. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

140. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

141. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 177
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

142. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

143. **[selene](https://github.com/tercumantanumut/selene)** - ⭐ 162
   Selene is a desktop app that runs AI agents on your machine. Connect them to your WhatsApp, Telegram, Slack, or Discord. Write code, generate images, build personal assistants. All from one place. Your data stays on your device.

144. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 159
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

145. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 146
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

146. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 143
   Seline is a local-first AI desktop application that brings together conversational AI, visual generation tools, vector search, and multi-channel connectivity in one place.

147. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 142
   ☕ Community-driven Java implementation of TOON

148. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

149. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

150. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 130
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

151. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 128
   A curated list of open source repositories for AI Engineers

152. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 127
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

153. **[Manifold](https://github.com/Garume/Manifold)** - ⭐ 119
   Operation-first .NET foundation for generating fast CLI and MCP surfaces from a single definition.

154. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 119
   5-Day Gen AI Intensive Course with Google

155. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 116
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

156. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 115
   Solid Tumor Associative Modeling in Pathology

157. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 114
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

158. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 111
   Scalable and extensible reinforcement learning for LM agents.

159. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 110
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

160. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 110
   One-click launch URL generator for protocol-based apps

161. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 109
   谷歌5天AI Agents强化课程

162. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 108
   Unity plugin for Coplay

163. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 106
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

164. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 92
   ai memory for coding

165. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP 

166. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

167. **[open-skills](https://github.com/besoeasy/open-skills)** - ⭐ 78
   Battle-tested skill library for AI agents. Save 98% of API costs with ready-to-use code for crypto, PDFs, search, web scraping & more. No trial-and-error, no expensive APIs.

168. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 77
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

169. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 77
   A lightweight, open, and extensible multi-LLM interaction studio.

170. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 75
   Quarkus Langchain4J Workshop

171. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 74
   OneMCP feature requests, bugs and improvements 

172. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 74
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

173. **[yes-ue-mcp](https://github.com/softdaddy-o/yes-ue-mcp)** - ⭐ 73
   Native C++ Model Context Protocol (MCP) plugin for Unreal Engine 5.4+

174. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 67
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

175. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 64
   MeMesh Plugin — Searchable project memory plugin for Claude Code.

176. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 64
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

177. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 61
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

178. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 61
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

179. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 56
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

180. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 52
   Houdini integration through the Model Context Protocol

181. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 51
   chm to markdown and vectorDB

182. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 47
   Backported Model Context Protocol SDK for Java 8

183. **[velocity](https://github.com/OptimiLabs/velocity)** - ⭐ 41
   Local-first workspace for Claude Code, Codex CLI, and Gemini CLI with sessions, analytics, workflows, and tools

184. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

185. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 39
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

186. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 37
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

187. **[Agience](https://github.com/Agience/Agience)** - ⭐ 36
   MCP-native workspace for turning live work into durable knowledge.

188. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 35
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

189. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 35
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

190. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

191. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 31
   Prompt-driven automation platform - Transform natural language into executable workflows

192. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 30
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

193. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 29
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

194. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

195. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 28
   Build AI Agent using Google ADK , MCP and Gemma 3 model

196. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

197. **[codai](https://github.com/codai-agent/codai)** - ⭐ 23
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

198. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 21
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

199. **[codectx](https://github.com/hey-granth/codectx)** - ⭐ 17
   Codebase context compiler for AI agents. Graph-ranked, token-budgeted, tier-compressed output. Smarter than the existing ones.

200. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

201. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 17
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

202. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

203. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

204. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 14
   Multi-agent system for software development

205. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 14
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

206. **[pic-standard](https://github.com/madeinplutofabio/pic-standard)** - ⭐ 14
   The industry standard for Provenance & Intent Contracts (PIC) in Agentic AI. Bridging the Causal Gap in autonomous systems.

207. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

208. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

209. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 12
   Unity MCP Tool template project

210. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

211. **[claude-colony](https://github.com/MakingJamie/claude-colony)** - ⭐ 10
   Multi-agent Claude Code you can actually control. Spawn specialist teams in tmux, watch them work side-by-side, steer when needed. Built on native Claude Code agents. No black boxes.

212. **[Tapnow-Studio--](https://github.com/Menaelz/Tapnow-Studio--)** - ⭐ 10
   🎨 Create visual AI workflows with Tapnow Studio, a browser-based tool that combines powerful AI capabilities in a single, interactive node editor.

213. **[Ai_agents](https://github.com/jenasuraj/Ai_agents)** - ⭐ 10
   This is a repository of collection of many agents build on top of Langchain , Langgraph, MCP and so many amazing tools

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,675
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

3. **[claude-mcp-examples](https://github.com/charIesding/claude-mcp-examples)** - ⭐ 151
   examples of claude with mcp integration

4. **[End-to-End-Agentic-Ai-Automation-Lab](https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab)** - ⭐ 50
   This repository contains hands-on projects, code examples, and deployment workflows. Explore multi-agent systems, LangChain, LangGraph, AutoGen, CrewAI, RAG, MCP, automation with n8n, and scalable agent deployment using Docker, AWS, and BentoML.

5. **[claude-mcp](https://github.com/thinkbigcd/claude-mcp)** - ⭐ 16
   claude and mcp integration examples and tutorials

6. **[agent-examples](https://github.com/kagenti/agent-examples)** - ⭐ 11
   Sample Agents and Tools for Kagenti platform

### Documentation

*Documentation, tutorials, and learning resources*

1. **[JavaGuide](https://github.com/Snailclimb/JavaGuide)** - ⭐ 154,663
   Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

2. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 11,209
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程、AI 工具用法（Cursor / Claude Code / TRAE / Lovable / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档，已升级为鱼皮 AI 导航网站

3. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 7,719
   Specification and documentation for the Model Context Protocol

4. **[openyak](https://github.com/openyak/openyak)** - ⭐ 673
   An open-source desktop AI agent that handles your documents, files, and daily workflows — locally, with any model.

5. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 503
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

6. **[platform-engineering](https://github.com/codetocloudorg/platform-engineering)** - ⭐ 94
   A centralized hub for platform engineering teams, providing resources, best practices, and automation tools. Includes IaC templates, blueprints, and operational guides to help build scalable, secure, and efficient platforms for cloud-native environments and DevSecOps workflows.

7. **[forksilly.doc](https://github.com/fatsnk/forksilly.doc)** - ⭐ 85
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

