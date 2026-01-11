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

## 📚 Projects (2672 total)

> Last updated: **2026-01-11**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 125,414
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 120,212
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 90,434
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 78,575
   A collection of MCP servers.

5. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,300
   The fastest path to AI-powered full stack observability, even for lean teams.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 75,915
   Model Context Protocol Servers

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 71,218
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 69,987
   🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers, Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.

9. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 53,120
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

10. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 44,973
   🔥AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

11. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 42,726
   🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。 AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测。支持 Docker 一键部署，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。⭐

12. **[context7](https://github.com/upstash/context7)** - ⭐ 41,484
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

13. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,230
   Federated Query Engine for AI - The only MCP Server you'll ever need

14. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

15. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 32,981
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

16. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 32,810
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

17. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,498
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

18. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 31,189
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

19. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,342
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

20. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 25,797
   GitHub's official MCP Server

21. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 25,718
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

22. **[goose](https://github.com/block/goose)** - ⭐ 25,699
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

23. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 25,342
   Playwright MCP server

24. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 24,794
   An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations.

25. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 23,056
   An MCP-based chatbot | 一个基于MCP的聊天机器人

26. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 22,389
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

27. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 21,836
   🚀 The fast, Pythonic way to build MCP servers and clients

28. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 21,118
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

29. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 21,047
   The official Python SDK for Model Context Protocol servers and clients

30. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,285
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

31. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 20,100
   Chrome DevTools for coding agents

32. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 19,784
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

33. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 19,232
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

34. **[serena](https://github.com/oraios/serena)** - ⭐ 18,441
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

35. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,088
   Your API ⇒ Paid MCP. Instantly.

36. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 14,904

37. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 14,009
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

38. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,383
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

39. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,258
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

40. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 12,899
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

41. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 12,469
   MCP server to provide Figma layout information to AI coding agents like Cursor

42. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 12,368
   MCP Toolbox for Databases is an open source MCP server for databases.

43. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 11,521
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

44. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,354
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

45. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 11,349
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

46. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,269
   The official TypeScript SDK for Model Context Protocol servers and clients

47. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 10,789
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

48. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 10,428
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex & Gemini CLI.

49. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,374
   Yet another WebUI for Nginx

50. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,242
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

51. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

52. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 9,869
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

53. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 9,708
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书无水印作品文件

54. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 8,882
   mcp-use is the easiest way to interact with mcp servers with custom agents

55. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,703
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

56. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 8,437
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

57. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,235
   Visual testing tool for MCP servers

58. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,219
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

59. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 7,960
   MCP for xiaohongshu.com

60. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 7,956
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

61. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 7,926
   Build effective agents using Model Context Protocol and simple workflow patterns

62. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 7,832
   AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.

63. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,353
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

64. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

65. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,252
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

66. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 7,039
   MCP Server for Ghidra

67. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 6,968
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

68. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 6,405
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

69. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,241
   A community driven registry service for Model Context Protocol (MCP) servers.

70. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,175
   A collection of MCP clients.

71. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 5,874
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

72. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 5,838
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

73. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 5,594
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

74. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,585
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

75. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,526
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

76. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,403
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

77. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,238
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

78. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,212
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

79. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,190
   WhatsApp MCP server

80. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,132
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

81. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,054
   Awesome MCP Servers - A curated list of Model Context Protocol servers

82. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,007
   Install, run and deploy your own decentralized AI agent service

83. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,000
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

84. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 4,962
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

85. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 4,952
   A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

86. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 4,934
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

87. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 4,850
   A model-driven approach to building AI agents in just a few lines of code.

88. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 4,777
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

89. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 4,732
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

90. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,694
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

91. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,531
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

92. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,382
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

93. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,346
   opensource self-hosted sandboxes for ai agents

94. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,305
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

95. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 4,283
   Memory infrastructure for LLMs and AI agents

96. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,238
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

97. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,100
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

98. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 3,999
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

99. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 3,935
   MCP server for Atlassian tools (Confluence, Jira)

100. **[Olares](https://github.com/beclab/Olares)** - ⭐ 3,892
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

101. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 3,885
   MCP Server for Computer Use in Windows

102. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,870
   The Cursor & Windsurf community, find rules and MCPs

103. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,858
   A simple, secure MCP-to-OpenAPI proxy server

104. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,816
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

105. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,769
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

106. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,750
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

107. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,687
   Official Notion MCP Server

108. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,672
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

109. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,671
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

110. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,608
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

111. **[core](https://github.com/opensumi/core)** - ⭐ 3,589
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

112. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,589
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

113. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 3,582
   A Model Context Protocol (MCP) server that provides Xcode-related tools for integration with AI assistants and other MCP clients.

114. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,580
   Define, Prompt and Test MCP enabled Agents and Workflows

115. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,523
   Exa MCP for web search and web crawling!

116. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,508
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

117. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,490
   🤖 A visualization mcp contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

118. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,466
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

119. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,436
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

120. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,416
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

121. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 3,349
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno) —or use via CLI, REST API, or MCP server.

122. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,345
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP. Built with Golang for efficient memory use. 

123. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,314
   A curated list of Model Context Protocol (MCP) servers

124. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,293
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

125. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,273

126. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,259
   LangChain 🔌 MCP

127. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,252
   Model Context Protocol(MCP) 编程极速入门

128. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,200
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

129. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,118
   An Autonomous Agentic Framework for Reflective PowerPoint Generation

130. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,108
   A Model Context Protocol server for Excel file manipulation

131. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,088
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

132. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,080
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

133. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,075
   Learn AI and LLMs from scratch using free resources

134. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,054
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

135. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,045
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

136. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 3,032
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

137. **[boost](https://github.com/laravel/boost)** - ⭐ 3,030
   Laravel-focused MCP server for augmenting your AI powered local development experience.

138. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,024
   Allow LLMs to control a browser with Browserbase and Stagehand

139. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,005
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

140. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 2,970
   Master Claude Code with this Guide! Includes: Setup, SKILL.md files, Agents, Commands, workflows and tricks making Claude's potential skyrocket!

141. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,952
   n8n custom node for MCP

142. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,945
   AI agent microservice

143. **[mcp](https://github.com/google/mcp)** - ⭐ 2,898
   Google 💚 MCP

144. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,869
   A TypeScript framework for building MCP servers.

145. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 2,866
   RikkaHub is an Android APP that supports for multiple LLM providers.

146. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,812
   The official Rust SDK for the Model Context Protocol

147. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,755
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

148. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 2,696
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

149. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,673
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

150. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,588
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

151. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

152. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,525
   A CLI tool for building Go applications.

153. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 2,414
   UltraRAG v2: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

154. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,407
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

155. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,376
   Connect Supabase to your AI assistants

156. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,356
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

157. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,344
   A Model Context Protocol server for converting almost anything to Markdown

158. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,332
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

159. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,205
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code

160. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,197
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

161. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,159
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

162. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,146
   A bridge between Streamable HTTP and stdio MCP transports

163. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,124

164. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,101
   MCP server for Grafana

165. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

166. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,070
   DDGS | Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services

167. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,061
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

168. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,035
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi, GLM, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

169. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,025
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

170. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,024
   A Model Context Protocol server for searching and analyzing arXiv papers

171. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,003
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

172. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 1,992
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

173. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 1,988
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

174. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 1,973
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

175. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,970
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

176. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 1,963
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

177. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,956
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

178. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,954
   directory for Awesome MCP Servers

179. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 1,891
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

180. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 1,879
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

181. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,878
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

182. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 1,877
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

183. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,873
   The official MCP server implementation for the Perplexity API Platform

184. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,825
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

185. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,820
   Witsy: desktop AI assistant / universal MCP client

186. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,807
   A secure low code honeypot framework, leveraging AI for System Virtualization.

187. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,801

188. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,800
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

189. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,799
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

190. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,781
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

191. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,750
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

192. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,705
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

193. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,697
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

194. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,688
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

195. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,675
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

196. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,652
   Interactive User Feedback MCP

197. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 1,638
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

198. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,635
   Desktop Extensions: One-click local MCP server installation in desktop apps

199. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,616
   Make RSS 📰 great again with AI 🧠✨!!

200. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,592
   Coding assistant MCP for Claude Desktop

201. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,585
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

202. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

203. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,562
   Local inspector for ChatGPT apps & MCP servers

204. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,550
   Next Generation Agentic Proxy for AI Agents and MCP servers

205. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,548
   ⭐ All-in-one AI Companion! AI Desktop Girlfriend + AI Virtual Streamer + AI Social App Bot + AI Browser + AI Smart Home + AI Gaming — and every feature you can imagine!⭐全能型AI伴侣！AI桌面女友 + AI虚拟主播 + AI社交APP机器人 + AI浏览器 + AI智能家居 + AI游戏 等你能想到的一切功能！

206. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,537
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

207. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,537
   MCP server that provides tools and resources for interacting with n8n API

208. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,535
   A Unified MCP Server Management App (MCP Manager).

209. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,518
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

210. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,514
   ToolHive makes deploying MCP servers easy, secure and fun

211. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,511
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

212. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,492
   An MCP server that installs other MCP servers for you

213. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 1,492
   The better playwright MCP: works as a browser extension. No context bloat. More capable.

214. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,442
   Standards for building agents, better

215. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,435
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

216. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,434
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

217. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,427
   MCP server for interacting with the iOS simulator

218. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,399
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

219. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,397
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

220. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,396
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

221. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,385
   Constrain, log and scan your MCP connections for security vulnerabilities.

222. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,385
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

223. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,385
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

224. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,378
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

225. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,375
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

226. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,359
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

227. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,351
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

228. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,315
   The Simple Agent Development Kit.

229. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,297
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

230. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,271
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

231. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,270
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

232. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,270
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

233. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,269
   Make your own story. User-friendly software for LLM roleplaying

234. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,268
   A connector for Claude Desktop to read and search an Obsidian vault.

235. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,268
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

236. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,254
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

237. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,251
   MCP Server for kubernetes management commands

238. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,246
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

239. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,238
   Damn Vulnerable MCP Server

240. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,233
   An MCP server that autonomously evaluates web applications. 

241. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

242. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

243. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,213
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

244. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,211
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

245. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,210
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

246. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,208
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

247. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,202

248. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,200
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

249. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,200
   The Grafbase GraphQL Federation Gateway

250. **[ai](https://github.com/stripe/ai)** - ⭐ 1,190
   One-stop shop for building AI-powered products and businesses with Stripe.

251. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,179
   The TypeScript MCP framework

252. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,174
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

253. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,172
   The official Swift SDK for Model Context Protocol servers and clients.

254. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,161
   The AI toolkit for the AI developer

255. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,158
   An official Qdrant Model Context Protocol (MCP) server implementation

256. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,157
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

257. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,143
   The official ElevenLabs MCP server

258. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 1,143
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

259. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,141
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

260. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,141
   告别AI提前终止烦恼，助力AI更加持久

261. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,140
   docker mcp CLI plugin / MCP Gateway

262. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,132
   Stop re-explaining your project to AI every session. Automatic context memory for Claude, VS Code, Cursor, and 13+ AI tools.

263. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,129
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

264. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,116
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

265. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,115
   A Ruby Implementation of the Model Context Protocol

266. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,115
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

267. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,099
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server

268. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 1,096
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

269. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,092
   Build, evaluate and train General Multi-Agent Assistance with ease

270. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,089
   The most powerful MCP Slack Server with no permission requirements, Apps support, multiple transports Stdio and SSE, DMs, Group DMs and smart history fetch logic.

271. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 1,083
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

272. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,077
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

273. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,074

274. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,066
   A web UI for Claude Code agents

275. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,063
   Production ready MCP server with real-time search, extract, map & crawl.

276. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,060
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

277. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,059
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

278. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,056
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

279. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,049
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

280. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,048
   Plugin for JADX to integrate MCP server

281. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,037
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

282. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,030
   Query and Summarize your chat messages.

283. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

284. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,025
   On-premises conversational RAG with configurable containers

285. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,021
   MCP Python Tutorial 

286. **[use-mcp](https://github.com/modelcontextprotocol/use-mcp)** - ⭐ 1,019

287. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,008
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

288. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 995
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

289. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 993
   Claude Code as one-shot MCP server to have an agent in your agent.

290. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 985
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

291. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 979
   Remote MCP Servers

292. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 976
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

293. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 975
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

294. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 973
   The Context Graph Factory for AI. Build, manage, and deploy AI-optimized Context Graphs.

295. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 970
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

296. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 959
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

297. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 956
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

298. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 952
   Bringing the power of MCP to the web

299. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 950
   MCP server for fetch web page content using Playwright headless browser.

300. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 945
   A repository of servers and clients from the Model Context Protocol tutorials

301. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 939
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

302. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 938
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

303. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 938
   Hundreds of Claude Code plugins with embedded AI skills. Learn via interactive Jupyter tutorials.

304. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 920
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

305. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 919
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

306. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 918
   Connect AI models like Claude & GPT with robots using MCP and ROS.

307. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 911
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

308. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

309. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 908
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

310. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 907
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

311. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 906
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

312. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 906
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

313. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 906
   A curated list of Model Context Protocol (MCP) servers 

314. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 901
   Expose llms-txt to IDEs for development

315. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 899
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

316. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 899
   Model Context Protocol for WinDBG

317. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 890
   A framework for writing MCP (Model Context Protocol) servers in Typescript

318. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 890
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

319. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 889
   A middleware to provide an openAI compatible endpoint that can call MCP tools

320. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 887
   MCP server helping models to understand your Vite/Nuxt app better.

321. **[tools](https://github.com/strands-agents/tools)** - ⭐ 884
   A set of tools that gives agents powerful capabilities.

322. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 880
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

323. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 877
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

324. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 876
   MCP integration for Google Calendar to manage events.

325. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 874
   First gitlab mcp for you

326. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 869
   A library for communication with a Minecraft client/server.

327. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 869
   Allow AI to wade through complex OpenAPIs using Simple Language

328. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 868
   A security scanner for your LLM agentic workflows

329. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 868
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

330. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 867
   Neo4j Labs Model Context Protocol servers

331. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 867

332. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 866

333. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 860
   ChatGPT CLI is a versatile tool for interacting with LLMs through OpenAI, Azure, and other popular providers like Perplexity AI and Llama. It supports prompt files, history tracking, and live data injection via MCP (Model Context Protocol), making it ideal for both casual users and developers seeking a powerful, customizable GPT experience.

334. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 855
   A concise list for mcp servers

335. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 853
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

336. **[agents](https://github.com/inkeep/agents)** - ⭐ 846
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

337. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 844

338. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 842
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

339. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 838
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

340. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 837
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

341. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 836
   APIM ❤️ AI - This repo contains experiments on Azure API Management's AI capabilities, integrating with Azure OpenAI, AI Foundry, and much more 🚀 . New workshop experience at https://aka.ms/ai-gateway/workshop

342. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

343. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

344. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 825
   A minimalistic MCP client with a good feature set.

345. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 823
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

346. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 816
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

347. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 815

348. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 813
   Simple, modular, and observable Go framework for backend applications.

349. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 811
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

350. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

351. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 807
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

352. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 807
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

353. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 807
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

354. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 802
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

355. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 800
   OpenAPI Tool Servers

356. **[context-space](https://github.com/context-space/context-space)** - ⭐ 799
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

357. **[server](https://github.com/php-mcp/server)** - ⭐ 799
   Core PHP implementation for the Model Context Protocol (MCP) server

358. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 792
   Browse the web, directly from Cursor etc.

359. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 788
   Self-hosted MCP Gateway and Registry for AI agents

360. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 787
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

361. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 787
   The best way to create, deploy, and share MCP Servers

362. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 775
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

363. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 773
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

364. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 765
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

365. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 764
   一个将ACE(Augment Context Engine) 做成MCP的项目

366. **[Context](https://github.com/indragiek/Context)** - ⭐ 761
   Native macOS client for Model Context Protocol (MCP)

367. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 761
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

368. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 756
   Vibetest MCP - automated QA testing using Browser-Use agents

369. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 756
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

370. **[runno](https://github.com/taybenlor/runno)** - ⭐ 755
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

371. **[vllora](https://github.com/vllora/vllora)** - ⭐ 753
   Debug your AI agents

372. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 752
   Chat with your Kubernetes Cluster using AI tools and IDEs like Claude and Cursor!

373. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 750
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

374. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 748
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

375. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 742
   Scan MCP servers for potential threats & security findings.

376. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 740
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

377. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 739
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

378. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 738
   LLDB MCP Integration + other helpful commands

379. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 733
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

380. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 731
   An MCP server for interacting with the Financial Datasets stock market API.

381. **[wordpress-mcp](https://github.com/Automattic/wordpress-mcp)** - ⭐ 722
   WordPress MCP — This repository will be deprecated as stable releases of mcp-adapter become available. Please use https://github.com/WordPress/mcp-adapter for ongoing development and support.

382. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 719
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

383. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 716
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

384. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 710
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

385. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 709
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

386. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 706
   A secure local sandbox to run LLM-generated code using Apple containers

387. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 704
   All in one vscode plugin for mcp developer

388. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 703
   A MCP server implementation for hyperbrowser

389. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 701
   Build MCP Agents

390. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 696
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

391. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 695
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles and companies, get your recommended jobs, and perform job searches.

392. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 692
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

393. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 686
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

394. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 686
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

395. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 681
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

396. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 678
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

397. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 676
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

398. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 676
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

399. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 675
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

400. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 674
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

401. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 668
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

402. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 667
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

403. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 666
   A flexible HTTP fetching Model Context Protocol server.

404. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 666
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

405. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 665
   MCP server for Docker

406. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 662
   Clojure MCP

407. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 658
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

408. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 658
   A simple CLI to run LLM prompt and implement MCP client.

409. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

410. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 652
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

411. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 645
   Connect ClickHouse to your AI assistants.

412. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 642
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

413. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

414. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 641
   Laravel API for Ai Agents and humans.

415. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 640
   Querying local documents, powered by LLM

416. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 640
   EnrichMCP is a python framework for building data driven MCP servers

417. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 635
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

418. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 634
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

419. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 633
   An MCP server that provides control over Android devices via adb

420. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 632
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

421. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 630
   Shell and coding agent on claude desktop app

422. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 629
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

423. **[mcp](https://github.com/laravel/mcp)** - ⭐ 628
   Rapidly build MCP servers for your Laravel applications.

424. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 624
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

425. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 621
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

426. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 618
   A simple MCP server for Obsidian

427. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 616
   Talk to a Cloudflare Worker from Claude Desktop!

428. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 615
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

429. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 611
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

430. **[samples](https://github.com/strands-agents/samples)** - ⭐ 605
   Agent samples built using the Strands Agents SDK.

431. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 601
   gcloud MCP server

432. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 599
   mem-agent mcp server

433. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 592
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

434. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 592
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

435. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 591
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

436. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 589
   Convert Any OpenAPI V3 API to MCP Server

437. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 589

438. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 588
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

439. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 587

440. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 584
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

441. **[tome](https://github.com/runebookai/tome)** - ⭐ 583
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

442. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 582
   MCP Server For Turkish Legal Databases

443. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 581
   Daydreams is a set of tools for building agents for commerce

444. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 578
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

445. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 574
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

446. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 573
   Dexto is a general-purpose agent harness for building and orchestrating agentic applications.

447. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 567
   LangGraph solution template for MCP

448. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 566
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

449. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 562
   VoiceMode MCP brings natural conversations to Claude Code

450. **[obot](https://github.com/obot-platform/obot)** - ⭐ 558
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

451. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 556
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

452. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 554
   MCP to connect your LLM with Spotify.

453. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 554

454. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 553
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

455. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 548

456. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 547
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

457. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 544
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

458. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 542
   Security scanner for MCP servers

459. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 542
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

460. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 541
   Draw.io Model Context Protocol (MCP) Server

461. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 540
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

462. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 533

463. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 533
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

464. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 533

465. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 533
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

466. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 533
   The .NET library to build AI agents with 25+ built-in connectors.

467. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 531
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

468. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 531
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

469. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 530
   MCP server for interacting with Neon Management API and databases

470. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 530

471. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 526
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

472. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 525
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

473. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 524
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

474. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 524
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

475. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 521

476. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 521
   An Mcp client inside Emacs

477. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 521
   An MCP Multimodal AI Agent with eyes and ears!

478. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 519
   提取抖音无水印视频链接，视频文案，douyin-mcp-server

479. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 518
   An MCP server to query any Postgres database in natural language.

480. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 518
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STEAMABLEHTTP access protocols to deploy MCP。

481. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 518
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

482. **[ethora](https://github.com/dappros/ethora)** - ⭐ 517
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

483. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 517
   A comprehensive collection of Model Context Protocol (MCP) servers

484. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 517
   Open Source Voice Agent Platform

485. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

486. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 513
   A MCP server for Home Assistant

487. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 512
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

488. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 511
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

489. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 510
   MCP server for querying Apple Health data with natural language and SQL

490. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 510
   A Model Context Protocol server for IDA

491. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 507
   MCP server to deploy apps to Cloud Run

492. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

493. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 507
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

494. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 507
   Next.js Development for Coding Agent

495. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 504
   微信读书MCP

496. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 501

497. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 500
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

498. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 499
   A tool that converts OpenAPI specifications to MCP server

499. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 499
   Yes Mcp server in bash

500. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 497

501. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 495
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

502. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 494
   An MCP server for interacting with Sentry via LLMs.

503. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

504. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 492
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

505. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

506. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 491

507. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 488
   MCP Monitoring with eBPF

508. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 488
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

509. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 486
   A Model-Context Protocol Server for YouTube

510. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 485
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

511. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 481
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

512. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 478
   MCP server for document format conversion using pandoc.

513. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 475
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

514. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 475
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, and comprehensive lifecycle management capabilities.

515. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 473
   MCP to allow AI agents to control Unreal

516. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 471
   Aser is a lightweight, self-assembling AI Agent frame.

517. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 470
   MCP Server to interact with Google Gsuite prodcuts

518. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 469
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

519. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 468
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

520. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 467
   Install, manage and develop MCP servers

521. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 466
   "AnyTool: Universal Tool-Use Layer for AI Agents"

522. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 465
   An SDK building Laravel MCP servers

523. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 465
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

524. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 462
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

525. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 461
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

526. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

527. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 460
   LLM + MCP + RAG = Magic

528. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 460
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

529. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 459
   MCP server integration for DaVinci Resolve

530. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 458
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

531. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 455
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

532. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 454
   A MCP (Model Context Protocol) server for interacting with dbt.

533. **[argo](https://github.com/xark-argo/argo)** - ⭐ 452
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

534. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 451
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

535. **[director](https://github.com/director-run/director)** - ⭐ 450
   MCP Playbooks for AI agents

536. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 445
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

537. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 445
   FreeCAD MCP(Model Context Protocol) server

538. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 445
   Govern & Secure your AI

539. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 444
   GitOps on Autopilot Mode

540. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 443
   A docker MCP Server (modelcontextprotocol)

541. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 443

542. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 443
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

543. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 441
   MCP Server for Turkish & American Stock Exchange and Fund Data

544. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 439
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

545. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 439
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

546. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 437
   MCP configuration to connect AI agent to a Linux machine.

547. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 436
   A simple, locally hosted Web Search MCP server for use with Local LLMs

548. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 435
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

549. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 431
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

550. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 424
   Send emails directly from Cursor with this email sending MCP server

551. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 421

552. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 421
   Spec-Driven Development MCP Server, not just Vibe Coding

553. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 421
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

554. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 421
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

555. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 420
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

556. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 420
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

557. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 419
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

558. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 419
   MCP Server for Burp

559. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 419
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

560. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 418
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

561. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 418
   Make your meetings accessible to AI Agents

562. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 418
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

563. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 418
   MCP Server for Metasploit

564. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 417
   im busy building ai agents so why not let an ai talk to my girlfriend? 

565. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 416
   小红书MCP服务 x-s x-t js逆向

566. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 415
   Unlock 650+ MCP servers tools in your favorite agentic framework.

567. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 415
   Enterprise-ready MCP gateway, MCP registry & orchestrator

568. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 411
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

569. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 411
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

570. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 411
   A structural code search engine for Al agents.

571. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 409
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

572. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 409
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

573. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 407
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

574. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 405
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

575. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 405
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

576. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 402
   A CLI inspector for the Model Context Protocol

577. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 402
   This is the official website for TuriX Computer-use-Agent

578. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 401
   基于NET搭建-AI智能体-现代化Saas企业级前后端分离架构-开启智能应用的无限可能：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR验证码识别、API多版本兼容、单元集成测试、RabbitMQ、代码生成器

579. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 401
   The safest way to make REST calls in C# with an MCP Generator

580. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 401
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

581. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 399
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

582. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 397
   MCP server that execute applescript giving you full control of your Mac

583. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 396
   Official Jina AI Remote MCP Server

584. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 394
   An experiment in software planning using MCP

585. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 394
   An MCP extension for Ghidra

586. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 393
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

587. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 393
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

588. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 393
   Official Docker MCP registry 

589. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 390
   MCP server for DuckDB and MotherDuck

590. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 388
   MCP-NixOS - Model Context Protocol Server for NixOS resources

591. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 387
   BioMCP: Biomedical Model Context Protocol

592. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 386
   Memento MCP: A Knowledge Graph Memory System for LLMs

593. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 385
   MCP Server for SearXNG

594. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 384
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

595. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 384
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

596. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 384
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

597. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 384
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

598. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 383
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

599. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 382
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

600. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 382
   A model-driven approach to building AI agents in just a few lines of code. 

601. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 381
   Local Groq Desktop chat app with MCP support

602. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 381
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

603. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 381
   lunar.dev: Agent native MCP Gateway for governance and security

604. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 379
   Baidu Map MCP Server

605. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 378
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

606. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 377
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

607. **[station](https://github.com/cloudshipai/station)** - ⭐ 376
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

608. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 375
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

609. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 374
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

610. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 374
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Cognito integration.

611. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 373
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

612. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 371
   Docfork MCP - Up-to-date Docs for AI Agents.

613. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 370
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

614. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 370
   MCP Server for code graph analysis and visualization by CodeGPT

615. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 369
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

616. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 369
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

617. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 369
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

618. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 368
   Model Context Protocol (MCP) Server for Graphlit Platform

619. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 368
   MCP server connecting to Kubernetes

620. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 368
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

621. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 368
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

622. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 365
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

623. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 363
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

624. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 363
   Making docling agentic through MCP

625. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 361
   Model Context Protocol SDK for PHP

626. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 361
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

627. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 361
   A fully functional MCP server and CLI for YouTube

628. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 360
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

629. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 360
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

630. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 358
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

631. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 357
   Search Airbnb using your AI Agent

632. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 357
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

633. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 357
   Professional Development Environment for Claude Code with Endless Mode, Spec-Driven Development, TDD, LSP, Persistent Memory, Semantic Search, Quality Hooks and Modular Rules 🛠️

634. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 355
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

635. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 355
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs, OpenRouter, Groq, Dashscope & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

636. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 354
   飞书/Lark官方 OpenAPI MCP

637. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 353
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

638. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 352
   MCP server that provides LLMs with tools for interacting with EVM networks

639. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 351
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

640. **[codexia](https://github.com/milisp/codexia)** - ⭐ 351
   A powerfull GUI and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

641. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 350
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的专有领域智能聊天助手

642. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 350
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

643. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 349
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

644. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 348
   Model Context Protocol (MCP) implementation in Rust

645. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 348
   MCP server for Todoist integration enabling natural language task management with Claude

646. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 347
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

647. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 347
   AI-based stock analysis and trading system

648. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 347
   Model Context Protocol server for GraphQL

649. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 346
   MCP Server implementation for Ableton Live OSC control

650. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 346
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

651. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 345
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

652. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 345
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

653. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 344
   A macOS AppleScript MCP server

654. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 343
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

655. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 342
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

656. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 342
   SonarQube MCP Server

657. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 342
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

658. **[daan](https://github.com/pluveto/daan)** - ⭐ 341
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

659. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 341
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

660. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 341
   MCP Server implementation for Xcode integration

661. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 341
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

662. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 340
   F2C MCP Server

663. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 339
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

664. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

665. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 337
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

666. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 337
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

667. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 337
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

668. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 336
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

669. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 336
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

670. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 334
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

671. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 334
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

672. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 333
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

673. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 333
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

674. **[devopness](https://github.com/devopness/devopness)** - ⭐ 333
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

675. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 332
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

676. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 331
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

677. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 331
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  全球首个通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

678. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 330
   Elixir Model Context Protocol (MCP) SDK

679. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 329
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

680. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 328
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

681. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 327
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models. v0.2.8

682. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 326
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

683. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 326

684. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 326
   Control your Android devices with AI using Model Context Protocol

685. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 326
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

686. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 326
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

687. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 325
   An MCP implementation for Selenium WebDriver

688. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 325
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

689. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 324

690. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 323

691. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 323
   AI-Powered Revit Modeling

692. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

693. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 322
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

694. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 322
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

695. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 322
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

696. **[moling](https://github.com/gojue/moling)** - ⭐ 321
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

697. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 321
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

698. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 319
   Xiaozhi MCP sample program

699. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 318
   A Production-Ready Runtime Framework for Agent Deployment and Tool Sandbox

700. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 318
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

701. **[gemini-flow](https://github.com/clduab11/gemini-flow)** - ⭐ 318
   rUv's Claude-Flow, translated to the new Gemini CLI; transforming it into an autonomous AI development team.

702. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 317
   This is a Minecraft Base Client

703. **[emcee](https://github.com/mattt/emcee)** - ⭐ 316
   MCP generator for OpenAPIs 🫳🎤💥

704. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 315
   An MCP server for Azure DevOps

705. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 315
   An MCP server for loading skills (shim for non-claude clients).

706. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 314
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

707. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 313
   Repo of skills for autogen studio using model context protocol (mcp)

708. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 313
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

709. **[mcp](https://github.com/IBM/mcp)** - ⭐ 313
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

710. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 313
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

711. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 311
   MCP server to expose VS Code editing features to an LLM for AI coding

712. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 311
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

713. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 310
   deep, reliable and confidential coding-context

714. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 309
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

715. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 307
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

716. **[mesh](https://github.com/decocms/mesh)** - ⭐ 304
   One secure endpoint for every MCP server. Deploy anywhere.

717. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 304
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

718. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 303
   A working pattern for SSE-based MCP clients and servers

719. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 303
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

720. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 302
   Turn any openapi file into an mcp server, with just the tools you need.

721. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 302
   api router for MCP Servers

722. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 302
   Lighweight CLI to interact with MCP servers

723. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

724. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 301
   Mapbox Model Context Protocol (MCP) server

725. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 300
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

726. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 299
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

727. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 298
   A Model Context Protocol server for building an investor agent

728. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 297
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

729. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 297
   An implementation of Model Context Protocol (MCP) server for Argo CD.

730. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 297

731. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 297
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

732. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 296
   MCP implementation of Claude Code capabilities and more

733. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 296

734. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 296
   Lightweight MCP Server for interacting with Android Operating System.

735. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 295
   MaverickMCP - Personal Stock Analysis MCP Server

736. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 293
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

737. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 292
   Agentic RAG for any scenario. Customize sources, depth, and width

738. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 292
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

739. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 290
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

740. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 289
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

741. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 289
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

742. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 288
   Model Context Protocol server for DeepSeek's advanced language models

743. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 287
   OpenSkills: Run Claude Skills Locally using any LLM

744. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 287
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

745. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 286

746. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 286
   Minimal MCP Server for Aider

747. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 285
   MCP server for OpenAI o3 web search

748. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 285
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

749. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 284

750. **[generator](https://github.com/context-hub/generator)** - ⭐ 284
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

751. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

752. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 283
   hydra-ai

753. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 283

754. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 283
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

755. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 283
   Discover Exceptional MCP Servers

756. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 282
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

757. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

758. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 281
   The specification for the Universal Tool Calling Protocol

759. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 281
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

760. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 281
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

761. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 281
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

762. **[consult7](https://github.com/szeider/consult7)** - ⭐ 280
   MCP server to consult a language model with large context size

763. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 279
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

764. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 279
   First AI‑enabled open-source Human Capital Management system that you can start using today.

765. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 278
   simple web ui to manage mcp (model context protocol) servers in the claude app

766. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 277
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

767. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 277
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

768. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 277
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

769. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 276
   Model Context Protocol (MCP) Server for dify workflows

770. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 276
   MCP integration platforms making AI-Agents developers focusing on their own tasks

771. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 276
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

772. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 275
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

773. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 275
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

774. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 275
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

775. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 274
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

776. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 274
   MCP server for browser automation using Playwright

777. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 274
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

778. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 274
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

779. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 274
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

780. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 274
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

781. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 273
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

782. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 272
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

783. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 272
   A Model Context Protocol Server for MongoDB

784. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 272
   MCP server retrieving transcripts of YouTube videos

785. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

786. **[mq](https://github.com/harehare/mq)** - ⭐ 270
   jq-like command-line tool for markdown processing

787. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

788. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 269
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

789. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 269
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

790. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 267
   MCP server for Windows OS automation

791. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 267
   An MCP server providing tools for image processing operations

792. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 266
   Obsidian MCP (Model Context Protocol) Server

793. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 266
   Source code of minecraft 1.12

794. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 266
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

795. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 265
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

796. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 264
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

797. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 264

798. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 263
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

799. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 263
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

800. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 263
   MCP server for JADX-AI Plugin

801. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 260
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

802. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 259
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

803. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 259
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

804. **[mcp](https://github.com/oracle/mcp)** - ⭐ 259
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

805. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 259
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

806. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 259
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

807. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 258
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

808. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 257
   Home Assistant MCP Server

809. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 257
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

810. **[app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server)** - ⭐ 256

811. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 255
   MCP Server for Odoo

812. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 255
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

813. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

814. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 253
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

815. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 253
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

816. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 253
   MCP server for searching and retrieving Claude Agent Skills using vector search

817. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 252
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

818. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 251
   Model Context Protocol server implementation for Reddit

819. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 251
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

820. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 251
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

821. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 250
   Java AI（智能体） 全场景应用开发框架（LLM，Function Call，RAG，Embedding，Reranking，Flow，MCP Server，Mcp Client，Mcp Proxy）。同时兼容 java8 ~ java25。也可嵌入到 SpringBoot2、jFinal、Vert.x 等框架中使用。。支持 MCP_2025_06_18（mcp streamable）

822. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 250
   MCP server(s) for Aipolabs ACI.dev

823. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 249
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

824. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 249
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

825. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 249
   Apollo MCP Server

826. **[api200](https://github.com/API-200/api200)** - ⭐ 248
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

827. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 248
   A code reasoning MCP server, a fork of sequential-thinking

828. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 248
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

829. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 246
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

830. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 244
   Context-Engine: MCP retrieval stack for AI coding assistants. Hybrid code search (dense + lexical + reranker), ReFRAG micro-chunking, local LLM prompt enhancement, and dual SSE/RMCP endpoints. One command deploys Qdrant-powered indexing for Cursor, Windsurf, Roo, Cline, Codex, and any MCP client.

831. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 243
   MCP server implementation for Google's Gemini API

832. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 243
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

833. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 243
   Apache Doris MCP Server

834. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 243
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

835. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 243
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

836. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 242
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

837. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 242
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

838. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 242
   MCP Server for interacting with Salesforce instances

839. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 241
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

840. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

841. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 241
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

842. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 241
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

843. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 241
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

844. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 240
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

845. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 240
   An MCP server for Massive.com Financial Market Data

846. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

847. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 238
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

848. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 238

849. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 238
   MCP Server for Tree-sitter

850. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 237
   MCP Interface for Video Jungle

851. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 237
   Simplified Gemini for Claude Code. 

852. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 237
   MCP server for Bazi (八字) information

853. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 236
   Easy guide to installing Claude Code MCPs globally on your machine.

854. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 236
   小智AI客户端，目前主要用于MCP的对接

855. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

856. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 235
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

857. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 235
   Standardized environment infrastructure for Agentic AI development.

858. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 235
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

859. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 234
   Turn any MCP server into a Python module

860. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 234
   The evaluation benchmark on MCP servers

861. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 234

862. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 234
   Code Runner MCP Server

863. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 234

864. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 233
   🔥 Model Context Protocol (MCP) server for Firebase.

865. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 233
   Creates a simple MCP tool server with "streaming" HTTP.

866. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 231
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

867. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 230
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

868. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 230
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

869. **[dat](https://github.com/hexinfo/dat)** - ⭐ 229
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

870. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 229
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

871. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 229
   SpringAI，LLM，MCP，Embedding

872. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 229
   The Unofficial and Awesome Home Assistant MCP Server

873. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 228
   A Model Context Protocol (MCP) server that enables natural language queries to databases

874. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

875. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 227
   An experimental MCP Server for foundry built for Solidity devs

876. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 227
   MCP Server for Telegram

877. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 227
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

878. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 227
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

879. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 226
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

880. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 226
   A collection of MCP servers

881. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 225
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

882. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 225
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

883. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 225
   Standalone Roblox Studio MCP Server

884. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 224
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

885. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 224
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

886. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 223
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

887. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 222
   Semantic code searcher and codebase utility with AI memory onboard

888. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 221
   AWS MCP Proxy Server

889. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 221
   BrowserWing turns your browser actions into MCP commands, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

890. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 220
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

891. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 220

892. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 220
   Model Context Protocol server to run commands

893. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

894. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 219
   Volcengine MCP Servers

895. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 219
   A TypeScript SSE proxy for MCP servers that use stdio transport.

896. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 218

897. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 218
   A Model Context Protocol (MCP) server for interacting with Twitter.

898. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 218
   Lean Theorem Prover MCP

899. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

900. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 217
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

901. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 217
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

902. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 217
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

903. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 217
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

904. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 217
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

905. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 216
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

906. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 216
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

907. **[tentix](https://github.com/labring/tentix)** - ⭐ 214
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

908. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 214
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

909. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 214

910. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 214
   CAD MCP Server

911. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 214
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

912. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 214
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

913. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 213
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

914. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

915. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 213
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

916. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 213
   Playwright MCP fork that works with Cloudflare Browser Rendering

917. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 213
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

918. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 212
   Agent MCP for ffmpeg

919. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 212
   MCP server for Claude to access Outlook data via Microsoft Graph API

920. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 212
   Lightweight MCP server for Spotify

921. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 212
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

922. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 211
   A ReAct-Based Highly Robust Autonomous Agent Framework.

923. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 211
   Razorpay's Official MCP Server

924. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 211

925. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 211
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

926. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 211
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

927. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 211
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

928. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 210
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

929. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 210
   ModelContextProtocol for Figma's REST API

930. **[lokka](https://github.com/merill/lokka)** - ⭐ 210
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

931. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 210
   Lightweight C++ MCP (Model Context Protocol) SDK

932. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 210
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

933. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 209
   Model Context Protocol Servers for Milvus

934. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 209
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

935. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 209
   Things.app MCP Server

936. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 209
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

937. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 208

938. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 208
   Penpot MCP server

939. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 208
   A Multi-modal MCP client for voice powered agentic workflows

940. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 208

941. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 207
   mindmap, mcp server, artifact

942. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 207
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

943. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 207
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

944. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 207
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

945. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

946. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 206
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

947. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 206
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

948. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

949. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

950. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

951. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 205
   Zerodha Kite MCP server

952. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 204
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

953. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 204
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

954. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 204
   interactive programming of melodies, producing MIDI 

955. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 204
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

956. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 204
   An MCP server to use Sora video generation APIs

957. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 203
   Model Context Protocol tool support for LangChain

958. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 203
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

959. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 203
   MCP server for Anki via AnkiConnect

960. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 202
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

961. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 201

962. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 201
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

963. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 201
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to make direct edits and formatting.

964. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

965. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 200
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

966. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 200
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

967. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 200
   A Tiny Terminal Chat App for AI Models with MCP Client Support

968. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 200
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

969. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 199
   Run and monitor MCP servers locally

970. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 199
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

971. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 198
   🔎 A MCP server for Unsplash image search.

972. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 198
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

973. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 198
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

974. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 197

975. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 197
   A MCP Server for the RAG Web Browser Actor

976. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 197
   Pure Rust implementation of MCP server for headless terminal 

977. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 197
   🤖 An MCP server for surfacing useful Claude Code conversation history

978. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

979. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 196
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

980. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

981. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 196
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

982. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

983. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 195
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

984. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 195
   R MCP Server

985. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 195
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

986. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 195
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

987. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 194
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

988. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 194
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

989. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 194
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

990. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 194
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

991. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 194
   Homeassistant MCP server for 小智AI

992. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 193
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

993. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 193
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

994. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 193
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

995. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 192
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

996. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 192
   A SEC EDGAR MCP (Model Context Protocol) Server

997. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 191
   Absurdly easy Model Context Protocol Servers in Typescript

998. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 191
   Manage / Proxy / Secure your MCP Servers

999. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 191
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1000. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 191
   A MCP server for our beloved terminal multiplexer tmux.

1001. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1002. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 190

1003. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 189
   MCP server for Dynatrace Observability

1004. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 188
   这是一个专为开发企业级MCP server而设计的通用开发框架

1005. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 188
   Platform to create, curate and host MCP servers ⚒️ Build production quality tools for your agents.

1006. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 188
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1007. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1008. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1009. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1010. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1011. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 186
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1012. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 186
   Self-hosted AI RAG + MCP Platform

1013. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 186
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1014. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 186
   Supabase MCP server created in Python.

1015. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 186
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1016. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 185
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1017. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 185
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1018. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 185
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1019. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 185
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1020. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 185
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

1021. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1022. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 184
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1023. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 184
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1024. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 183
   A TypeScript framework for building MCP servers elegantly

1025. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1026. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1027. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 182
   The Power BI Desktop MCP Server is a tool that lets AI assistants like Claude interact with your Power BI models programmatically. It enables Claude to read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1028. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 181
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1029. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 181
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

1030. **[siconos](https://github.com/siconos/siconos)** - ⭐ 180
   Simulation framework for nonsmooth dynamical systems

1031. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 180
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1032. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 180

1033. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 180
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1034. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 180
   Hugging Face MCP Server

1035. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 180
   Model Context Protocol Servers in Quarkus

1036. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 180
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1037. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 180
   MCP Server for ServiceNow

1038. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 179
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1039. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1040. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1041. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 178
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1042. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 178
   Google Search Console Insights with Claude AI for SEOs

1043. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1044. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 177
   An MCP server for Anki

1045. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 177
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1046. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 175

1047. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 174
   This extension enables developers to implement the MCP server features easily.

1048. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 174
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1049. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1050. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 174
   MCP Server for the Bilibili API, supporting various operations.

1051. **[mcp-run-python](https://github.com/pydantic/mcp-run-python)** - ⭐ 174
   MCP server to run Python code in a sandbox.

1052. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 173
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1053. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 173
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

1054. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 172
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1055. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 171

1056. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 171
   MCP for calling Siri Shorcuts from LLMs

1057. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 171
   pctx is the execution layer for agentic tool calls. It exposes custom tools and MCP servers as code that runs in secure sandboxes for token-efficient calls.

1058. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 171
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1059. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 169
   Examples of using Pipedream's MCP server in your app or AI agent.

1060. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 169
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1061. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 169
   MCP stdio server for frida

1062. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 169
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1063. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 169
   A list of open-source AI projects you can use to generate income easily.

1064. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 169
   Built-in MCP client–powered document/news management tool with daily auto summaries, document interaction, user-defined notifications (email, apns, etc.), and customizable model support.内置 MCP 客户端的文档/资讯管理工具，支持每日自动总结、文档交互、自定义通知（邮箱、APNS等）以及模型自定义。

1065. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 169
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1066. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 168
   A MCP server to search for accurate academic articles.

1067. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 168
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1068. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 168
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1069. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 168
   Turn any website or doc into an MCP server

1070. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 167
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1071. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 167
   A Tiny Web Chat App for AI Models with MCP Client Support

1072. **[command](https://github.com/scopecraft/command)** - ⭐ 167
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1073. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 166
   MCP server for TouchDesigner

1074. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 165
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1075. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 165
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1076. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 165
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1077. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 165
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1078. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 165
   Discord MCP Server for Claude Integration

1079. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 164
   A desktop application that adds powerful tools to Claude and AI platforms

1080. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 164
   One MCP Server, All Your Apps, Privacy First

1081. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 164
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1082. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 162
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1083. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 162
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1084. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 162
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1085. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 162
   MCP (Model Context Protocol) server for Weaviate

1086. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 162
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1087. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 161
   MCP server to work with Telegram through MTProto

1088. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 161
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1089. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 161
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1090. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 161
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1091. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 160
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1092. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 160
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1093. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 159
   Official Magic UI MCP server.

1094. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 159
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1095. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 159
   Command line interface for MCP clients with secure execution and customizable security policies

1096. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 159
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1097. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 159
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1098. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 159
   MCP Server for Wazuh SIEM

1099. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 159
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1100. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 158
   Turn a web server into an MCP server in one click without making any code changes.

1101. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1102. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 158
   Sketchup Model Context Protocol

1103. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 158
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1104. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 157
   An MCP server for fetching URLs / Youtube video transcript.

1105. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 157
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1106. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 157
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1107. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 157
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1108. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 156
   A simple CLI to install MCP servers into any client - auth included!

1109. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 156
   ToolSDK.ai's Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1110. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 156

1111. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 156
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1112. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 155
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1113. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 155
   Learn how to use MCP Servers with GitHub Copilot

1114. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 154
   Simple Slackbot MCP Client

1115. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 154
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1116. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 153
   An MCP server to search for flights.

1117. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 153
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1118. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 152
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1119. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 151
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1120. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 151
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1121. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 151

1122. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 151
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1123. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 150
   MCP Server for AI Summarization

1124. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 150
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1125. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 150
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1126. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 150
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1127. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 149
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1128. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1129. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 149
   Deep Research for crypto - free & fully local

1130. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 149
   Desktop APP for Discover and Install MCP Servers

1131. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 149
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1132. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 149
   Typescript SDK to build MCP servers in an agnostic way

1133. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 148
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1134. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 148
   MCP server for searching and querying PubMed medical papers/research database

1135. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 148
   MCP Server for Postgres

1136. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 148
   A simple MCP server to search for documentation (tutorial)

1137. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 148
   A gateway demo for MCP SSE Server

1138. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 148
   Instagram Direct messages MCP

1139. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 148
   A list of MCP (Model Context Protocol) servers for developer tools and services

1140. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 147
   Model Context Protocol For R

1141. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 147
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1142. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 147
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1143. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 147
   Model Context Protocol (MCP) server for constraint optimization and solving"

1144. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 146
   Make MCP Server

1145. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 146
   MCP server implementation for Google's Gemini API

1146. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 146
   MCP Server for using any LLM as a Tool

1147. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 146
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1148. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 146
   Your own Claude Code UI — local or cloud sandbox, in-browser VS Code, terminal, multi-provider support (Max, Z.AI, OpenRouter), custom skills, and MCP servers.

1149. **[relay](https://github.com/prism-php/relay)** - ⭐ 145
   An MCP client tool for Prism

1150. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 145

1151. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 145
   Model Context Protocol server implementation for Figma API

1152. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 145
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1153. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 144
   MCP server to download entire websites

1154. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 144
   Connect any Open Data to any LLM with Model Context Protocol.

1155. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 144
   Goku is an HTTP load testing application written in Rust 

1156. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 144
   An MCP server that provides access to Postman.

1157. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 144
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1158. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 144
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1159. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 144
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1160. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 144
   Scrapeless Mcp Server

1161. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 143
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1162. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 143
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1163. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 142
   A PubMed MCP server.

1164. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 142

1165. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 142
   Neo4j official MCP Server

1166. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1167. **[kom](https://github.com/weibaohui/kom)** - ⭐ 141
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1168. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 141
   Connect your AI to your APIs on Postman

1169. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 141
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1170. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 141
   Persistent Intelligence Infrastructure for AI Agents

1171. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 140
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1172. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 140
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1173. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 140
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1174. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 140
   A Model Context Protocol server for MySQL database operations

1175. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 140
   A MCP Server for creating Powerpoint Presentations

1176. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 140
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1177. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 140
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1178. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 140
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1179. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 139
   Simple MCP Server Implementation

1180. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 139
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1181. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 139
   Persistent AI memory for coding assistants - MCP server providing context persistence across sessions for Claude, Cursor, Windsurf.  MCP Tools for task tracking, workflow automation, and AI memory. Eliminates context loss between sessions.

1182. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 139
   MCP server for discord bot

1183. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 138
   MCP server for Israel Government Data

1184. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 138
   Catch MCP server issues before your agents do.

1185. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 138
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1186. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 138
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1187. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 138
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1188. **[eion](https://github.com/eiondb/eion)** - ⭐ 138
   Shared Memory Storage for Multi-Agent Systems

1189. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 138
   StarRocks MCP (Model Context Protocol) Server

1190. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 138
   Dynamically expose tools from proxied servers based on an Agent Persona

1191. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 138
   A Model Context Protocol server for calculating.

1192. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 137
   MCP Server for Google Slides

1193. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 137
   MSSQL Server MCP implementation written in C#

1194. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 136
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1195. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 136
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1196. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 136
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1197. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 135
   MCP server for seamless document format conversion and processing

1198. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 135
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1199. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 135
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1200. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 135
   MCP server for AutoCAD LT: AI agents translate natural language into AutoLISP code for geometry, 600+ ISA 5.1 P&ID symbols, block attributes, and layer management—generating technical drawings with 80% performance improvement via batch operations.

1201. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 135
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1202. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1203. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 134
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1204. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 134
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1205. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 134
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1206. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1207. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 133
   Serper MCP Server supporting search and webpage scraping

1208. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 133
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1209. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 133
   MCP server to access Garmin data

1210. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 133
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1211. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 133
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1212. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 133
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1213. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 133
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1214. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 133

1215. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 133
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1216. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 133
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1217. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 132
   An MCP server implementing the think tool for Claude

1218. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 132
   DataForSEO API modelcontextprotocol server 

1219. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 132
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1220. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 132
   mcp server for gitingest

1221. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 132
   A local Apple Documentation crawler and MCP server. Written in Swift.

1222. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 131
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1223. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 131
   Graphiti MCP Server

1224. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 131
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1225. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 131
   The Logfire MCP Server is here! :tada:

1226. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 131
   IMAP and SMTP via MCP Server

1227. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 130
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1228. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 130
   Manage Your Kubernetes Cluster with k8s mcp-server

1229. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 130
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1230. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 130
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1231. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 130
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1232. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 130
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1233. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 130
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1234. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 130
   A guide on how to use the Figma MCP server

1235. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 130
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1236. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 129
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

1237. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 129
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1238. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 129
   Chat application with multi-agents system supports multi-models and MCP

1239. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 129
   Model Context Protocol (MCP) server for the Zotero API, in Python

1240. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 128
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1241. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 128
   MCP server for understanding AWS spend

1242. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 128
   A collection of crypto MCP servers.

1243. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 128
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1244. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 128
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1245. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1246. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 128
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1247. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

1248. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 127
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1249. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 127
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1250. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1251. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 126
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1252. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 126
   🚀🎬 Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1253. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 126
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1254. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 126

1255. **[magg](https://github.com/sitbon/magg)** - ⭐ 126
   Magg: The MCP Aggregator

1256. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1257. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 126

1258. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 125
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1259. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 125
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1260. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 125
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1261. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1262. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 125
   Dart AI Model Context Protocol (MCP) server

1263. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 125
   Intelligent spec workflow management MCP server

1264. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 124
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1265. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1266. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 124
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1267. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 124
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1268. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 124
   High-performance CCXT MCP server for cryptocurrency exchange integration

1269. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 124
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1270. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 124
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1271. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 124
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1272. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 123
   Buttplug.io Model Context Protocol (MCP) Server

1273. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 123
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1274. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 123
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1275. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 123
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1276. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 123
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1277. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 123
   An MCP Server for Ollama

1278. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 122
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1279. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 122
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1280. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 122
   a private MCP server for accessing Linear

1281. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 122
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1282. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 122
   It's time to push beyond MCP Servers... Right?

1283. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 122
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1284. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 122
   🐉 The fast, PHP way to build MCP servers

1285. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 122
   Penpot's official MCP Server

1286. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 122
   MCP stdio server for radare2

1287. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 122
   Open Source AI platform to build Agentic workflows, MCP servers and ChatGPT apps 

1288. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 122
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1289. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1290. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 121
   MCP server for Unreal Engine 5

1291. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 121
   Model Context Protocol (MCP) with TikTok integration

1292. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 121
   MCP Server for Searching Turkish Legislation

1293. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 121
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1294. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 121
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1295. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 121
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1296. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 120
   A Model Context Protocol server that provides access to BigQuery

1297. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 120
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1298. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 120
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1299. **[openapi](https://github.com/samchon/openapi)** - ⭐ 120
   OpenAPI definitions, converters and LLM function calling schema composer.

1300. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 119
   MCP server implementation for n8n workflow automation

1301. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 119
   An MCP server for FFmpeg

1302. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 119
   An MCP server that provides LLMs with the latest stable package versions when coding

1303. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 119
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1304. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 119
   Toolkit for Coding Agents to work reliably with repo of any size.

1305. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 119
   Universal command-line client for MCP. Supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for scripting and code mode, proxy for AI sandboxes, and more.

1306. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 118
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1307. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 118
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1308. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 118
   Lightweight agent orchestration dev tool that lives in your repo

1309. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 117
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1310. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 117

1311. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 117
   Salesforce MCP Server

1312. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 116
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1313. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 116

1314. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 116
   BrowserStack's Official MCP Server

1315. **[kodit](https://github.com/helixml/kodit)** - ⭐ 115
   👩‍💻 MCP server to index external repositories

1316. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 115
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1317. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 115
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1318. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) for Jupyter Notebook

1319. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 114
   A proxy to use HTTP/SSE MCPs from STDIO clients

1320. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 114
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1321. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 114
   Codex Mcp Server 

1322. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 114
   A modular MCP server that provides commonly used developer tools for AI coding agents

1323. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 114
   Fast and super efficient Minecraft Server written in C++

1324. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 114
   Vector-search powered agent memory MCP server

1325. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 113
   An MCP server for InterviewReady

1326. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 113
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1327. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1328. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 113

1329. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 113
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1330. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 112
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1331. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 112
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1332. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 112
   Swagger to MCP server

1333. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 112
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1334. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 112
   MariaDB MCP (Model Context Protocol) server implementation

1335. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 112
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1336. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 112
   Tools to allow LLM clients to interact with Linux systems remotely

1337. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1338. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 111
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1339. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1340. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1341. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 111
   Azure API Management as AI Gateway to Remote MCP servers.

1342. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1343. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

1344. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 111
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1345. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 111
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1346. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1347. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 110
   Google Sheets MCP Server 📊🤖

1348. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 110
   💻 Give AI models complete control of your computer (probably a bad idea)

1349. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 110
   MCP server implementation for the UniFi network application

1350. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 110
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1351. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 110
   MCP server for Oura API integration

1352. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 110
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1353. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 110

1354. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 110
   Model Context Protocol Server for Swift

1355. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 110
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1356. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 110
   Docker Hub MCP Server

1357. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1358. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 110
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1359. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 109
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1360. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 109
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1361. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 109
   A Model Context Protocol Server to manipulate *.xcodeproj

1362. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 109
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1363. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 109
   MCP server for connecting agentic systems to search systems via searXNG

1364. **[modex](https://github.com/theronic/modex)** - ⭐ 108
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1365. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1366. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1367. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 108
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1368. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 108
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1369. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 108
   MCP server for interaction with Bitwarden.

1370. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 107
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1371. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 107
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1372. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 107
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1373. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 107
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1374. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 107
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1375. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 107
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1376. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 106
   Supercharge AI Agents, Safely

1377. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 106
   A Slack MCP server

1378. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 106
   Control WordPress using WP-CLI, AI, and MCP.

1379. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 106
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1380. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 106
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1381. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 106
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1382. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 105
   A redmine MCP server covering close to 100% of redmines API

1383. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 105
   Payload CMS MCP Server

1384. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 105
   MCP Client Implementation using Python, LangGraph and Gemini

1385. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 105
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1386. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 105
   blazigly fast gRPC/MCP client & server implementation in zig

1387. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1388. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1389. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 105
   An MCP client for Node.js.

1390. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 105
   MCP Server for working with large Oracle databases

1391. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1392. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 104
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1393. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 104
   An MCP Server for your Self Hosted Supabase

1394. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 104

1395. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 104
   MCP for semantic code search & navigation that reduces token waste

1396. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 104
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1397. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 104
   Open Source MCP Servers for Scientific Research

1398. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 104
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1399. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1400. **[mcp](https://github.com/frappe/mcp)** - ⭐ 103
   Frappe MCP allows Frappe apps to function as MCP servers

1401. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1402. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 103
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1403. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 103
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1404. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 103
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1405. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 103
   MCP server for Dash, the macOS documentation browser

1406. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 103
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1407. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 103
   Isaac Simulation MCP Extension and Server

1408. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 102
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1409. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 102
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1410. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 102
   fast, secure c# runner

1411. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1412. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1413. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 102
   Raindrop MCP Server

1414. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 102
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1415. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 102
   MCP Server for EMRs with FHIR

1416. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 102
   MCP server for interacting with the Aseprite API

1417. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 102
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1418. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 102
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1419. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 102
   Official Railway MCP Server for interacting with your Railway account

1420. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 102
      Convert any MCP server into a Claude Skill with 90% context savings

1421. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 101
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1422. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 101
   Official Vectorize MCP Server

1423. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 101
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1424. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 101
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1425. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 101
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1426. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1427. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 101
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1428. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 101
   MCP Server for PolyMarket API

1429. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 101
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1430. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1431. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 100
    AI-powered security operations with Wazuh SIEM + Claude Desktop. Natural language threat detection, automated incident response & compliance. Real-time monitoring, ML anomaly detection. Transform your SOC with conversational security analysis. Production-ready MCP server.

1432. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 100
   Portainer MCP server

1433. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1434. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 100
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1435. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1436. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 99
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1437. **[mcp](https://github.com/taskade/mcp)** - ⭐ 99
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1438. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 99
   Collection of examples of how to use Model Context Protocol with AWS.

1439. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1440. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 99
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1441. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1442. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1443. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1444. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 99
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1445. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 99
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1446. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 99
   MCP server for Coolify

1447. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1448. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 98
   claude mcp sse demo with server and client(cli、web)

1449. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

1450. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 98
   MCP server for querying the Shodan API

1451. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

1452. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 98
   Node.js Client Implementation for Model Context Protocol (MCP)

1453. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 97
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1454. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 97
   A Google Tasks Model Context Protocol Server for Claude

1455. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 97
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1456. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 97
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1457. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 97
   first gemini based desktop client for MCP

1458. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 97
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1459. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 96
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1460. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 96
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1461. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1462. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 96
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1463. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 96
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1464. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 96
   MCP server for natural language interaction with Power BI datasets

1465. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 95
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1466. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 95
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1467. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 95
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1468. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 95
   Model Context Protocol (MCP) server for the Webflow Data API.

1469. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 94
   This is a Ruby implementation of MCP (Model Context Protocol) client

1470. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 94
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1471. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 94
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1472. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 94
    Official Go implementation of the UTCP 

1473. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1474. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 93
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1475. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 92
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1476. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 92
   Model Context Protocol server for Replicate's API

1477. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 92
   A Model Context Protocol (MCP) server providing access to Google Search Console

1478. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 92
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1479. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 92
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1480. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 92
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1481. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for square

1482. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1483. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1484. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 90
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1485. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 90
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1486. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 90
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search and News Search capabilities

1487. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 89
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1488. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 88
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1489. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 88
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1490. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 88
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1491. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 88
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

1492. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 87
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1493. **[mcp-web-ui](https://github.com/MegaGrindStone/mcp-web-ui)** - ⭐ 87
   MCP Web UI is a web-based user interface that serves as a Host within the Model Context Protocol (MCP) architecture. It provides a powerful and user-friendly interface for interacting with Large Language Models (LLMs) while managing context aggregation and coordination between clients and servers.

1494. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 87
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1495. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 87
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1496. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 87
   A model-context-protocol server for molecules.

1497. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 86
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1498. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 86
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1499. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 86
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1500. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 86
   Nextcloud MCP Server

1501. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 86
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

1502. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 86
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

1503. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1504. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 85
   CLI & API for MCP management

1505. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 85
   Ragie Model Context Protocol Server

1506. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 85
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1507. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 84
   Rails Engine with MCP compliant Spec.

1508. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 84
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1509. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 83
   A Model Context Protocol server that provides knowledge graph management capabilities.

1510. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 83
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1511. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 83
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1512. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 83
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1513. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 82
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1514. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1515. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1516. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1517. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1518. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 81
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1519. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 81
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1520. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 81
   MCP server for Mikrotik

1521. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 80
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1522. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 80
   Model Context Protocol (MCP) Server for the Keboola Platform

1523. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 80
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1524. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 80
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1525. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 80
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1526. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 80
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1527. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 80
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1528. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 80
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

1529. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 79
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1530. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 79
   A model context protocol server that connects to Anki through AnkiConnect

1531. **[identity](https://github.com/agntcy/identity)** - ⭐ 79
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1532. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 79
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1533. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 79
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1534. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 79
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1535. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 79
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1536. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 79
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1537. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 78
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1538. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 78
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1539. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 78
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

1540. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 77
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1541. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 76
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1542. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 76
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1543. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 76
   Model Context Protocol (MCP) Client for Apify's Actors

1544. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1545. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 76
   Official Oxylabs MCP integration

1546. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1547. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 75
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1548. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 75
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1549. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 75
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1550. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 75
   A WooCommerce (MCP) Model Context Protocol server

1551. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1552. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 74
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1553. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 74
   Model Context Protocol for Actual Budget API

1554. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 74
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1555. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 74
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

1556. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 73
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1557. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 73
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1558. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1559. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 72
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1560. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 72
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1561. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 72
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1562. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 72
   An md file as a chat interface and editable history in one.

1563. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 72
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1564. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 72
   The Privacy Firewall for LLMs

1565. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 71
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1566. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 71
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1567. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 71
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1568. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 71
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1569. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 71
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1570. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 70
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1571. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1572. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 70
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1573. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 70
   An unofficial and community-built MCP server for integrating with https://railway.app

1574. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 69
   Model Context Protocol implementation for retrieving codebases using RepoMix

1575. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 69
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1576. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 69
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1577. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 69
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

1578. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 68
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1579. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 68
   A Model Context Protocol server for Hopper Disassembler

1580. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

1581. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 68
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1582. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 68
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

1583. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1584. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1585. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1586. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 67
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1587. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1588. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 67
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1589. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 67
   MCP client for local ollama models

1590. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 67
   An extension of MCP for SillyTavern.

1591. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 67
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1592. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 67
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1593. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 67
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

1594. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 66
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1595. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 66
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1596. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 66
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

1597. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 66
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1598. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 66
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1599. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 66

1600. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 66
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1601. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 66
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1602. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 66
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1603. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 66
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1604. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 66
   Open Models MCP for Blender Using Ollama

1605. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 66
   AniList MCP server for accessing anime and manga data

1606. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 66
   web GUI for securely managing local Opencode configuration

1607. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 65
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1608. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 65
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1609. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 65
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1610. **[ViaMCP](https://github.com/ViaVersionMCP/ViaMCP)** - ⭐ 65
   Client-side Implementation of the Via* projects for MCP

1611. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 65
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1612. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 65
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1613. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 65
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1614. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 65
   Model Context Protocol(MCP) 中文教程讲解

1615. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 65
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

1616. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 65
   From Java Dev to AI Engineer: Spring AI Fast Track

1617. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 65
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1618. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 64
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1619. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1620. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1621. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

1622. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

1623. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 64
   The official MCP server for SurrealDB

1624. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 63
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1625. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 63
   A Model Context Protocol implementation for FHIR

1626. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 63
   Model Context Protocol for x64dbg & x32dbg

1627. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 63
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1628. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1629. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 62
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1630. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

1631. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 62
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resources for client-side exploration.

1632. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 62
   Model Context Protocol for YNAB (you need a budget)

1633. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 62
   Index of all Model Context Protocol (MCP) clients and their capabilities

1634. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 62
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

1635. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 61
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1636. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1637. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1638. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 61
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1639. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 61
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1640. **[kollektiv-mcp](https://github.com/alexander-zuev/kollektiv-mcp)** - ⭐ 61
   Kollektiv MCP enables you to chat with and query your own documents directly from IDEs and MCP clients. Private, secure, and integrated into your favorite code editor

1641. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 61
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1642. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1643. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 61
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1644. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 61
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

1645. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 61
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1646. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 60
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1647. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1648. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 60
   Python 实现 MCP client / service

1649. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 60
   Python code execution sandbox with programmatic MCP tool calling (PTC)

1650. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 60
   Miro integration for Model Context Protocol

1651. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 60
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

1652. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1653. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server for Rember.

1654. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 59
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1655. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 59
   A full featured, enterprise grade rust MCP SDK

1656. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 59
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1657. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 59
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1658. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 59
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1659. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

1660. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

1661. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 58
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1662. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 58
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

1663. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 58
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

1664. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 58
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

1665. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 58
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

1666. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 58
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1667. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 57
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

1668. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 57
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1669. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

1670. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 57
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

1671. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 57
   A Clojure SDK to create MCP servers (and eventually clients)

1672. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 57
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1673. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 57
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1674. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 57
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

1675. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 56
   MCP router and Web Based MCP client

1676. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 56
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

1677. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

1678. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1679. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 56
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1680. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

1681. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 56
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1682. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 56
   A Model Context Protocol server for Ashra

1683. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 56
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

1684. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 56
   Open-source FRED MCP Server (Federal Reserve Economic Data)

1685. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

1686. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 55
   MKP is a Model Context Protocol (MCP) server for Kubernetes

1687. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 55
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

1688. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 55
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

1689. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 55
   A Model Context Protocol (MCP) server for Microsoft Clarity

1690. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 55
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

1691. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 55
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source.

1692. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 54
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

1693. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

1694. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

1695. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 54
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

1696. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

1697. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 54
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

1698. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 54
   可视化的配置和管理，给xiaozhi接入mcp

1699. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 54
   MCP server for Slither static analysis of Solidity smart contracts

1700. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

1701. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 53
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

1702. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 53
   Quantum-proof MCP Server and Client Interactions

1703. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 53
   MCP server for *arr media management suite

1704. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 52
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

1705. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 52
   Model Context Protocol Servers for Azure AI Search

1706. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

1707. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 52
   A Nasdaq Data Link MCP (Model Context Protocol) Server

1708. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 52
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

1709. **[client](https://github.com/php-mcp/client)** - ⭐ 52
   Core PHP implementation for the Model Context Protocol (MCP) Client

1710. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 52
   MCP (Model Context Protocol) server plugin for CAP NodeJS

1711. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

1712. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 52
   OCaml implementation of the Model Context Protocol (MCP)

1713. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 52
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

1714. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

1715. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 52
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1716. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 52
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

1717. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 52
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

1718. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 52
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

1719. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 52
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

1720. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1721. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 52
   MCP Memory Server with DuckDB backend

1722. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 52
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

1723. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 52
   Universal MCP Server Configuration Manager

1724. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 52
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

1725. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

1726. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 51
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1727. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 51
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

1728. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

1729. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 51
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

1730. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 51
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1731. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 51
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

1732. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 51
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

1733. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 50
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

1734. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

1735. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

1736. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 50
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

1737. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 50
   ABAP MCP - Model Context Protocol - Server SDK

1738. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 50
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

1739. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 50
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

1740. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

1741. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 50
   MCP Server for IBKR Client

1742. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 50
   MCP Guard secures your MCP client from prompt injection attacks and more.

1743. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 50
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

1744. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 50
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

1745. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 50
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

1746. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 50
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

1747. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 49
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

1748. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 49
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

1749. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 49
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

1750. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

1751. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 49
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

1752. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 49
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1753. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 49
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

1754. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 48
   Anthropic’s Model Context Protocol implementation for Oat++

1755. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

1756. **[mcp](https://github.com/goplus/mcp)** - ⭐ 48
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

1757. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 48
   A Model Context Protocol server that validates and renders Mermaid diagrams.

1758. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

1759. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

1760. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 48
   Unblock, scrape, and search tools for MCP clients

1761. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 48
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1762. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 48
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

1763. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 48
   vMCP - Virtual Model Context Protocol

1764. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 48
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

1765. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 48
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

1766. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 48
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

1767. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 48
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

1768. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 47
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

1769. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

1770. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 47
   An implementation of the Model Context Protocol in Ruby.

1771. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

1772. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 47
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

1773. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 47
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

1774. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

1775. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

1776. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 47
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

1777. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 47
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

1778. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 47
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

1779. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 47
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

1780. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

1781. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 47
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

1782. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 46
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

1783. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 46
   Inkdrop Model Context Protocol Server

1784. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 46
   OpenAPI Schema Model Context Protocol Server

1785. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

1786. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 46
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

1787. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

1788. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 46
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

1789. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

1790. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 46
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1791. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

1792. **[go-mcp](https://github.com/MegaGrindStone/go-mcp)** - ⭐ 46
   A Go implementation of the Model Context Protocol (MCP) - an open protocol that enables seamless integration between LLM applications and external data sources and tools.

1793. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 46
   Sample MCP Server and MCP client with Aspire

1794. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 46
   A Model Context Protocol server for Zendesk

1795. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 46
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

1796. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 45
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

1797. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

1798. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

1799. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 45
   A Model-Context-Protocol (MCP) Server for Active Directory

1800. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 45
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

1801. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

1802. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 45
   Un-official Serper Google search server for Cline and other MCP clients

1803. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 45
   MCPcat is an analytics platform for MCP server owners 🐱.

1804. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

1805. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 45
   共学《MCP极简开发》项目代码

1806. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 45
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

1807. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 45
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

1808. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 45
   Model Context Protocol to fetch youtube transcript

1809. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 45
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1810. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 45
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

1811. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 45
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

1812. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 44
   Model Context Protocol server for Flight Tracking

1813. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

1814. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 44
   📚 An intelligent toolkit to automatically parse, complete, and format academic references, with Model Context Protocol (MCP) support.

1815. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

1816. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 44
   An opinionated starter template for making Model Context Protocol (MCP) servers

1817. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 44
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

1818. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 44
   Model Context Protocol for WeChat

1819. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

1820. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

1821. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

1822. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 44
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

1823. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 44
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

1824. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 44
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

1825. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 44
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

1826. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

1827. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

1828. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

1829. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 43
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

1830. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 43
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

1831. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 43
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

1832. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 43
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

1833. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

1834. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 43
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

1835. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 43
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

1836. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 43
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

1837. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 43
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

1838. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

1839. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

1840. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 43
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

1841. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 43
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1842. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

1843. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 42
   GraphQL Schema Model Context Protocol Server

1844. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

1845. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

1846. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 42
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

1847. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 42
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

1848. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 42
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

1849. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 42
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

1850. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 42
   Amadeus MCP(Model Context Protocol) Server

1851. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 42
   An implementation of the Model Context Protocol for the World Bank open data API

1852. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 42
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

1853. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 42
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

1854. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

1855. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 42
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

1856. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

1857. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 42
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

1858. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 42
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

1859. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 41
   Model Context Protocol server for Salesforce REST API integration

1860. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

1861. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

1862. **[mcp](https://github.com/40ants/mcp)** - ⭐ 41
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

1863. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

1864. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 41
   A Model Context Protocol server for Go developers

1865. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 41
   A production-ready Model Context Protocol (MCP) server for semantic memory management

1866. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 41
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

1867. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 41
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

1868. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 41
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

1869. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 41
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

1870. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 41
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

1871. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 41
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

1872. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

1873. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 41
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

1874. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 41
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

1875. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 40
   A Model Context Protocol server for Dify

1876. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

1877. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

1878. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

1879. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

1880. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

1881. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

1882. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 40
   MCP (Model Context Protocol) server for the Contentful Management API

1883. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 40
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

1884. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

1885. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

1886. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 40
   Model Context Protocol Clojure support including REPL integration with development tools.

1887. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 40
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

1888. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 40
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

1889. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 40
   A simple NextJS MCP client with sensible keybindings

1890. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 40
   Implementation of Model Context Protocol server for Mailgun APIs

1891. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 40
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

1892. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

1893. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 40
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

1894. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 40
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1895. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 40
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

1896. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

1897. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 40
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

1898. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

1899. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 40
   Attio Model Context Protocol (MCP) server implementation

1900. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

1901. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

1902. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

1903. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 39
   Model Context Protocol server for OpenStreetMap data

1904. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

1905. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 39
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

1906. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 39
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

1907. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

1908. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

1909. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 39
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

1910. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 39
   It shows how to use model-context-protocol. 

1911. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 39
   Go SDK for interacting with the MCP Toolbox for Databases.

1912. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 39
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

1913. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 39
   Model Context Protocol server for ActivityWatch time tracking data

1914. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

1915. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 38
   Algorand Model Context Protocol (Server & Client)

1916. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

1917. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 38
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

1918. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

1919. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

1920. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 38
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

1921. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 38
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

1922. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 38
   MCP server for anki

1923. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

1924. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 38
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

1925. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 38
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

1926. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 38
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

1927. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

1928. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

1929. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 37
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

1930. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1931. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 37
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

1932. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 37
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

1933. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 37
   Model Context Protocol server for Sitecore

1934. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 37
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

1935. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 37
   A Model Context Protocol server that provides access to Shodan API functionality

1936. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 37
   An MCP server for querying Solana transactions using natural language with Solscan API

1937. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 37
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

1938. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 37
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

1939. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 37
   A Chat Client for LLMs, written in Compose Multiplatform.

1940. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 37
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

1941. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 37
   Model Context Protocol server to let LLMs write and execute matlab scripts 

1942. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 37
   Bluesky MCP (Model Context Protocol) Server

1943. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

1944. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 37
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

1945. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 37
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

1946. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

1947. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 36
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

1948. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

1949. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 36
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

1950. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

1951. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 36
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

1952. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

1953. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

1954. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

1955. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 36
   Model Context Protocol Minecraft Server

1956. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

1957. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 36
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

1958. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 36
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

1959. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

1960. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 36
   Model Context Protocol (MCP) implementation for iOS simulators

1961. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

1962. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 36
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

1963. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

1964. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

1965. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

1966. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 35
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

1967. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 35
   Privacy-first local RAG server for Cursor, Claude Code, and more — powered by the Model Context Protocol.

1968. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 35
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

1969. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 35
   Model Context Protocol (MCP) server for LinkedIn API integration

1970. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 35
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

1971. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 35
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

1972. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

1973. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 35
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

1974. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

1975. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 35
   Altium Model Context Protocol server and Altium API script

1976. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 35
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

1977. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 35
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

1978. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 34
   Model Context Protocol (MCP) Server for Mistral OCR API

1979. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 34
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

1980. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

1981. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

1982. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 34
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

1983. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

1984. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

1985. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 34
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

1986. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 34
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

1987. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

1988. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

1989. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 34
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

1990. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 34
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

1991. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 34
   IMAP Model Context Protocol server for interactive email processing

1992. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 34
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

1993. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

1994. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

1995. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 34
   Rimworld Coding RAG MCP server

1996. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

1997. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 33
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

1998. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 33
   Model Context Protocol server written in Scala

1999. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 33
   Model Context Protocol Server for Apache OpenDAL™

2000. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 33
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

2001. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

2002. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

2003. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 33
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

2004. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 33
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2005. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 33
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2006. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 33
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

2007. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2008. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 33
   A powerful Model Context Protocol server for LinkedIn API integration

2009. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 33
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

2010. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

2011. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2012. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 33
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

2013. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 33
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2014. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 33
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2015. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 33
   Turn any MCP Client into a "multi-agent" system (via prompting)

2016. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

2017. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

2018. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

2019. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

2020. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 32
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

2021. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 32
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

2022. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 32
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2023. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 32
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

2024. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

2025. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 32
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

2026. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 32
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2027. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 32
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

2028. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 32
   MCP client for Discourse sites

2029. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 32
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2030. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 32
   Claude Unified Model Context Interaction Protocol

2031. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 31
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

2032. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 31
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2033. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

2034. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

2035. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 31
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2036. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

2037. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 31
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2038. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

2039. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 31
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2040. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 31
   About A Model Context Protocol server that executes commands in the current WezTerm session

2041. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 31
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

2042. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

2043. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 31
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2044. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 31
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2045. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 31
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

2046. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 31
   Emacs Lisp implementation of the Model Context Protocol

2047. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 31
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2048. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

2049. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

2050. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 30
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2051. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

2052. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

2053. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 30
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

2054. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 30
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

2055. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 30
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

2056. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 30
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

2057. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server for openBIM

2058. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 30
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2059. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 30
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

2060. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 30
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

2061. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 30
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

2062. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 30
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

2063. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

2064. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 30
   Model Context Server Protocol for your HANA DB

2065. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

2066. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 30
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

2067. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

2068. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 30
   List of Awesome MCP Servers and Clients for building Agentic Devops 

2069. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 30
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

2070. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 30
   Query model running with Ollama from within Claude Desktop or other MCP clients

2071. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2072. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 30
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2073. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 30
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2074. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server for Polymarket prediction markets, providing real-time market data, prices, and AI-powered analysis tools for Claude Desktop integration.

2075. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 30
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2076. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 30
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2077. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 30
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2078. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2079. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 30
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2080. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

2081. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2082. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 29
   Model Context Protocol server for Cyclops

2083. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2084. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 29
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2085. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2086. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2087. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2088. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 29
   Model Context Protocol (MCP) server that interacts with a Debugger

2089. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 29
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2090. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 29
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2091. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 29
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2092. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 29
   Sync MCP (Model Context Protocol) configurations across AI tools

2093. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2094. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2095. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2096. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 29
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2097. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 29
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2098. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 29
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2099. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 29
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2100. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

2101. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

2102. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

2103. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

2104. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 28
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2105. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 28
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2106. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2107. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 28
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2108. **[mcp](https://github.com/fastly/mcp)** - ⭐ 28
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2109. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

2110. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2111. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2112. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 28
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2113. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 28
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2114. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 28
   Model Context Protocol Server of Rod

2115. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 28
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2116. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 28
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2117. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2118. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 28
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2119. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 28
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2120. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2121. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 28
   Tools for building modern & secure MCP integrations across the client and server side

2122. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 28
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2123. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

2124. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 28
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

2125. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 28
   Asterisk Model Context Protocol (MCP) server.

2126. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 28
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2127. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 28
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2128. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2129. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 27
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

2130. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 27
   MCP (Model Context Protocol) server for biothings

2131. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

2132. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2133. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 27
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2134. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2135. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

2136. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2137. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 27
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

2138. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

2139. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 27
   Fast rust MCP proxy between stdio and SSE

2140. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 27
   Learn Model Context Protocol with Python, published by Packt

2141. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 27
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

2142. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

2143. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 27
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2144. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 27
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2145. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 27
   MCP (Model Context Protocol) Server for postgres Database

2146. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 27
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2147. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 27
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2148. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 27
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2149. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 27
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2150. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 27
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2151. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 27
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2152. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 27
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2153. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 27
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2154. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 27
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

2155. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 27
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2156. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2157. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 26
   Model Context Protocol server for Directus

2158. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

2159. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

2160. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

2161. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 26
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

2162. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

2163. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 26
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

2164. **[mcp-advisor](https://github.com/olaservo/mcp-advisor)** - ⭐ 26
   MCP Server to assist LLMs and humans on Model Context Protocol spec compliance and understanding

2165. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 26
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2166. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 26
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

2167. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

2168. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

2169. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 26
   a web logging proxy for MCP client-server communication

2170. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

2171. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 26
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

2172. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 26
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2173. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 26
   Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from data.gouv.fr, the French national Open Data platform, directly through conversation.

2174. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 26
   An implementation of Giphy integration with Model Context Protocol

2175. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 25
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2176. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

2177. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

2178. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 25
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

2179. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

2180. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 25
   Model Context Protocol to bridge in Substack writings to Claude.

2181. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

2182. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

2183. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

2184. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 25
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

2185. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2186. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

2187. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

2188. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 25
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

2189. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 25
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

2190. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 25
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2191. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 25
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2192. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

2193. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 25
   Headless IDA Pro binary analysis via Model Context Protocol

2194. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 25
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2195. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2196. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

2197. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 25
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2198. **[levante](https://github.com/levante-hub/levante)** - ⭐ 25
   Levante - Personal, Secure, Free, Local AI, MCP Client

2199. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 25
   Azure AI Foundry - Agents related sample code

2200. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 25
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

2201. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

2202. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

2203. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 25
   A generic mcp server fuzzer

2204. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

2205. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 25
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

2206. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 25
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

2207. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 25
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2208. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 25
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2209. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 25
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

2210. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 25
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2211. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 25
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

2212. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 25
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2213. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 25
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

2214. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 24
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

2215. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

2216. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

2217. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 24
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

2218. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

2219. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

2220. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

2221. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2222. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2223. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 24
   Model Context Protocol Server for NebulaGraph 3.x

2224. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

2225. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 24
   A simple Model Context Protocol (MCP) server for Clay.

2226. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

2227. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 24
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2228. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 24
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

2229. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

2230. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 24
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

2231. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

2232. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 24
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

2233. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 24
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2234. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

2235. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 24
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2236. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 24
   Simple MCP Client for remote MCP Servers 🌐

2237. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 24
   A Curated List of MCP Servers, Clients and Toolkits

2238. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 24
   Educational repo for MCP streamable HTTP servers and clients

2239. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

2240. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 24
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

2241. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 24
   PowerPlatform Model Context Protocol server

2242. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 24
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2243. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 24
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

2244. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

2245. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for GreptimeDB

2246. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 23
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2247. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

2248. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 23
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2249. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 23
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

2250. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

2251. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2252. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

2253. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 23
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

2254. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

2255. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

2256. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 23
   A Fastify plugin to run Model Context Protocol (MCP) servers

2257. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 23
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

2258. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 23
   Model Context Protocol SDK implemented in Lua for OpenResty

2259. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 23
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

2260. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

2261. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 23
   A Model Context Protocol server for 3D Slicer integration

2262. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 23
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2263. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 23
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2264. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 23
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2265. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 23
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2266. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 23
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

2267. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 23
   CLI that uses DSPy to interact with MCP servers.

2268. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

2269. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 23
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

2270. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 23
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

2271. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 23
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

2272. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

2273. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 23
   Zillow MCP Server for real estate data access via the Model Context Protocol

2274. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 23
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

2275. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 23
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2276. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

2277. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 23
   model context protocol for Autodesk Revit

2278. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

2279. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

2280. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 23
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2281. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

2282. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

2283. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 22
   A MCP(Model Context Protocol) server that accesses to Lightdash

2284. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

2285. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

2286. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

2287. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

2288. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

2289. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

2290. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

2291. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

2292. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

2293. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 22
   Python-based MCP server for BlazeMeter API — orchestrate performance-test lifecycle (create, configure, run, analyze) and manage tests, workspaces, projects & accounts via Model Context Protocol

2294. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

2295. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 22
   Model Context Protocol server for querying Cursor chat history

2296. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 22
   Model Context Protocol server for Github Repo // Reading Github Repo

2297. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 22
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2298. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 22
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

2299. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2300. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

2301. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

2302. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 22
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2303. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2304. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 22
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2305. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 22
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

2306. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 22
   Tanzu Platform Chat

2307. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

2308. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

2309. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

2310. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 22
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

2311. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 22
   Model Context Protocol server for CODESYS automation platform

2312. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

2313. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 22
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2314. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

2315. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2316. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

2317. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

2318. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

2319. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

2320. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 21
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

2321. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

2322. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

2323. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

2324. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

2325. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 21
   An MCP client for slack in Typescript

2326. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 21
   MCP agent/client/server implementation for private knowledge base

2327. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 21
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

2328. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 21
   A collection of mcp servers/client/sdks

2329. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

2330. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 21
   Simple MCP SDK in Java

2331. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 21
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

2332. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 20
   Memory Cache Server for use with supported MCP API Clients.

2333. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 20
   Haskell server/client for MCP (Model Context Protocol)

2334. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 20
   MCP server to expose local zotero repository to MCP clients 

2335. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 20
   Minimal Metals stand alone client that allows running the metals mcp server

2336. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 20
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

2337. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

2338. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 20
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

2339. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 20
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

2340. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 20
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

2341. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 20
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

2342. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 20
   CLI for calling successive MCP Server tools

2343. **[plux](https://github.com/milisp/plux)** - ⭐ 20
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

2344. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 20
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

2345. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

2346. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 20
   Command-line interface for any Model Context Protocol (MCP) server.

2347. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 19
   An MCP Server and client for communicating with Nifi (v1.28)

2348. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 19
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

2349. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 19
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

2350. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 19
   deepseek 结合 mcp 场景，最小用例，包括 client and server

2351. **[starbase](https://github.com/metorial/starbase)** - ⭐ 19
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

2352. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 19
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

2353. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 19
   Rust MCP framework for building AI agents

2354. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 19
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

2355. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

2356. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 18
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

2357. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 18
   MCP server and client for running Linux commands

2358. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 18
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

2359. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 18

2360. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 18
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

2361. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

2362. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

2363. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 18
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

2364. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 18
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

2365. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 18
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

2366. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

2367. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 18
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

2368. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 18
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

2369. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 17
   The Decodo MCP server which enables MCP clients to interface with services.

2370. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

2371. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

2372. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 17
   Pre-release - Model Context Protocol server for Rollbar

2373. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

2374. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 17
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

2375. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 17
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

2376. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 17
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

2377. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 17
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

2378. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 16
   An extensible AI agents framework

2379. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 16
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

2380. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 16
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

2381. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

2382. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 16
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

2383. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 16
   A model-agnostic MCP Client-Server for .Net and Unity

2384. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 16
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, and Slides. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

2385. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 16
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

2386. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

2387. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

2388. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 16
   LLM Function Calling Library and CLI with Support for MCP Servers

2389. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 16
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

2390. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 16
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

2391. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 16
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

2392. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

2393. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

2394. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 16
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

2395. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 16
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

2396. **[daiv](https://github.com/srtab/daiv)** - ⭐ 16
   Async SWE agents seamlessly integrated on your git platform to automate code issues implementation, reviews, and pipeline repairs.

2397. **[ACP-MCP-Server](https://github.com/GongRzhe/ACP-MCP-Server)** - ⭐ 16
   A bridge server that connects Agent Communication Protocol (ACP) agents with Model Context Protocol (MCP) clients, enabling seamless integration between ACP-based AI agents and MCP-compatible tools like Claude Desktop.

2398. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 15

2399. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 15
   An MCP server to read MCP logs to debug directly inside the client

2400. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 15
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

2401. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

2402. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 15
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

2403. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 15

2404. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 15
   Connect to any MCP servers using agents

2405. **[gno](https://github.com/gmickel/gno)** - ⭐ 15
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2406. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

2407. **[Open-MCP-Client](https://github.com/GongRzhe/Open-MCP-Client)** - ⭐ 14
   ChatMCP is a powerful command-line chat interface that connects to multiple LLM providers (OpenAI, Anthropic, Groq, etc.) and extends their capabilities with tools using the Model Context Protocol (MCP).

2408. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 14
   An MCP client that uses signal for sending and receiving messages.

2409. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 14
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

2410. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 14
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

2411. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 14
   An MCP server and client for LLMs to interact with Unity Projects

2412. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 14
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

2413. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

2414. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

2415. **[mcp-cli](https://github.com/tilesprivacy/mcp-cli)** - ⭐ 14
   Interactive CLI client for remote Model Context Protocol (MCP) servers with OAuth 2.0 support.

2416. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 14
   MCP host app w/ textual user interface, in Python

2417. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 14
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

2418. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 14
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

2419. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

2420. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

2421. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

2422. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

2423. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 13

2424. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

2425. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 13
   A web-based client for connecting to MCP servers with OAuth support

2426. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 13
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

2427. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

2428. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

2429. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 13
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

2430. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

2431. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

2432. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 13
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

2433. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 13
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

2434. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 12
   MCP server and client for Frontapp

2435. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 12
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

2436. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 12
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

2437. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 12
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

2438. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

2439. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 12
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

2440. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

2441. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 12
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

2442. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

2443. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 12
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

2444. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 12
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

2445. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

2446. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 12
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

2447. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

2448. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 12
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

2449. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 12
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

2450. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 12
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

2451. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 12
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

2452. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 12
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

2453. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 12
   Peta core: The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2454. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

2455. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 11
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

2456. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

2457. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 11
   MCP server to manage Spotify from MCP clients

2458. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 11
   MCP Client for Gemma-3

2459. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

2460. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

2461. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 11
   MCP server to give client the ability to access Wikipedia pages

2462. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 11
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

2463. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

2464. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

2465. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

2466. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

2467. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

2468. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 11
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

2469. **[goldrush-mcp-server](https://github.com/covalenthq/goldrush-mcp-server)** - ⭐ 11
   This project provides a MCP (Model Context Protocol) server that exposes Covalent's GoldRush APIs as MCP resources and tools. It is implemented in TypeScript using @modelcontextprotocol/sdk and @covalenthq/client-sdk.

2470. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 11
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

2471. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

2472. **[muster](https://github.com/giantswarm/muster)** - ⭐ 11
   MCP tool management and workflow proxy

2473. **[claude_autoapprove](https://github.com/PyneSys/claude_autoapprove)** - ⭐ 11
   Autoapprove support for claude

2474. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

2475. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 11
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

2476. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

2477. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 10
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

2478. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 10
   Documentation

2479. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

2480. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

2481. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

2482. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 10
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

2483. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

2484. **[server](https://github.com/mcpfinder/server)** - ⭐ 10
   MCPfinder 🔧🤖 is a service that enables LLMs, running through client applications that support the MCP protocol, to dynamically discover and access new tools, features, and capabilities. When a user requests functionality the AI doesn’t have, it can simply ask MCP Finder to locate relevant MCP servers, expanding its toolset in real time.

2485. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 10
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

2486. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

2487. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 10
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

2488. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 10
   A TUI to probe the calls between MCP client and server

2489. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 10
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

2490. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 10
   tool management service for performing vector tool calling at scale.

2491. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

2492. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 10
   Simple template project for controlling Unity via MCP

2493. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 10
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

2494. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 10
   A multi-agent CLI tool powered by Swarms-rs and Composio

2495. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 10
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

2496. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 10
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

2497. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 10
   Awesome list of MCP servers for interacting with hardware and the physical world.

2498. **[polaris](https://github.com/octu0/polaris)** - ⭐ 10
   Distributed AI Agent Framework

2499. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 40,537
   基于大模型搭建的聊天机器人，同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入，可选择ChatGPT/Claude/DeepSeek/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Kimi/LinkAI，能处理文本、语音和图片，访问操作系统和互联网，支持基于自有知识库进行定制企业智能客服。

2. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 15,361
   AgentScope: Agent-Oriented Programming for Building LLM Applications

3. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,186
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 8,043
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,336
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

6. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,640
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

7. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,608
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

8. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,320
   extendable code review and QA agent 🚢

9. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,635

10. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,583
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

11. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 802
   OpenTelemetry Instrumentation for AI Observability

12. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 767
   A code repository indexing tool to supercharge your LLM experience.

13. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 707
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

14. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 580
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

15. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 561
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

16. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 530
   The easiest way to discover and install MCPs

17. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 402
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

18. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 272
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

19. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 154
   Python SDK for interacting with the MCP Toolbox for Databases. 

20. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 95
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

21. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 69
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

22. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

23. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 58
   Javascript SDK for interacting with the MCP Toolbox for Databases.

24. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 53

25. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 44
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

26. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 41
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

27. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

28. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

29. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 26
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

30. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

31. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

32. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

33. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 17
   A desktop client with MCP support for Mistral LLMs

34. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

35. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 168,024
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,510
   🦍 The Cloud-Native Gateway for APIs & AI

3. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 41,255
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 26,834
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,321
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,177
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 15,737
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 14,868
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI features. ✨

9. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

10. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

11. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,445
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,482
   A cross-platform Markdown AI note-taking software.

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,315
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

14. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,414
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

15. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,396
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,736
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,538
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 7,041
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

19. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,612
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,638
   Adversary simulation and Red teaming platform with AI

21. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,433
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,151
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,111
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,032
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

25. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,001
   Bulk port forwarding Kubernetes services for local development.

26. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 3,838
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

27. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,258
   A shadcn/ui library for building ChatGPT Apps

28. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 2,714
   System Level Intelligent Router for Mixture-of-Models

29. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,688
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

30. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,530
   A highly opinionated, zero-configuration linter and formatter.

31. **[harbor](https://github.com/av/harbor)** - ⭐ 2,246
   Effortlessly run LLM backends, APIs, frontends, and services with one command.

32. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 2,144
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

33. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,871
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

34. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,727
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

35. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,698
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

36. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,460
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

37. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,414
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

38. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,392
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

39. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

40. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,301
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

41. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,263
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

42. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,261
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

43. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,146
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

44. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,098
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

45. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,074
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

46. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,065
   A single interface to use and evaluate different agent frameworks 

47. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,006
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

48. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 999
   AIPex: AI browser automation assistant, no migration and privacy first. ChatGPT Atlas Alternative, Alternative to Manus Browser Operator, Alternative to Claude Chrome

49. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 977
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

50. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 963
   Korea Investment & Securities Open API Github

51. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 952
   Arduino MCP2515 CAN interface library

52. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 763
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

53. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 725
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

54. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 696
   Solidity Static Analyzer that easily integrates into your editor

55. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 696
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

56. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 690
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

57. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 656
   A personal AI assistant for everyone

58. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 620
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

59. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 581
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

60. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 525
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

61. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 488
   Marmot helps teams discover, understand, and leverage their data with powerful search and lineage visualisation tools. It's designed to make data accessible for everyone.

62. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 449
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

63. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 448
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

64. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

65. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 420
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

66. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 417
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

67. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 409
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

68. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 385
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

69. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 384
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

70. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 383
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

71. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 382
   Minecraft: Pi Edition API Python Library

72. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 380
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

73. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

74. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 365
   Local first codebase intelligence

75. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 346
   Python toolkit for building graph-enhanced GenAI applications

76. **[exograph](https://github.com/exograph/exograph)** - ⭐ 340
   Build production-ready backends in minutes

77. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 335
   Blender python addon to increase workflow for creating minecraft renders and animations

78. **[bridle](https://github.com/neiii/bridle)** - ⭐ 333
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose)

79. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 331
   MCP for Unreal Engine 5

80. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 321
   Sega Master System / Game Gear / SG-1000 emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

81. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

82. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 319
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

83. **[amical](https://github.com/amicalhq/amical)** - ⭐ 313
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

84. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 308
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

85. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 304
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

86. **[depyler](https://github.com/paiml/depyler)** - ⭐ 297
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

87. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 292
   Software architecture tooling for the AI age

88. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 283
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

89. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 270
   An in-depth book and reference on building agentic systems like Claude Code

90. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 265
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

91. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 260
   Android App: 漢字古今中外讀音查詢

92. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 243
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

93. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 243
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

94. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 242
   AI for Ethical Hacking - Workshop

95. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 239
   Public facing repo for MCP SRG mappings.

96. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 236
   An introduction to the world of AI Agents

97. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 233
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

98. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 230
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

99. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 229
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

100. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 219
   A website to generate Minecraft profile pictures

101. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

102. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 214
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

103. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

104. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 201
   Re-usable multi part components built on React Aria and TailwindCSS. 

105. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

106. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

107. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 185
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

108. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 183
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

109. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

110. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 120
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

111. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 119
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

112. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 118
   wanna develop an app ❓

113. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 106
   Solid Tumor Associative Modeling in Pathology

114. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 101
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

115. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 71
   A lightweight, open, and extensible multi-LLM interaction studio.

116. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 69
   Unity plugin for Coplay

117. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 68
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

118. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 63
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

119. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 61
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

120. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 58
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

121. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 48
   Houdini integration through the Model Context Protocol

122. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

123. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 31
   Prompt-driven automation platform - Transform natural language into executable workflows

124. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

125. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 26
   Build AI Agent using Google ADK , MCP and Gemma 3 model

126. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 25
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具与 Wireshark 进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

127. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

128. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 24
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

129. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

130. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 14
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

131. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 13
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,617
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 6,863
   Specification and documentation for the Model Context Protocol

2. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,859
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

3. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 940
   程序员鱼皮的 AI 资源导航，汇总热门的 AI 大模型和工具，比如 Deepseek 使用指南、提示词技巧、知识干货、应用场景、AI 变现、行业资讯、教程资源等一系列内容，帮助你快速掌握 AI 技术，走在时代前沿。涉及大模型 ChatGPT、Claude、Gemini、Deepseek、QWEN、GROK 等；涉及技术 Spring AI、LangChain、RAG、MCP、A2A 等；涉及 Cursor、TRAE 等工具。本项目为开源文档版本，已升级为鱼皮AI导航网站

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 359
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

5. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 27
    A powerful system for crawling documentation websites, extracting code snippets, and providing fast search capabilities via MCP (Model Context Protocol) integration.

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

