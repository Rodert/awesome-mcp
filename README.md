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

## 📚 Projects (3990 total)

> Last updated: **2026-03-10**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 131,842
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 126,477
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 97,065
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 82,625
   A collection of MCP servers.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 80,654
   Model Context Protocol Servers

6. **[netdata](https://github.com/netdata/netdata)** - ⭐ 78,006
   The fastest path to AI-powered full stack observability, even for lean teams.

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 74,606
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 73,359
   The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

9. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

10. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 69,398
   The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

11. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 55,989
   The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

12. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 48,348
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

13. **[context7](https://github.com/upstash/context7)** - ⭐ 48,333
   Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

14. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 45,368
   【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

15. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 43,438
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

16. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 42,403
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

17. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

18. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 34,481
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

19. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

20. **[goose](https://github.com/block/goose)** - ⭐ 32,740
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

21. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,706
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

22. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 32,143
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

23. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 31,600
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

24. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 28,673
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

25. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 28,533
   Playwright MCP server

26. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 28,275
   Chrome DevTools for coding agents

27. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 27,698
   GitHub's official MCP Server

28. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 27,448
   🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

29. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 27,335
   Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

30. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 25,976
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

31. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 25,629
   An autonomous agent that conducts deep research on any data using any LLM providers

32. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 24,595
   An MCP-based chatbot | 一个基于MCP的聊天机器人

33. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,392
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

34. **[fastmcp](https://github.com/PrefectHQ/fastmcp)** - ⭐ 23,542
   🚀 The fast, Pythonic way to build MCP servers and clients.

35. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,902
   🚀 The fast, Pythonic way to build MCP servers and clients

36. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 22,526
   The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

37. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 22,332
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

38. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 22,060
   The official Python SDK for Model Context Protocol servers and clients

39. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 21,840
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

40. **[serena](https://github.com/oraios/serena)** - ⭐ 21,232
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

41. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 21,149
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

42. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 20,299
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

43. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 20,275
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

44. **[ruflo](https://github.com/ruvnet/ruflo)** - ⭐ 20,272
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

45. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 17,885
   Build and run agents you can see, understand and trust.

46. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 17,620

47. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 15,277
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

48. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 15,239
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

49. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 15,103
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

50. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 14,752
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

51. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,980
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

52. **[electerm](https://github.com/electerm/electerm)** - ⭐ 13,700
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(linux, mac, win)

53. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 13,512
   MCP server to provide Figma layout information to AI coding agents like Cursor

54. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

55. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 13,353
   MCP Toolbox for Databases is an open source MCP server for databases.

56. **[openfang](https://github.com/RightNow-AI/openfang)** - ⭐ 13,331
   Open-source Agent Operating System

57. **[casdoor](https://github.com/casdoor/casdoor)** - ⭐ 13,126
   An open-source AI-first Identity and Access Management (IAM) /AI MCP gateway and auth server with web UI supporting MCP, A2A, OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD

58. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 12,777
   Memory for 24/7 proactive agents like openclaw (moltbot, clawdbot).

59. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,798
   The official TypeScript SDK for Model Context Protocol servers and clients

60. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,638
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

61. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,222
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

62. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 11,041
   MCP for xiaohongshu.com

63. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,838
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

64. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,803
   Yet another WebUI for Nginx

65. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 10,696
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

66. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 10,547
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

67. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 10,312
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

68. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

69. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 9,604
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

70. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 9,410
   The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

71. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 9,198
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

72. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,979
   Visual testing tool for MCP servers

73. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,823
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

74. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 8,397
   Official MCP Servers for AWS

75. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,310
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

76. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,089
   Build effective agents using Model Context Protocol and simple workflow patterns

77. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 7,847
   MCP Server for Ghidra

78. **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** - ⭐ 7,793
   Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

79. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,729
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

80. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,671
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

81. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 7,338
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

82. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

83. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,111
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

84. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 6,834
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

85. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 6,660
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

86. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 6,641
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 76+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, R, C, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

87. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 6,579
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

88. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,535
   A community driven registry service for Model Context Protocol (MCP) servers.

89. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,453
   TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

90. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 6,432
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

91. **[superset](https://github.com/superset-sh/superset)** - ⭐ 6,389
   IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

92. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,336
   A collection of MCP clients.

93. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 6,180
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

94. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

95. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 6,003
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

96. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,717
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

97. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,655
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

98. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,646
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

99. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,642
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

100. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,587
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

101. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,439
   A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

102. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,399
   WhatsApp MCP server

103. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,294
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

104. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,287
   A model-driven approach to building AI agents in just a few lines of code.

105. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,222
   Awesome MCP Servers - A curated list of Model Context Protocol servers

106. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,062
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

107. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,008
   Install, run and deploy your own decentralized AI agent service

108. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,950
   opensource self-hosted sandboxes for ai agents

109. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 4,937
   Learn AI and LLMs from scratch using free resources

110. **[unidbg](https://github.com/zhkl0228/unidbg)** - ⭐ 4,817
   Allows you to emulate an Android native library, and an experimental  iOS emulation

111. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,730
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

112. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,692
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

113. **[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)** - ⭐ 4,660
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

114. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 4,618
   MCP Server for Computer Use in Windows

115. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 4,541
   MCP server for Atlassian tools (Confluence, Jira)

116. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,504
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

117. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,504
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

118. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,457
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

119. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,389
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

120. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,263
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

121. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,184
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

122. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

123. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 4,070
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

124. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 4,041
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

125. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 4,035
   A simple, secure MCP-to-OpenAPI proxy server

126. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 4,007
   Official Notion MCP Server

127. **[osaurus](https://github.com/osaurus-ai/osaurus)** - ⭐ 3,997
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

128. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,972
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

129. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,959
   Exa MCP for web search and web crawling!

130. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,953
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

131. **[directories](https://github.com/leerob/directories)** - ⭐ 3,913
   Find rules and MCP servers

132. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

133. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,852
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

134. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,812
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

135. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,787
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

136. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 3,772
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

137. **[atmosphere](https://github.com/Atmosphere/atmosphere)** - ⭐ 3,744
   The transport-agnostic real-time framework for the JVM. WebSocket, SSE, Long-Polling, gRPC, MCP — one API, any transport.

138. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,718
   A curated list of Model Context Protocol (MCP) servers

139. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,710
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

140. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,703
   Define, Prompt and Test MCP enabled Agents and Workflows

141. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,640
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

142. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,640
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use. 

143. **[core](https://github.com/opensumi/core)** - ⭐ 3,607
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

144. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,599
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

145. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,596
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

146. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 3,573
   easy vibe 一起 vibe ! Learn Vibe Coding From 0 to 1 ｜ Vibe Coding 零基础教程 ｜ 产品原型、AI 能力集成、前后端开发、多平台应用开发教程 ｜ Tutorial on Product Prototype, AI Capability Integration, Frontend and Backend Development, and Multi-platform Application Development

147. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,562
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

148. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 3,556
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks go from beginner to power user!

149. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,548
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

150. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,547
   Secure cloud-native MCP registry, gateway & orchestrator

151. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,520

152. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,472
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

153. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,472
   An Agentic Framework for Reflective PowerPoint Generation

154. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

155. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 3,451
   RikkaHub is an Android APP that supports for multiple LLM providers.

156. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,438
   A Model Context Protocol server for Excel file manipulation

157. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,407
   LangChain 🔌 MCP

158. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,381
   An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins.

159. **[mcp](https://github.com/google/mcp)** - ⭐ 3,366
   Google 💚 MCP

160. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,364
   Model Context Protocol(MCP) 编程极速入门

161. **[boost](https://github.com/laravel/boost)** - ⭐ 3,325
   Laravel-focused MCP server for augmenting your AI powered local development experience.

162. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,309
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

163. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,241
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

164. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,230
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

165. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,206
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

166. **[excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)** - ⭐ 3,198
   Fast and streamable Excalidraw MCP App

167. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,182
   Allow LLMs to control a browser with Browserbase and Stagehand

168. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 3,133
   The official Rust SDK for the Model Context Protocol

169. **[SimpleMem](https://github.com/aiming-lab/SimpleMem)** - ⭐ 3,128
   SimpleMem: Efficient Lifelong Memory for LLM Agents

170. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 3,110
   A full-stack AI Red Teaming platform securing AI ecosystems via AI Infra scan, MCP scan, Agent skills scan, and LLM jailbreak evaluation.

171. **[context-mode](https://github.com/mksglu/context-mode)** - ⭐ 3,104
   MCP is the protocol for tool access. We're the virtualization layer for context.

172. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 3,057
   Chrome extension to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

173. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,995
   n8n custom node for MCP

174. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,986
   AI agent microservice

175. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,985
   A TypeScript framework for building MCP servers.

176. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,978
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

177. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 2,937
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

178. **[Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)** - ⭐ 2,880
   Multi-modal Generative Media Skills for AI Agents (Claude Code, Cursor, Gemini CLI). High-quality image, video, and audio generation powered by muapi.ai.

179. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 2,826
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Antigravity, Copilot, VS Code)

180. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 2,802
   Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

181. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,739
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

182. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,684
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

183. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 2,653
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

184. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 2,635
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

185. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 2,635
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

186. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,613
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

187. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

188. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,561
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

189. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,550
   A CLI tool for building Go applications.

190. **[claude-context-mode](https://github.com/mksglu/claude-context-mode)** - ⭐ 2,522
   MCP is the protocol for tool access. We're the virtualization layer for context.

191. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,518
   Connect Supabase to your AI assistants

192. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,509
   MCP server for Grafana

193. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,485
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

194. **[EverMemOS](https://github.com/EverMind-AI/EverMemOS)** - ⭐ 2,483
   Long-term memory for your 24/7 OpenClaw agents across LLMs and platforms.

195. **[slackdump](https://github.com/rusq/slackdump)** - ⭐ 2,459
   Save or export your private and public Slack messages, threads, files, and users locally without admin privileges.

196. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,439
   A Model Context Protocol server for converting almost anything to Markdown

197. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 2,339
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

198. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,324
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

199. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,324
   A bridge between Streamable HTTP and stdio MCP transports

200. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,317
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

201. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,305
   A Model Context Protocol server for searching and analyzing arXiv papers

202. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,295

203. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 2,295
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

204. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,279
   A metasearch library that aggregates results from diverse web search services

205. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,270
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

206. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 2,269

207. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 2,248
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

208. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 2,234
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

209. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,179
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

210. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,175
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

211. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,160
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.1, Claude, Grok, DeepSeek, OpenRouter, Kimi 2.5, GLM 5, SiliconFlow, GPT-oss, Gemma 3, Qwen 3.5

212. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,127
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

213. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

214. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,095
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

215. **[code-graph-rag](https://github.com/vitali87/code-graph-rag)** - ⭐ 2,065
   The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

216. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,048
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

217. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 2,047
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

218. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,041
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

219. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,037
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

220. **[moltis](https://github.com/moltis-org/moltis)** - ⭐ 2,036
   A Rust-native claw you can trust. One binary — sandboxed, secure, auditable. Voice, memory, MCP tools, and multi-channel access built-in.

221. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 2,031
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

222. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 2,000
   The official MCP server implementation for the Perplexity API Platform

223. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,992
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

224. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 1,988
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

225. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,978
   directory for Awesome MCP Servers

226. **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** - ⭐ 1,918
   Universal SEO skill for Claude Code. 13 sub-skills, 6 subagents, extensions system with DataForSEO MCP integration. Technical SEO, E-E-A-T, schema, GEO/AEO, and strategic planning.

227. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,908
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

228. **[mcp-cli](https://github.com/IBM/mcp-cli)** - ⭐ 1,904

229. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,901
   Witsy: desktop AI assistant / universal MCP client

230. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,893
   Next Generation Agentic Proxy for AI Agents and MCP servers

231. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,891

232. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,888
   A secure low code honeypot framework, leveraging AI for System Virtualization.

233. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,887
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

234. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,855
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

235. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,832
   A Unified MCP Server Management App (MCP Manager).

236. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,828
   ⭐ All-in-one AI companion! Super Agent Party = Self hosted neuro sama + openclaw! ⭐ 全能AI伴侣！超级智能体派对 = 自托管neuro sama + openclaw!

237. **[esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** - ⭐ 1,822
   An AI-enabled NAT Router/Firewall for the ESP32

238. **[oh-my-pi](https://github.com/can1357/oh-my-pi)** - ⭐ 1,821
   ⌥  AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

239. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

240. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 1,802
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

241. **[agent-scan](https://github.com/snyk/agent-scan)** - ⭐ 1,797
   Security scanner for AI agents, MCP servers and agent skills.

242. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,790
   Test & Debug MCP servers, ChatGPT apps, and MCP Apps (ext-apps)

243. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,788
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

244. **[vexa](https://github.com/Vexa-ai/vexa)** - ⭐ 1,787
   Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.

245. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,785
   Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite

246. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,782
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

247. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,765
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

248. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,760
   Desktop Extensions: One-click local MCP server installation in desktop apps

249. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,747
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

250. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,745
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

251. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,743
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

252. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 1,738
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

253. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,723
   MCP server for interacting with the iOS simulator

254. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,721
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

255. **[plik](https://github.com/root-gg/plik)** - ⭐ 1,709
   Plik is a temporary file upload system (Wetransfer like) in Go.

256. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,687
   Interactive User Feedback MCP

257. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,671
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

258. **[skills](https://github.com/microsoft/skills)** - ⭐ 1,664
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

259. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,662
   Make RSS 📰 great again with AI 🧠✨!! [网页监控工具-预定送会员：https://waitlist.dingding.glidea.app]

260. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,647
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

261. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,636
   ToolHive makes deploying MCP servers easy, secure and fun

262. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,634
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

263. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,613
   Coding assistant MCP for Claude Desktop

264. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,595
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

265. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

266. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,575
   MCP server that provides tools and resources for interacting with n8n API

267. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,573
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

268. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 1,563
   339 plugins + 1896 agent skills for Claude Code. Open-source marketplace with CCPI package manager, interactive tutorials, and production orchestration patterns.

269. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 1,541
   An MCP server for interacting with the Financial Datasets stock market API.

270. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,535
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

271. **[pilot-shell](https://github.com/maxritter/pilot-shell)** - ⭐ 1,519
   The professional development environment for Claude Code. Claude Code is powerful. Pilot Shell makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

272. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,512
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

273. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,508
   An MCP server that installs other MCP servers for you

274. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,503
   Standards for building agents, better

275. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

276. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,486
   Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

277. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,475
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

278. **[NagaAgent](https://github.com/RTGS2017/NagaAgent)** - ⭐ 1,472
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

279. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,466
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

280. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,458
   Security scanner for AI agents, MCP servers and agent skills.

281. **[contextplus](https://github.com/ForLoopCodes/contextplus)** - ⭐ 1,439
   Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

282. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,437

283. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,432
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

284. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,431
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

285. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,429
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

286. **[agent-deck](https://github.com/asheshgoplani/agent-deck)** - ⭐ 1,426
   Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more.

287. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,425
   Semantic Search & Call Graphs for AI Agents (100% Local)

288. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,422
   Plugin for JADX to integrate MCP server

289. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 1,418
   Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

290. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,400
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

291. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,398
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

292. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,387
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

293. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 1,381
   MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

294. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,380
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

295. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 1,378
   This is the official website for TuriX Computer-use-Agent

296. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 1,369
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

297. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,363
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

298. **[ai](https://github.com/stripe/ai)** - ⭐ 1,350
   One-stop shop for building AI-powered products and businesses with Stripe.

299. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,349
   Make your own story. User-friendly software for LLM roleplaying

300. **[hotpath-rs](https://github.com/pawurb/hotpath-rs)** - ⭐ 1,344
   Rust Performance Profiler & Channels Monitoring Toolkit (TUI, MCP)

301. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,341
   MCP Server for kubernetes management commands

302. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,339
   Production ready MCP server with real-time search, extract, map & crawl.

303. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,331
   A connector for Claude Desktop to read and search an Obsidian vault.

304. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,321
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

305. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,320
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

306. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 1,309
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

307. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,307
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

308. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,302

309. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,302
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

310. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,294
   The official Swift SDK for Model Context Protocol servers and clients.

311. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,285
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

312. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,285
   docker mcp CLI plugin / MCP Gateway

313. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,279
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

314. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,270
   An official Qdrant Model Context Protocol (MCP) server implementation

315. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,267
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

316. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,263
   Damn Vulnerable MCP Server

317. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,248
   The official ElevenLabs MCP server

318. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,248
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

319. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,239
   An MCP server that autonomously evaluates web applications. 

320. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 1,239
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

321. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,237
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

322. **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** - ⭐ 1,234
   Humans and AI agents, building knowledge bases together. Self-hosted document annotation, version control, semantic search, and MCP.

323. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

324. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,223
   告别AI提前终止烦恼，助力AI更加持久

325. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,223
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

326. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

327. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,218
   The Grafbase GraphQL Federation Gateway

328. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,217
   The TypeScript MCP framework

329. **[claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** - ⭐ 1,209
   Personal AI CLI configuration for academic research & software development. Supports Claude Code, OpenCode, and Codex CLI — covering the full research lifecycle from ideation to publication.

330. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,203
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

331. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

332. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,201
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

333. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,188
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

334. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,187
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

335. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,181
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

336. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 1,181
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

337. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 1,167
   Claude Code as one-shot MCP server to have an agent in your agent.

338. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 1,160
   Build MCP Agents

339. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,157
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

340. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,151
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

341. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,150
   First gitlab mcp for you

342. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

343. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,146
   A Ruby Implementation of the Model Context Protocol

344. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,140
   A web UI for Claude Code agents

345. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 1,139
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

346. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 1,138
   The Unofficial and Awesome Home Assistant MCP Server

347. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,134
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

348. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,129
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

349. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 1,129
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

350. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 1,127
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

351. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,116
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

352. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,109
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

353. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,092
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

354. **[drawio-mcp](https://github.com/jgraph/drawio-mcp)** - ⭐ 1,088

355. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,081
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

356. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,078
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

357. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 1,069
   Model Context Protocol for WinDBG

358. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 1,065
   Connect AI models like Claude & GPT with robots using MCP and ROS.

359. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,062
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

360. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,041
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

361. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,039
   On-premises conversational RAG with configurable containers

362. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,039
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

363. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,038
   MCP Python Tutorial 

364. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 1,037
   MCP integration for Google Calendar to manage events.

365. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 1,036
   Bringing the power of MCP to the web

366. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 1,036
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

367. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,035
   Query and Summarize your chat messages.

368. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,029
   A curated list of Model Context Protocol (MCP) servers 

369. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

370. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 1,019
   A repository of servers and clients from the Model Context Protocol tutorials

371. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 1,019
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and perform job searches.

372. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,015
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

373. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 1,013
   Remote MCP Servers

374. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 1,010
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

375. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 1,006
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

376. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 1,003
   MCP server for fetch web page content using Playwright headless browser.

377. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 999
   Draw.io Model Context Protocol (MCP) Server

378. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 998
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

379. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 992
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

380. **[agents](https://github.com/inkeep/agents)** - ⭐ 987
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

381. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 977
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

382. **[muapi-cli](https://github.com/SamurAIGPT/muapi-cli)** - ⭐ 970
   Official CLI for muapi.ai — generate images, videos & audio from the terminal. MCP server, 14 AI models, npm + pip installable.

383. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 970
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

384. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 970
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

385. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 969
   Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

386. **[amical](https://github.com/amicalhq/amical)** - ⭐ 966
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

387. **[FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline)** - ⭐ 966
   FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestration. It facilitates transparent, human-in-the-loop creation with reusable Style Skills for consistent, professional storytelling.

388. **[tools](https://github.com/strands-agents/tools)** - ⭐ 962
   A set of tools that gives agents powerful capabilities.

389. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 957
   Lighweight CLI to interact with MCP servers

390. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 954
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

391. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 953
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

392. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 948
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

393. **[jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp)** - ⭐ 948
   Token-efficient MCP server for GitHub source code exploration via tree-sitter AST parsing

394. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 943
   Expose llms-txt to IDEs for development

395. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 942
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

396. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 935
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

397. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 931
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

398. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 929
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

399. **[engram](https://github.com/Gentleman-Programming/engram)** - ⭐ 926
   Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

400. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 924
   A security scanner for your LLM agentic workflows

401. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 918
   A middleware to provide an openAI compatible endpoint that can call MCP tools

402. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 912
   Neo4j Labs Model Context Protocol servers

403. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 911

404. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

405. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 905
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

406. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 904
   A framework for writing MCP (Model Context Protocol) servers in Typescript

407. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 897
   MCP server helping models to understand your Vite/Nuxt app better.

408. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 894
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

409. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 894
   Self-hosted MCP Gateway for AI agents

410. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 894
   Delegate tasks to Codex and Gemini directly from within Claude Code.

411. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 889
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

412. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 884
   Allow AI to wade through complex OpenAPIs using Simple Language

413. **[shellfirm](https://github.com/kaplanelad/shellfirm)** - ⭐ 883
   Safety guardrails for ai coding agents and human terminal commands

414. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 882
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility. Since 2018.

415. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 881
   A library for communication with a Minecraft client/server.

416. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 881
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

417. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

418. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 876
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

419. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 875

420. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 875
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

421. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 873
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

422. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 871
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

423. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 871
   OpenAPI Tool Servers

424. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 870
   A concise list for mcp servers

425. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 867
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

426. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 866
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

427. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 865

428. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 856

429. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 853
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

430. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 847
   A Model Context Protocol (MCP) server for Kubernetes. Install: npx kubectl-mcp-server or pip install kubectl-mcp-server

431. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 836
   Scan MCP servers for potential threats & security findings.

432. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

433. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 835
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

434. **[nono](https://github.com/always-further/nono)** - ⭐ 835
   Secure, kernel-enforced sandbox CLI and SDKs for AI agents. Capability-based isolation with secure key management, atomic rollback, cryptographic immutable audit chain of provenance. Run your agents in a zero-trust environment.

435. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

436. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 833
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

437. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 831
   A minimalistic MCP client with a good feature set.

438. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 824
   Interactive web apps for AI agents.

439. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 823
   The best way to create, deploy, and share MCP Servers

440. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 821
   Simple, modular, and observable Go framework for backend applications.

441. **[server](https://github.com/php-mcp/server)** - ⭐ 819
   Core PHP implementation for the Model Context Protocol (MCP) server

442. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 819
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

443. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 815
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

444. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 813
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

445. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 811
   Browse the web, directly from Cursor etc.

446. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 811
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

447. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

448. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 809
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

449. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 806
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

450. **[context-space](https://github.com/context-space/context-space)** - ⭐ 805
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

451. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 802
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

452. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 800
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

453. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 799
   A secure local sandbox to run LLM-generated code using Apple containers

454. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 798
   一个将ACE(Augment Context Engine) 做成MCP的项目

455. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 792
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

456. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 786
   A self-hosted RSS reader and personal knowledge management tool.

457. **[vllora](https://github.com/vllora/vllora)** - ⭐ 781
   Debug your AI agents

458. **[GrokSearch](https://github.com/GuDaStudio/GrokSearch)** - ⭐ 780
   Integrate Grok's powerful real-time search capabilities into Claude via the MCP protocol!

459. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 779
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

460. **[Context](https://github.com/indragiek/Context)** - ⭐ 778
   Native macOS client for Model Context Protocol (MCP)

461. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 777
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

462. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 773
   A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations.

463. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 772
   Vibetest MCP - automated QA testing using Browser-Use agents

464. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 763
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

465. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 762
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

466. **[runno](https://github.com/taybenlor/runno)** - ⭐ 761
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

467. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 760
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

468. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 758
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

469. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 758

470. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 755
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

471. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 753
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

472. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 750
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

473. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 745
   The official Ruby SDK for the Model Context Protocol.

474. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 744
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

475. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 742
   LLDB MCP Integration + other helpful commands

476. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 742
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

477. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 741
   A MCP server implementation for hyperbrowser

478. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 733
   All in one vscode plugin for mcp developer

479. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 731
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

480. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 728
   提取抖音无水印视频链接，视频文案，douyin-mcp-server，mcp，claude skill

481. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 720
   Skybridge is a framework for building ChatGPT & MCP Apps

482. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 718
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

483. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 716
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

484. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 716
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

485. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 715
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

486. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 713
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

487. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 708
   A flexible HTTP fetching Model Context Protocol server.

488. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 707
   Connect ClickHouse to your AI assistants.

489. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 706
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

490. **[headroom](https://github.com/chopratejas/headroom)** - ⭐ 706
   The Context Optimization Layer for LLM Applications

491. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 705
   Clojure MCP

492. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 702
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  全球首个通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

493. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 702
   gcloud MCP server

494. **[mcp](https://github.com/laravel/mcp)** - ⭐ 700
   Rapidly build MCP servers for your Laravel applications.

495. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 696
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

496. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 692
   An MCP server that provides control over Android devices via adb

497. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 690
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

498. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 689
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

499. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 687
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

500. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 686
   MCP server for Docker

501. **[Horizon](https://github.com/Thysrael/Horizon)** - ⭐ 686
   Automated AI news aggregator & summarizer. Generates daily briefings in English & Chinese. | 全自动 AI 科技新闻聚合与摘要生成器。

502. **[samples](https://github.com/strands-agents/samples)** - ⭐ 682
   Agent samples built using the Strands Agents SDK.

503. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 669
   A simple CLI to run LLM prompt and implement MCP client.

504. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 667
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

505. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 666
   Next.js Development for Coding Agent

506. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 663
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

507. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 663
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+15,000 via SkillKit), 42 commands, 120 plugins, 19 hooks, 15 rules, 7 templates, 6 MCP configs, and more.

508. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 659
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

509. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 657
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

510. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

511. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 654
   MCP Server For Turkish Legal Databases

512. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 654
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

513. **[opennews-mcp](https://github.com/6551Team/opennews-mcp)** - ⭐ 652
   Crypto News Aggregation · AI Ratings · Trading Signals · Real-time Updates

514. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 651
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

515. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 650
   Laravel API for Ai Agents and humans.

516. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 648
   Shell and coding agent on mcp clients

517. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 647
   Querying local documents, powered by LLM

518. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 647
   A simple MCP server for Obsidian

519. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 647
   A lightweight, developer-focused database management tool. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

520. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 643
   EnrichMCP is a python framework for building data driven MCP servers

521. **[Wax](https://github.com/christopherkarani/Wax)** - ⭐ 642
   Lightening fast RAG on Apple Silicon. On-Device. No Server. No API. One File. Pure Swift

522. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

523. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 641
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

524. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 639
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

525. **[obot](https://github.com/obot-platform/obot)** - ⭐ 633
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

526. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 630
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

527. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 628

528. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 627
   Talk to a Cloudflare Worker from Claude Desktop!

529. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

530. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

531. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 624
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

532. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 621

533. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 618

534. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 618
   A simple, locally hosted Web Search MCP server for use with Local LLMs

535. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 617
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

536. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 615
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

537. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 614
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

538. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 613
   MCP server integration for DaVinci Resolve

539. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 612
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

540. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 612
   mem-agent mcp server

541. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 611
   A local Apple Documentation crawler and MCP server. Written in Swift.

542. **[goclaw](https://github.com/nextlevelbuilder/goclaw)** - ⭐ 608
   Multi-agent AI gateway with teams, delegation & orchestration. Single Go binary, 11+ LLM providers, 5 channels.

543. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 604
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

544. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 604
   Convert Any OpenAPI V3 API to MCP Server

545. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 601
   Daydreams is a set of tools for building agents for commerce

546. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 601
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

547. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 600
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

548. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 598
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

549. **[room](https://github.com/quoroom-ai/room)** - ⭐ 596
   Open-source earning-focused swarm intelligence engine. Self-governing AI collectives (queen, workers, quorum voting) running locally via MCP. Works with Claude Code, Codex, or pay-per-use APIs.

550. **[tome](https://github.com/runebookai/tome)** - ⭐ 596
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

551. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 595
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

552. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 595
   A coding agent and general agent harness for building and orchestrating agentic applications.

553. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 595
   "AnyTool: Universal Tool-Use Layer for AI Agents"

554. **[clihub](https://github.com/thellimist/clihub)** - ⭐ 594
   Turn any MCP server into CLI

555. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 593
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

556. **[Overture](https://github.com/SixHq/Overture)** - ⭐ 593
   Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. 

557. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 590
   An MCP server for interacting with Sentry via LLMs.

558. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 590
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

559. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 588
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

560. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 587
   MCP to connect your LLM with Spotify.

561. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 587
   FreeCAD MCP(Model Context Protocol) server

562. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 584
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

563. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 583
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

564. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 583
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

565. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 580
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

566. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 578
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

567. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 577
   LangGraph solution template for MCP

568. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 572
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

569. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 570
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

570. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 570
   The .NET library to build AI agents with 30+ built-in connectors.

571. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 568
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

572. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 567
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

573. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 566

574. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 565
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

575. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 563
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

576. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 562
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

577. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 561
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

578. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 561
   A comprehensive collection of Model Context Protocol (MCP) servers

579. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 561
   Install, manage and develop MCP servers and skills for agents

580. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 560
   MCP server for interacting with Neon Management API and databases

581. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 558
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

582. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 558
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

583. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 558
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

584. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 556
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

585. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

586. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 555
   MCP server to deploy apps to Cloud Run

587. **[casbin-gateway](https://github.com/casbin/casbin-gateway)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

588. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 554
   MCP configuration to connect AI agent to a Linux machine.

589. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 552
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

590. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 552
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

591. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 551
   An Mcp client inside Emacs

592. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 551
   A MCP server for Home Assistant

593. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 549
   Open Source Voice Agent Platform

594. **[work-iq](https://github.com/microsoft/work-iq)** - ⭐ 547
   MCP Server and CLI for accessing Work IQ

595. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 546
   Security scanner for MCP servers

596. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 546
   An MCP Multimodal AI Agent with eyes and ears!

597. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 545
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

598. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 545
   OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s. Works with Claude Code.

599. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 543
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

600. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 543
   GitOps on Autopilot Mode

601. **[nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** - ⭐ 542
   A lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents. Say goodbye to Vector RAG and amnesia. Empower your AI with persistent, graph-like structured memory across any model, session, or tool. Drop-in replacement for OpenClaw.

602. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 541
   A structural code search engine for Al agents.

603. **[tda](https://github.com/irockel/tda)** - ⭐ 537
   TDA - Thread Dump Analyzer (for Java). Analyze your Thread Dumps with a GUI or use it as MCP Server.

604. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 536
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

605. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 536

606. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 535
   MCP Server for Burp

607. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 534
   MCP Server and CLI for accessing Work IQ

608. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 534
   A tool that converts OpenAPI specifications to MCP server

609. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 533
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

610. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 531

611. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 529
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

612. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 528

613. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 527
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

614. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 527
   微信读书MCP

615. **[axon](https://github.com/harshkedia177/axon)** - ⭐ 527
   Graph-powered code intelligence engine — indexes codebases into a knowledge graph, exposed via MCP tools for AI agents and a CLI for developers.

616. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 526
   Official Jina AI Remote MCP Server

617. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 525
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

618. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 525
   MCP to allow AI agents to control Unreal

619. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 524
   A Model Context Protocol server for IDA

620. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 524
   An MCP server to query any Postgres database in natural language.

621. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 523
   飞书/Lark官方 OpenAPI MCP

622. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 522
   MCP server for querying Apple Health data with natural language and SQL

623. **[ethora](https://github.com/dappros/ethora)** - ⭐ 521
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

624. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 520
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

625. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 519
   MCP Server for Metasploit

626. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 519
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

627. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 519
   Google Search Console Insights with Claude AI for SEOs

628. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 517
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

629. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

630. **[GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP)** - ⭐ 515
   An MCP extension for Ghidra

631. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 513
   A model-driven approach to building AI agents in just a few lines of code. 

632. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 512
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

633. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 511
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single) 

634. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 511
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

635. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 510
   An MCP extension for Ghidra

636. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 509
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

637. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 509

638. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 509
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

639. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 508
   MCP Server for Turkish & American Stock Exchange and Fund Data

640. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 508
   MCP Server for SearXNG

641. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

642. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 507
   MCP server for document format conversion using pandoc.

643. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 507

644. **[openpencil](https://github.com/ZSeven-W/openpencil)** - ⭐ 506
   The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.

645. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 505
   A MCP (Model Context Protocol) server for interacting with dbt.

646. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 502
   Yes Mcp server in bash

647. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 502
   Making docling agentic through MCP

648. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 501
   MCP Monitoring with eBPF

649. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 501
   A Model-Context Protocol Server for YouTube

650. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 501
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

651. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 500
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

652. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 499
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

653. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 498
   LLM + MCP + RAG = Magic

654. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 498

655. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 497
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

656. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 494
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

657. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

658. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 493
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

659. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 493
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

660. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 492
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

661. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

662. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 491
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

663. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 490
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

664. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 487
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

665. **[probe](https://github.com/probelabs/probe)** - ⭐ 487
   AI-friendly semantic code search engine for large codebases. Combines ripgrep speed with tree-sitter AST parsing. Powers AI coding assistants with precise, context-aware code understanding.

666. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 487
   AI-based stock analysis and trading system

667. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 486
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

668. **[ShipSwift](https://github.com/signerlabs/ShipSwift)** - ⭐ 483
   AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

669. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 481
   🚀 Universal SDK for building next-gen MCP servers

670. **[argo](https://github.com/xark-argo/argo)** - ⭐ 480
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

671. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 480
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

672. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 479
   MCP Server to interact with Google Gsuite prodcuts

673. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 479
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

674. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 478
   A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI.

675. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 478
   Govern & Secure your AI

676. **[codexia](https://github.com/milisp/codexia)** - ⭐ 475
   Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, Tauri

677. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 475
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

678. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 475
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

679. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 473
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

680. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 472
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (Claude Code, Cursor, Antigravity, etc.) to read, analyze, and modify Figma designs

681. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 471
   An SDK building Laravel MCP servers

682. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 471
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

683. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 470
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

684. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 469
   Aser is a lightweight, self-assembling AI Agent frame.

685. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 469
   MCP-NixOS - Model Context Protocol Server for NixOS resources

686. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 467
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

687. **[director](https://github.com/director-run/director)** - ⭐ 466
   MCP Playbooks for AI agents

688. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 466
   Make your meetings accessible to AI Agents

689. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 466
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

690. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 464
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

691. **[resend-mcp](https://github.com/resend/resend-mcp)** - ⭐ 464
   The official MCP server to send emails and interact with Resend

692. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 463
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

693. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 459
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

694. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 458
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

695. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 458
   BioMCP: Biomedical Model Context Protocol

696. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 455
   A docker MCP Server (modelcontextprotocol)

697. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 455
   小红书MCP服务 x-s x-t js逆向

698. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 455
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

699. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 454
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

700. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 453
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

701. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 453
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

702. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 450
   Official Docker MCP registry 

703. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 448

704. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 448
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

705. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 447
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

706. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

707. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

708. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 445
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

709. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

710. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 443
   MCP Server for interacting with Android Devices.

711. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 438
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

712. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 436
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

713. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 436
   Local MCP server for DuckDB and MotherDuck

714. **[docfork](https://github.com/docfork/docfork)** - ⭐ 433
   Docfork - Up-to-date Docs for AI Agents.

715. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 431
   MCP server that execute applescript giving you full control of your Mac

716. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 430
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

717. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 429
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

718. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 427
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

719. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 427
   Spec-Driven Development MCP Server, not just Vibe Coding

720. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 427
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

721. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 426
   基于NET搭建-AI知识库智能体-现代化Saas企业级前后端分离架构：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR识别、API多版本、单元测试、RabbitMQ、代码生成器、AI知识库、AI联网搜索

722. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 424
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

723. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 424
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT, Deepseek, Claude Sonnet/Opus APIs, Google Gemini 3, Alibaba Qwen, Kimi, and Grok 4.1, with plans to add TTS, Elevenlabs, Inworld, OpenRouter, Groq, Dashscope, Responses APIs, UnrealClaude soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

724. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 423
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

725. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

726. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 422
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

727. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 422
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

728. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 421
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

729. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 421
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

730. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 418
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

731. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 418
   Unlock 650+ MCP servers tools in your favorite agentic framework.

732. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 416
   A CLI inspector for the Model Context Protocol

733. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 415
   SonarQube MCP Server

734. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 414
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

735. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 413
   Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

736. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 412
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

737. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 411

738. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 410
   Baidu Map MCP Server

739. **[keeper.sh](https://github.com/ridafkih/keeper.sh)** - ⭐ 410
   Open-source calendar sync tool. Aggregate events from Google, Outlook, iCloud & CalDAV into one anonymized feed.

740. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 409
   Memento MCP: A Knowledge Graph Memory System for LLMs

741. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 409
   Skill and MCP server for searching and retrieving icons

742. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 409
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

743. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 408
   MaverickMCP - Personal Stock Analysis MCP Server

744. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 407
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

745. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 405
   The safest way to make REST calls in C# with an MCP Generator

746. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 405
   lunar.dev: Agent native MCP Gateway for governance and security

747. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 405
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

748. **[roam-code](https://github.com/Cranot/roam-code)** - ⭐ 404
   Architectural intelligence layer for AI coding agents. Structural graph, architecture governance, multi-agent orchestration, vulnerability mapping. 139 commands, 101 MCP tools, 26 languages, 100% local.

749. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 404
   Standalone Roblox Studio MCP Server

750. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 401
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

751. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 399
   An experiment in software planning using MCP

752. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 396
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

753. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 395
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

754. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 395
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

755. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 394
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

756. **[speakeasy](https://github.com/speakeasy-api/speakeasy)** - ⭐ 393
   Build APIs your users love ❤️ with Speakeasy. ✨ Polished and type-safe SDKs. 🌐 Terraform providers, MCP servers, CLIs and Contract Tests for your API. OpenAPI native. 

757. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 393
   Search Airbnb using your AI Agent

758. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 392
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

759. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 390
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

760. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 390
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

761. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 390
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

762. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 390
   The AI agent that grows your YouTube channel on autopilot.

763. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 389
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

764. **[station](https://github.com/cloudshipai/station)** - ⭐ 389
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

765. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 387
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

766. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 387
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

767. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 383
   MCP Server for code graph analysis and visualization by CodeGPT

768. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 382
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

769. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 382
   Local Groq Desktop chat app with MCP support

770. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 382
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

771. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 382
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

772. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 382
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

773. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 381
   OpenSkills: Run Claude Skills Locally using any LLM

774. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 380
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

775. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 380
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

776. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 379
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

777. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 379
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

778. **[daymon](https://github.com/daymonio/daymon)** - ⭐ 378
   Daymon puts your favorite AI to work 24/7. It schedules, remembers, and orchestrates your own virtual team. Free.

779. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 378
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

780. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 378
   MCP server for Todoist integration enabling natural language task management with Claude

781. **[opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp)** - ⭐ 378
   Twitter/X Data · User Profiles · Tweet Search · Follower Events · KOL Tracking

782. **[stitch-mcp](https://github.com/davideast/stitch-mcp)** - ⭐ 376
   A CLI for moving AI-generated UI designs from Google’s Stitch platform into your development workflow.

783. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 374
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

784. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 374
   MCP server connecting to Kubernetes

785. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 374
   An MCP server for loading skills (shim for non-claude clients).

786. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 373
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

787. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 373
   An MCP implementation for Selenium WebDriver

788. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 372
   Model Context Protocol (MCP) Server for Graphlit Platform

789. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

790. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 372
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

791. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 372
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

792. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 369
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

793. **[mcp2cli](https://github.com/knowsuchagency/mcp2cli)** - ⭐ 369
   Turn any MCP server or OpenAPI spec into a CLI — at runtime, with zero codegen

794. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 368
   A guide on how to use the Figma MCP server

795. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 367
   MCP server that provides LLMs with tools for interacting with EVM networks

796. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 367
   MCP Server implementation for Ableton Live OSC control

797. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 367
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

798. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 366
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

799. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 366
   F2C MCP Server

800. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 366
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

801. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 366
   A macOS AppleScript MCP server

802. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

803. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 365
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

804. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 364
   Model Context Protocol server for GraphQL

805. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 363
   Model Context Protocol SDK for PHP

806. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 362
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

807. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 362
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

808. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 362
   MCP Server implementation for Xcode integration

809. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 362
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

810. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 362
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

811. **[devopness](https://github.com/devopness/devopness)** - ⭐ 361
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

812. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 360
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

813. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 360
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

814. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 359
   Context-Engine MCP - Agentic Context Compression Suite

815. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 359
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

816. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 358
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

817. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 357
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

818. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 357
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

819. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 357
   Create a plan from a description in minutes

820. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 357
   Control your Android devices with AI using Model Context Protocol

821. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 357
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to make direct edits and formatting.

822. **[pinion-os](https://github.com/chu2bard/pinion-os)** - ⭐ 356
   Client SDK, Claude plugin and skill framework for the Pinion protocol. x402 micropayments on Base.

823. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 356
   Xiaozhi MCP sample program

824. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 356
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript and C++.

825. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

826. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 355

827. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 354
   🐕⚡「极简至上 效率为王 秒级接入 一链即用」的 AI Bot

828. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 352
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

829. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 352
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

830. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 351
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

831. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 351
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

832. **[mcp](https://github.com/IBM/mcp)** - ⭐ 351
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

833. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 351
   A centralized reverse-proxy platform for MCP servers — manage, group, and export as Skills from a single endpoint.

834. **[mq](https://github.com/harehare/mq)** - ⭐ 351
   jq-like command-line tool for markdown processing

835. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 350
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

836. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 350
   Things.app MCP Server

837. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 349
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

838. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 348
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

839. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

840. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 347
   Elixir Model Context Protocol (MCP) SDK

841. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 345
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

842. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 345

843. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 345
   MCP server for searching and retrieving Claude Agent Skills using vector search

844. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 342
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

845. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 341
   An implementation of Model Context Protocol (MCP) server for Argo CD.

846. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 341
   An MCP server for Azure DevOps

847. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 341
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

848. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

849. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 340
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

850. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 339
   MCP server to expose VS Code editing features to an LLM for AI coding

851. **[studio](https://github.com/decocms/studio)** - ⭐ 339
   Open-source control plane for your AI agents. Connect tools, hire agents, track every token and dollar

852. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 338
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

853. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

854. **[mesh](https://github.com/decocms/mesh)** - ⭐ 337
   One secure endpoint for every MCP server. Deploy anywhere.

855. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 336
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

856. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 336
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

857. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 335
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

858. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 335
   MCP server retrieving transcripts of YouTube videos

859. **[daan](https://github.com/pluveto/daan)** - ⭐ 334
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

860. **[boltmcp](https://github.com/boltmcp/boltmcp)** - ⭐ 334

861. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 333

862. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 333
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

863. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 332
   deep, reliable and confidential coding-context

864. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 331
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

865. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

866. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 331
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

867. **[moling](https://github.com/gojue/moling)** - ⭐ 330
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

868. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 330
   Sega Master System / Game Gear / SG-1000 emulator, debugger and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

869. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 329

870. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 329
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

871. **[skylos](https://github.com/duriantaco/skylos)** - ⭐ 328
   High-precision Python SAST & Dead Code Remover. Finds unused functions, secrets, and security flaws with hybrid static analysis + local LLM agents. Privacy-first & low noise. MCP server for SAST too. Docs: https://docs.skylos.dev/

872. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 328
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

873. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 326
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

874. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 325
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

875. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 325
   MCP to help Defenders Detection Engineer Harder and Smarter

876. **[MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)** - ⭐ 323
   MeiGen-AI-Design-MCP — Turn Claude Code / OpenClaw into your local Lovart. Local ComfyUI, 1,400+ prompt library, multi-direction parallel generation.

877. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

878. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 322
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

879. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 321
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

880. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 321
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

881. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 321
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

882. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 320
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

883. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 319
   This is a Minecraft Base Client

884. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 319
   MCP server for JADX-AI Plugin

885. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 319
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

886. **[real-estate-mcp](https://github.com/tae0y/real-estate-mcp)** - ⭐ 319
   Ask Claude about Korean apartment prices — powered by MOLIT's open API

887. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 318
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

888. **[emcee](https://github.com/mattt/emcee)** - ⭐ 318
   MCP generator for OpenAPIs 🫳🎤💥

889. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 318
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

890. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 316
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

891. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 316
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

892. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 316
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

893. **[deep-research-mcp](https://github.com/teelaitila/deep-research-mcp)** - ⭐ 315

894. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 315
   Mapbox Model Context Protocol (MCP) server

895. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 315
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

896. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 314
   Repo of skills for autogen studio using model context protocol (mcp)

897. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 314
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

898. **[safe-mcp](https://github.com/safe-agentic-framework/safe-mcp)** - ⭐ 313
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

899. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 313
   A Model Context Protocol server for building an investor agent

900. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 312
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

901. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 311

902. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 311
   Lean Theorem Prover MCP

903. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 310
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

904. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 310

905. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 310
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

906. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

907. **[cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)** - ⭐ 309
   A super light-weight embedded code mcp (AST based) that just works - saves 70% token and improves speed for coding agent. 🌟 Star if you like it!

908. **[generator](https://github.com/context-hub/generator)** - ⭐ 308
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

909. **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** - ⭐ 307
   MCP server that indexes your codebase into a persistent knowledge graph. 64 languages, sub-ms queries, 99% fewer tokens than grep. Single Go binary, no Docker, no API keys.

910. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 306
   api router for MCP Servers

911. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 306
   First AI‑enabled open-source Human Capital Management system that you can start using today.

912. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 305
   Smithery helps AI agents access external services via a unified gateway.

913. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 305
   MCP Server for interacting with Salesforce instances

914. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 305
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

915. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 304
   A working pattern for SSE-based MCP clients and servers

916. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 304
   Turn any openapi file into an mcp server, with just the tools you need.

917. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 303
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

918. **[freee-mcp](https://github.com/freee/freee-mcp)** - ⭐ 303
   Model Context Protocol (MCP) server for freee API integration

919. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 302
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

920. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 302
   Model Context Protocol server for DeepSeek's advanced language models

921. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 302
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

922. **[idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)** - ⭐ 301
   Pre-build reality check for AI coding agents. Scans GitHub, HN, npm, PyPI & Product Hunt — returns a 0-100 reality signal. MCP tool. Try: mnemox.ai/check

923. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 299
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

924. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 299
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

925. **[mcp](https://github.com/oracle/mcp)** - ⭐ 298
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

926. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 298
   Source code of minecraft 1.12

927. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 298
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

928. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 297
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

929. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 296
   MCP implementation of Claude Code capabilities and more

930. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 296
   Agentic RAG for any scenario. Customize sources, depth, and width

931. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 296
   MCP server for Windows OS automation

932. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 295
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

933. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 295
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

934. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 295
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

935. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 294
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

936. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 293
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

937. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 292
   An MCP server providing tools for image processing operations

938. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 292
   Obsidian MCP (Model Context Protocol) Server

939. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 292
   Discover Exceptional MCP Servers

940. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 292
   Minimal MCP Server for Aider

941. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 292
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

942. **[consult7](https://github.com/szeider/consult7)** - ⭐ 291
   MCP server to consult a language model with large context size

943. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 291
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

944. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 290

945. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 290
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

946. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 290
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

947. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 289
   The specification for the Universal Tool Calling Protocol

948. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 289
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

949. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 289

950. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 288
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

951. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 287
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

952. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 287
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

953. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 287
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

954. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 287
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands. 

955. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 287
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

956. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

957. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 286
   simple web ui to manage mcp (model context protocol) servers in the claude app

958. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 286
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

959. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

960. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 285
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

961. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 284
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

962. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 284
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

963. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

964. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 283
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

965. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 282
   MCP server for browser automation using Playwright

966. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 282
   Home Assistant MCP Server

967. **[alfanous](https://github.com/Alfanous-team/alfanous)** - ⭐ 282
   Alfanous is an Arabic search engine API provides the simple and advanced search in Quran , more features and many interfaces...

968. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 282
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

969. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 282
   MCP Server for Odoo

970. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

971. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 281
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

972. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

973. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 280
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

974. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 278
   MCP integration platforms making AI-Agents developers focusing on their own tasks

975. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 277
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

976. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 277
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

977. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 277
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

978. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 276
   A Model Context Protocol Server for MongoDB

979. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

980. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 276
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

981. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 274
   Model Context Protocol (MCP) Server for dify workflows

982. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 272
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

983. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

984. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 271
   MCP Server for Tree-sitter

985. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 271
   Bring your project into LLM context - tool and MCP server

986. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 270
   Model Context Protocol server implementation for Reddit

987. **[BitFun](https://github.com/GCWing/BitFun)** - ⭐ 270
   BitFun is an Agentic Development Environment (ADE，AI IDE) featuring a cutting-edge Code Agent system with four modes — Agentic, Plan, Debug, and Review. Extensible via MCP, Skills, custom Agents and Rules. Built with Rust + TypeScript for an ultra-lightweight, fluid cross-platform experience.

988. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 270
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

989. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 270
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

990. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 270
   MCP server for Bazi (八字) information

991. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 270
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

992. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

993. **[agents](https://github.com/astronomer/agents)** - ⭐ 269
   AI agent tooling for data engineering workflows.

994. **[google-ads-mcp](https://github.com/googleads/google-ads-mcp)** - ⭐ 269

995. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 268
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

996. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 268
   Apollo MCP Server

997. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 268
   MCP server for Claude to access Outlook data via Microsoft Graph API

998. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 268
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

999. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 268
   SpringAI，LLM，MCP，Embedding

1000. **[robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp)** - ⭐ 268
   Create agentic AI workflows in ROBLOX Studio

1001. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 267
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

1002. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 265
   小智AI客户端，目前主要用于MCP的对接

1003. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 265
   Bringing Human Capabilities to AI Agents

1004. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 263
   Apache Doris MCP Server

1005. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 262
   An MCP server for Massive.com Financial Market Data

1006. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 261
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

1007. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 261
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

1008. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 260
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

1009. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 260
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

1010. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 259
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

1011. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 258
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

1012. **[api200](https://github.com/API-200/api200)** - ⭐ 258
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

1013. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 258
   Volcengine MCP Servers

1014. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 258
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1015. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 257
   An introduction to the world of AI Agents

1016. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 257
   Standardized environment infrastructure for Agentic AI development.

1017. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 257
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1018. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 257
   CAD MCP Server

1019. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 257
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

1020. **[swiss-ai-call-agent](https://github.com/Chrissotino/swiss-ai-call-agent)** - ⭐ 256
   Enterprise-grade AI Call Agent for the Swiss market – inbound & outbound calls, multilingual (DE/FR/IT), MCP architecture, Claude AI decision engine, real-time dashboard

1021. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 255
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

1022. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 255
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

1023. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 255
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

1024. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 255
   A code reasoning MCP server, a fork of sequential-thinking

1025. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 255
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1026. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 254
   MCP server to access Garmin data

1027. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

1028. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 253
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

1029. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 252
   hydra-ai

1030. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 251
   MCP server(s) for Aipolabs ACI.dev

1031. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 251
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

1032. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 251
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

1033. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 250
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

1034. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 250
   A collection of MCP servers

1035. **[aso-skills](https://github.com/Eronred/aso-skills)** - ⭐ 250
   AI agent skills for App Store Optimization (ASO) and mobile app marketing. Built for indie developers, app marketers, and growth teams who want Cursor, Claude Code, or any Agent Skills-compatible AI assistant to help with keyword research, metadata optimization, competitor analysis, and app growth.

1036. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 248
   MCP server implementation for Google's Gemini API

1037. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 248
   MCP Interface for Video Jungle

1038. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 248
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

1039. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 248

1040. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 248
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1041. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

1042. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

1043. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 247
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

1044. **[api-agent](https://github.com/agoda-com/api-agent)** - ⭐ 246
   Universal MCP server for GraphQL/REST APIs

1045. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 246
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

1046. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 246
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

1047. **[meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)** - ⭐ 245
   Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis.

1048. **[domain-check](https://github.com/saidutt46/domain-check)** - ⭐ 245
   Fast, universal domain availability checker - 1,200+ TLDs, pattern generation, RDAP with WHOIS fallback. CLI + Rust library + MCP server for AI agents.

1049. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1050. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1051. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 244
   Lightweight MCP server for Spotify

1052. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 244
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

1053. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 243
   Semantic code searcher and codebase utility

1054. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 243
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

1055. **[embodied-claude](https://github.com/lifemate-ai/embodied-claude)** - ⭐ 243
   Claudeに身体性を与えるMCP群

1056. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 243
   AWS MCP Proxy Server

1057. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 243
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

1058. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 242
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

1059. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 242
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

1060. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 242
   An experimental MCP Server for foundry built for Solidity devs

1061. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 241
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

1062. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 241
   The evaluation benchmark on MCP servers

1063. **[mcp](https://github.com/cloudflare/mcp)** - ⭐ 241
   MCP server for the Cloudflare API

1064. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 240
   Turn any MCP server into a Python module

1065. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

1066. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 240
   🔥 Model Context Protocol (MCP) server for Firebase.

1067. **[dat](https://github.com/hexinfo/dat)** - ⭐ 240
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

1068. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 239
   Simplified Gemini for Claude Code. 

1069. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 239
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

1070. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

1071. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 239
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

1072. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 239
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1073. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 239
   Code Runner MCP Server

1074. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 238

1075. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 237
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

1076. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 236
   MCP Server for Telegram

1077. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 236
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1078. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 236
   A list of open-source AI projects you can use to generate income easily.

1079. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

1080. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 235
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1081. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 235
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1082. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 235
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1083. **[PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor)** - ⭐ 235
   Free, open-source SQL Server performance monitoring. Full Edition (server-installed, 30 collectors) and Lite Edition (standalone, DuckDB). Built-in MCP server for AI integration.

1084. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 233
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

1085. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 233
   A MCP server for our beloved terminal multiplexer tmux.

1086. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 232
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

1087. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 232
   Playwright MCP fork that works with Cloudflare Browser Rendering

1088. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 232
   A Model Context Protocol (MCP) server that enables natural language queries to databases

1089. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 231
   Creates a simple MCP tool server with "streaming" HTTP.

1090. **[agentrove](https://github.com/Mng-dev-ai/agentrove)** - ⭐ 231
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1091. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 230
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

1092. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 230
   Zerodha Kite MCP server

1093. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 230
   Lightweight C++ MCP (Model Context Protocol) SDK

1094. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1095. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 229
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

1096. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 229
   MCP server for Anki via AnkiConnect

1097. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 228
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

1098. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 228
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1099. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 228
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

1100. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 228
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1101. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 228
   Korea public data portal (data.go.kr) API MCP servers

1102. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 228
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1103. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 228
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1104. **[lokka](https://github.com/merill/lokka)** - ⭐ 228
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1105. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1106. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

1107. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 227
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

1108. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 227
   A Model Context Protocol (MCP) server for interacting with Twitter.

1109. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 227
   Appium MCP on Steroids!

1110. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 226
   MCP stdio server for frida

1111. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 226
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

1112. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 226
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1113. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 226
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1114. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 226
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1115. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 225
   Model Context Protocol server to run commands (tool: `runProcess`)

1116. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 225
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1117. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 225
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1118. **[flyto-core](https://github.com/flytohub/flyto-core)** - ⭐ 225
   The open-source execution engine for AI agents. 412 modules, MCP-native, triggers, queue, versioning, metering.

1119. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 224
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1120. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 224
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1121. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 223
   Penpot MCP server

1122. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 223
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1123. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 223
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1124. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

1125. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

1126. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

1127. **[overseer](https://github.com/dmmulroy/overseer)** - ⭐ 222
   CLI & Codemode MCP server for agent task management

1128. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 222
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1129. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 222
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1130. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

1131. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 221
   A SEC EDGAR MCP (Model Context Protocol) Server

1132. **[MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio)** - ⭐ 221
   MimikaStudio - A local-first application for macOS (Apple Silicon) + Agentic MCP Support

1133. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 220
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1134. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 220
   mindmap, mcp server, artifact

1135. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 220
   Lightweight agent orchestration dev tool that lives in your repo

1136. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 220
   Penpot's official MCP Server

1137. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

1138. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 219
   🧰 All-in-one domain name intelligence as a service

1139. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 219
   Model Context Protocol Servers for Milvus

1140. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 218
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1141. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 217

1142. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 217
   A tool for AI agents to discover and learn skills autonomously

1143. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 217
   Headless IDA Pro MCP Server

1144. **[tentix](https://github.com/labring/tentix)** - ⭐ 216
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

1145. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 216
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1146. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 216
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1147. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 216
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1148. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 215
   📜 An MCP server for conversation history search and retrieval in Claude Code

1149. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 215
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1150. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 215
   MCP server for TouchDesigner

1151. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1152. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 214
   Razorpay's Official MCP Server

1153. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 214
   Context layer for your product. Connect your agents and chat to 1st and 3rd party MCP servers!

1154. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 214
   MCP Server for ServiceNow

1155. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 214

1156. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 214
   MCP server for Coolify — 38 optimized tools for managing self-hosted PaaS through AI assistants

1157. **[airbroke](https://github.com/icoretech/airbroke)** - ⭐ 214
   🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher

1158. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1159. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 213
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1160. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 213
   pctx is the execution layer for agentic tool calls. It auto-converts agent tools and MCP servers into code that runs in secure sandboxes for token-efficient workflows.

1161. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 212
   Homeassistant MCP server for 小智AI

1162. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 212
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1163. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 212
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1164. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 211
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1165. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 211
   Run and monitor MCP servers locally

1166. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 211
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1167. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1168. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 210
   A Multi-modal MCP client for voice powered agentic workflows

1169. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1170. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 210
   An MCP server to use Sora video generation APIs

1171. **[genie](https://github.com/automagik-dev/genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1172. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 210
   🔎 A MCP server for Unsplash image search.

1173. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 210
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1174. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 210
   A list of MCP (Model Context Protocol) servers for developer tools and services

1175. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 210
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.) and AI agents (Claude Desktop, OpenClaw, etc.). Supports Serper, Tavily, and SearXNG.

1176. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 209

1177. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 209
   A ReAct-Based Highly Robust Autonomous Agent Framework.

1178. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1179. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 209
   Pure Rust implementation of MCP server for headless terminal 

1180. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 209
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

1181. **[octo-terminal-releases](https://github.com/johunsang/octo-terminal-releases)** - ⭐ 209
   Octo Terminal — The ultimate vibe coding terminal. AI-powered IDE with Claude, Codex, Ollama built-in. Terminal + editor + notes + browser in one app. Tauri + React + Rust.

1182. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 207
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

1183. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 207
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1184. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 207
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1185. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 207
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1186. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 207
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1187. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 207
   Agentify Desktop lets Codex/Claude/OpenCode  control your logged-in ChatGPT, Claude, AiStudio, Gemini, Grok, Perplexity web sessions via MCP, parallel hidden/visible tabs, file upload + image download

1188. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1189. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 206
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1190. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 206
   interactive programming of melodies, producing MIDI 

1191. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 206
   MCP server for Dynatrace Observability

1192. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 206
   Hugging Face MCP Server

1193. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1194. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1195. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 205
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1196. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1197. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 205
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1198. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 205
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1199. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 204
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1200. **[mcp-fusion](https://github.com/vinkius-labs/mcp-fusion)** - ⭐ 204
   MCP Fusion - The framework for AI-native MCP servers. 

1201. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 204
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1202. **[vurb.ts](https://github.com/vinkius-labs/vurb.ts)** - ⭐ 204
   Vurb.ts - The MVA framework for production MCP servers. Structured perception for AI agents. Zero hallucination. Zero data leaks.

1203. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 203
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1204. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 203
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1205. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 203
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1206. **[codemogger](https://github.com/glommer/codemogger)** - ⭐ 203
   Codemogger is a code indexing library and MCP server for AI coding agents

1207. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1208. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 202
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1209. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 201
   Self-hosted AI RAG + MCP Platform

1210. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1211. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 199
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1212. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 199
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1213. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 199
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

1214. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 199
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1215. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 199
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1216. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 198
   A MCP Server for the RAG Web Browser Actor

1217. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 198
   R MCP Server

1218. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 198
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1219. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 198
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1220. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 197
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1221. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 197
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1222. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 197
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1223. **[pipelock](https://github.com/luckyPipewrench/pipelock)** - ⭐ 197
   Firewall for AI agents. DLP scanning, SSRF protection, bidirectional MCP scanning, tool poisoning detection, and workspace integrity monitoring.

1224. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1225. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 196
   这是一个专为开发企业级MCP server而设计的通用开发框架

1226. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1227. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 196
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1228. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 196
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1229. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 196
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1230. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 196
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1231. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 196
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1232. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1233. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 195
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1234. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 195
   Tableau's official MCP Server. Helping Agents see and understand data.

1235. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 194
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1236. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 193
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1237. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 193
   Manage / Proxy / Secure your MCP Servers

1238. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 193
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1239. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 193
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1240. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 193
   Index the world's undocumented APIs

1241. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 192
   Absurdly easy Model Context Protocol Servers in Typescript

1242. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 192

1243. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 192
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1244. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 192
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1245. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 192
   Opensource Memory for Agents

1246. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 191
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1247. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1248. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 190
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1249. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 190
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1250. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 190
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1251. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 190
   MCP server implementation for the UniFi network application

1252. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 189
   Supabase MCP server created in Python.

1253. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 189
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1254. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 189
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1255. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 188
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1256. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 188
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1257. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 188
   Fast-track AI innovation with a centralized, trusted, curated registry

1258. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 188
   Neo4j official MCP Server

1259. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1260. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1261. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1262. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 187
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1263. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 187
   Sketchup Model Context Protocol

1264. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 187
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1265. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 187
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1266. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1267. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 186

1268. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 186
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1269. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 186
   Discord MCP Server for Claude Integration

1270. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1271. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 185
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1272. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 185
   IMAP and SMTP via MCP Server

1273. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 185
   Connect your AI to your APIs on Postman

1274. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1275. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 184
   Model Context Protocol Servers in Quarkus

1276. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 184
   Tools to allow LLM clients to interact with Linux systems remotely

1277. **[pasal](https://github.com/ilhamfp/pasal)** - ⭐ 184
   Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + web app giving Claude grounded access Indonesian laws.

1278. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 183
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1279. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 183
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1280. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 183
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1281. **[memorix](https://github.com/AVIDS2/memorix)** - ⭐ 183
   Cross-Agent Memory Bridge  Persistent memory for AI coding agents across 10 IDEs (Cursor, Windsurf, Claude Code, Codex, Copilot, Kiro, Antigravity, OpenCode, Trae, Gemini CLI) via MCP. Team collaboration, auto-cleanup, mini-skills, workspace sync. Never re-explain your project again.

1282. **[siconos](https://github.com/siconos/siconos)** - ⭐ 182
   Simulation framework for nonsmooth dynamical systems

1283. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1284. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1285. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 182
   This extension enables developers to implement the MCP server features easily.

1286. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 182
   MCP for calling Siri Shorcuts from LLMs

1287. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 182
   MCP Server for Wazuh SIEM

1288. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 182
   A Model Context Protocol (MCP) server providing access to Google Search Console

1289. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 181
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1290. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 181
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1291. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 181
   MCP Server for the Bilibili API, supporting various operations.

1292. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 181
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1293. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 180

1294. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 179
   Official MCP server for Tripo

1295. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1296. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1297. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 178
   An MCP server for Anki

1298. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 178
   A simple CLI to install MCP servers into any client - auth included!

1299. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 178
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1300. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 178
   Official Magic UI MCP server.

1301. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 178
   Token-efficient MCP adapter for Pi coding agent

1302. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 177
   A self-hosted web UI that simplifies AI experimentation and testing for Java developers. It provides playgrounds for all major vector databases and MCP tools, supports intuitive interaction with LLMs, and enables rapid development and testing of RAG workflows, MCP integrations, and unified chat experiences.

1303. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 177
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1304. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 176
   Examples of using Pipedream's MCP server in your app or AI agent.

1305. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 176
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1306. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 176
   Learn how to use MCP Servers with GitHub Copilot

1307. **[awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)** - ⭐ 176
   Curated list of AI agent templates for OpenClaw. Ready-to-use SOUL.md configs for productivity, development, marketing, and business agents. Deploy with CrewClaw.

1308. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 175
   拒绝FOMO！面对信息流，做个懒人，剩下的，交给AI！Reject FOMO! When facing the information stream, be lazy—leave the rest to AI!

1309. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 175
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1310. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 175
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1311. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 175
   Skill + MCP server to turn your agent into an RLM. Load context, iterate with search/code/think tools, converge on answers.

1312. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 174
   Turn any website or doc into an MCP server

1313. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1314. **[docs](https://github.com/strands-agents/docs)** - ⭐ 174
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1315. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 174
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1316. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 174
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1317. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 173
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1318. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 173
   AI-Driven Automated Red Team Orchestration Framework | AI驱动的自动化红队编排框架 | 101 MCP Tools | 2000+ Payloads | Full ATT&CK Coverage | MCTS Attack Planner | Knowledge Graph | Cross-platform

1319. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 173
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1320. **[command](https://github.com/scopecraft/command)** - ⭐ 172
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1321. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 172
   AI-first security scanner with 76 analyzers, 4,000+ detection rules, 508 FP filters (96.8% reduction), and 133 CVE detections for AI/ML, LLM agents, and MCP servers

1322. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 172
   A MCP server to search for accurate academic articles.

1323. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 172
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1324. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 172
   MCP server to work with Telegram through MTProto

1325. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 172
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1326. **[vibing-steampunk](https://github.com/oisee/vibing-steampunk)** - ⭐ 172
   vs-punk: ADT to MCP bridge - Vibe code in ABAP / AMDP

1327. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 171
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1328. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 171
   One MCP Server, All Your Apps, Privacy First

1329. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 171
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1330. **[Companion](https://github.com/mattt/Companion)** - ⭐ 171
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1331. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 171
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1332. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 171
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1333. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1334. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 170
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1335. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 170
   Turn a web server into an MCP server in one click without making any code changes.

1336. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 170
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1337. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 170
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1338. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 170
   Typescript SDK to build MCP servers in an agnostic way

1339. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 170
   MCP server for AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends, focus-free dispatch, undo/redo, P&ID symbols, and robust IPC with ESC prefix and UTF-8 fallback. Companion agent skill: puran-water/autocad-drafting

1340. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 170
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1341. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 169

1342. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 169
   A Tiny Web Chat App for AI Models with MCP Client Support

1343. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 169
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1344. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 169
   A light touch MCP task orchestration server for AI agents. Persistent work tracking and context storage across sessions and agents.  Defines planning floors through composable notes with optional gating transitions.   Coordinates multi-agent execution without prescribing how agents do their work.

1345. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 169
   An MCP server to search for flights.

1346. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 168
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1347. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 168
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1348. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 168
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1349. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 168
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1350. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 167
   MCP Server for Postgres

1351. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 167
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1352. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 167
   web GUI for securely managing local OpenCode configuration

1353. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 167
   MCPSDK.dev(ToolSDK.ai)'s Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1354. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 167
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1355. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 166
   A desktop application that adds powerful tools to Claude and AI platforms

1356. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 166
   Command line interface for MCP clients with secure execution and customizable security policies

1357. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 166
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1358. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 165
   c4 GenAI Suite

1359. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 165
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1360. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 165
   MCP Salesforce connector

1361. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 164
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1362. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 164
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1363. **[JoySafeter](https://github.com/jd-opensource/JoySafeter)** - ⭐ 164
   🚀 JoySafeter: An enterprise AI Agent Platform—Not just chatting. building、running、testing, and tracing autonomous Agent Teams with visual orchestration...

1364. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 163
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1365. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 163
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1366. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 163
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1367. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 163
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1368. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 163
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1369. **[n8n-claw](https://github.com/freddy-schuetz/n8n-claw)** - ⭐ 163
   OpenClaw-inspired autonomous AI agent built entirely in n8n. Adaptive RAG-powered memory, Skills via MCP templates, proactive task management, media understanding - self-hosted with one setup script

1370. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 162
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1371. **[recall](https://github.com/joseairosa/recall)** - ⭐ 162
   Persistent cross-session memory for Claude & AI agents. Self-host on Redis/Valkey, or use the managed SaaS at recallmcp.com.

1372. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 162
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1373. **[xiaoi](https://github.com/xvhuan/xiaoi)** - ⭐ 162
   小爱音箱语音通知工具：提供 CLI/TUI/MCP/Webhook 一键播报与控制音量，支持 PM2 常驻部署，支持docker部署。

1374. **[memov](https://github.com/memovai/memov)** - ⭐ 162
   Give git-like & traceable memory to OpenClaw and any coding agents. By https://memov.ai/ aka Entire CLI for every coding agents by MCP.

1375. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 162
   MCP Server for Searching Turkish Legislation

1376. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1377. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 160
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1378. **[PolyMCP](https://github.com/poly-mcp/PolyMCP)** - ⭐ 160
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1379. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 160
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1380. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 160
   MCP server for searching and querying PubMed medical papers/research database

1381. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 160
   Model Context Protocol For R

1382. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 160
   MCP stdio server for radare2

1383. **[MODULAR-RAG-MCP-SERVER](https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER)** - ⭐ 160
   A modular RAG (Retrieval-Augmented Generation) system with MCP Server architecture. Using Skill to make AI follow each step of the spec and complete the code 100% by AI.

1384. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 159
   Chat application with multi-agents system supports multi-models and MCP

1385. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1386. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 158
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1387. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 158
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1388. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 158
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1389. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 158
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1390. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 158
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1391. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 157
   An MCP server for fetching URLs / Youtube video transcript.

1392. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 157
   Simple Slackbot MCP Client

1393. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 157
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1394. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 157
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1395. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 157
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1396. **[Axon.MCP.Server](https://github.com/ali-kamali/Axon.MCP.Server)** - ⭐ 157
   Transform your codebase into an intelligent knowledge base for AI-powered development with Cursor IDE, Google AntiGravity, and MCP-enabled assistants

1397. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 156
   Scrapeless Mcp Server

1398. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 156
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1399. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 156
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1400. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 156
   Persistent Intelligence Infrastructure for AI Agents

1401. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 156
   MCP Server for AI Summarization

1402. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 155

1403. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 155
   MCP Server for Google Slides

1404. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 155
   DataForSEO API modelcontextprotocol server 

1405. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 155
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1406. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 155

1407. **[cachebro](https://github.com/glommer/cachebro)** - ⭐ 155
   File cache with diff tracking for AI coding agents. Drop-in MCP server that cuts token usage by 26%.

1408. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 155
   Local-first RAG server for developers using MCP. Semantic + keyword search for code and technical docs. Fully private, zero setup.

1409. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 155
   Supercharge AI Agents, Safely

1410. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 154
   Model Context Protocol (MCP) server for constraint optimization and solving"

1411. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 154
   A simple MCP server to search for documentation (tutorial)

1412. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 154
   Local-first MCP App framework for ChatGPT Apps, Claude, and more.

1413. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 154
   Official Railway MCP Server for interacting with your Railway account

1414. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 153
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1415. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 153
   ChatGPT Copilot Extension for Visual Studio Code

1416. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 153
   Make MCP Server

1417. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 153
   Deep Research for crypto - free & fully local

1418. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 153
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1419. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 153
   The Logfire MCP Server is here! :tada:

1420. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 153
   MCP Server that enables Claude code to interact with Gemini

1421. **[refref](https://github.com/refrefhq/refref)** - ⭐ 153
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1422. **[claude-code-open](https://github.com/kill136/claude-code-open)** - ⭐ 153
   Open source AI coding platform with Web IDE, multi-agent system, 37+ tools, MCP protocol. MIT licensed.

1423. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 153
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1424. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 153
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1425. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 153
   Codex Mcp Server 

1426. **[mcp-todoist](https://github.com/greirson/mcp-todoist)** - ⭐ 153
   MCP server that connects Claude to Todoist for natural language task and project   management with bulk operations

1427. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 152
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1428. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 152
   A Model Context Protocol server for MySQL database operations

1429. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 152
   Instagram Direct messages MCP

1430. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 152
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1431. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 152
   Vector-search powered agent memory MCP server

1432. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 152

1433. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 152
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1434. **[nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server)** - ⭐ 152

1435. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 151
   A gateway demo for MCP SSE Server

1436. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 151
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1437. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 151
   :octocat: GitHub Emoji for C#, dotnet and beyond

1438. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 151
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1439. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 150
   A simple and performant Model Context Protocol framework for Python.

1440. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1441. **[relay](https://github.com/prism-php/relay)** - ⭐ 150
   An MCP client tool for Prism

1442. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 150
   StarRocks MCP (Model Context Protocol) Server

1443. **[bocha-search-mcp](https://github.com/BochaAI/bocha-search-mcp)** - ⭐ 150
   Bocha Search MCP Server.

1444. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 150
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1445. **[Express-REST-API-and-MCP-Server-Framework](https://github.com/iolufemi/Express-REST-API-and-MCP-Server-Framework)** - ⭐ 149
   Express REST API and MCP Server Framework is a comprehensive development framework for building RESTful APIs and MCP servers with Express.js. It provides a complete template for creating production-ready APIs using Node.js, Express, Mongoose (MongoDB), and Sequelize (SQL databases).

1446. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 149
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1447. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 149
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1448. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1449. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 149
   MCP Server for using any LLM as a Tool

1450. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 149
   Desktop APP for Discover and Install MCP Servers

1451. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 149
   MCP server to download entire websites

1452. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 148
   Manage Your Kubernetes Cluster with k8s mcp-server

1453. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 148
   Dynamically expose tools from proxied servers based on an Agent Persona

1454. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 148
   MCP server for discord bot

1455. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 148
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1456. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 147
   Async Python client for the Model Context Protocol with interactive CLI and reactive Web UI, connecting AI models to MCP servers via stdio and SSE

1457. **[kom](https://github.com/weibaohui/kom)** - ⭐ 147
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1458. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 147
   Model Context Protocol server implementation for Figma API

1459. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 147
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1460. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 147
   Catch MCP server issues before your agents do.

1461. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 147
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1462. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 147
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1463. **[claude-emporium](https://github.com/Vvkmnn/claude-emporium)** - ⭐ 146
   🏛 [UNDER CONSTRUCTION] A (roman) claude plugin marketplace 

1464. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 146
   Toolkit for Coding Agents to work reliably with repo of any size.

1465. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 146
   A PubMed MCP server.

1466. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 146
   A Model Context Protocol server for calculating.

1467. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 146
   💻 Give AI models complete control of your computer (probably a bad idea)

1468. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 146
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1469. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 146
   MariaDB MCP (Model Context Protocol) server implementation

1470. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 145
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1471. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust 

1472. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 145
   Connect any Open Data to any LLM with Model Context Protocol.

1473. **[eion](https://github.com/eiondb/eion)** - ⭐ 145
   Shared Memory Storage for Multi-Agent Systems

1474. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 145
   An MCP server that provides access to Postman.

1475. **[deterministic-agent-control-protocol](https://github.com/elliot35/deterministic-agent-control-protocol)** - ⭐ 145
   Governance gateway for AI agents — bounded, auditable, session-aware control with MCP proxy, shell proxy & HTTP API. Works with Cursor, Claude Code, Codex, and any MCP-compatible agent.

1476. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 145
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1477. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

1478. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 144

1479. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 144
   A MCP Server for creating Powerpoint Presentations

1480. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 144
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1481. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 144
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1482. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 144
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1483. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 143
   MCP server implementation for Google's Gemini API

1484. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

1485. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 143
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1486. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 143
   An MCP Server for Ollama

1487. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 143
   Nextcloud MCP Server

1488. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 143
   A redmine MCP server covering close to 100% of redmines API

1489. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 143
   Model Context Protocol for x64dbg & x32dbg

1490. **[mcp-codex-dev](https://github.com/FYZAFH/mcp-codex-dev)** - ⭐ 143
   MCP Server for Codex CLI integration - stateful code writing and review workflows

1491. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 142
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1492. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1493. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 142
   MSSQL Server MCP implementation written in C#

1494. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 142
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1495. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 142
   Comprehensive MCP server exposing dozens of capabilities to AI agents: multi-provider LLM delegation, browser automation, document processing, vector ops, and cognitive memory systems

1496. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 142

1497. **[ClaudeR](https://github.com/IMNMV/ClaudeR)** - ⭐ 142
   Connect RStudio to Claude, Codex, Gemini, and other AI assistants via MCP. Multi-agent orchestration, async execution, and zero-config setup with uvx.

1498. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 142
   MCP server for Unreal Engine 5

1499. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1500. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1501. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 141
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1502. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 141
   Serper MCP Server supporting search and webpage scraping

1503. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 140
   Graphiti MCP Server

1504. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 140
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1505. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 140
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1506. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 140
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1507. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 140
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1508. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 140
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1509. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 140
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1510. **[claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager)** - ⭐ 140
   GUI app to manage MCP servers for Claude Code

1511. **[ai-skills](https://github.com/sanjay3290/ai-skills)** - ⭐ 140
   Collection of agent skills for AI coding assistants

1512. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 139
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1513. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 139
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1514. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 139
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1515. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 139
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

1516. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 139

1517. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 139
   MCP server for Israel Government Data

1518. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 139
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1519. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 139
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1520. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 139
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1521. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 139
   Operating System for your personal AI Agents with Security-first approach. Multi-channel (WhatsApp, Telegram, Discord, Slack, iMessage), multi-provider (Claude, GPT, Gemini, Ollama), fully self-hosted.

1522. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 138
   Simple MCP Server Implementation

1523. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 138
   MCP server for seamless document format conversion and processing

1524. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 138
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1525. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 138
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1526. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 138
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1527. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 138
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1528. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 137
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1529. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 137
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1530. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 137
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1531. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 136
   mcp server for gitingest

1532. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 136
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1533. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 136
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1534. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 136
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1535. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 136
   Model Context Protocol (MCP) server for the Zotero API, in Python

1536. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 136
   Model Context Protocol (MCP) with TikTok integration

1537. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 136
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1538. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 135
   AI-powered security operations for Wazuh SIEM—use any MCP-compatible client to ask security questions in plain English. Faster threat detection, incident triage, and compliance checks with real-time monitoring and anomaly spotting. Production-ready MCP server for conversational SOC workflows.

1539. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 135
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1540. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 135
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1541. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 135
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1542. **[forgemax](https://github.com/postrv/forgemax)** - ⭐ 135
   Code Mode inspired local sandboxed MCP Gateway - collapses N servers x M tools into 2 tools (~1,000 tokens)

1543. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 135
   Enable AI Agents to Control Unity

1544. **[openchrome](https://github.com/shaun0927/openchrome)** - ⭐ 135
   Open-source browser automation MCP server. Control your real Chrome from any AI agent.

1545. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1546. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 134
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1547. **[claude-in-mobile](https://github.com/AlexGladkov/claude-in-mobile)** - ⭐ 134
   MCP server for mobile and desktop automation — Android (via ADB), iOS Simulator (via simctl), and Desktop (Compose Multiplatform). Like Claude in Chrome but for mobile devices and desktop apps

1548. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1549. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1550. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 133
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1551. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 133
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1552. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 133
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1553. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 133
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1554. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 133
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1555. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 133
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1556. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 133
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1557. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 133
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1558. **[meta_skill](https://github.com/Dicklesworthstone/meta_skill)** - ⭐ 133
   Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic search, bandit-optimized suggestions, and MCP integration

1559. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 133
   MCP server that provides access to Chinese stock market data using akshare-one

1560. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 133
   Salesforce MCP Server

1561. **[binary-ninja-headless-mcp](https://github.com/mrphrazer/binary-ninja-headless-mcp)** - ⭐ 133
   Headless Binary Ninja MCP server — giving AI agents deep reverse-engineering capabilities via 180 tools.

1562. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 132
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1563. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 132
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1564. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 132
   Isaac Simulation MCP Extension and Server

1565. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 132
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1566. **[Dex](https://github.com/davekilleen/Dex)** - ⭐ 132
   Your AI Chief of Staff — a personal operating system starter kit that adapts to your role. No coding required.

1567. **[magg](https://github.com/sitbon/magg)** - ⭐ 131
   Magg: The MCP Aggregator

1568. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 131
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1569. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 130
   BrowserStack's Official MCP Server

1570. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 130
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1571. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 130
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1572. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 130
      Convert any MCP server into a Claude Skill with 90% context savings

1573. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 130
   High-performance CCXT MCP server for cryptocurrency exchange integration

1574. **[sap-skills](https://github.com/secondsky/sap-skills)** - ⭐ 130
   Production-ready Claude Code skills for SAP development - 35 skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more

1575. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 129
   Docker Hub MCP Server

1576. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 129
   A collection of crypto MCP servers.

1577. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 129
   It's time to push beyond MCP Servers... Right?

1578. **[mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** - ⭐ 129
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1579. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 129
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1580. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 129
   A modular MCP server that provides commonly used developer tools for AI coding agents

1581. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1582. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1583. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 128
   Intelligent spec workflow management MCP server

1584. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 128
   Raindrop MCP Server

1585. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 128
   A powerful MCP server for intelligently reading Java source code (For Jar and local project).

1586. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 128
   MCP server for interaction with Bitwarden.

1587. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 128
   MCP Server connecting to Perplexity Comet browser

1588. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 128

1589. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 128
   MCP server for interacting with the Aseprite API

1590. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 128
   MCP server for Mikrotik

1591. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 128
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1592. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1593. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 127
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1594. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 127
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1595. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 127
   MCP server for understanding AWS spend

1596. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 127
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

1597. **[turbo-flow](https://github.com/marcuspat/turbo-flow)** - ⭐ 127
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI subagents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1598. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 126
   Dart AI Model Context Protocol (MCP) server

1599. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1600. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 126

1601. **[sysplant](https://github.com/x42en/sysplant)** - ⭐ 126
   Your Windows syscall hooking factory - feat Canterlot's Gate - All accessible over MCP

1602. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 126
   a private MCP server for accessing Linear

1603. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 126
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1604. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 126
   Buttplug.io Model Context Protocol (MCP) Server

1605. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 126
   Conversion from Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines, and autonomous Excel reading and writing by AI agents through MCP integration.

1606. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 126
   Portainer MCP server

1607. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 126
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1608. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 126
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

1609. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1610. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 125
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1611. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 125
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1612. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 125
   Model Context Protocol Server for Swift

1613. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 125
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1614. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 125
   unofficial mcp server for cloudflare api

1615. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1616. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 124
   🐉 The fast, PHP way to build MCP servers

1617. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 124
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1618. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 124
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1619. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 124
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1620. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 124
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1621. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 123
   A Model Context Protocol server that provides access to BigQuery

1622. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 123
   wanna develop an app ❓

1623. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 123
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1624. **[openapi](https://github.com/samchon/openapi)** - ⭐ 123
   OpenAPI definitions, converters and LLM function calling schema composer.

1625. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 123
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1626. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 123
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1627. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 123
   A Model Context Protocol (MCP) for Jupyter Notebook

1628. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 123
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1629. **[mcp-gm](https://github.com/AnEntrypoint/mcp-gm)** - ⭐ 122
   wanna develop an app ❓

1630. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 122
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

1631. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 122
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1632. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 122
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

1633. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 122
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1634. **[env-doctor](https://github.com/mitulgarg/env-doctor)** - ⭐ 122
   Debug your GPU, CUDA, and AI stacks across local, Docker, and CI/CD (CLI and MCP server)

1635. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 122
   A Model Context Protocol Server to manipulate *.xcodeproj

1636. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 122
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1637. **[shodh-memory](https://github.com/varun29ankuS/shodh-memory)** - ⭐ 122
   Cognitive memory for AI agents — learns from use, forgets what's irrelevant, strengthens what matters. Single binary, fully offline.

1638. **[comfy-pilot](https://github.com/ConstantineB6/comfy-pilot)** - ⭐ 122
   MCP server + embedded terminal that lets Claude Code see and edit your ComfyUI workflows

1639. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 122
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1640. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1641. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 121
   MCP server implementation for n8n workflow automation

1642. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 121
   An MCP server that provides LLMs with the latest stable package versions when coding

1643. **[ASI](https://github.com/vNeeL-code/ASI)** - ⭐ 121
   Android ✧ Gemma Integration into Android System Intelligence

1644. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 121
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

1645. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 121
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1646. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

1647. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 120
   Google Sheets MCP Server 📊🤖

1648. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 120
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1649. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 120
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

1650. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 120
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1651. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 120
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1652. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 119
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1653. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 119

1654. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 119
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1655. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 119
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1656. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 119
   TypeScript template for building Model Context Protocol (MCP) servers. Ships with declarative tools/resources, pluggable auth, multi-backend storage, OpenTelemetry observability, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1657. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

1658. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 118
   MCP Server for PolyMarket API

1659. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 118
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1660. **[codefire-app](https://github.com/websitebutlers/codefire-app)** - ⭐ 118
   CodeFire gives AI coding tools persistent memory, task tracking, and project intelligence. A desktop companion for the AI-native workflow.

1661. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 117
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1662. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 117
   An MCP server for InterviewReady

1663. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 117
   A proxy to use HTTP/SSE MCPs from STDIO clients

1664. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 117
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1665. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 116
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1666. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 116
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1667. **[kodit](https://github.com/helixml/kodit)** - ⭐ 116
   👩‍💻 MCP server to index external repositories

1668. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 116
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

1669. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 116
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1670. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 116
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1671. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 116
   It's an MCP server... for Outline (the documentation platform!)

1672. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 115
   Fast and super efficient Minecraft Server written in C++

1673. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 115
   Azure API Management as AI Gateway to Remote MCP servers.

1674. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 115
   MCP Server for working with large Oracle databases

1675. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 115
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1676. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 115
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

1677. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 115
   Getting Started with Remote MCP Servers using Azure Functions (Python)

1678. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 115

1679. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 115
   MCP server for Google Tag Manager

1680. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 114
   Swagger to MCP server

1681. **[mcp](https://github.com/frappe/mcp)** - ⭐ 114
   Frappe MCP allows Frappe apps to function as MCP servers

1682. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1683. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 114
   Control WordPress using WP-CLI, AI, and MCP.

1684. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 114
   MCP server for Shodan — search internet-connected devices, IP reconnaissance, DNS lookups, and CVE/CPE vulnerability intelligence. Works with Claude Code, Codex, Gemini CLI, and Claude Desktop.

1685. **[mcp](https://github.com/taskade/mcp)** - ⭐ 114
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1686. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 114
   blazigly fast gRPC/MCP client & server implementation in zig

1687. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 114
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

1688. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 114
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1689. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 114
   MCP for 1C:EDT

1690. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 113
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1691. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1692. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

1693. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 113
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1694. **[orchestkit](https://github.com/yonatangross/orchestkit)** - ⭐ 113
   The Complete AI Development Toolkit for Claude Code — 79 skills, 30 agents, 105 hooks. Production-ready patterns for full-stack development.

1695. **[ironcurtain](https://github.com/provos/ironcurtain)** - ⭐ 113
   A secure* runtime for autonomous AI agents. Policy from plain-English constitutions. (*https://ironcurtain.dev)

1696. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1697. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 112
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1698. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 112
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1699. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 112
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1700. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 112
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1701. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 112
   MCP server for VirusTotal API — analyze URLs, files, IPs, and domains with comprehensive security reports, relationship analysis, and pagination support.

1702. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 111
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1703. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1704. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

1705. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1706. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1707. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 111
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1708. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

1709. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 111

1710. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 111
   Open Source MCP Servers for Scientific Research

1711. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 111
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

1712. **[AgenticGoKit](https://github.com/AgenticGoKit/AgenticGoKit)** - ⭐ 111
   Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent agents. LLM-agnostic, event-driven, with multi-agent workflows, MCP tool discovery, and production-grade observability.

1713. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 111
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1714. **[Aegis](https://github.com/Justin0504/Aegis)** - ⭐ 111
   Runtime policy enforcement for AI agents. Cryptographic audit trail, human-in-the-loop approvals, kill switch. Zero code changes.                                                                         

1715. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1716. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

1717. **[modex](https://github.com/theronic/modex)** - ⭐ 110
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1718. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 110
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via CLI wrappers

1719. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 110
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1720. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 110
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

1721. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 110

1722. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 110
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1723. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 110
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under GNU General Public License.

1724. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

1725. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1726. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 109
   MCP Client Implementation using Python, LangGraph and Gemini

1727. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 109
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1728. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 109
   The coding agent for professionals

1729. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 109
   MCP server for token-efficient large document analysis via the use of REPL state

1730. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 109
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

1731. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 109
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

1732. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 109
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

1733. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 109
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1734. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 109
   A Google Tasks Model Context Protocol Server for Claude

1735. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 109
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1736. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1737. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1738. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

1739. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 108
   An MCP client for Node.js.

1740. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 108
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1741. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 108
   Payload CMS MCP Server

1742. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

1743. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

1744. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 107
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1745. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 107
   MCP for semantic code search & navigation that reduces token waste

1746. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 107
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

1747. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 107
   fast, secure c# runner

1748. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 107
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

1749. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 107
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1750. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 107
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search, News Search and LLM Context Search capabilities

1751. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 106
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1752. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 106
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1753. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 106
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

1754. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

1755. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

1756. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

1757. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 105
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

1758. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 105
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1759. **[linggen-memory](https://github.com/linggen/linggen-memory)** - ⭐ 105
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1760. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 105
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1761. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 105
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref. 

1762. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 105
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1763. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 105
   Model Context Protocol (MCP) server for the Webflow Data API.

1764. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

1765. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1766. **[linggen](https://github.com/linggen/linggen)** - ⭐ 104
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1767. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 104
   An md file as a chat interface and editable history in one.

1768. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1769. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 104
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1770. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 104
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1771. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 104
   Official Vectorize MCP Server

1772. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 104
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1773. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1774. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1775. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

1776. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1777. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1778. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 103
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

1779. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 103
   AlibabaCloud CloudOps MCP Server

1780. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 103
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1781. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 103
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1782. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 103
   Wanaku MCP Router

1783. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 103
    QMT-MCP 模块化量化交易助手

1784. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1785. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1786. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 102
   go doc mcp server

1787. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 102
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1788. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 102
   MCP server for natural language interaction with Power BI datasets

1789. **[forge-orchestrator](https://github.com/nxtg-ai/forge-orchestrator)** - ⭐ 102
   Forge Orchestrator: Multi-AI task orchestration. File locking, knowledge capture, drift detection. Rust.

1790. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 102
   Quickly screenshots webpages and converts to an LLM friendly size

1791. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1792. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 102
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1793. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 102
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1794. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 101
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1795. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1796. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 101
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1797. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 101
    Official Go implementation of the UTCP 

1798. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 101
   Collection of examples of how to use Model Context Protocol with AWS.

1799. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 101
   Memory and context manager just works.

1800. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 101
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

1801. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 101
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1802. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1803. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1804. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1805. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1806. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1807. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 100
   Node.js Client Implementation for Model Context Protocol (MCP)

1808. **[mpm-vibe-coding](https://github.com/halflifezyf2680/mpm-vibe-coding)** - ⭐ 100
   MPM is an MCP context-engineering layer for Vibe Coding, focused on three delivery bottlenecks: context loss, uncontrolled changes, and non-verifiable outcomes.

1809. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 100
   LangGraph AI Repository

1810. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 100
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1811. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 100
   MCP server for persistent context management in AI coding assistants

1812. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1813. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1814. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1815. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1816. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 99
   lapras.com 公式MCP Server

1817. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 99
   Your AI Coding Assistant's Long-Term Memory

1818. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 99
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

1819. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 99
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1820. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 99
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1821. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 99
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1822. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 99
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1823. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 99
   MCP Server for use with Monarch Money

1824. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 99
   Model Context Protocol for Actual Budget API

1825. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 99
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1826. **[harnss](https://github.com/OpenSource03/harnss)** - ⭐ 99
   Open-source desktop client/UI build to harness the Claude Code, Codex and any other Agent. Run multiple AI coding agents side by side with rich tool visualization, MCP integrations, built-in terminal, git, browser and just about anything else you would need.

1827. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

1828. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 98
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1829. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 98
   MCP Server for AI automation of the PlayCanvas Editor

1830. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 98
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1831. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 98
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

1832. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

1833. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 98
   Context7 MCP Server for Zed

1834. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 98
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1835. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 97
   claude mcp sse demo with server and client(cli、web)

1836. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1837. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1838. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 97
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1839. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 97
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

1840. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 97
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

1841. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 97
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1842. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 97
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1843. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 96
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1844. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 96
   first gemini based desktop client for MCP

1845. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 96
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1846. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 96
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

1847. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 96
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

1848. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 96
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

1849. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 96
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

1850. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 96
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1851. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 96
   Portable , scalable , secure AI Agents

1852. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 96
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1853. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 95
   This is a Ruby implementation of MCP (Model Context Protocol) client

1854. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 95
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

1855. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 95
   MCP Server for Linux Scheduler Management and Auto optimization

1856. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 95
   Collection of resources to help AI agents build better with Sanity.

1857. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 95
   MCP Server for connecting to the Meta Marketing API

1858. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 95
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1859. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 94
   Sandbox for Agents 

1860. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 94
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

1861. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 94
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1862. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 94
   MCP server for *arr media management suite

1863. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 94
   A Model Context Protocol (MCP) server for square

1864. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 94
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1865. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 94
   Interact with all three types of generative UI, all in one interface

1866. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 94
   From Java Dev to AI Engineer: Spring AI Fast Track

1867. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1868. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

1869. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 93
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1870. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 93
   Model Context Protocol server for Replicate's API

1871. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

1872. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 93
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1873. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 93
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1874. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 93
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

1875. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 93
   Rails Engine with MCP compliant Spec.

1876. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 93
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1877. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 93
   Octopus Deploy Official MCP Server

1878. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 93
   MCPcat is an analytics platform for MCP server owners 🐱.

1879. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 93
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

1880. **[charlotte](https://github.com/TickTockBent/charlotte)** - ⭐ 93
   Token-efficient browser MCP server — structured web pages for AI agents, not raw accessibility dumps

1881. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

1882. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 92
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

1883. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 92
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1884. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 92
   A curated list of OSINT MCP servers. Pull requests are welcomed!

1885. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 92
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1886. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

1887. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

1888. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 91
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1889. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 91
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1890. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 91
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1891. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 91
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

1892. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 90
   A model-context-protocol server for molecules.

1893. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 90
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1894. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 89
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1895. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 89
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

1896. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 89
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1897. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 88
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1898. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

1899. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 88
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1900. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 88
   高德地图MCP Server，支持stdio, sse和streamable-http

1901. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 88
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

1902. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 88
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

1903. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 88
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

1904. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 88
   A Model Context Protocol server that provides knowledge graph management capabilities.

1905. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 87
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

1906. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

1907. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

1908. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

1909. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 87
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

1910. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 87
   Official Oxylabs MCP integration

1911. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 87
   Ragie Model Context Protocol Server

1912. **[identity](https://github.com/agntcy/identity)** - ⭐ 87
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1913. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 87
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

1914. **[sdl-mcp](https://github.com/GlitterKill/sdl-mcp)** - ⭐ 87
   SDL-MCP (Symbol Delta Ledger MCP Server) is a cards-first context system for coding agents that saves tokens and improves context.

1915. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

1916. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

1917. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

1918. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

1919. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 86
   CLI & API for MCP management

1920. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

1921. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 86
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1922. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 86
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1923. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 86
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1924. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 86
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1925. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 86
   MCP server for AI-assisted development of CAP applications

1926. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 86
   WeChat-MCP: let Claude/ChatGPT and other AI assistants read and reply to WeChat for you

1927. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 86
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

1928. **[NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform)** - ⭐ 86
   AI-powered network automation via Netbox and Model Context Protocol (MCP). 178 tools for multi-vendor infrastructure   management, self-healing agents, drift detection, and a real-time web dashboard.

1929. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1930. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

1931. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 85
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1932. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 85
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

1933. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 85
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

1934. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 85
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

1935. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 85
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1936. **[mcp-bridge](https://github.com/firekula/mcp-bridge)** - ⭐ 85
   这是一个为 Cocos Creator 设计的 MCP (Model Context Protocol) 桥接插件，用于连接外部 AI 工具与 Cocos Creator 编辑器，实现对场景、节点等资源的自动化操作。

1937. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

1938. **[spiceflow-framework](https://github.com/remorses/spiceflow-framework)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1939. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 84
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

1940. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 84
   a mcp server to manage github project's functionality 

1941. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 84
   The official MCP server for SurrealDB

1942. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 84
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1943. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 84
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1944. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 84
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

1945. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 84
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1946. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 84
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

1947. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

1948. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

1949. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

1950. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

1951. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 83
   A WooCommerce (MCP) Model Context Protocol server

1952. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 83
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

1953. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 83
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

1954. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 83
   The EMBL-EBI Ontology Lookup Service (OLS)

1955. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 83
   A GitHub MCP Server extension for Zed

1956. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 83
   A complete MCP server template that include vitamins (oauth authentication included)

1957. **[us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp)** - ⭐ 83
   MCP server + TypeScript SDK for 40+ U.S. government data APIs — 250+ tools. Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, and many more. Works with VS Code Copilot, Claude Desktop, Cursor.

1958. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 82
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1959. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

1960. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 82
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

1961. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 82
   Model Context Protocol (MCP) CLI server template for Rust

1962. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 82
   Model Context Protocol (MCP) Server for the Keboola Platform

1963. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 82
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1964. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 82
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1965. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 82
   MCP Server to previewing mermaid diagrams with live reload

1966. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 82
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1967. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 81
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1968. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1969. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1970. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

1971. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 81
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1972. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 81
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1973. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 81
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1974. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 81
   OpenAPI specification MCP server.

1975. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 81
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

1976. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 81
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1977. **[tradememory-protocol](https://github.com/mnemox-ai/tradememory-protocol)** - ⭐ 81
   MCP server for AI trading memory — outcome-weighted cognitive memory with 10 tools, 399 tests.

1978. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 80
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1979. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

1980. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 80
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

1981. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 80
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1982. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 80
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1983. **[ophis](https://github.com/njayp/ophis)** - ⭐ 80
   Transform any Cobra CLI into an MCP server

1984. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 80
   Build agentic-MCP servers by composing existing MCP tools.

1985. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 80
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

1986. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 80
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1987. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 80
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1988. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 80
   MCP server for AI image generation and editing with automatic prompt optimization and quality presets (fast/balanced/quality). Powered by Gemini (Nano Banana 2 & Pro).

1989. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

1990. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

1991. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

1992. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 79
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

1993. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 79
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

1994. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 79
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1995. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 79
   MCP server that can execute terminal commands

1996. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 79
   Model Context Protocol for YNAB (you need a budget)

1997. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 79
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1998. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 79
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

1999. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 79
   A MCP server for Django applications, inspired by Laravel Boost.

2000. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 79
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

2001. **[uxc](https://github.com/holon-run/uxc)** - ⭐ 79
   Universal API calling CLI for URL-first discovery and invocation across OpenAPI, gRPC, GraphQL, MCP, and JSON-RPC.

2002. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 78
   MCP Server for Bing Search API

2003. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 78
   MCP server for Slither static analysis of Solidity smart contracts

2004. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 78
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

2005. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 77
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

2006. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

2007. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

2008. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

2009. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

2010. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2011. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 77
    An MCP server that provides LLMs access to other LLMs

2012. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 77
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

2013. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 77
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

2014. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 77
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

2015. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 77
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

2016. **[agent-security-scanner-mcp](https://github.com/sinewaveai/agent-security-scanner-mcp)** - ⭐ 77
   Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

2017. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 76
   MCP server for Google Search integration using Gemini's built-in search capabilities

2018. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

2019. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 76
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

2020. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 76
   A Model Context Protocol server for Hopper Disassembler

2021. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 76
   A Model Context Protocol Server to perform Kafka client operations

2022. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 76
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

2023. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 76
   MCP web search using perplexity without any API KEYS 

2024. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 76
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

2025. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 76
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

2026. **[apitap](https://github.com/n1byn1kt/apitap)** - ⭐ 76
   The MCP server that turns any website into an API — no docs, no SDK, no browser. npm: @apitap/core

2027. **[elementor-mcp](https://github.com/msrbuilds/elementor-mcp)** - ⭐ 76
   Comprehensive Elementor MCP Server plugin with 90+ Tools.

2028. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 76
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

2029. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

2030. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 75
   MCP to explore websites with llms.txt files

2031. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 75
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

2032. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 75
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

2033. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 75
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

2034. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 75
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

2035. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 75
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

2036. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 75
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

2037. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 75
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

2038. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 75
   Interactive Brokers MCP Server

2039. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 74
   The Privacy Firewall for LLMs

2040. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 74
   A task management system designed for AI development

2041. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 74
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

2042. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 74
   Index of all Model Context Protocol (MCP) clients and their capabilities

2043. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 74
   Model Context Protocol implementation for retrieving codebases using RepoMix

2044. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 74
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

2045. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 74
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2046. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 74
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

2047. **[Pare](https://github.com/Dave-London/Pare)** - ⭐ 74
   Dev tools, optimized for agents. Structured, token-efficient MCP servers for git, test runners, npm, Docker, and more.

2048. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 73
   An extension of MCP for SillyTavern.

2049. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

2050. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 73
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

2051. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 73
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

2052. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 73
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

2053. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 73
   Open Models MCP for Blender Using Ollama

2054. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 73
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

2055. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 73
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

2056. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 73
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

2057. **[yuque-mcp-server](https://github.com/yuque/yuque-mcp-server)** - ⭐ 73
   Yuque MCP Server - Model Context Protocol server for Yuque API

2058. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 72
   An experimental GitHub MCP server with local database.

2059. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 72
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

2060. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 72
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

2061. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 72
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

2062. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 72
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

2063. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 72
   A full featured, enterprise grade rust MCP SDK

2064. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 72
   MCP server for the Joplin note taking app

2065. **[mengram](https://github.com/alibaizhanov/mengram)** - ⭐ 72
   Human-like memory for AI agents — semantic, episodic & procedural. Experience-driven procedures that learn from failures. Free API, Python & JS SDKs, LangChain & CrewAI integrations.

2066. **[tradingview-chart-mcp](https://github.com/ertugrul59/tradingview-chart-mcp)** - ⭐ 72
   MCP server that captures TradingView chart images via Selenium — supports any ticker/interval with browser pooling for concurrent performance

2067. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 71
   MCP server to fetch YouTube transcripts

2068. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

2069. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server 

2070. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 71
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

2071. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 71
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

2072. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 71
   AniList MCP server for accessing anime and manga data

2073. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 71
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

2074. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 71
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

2075. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 71
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2076. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 71
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

2077. **[trading-mcp](https://github.com/netanelavr/trading-mcp)** - ⭐ 70
   The MCP server that will help you trade smarter (or at least try)

2078. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 70
   An unofficial and community-built MCP server for integrating with https://railway.app

2079. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 70
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

2080. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 70
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

2081. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 70
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

2082. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 70
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

2083. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 70
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2084. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 70
   McDonald's China MCP Server Integration Guide

2085. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2086. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 69

2087. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 69
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

2088. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 69
   MCP client for local ollama models

2089. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 69
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

2090. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 69
   Build MCP servers with WebAssembly components

2091. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 69
   Python code execution sandbox with programmatic MCP tool calling (PTC)

2092. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 69
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

2093. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 69
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

2094. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 69
   Model Context Protocol (MCP) server for Gmail

2095. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 69
   A simple MCP server for the SO-ARM100 control

2096. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 69
   A Model Context Protocol server for Zendesk

2097. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 69
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2098. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 69
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2099. **[QuickDesk](https://github.com/barry-ran/QuickDesk)** - ⭐ 69
   QuickDesk is the first AI-native remote desktop — an open-source, free application with a built-in MCP (Model Context Protocol) Server that lets any AI agent see and control remote computers.

2100. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 68
   Convert LangChain tools to FastMCP tools

2101. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 68
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

2102. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

2103. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

2104. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 68
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

2105. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 68
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

2106. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 68
   MCP Deep Research Server using Gemini creating a Research AI Agent

2107. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 68
   Python 实现 MCP client / service

2108. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 68
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

2109. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 68
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

2110. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 68
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

2111. **[vesta-mac-dist](https://github.com/scouzi1966/vesta-mac-dist)** - ⭐ 68
   Vesta macOS Distribution - Official releases and downloads.Vesta AI Chat Assistant for macOS - Built with SwiftUI, Swift MLX  and Apple Intelligence using Apple's on device model on MacOs Tahoe (MacOS 26). Now with side-by-side Qwen3-VL for vison

2112. **[hyperterse](https://github.com/hyperterse/hyperterse)** - ⭐ 68
   The MCP framework. Connect your data to your agents.

2113. **[regenerator2000](https://github.com/ricardoquesada/regenerator2000)** - ⭐ 68
   An interactive disassembler for the CPU 6502, focused mostly on Commodore 8-bit computers. Features a TUI with modern features like x-ref, undo/redo, arrows, keyboard-driven, mcp server, VICE debugger and more!

2114. **[nothumanallowed](https://github.com/adoslabsproject-gif/nothumanallowed)** - ⭐ 68
   Epistemic dataset generation engine. 38 AI agents deliberate through multi-round Geth Consensus — producing auditable reasoning traces for AI training. Parliament System, Knowledge Grounding, zero-trust security.

2115. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 68
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2116. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 68
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

2117. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 68
   Excel MCP Server & CLI - 23 tools, 214 operations for AI-powered Excel automation via COM API

2118. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 67
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

2119. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

2120. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

2121. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 67
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

2122. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

2123. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 67
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

2124. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 67
   MCP server that provides tools and resources to control and monitor robots using Nav2.

2125. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 67
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

2126. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 67
   A MCP server for interacting with Bear note-taking software.

2127. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 67
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

2128. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 67
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

2129. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 67
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

2130. **[mcp-dock](https://github.com/OldJii/mcp-dock)** - ⭐ 67
   A cross-platform MCP Server manager for Cursor, Claude, Windsurf, Zed & TRAE. Features one-click installation, multi-client sync, and a curated registry of Official & Smithery servers.

2131. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 66
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

2132. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 66
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

2133. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 66
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

2134. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 66
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

2135. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 66
   [MCP Server] The Security Agent for AI assisted coding

2136. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 66
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

2137. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 66
   Amazon MCP server to search & buy products using the L402

2138. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 66
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

2139. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 66
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

2140. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 66
   Model Context Protocol(MCP) 中文教程讲解

2141. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 66
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2142. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 66
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

2143. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 66
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2144. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 66
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2145. **[agenticmail](https://github.com/agenticmail/agenticmail)** - ⭐ 66
   Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically

2146. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 66
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2147. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 66
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

2148. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 65
   Compiler-driven MCP framework for Kotlin Multiplatform

2149. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 65
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

2150. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 65
   Open-source FRED MCP Server (Federal Reserve Economic Data)

2151. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 65
   A Model Context Protocol implementation for FHIR

2152. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 65
   FHIR MCP Server for handling medical data standard.

2153. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 65
   Academia MCP server: Tools for automatic scientific research

2154. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 65
   A Model Context Protocol (MCP) server for Microsoft Clarity

2155. **[hulunote](https://github.com/hulunote/hulunote)** - ⭐ 65
   An open-source outliner note-taking application with bidirectional linking.

2156. **[aivectormemory](https://github.com/Edlineas/aivectormemory)** - ⭐ 65
   aivectormemory 是一款基于 Model Context Protocol (MCP) 开发的OpenClaw、OpenCode、ClaudeCodeAI记忆管理工具。它专门为 Claude、OpenCode、Cursor 和 主流IDE 编程工具设计，通过向量数据库技术解决 AI 在不同对话会话中「健忘」的问题。aivectormemory: A lightweight MCP Server enabling persistent, cross-session memory for AI-powered IDEs via vector search.

2157. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

2158. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

2159. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

2160. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 64
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

2161. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 64
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2162. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 64
   可视化的配置和管理，给xiaozhi接入mcp

2163. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 64
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2164. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 64
   MCP server for the NCBI E-utilities API. Search PubMed, fetch article metadata, generate citations, explore MeSH terms, and discover related research. Runs over stdio or HTTP. Deployable to Cloudflare Workers.

2165. **[ClaudeHistoryMCP](https://github.com/jhammant/ClaudeHistoryMCP)** - ⭐ 64
   MCP server for searching and surfacing Claude Code conversation history

2166. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 64
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2167. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 64
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2168. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 64
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2169. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 63
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

2170. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

2171. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 63
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

2172. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 63
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

2173. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 63
   [Community Supported] Perforce P4 MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2174. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 63
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2175. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 62
   Miro integration for Model Context Protocol

2176. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 62
   Cryptocurrency Market Data MCP Server

2177. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

2178. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 62
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

2179. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 62
   Advanced MCP server for seamless access to Israeli Government Open Data

2180. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 62
   Model Context Protocol server and client for R

2181. **[fli](https://github.com/punitarani/fli)** - ⭐ 62
   Google Flights MCP and Python Library

2182. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 62
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2183. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 62
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

2184. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 62
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

2185. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 62
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2186. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

2187. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

2188. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 61
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

2189. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services. 

2190. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 61
   A Model Context Protocol (MCP) server for Rember.

2191. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 61
   nocodb mcp server

2192. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 61
   A Clojure SDK to create MCP servers (and eventually clients)

2193. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 61
   Zero-dependency MCP server implementation.

2194. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2195. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 61
   A curated list of awesome Model Context Protocol (MCP) servers.

2196. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 61
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2197. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 61
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2198. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

2199. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

2200. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 60
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2201. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 60
   Universal MCP Server Configuration Manager

2202. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 60
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

2203. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 60
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2204. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 60
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2205. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 60
   Adds MCP server to Blockbench

2206. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 60
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

2207. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 60
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2208. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 60
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2209. **[Skills-ContextManager](https://github.com/One-Man-Company/Skills-ContextManager)** - ⭐ 60
   A self-hosted web application for managing AI skills, workflows, and contexts with full MCP (Model Context Protocol) integration. Organize, manage, and dynamically load specialized knowledge bases into any AI Agent just by toggling your Skills On/Off in simple local hosted WEB UI.

2210. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 60
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2211. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 60
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2212. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 60
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2213. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 60
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2214. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 59
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

2215. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 59
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

2216. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

2217. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

2218. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

2219. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 59
   MCP Server to expose the GDB debugging capabilities

2220. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 59
   ABAP MCP - Model Context Protocol - Server SDK

2221. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 59
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2222. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 59
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2223. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 59
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2224. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 59
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

2225. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 59
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2226. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 59
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2227. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 59
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2228. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 59
   MCP router and Web Based MCP client

2229. **[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)** - ⭐ 59
   Curated awesome list for OpenClaw (formerly Moltbot/Clawdbot): skills, plugins, memory systems, MCP tools, deployment stacks, ecosystem platforms, and developer tooling.

2230. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 58
   Model Context Protocol server for Daipendency

2231. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 58
   A Model Context Protocol server for Ashra

2232. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 58
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2233. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2234. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2235. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 58
   ScapeGraph MCP Server

2236. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 58
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2237. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 58
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2238. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 58
   A Model Context Protocol server for Go developers

2239. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 58
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2240. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 58
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2241. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 58
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2242. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 58
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2243. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 58
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2244. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 57
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2245. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2246. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2247. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 57
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2248. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 57
   A model context protocol  (MCP) server for Umbraco 

2249. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 57
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2250. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 57
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2251. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 57
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2252. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 57
   Unblock, scrape, and search tools for MCP clients

2253. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 57
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2254. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 57
   Attio Model Context Protocol (MCP) server implementation

2255. **[flutter-skill](https://github.com/ai-dashboad/flutter-skill)** - ⭐ 57
   AI-powered E2E testing for 10 platforms. 253 MCP tools. Zero config. Works with Claude, Cursor, Windsurf, Copilot. Test Flutter, React Native, iOS, Android, Web, Electron, Tauri, KMP, .NET MAUI — all from natural language.

2256. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 57
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2257. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 57
   MCP server for the ClinicalTrials.gov v2 API. Allow LLMs to search trials, retrieve study details, compare studies, analyze trends, and match patients to eligible trials.

2258. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, Slides and Calendar. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

2259. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 56
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2260. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2261. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

2262. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2263. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

2264. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2265. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 56
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2266. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 56
   Generate an MCP for any web app

2267. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 56
   Write notes to Flomo

2268. **[MegaMemory](https://github.com/0xK3vin/MegaMemory)** - ⭐ 56
   Persistent project knowledge graph for coding agents. MCP server with semantic search, in-process embeddings, and web explorer.

2269. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 56
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2270. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 56
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2271. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 56
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2272. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 56
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2273. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 56
   OCaml implementation of the Model Context Protocol (MCP)

2274. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 56
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2275. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 56
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2276. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 56
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2277. **[gdal-mcp](https://github.com/JordanGunn/gdal-mcp)** - ⭐ 56
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2278. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 56
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

2279. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 55
   MCP server to support Astro project development

2280. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 55
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2281. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 55
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2282. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 55
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2283. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 55
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2284. **[python](https://github.com/mcp-auth/python)** - ⭐ 55
   🔐 Plug-and-play auth for Python MCP servers.

2285. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 55
   Multiplatform system monitoring tool using Cosmopolitan Libc

2286. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 55
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2287. **[AfdianToMarkdown](https://github.com/PhiFever/AfdianToMarkdown)** - ⭐ 55
   爱发电爬虫(afdian.com)

2288. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 55
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2289. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 55
   MCP Server for IBKR Client

2290. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 55
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2291. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 55
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2292. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 55
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2293. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2294. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2295. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2296. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 54
   Model Context Protocol Servers for Azure AI Search

2297. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 54
   MCP Memory Server with DuckDB backend

2298. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 54
   A MCP server for symbolic manipulation of mathematical expressions

2299. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 54
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2300. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 54
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2301. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 54
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2302. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 54
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2303. **[client](https://github.com/php-mcp/client)** - ⭐ 54
   Core PHP implementation for the Model Context Protocol (MCP) Client

2304. **[cortex-scout](https://github.com/cortex-works/cortex-scout)** - ⭐ 54
   An advanced web extraction and meta-search engine for AI agents. It features native parallel searching, Human-in-the-Loop (HITL) authentication fallback, and LLM-optimized data synthesis for deep web research.

2305. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 54
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2306. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 54
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2307. **[mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs)** - ⭐ 54
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2308. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 53
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2309. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 53
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2310. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2311. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

2312. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 53
   Unofficial Golang SDK for Anthropic Model Context Protocol

2313. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2314. **[Multi-Agent-System-A2A-ADK-MCP](https://github.com/RubensZimbres/Multi-Agent-System-A2A-ADK-MCP)** - ⭐ 53
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2315. **[skrills](https://github.com/athola/skrills)** - ⭐ 53
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2316. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 53
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2317. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 53
   🍰 Sugar - The autonomous layer for AI coding agents

2318. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 53
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2319. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 53
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2320. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 53
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2321. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 53
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2322. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 53
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2323. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 53
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2324. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 53
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2325. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2326. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

2327. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2328. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2329. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 52
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2330. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 52
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2331. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 52
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2332. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2333. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 52
   Claude  et al. play the brilliant puzzle title "Baba is You"

2334. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 52
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

2335. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 52
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2336. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 52
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

2337. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 52
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2338. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 52
   Inkdrop Model Context Protocol Server

2339. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 52
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

2340. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 52
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2341. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 52
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2342. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 52
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2343. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 52
   Headless IDA Pro binary analysis via Model Context Protocol

2344. **[winremote-mcp](https://github.com/dddabtc/winremote-mcp)** - ⭐ 52
   Windows Remote MCP Server — 40+ tools for desktop automation, process management, file operations via FastMCP

2345. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 51
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

2346. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 51
   Quantum-proof MCP Server and Client Interactions

2347. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

2348. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 51
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2349. **[gdal-mcp](https://github.com/Wayfinder-Foundry/gdal-mcp)** - ⭐ 51
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2350. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 51
   MCP Server for whois lookups.

2351. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 51
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

2352. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 51
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2353. **[ShadowCrawl](https://github.com/DevsHero/ShadowCrawl)** - ⭐ 51
   🥷 The FREE, Sovereign alternative to Firecrawl & Tavily. Pure Rust Stealth Scraper + Built-in God-Tier Meta-Search for AI Agents. Bypass Cloudflare & DataDome via HITL. Zero-bloat, ultra-clean LLM data. 99.99% Success Rate. 🦀

2354. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 51
   Official Rust implementation of the UTCP

2355. **[hmr](https://github.com/promplate/hmr)** - ⭐ 51
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

2356. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 51
   MCP Guard secures your MCP client from prompt injection attacks and more.

2357. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 51
   Matlab MCP Server in python

2358. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 51
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

2359. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 51
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2360. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 51
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2361. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 51
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2362. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 51
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2363. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 51
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2364. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 51
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2365. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

2366. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

2367. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

2368. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

2369. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

2370. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 50
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2371. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 50
   An implementation of the Model Context Protocol in Ruby.

2372. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 50
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2373. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 50
   Model Context Protocol server for ActivityWatch time tracking data

2374. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 50
   GIMP MCP server

2375. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 50
   vMCP - Virtual Model Context Protocol

2376. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

2377. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 50
   MCP Server for Text to Speech

2378. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 50
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2379. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 50
   Amadeus MCP(Model Context Protocol) Server

2380. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 50
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2381. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2382. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 50
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2383. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2384. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 50
   A powerful Model Context Protocol server for LinkedIn API integration

2385. **[civyk-winwright](https://github.com/civyk-official/civyk-winwright)** - ⭐ 50
   Playwright-style MCP server for Windows desktop, system, and browser automation. 59 tools for WPF, WinForms, Win32, Chrome/Edge via Model Context Protocol.

2386. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 49
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2387. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 49
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

2388. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

2389. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

2390. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 49
   Anthropic’s Model Context Protocol implementation for Oat++

2391. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

2392. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 49
   A Model-Context-Protocol (MCP) Server for Active Directory

2393. **[agent-os](https://github.com/imran-siddique/agent-os)** - ⭐ 49
   A Safety-First Kernel for Autonomous AI Agents - POSIX-inspired primitives with 0% policy violation guarantee

2394. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 49
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

2395. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 49
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

2396. **[mcp](https://github.com/goplus/mcp)** - ⭐ 49
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

2397. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 49
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2398. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 49
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

2399. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 49
   Send system notification when Agent task is done.

2400. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2401. **[mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events)** - ⭐ 49
   MCP server providing native macOS integration with Apple Reminders and Calendar via EventKit

2402. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2403. **[aguara](https://github.com/garagon/aguara)** - ⭐ 49
   Security scanner for AI agent skills & MCP servers. 173 detection rules. 13 categories. 5 registries monitored daily. OpenClaw detection included. No API keys, no cloud, no LLM. One binary. Detection engine behind Oktsec.

2404. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

2405. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

2406. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

2407. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

2408. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

2409. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 48
   Official MCP Server for Buildkite.

2410. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 48
   A comprehensive MCP server for Metabase with 70+ tools.

2411. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 48
   Remote MCP server that gives LLMs access to run network commands

2412. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 48
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

2413. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2414. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 48
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

2415. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 48
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

2416. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 48
   Go SDK for interacting with the MCP Toolbox for Databases.

2417. **[mcp](https://github.com/40ants/mcp)** - ⭐ 48
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2418. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 48
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

2419. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 48
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2420. **[gno](https://github.com/gmickel/gno)** - ⭐ 48
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2421. **[fossil-mcp](https://github.com/yfedoseev/fossil-mcp)** - ⭐ 48
   The code quality toolkit for the agentic AI era. Find dead code, clones, and scaffolding across 15 languages. MCP server + CLI.

2422. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

2423. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

2424. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

2425. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

2426. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 47
   Model Context Protocol to fetch youtube transcript

2427. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 47
   Sample MCP Server and MCP client with Aspire

2428. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 47
   Grant the AI octopus access to a portion of your desktop

2429. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 47
   Dremio MCP server

2430. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 47
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

2431. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 47
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

2432. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 47
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

2433. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 47
   OpenAPI Schema Model Context Protocol Server

2434. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 47
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

2435. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 47
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2436. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 47
   Enhanced Zen MCP Server with 'zen' default tool and improvements

2437. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

2438. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

2439. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 47
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2440. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 47
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

2441. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 47
   Deep Research & Competitor Analysis MCP for Claude & Cursor. No API Keys. Features: Web Search, Social Media (Reddit/HN), Trends & OCR.

2442. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 47
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2443. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 47
   Thoughtbox is a Git-inspired workspace for Agent Teams.

2444. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 47
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2445. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 47
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

2446. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 47
   Altium Model Context Protocol server and Altium API script

2447. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 47
   Implementation of Model Context Protocol server for Mailgun APIs

2448. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 47
   Model Context Protocol server for OpenStreetMap data

2449. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2450. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 47
   共学《MCP极简开发》项目代码

2451. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 47
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2452. **[mcpshim](https://github.com/mcpshim/mcpshim)** - ⭐ 47
   Turn remote MCP servers into local command workflows.

2453. **[tokio-prompt-orchestrator](https://github.com/Mattbusel/tokio-prompt-orchestrator)** - ⭐ 47
   Multi-core, Tokio-native orchestration for LLM pipelines.

2454. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 46
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2455. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

2456. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2457. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

2458. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

2459. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 46
   Model Context Protocol server for Flight Tracking

2460. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 46
   MCPcat is an analytics platform for MCP server owners 🐱.

2461. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 46
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2462. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 46
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

2463. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 46
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

2464. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 46
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

2465. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 46
   MCP client for Discourse sites

2466. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 46
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2467. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 46
   MCP (Model Context Protocol) server for the Contentful Management API

2468. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 46
   Un-official Serper Google search server for Cline and other MCP clients

2469. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 46
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

2470. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

2471. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 45
   An opinionated starter template for making Model Context Protocol (MCP) servers

2472. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

2473. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

2474. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

2475. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 45
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

2476. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

2477. **[js](https://github.com/mcp-auth/js)** - ⭐ 45
   🔐 Plug-and-play auth for Node.js MCP servers.

2478. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

2479. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 45
   An implementation of the Model Context Protocol for the World Bank open data API

2480. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 45
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

2481. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 45
   Create the prompts you need to write your Novel using AI

2482. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 45
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2483. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 45
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

2484. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 45
   MCP server for golang projects development: Expand AI Code Agent ability boundary to have a semantic understanding and determinisic information for golang projects.

2485. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 45
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2486. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 45
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2487. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

2488. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 45
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2489. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 45
   IMAP Model Context Protocol server for interactive email processing

2490. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 45
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

2491. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 45
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2492. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 45
   mcp server to run scripts on adobe illustrator

2493. **[Gopeak-godot-mcp](https://github.com/HaD0Yun/Gopeak-godot-mcp)** - ⭐ 45
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

2494. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 44
   Moondream MCP Server in Python

2495. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

2496. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

2497. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 44
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

2498. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 44
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2499. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

2500. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

2501. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 44
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

2502. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 44
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

2503. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 44
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

2504. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

2505. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 44
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

2506. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 44
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

2507. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 44
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

2508. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 44
   An MCP server to allow you to debug webpages using LLMs

2509. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 44
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

2510. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 44
   A production-ready Model Context Protocol (MCP) server for semantic memory management

2511. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 44
   Yandex Tracker MCP Server with OAuth2 support

2512. **[adal-cli](https://github.com/SylphAI-Inc/adal-cli)** - ⭐ 44
   The self-evolving coding agent that learns from your entire team and codebase. Less syncing. Less waiting. Deliver at the speed of thought.

2513. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 44
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2514. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

2515. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 44
   Model Context Protocol Platform，统一管理你的MCP服务

2516. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 44
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

2517. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 44
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

2518. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2519. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 44
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2520. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

2521. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 44
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2522. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 44
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2523. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

2524. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 43
   Generic MCP Client to use any MCP tool in a chat

2525. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 43
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

2526. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

2527. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

2528. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

2529. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 43
   GraphQL Schema Model Context Protocol Server

2530. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

2531. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

2532. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 43
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

2533. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 43
   Model Context Protocol server for Salesforce REST API integration

2534. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

2535. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

2536. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 43
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

2537. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 43
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

2538. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 43
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

2539. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 43
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

2540. **[lastsaas](https://github.com/jonradoff/lastsaas)** - ⭐ 43
   SaaS boilerplate/starter-kit in Go+React with Stripe integration, multi-tenant support, comprehensive features and AI-agent ready

2541. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 43
   A curated list of excellent Model Context Protocol (MCP) servers.

2542. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 43
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

2543. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2544. **[bonnard-cli](https://github.com/bonnard-data/bonnard-cli)** - ⭐ 43
   Open-source agentic schema CLI. Optimised for claude code, gemini, codex and co-pilot. Skills included.

2545. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2546. **[sharedcontext](https://github.com/Eversmile12/sharedcontext)** - ⭐ 43
   MCP server that gives AI coding assistants persistent cross-client memory. Facts and conversations stored in SQLite, encrypted with AES-256-GCM, synced to Arweave. No server, no account, recoverable with a 12-word phrase.

2547. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 43
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2548. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 43
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2549. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 43
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2550. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2551. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

2552. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

2553. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

2554. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

2555. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

2556. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 42
   Model Context Protocol (MCP) implementation for iOS simulators

2557. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 42
   WhatsApp Unofficial MCP Server

2558. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 42
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

2559. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 42
   台灣證交所OpenAPI 的 MCP Server

2560. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

2561. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 42
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

2562. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 42
   Bluesky MCP (Model Context Protocol) Server

2563. **[SageFs](https://github.com/WillEhrendreich/SageFs)** - ⭐ 42
   Sage Mode for F# development — REPL with solution or project loading, Live Testing for FREE, Hot Reload, and session management.

2564. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 42
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2565. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2566. **[1c-mcp](https://github.com/Untru/1c-mcp)** - ⭐ 42
   Curated list of MCP servers for 1C:Enterprise ecosystem | Каталог MCP-серверов для экосистемы 1С:Предприятие

2567. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   MCP server that exposes YepCode processes as callable tools for AI platforms. Securely connect AI assistants to your YepCode workflows, APIs, and automations.

2568. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

2569. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 41
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

2570. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

2571. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

2572. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

2573. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

2574. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 41
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

2575. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

2576. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 41
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

2577. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 41
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

2578. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 41
   MCP server for Obsidian (TypeScript + Bun)

2579. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 41
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

2580. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 41
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

2581. **[processhacker-mcp](https://github.com/illegal-instruction-co/processhacker-mcp)** - ⭐ 41
   your ai debugger, vibe hacking tool

2582. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 41
   Model Context Protocol (MCP) server for LinkedIn API integration

2583. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 41
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2584. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 41
   A Model Context Protocol server that provides access to Shodan API functionality

2585. **[claude-additional-models-mcp](https://github.com/Arkya-AI/claude-additional-models-mcp)** - ⭐ 41
   Reduce Claude Desktop consumption by 10x - Integrate Google's Gemini or Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

2586. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 41
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2587. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 41
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2588. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 41
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2589. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 40
   a mcp server for polymarket

2590. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 40
   A generic, modular server for implementing the Model Context Protocol (MCP). 

2591. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

2592. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

2593. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

2594. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 40
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

2595. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

2596. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

2597. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 40
   Algorand Local Model Context Protocol (Server & Client)

2598. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 40
   Write detections, investigate alerts, and query logs from your favorite AI agents

2599. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 40
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

2600. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 40
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

2601. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 40
   PDF RAG server for cursor.

2602. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 40
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

2603. **[bonnard-cli](https://github.com/meal-inc/bonnard-cli)** - ⭐ 40
   Agent-native analytics. MCP server, dashboards, SDK, and semantic layer CLI.

2604. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 40
   Apple Books MCP Server

2605. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 40
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2606. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 40
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2607. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 40
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2608. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 40
   It shows how to use model-context-protocol. 

2609. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 40
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

2610. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 40
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

2611. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 40
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2612. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 40
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2613. **[unreal-api-mcp](https://github.com/Codeturion/unreal-api-mcp)** - ⭐ 40
   Instant, accurate Unreal Engine API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations.

2614. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 39
   MCP server for anki

2615. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

2616. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 39
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

2617. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

2618. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

2619. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

2620. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

2621. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 39
   A package manager to manage all your mcp servers across platforms

2622. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

2623. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

2624. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 39
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

2625. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 39
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

2626. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 39
   Self-hosted Stealth Scraping & Federated Search for AI Agents. A 100% private, free alternative to Firecrawl, Jina Reader, and Tavily. Featuring Universal Anti-bot Bypass + Semantic Research Memory, Copy-Paste setup

2627. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 39
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2628. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 39
   Enable AI assistants to explore and query your Steampipe data!

2629. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 39
   A MCP server for Storybook.

2630. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 39
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

2631. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 39
   A hackable Model Context Protocol (MCP) gateway

2632. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2633. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 39
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

2634. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 39
   Rimworld Coding RAG MCP server

2635. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 39
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

2636. **[music-composer-webmcp](https://github.com/Leanmcp-Community/music-composer-webmcp)** - ⭐ 39
   This WebMCP Music Composer project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with local browser contexts (tools) to achieve complex workflows autonomously.

2637. **[best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** - ⭐ 39
   🏆  A ranked list of MCP servers. Updated weekly.

2638. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 39
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2639. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 39
   Model Context Protocol server for Sitecore

2640. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 39
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2641. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

2642. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 39
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

2643. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 39
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2644. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 39
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2645. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 39
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

2646. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 38
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

2647. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 38
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2648. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 38
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 14 security hardening layers

2649. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 38

2650. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 38
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

2651. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

2652. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 38
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

2653. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

2654. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 38
   A Chat Client for LLMs, written in Compose Multiplatform.

2655. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

2656. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

2657. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

2658. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

2659. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 38
   Model Context Protocol Minecraft Server

2660. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

2661. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

2662. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 38
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

2663. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 38
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

2664. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 38
   Highly configurable autonomous efficient-first agentic AI framework for CLI

2665. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 38
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

2666. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 38
   Enhanced MCP server for GitLab: group projects listing and activity tracking

2667. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 38
   awesome-lists now available as MCP server for you agent.

2668. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 38
   An MCP server for querying Solana transactions using natural language with Solscan API

2669. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 38
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

2670. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 38
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

2671. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 38
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

2672. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 38
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2673. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 38
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

2674. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 38
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

2675. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 38
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

2676. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 38
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2677. **[notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)** - ⭐ 38
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

2678. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 38
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

2679. **[brainstorm-mcp](https://github.com/spranab/brainstorm-mcp)** - ⭐ 38
   MCP server for multi-round AI brainstorming debates between multiple models (GPT, DeepSeek, Groq, Ollama, etc.)

2680. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 38
   Claude Unified Model Context Interaction Protocol

2681. **[unity-api-mcp](https://github.com/Codeturion/unity-api-mcp)** - ⭐ 38
   Instant, accurate Unity API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations

2682. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 38
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2683. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 37
   Peta core: The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2684. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 37
   Trivy plugin for starting an MCP server

2685. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 37
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

2686. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

2687. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 37
   MCP server tailored to connecting web crawler data and archives

2688. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 37
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

2689. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 37
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

2690. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

2691. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

2692. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2693. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 37
   Model Context Protocol server to let LLMs write and execute matlab scripts 

2694. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 37
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

2695. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 37
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

2696. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2697. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 37
   Model Context Protocol (MCP) Server for Mistral OCR API

2698. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 37
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

2699. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 37
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

2700. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 37
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

2701. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 37
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

2702. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 37
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2703. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 37
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

2704. **[google-workspace-mcp](https://github.com/dguido/google-workspace-mcp)** - ⭐ 37
   MCP server for Google Drive, Docs, Sheets, Slides, Calendar, Gmail, and Contacts

2705. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 37
   An MCP server for Android's Tasker automation app.

2706. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 37
   A simple note-taking MCP server for recording and managing notes with AI models.

2707. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 37
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

2708. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 37
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

2709. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 37
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2710. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 37
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2711. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 37
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2712. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 37
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2713. **[godot-mcp](https://github.com/HaD0Yun/godot-mcp)** - ⭐ 37
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

2714. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 37
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

2715. **[arifosmcp](https://github.com/ariffazil/arifosmcp)** - ⭐ 37
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

2716. **[mcp-server](https://github.com/Aayush9029/mcp-server)** - ⭐ 37
   MCP SERVER

2717. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 37
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2718. **[MCPwner](https://github.com/Pigyon/MCPwner)** - ⭐ 37
   Model Context Protocol server for autonomous vulnerability discovery

2719. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

2720. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

2721. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

2722. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

2723. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

2724. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

2725. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

2726. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

2727. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 36
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

2728. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 36
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

2729. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 36
   A2A Protocol client and developer toolkit.

2730. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 36
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

2731. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 36
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2732. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 36
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2733. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 36
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

2734. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 36
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

2735. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 36
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2736. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 36
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2737. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 36
   Python sandboxes for llms

2738. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 36
   A curated collection of persona-based mcp server & tool groupings.

2739. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 36
   Vapi MCP Server

2740. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 36
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

2741. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 36
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

2742. **[apple-mail-mcp](https://github.com/patrickfreyer/apple-mail-mcp)** - ⭐ 36
   MCP server giving AI assistants full access to Apple Mail - read, search, compose, organize & analyze emails via natural language

2743. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 36
   Command-line interface for any Model Context Protocol (MCP) server.

2744. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 36
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

2745. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

2746. **[arifOS](https://github.com/ariffazil/arifOS)** - ⭐ 36
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

2747. **[mie](https://github.com/kraklabs/mie)** - ⭐ 36
   Persistent memory graph for AI agents. Facts, decisions, entities, and relationships that survive across sessions, tools, and providers. MCP server — works with Claude, Cursor, ChatGPT, and any MCP client.

2748. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2749. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 36
   Sync MCP (Model Context Protocol) configurations across AI tools

2750. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 36
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2751. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 36
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

2752. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 36
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

2753. **[roampal-core](https://github.com/roampal-ai/roampal-core)** - ⭐ 36
   Outcome-based persistent memory MCP server for Claude Code and OpenCode. Good advice promoted, bad advice demoted. pip install roampal.

2754. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 36
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2755. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 36
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2756. **[mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index)** - ⭐ 36
   17 MCP query tools for codebase navigation — functions, classes, imports, dependency graphs, change impact. Zero dependencies. 87% token reduction.

2757. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 36
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2758. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 36
   Emacs Lisp implementation of the Model Context Protocol

2759. **[omnifocus-mcp-enhanced](https://github.com/jqlts1/omnifocus-mcp-enhanced)** - ⭐ 36
   Enhanced Model Context Protocol (MCP) server for OmniFocus with complete subtask support, perspective views (Inbox/Flagged/Forecast/Tags), ultimate   task filtering, and direct access to custom perspectives. Seamlessly integrate OmniFocus with Claude AI for intelligent task management.

2760. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 36
   Learn Model Context Protocol with Python, published by Packt

2761. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

2762. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

2763. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

2764. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

2765. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

2766. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

2767. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 35
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

2768. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

2769. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 35
   An open source implementation of the Claude built-in text editor tool

2770. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 35
   A super simple Starter to build your own MCP Server

2771. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

2772. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 35
   A Model Context Protocol (MCP) server for NATS messaging system integration

2773. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 35
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2774. **[daisyui-mcp](https://github.com/birdseyevue/daisyui-mcp)** - ⭐ 35
   🌼 A token-friendly local MCP server for DaisyUI component documentation using their public llms.txt.

2775. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 35
   Turn any MCP Client into a "multi-agent" system (via prompting)

2776. **[mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp)** - ⭐ 35
   A Model-Context Protocol server for the MITRE ATT&CK knowledge base

2777. **[awesome-mcp-servers](https://github.com/ever-works/awesome-mcp-servers)** - ⭐ 35
   A curated list of the best MCP Servers, featuring top solutions, libraries, tools, and more. - https://mcpserver.works

2778. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 35
   List of Awesome MCP Servers and Clients for building Agentic Devops 

2779. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 35
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

2780. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2781. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 35
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2782. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 35
   Model Context Server Protocol for your HANA DB

2783. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 35
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2784. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 35
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

2785. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 35
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2786. **[omega-memory](https://github.com/omega-memory/omega-memory)** - ⭐ 35
   Persistent memory for AI coding agents

2787. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 35
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2788. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 34
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

2789. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 34
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

2790. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

2791. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

2792. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

2793. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 34
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

2794. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 34
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

2795. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 34
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

2796. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

2797. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 34
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

2798. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform. 

2799. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

2800. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

2801. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

2802. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 34
   MCP Server connects with claude code local command.

2803. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 34
   Model Context Protocol server written in Scala

2804. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 34
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

2805. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 34
   Apache IoTDB MCP Server

2806. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 34
   Let your agent write code and execute code directly in the browser with WASM

2807. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 34
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

2808. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2809. **[vulnerablemcp](https://github.com/vineethsai/vulnerablemcp)** - ⭐ 34
   A comprehensive database of Model Context Protocol vulnerabilities, security research, and exploits

2810. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 34
   An MCP server that allows users to dynamically add custom tools/functions at runtime

2811. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 34
   A MCP implementation for sending notifications via Pushover

2812. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

2813. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 34
   Capacities×MCP

2814. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 34
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

2815. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 34
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2816. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 34
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

2817. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 34
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

2818. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 34
   Model Context Protocol (MCP) server that interacts with a Debugger

2819. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2820. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 34
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2821. **[mcp-stata](https://github.com/tmonk/mcp-stata)** - ⭐ 34
    A lightweight Model Context Protocol (MCP) server for Stata. Execute commands, inspect data, retrieve stored results (r()/e()), and view graphs in your chat interface. Built for economists who want to integrate LLM assistance into their Stata workflow. 

2822. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 34
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2823. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 34
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

2824. **[mcp](https://github.com/fastly/mcp)** - ⭐ 34
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2825. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 34
   MCP server for native app testing — screenshot, OCR, click, type, find_text, template matching. macOS, Windows & Android. Works with Claude, Cursor, and any MCP client.

2826. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 34
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2827. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 34
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2828. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

2829. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

2830. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 33
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

2831. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 33
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

2832. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

2833. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

2834. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

2835. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

2836. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 33
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

2837. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 33
   About A Model Context Protocol server that executes commands in the current WezTerm session

2838. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 33
   MCP Server for Membrane

2839. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 33
   Minimalist AI agent that fixes itself when things break.

2840. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 33
   AI-Powered Threat Intelligence MCP tool

2841. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 33
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

2842. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 33
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

2843. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 33
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi. 

2844. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 33
   Tools for building modern & secure MCP integrations across the client and server side

2845. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 33
   Minimal Metals stand alone client that allows running the metals mcp server

2846. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 33
   A generic mcp server fuzzer

2847. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 33
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2848. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 33
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2849. **[drawio-mcp-server](https://github.com/simonkurtz-MSFT/drawio-mcp-server)** - ⭐ 33
   A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server generates Draw.io XML directly — no browser extension or Draw.io instance required.

2850. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 33
   Model Context Protocol (MCP) server for openBIM

2851. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 33
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

2852. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2853. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

2854. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

2855. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

2856. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

2857. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 32
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

2858. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

2859. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 32
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2860. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 32
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2861. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

2862. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

2863. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

2864. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 32
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2865. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 32
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

2866. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 32
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

2867. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 32
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2868. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 32
   A Model Context Protocol server starter template

2869. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 32
   A collection of MCP server examples developed by various Java SDKs

2870. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2871. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 32
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

2872. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 32
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

2873. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 32
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2874. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 32
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

2875. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 32
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

2876. **[chabeau](https://github.com/permacommons/chabeau)** - ⭐ 32
   OpenAI-API compatible terminal chatbot and MCP client in Rust

2877. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 32
   Asterisk Model Context Protocol (MCP) server.

2878. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 32
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2879. **[myBrAIn](https://github.com/lilium360/myBrAIn)** - ⭐ 32
   myBrAIn is an MCP (Model Context Protocol) server designed to provide persistent and contextual memory to language models (like Google Antigravity). It acts as a "second brain" for your development environment, allowing the AI to remember project rules, architectural decisions, and technical insights across different chat sessions

2880. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 32
   Arch Linux MCP (Model Context Protocol)

2881. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 32
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

2882. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 32
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2883. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 32
   Implements a model context protocol server using Wolfram Language

2884. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 32
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

2885. **[MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP)** - ⭐ 32
   Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered search and vision analysis APIs optimized for code development workflows

2886. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 32
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2887. **[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp)** - ⭐ 32
   MCP server for controlling a real iPhone via macOS iPhone Mirroring...and any MacOs app. Screenshot, tap, swipe, type — from any MCP client.

2888. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 31
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

2889. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 31
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2890. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

2891. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

2892. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

2893. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 31
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

2894. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

2895. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

2896. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

2897. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32. 

2898. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 31
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

2899. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 31
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2900. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

2901. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 31
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

2902. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 31
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

2903. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 31
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2904. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 31
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

2905. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 31
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2906. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 31
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

2907. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 31
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2908. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2909. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

2910. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 31
   Model Context Protocol Server of Rod

2911. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 31
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

2912. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 31
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2913. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 31
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2914. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 31
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2915. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 31
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2916. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 31
   Query model running with Ollama from within Claude Desktop or other MCP clients

2917. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 31
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

2918. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 31
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2919. **[camofox-mcp](https://github.com/redf0x1/camofox-mcp)** - ⭐ 31
   Anti-detection browser MCP server for AI agents — navigate, interact, and automate the web without getting blocked

2920. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 31
   Model Context Protocol server for CODESYS automation platform

2921. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 31
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2922. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 31
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2923. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 31
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

2924. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 31
   model context protocol for Autodesk Revit

2925. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 31
   Local-first Second brain for AI agents working on your codebase -  detects your team coding conventions and patterns, brings in persistent memory, code-generation checks, and hybrid search with evidence scoring. Exposed through CLI and MCP server.

2926. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 31
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2927. **[godot-mcp](https://github.com/tugcantopaloglu/godot-mcp)** - ⭐ 31
   MCP server for full Godot 4.x engine control — 149 tools for AI-driven game development

2928. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 30
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

2929. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 30
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2930. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 30
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

2931. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

2932. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

2933. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2934. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2935. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

2936. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

2937. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

2938. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

2939. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

2940. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

2941. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

2942. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 30
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

2943. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 30
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

2944. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 30
   MCP (Model Context Protocol) Server for postgres Database

2945. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 30
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2946. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 30
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2947. **[levante](https://github.com/levante-hub/levante)** - ⭐ 30
   Levante - Personal, Secure, Free, Local AI, MCP Client

2948. **[pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server)** - ⭐ 30
   PubNub MCP Model Context Protocol Server for use in Cursor, Windsurf, Claude Desktop, Claude Code and OpenAI Codex and more!

2949. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 30
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2950. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 30
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

2951. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 30
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2952. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 30
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

2953. **[mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm)** - ⭐ 30
   MCP server for Klever blockchain smart contract development

2954. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 30
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2955. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 30
   Zillow MCP Server for real estate data access via the Model Context Protocol

2956. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 30
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2957. **[rss-mcp](https://github.com/veithly/rss-mcp)** - ⭐ 30
   This is a Model Context Protocol (MCP) server built with TypeScript. It provides a versatile tool to fetch and parse any standard RSS/Atom feed, and also includes special support for RSSHub feeds. 

2958. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 30
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

2959. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 30
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2960. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 30
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2961. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 30
   PowerPlatform Model Context Protocol server

2962. **[jdwp-mcp](https://github.com/navicore/jdwp-mcp)** - ⭐ 30
   Java debugging for LLMs via JDWP and Model Context Protocol

2963. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 30
   Open source local MCP server providing AI assistants with comprehensive access to eBay's Sell APIs. Includes 325 tools for inventory management, order fulfillment, marketing campaigns, analytics, developer tools, and more.

2964. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 29
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

2965. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2966. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2967. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2968. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2969. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2970. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 29
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2971. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2972. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 29
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

2973. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 29
   MCP (Model Context Protocol) server for biothings

2974. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

2975. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

2976. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

2977. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

2978. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

2979. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

2980. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

2981. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2982. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 29
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2983. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2984. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2985. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 29
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2986. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 29
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

2987. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2988. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 29
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2989. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 29
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2990. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 29
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2991. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 29
   Convert source code to LLM ready knowledge base

2992. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 29

2993. **[izan.io](https://github.com/ekingunoncu/izan.io)** - ⭐ 29
   Turn Any Browser Action & Data Extraction into an AI Tool in 60 Seconds

2994. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 29
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

2995. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 29
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2996. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2997. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 29
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2998. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 29
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

2999. **[npm-packages](https://github.com/WebMCP-org/npm-packages)** - ⭐ 29
   NPM packages for MCP-B: Transport layers, React hooks, and browser tools for the Model Context Protocol

3000. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 29
   Testing framework for Model Context Protocol (MCP)

3001. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 29
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

3002. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 29
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

3003. **[context-harness](https://github.com/parallax-labs/context-harness)** - ⭐ 29
   Local-first context ingestion and retrieval for AI tools. SQLite + embeddings + MCP server for Cursor & Claude.

3004. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 29
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

3005. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 29
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

3006. **[Ori-Mnemos](https://github.com/aayoawoyemi/Ori-Mnemos)** - ⭐ 29
   Local-first persistent memory for AI agents. Knowledge graph + ACT-R decay + three-signal retrieval. Agents wake up as themselves. MCP server (14 tools) for Claude, Cursor, Windsurf, Cline.

3007. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

3008. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

3009. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

3010. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

3011. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

3012. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 28
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

3013. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

3014. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

3015. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

3016. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 28
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

3017. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

3018. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 28
   ESPN Fantasy API with LLMs!

3019. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 28
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

3020. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 28
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

3021. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 28
   a web logging proxy for MCP client-server communication

3022. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 28
   Model Context Protocol to bridge in Substack writings to Claude.

3023. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 28
   Azure AI Foundry - Agents related sample code

3024. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 28
   Fast rust MCP proxy between stdio and SSE

3025. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 28
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

3026. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 28
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

3027. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 28
   An implementation of Giphy integration with Model Context Protocol

3028. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 28
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

3029. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 28
   A simple Model Context Protocol (MCP) server for Clay.

3030. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 28
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

3031. **[drawio-mcp-extension](https://github.com/lgazo/drawio-mcp-extension)** - ⭐ 28
   Draw.io Model Context Protocol (MCP) Browser Extension

3032. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

3033. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

3034. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

3035. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

3036. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

3037. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

3038. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

3039. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 27
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

3040. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

3041. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 27
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

3042. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

3043. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 27
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

3044. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 27
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

3045. **[review-flow](https://github.com/DGouron/review-flow)** - ⭐ 27
   Automated AI code reviews powered — webhook-driven, real-time dashboard, MCP integration, smart queue with deduplication, multi-agent audits, and iterative follow-up reviews for GitLab MRs and GitHub PRs

3046. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 27
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

3047. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 27
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

3048. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

3049. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 27
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

3050. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 27
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

3051. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 27
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

3052. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 27
   Model Context Protocol Server for NebulaGraph 3.x

3053. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 27
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

3054. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 27
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

3055. **[mcp_xpp](https://github.com/ccampora/mcp_xpp)** - ⭐ 27
   Experimental MCP server for Dynamics 365 F&O X++ development. Provides object creation, modification, and codebase navigation through the Model Context Protocol. Includes VS2022 service integration for D365 object handling.

3056. **[unplugin-devpilot](https://github.com/zcf0508/unplugin-devpilot)** - ⭐ 27
   A universal plugin framework for development tools that enables seamless browser-server communication and MCP (Model Context Protocol) integration with AI/LLM systems.

3057. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 27
   Simple MCP to give Claude ability to check current time as well as know when holidays are, what is the time distance between dates etc.

3058. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 27
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

3059. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 27
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3060. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 27
   Antrophics Model context protocol to edit powerpoint files

3061. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 27
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

3062. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

3063. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 27
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

3064. **[pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp)** - ⭐ 27
   Model Context Protocol (MCP) server for AI-powered reservoir engineering calculations. Integrates pyResToolbox with Claude AI for PVT analysis, well   performance, simulation support, and more. 47 production-ready tools using industry-standard correlations.

3065. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 27
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

3066. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 27
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

3067. **[amazon_ads_mcp](https://github.com/KuudoAI/amazon_ads_mcp)** - ⭐ 27
   Amazon Ads MCP - Model Context Protocol server for Amazon Advertising API

3068. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 27
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

3069. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

3070. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

3071. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

3072. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

3073. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

3074. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

3075. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 26
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

3076. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

3077. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

3078. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 26
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

3079. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy 

3080. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 26
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

3081. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

3082. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for GreptimeDB

3083. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 26
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

3084. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 26
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

3085. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 26
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

3086. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 26
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

3087. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 26
   Educational repo for MCP streamable HTTP servers and clients

3088. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 26
   A Model Context Protocol server for 3D Slicer integration

3089. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 26
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

3090. **[lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server exposing Lucide icons as resources and tools for LLMs and agentic applications. Built with Bun and the MCP TypeScript SDK.

3091. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 26
   Model Context Protocol server for Github Repo // Reading Github Repo

3092. **[autotask-mcp](https://github.com/wyre-technology/autotask-mcp)** - ⭐ 26
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3093. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 26
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

3094. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 26
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

3095. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 26
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

3096. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 26
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

3097. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 26
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

3098. **[computeruseprotocol](https://github.com/computeruseprotocol/computeruseprotocol)** - ⭐ 26
   Computer Use Protocol is a universal schema for AI agents to perceive and interact with any desktop UI.

3099. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 26
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3100. **[hop](https://github.com/danmartuszewski/hop)** - ⭐ 26
   Fast, elegant SSH connection manager with a TUI dashboard and MCP server

3101. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 25
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

3102. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

3103. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

3104. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

3105. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

3106. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

3107. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

3108. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3109. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

3110. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

3111. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

3112. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

3113. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

3114. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

3115. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 25
   A Curated List of MCP Servers, Clients and Toolkits

3116. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

3117. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 25
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

3118. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 25
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

3119. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 25
   Message Communication Protocol server for json2video API integration

3120. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 25
   Simple MCP Client for remote MCP Servers 🌐

3121. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 25
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

3122. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 25
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

3123. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 25
   Simple MCP SDK in Java

3124. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 25
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

3125. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 25
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

3126. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 25
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

3127. **[raybridge](https://github.com/jlokos/raybridge)** - ⭐ 25
   MCP server that bridges Raycast extensions to any MCP-compatible client

3128. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 25
   A Fastify plugin to run Model Context Protocol (MCP) servers

3129. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

3130. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 25
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3131. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server for creating Datawrapper charts using AI assistants.

3132. **[mcpx](https://github.com/lydakis/mcpx)** - ⭐ 25
   Turn MCP servers into composable CLIs.

3133. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

3134. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

3135. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

3136. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

3137. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

3138. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3139. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

3140. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

3141. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

3142. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

3143. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

3144. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

3145. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

3146. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

3147. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 24
   An MCP server enabling CFBD API queries within Claude Desktop.

3148. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 24
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

3149. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

3150. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

3151. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

3152. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

3153. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

3154. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

3155. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

3156. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

3157. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 24
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

3158. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 24
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + Java + TypeScript

3159. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3160. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 24
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

3161. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 24
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

3162. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 24
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

3163. **[markview](https://github.com/paulhkang94/markview)** - ⭐ 24
   Native macOS markdown preview app. Swift/SwiftUI, GitHub Flavored Markdown, syntax highlighting, linting, plugins. No Electron.

3164. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 24
   MCP server wrapping around the Fabric Rest API

3165. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 24
   An MCP Server and client for communicating with Nifi (v1.28)

3166. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 24
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

3167. **[golemcore-bot](https://github.com/alexk-dev/golemcore-bot)** - ⭐ 24
   AI agent framework for Java — skill-based architecture with MCP support, tool calling, RAG, and Telegram integration. Built on Spring Boot and  LangChain4j

3168. **[Kaimon.jl](https://github.com/kahliburke/Kaimon.jl)** - ⭐ 24
   MCP server giving AI agents full access to Julia's runtime via a live Gate — code execution, introspection, debugging, testing, and semantic search

3169. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 23
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

3170. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

3171. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

3172. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

3173. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3174. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

3175. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

3176. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

3177. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

3178. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

3179. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

3180. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

3181. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

3182. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

3183. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

3184. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

3185. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 23
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

3186. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 23
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

3187. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 23
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

3188. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 23
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

3189. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 23
   Tanzu Platform Chat

3190. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 23
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3191. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 23
   MCP server to expose local zotero repository to MCP clients 

3192. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 23
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

3193. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 23
   CLI for calling successive MCP Server tools

3194. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 23
   Local FAISS vector store as an MCP server – Agent Memory, drop-in local semantic search for Claude / Copilot / Agents.

3195. **[MCPHammer](https://github.com/praetorian-inc/MCPHammer)** - ⭐ 23
   MCP security testing framework for evaluating Model Context Protocol server vulnerabilities

3196. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 23
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3197. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 23
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3198. **[agentgate](https://github.com/agentkitai/agentgate)** - ⭐ 23
   Approval workflows for AI agents

3199. **[nitrostack](https://github.com/nitrocloudofficial/nitrostack)** - ⭐ 23
   The full-stack TypeScript framework to build, test, and deploy production-ready MCP servers and AI-native apps.

3200. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

3201. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

3202. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

3203. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

3204. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

3205. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

3206. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

3207. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

3208. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

3209. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

3210. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

3211. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

3212. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

3213. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

3214. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

3215. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

3216. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 22
   Memory Cache Server for use with supported MCP API Clients.

3217. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 22
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

3218. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 22
   Rust MCP framework for building AI agents

3219. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 22
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

3220. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 22
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

3221. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 22
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3222. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 22
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

3223. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 22
   A collection of mcp servers/client/sdks

3224. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 22
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

3225. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 22
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3226. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 22
   MCP agent/client/server implementation for private knowledge base

3227. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 22
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

3228. **[janee](https://github.com/rsdouglas/janee)** - ⭐ 22
   Secrets management for AI agents via MCP • @janeesecure

3229. **[kimi-code-mcp](https://github.com/howardpen9/kimi-code-mcp)** - ⭐ 22
   MCP server for Claude Code × Kimi K2.5 (256K context) — delegate bulk codebase analysis to Kimi, save 90% on token costs. Session caching, parallel agents, TypeScript.

3230. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 22
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3231. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 22
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3232. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 21
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

3233. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

3234. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

3235. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

3236. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

3237. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

3238. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

3239. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

3240. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

3241. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

3242. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

3243. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

3244. **[plux](https://github.com/milisp/plux)** - ⭐ 21
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

3245. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

3246. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 21
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

3247. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 21
   Haskell server/client for MCP (Model Context Protocol)

3248. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 21
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3249. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 21
   MCP server to integrate AWS S3 and LLM

3250. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 21
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

3251. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 21
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3252. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 21
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

3253. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 21
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

3254. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 21
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

3255. **[heuristic-mcp](https://github.com/softerist/heuristic-mcp)** - ⭐ 21
   Enhanced MCP server for semantic code search with call-graph proximity, recency ranking, and find-similar-code. Built for AI coding assistants.

3256. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 21
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

3257. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 21
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3258. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 21
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

3259. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 21
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

3260. **[agent-studio-starter](https://github.com/nsphung/agent-studio-starter)** - ⭐ 21
   Stop building AI agents from scratch. Bootstrap starter Agent app with LangGraph, CopilotKit, and beautiful Generative UIs.

3261. **[codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool)** - ⭐ 21

3262. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 21
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets. 

3263. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 21
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3264. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 21
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

3265. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 20
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

3266. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

3267. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

3268. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

3269. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

3270. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

3271. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 20
   BioContextAI Knowledgebase MCP server for biomedical agentic AI 

3272. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 20
   The BioContextAI Registry for biomedical MCP servers

3273. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 20
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

3274. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 20
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

3275. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 20
   The Decodo MCP server which enables MCP clients to interface with services.

3276. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 20
   Pre-release - Model Context Protocol server for Rollbar

3277. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 20
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3278. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 20
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3279. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 20
   MCP Server for fething yfinance financial data into Claude Desktop

3280. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 20
   MCP server and client for running Linux commands

3281. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 20
   HasMCP Community Edition

3282. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 20
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3283. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 20
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

3284. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 20
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3285. **[archmcp](https://github.com/dejo1307/archmcp)** - ⭐ 20
   archmcp - MCP Architectural Snapshot Server and Knowledge Graph

3286. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 20

3287. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 20
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

3288. **[Jiva](https://github.com/KarmaloopAI/Jiva)** - ⭐ 20
   Jiva is a CLI-first, open source autonomous AI agent and open alternative to Claude. Built in TypeScript with a three-agent architecture (Manager, Worker, Client), it autonomously plans and executes tasks from your terminal. Supports MCP servers, a built-in Skills system, and Jiva Personas - a plugin framework fully compatible with Claude Plugins.

3289. **[gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp)** - ⭐ 20
   MCP server for Google Gemini — free image generation, editing & chat via browser cookies. No API keys needed.

3290. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 20
   Connect to any MCP servers using agents

3291. **[fcpxml-mcp-server](https://github.com/DareDev256/fcpxml-mcp-server)** - ⭐ 20
   🎬 The first AI-powered MCP server for Final Cut Pro XML. Control your edits with natural language.

3292. **[ctxvault](https://github.com/Filippo-Venturini/ctxvault)** - ⭐ 20
   Local memory infrastructure for AI agents. Isolated vaults you compose, control, monitor and query — no cloud, no setup.

3293. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 19
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3294. **[starbase](https://github.com/metorial/starbase)** - ⭐ 19
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

3295. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

3296. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

3297. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 19
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

3298. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 19
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

3299. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

3300. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 19
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3301. **[termlink](https://github.com/chu2bard/termlink)** - ⭐ 19
   MCP server for shell and terminal operations

3302. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database. 

3303. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

3304. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 19
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3305. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 19
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

3306. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 19
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

3307. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 19
   Yandex Cloud MCP Servers

3308. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 19
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

3309. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 19
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3310. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 19
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

3311. **[mcp-client-cli](https://github.com/addity3/mcp-client-cli)** - ⭐ 19
   cli-based program to run llm prompt and mcp

3312. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 19
   🧬 Analyze spatial transcriptomics data through natural language conversation. Stop writing code, start having conversations with your data. MCP server for Claude Code and Codex.

3313. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 19
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3314. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 19
   A GitHub CLI extension that seamlessly runs the github-mcp-server using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

3315. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 19
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3316. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) library for Zig — bringing MCP support to the Zig ecosystem.

3317. **[ckan-mcp-server](https://github.com/ondata/ckan-mcp-server)** - ⭐ 19
   MCP server for querying CKAN open data portals (package search, DataStore SQL, organizations, groups, tags)

3318. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 18
   A fetch API based TypeScript SDK for MCP

3319. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 18
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3320. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

3321. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

3322. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

3323. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

3324. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 18
   a Nushell cross.stream extension to interact with LLMs and MCP servers

3325. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

3326. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

3327. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

3328. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 18
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

3329. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 18
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

3330. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 18

3331. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

3332. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 18
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

3333. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 18
   Model Context Protocol (MCP)

3334. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 18
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

3335. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 18
   An MCP server and client for LLMs to interact with Unity Projects

3336. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 18
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

3337. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 18
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

3338. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 18
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

3339. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 18
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

3340. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 18
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

3341. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server implementation for Gumroad API

3342. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 18
   A command-line utility for interacting with MCP servers.

3343. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 18
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

3344. **[agentidentityprotocol](https://github.com/openagentidentityprotocol/agentidentityprotocol)** - ⭐ 18
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3345. **[toolhive-catalog](https://github.com/stacklok/toolhive-catalog)** - ⭐ 18
   ToolHive's registry catalog of MCP servers

3346. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 18
   Local-first quality gate + fix-loop controller for AI coding agents (CLI + MCP).

3347. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 18
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

3348. **[twincat-validator-mcp](https://github.com/agenticcontrolio/twincat-validator-mcp)** - ⭐ 18
   An MCP server that validates, auto-fixes, and scaffolds TwinCAT 3 XML files. Connect it to any LLM client to give your AI assistant reliable, deterministic TwinCAT code quality tooling — structural checks, 21 IEC 61131-3 OOP checks, auto-fix pipelines, and canonical skeleton generation.

3349. **[minimal-godot-mcp](https://github.com/ryanmazzolini/minimal-godot-mcp)** - ⭐ 18
   Lightweight MCP server bridging Godot LSP to MCP clients for GDScript validation

3350. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 18
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3351. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

3352. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

3353. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

3354. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

3355. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

3356. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 17
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

3357. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

3358. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

3359. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

3360. **[daiv](https://github.com/srtab/daiv)** - ⭐ 17
   Your AI-powered SWE teammate, built into your git workflow

3361. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

3362. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 17
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

3363. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 17
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3364. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 17
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

3365. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 17
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

3366. **[rpc-nodes-mcp](https://github.com/chainstacklabs/rpc-nodes-mcp)** - ⭐ 17
   Minimal, fast, and extensible MCP server for interactions with JSON-RPC blockchain nodes

3367. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 17
   MCP server for graph representation of a codebase

3368. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 17
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

3369. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 17
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

3370. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 17
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

3371. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 17
   An MCP client that uses signal for sending and receiving messages.

3372. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 17
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

3373. **[mcpforge](https://github.com/lorenzosaraiva/mcpforge)** - ⭐ 17

3374. **[stitch-mcp-auto](https://github.com/GreenSheep01201/stitch-mcp-auto)** - ⭐ 17
   Automated installer for Stitch MCP - The easiest way to set up your Universal MCP server for Google Stitch.

3375. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 17
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

3376. **[subcog](https://github.com/zircote/subcog)** - ⭐ 17
   Persistent memory system for AI coding assistants. Captures decisions, learnings, and context from coding sessions. Features hybrid search (semantic + BM25), MCP server integration, SQLite persistence with knowledge graph, and proactive memory surfacing. Written in Rust.

3377. **[awesome-finance-mcp](https://github.com/BlockRunAI/awesome-finance-mcp)** - ⭐ 17
   A curated list of MCP servers for AI finance agents

3378. **[slack-mcp-plugin](https://github.com/slackapi/slack-mcp-plugin)** - ⭐ 17
   Repo containing the configuration information for the Slack MCP to be added to other clients

3379. **[mcp-kling](https://github.com/199-mcp/mcp-kling)** - ⭐ 17
   🎬 The FIRST MCP server for Kling AI video generation! Generate stunning AI videos directly from Claude.

3380. **[ads-mcp](https://github.com/amekala/ads-mcp)** - ⭐ 17
   MCP server for managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. 100+ tools for campaign creation, performance analysis, keyword research, and budget optimization. Works with Claude Code, Cursor, Codex, ChatGPT, Windsurf, and Cline.

3381. **[claude-vigil-mcp](https://github.com/Vvkmnn/claude-vigil-mcp)** - ⭐ 16
   🏺 An MCP server for checkpointing and file recovery in Claude Code

3382. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 16
   An extensible AI agents framework

3383. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

3384. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 16
   A model-agnostic MCP Client-Server for .Net and Unity

3385. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

3386. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

3387. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

3388. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

3389. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

3390. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

3391. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3392. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 16
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

3393. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

3394. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

3395. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 16

3396. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 16
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

3397. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 16
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

3398. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 16
   MCP server for xAI Grok — read and serve .faf project context. npm: grok-faf-mcp

3399. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 16
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

3400. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 16
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

3401. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 16
   simple mcp server for interacting with local obsidian notes

3402. **[MicrosoftGraph_Transcript_MCP](https://github.com/ITSpecialist111/MicrosoftGraph_Transcript_MCP)** - ⭐ 16
   A remote Model Context Protocol (MCP) server that retrieves Microsoft Teams meeting transcripts via the Microsoft Graph API, using delegated **OAuth 2.0 On-Behalf-Of (OBO)** authentication.  Designed for integration with Microsoft Copilot Studio (via the MCP Wizard), though any MCP-compatible client can connect.

3403. **[mcp-ecosystem](https://github.com/SynkraAI/mcp-ecosystem)** - ⭐ 16
   MCP Ecosystem: Docker MCP Toolkit, IDE Configs & Presets for AIOS

3404. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 16
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

3405. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 16
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

3406. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 16
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

3407. **[penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** - ⭐ 16
   MCP server for Penpot - Connect AI assistants to Penpot design platform via Model Context Protocol

3408. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 16

3409. **[faf](https://github.com/Wolfe-Jam/faf)** - ⭐ 16
   FAF specification — IANA-registered AI context format (application/vnd.faf+yaml)

3410. **[bonnard](https://github.com/bonnard-data/bonnard)** - ⭐ 16
   Open-source agentic schema for reliable data outputs. Query data through MCP and via our SDK. Create apps, embed data or just simply explore through your preferred agent.

3411. **[speclock](https://github.com/sgroy10/speclock)** - ⭐ 16
   AI Constraint Engine by Sandeep Roy — stops AI from breaking what you locked. 100/100 on Claude's adversarial test suite. 42 MCP tools. Works with Bolt.new, Lovable, Claude Code, Cursor. Free & open source.

3412. **[scopus-mcp](https://github.com/qwe4559999/scopus-mcp)** - ⭐ 16
   A Model Context Protocol (MCP) server for Elsevier Scopus. Allows AI assistants like Claude to search academic papers, retrieve abstracts, and analyze author profiles directly.

3413. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 16
   MCP server for penetration testing

3414. **[nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp)** - ⭐ 16
   Gemini Vision & Image Generation MCP for Claude Desktop and Claude Code

3415. **[email-mcp](https://github.com/codefuturist/email-mcp)** - ⭐ 16
   Email MCP server with full IMAP + SMTP support — read, search, send, manage, and organize email from any AI assistant via the Model Context Protocol

3416. **[linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server)** - ⭐ 16
   🔗 A Model Context Protocol (MCP) server for LinkedIn — search people, companies, and jobs, scrape profiles, and get structured data via any MCP-compatible AI client.

3417. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 15
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

3418. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 15
   An MCP server to read MCP logs to debug directly inside the client

3419. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

3420. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 15
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

3421. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

3422. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

3423. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data 

3424. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

3425. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 15
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

3426. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 15
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

3427. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

3428. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 15
   Unity Catalog AI Model Context Protocol Server

3429. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 15
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

3430. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 15
   MCP server and client for Frontapp

3431. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 15
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

3432. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 15
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

3433. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 15
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

3434. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 15
   A web-based client for connecting to MCP servers with OAuth support

3435. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 15
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

3436. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 15
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

3437. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 15
   A Socratic dialogue engine for AI agents. 

3438. **[mcp](https://github.com/local-falcon/mcp)** - ⭐ 15
   MCP server for Local Falcon's local SEO and AI visibility platform: geo-grid rank tracking, campaign management, and competitor analysis via Model Context Protocol

3439. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 15
   MCP server for Open Targets Data

3440. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 15
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

3441. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 15
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

3442. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 15
   Markdown To PDF Conversion MCP

3443. **[Unity-AI-ParticleSystem](https://github.com/IvanMurzak/Unity-AI-ParticleSystem)** - ⭐ 15
   AI-powered tools for Unity Particle System. Create and modify Particle System directly through natural language commands.

3444. **[XcodeMCPWrapper](https://github.com/SoundBlaster/XcodeMCPWrapper)** - ⭐ 15
   MCP that makes Xcode 26.3's MCP compatible with Cursor and other strict MCP-spec-compliant clients

3445. **[opencode-browser](https://github.com/michaljach/opencode-browser)** - ⭐ 15
   Browser automation plugin for OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via MCP integration

3446. **[agent-architecture-review-sample](https://github.com/Azure-Samples/agent-architecture-review-sample)** - ⭐ 15
   The Architecture Review Agent is an open-source AI agent sample that reviews software architectures and generates interactive diagrams automatically. 

3447. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 15
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

3448. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 15
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

3449. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 15
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

3450. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 15
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

3451. **[Screenhand](https://github.com/manushi4/Screenhand)** - ⭐ 15
   Give AI eyes and hands on your desktop. Open-source MCP server for desktop automation — screenshots, UI control, browser automation, OCR. Works with Claude, Cursor, and any MCP client. macOS + Windows.

3452. **[agentify](https://github.com/koriyoshi2041/agentify)** - ⭐ 15
   Agent Interface Compiler — One command. Every agent speaks your product. Transform OpenAPI specs into MCP Servers, Skills, CLAUDE.md, AGENTS.md, and more.

3453. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 15
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

3454. **[video-research-mcp](https://github.com/Galbaz1/video-research-mcp)** - ⭐ 15
   Give Claude Code 41 research & video tools with one command. Video analysis, deep research, content extraction, explainer video creation, and Weaviate vector search — powered by Gemini 3.1 Pro.

3455. **[roblox-executor-mcp](https://github.com/notpoiu/roblox-executor-mcp)** - ⭐ 15
   A MCP Server which allows for direct access to the roblox game client

3456. **[trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp)** - ⭐ 15
   TrainingPeaks MCP server for Claude Desktop, Code and Cowork. No API approval needed - works with any account. Query workouts, CTL/ATL/TSB fitness data, power PRs via natural language.

3457. **[better-notion-mcp](https://github.com/n24q02m/better-notion-mcp)** - ⭐ 15
   Markdown-first MCP server for Notion API - composite tools optimized for AI agents

3458. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 15
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3459. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 14
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

3460. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

3461. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

3462. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

3463. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

3464. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

3465. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

3466. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server 

3467. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 14
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

3468. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 14
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics 

3469. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3470. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 14
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

3471. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

3472. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

3473. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 14
   Official ConfigCat Model Context Protocol (MCP) Server 

3474. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 14
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

3475. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 14
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

3476. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 14
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

3477. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 14

3478. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 14
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

3479. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 14
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

3480. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 14
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

3481. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 14
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

3482. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 14
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

3483. **[mcpskills-cli](https://github.com/dhanababum/mcpskills-cli)** - ⭐ 14
   Generate Agent Skills from MCP server tools. Connects via Streamable HTTP, discovers tools, and outputs a skill with schema docs and a call script in the language of your choice.

3484. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 14
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3485. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 14
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

3486. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 14
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

3487. **[mcp-server-zotero-dev](https://github.com/introfini/mcp-server-zotero-dev)** - ⭐ 14
   Give your AI assistant superpowers for Zotero plugin development. 25 tools for screenshots, DOM inspection, JavaScript execution, build integration, and debugging via Model Context Protocol.

3488. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 14
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

3489. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 14
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

3490. **[webfetch-mcp](https://github.com/manooll/webfetch-mcp)** - ⭐ 14
   Live Web Access for Your Local AI — Tunable Search & Clean Content Extraction

3491. **[LSP4J-MCP](https://github.com/stephanj/LSP4J-MCP)** - ⭐ 14
   A Java MCP (Model Context Protocol) server that wraps JDTLS (Eclipse JDT Language Server) using LSP4J to provide Java IDE features to AI assistants like Claude.

3492. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 14
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

3493. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 14
   Session-based Slack MCP for Claude and MCP clients: local-first workflows, secure-default HTTP.

3494. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 14
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

3495. **[domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp)** - ⭐ 14
   Zero-config domain availability MCP for Claude & ChatGPT. AI suggestions, premium/auction detection via GoDaddy, RDAP/WHOIS fallback. Stdio + HTTP.

3496. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 14
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

3497. **[swift-mcp](https://github.com/DePasqualeOrg/swift-mcp)** - ⭐ 14
   Full-featured Swift SDK for Model Context Protocol servers and clients

3498. **[FocusRelayMCP](https://github.com/deverman/FocusRelayMCP)** - ⭐ 14
   Talk to your OmniFocus tasks. An OmniFocus MCP server that lets AI assistants query your tasks, projects, and tags using natural language—no more clicking through endless lists.

3499. **[webmcp-react](https://github.com/MCPCat/webmcp-react)** - ⭐ 14
   React hooks for exposing your app's functionality as WebMCP tools - transport-agnostic, SSR-safe, Strict Mode safe, W3C spec-aligned

3500. **[extract-llms-docs](https://github.com/nirholas/extract-llms-docs)** - ⭐ 14
   Extract documentation for AI agents from any site with llms.txt support. Features MCP server, REST API, batch processing, and multiple export formats.

3501. **[muster](https://github.com/giantswarm/muster)** - ⭐ 14
   MCP tool management and workflow proxy

3502. **[photon](https://github.com/portel-dev/photon)** - ⭐ 14
   Define intent once. Photon turns a single TypeScript file into CLI tools, MCP servers, and web interfaces.

3503. **[ida-codex-mcp](https://github.com/Iamgublin/ida-codex-mcp)** - ⭐ 14
   IDA Codex MCP bridges IDA Pro 9.2 with the MCP ecosystem. It provides an IDA plugin and a stdio MCP server that expose   function lists, call graphs, Hex‑Rays pseudocode, disassembly, imports/exports, xrefs, strings, and memory reads to   MCP clients.

3504. **[robotmem](https://github.com/robotmem/robotmem)** - ⭐ 14
   Robot Memory - Persistent memory system for AI robots. MCP Server + hybrid search + spatial retrieval.

3505. **[nest-mcp](https://github.com/btwld/nest-mcp)** - ⭐ 13
   Build Model Context Protocol (MCP) servers, clients, and gateways using the NestJS ecosystem you already know.

3506. **[claude-praetorian-mcp](https://github.com/Vvkmnn/claude-praetorian-mcp)** - ⭐ 13
   ⚜️ An MCP server for context compaction and recycling in Claude Code

3507. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

3508. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

3509. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

3510. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

3511. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

3512. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

3513. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

3514. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

3515. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

3516. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

3517. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

3518. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

3519. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

3520. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

3521. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 13
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3522. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 13
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3523. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

3524. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

3525. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 13
   MCP server to manage Spotify from MCP clients

3526. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

3527. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

3528. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

3529. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 13
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

3530. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 13
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

3531. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 13
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

3532. **[devtap](https://github.com/killme2008/devtap)** - ⭐ 13
   Bridge build/dev process output to AI coding sessions via MCP — supports Claude Code, Codex, OpenCode, Gemini CLI, and aider

3533. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 13
   talk to sarvam APIs directly, without code.

3534. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 13
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

3535. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 13
   A server implementation for the Model Context Protocol (MCP) in Ruby.

3536. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 13
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

3537. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 13
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

3538. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 13
   Taiga UI MCP server providing documentation search and scaffolding tools.

3539. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 13
   MCP server for OWL applications

3540. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 13
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

3541. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 13
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

3542. **[shodan-mcp](https://github.com/Vorota-ai/shodan-mcp)** - ⭐ 13
   Shodan MCP server for Claude, Cursor & VS Code. 20 tools for passive reconnaissance, CVE/CPE intelligence, DNS analysis, and device search. 4 tools work free without an API key. OSINT and vulnerability research from your IDE.

3543. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 13
   Simple Weather MCP Server Example

3544. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 13
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

3545. **[agent-board](https://github.com/quentintou/agent-board)** - ⭐ 13
   Open-source multi-agent task board for OpenClaw. Kanban + DAG dependencies + MCP server + auto-retry + audit trail. Built for autonomous AI agent teams.

3546. **[istek](https://github.com/istekapp/istek)** - ⭐ 13
   The API client built for AI agents. HTTP, GraphQL, gRPC, WebSocket, MQTT + MCP."

3547. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 13
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

3548. **[mcp-server-template](https://github.com/BearHuddleston/mcp-server-template)** - ⭐ 13
   Spec-driven Go MCP server template for building domain MCPs with AI-agent onboarding.

3549. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

3550. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 13
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

3551. **[obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** - ⭐ 13
   MCP server for Obsidian vault management - enables Claude and other AI assistants to read, write, search, and organize your notes

3552. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 13
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

3553. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 13
   MCP Client for Gemma-3

3554. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 13
   Awesome list of MCP servers for interacting with hardware and the physical world.

3555. **[phabricator-mcp](https://github.com/freelancer/phabricator-mcp)** - ⭐ 13
   MCP server for Phabricator

3556. **[WAIaaS](https://github.com/minhoyoo-iotrust/WAIaaS)** - ⭐ 13
   Wallet-as-a-Service for all AI agents in the world

3557. **[x402-deploy](https://github.com/nirholas/x402-deploy)** - ⭐ 13
   Turn any API or MCP server into a paid service with x402 

3558. **[servicenow-mcp](https://github.com/aartiq/servicenow-mcp)** - ⭐ 13
   Production-ready Model Context Protocol server for ServiceNow platform integration - ITOM, ITSM, CMDB with OAuth, natural language queries, and enterprise security controls

3559. **[stata-workbench](https://github.com/tmonk/stata-workbench)** - ⭐ 13
   A VS Code compatible extension (Cursor, Windsurf, Antigravity etc.) that allows Stata code to be run directly from the editor. Enables AI agents to directly interact with Stata. Powered by mcp-stata, https://github.com/tmonk/mcp-stata.

3560. **[conductor](https://github.com/aryabyte21/conductor)** - ⭐ 13
   Manage MCP server configs across AI coding clients

3561. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 12
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

3562. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

3563. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 12
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

3564. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

3565. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

3566. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

3567. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

3568. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 12
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

3569. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

3570. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

3571. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

3572. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 12
   The ultimate AI-powered generator for llms.txt and llms-full.txt files. 

3573. **[claude_autoapprove](https://github.com/PyneSys/claude_autoapprove)** - ⭐ 12
   Autoapprove support for claude

3574. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

3575. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

3576. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 12
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

3577. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 12
   An opinionated MCP module for NestJS

3578. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

3579. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 12
   MCP server for kintone

3580. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

3581. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3582. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 12
   🥾 _b00t_:  brians dotfiles aka state of the art agentic tooling & context initialization

3583. **[jenkins-mcp-server](https://github.com/AshwiniGhuge3012/jenkins-mcp-server)** - ⭐ 12
   An MCP server for interacting with a Jenkins server. Allows you to trigger jobs, check build statuses, and manage your Jenkins instance through MCP.

3584. **[openagentidentityprotocol](https://github.com/openagentidentityprotocol/openagentidentityprotocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3585. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 12
   Universal cli to add an MCP server to a variety of clients

3586. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 12
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

3587. **[MCPGateway](https://github.com/abdullah1854/MCPGateway)** - ⭐ 12
   Open-source MCP server — progressive tool discovery, code execution, intelligent routing & token optimization across 50+ tools

3588. **[mcp-interactive-terminal](https://github.com/amol21p/mcp-interactive-terminal)** - ⭐ 12
   MCP server that gives AI agents (Claude Code, Cursor, Windsurf) real interactive terminal sessions — REPLs, SSH, databases, Docker, and any interactive CLI with clean output and smart completion detection

3589. **[kiro-powers](https://github.com/praveenc/kiro-powers)** - ⭐ 12
   Repository of custom kiro powers. https://kiro.dev/docs/powers/

3590. **[cie](https://github.com/kraklabs/cie)** - ⭐ 12
   Code Intelligence Engine — indexes your codebase and gives AI assistants deep understanding via MCP (semantic search, call graphs, 20+ tools)

3591. **[guildbridge](https://github.com/dend/guildbridge)** - ⭐ 12
   🏰 Remotely hosted MCP server for Discord

3592. **[arxiv-mcp-server](https://github.com/1Dark134/arxiv-mcp-server)** - ⭐ 12
   arXiv MCP Server Client 🐙 enables AI assistants to search, retrieve, analyze, and summarize arXiv papers with features like author/category browsing, trends, and citation insights.

3593. **[docdex](https://github.com/bekirdag/docdex)** - ⭐ 12
   A document index with MCP, http and client support. https://docdex.org/ 

3594. **[KunAvatar](https://github.com/KunLabAI/KunAvatar)** - ⭐ 12
   基于ollama推理框架本地部署的Agent应用，实现MCP工具调用，短长期记忆等功能。||  A locally deployed agent application built on the Ollama, featuring MCP tool integration along with both short-term and long-term memory support.

3595. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 12
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

3596. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 12
   MCP server for accessing VS Code/Cursor's Local History

3597. **[opentrace](https://github.com/adham90/opentrace)** - ⭐ 12
   Self-hosted observability server with 75+ MCP tools. Ingest logs, connect Postgres, monitor servers — then debug it all from Claude, Cursor, or any MCP client.

3598. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 12
   Anthropic MCP server for .faf — 33 tools, IANA-registered format. npm: claude-faf-mcp. MCP Registry #2759

3599. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 12
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

3600. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 12
   Connecting AI agent to biomedical data

3601. **[ue5-mcp-bridge](https://github.com/Natfii/ue5-mcp-bridge)** - ⭐ 12
   MCP server bridging AI assistants to Unreal Engine 5 editor

3602. **[nodebench-ai](https://github.com/HomenShum/nodebench-ai)** - ⭐ 12
   NodeBench MCP - 260-tool Model Context Protocol server with progressive discovery, agent-as-a-graph embeddings, research optimization, and adaptive web scraping. Monorepo: MCP server + Convex backend + React frontend.

3603. **[mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** - ⭐ 12
   WooCommerce MCP Server — WordPress community plugin implementing the Model Context Protocol (MCP) for WooCommerce. Supports STDIO and HTTP streamable transport, with optional JWT authentication. Based on Automattic’s official WordPress MCP.  This plugin is not affiliated with Automattic.

3604. **[asap-protocol](https://github.com/adriannoes/asap-protocol)** - ⭐ 12
   Standard protocol for agent-to-agent communication with stateful orchestration, MCP-compatible and a public marketplace to discover and register agents.

3605. **[ai-mate](https://github.com/symfony/ai-mate)** - ⭐ 12
   AI development assistant MCP server for Symfony projects

3606. **[drf-mcp-docs](https://github.com/Abdulkhalek-1/drf-mcp-docs)** - ⭐ 12
   API documentation via MCP for AI coding agents

3607. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 11
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

3608. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 11
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

3609. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

3610. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

3611. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 11
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

3612. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

3613. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

3614. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

3615. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

3616. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

3617. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

3618. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 11
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

3619. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

3620. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

3621. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

3622. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

3623. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

3624. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 11
   MCP for Scorable Evaluation Platform

3625. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

3626. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

3627. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 11
   Documentation

3628. **[polaris](https://github.com/octu0/polaris)** - ⭐ 11
   Distributed AI Agent Framework

3629. **[glm5-mcp](https://github.com/Arkya-AI/glm5-mcp)** - ⭐ 11
   Reduce Claude Desktop consumption by 10x - Integrate Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

3630. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 11
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

3631. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 11
   Example Spring AI Model Context Protocol (MCP)

3632. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 11
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

3633. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 11
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

3634. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 11
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

3635. **[ProxmoxMCP-advance](https://github.com/Markermav/ProxmoxMCP-advance)** - ⭐ 11
   ProxmoxMCP (advance): MCP for Proxmox integration in Claude, Goose, Cline, any client.

3636. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 11
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

3637. **[robotmcp_client](https://github.com/robotmcp/robotmcp_client)** - ⭐ 11
   Connect AI models like Claude & GPT with robots using MCP and ROS.

3638. **[plumcp](https://github.com/plumce/plumcp)** - ⭐ 11
   Clojure/ClojureScript library for making MCP server and client

3639. **[claude-qdrant-mcp](https://github.com/marlian/claude-qdrant-mcp)** - ⭐ 11
   Local-first TypeScript MCP server for Qdrant with client isolation, LM Studio integration, and scalable document workflows.

3640. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 11
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

3641. **[gtm-mcp](https://github.com/pouyanafisi/gtm-mcp)** - ⭐ 11
   MCP server for Google Tag Manager: read tags/triggers/variables, publish containers, and audit changes via Claude/Gemini.

3642. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 11
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

3643. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 11
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

3644. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 11
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

3645. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 11
   DataAnalysis Agent using LangGraph & MCP server and client

3646. **[mcp-coroot](https://github.com/jamesbrink/mcp-coroot)** - ⭐ 11
   MCP server for Coroot observability platform - integrate monitoring, troubleshooting, and configuration tools with AI agents

3647. **[bookmark-manager-mcp](https://github.com/infinitepi-io/bookmark-manager-mcp)** - ⭐ 11
   A lightweight Model Context Protocol (MCP) server that provides persistent bookmark management for Claude and other MCP-compatible clients. Features categorized storage, resource discovery, and seamless integration with your AI workflow.

3648. **[chromadb-remote-mcp](https://github.com/meloncafe/chromadb-remote-mcp)** - ⭐ 11
   Remote MCP server for ChromaDB

3649. **[Hoofy](https://github.com/HendryAvila/Hoofy)** - ⭐ 11
   Hoofy — AI development companion MCP server. Persistent memory, spec-driven development, adaptive change pipeline, Clarity Gate. 32 tools, single Go binary, zero deps.

3650. **[webclaw](https://github.com/kuroko1t/webclaw)** - ⭐ 11
   A WebMCP-native browser agent that runs inside your real Chrome — control it from Claude, Cursor, and any MCP client

3651. **[msty-admin-mcp](https://github.com/M-Pineapple/msty-admin-mcp)** - ⭐ 11
   AI-powered administration for Msty Studio Desktop. 24 MCP tools for database insights, config sync, local model orchestration, and Claude handoff workflows.

3652. **[miro-mcp-server](https://github.com/olgasafonova/miro-mcp-server)** - ⭐ 11
   MCP server for controlling Miro whiteboards with AI assistants

3653. **[lm](https://github.com/houtini-ai/lm)** - ⭐ 11
   Offload Tasks from Claude to your Local LLM With Houtini-LM - uses OpenAPI for LM Studio and Ollama Compatibility. Save tokens by offloading some grunt work for your API - our tool description helps claude decide what work to assign and why.

3654. **[qurio](https://github.com/irahardianto/qurio)** - ⭐ 11
   Self-hosted RAG engine for AI coding assistants. Ingests technical docs & code repositories locally with structure-aware chunking. Serves grounded context via MCP to prevent hallucinations in software development workflows.

3655. **[ue5-mcp](https://github.com/mirno-ehf/ue5-mcp)** - ⭐ 11
   Let AI edit your Unreal Engine Blueprints. MCP server plugin for Claude Code — describe what you want in plain English.

3656. **[sift-gateway](https://github.com/lourencomaciel/sift-gateway)** - ⭐ 11
   Reliability gateway for AI tool output: schema-stable, secret-safe, pagination-complete JSON for MCP and CLI agents.

3657. **[kroki-mcp](https://github.com/utain/kroki-mcp)** - ⭐ 10
   Kroki-MCP is a Go-based Model Context Protocol tool that converts textual diagram definitions (PlantUML, Mermaid, and more) into images via a Kroki backend. Designed for simplicity and flexibility, it supports both local and remote Kroki servers, offers configurable settings, and outputs multiple formats – making it ideal for developers building AI

3658. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 10
   MCP server to give client the ability to access Wikipedia pages

3659. **[taskboard](https://github.com/tcarac/taskboard)** - ⭐ 10
   Local project management with Kanban UI, CLI, and MCP server for AI assistants. SQLite-backed, single binary, installable via Homebrew.

3660. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

3661. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

3662. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

3663. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

3664. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

3665. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 10
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

3666. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

3667. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 10
   A TUI to probe the calls between MCP client and server

3668. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

3669. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 10
   Simple template project for controlling Unity via MCP

3670. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

3671. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 10
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

3672. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3673. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

3674. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

3675. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

3676. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

3677. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

3678. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

3679. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

3680. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

3681. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

3682. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

3683. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault 

3684. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

3685. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

3686. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

3687. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

3688. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

3689. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

3690. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

3691. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

3692. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 10
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

3693. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

3694. **[Simple_MCP_Client](https://github.com/Avento/Simple_MCP_Client)** - ⭐ 10
   Simple MCP Client for OpenAI/Deepseek R1/V3

3695. **[awesome-mcp](https://github.com/gauravfs-14/awesome-mcp)** - ⭐ 10
   A carefully curated collection of high-quality tools, libraries, research papers, projects, and tutorials centered around Model Context Protocol (MCP) — a novel paradigm designed to enable modular, adaptive coordination between large language models (LLMs) and external tools or data contexts.

3696. **[openapi-mcp-swagger](https://github.com/salacoste/openapi-mcp-swagger)** - ⭐ 10
   Solve AI context window limits for API docs | Convert any Swagger/OpenAPI to searchable MCP server | AI-powered endpoint discovery & code generation | Works with Cursor, Claude, VS Code

3697. **[mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig)** - ⭐ 10
   A local MCP server that breaks on demand. Test your client against auth failures, disappearing tools, flaky responses, and token expiry, all from a web UI.

3698. **[notification-mcp](https://github.com/pinkpixel-dev/notification-mcp)** - ⭐ 10
   A Model Context Protocol server that allows AI agents to play a notification sound via a tool when a task is completed.

3699. **[adonis-mcp](https://github.com/7nohe/adonis-mcp)** - ⭐ 10
   An AdonisJS package for building remote MCP servers

3700. **[webmcp-sh](https://github.com/WebMCP-org/webmcp-sh)** - ⭐ 10
   A modern web-based Model Context Protocol (MCP) playground for testing and developing MCP servers and clients

3701. **[genkit-mcp-client-blender](https://github.com/xprilion/genkit-mcp-client-blender)** - ⭐ 10
   An MCP Client for interfacing with the Blender MCP Server built with Firebase Genkit and Gemini

3702. **[esp32-mcpserver](https://github.com/solnera/esp32-mcpserver)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server framework for ESP32. Seamlessly connect embedded devices to LLMs.

3703. **[youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server providing real-time YouTube Data API access for AI assistants. Features 14 functions including intelligent content evaluation with technology freshness scoring for knowledge base curation.

3704. **[Azure-Foundry-Webinar](https://github.com/ShivamGoyal03/Azure-Foundry-Webinar)** - ⭐ 10
   This repository is the official companion for the Azure AI Foundry Agent Service Webinar Series. It provides hands-on code samples, modular use cases, and practical guides for building, deploying, and scaling AI agents on Azure.

3705. **[Cognio](https://github.com/0xReLogic/Cognio)** - ⭐ 10
   Persistent semantic memory server for MCP - Give your AI long-term memory that survives across conversations. Lightweight Python server with SQLite storage and semantic search.

3706. **[bruno-mcp](https://github.com/macarthy/bruno-mcp)** - ⭐ 10
   🚀 MCP server for generating Bruno API testing files programmatically. Create collections, environments, requests, and test scripts using AI clients like Claude Desktop.

3707. **[systemprompt-template](https://github.com/systempromptio/systemprompt-template)** - ⭐ 10
   Production AI agent mesh in 3 commands. MCP servers, playbooks, and multi-agent orchestration built on systemprompt-core.

3708. **[cheatengine-mcp-bridge](https://github.com/beamstar/cheatengine-mcp-bridge)** - ⭐ 10
   🔗 Connect AI to Cheat Engine for fast memory analysis, enabling quick mods and audits without the tedious manual work.

3709. **[toolhive-cloud-ui](https://github.com/stacklok/toolhive-cloud-ui)** - ⭐ 10
   ToolHive Cloud UI surfaces MCP servers running in your infrastructure, highlighting metadata, tool capabilities, and copy-ready endpoints for fast AI agent integrations.

3710. **[Rube](https://github.com/dorucioclea/Rube)** - ⭐ 10
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

3711. **[keycloak-mcp](https://github.com/HaithamOumerzoug/keycloak-mcp)** - ⭐ 10
   MCP server that integrates with Keycloak, allowing you to manage Keycloak users and realms through a standardized protocol. It uses the official Keycloak Admin Client to interact with Keycloak's API.

3712. **[java-xiaohongshu-mcp](https://github.com/bzlrj/java-xiaohongshu-mcp)** - ⭐ 10
   Java 实现的小红书 Model Context Protocol (MCP) 工具服务  为 AI Agent / MCP Client 提供标准化接口，实现： 登录、发图文、发视频、搜索、评论、推荐内容、用户主页 等核心功能

3713. **[mcpd](https://github.com/pouriya/mcpd)** - ⭐ 10
   A ~3MB MCP daemon that exposes any script as a tool for Claude, Cursor & AI assistants

3714. **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** - ⭐ 10
   Extended WhatsApp MCP server with 41 tools - reactions, group management, polls, presence, newsletters & more. Fork of lharries/whatsapp-mcp

3715. **[chessmata](https://github.com/jonradoff/chessmata)** - ⭐ 10
   Chessmata: chess game for humans and AI agents

3716. **[storybook-mcp-server](https://github.com/stefanoamorelli/storybook-mcp-server)** - ⭐ 10
   MCP server for Storybook - provides AI assistants access to components, stories, properties and screenshots. Built with TypeScript and Model Context Protocol SDK.

3717. **[dbt-core-mcp](https://github.com/NiclasOlofsson/dbt-core-mcp)** - ⭐ 10
   dbt Core MCP Server: Interact with dbt projects via Model Context Protocol

3718. **[chatgpt2md](https://github.com/NextStat/chatgpt2md)** - ⭐ 10
   Convert ChatGPT export to Markdown with full-text search and MCP server for Claude

3719. **[mini_claude](https://github.com/20alexl/mini_claude)** - ⭐ 10
   Give Claude Code persistent memory across sessions. Track habits, log mistakes, prevent death spirals. Runs locally with Ollama.

3720. **[statelessagent](https://github.com/sgx-labs/statelessagent)** - ⭐ 10
   Your AI forgets everything between sessions. SAME fixes that. Local-first, no API keys, single binary.

3721. **[MCP-Penetration-testing](https://github.com/Mr-Infect/MCP-Penetration-testing)** - ⭐ 10
   The ultimate OWASP MCP Top 10 security checklist and pentesting framework for Model Context Protocol (MCP), AI agents, and LLM-powered systems.

3722. **[caltrain-mcp](https://github.com/davidyen1124/caltrain-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for Caltrain schedules. Get real-time train departures using GTFS data, designed for Claude Desktop and other MCP clients.

3723. **[shellguard](https://github.com/fawdyinc/shellguard)** - ⭐ 10
   MCP server that gives LLM agents read-only shell access over SSH

3724. **[PsMCP-MCP-Server-for-Photoshop](https://github.com/Chandrahas455/PsMCP-MCP-Server-for-Photoshop)** - ⭐ 10
   An Extensive MCP server and a Gradio MCP client ( with Gemini ) with several tools made using win32com to intereact with Photoshop. Designing with Photoshop has never been more fun!

3725. **[fathom-mcp](https://github.com/Dot-Fun/fathom-mcp)** - ⭐ 10
   Model Context Protocol server for Fathom AI - access meeting recordings, transcripts, summaries, teams, and webhooks

3726. **[wamcp](https://github.com/delltrak/wamcp)** - ⭐ 10
   WhatsApp MCP Server — Connect AI agents to WhatsApp via Model Context Protocol. 61 tools, 10 resources, 12 real-time events. Supports Baileys (WhatsApp Web) and Cloud API. Built with TypeScript, BullMQ, and Docker.

3727. **[ollama-mcp-example](https://github.com/kirillsaidov/ollama-mcp-example)** - ⭐ 10
   Ollama MCP example for dummies. 

3728. **[civitai-mcp-server](https://github.com/Cicatriiz/civitai-mcp-server)** - ⭐ 10
   A Model Context Protocol server for browsing and discovering AI models on Civitai

3729. **[openapi-to-mcp](https://github.com/agentic-community/openapi-to-mcp)** - ⭐ 10
   Transform OpenAPI specifications into production-ready MCP servers   with AI-powered evaluation and enhancement. Leverages LLMs to   analyze, improve, and generate Model Context Protocol   implementations from your existing API documentation.

3730. **[world-intel-mcp](https://github.com/marc-shade/world-intel-mcp)** - ⭐ 10
   100+ tool MCP server for real-time global intelligence — markets, FX, bonds, earnings, SEC filings, conflict, military, cyber, climate, news, company enrichment, and 30+ domains. Live Leaflet dashboard with 20 map layers, SSE streaming, and AI situation briefs.

3731. **[ILSpy-Mcp](https://github.com/bivex/ILSpy-Mcp)** - ⭐ 10
   🔓 UNLEASH ILSpy'S POWER. Reverse-engineer DOTNET code at GOD SPEED. AI-assisted debugging that THINKS with you. Decompile ANYTHING. 🚀

3732. **[overleaf-mcp-server](https://github.com/YounesBensafia/overleaf-mcp-server)** - ⭐ 10
   MCP server for Overleaf projects. Syncs LaTeX files via Git, parses sections, equations, and citations, and exposes them to AI clients for assisted paper review, LaTeX fixes, and content generation.

3733. **[openalex-research-mcp](https://github.com/oksure/openalex-research-mcp)** - ⭐ 10
   MCP server for the OpenAlex API — search 240M+ scholarly works, analyze citations, track research trends, and map collaboration networks

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 42,075
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

2. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 9,480
   ValueCell is a community-driven, multi-agent platform for financial applications.

3. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,557
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

4. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,884
   面向企业级市场的一站式AI应用开发框架，支持多厂商大模型统一接入与管理，具备安全可控的企业知识库与高精度检索优化能力，提供可视化流程编排、自主决策智能体与多智能体协同调度，兼容主流 Agent Skill 协议，同时支持微信生态扩展，帮助企业与开发者零门槛快速构建安全、高效、可落地的AI智能体应用与行业解决方案。

5. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,786
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

6. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,339
   extendable code review and QA agent 🚢

7. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,642

8. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,629
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

9. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 878
   OpenTelemetry Instrumentation for AI Observability

10. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 815
   A code repository indexing tool to supercharge your LLM experience.

11. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 713
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

12. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 580
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

13. **[comunica](https://github.com/comunica/comunica)** - ⭐ 547
   📬 A knowledge graph querying framework for JavaScript

14. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 532
   The easiest way to discover and install MCPs

15. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 464
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

16. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 357
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

17. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 164
   Python SDK for interacting with the MCP Toolbox for Databases. 

18. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 155
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

19. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

20. **[ai](https://github.com/WordPress/ai)** - ⭐ 152
   Demonstrate and deliver AI features by combining all AI Building Blocks into a unified WordPress experience.

21. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 109
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

22. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

23. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 96
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

24. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 95
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

25. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 80
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

26. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 70
   Javascript SDK for interacting with the MCP Toolbox for Databases.

27. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

28. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 54

29. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

30. **[askimo](https://github.com/haiphucnguyen/askimo)** - ⭐ 45
   AI Native App Client App with Built-in Knowledge Base & Multi-Provider Support (OpenAI, Gemini, Ollama,  ...)

31. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 44
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

32. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

33. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

34. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

35. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 27
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

36. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

37. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

38. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

39. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

40. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 21
   Powered by Ray (video) and Photon (image) models by Luma AI

41. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 18
   A desktop client with MCP support for Mistral LLMs

42. **[pic-standard](https://github.com/madeinplutofabio/pic-standard)** - ⭐ 14
   The industry standard for Provenance & Intent Contracts (PIC) in Agentic AI. Bridging the Causal Gap in autonomous systems.

43. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

44. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

45. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 10

46. **[ArcaMCP](https://github.com/Yoryoboy/ArcaMCP)** - ⭐ 10
   Servidor MCP para AFIP/ARCA: automatiza certificados, autorización de Web Services, emisión/consulta de comprobantes y generación de PDF con QR.

47. **[Reversal](https://github.com/RinoRika/Reversal)** - ⭐ 10
   A PVP Client Based on Minecraft MCP 1.8.9

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 178,410
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,911
   🦍 The API and AI Gateway

3. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,660
   Query Engine for AI Analytics: Build self-reasoning agents across all your live data

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 27,326
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,511
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,378
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 16,006
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

9. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

10. **[kubeshark](https://github.com/kubeshark/kubeshark)** - ⭐ 11,818
   Cluster-wide network observability for Kubernetes. Captures L4 packets, L7 API calls, and decrypted TLS traffic using eBPF, with full Kubernetes context. Available to AI agents via MCP and human operators via dashboard.

11. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,751
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 11,028
   A cross-platform Markdown AI note-taking software.

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 11,008
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

14. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 9,984
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

15. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 8,881
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

16. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,875
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

17. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,809
   Agent Framework For Fintech and Banks

18. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,656
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

19. **[adk-go](https://github.com/google/adk-go)** - ⭐ 7,118
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,986
   Adversary simulation and Red teaming platform with AI

21. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,486
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

22. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,481
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,262
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,241
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

25. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,238
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

26. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,064
   Bulk port forwarding Kubernetes services for local development.

27. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,309
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

28. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 3,307
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

29. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,734
   A highly opinionated, zero-configuration linter and formatter.

30. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,711
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

31. **[harbor](https://github.com/av/harbor)** - ⭐ 2,491
   One command brings a complete pre-wired LLM stack with hundreds of services to explore.

32. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 2,038
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

33. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,905
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

34. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,718
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

35. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,583
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

36. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,503
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

37. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,469
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

38. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,408
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

39. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

40. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

41. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,298
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

42. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

43. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,183
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

44. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,140
   Build, evaluate and train General Multi-Agent Assistance with ease

45. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,115
   A single interface to use and evaluate different agent frameworks 

46. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 1,110
   Local first codebase intelligence

47. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,095
   Korea Investment & Securities Open API Github

48. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,085
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

49. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,060
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

50. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 1,003
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

51. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 971
   Arduino MCP2515 CAN interface library

52. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 878
   Natural (2-way) voice conversations with Claude Code

53. **[rulesync](https://github.com/dyoshikawa/rulesync)** - ⭐ 864
   A Utility CLI for AI Coding Agents

54. **[DataDesigner](https://github.com/NVIDIA-NeMo/DataDesigner)** - ⭐ 784
   🎨 NeMo Data Designer: A general library for generating high-quality synthetic data from scratch or based on seed data.

55. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 773
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

56. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 738
   Solidity Static Analyzer that easily integrates into your editor

57. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 737
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

58. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 732
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

59. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 730
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

60. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 707
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

61. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 694
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

62. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 676
   A personal AI assistant for everyone

63. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 671
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

64. **[weave](https://github.com/Ataraxy-Labs/weave)** - ⭐ 653
   Entity-level semantic merge driver for Git. Resolves conflicts that git can't by understanding code structure via tree-sitter. 31/31 clean merges vs git's 15/31.

65. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 651
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

66. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 646
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

67. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 595
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

68. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 582
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

69. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 567
   UI components for AI interfaces

70. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 526
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

71. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 525
   Marmot helps teams discover, understand, and leverage their data with powerful search and lineage visualisation tools. It's designed to make data accessible for everyone.

72. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 513
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

73. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 468
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

74. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

75. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 431
   Python Deep Agent framework built on top of Pydantic-AI, designed to help you quickly build production-grade autonomous AI agents with planning, filesystem operations, subagent delegation, skills, and structured outputs—in just 10 lines of code.

76. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

77. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 420
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

78. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 398
   本项目基于React+TypeScript+Hono+ SQLite3实现，实现Google、Github授权登录，已接入OpenAI SDK、MCP服务和Agent相关大模型，扩展实时黄金和K线图，获取Hugging Face论文，以及文生图服务(无需再代理和APIKey)，同时支持腾讯视频、爱奇艺、优酷、芒果TV、哔哩哔哩、网易云音乐等平台会员视频破解可在线解析、动漫漫画畅享阅读、思维导图、论文降重、闲鱼自动发货回复等操作管理和AI像素办公室监工（适配PC端、移动端）

79. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 396
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

80. **[bridle](https://github.com/neiii/bridle)** - ⭐ 392
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

81. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 389
   Minecraft: Pi Edition API Python Library

82. **[volcano-agent-sdk](https://github.com/Kong/volcano-agent-sdk)** - ⭐ 388
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

83. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

84. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 382
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

85. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

86. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 370
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

87. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 365
   Python toolkit for building graph-enhanced GenAI applications

88. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 362
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

89. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 360
   MCP for Unreal Engine 5

90. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 345
   Blender python addon to increase workflow for creating minecraft renders and animations

91. **[exograph](https://github.com/exograph/exograph)** - ⭐ 343
   Build production-ready backends in minutes

92. **[depyler](https://github.com/paiml/depyler)** - ⭐ 338
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

93. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 335
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

94. **[vocotype-cli](https://github.com/233stone/vocotype-cli)** - ⭐ 323
   VocoType 是一款运行在本地端侧的隐私安全语音输入工具，通过快捷键即可将语音实时转换为文字并自动输入到当前应用。支持语音转文字MCP、AI 优化文本、自定义替换词典、录音视频转文字等功能，让语音输入更高效、更安全。

95. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

96. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 313
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

97. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

98. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 296
   Software architecture tooling for the AI age

99. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 296
   An in-depth book and reference on building agentic systems like Claude Code

100. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 276
   AI for Ethical Hacking - Workshop

101. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

102. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 246
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

103. **[agentica](https://github.com/shibing624/agentica)** - ⭐ 246
   Agentica: Lightweight async-first Python framework for AI agents. 轻量级异步优先的AI Agent框架，支持工具调用、RAG、多智能体和MCP。

104. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 245
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

105. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 244
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

106. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 240
   Public facing repo for MCP SRG mappings.

107. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 236
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

108. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 233
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

109. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

110. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

111. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 219
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

112. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

113. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 216
   小红书创作中心

114. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

115. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

116. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

117. **[weam](https://github.com/weam-ai/weam)** - ⭐ 207
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

118. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 205
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

119. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 202
   Re-usable multi part components built on React Aria and TailwindCSS. 

120. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 202
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

121. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

122. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 190
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

123. **[ATaC](https://github.com/ATaC-team/ATaC)** - ⭐ 190
   Recording and Replay AI Agent Trajectory.

124. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

125. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 184
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

126. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 172
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

127. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

128. **[talkio](https://github.com/llt22/talkio)** - ⭐ 159
   Local-first multi-AI group chat desktop app — pull gpt, Claude, Gemini, DeepSeek into one conversation. Tauri 2 + React 19.

129. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 156
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

130. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 143
   Seline is a local-first AI desktop application that brings together conversational AI, visual generation tools, vector search, and multi-channel connectivity in one place.

131. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 143
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

132. **[selene](https://github.com/tercumantanumut/selene)** - ⭐ 143
   Selene is a desktop app that runs AI agents on your machine. Connect them to your WhatsApp, Telegram, Slack, or Discord. Write code, generate images, build personal assistants. All from one place. Your data stays on your device.

133. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 140
   ☕ Community-driven Java implementation of TOON

134. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

135. **[machi](https://github.com/qntx/machi)** - ⭐ 139
   A Web4.0-native AI Agent Framework.

136. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

137. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 127
   A curated list of open source repositories for AI Engineers

138. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 126
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

139. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 125
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

140. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 118
   5-Day Gen AI Intensive Course with Google

141. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 115
   Solid Tumor Associative Modeling in Pathology

142. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 114
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

143. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 110
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

144. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 110
   One-click launch URL generator for protocol-based apps

145. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 110
   Scalable and extensible reinforcement learning for LM agents.

146. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 109
   谷歌5天AI Agents强化课程

147. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 106
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

148. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 106
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

149. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 94
   Unity plugin for Coplay

150. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 92
   ai memory for coding

151. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP 

152. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

153. **[open-skills](https://github.com/besoeasy/open-skills)** - ⭐ 78
   Battle-tested skill library for AI agents. Save 98% of API costs with ready-to-use code for crypto, PDFs, search, web scraping & more. No trial-and-error, no expensive APIs.

154. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 77
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

155. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 75
   A lightweight, open, and extensible multi-LLM interaction studio.

156. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 75
   Quarkus Langchain4J Workshop

157. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 74
   OneMCP feature requests, bugs and improvements 

158. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 73
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

159. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 67
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

160. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 64
   MeMesh Plugin — Searchable project memory plugin for Claude Code.

161. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 64
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

162. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 61
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

163. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 60
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

164. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 56
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

165. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 51
   chm to markdown and vectorDB

166. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 50
   Houdini integration through the Model Context Protocol

167. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 48
   Backported Model Context Protocol SDK for Java 8

168. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

169. **[velocity](https://github.com/OptimiLabs/velocity)** - ⭐ 40
   Local-first workspace for Claude Code, Codex CLI, and Gemini CLI with sessions, analytics, workflows, and tools

170. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 37
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

171. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 37
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

172. **[Agience](https://github.com/Agience/Agience)** - ⭐ 36
   MCP-native workspace for turning live work into durable knowledge.

173. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 35
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

174. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 35
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

175. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

176. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 32
   Prompt-driven automation platform - Transform natural language into executable workflows

177. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 30
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

178. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

179. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 28
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

180. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 27
   Build AI Agent using Google ADK , MCP and Gemma 3 model

181. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

182. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

183. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 21
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

184. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

185. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

186. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

187. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 16
   Language to Maps

188. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 15
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

189. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 14
   Multi-agent system for software development

190. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 14
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

191. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

192. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

193. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 12
   Unity MCP Tool template project

194. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

195. **[claude-colony](https://github.com/MakingJamie/claude-colony)** - ⭐ 10
   Multi-agent Claude Code you can actually control. Spawn specialist teams in tmux, watch them work side-by-side, steer when needed. Built on native Claude Code agents. No black boxes.

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,671
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

3. **[claude-mcp-examples](https://github.com/charIesding/claude-mcp-examples)** - ⭐ 151
   examples of claude with mcp integration

4. **[End-to-End-Agentic-Ai-Automation-Lab](https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab)** - ⭐ 50
   This repository contains hands-on projects, code examples, and deployment workflows. Explore multi-agent systems, LangChain, LangGraph, AutoGen, CrewAI, RAG, MCP, automation with n8n, and scalable agent deployment using Docker, AWS, and BentoML.

5. **[claude-mcp](https://github.com/thinkbigcd/claude-mcp)** - ⭐ 16
   claude and mcp integration examples and tutorials

### Documentation

*Documentation, tutorials, and learning resources*

1. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 9,321
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享大模型选择指南（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（RAG / MCP / A2A）、AI 编程教程、AI 工具用法（Cursor / Claude Code / OpenClaw / TRAE / Lovable / Agent Skills）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档版本，已升级为鱼皮 AI 导航网站

2. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 7,439
   Specification and documentation for the Model Context Protocol

3. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,938
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 495
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

5. **[platform-engineering](https://github.com/codetocloudorg/platform-engineering)** - ⭐ 94
   A centralized hub for platform engineering teams, providing resources, best practices, and automation tools. Includes IaC templates, blueprints, and operational guides to help build scalable, secure, and efficient platforms for cloud-native environments and DevSecOps workflows.

6. **[pew-pew-plaza-packs](https://github.com/appboypov/pew-pew-plaza-packs)** - ⭐ 83
   AI-powered project management framework based on an opinionated view on effective prompts and a highly modular approach to building effective agents, workflows, templates, prompts and context documents.

7. **[forksilly.doc](https://github.com/fatsnk/forksilly.doc)** - ⭐ 75
   Documents repo of ForkSilly. ForkSilly：兼容sillytavern（酒馆）角色卡、世界书、正则、预设、聊天记录的安卓移动端应用；同时也可作为stable diffusion客户端使用。

8. **[Agent-Fusion](https://github.com/krokozyab/Agent-Fusion)** - ⭐ 57
    Agent Fusion is a local RAG semantic search engine that gives AI agents instant access to your code, documentation (Markdown, Word, PDF). Query    your codebase from code agents without hallucinations. Runs 100% locally, includes a lightweight embedding model, and optional multi-agent task    orchestration. Deploy with a single JAR

9. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 27
    A powerful system for crawling documentation websites, extracting code snippets, and providing fast search capabilities via MCP (Model Context Protocol) integration.

10. **[Q4_learning](https://github.com/DanielHashmi/Q4_learning)** - ⭐ 15
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

