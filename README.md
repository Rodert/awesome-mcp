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

## 📚 Projects (1847 total)

> Last updated: **2025-12-12**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 121,226
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 117,560
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[netdata](https://github.com/netdata/netdata)** - ⭐ 76,975
   The fastest path to AI-powered full stack observability, even for lean teams.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 76,494
   A collection of MCP servers.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 74,274
   Model Context Protocol Servers

6. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 69,551
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

7. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 68,965
   🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers, Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.

8. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 52,060
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

9. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 44,663
   🔥AI低代码平台，助力企业快速实现低代码开发和构建AI应用！ 成熟的AI应用平台：涵盖AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等，兼容多种大模型；提供强大代码生成器：实现前后端一键生成，无需手写代码! 引领AI开发模式：AI生成→在线配置→代码生成→手工合并，解决Java项目80%重复工作，提升效率节省成本，又不失灵活~

10. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 40,037
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

11. **[context7](https://github.com/upstash/context7)** - ⭐ 39,131
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

12. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 38,767
   🎯 告别信息过载，AI 助你看懂新闻资讯热点，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等13种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，1分钟手机通知，无需编程。支持Docker部署⭐ 让算法为你服务，用AI理解热点

13. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 37,660
   Federated query engine for AI - The only MCP Server you'll ever need

14. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 32,415
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

15. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,379
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

16. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 32,350
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

17. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 30,466
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

18. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,197
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

19. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 25,102
   GitHub's official MCP Server

20. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 24,469
   An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations.

21. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 24,251
   Playwright MCP server

22. **[goose](https://github.com/block/goose)** - ⭐ 23,815
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

23. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 23,082
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

24. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 22,296
   An MCP-based chatbot | 一个基于MCP的聊天机器人

25. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 21,084
   🚀 The fast, Pythonic way to build MCP servers and clients

26. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 20,611
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

27. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 20,559
   The official Python SDK for Model Context Protocol servers and clients

28. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 19,843
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

29. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 19,686
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

30. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 19,534
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

31. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 18,764
   The TypeScript AI agent framework. ⚡ Assistants, RAG, observability. Supports any LLM: GPT-4, Claude, Gemini, Llama.

32. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,057
   Your API ⇒ Paid MCP. Instantly.

33. **[serena](https://github.com/oraios/serena)** - ⭐ 17,067
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

34. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 16,370
   Chrome DevTools for coding agents

35. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 14,473

36. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 13,637
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

37. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,168
   :file_folder: The Dropbox like web client for SFTP, S3, FTP, WebDAV, Git, Minio, LDAP, CalDAV, CardDAV, Mysql, Backblaze, ...

38. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 12,959
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

39. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 12,640
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

40. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 12,177
   MCP server to provide Figma layout information to AI coding agents like Cursor

41. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 11,754
   MCP Toolbox for Databases is an open source MCP server for databases.

42. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,226
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

43. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 10,989
   The official TypeScript SDK for Model Context Protocol servers and clients

44. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 10,716
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

45. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 10,550
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

46. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 10,435
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

47. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,139
   Yet another WebUI for Nginx

48. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,087
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

49. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

50. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 9,511
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

51. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 9,382
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书无水印作品文件

52. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 8,536
   mcp-use is the easiest way to interact with mcp servers with custom agents

53. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,294
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

54. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 7,905
   Visual testing tool for MCP servers

55. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 7,876
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

56. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 7,871
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

57. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 7,843
   Build effective agents using Model Context Protocol and simple workflow patterns

58. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 7,784
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

59. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 7,623
   AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.

60. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 7,404
   MCP for xiaohongshu.com

61. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,145
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

62. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 6,936
   🧑‍🚀 全世界最好的LLM资料总结（语音视频生成、Agent、辅助编程、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

63. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 6,897
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

64. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 6,695
   MCP Server for Ghidra

65. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 6,330
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex & Gemini CLI.

66. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,104
   A community driven registry service for Model Context Protocol (MCP) servers.

67. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,082
   A collection of MCP clients.

68. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 5,784
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

69. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,504
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

70. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 5,266
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

71. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,130
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

72. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,129
   WhatsApp MCP server

73. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,056
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

74. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,055
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

75. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,051
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

76. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,009
   Install, run and deploy your own decentralized AI agent service

77. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 4,991
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

78. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 4,968
   Awesome MCP Servers - A curated list of Model Context Protocol servers

79. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 4,924
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

80. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 4,853
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

81. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 4,713
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

82. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,686
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

83. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 4,660
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

84. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 4,554
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

85. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,468
   Easily build AI systems with Evals, RAG, Agents, fine-tuning, synthetic data, and more.

86. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 4,399
   A model-driven approach to building AI agents in just a few lines of code.

87. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,324
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

88. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,254
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

89. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 4,232
   An MCP server that allows MCP clients like Claude Desktop or Cursor to perform actions in the Unity Editor

90. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,230
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

91. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 4,173
   Open Source TypeScript AI Agent Framework with built-in LLM Observability

92. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 4,172
   A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

93. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,150
   opensource self-hosted ai agent sandboxes

94. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,003
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

95. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,840
   The Cursor & Windsurf community, find rules and MCPs

96. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 3,779
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

97. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,768
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

98. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 3,767
   MCP server for Atlassian tools (Confluence, Jira)

99. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,746
   A simple, secure MCP-to-OpenAPI proxy server

100. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,675
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

101. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 3,607
   MCP Server for Computer Use in Windows

102. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,573
   Official Notion MCP Server

103. **[core](https://github.com/opensumi/core)** - ⭐ 3,570
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

104. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,527
   Define, Prompt and Test MCP enabled Agents and Workflows

105. **[Olares](https://github.com/beclab/Olares)** - ⭐ 3,487
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

106. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,428
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

107. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,419
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

108. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,406
   CISO Assistant is a one-stop-shop for GRC, covering Risk, AppSec, Compliance/Audit Management, Privacy and supporting +100 frameworks worldwide with auto-mapping: NIST CSF, ISO 27001, SOC2, CIS, PCI DSS, NIS2, CMMC, PSPF, GDPR, HIPAA, Essential Eight, NYDFS-500, DORA, NIST AI RMF, 800-53, CyFun, AirCyber, NCSC, ECC, SCF and so much more

109. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,381
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

110. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,376
   Exa MCP for web search and web crawling!

111. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,321
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

112. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,320
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

113. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,296
   🤖 A visualization mcp contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

114. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,265
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

115. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,240
   🔍  Semantic search your Telegram chat history | 语义化搜索您的 Telegram 聊天记录

116. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,221
   GOWA - WhatsApp REST API with support for UI, Webhooks, and MCP. Built with Golang for efficient memory use. 

117. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,194

118. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,194
   LangChain 🔌 MCP

119. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,178
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

120. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,175
   Model Context Protocol(MCP) 编程极速入门

121. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,076
   A curated list of Model Context Protocol (MCP) servers

122. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,051
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

123. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 3,020
   Memory infrastructure for LLMs and AI agents

124. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,004
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

125. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 2,975
   A Model Context Protocol (MCP) server that provides Xcode-related tools for integration with AI assistants and other MCP clients.

126. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 2,973
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

127. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 2,966
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

128. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 2,946
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

129. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 2,946
   A Model Context Protocol server for Excel file manipulation

130. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,929
   AI agent microservice

131. **[boost](https://github.com/laravel/boost)** - ⭐ 2,924
   Laravel-focused MCP server for augmenting your AI powered local development experience.

132. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,917
   n8n custom node for MCP

133. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 2,913
   Learn AI and LLMs from scratch using free resources

134. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 2,913
   Allow LLMs to control a browser with Browserbase and Stagehand

135. **[octelium](https://github.com/octelium/octelium)** - ⭐ 2,883
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

136. **[apple-mcp](https://github.com/supermemoryai/apple-mcp)** - ⭐ 2,882
   Collection of apple-native tools for the model context protocol.

137. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,814
   A TypeScript framework for building MCP servers.

138. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 2,801
   PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides [EMNLP 2025]

139. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 2,743
   Full guide on claude tips and tricks and how you can optimise your claude code the best & strive to find every command possible even hidden ones!

140. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,689
   The official Rust SDK for the Model Context Protocol

141. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 2,629
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

142. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 2,603
   RikkaHub is an Android APP that supports for multiple LLM providers.

143. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 2,581
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

144. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

145. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,527
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

146. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,523
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,and vue

147. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,522
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

148. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,510
   A CLI tool for building Go applications.

149. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,318
   Connect Supabase to your AI assistants

150. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 2,304
   UltraRAG v2: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

151. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,296
   A Model Context Protocol server for converting almost anything to Markdown

152. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,290
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

153. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,288
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

154. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,186
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

155. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,140
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

156. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,137
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

157. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,073
   A bridge between Streamable HTTP and stdio MCP transports

158. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,054
   Claude Code Subagents & Commands Collection + CLI Tool

159. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,045

160. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,035
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

161. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,001
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi, GLM, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

162. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 1,987
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

163. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 1,969
   MCP server for Grafana

164. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,956
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

165. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 1,951
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

166. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 1,944
   A Model Context Protocol server for searching and analyzing arXiv papers

167. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,932
   directory for Awesome MCP Servers

168. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 1,930
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

169. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 1,914
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

170. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,907
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

171. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,873
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

172. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 1,846
   Lemonade helps users run local LLMs with the highest performance by configuring state-of-the-art inference engines for their NPUs and GPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

173. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,817
   The official MCP server implementation for the Perplexity API Platform

174. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,780

175. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,774
   Witsy: desktop AI assistant / universal MCP client

176. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 1,768
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

177. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,746
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

178. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,738
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

179. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,729
   A secure low code honeypot framework, leveraging AI for System Virtualization. 🇮🇹

180. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,728
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

181. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 1,718
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

182. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 1,703
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB, SQLite.

183. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,662
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

184. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,658
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

185. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 1,655
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

186. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,652
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

187. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,642
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

188. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,639
   Interactive User Feedback MCP

189. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,626
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

190. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 1,626
   The missing macOS LLM server. Run local or cloud models with one API. MCP server for Cursor & Claude Desktop, menu bar chat, plugins, and dev tools. Native Apple Silicon.

191. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,626
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

192. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,595
   Make RSS 📰 great again with AI 🧠✨!!

193. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,594
   Desktop Extensions: One-click local MCP server installation in desktop apps

194. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,579
   Coding assistant MCP for Claude Desktop

195. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,559
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

196. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,497
   MCP server that provides tools and resources for interacting with n8n API

197. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,495
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

198. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,488
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

199. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,484
   Build ChatGPT Apps and MCP servers locally.

200. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,476
   An MCP server that installs other MCP servers for you

201. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,455
   🧩 The ultimate toolkit for working with APIs. 🎅🏼 HO. HO. HO.

202. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,421
   ToolHive makes deploying MCP servers easy, secure and fun

203. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,420
   Next Generation Agentic Proxy for AI Agents and MCP servers

204. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,411
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

205. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,394
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

206. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,376
   ⭐无处不在的AI桌面女友！可接入QQ、飞书、telegram、discord、b站、YouTube、twitch、Dify、 Home Assistant、MCP、A2A、Comfyui、酒馆角色卡、Cluade code等生态！⭐ AI Desktop Girlfriend Everywhere! Compatible with QQ, Feishu, Telegram, Discord, Bilibili, YouTube, Twitch, Dify, Home Assistant, MCP, A2A, ComfyUI, Tavern Character Cards, Cluade code, and more ecosystems!

207. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,371
   Standards for building agents, better

208. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,367
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

209. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,353
   A Unified MCP Server Management App (MCP Manager).

210. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,330
   Constrain, log and scan your MCP connections for security vulnerabilities.

211. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 1,315
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

212. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,308
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

213. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,307
   The Simple Agent Development Kit.

214. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,304
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

215. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,301
   MCP server for interacting with the iOS simulator

216. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,257
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

217. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,249
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

218. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,243
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

219. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,237
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

220. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,235
   Damn Vulnerable MCP Server

221. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,232
   A connector for Claude Desktop to read and search an Obsidian vault.

222. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

223. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,220
   Make your own story. User-friendly software for LLM roleplaying

224. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,209
   MCP Server for kubernetes management commands

225. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,202
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

226. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,198
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

227. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,192
   The Grafbase GraphQL Federation Gateway

228. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,188
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

229. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,181
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

230. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,172
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

231. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,172
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

232. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,168
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

233. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,167

234. **[ai](https://github.com/stripe/ai)** - ⭐ 1,151
   One-stop shop for building AI-powered products and businesses with Stripe.

235. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,137
   The TypeScript MCP framework

236. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,135
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for OpenAI, Gemini, Claude, Deepseek and Grok interoperability

237. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,131
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

238. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,128
   The official Swift SDK for Model Context Protocol servers and clients.

239. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,117
   The AI toolkit for the AI developer

240. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,115
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

241. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,113
   An official Qdrant Model Context Protocol (MCP) server implementation

242. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,112
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

243. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,095
   A Ruby Implementation of the Model Context Protocol

244. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,092
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

245. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,092
   The official ElevenLabs MCP server

246. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,084
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

247. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,084
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

248. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,081
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

249. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,075
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

250. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,069
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

251. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,061
   docker mcp CLI plugin / MCP Gateway

252. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,056
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

253. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,056
   Build, evaluate and train General Multi-Agent Assistance with ease

254. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,038
   Paper Debugger is the best overleaf companion

255. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,030
   告别AI提前终止烦恼，助力AI更加持久

256. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,027
   A web UI for Claude Code agents

257. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,026
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

258. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

259. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,025
   Query and Summarize your chat messages.

260. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,021
   On-premises conversational RAG with configurable containers

261. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,021
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

262. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,018
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

263. **[use-mcp](https://github.com/modelcontextprotocol/use-mcp)** - ⭐ 1,009

264. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,002
   MCP Python Tutorial 

265. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 991
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

266. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 989
   Production ready MCP server with real-time search, extract, map & crawl.

267. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 988
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

268. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 988
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server

269. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 987
   The most powerful MCP Slack Server with no permission requirements, Apps support, multiple transports Stdio and SSE, DMs, Group DMs and smart history fetch logic.

270. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 976
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

271. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 975
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

272. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 973
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

273. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 964
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

274. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 956
   Remote MCP Servers

275. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 953
   Claude Code as one-shot MCP server to have an agent in your agent.

276. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 953

277. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 948
   Bringing the power of MCP to the web

278. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 948
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

279. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 940
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

280. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 937
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

281. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 932
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

282. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 932
   MCP server for fetch web page content using Playwright headless browser.

283. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 927
    Universal MCP memory service with semantic search, multi-client support, and autonomous consolidation for Claude Desktop, VS Code, and 13+ AI   applications

284. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 920
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

285. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 914
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

286. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 904
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

287. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 898
   A repository of servers and clients from the Model Context Protocol tutorials

288. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 885
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

289. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 882
   A middleware to provide an openAI compatible endpoint that can call MCP tools

290. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 879
   MCP server helping models to understand your Vite/Nuxt app better.

291. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 879
   A framework for writing MCP (Model Context Protocol) servers in Typescript

292. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 878
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

293. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 874
   Expose llms-txt to IDEs for development

294. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 874
   Connect AI models like Claude & GPT with robots using MCP and ROS.

295. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 868
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

296. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 865
   A library for communication with a Minecraft client/server.

297. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 860
   Allow AI to wade through complex OpenAPIs using Simple Language

298. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 855
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

299. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 853

300. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 853
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

301. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 852
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

302. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 850
   A concise list for mcp servers

303. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 850

304. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 848
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

305. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 842
   Model Context Protocol with Neo4j

306. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 841
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

307. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 840

308. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 839
   Grounded Docs MCP Server: Enhance Your AI Coding Assistant 

309. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 837
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

310. **[tools](https://github.com/strands-agents/tools)** - ⭐ 837
   A set of tools that gives agents powerful capabilities.

311. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 837
   A security scanner for your LLM agentic workflows

312. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 835
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

313. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 835
   Model Context Protocol for WinDBG

314. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 832
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

315. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 831
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

316. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 822
   APIM ❤️ AI - This repo contains experiments on Azure API Management's AI capabilities, integrating with Azure OpenAI, AI Foundry, and much more 🚀 . New workshop experience at https://aka.ms/ai-gateway/workshop

317. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 818
   A minimalistic MCP client with a good feature set.

318. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 818
   First gitlab mcp for you

319. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 815
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

320. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 812
   🪐 ✨ Model Context Protocol (MCP) Server for Jupyter.

321. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 811
   Eliminate hallucinations from your AI agents.

322. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 807
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

323. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 804
   MCP integration for Google Calendar to manage events.

324. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 803
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

325. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 799

326. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 799
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

327. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 797
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

328. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 796
   Simple, modular, and observable Go framework for backend applications.

329. **[context-space](https://github.com/context-space/context-space)** - ⭐ 793
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

330. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 789
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

331. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 787
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

332. **[agents](https://github.com/inkeep/agents)** - ⭐ 786
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

333. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 783
   Browse the web, directly from Cursor etc.

334. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 781
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

335. **[server](https://github.com/php-mcp/server)** - ⭐ 781
   Core PHP implementation for the Model Context Protocol (MCP) server

336. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 777
   Plugin for JADX to integrate MCP server

337. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 776
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

338. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 775
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

339. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 774
   OpenAPI Tool Servers

340. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 769
   The best way to create, deploy, and share MCP Servers

341. **[runno](https://github.com/taybenlor/runno)** - ⭐ 754
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

342. **[Context](https://github.com/indragiek/Context)** - ⭐ 749
   Native macOS client for Model Context Protocol (MCP)

343. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 747
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

344. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 743
   Vibetest MCP - automated QA testing using Browser-Use agents

345. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 742
   Chat with your Kubernetes Cluster using AI tools and IDEs like Claude and Cursor!

346. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 741
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

347. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 738
   LLDB MCP Integration + other helpful commands

348. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 737
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

349. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 733
   Self-hosted MCP Gateway and Registry for AI agents

350. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 725
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

351. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 721
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

352. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 716
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

353. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 715
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

354. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 714
   An MCP server for interacting with the Financial Datasets stock market API.

355. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 713
   一个将ACE(Augment Context Engine) 做成MCP的项目

356. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 708
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

357. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 705
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

358. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 704
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

359. **[wordpress-mcp](https://github.com/Automattic/wordpress-mcp)** - ⭐ 693
   WordPress MCP — This repository will be deprecated as stable releases of mcp-adapter become available. Please use https://github.com/WordPress/mcp-adapter for ongoing development and support.

360. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 685
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

361. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 682
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

362. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 681
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

363. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 676
   All in one vscode plugin for mcp developer

364. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 675
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

365. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 667
   Scan MCP servers for potential threats & security findings.

366. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 664
   Build MCP Agents

367. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 663
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

368. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 662
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

369. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 661
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

370. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 656
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

371. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 656
   MCP server for Docker

372. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 656
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

373. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

374. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 655
   A flexible HTTP fetching Model Context Protocol server.

375. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 655
   A simple CLI to run LLM prompt and implement MCP client.

376. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 650
   A MCP server implementation for hyperbrowser

377. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 650
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

378. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 648
   Clojure MCP

379. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 647
   A secure local sandbox to run LLM-generated code using Apple containers

380. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 638
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

381. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 637
   Laravel API for Ai Agents and humans.

382. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 635
   Querying local documents, powered by LLM

383. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 634
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

384. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 634
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles and companies, get your recommended jobs, and perform job searches.

385. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 631
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

386. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 629
   EnrichMCP is a python framework for building data driven MCP servers

387. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 628
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

388. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 627
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

389. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 625
   Shell and coding agent on claude desktop app

390. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 620
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

391. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 617
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

392. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 614
   Connect ClickHouse to your AI assistants.

393. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 614
   An MCP server that provides control over Android devices via adb

394. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 613
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

395. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 609
   Talk to a Cloudflare Worker from Claude Desktop!

396. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 609
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

397. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 607
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

398. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 604
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

399. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 598
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

400. **[mcp](https://github.com/laravel/mcp)** - ⭐ 593
   Rapidly build MCP servers for your Laravel applications.

401. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 590
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

402. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 586
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

403. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 586
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

404. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 585
   A simple MCP server for Obsidian

405. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 583
   mem-agent mcp server

406. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 580
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

407. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 580
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

408. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 579
   Convert Any OpenAPI V3 API to MCP Server

409. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 579
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

410. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 577
   Daydreams is a set of tools for building agents for commerce

411. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 577
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

412. **[tome](https://github.com/runebookai/tome)** - ⭐ 572
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

413. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 571
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

414. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 567
   LangGraph solution template for MCP

415. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 567
   The Intelligence Layer for AI agents. Connect your models, tools, and data to create agentic apps that can think, act and talk to you.

416. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 563

417. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 561
   MCP Server For Turkish Legal Databases

418. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 560
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

419. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 557
   gcloud MCP server

420. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 553
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

421. **[samples](https://github.com/strands-agents/samples)** - ⭐ 552
   Agent samples built using the Strands Agents SDK.

422. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 549
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

423. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 542
   MCP to connect your LLM with Spotify.

424. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 535
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

425. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 532
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

426. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 531
   Security scanner for MCP servers

427. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 530
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

428. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 529

429. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 528

430. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 528

431. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 526
   MCP server for interacting with Neon Management API and databases

432. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 523
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

433. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 523

434. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 523
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

435. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 520
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

436. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 512
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

437. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 511
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

438. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 511
   An MCP server to query any Postgres database in natural language.

439. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 510

440. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 507
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

441. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 506
   An MCP Multimodal AI Agent with eyes and ears!

442. **[ethora](https://github.com/dappros/ethora)** - ⭐ 506
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

443. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 505
   A curated list of Model Context Protocol (MCP) servers 

444. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 503
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

445. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 503
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

446. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 502
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

447. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 502
   An Mcp client inside Emacs

448. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 502

449. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 501
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

450. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 498
   Yes Mcp server in bash

451. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 498
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

452. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 498
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, reproducible workflows, and interactive assistance.

453. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 497

454. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 496
   A Model Context Protocol server for IDA

455. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 495
   A MCP server for Home Assistant

456. **[obot](https://github.com/obot-platform/obot)** - ⭐ 494
   Enterprise MCP Platform

457. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 494
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

458. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

459. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 493
   MCP server for querying Apple Health data with natural language and SQL

460. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 491

461. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 490
   微信读书MCP

462. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 489
   A comprehensive collection of Model Context Protocol (MCP) servers

463. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 487
   The .NET library to build AI agents with 25+ built-in connectors.

464. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 486
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

465. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 483
   MCP server to deploy apps to Cloud Run

466. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 481

467. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 481
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

468. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 480
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

469. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 478
   MCP Monitoring with eBPF

470. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 478

471. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 478
   A tool that converts OpenAPI specifications to MCP server

472. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 477
   提取抖音无水印视频链接，视频文案，douyin-mcp-server

473. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 476
   A Model-Context Protocol Server for YouTube

474. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 474
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

475. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 474
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

476. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 473
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

477. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 471
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

478. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 470
   Aser is a lightweight, self-assembling AI Agent frame.

479. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 468
   An MCP server for interacting with Sentry via LLMs.

480. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 468
   MCP server for document format conversion using pandoc.

481. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 465
   MCP Server to interact with Google Gsuite prodcuts

482. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 464
   An SDK building Laravel MCP servers

483. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 464
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

484. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 462
   The better playwright MCP: works as a browser extension. No context bloat. More capable.

485. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 461
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

486. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 461
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

487. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 461
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

488. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

489. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 458
   Next.js Development for Coding Agent

490. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 457
   Open Source Voice Agent Platform

491. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 453
   MCP to allow AI agents to control Unreal

492. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 450
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

493. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 450
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

494. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 449
   Draw.io Model Context Protocol (MCP) Server

495. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 448
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

496. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 447
   Install, manage and develop MCP servers

497. **[argo](https://github.com/xark-argo/argo)** - ⭐ 442
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

498. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 441
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

499. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 438
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

500. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 438
   LLM + MCP + RAG = Magic

501. **[director](https://github.com/director-run/director)** - ⭐ 434
   MCP Playbooks for AI agents

502. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 433
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

503. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 433
   A docker MCP Server (modelcontextprotocol)

504. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 432
   A MCP (Model Context Protocol) server for interacting with dbt.

505. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 430
   MCP server integration for DaVinci Resolve

506. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 429
   Govern & Secure your AI

507. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 428

508. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 425
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

509. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 423
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

510. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 421
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, dynamic model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model parameters configuration, custom system prompt and saved preferences. Built for developers working with local LLMs.

511. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 418
   Send emails directly from Cursor with this email sending MCP server

512. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 417
   MCP Server for Istanbul Stock Exchange and Turkish Investment Fund Data

513. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 417
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

514. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 415
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

515. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 414
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

516. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 413
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

517. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 413

518. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 413
   Unlock 650+ MCP servers tools in your favorite agentic framework.

519. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 411
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

520. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 411
   Spec-Driven Development MCP Server, not just Vibe Coding

521. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 408
   Make your meetings accessible to AI Agents

522. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 408
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

523. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 405
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

524. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 402
   小红书MCP服务 x-s x-t js逆向

525. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 402

526. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 401
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

527. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 400
   The safest way to make REST calls in C# with an MCP Generator

528. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 400
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

529. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 397
   A CLI inspector for the Model Context Protocol

530. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 396
   FreeCAD MCP(Model Context Protocol) server

531. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 394
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

532. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 393
   An experiment in software planning using MCP

533. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 393
   MCP Server for Burp

534. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 392
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

535. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 389
   Flux Operator is a Kubernetes controller for managing the lifecycle of Flux CD

536. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 388
   A simple, locally hosted Web Search MCP server for use with Local LLMs

537. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 387
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

538. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 387
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

539. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 387
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

540. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 386
   MCP configuration to connect AI agent to a Linux machine.

541. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 384
   MCP server that execute applescript giving you full control of your Mac

542. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 384
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

543. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 381
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

544. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 380
   MCP Server for Metasploit

545. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 380
   基于NET搭建-AI智能体-现代化Saas企业级前后端分离架构-开启智能应用的无限可能：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR验证码识别、API多版本兼容、单元集成测试、RabbitMQ

546. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 378
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

547. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 377
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

548. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 377
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

549. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 377
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

550. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 376
   Local Groq Desktop chat app with MCP support

551. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 376
   AI-Powered Autonomous Penetration Testing Platform - Built with Golang, featuring hundreds of built-in security tools, flexible custom tool extensions, and intelligent AI decision-making through MCP protocol, making security testing as simple as a conversation.

552. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 374
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

553. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 374
   An MCP extension for Ghidra

554. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 373
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

555. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 373
   Memento MCP: A Knowledge Graph Memory System for LLMs

556. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 372
   MCP server for DuckDB and MotherDuck

557. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 372
   BioMCP: Biomedical Model Context Protocol

558. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 371
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

559. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 370
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

560. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 369
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

561. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 369
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

562. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 368
   Official Docker MCP registry 

563. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 368
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

564. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 366
   Model Context Protocol (MCP) Server for Graphlit Platform

565. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 366
   Baidu Map MCP Server

566. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 365
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

567. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 365
   MCP server connecting to Kubernetes

568. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 364
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

569. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 364
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

570. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 364
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

571. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 363
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

572. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 362
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

573. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 361
   Model Context Protocol SDK for PHP

574. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 360
   MCP-NixOS - Model Context Protocol Server for NixOS resources

575. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 360
   MCP Server for SearXNG

576. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 358
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

577. **[station](https://github.com/cloudshipai/station)** - ⭐ 358
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

578. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 355
   MCP Server for code graph analysis and visualization by CodeGPT

579. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 355
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

580. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 352
   MCP integration platforms making AI-Agents developers focusing on their own tasks

581. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 351
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

582. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 350
   A fully functional MCP server and CLI for YouTube

583. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 350
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

584. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 347
   Search Airbnb using your AI Agent

585. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 347
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

586. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 347
   MCP server that provides LLMs with tools for interacting with EVM networks

587. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 347
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

588. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 346
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

589. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 346
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

590. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 346
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

591. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 346
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

592. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 344
   Model Context Protocol (MCP) implementation in Rust

593. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 344
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的专有领域智能聊天助手

594. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 343
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

595. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 343
   Making docling agentic through MCP

596. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 342
   MCP Server implementation for Ableton Live OSC control

597. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 342
   Enterprise-ready MCP gateway, MCP registry & orchestrator

598. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 341
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Cognito integration.

599. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 339
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

600. **[daan](https://github.com/pluveto/daan)** - ⭐ 339
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

601. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 338
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

602. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 338
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

603. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 338
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

604. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

605. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 337
   lunar.dev: Ground Control for 3rd Party APIs

606. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 336
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

607. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 336
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

608. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 336
   Model Context Protocol server for GraphQL

609. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 335
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

610. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 335
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

611. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 335
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

612. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 335
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

613. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 335
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

614. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 335
   Official Jina AI Remote MCP Server

615. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 334
   MCP server for Todoist integration enabling natural language task management with Claude

616. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 334
   MCP Server implementation for Xcode integration

617. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 332
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

618. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 332
   AI-based stock analysis and trading system

619. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 331
   Up-to-date documentation for devs and AI agents.

620. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 330
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! Supports Claude Desktop, Dashscope & Cursor.

621. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 329
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

622. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 329
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

623. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 328
   F2C MCP Server

624. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 327
   A macOS AppleScript MCP server

625. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 327
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

626. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 326
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

627. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 325
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

628. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 324
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

629. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 323
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

630. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 322
   Elixir Model Context Protocol (MCP) SDK

631. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 321

632. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 319
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models. v0.2.8

633. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 319
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

634. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 317
   This is a Minecraft Base Client

635. **[moling](https://github.com/gojue/moling)** - ⭐ 317
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

636. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 316
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

637. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 314
   Repo of skills for autogen studio using model context protocol (mcp)

638. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 314
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

639. **[emcee](https://github.com/mattt/emcee)** - ⭐ 314
   MCP generator for OpenAPIs 🫳🎤💥

640. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 314

641. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 312
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

642. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 312
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

643. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 311
   An MCP implementation for Selenium WebDriver

644. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 310
   An MCP server for Azure DevOps

645. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 309
   Nuwax AI - Easily build and deploy your private Agentic AI solutions.  智能体智能应用一站式搭建平台，无需编程基础，构建你的MCP、工作流、智能体，还可一句话生成智能应用，从想法到实现只差1分钟.

646. **[mcp](https://github.com/IBM/mcp)** - ⭐ 309
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

647. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 309

648. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 309
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

649. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 308
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

650. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 307
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

651. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 307
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

652. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 306
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

653. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 304
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

654. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 304
   飞书/Lark官方 OpenAPI MCP

655. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 303
   AI-Powered Revit Modeling

656. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 302
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

657. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

658. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 301
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

659. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 300
   Turn any openapi file into an mcp server, with just the tools you need.

660. **[codexia](https://github.com/milisp/codexia)** - ⭐ 300
   A powerfull GUI and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

661. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 300
   A working pattern for SSE-based MCP clients and servers

662. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 297
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

663. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 296
   A Model Context Protocol server for building an investor agent

664. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 296
   MCP server to expose VS Code editing features to an LLM for AI coding

665. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 295
   api router for MCP Servers

666. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 295
   deep, reliable and confidential coding-context

667. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 294
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

668. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 293
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

669. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 292
   Xiaozhi MCP sample program

670. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 291
   Mapbox Model Context Protocol (MCP) server

671. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 291
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

672. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 291
   Deep Research for Code & Files

673. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 290
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

674. **[mcp-nodejs-debugger](https://github.com/workbackai/mcp-nodejs-debugger)** - ⭐ 289
   🐞 MCP Node.js debugger

675. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 289
   MCP implementation of Claude Code capabilities and more

676. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 288

677. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 287

678. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 286
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

679. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 286
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

680. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 286
   A model-driven approach to building AI agents in just a few lines of code. 

681. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 285
   Minimal MCP Server for Aider

682. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 285
   Model Context Protocol server for DeepSeek's advanced language models

683. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 285
   An implementation of Model Context Protocol (MCP) server for Argo CD.

684. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 285
   MCP server for OpenAI o3 web search

685. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 285
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

686. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

687. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 282
   hydra-ai

688. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 281
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

689. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 281
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

690. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 278

691. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 278
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

692. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 278
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

693. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 277
   Discover Exceptional MCP Servers

694. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 275
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

695. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 275

696. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 275
   The specification for the Universal Tool Calling Protocol

697. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 275
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

698. **[consult7](https://github.com/szeider/consult7)** - ⭐ 275
   MCP server to consult a language model with large context size

699. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 274

700. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 274
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

701. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 273
   simple web ui to manage mcp (model context protocol) servers in the claude app

702. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 272
   Model Context Protocol (MCP) Server for dify workflows

703. **[generator](https://github.com/context-hub/generator)** - ⭐ 272
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

704. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 272
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

705. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 271
   Control your Android devices with AI using Model Context Protocol

706. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 271
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

707. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 271
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

708. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

709. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 269
   First AI‑enabled open-source Human Capital Management system that you can start using today.

710. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 269
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

711. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 269
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

712. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 268
   A Model Context Protocol Server for MongoDB

713. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 268
   MCP server for browser automation using Playwright

714. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 268
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

715. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 268
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

716. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 268
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

717. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 268
   SonarQube MCP Server

718. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 267
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

719. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 266
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

720. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 266
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

721. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 265
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

722. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 264
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

723. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 263
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

724. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 263
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

725. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 262
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

726. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 262
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

727. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 261
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

728. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 261
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

729. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 259
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

730. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 259
   MaverickMCP - Personal Stock Analysis MCP Server

731. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 258
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

732. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 258
   Proximity is a MCP security scanner powered with NOVA

733. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 257
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

734. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 257
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

735. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 257
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

736. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 256
   MCP server for Windows OS automation

737. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 256

738. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 255
   Source code of minecraft 1.12

739. **[gemini-flow](https://github.com/clduab11/gemini-flow)** - ⭐ 254
   rUv's Claude-Flow, translated to the new Gemini CLI; transforming it into an autonomous AI development team.

740. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

741. **[mesh](https://github.com/decocms/mesh)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

742. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 252
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

743. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 251
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

744. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 250
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

745. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 248
   An MCP server providing tools for image processing operations

746. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 248
   Agentic RAG for any scenario. Customize sources, depth, and width

747. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 247
   MCP server(s) for Aipolabs ACI.dev

748. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 247
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

749. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 247
   Obsidian MCP (Model Context Protocol) Server

750. **[api200](https://github.com/API-200/api200)** - ⭐ 246
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

751. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 246
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

752. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 245
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

753. **[mcp](https://github.com/oracle/mcp)** - ⭐ 245
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

754. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 244
   A code reasoning MCP server, a fork of sequential-thinking

755. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 244
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

756. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 243
   Home Assistant MCP Server

757. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 243
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

758. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 242
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

759. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

760. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 241
   A Production-Ready Runtime Framework for Agent Deployment and Tool Sandbox

761. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 240
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

762. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 240
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

763. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 240
   MCP server implementation for Google's Gemini API

764. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 240
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

765. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 239
   MCP Server for Odoo

766. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 238
   Pixelize the real world on-chain

767. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 238
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

768. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 237
   Model Context Protocol server implementation for Reddit

769. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 237
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

770. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 237
   mcp manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent, mcphub

771. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 236
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

772. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 235
   Apollo MCP Server

773. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 234
   Easy guide to installing Claude Code MCPs globally on your machine.

774. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 234
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

775. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 233
   Simplified Gemini for Claude Code. 

776. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 233
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

777. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 233
   MCP server for JADX-AI Plugin

778. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 233
   An MCP server for loading skills (shim for non-claude clients).

779. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 232

780. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 232
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

781. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 232
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. What makes it popular:

782. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 231
   Code Runner MCP Server

783. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 231
   MCP Interface for Video Jungle

784. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 230
   🔥 Model Context Protocol (MCP) server for Firebase.

785. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 230
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

786. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 230
   MCP Server for interacting with Salesforce instances

787. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 229
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

788. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 229
   Turn any MCP server into a Python module

789. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 229
   Creates a simple MCP tool server with "streaming" HTTP.

790. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 229
   The evaluation benchmark on MCP servers

791. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 229
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

792. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 229
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

793. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 228

794. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 228
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

795. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 227
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

796. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 227
   Apache Doris MCP Server

797. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 226
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

798. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 226
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

799. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 225
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

800. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 224
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

801. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 224
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

802. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 223
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

803. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 223
   An MCP server for Massive.com Financial Market Data

804. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 223
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

805. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 222
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

806. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 221
   An experimental MCP Server for foundry built for Solidity devs

807. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 220
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

808. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 220
   小智AI客户端，目前主要用于MCP的对接

809. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 219

810. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

811. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 219

812. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 219
   A collection of MCP servers

813. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 219
   A Model Context Protocol (MCP) server that enables natural language queries to databases

814. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 219
   MCP Server for Tree-sitter

815. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 218
   MCP Server for Telegram

816. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 216

817. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 216
   MCP server for Bazi (八字) information

818. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 215
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

819. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 215
   A Model Context Protocol (MCP) server for interacting with Twitter.

820. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 215
   Semantic code searcher and codebase utility with AI memory onboard

821. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 214
   Model Context Protocol server to run commands

822. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 213
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

823. **[dat](https://github.com/hexinfo/dat)** - ⭐ 213
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

824. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 212
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

825. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 212
   A TypeScript SSE proxy for MCP servers that use stdio transport.

826. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 212
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

827. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 212
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

828. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 211
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

829. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 211
   An MCP server that indexes local code into a graph database to provide context to AI assistants.

830. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 210
   Agent MCP for ffmpeg

831. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 210
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

832. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 210
   A ReAct-Based Highly Robust Autonomous Agent Framework.

833. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 210
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

834. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 210
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

835. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 210
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

836. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 210
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

837. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 210
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

838. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 209

839. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 209

840. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 209
   Razorpay's Official MCP Server

841. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 209

842. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 209
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

843. **[mq](https://github.com/harehare/mq)** - ⭐ 209
   jq-like command-line tool for markdown processing

844. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 207
   ModelContextProtocol for Figma's REST API

845. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 207

846. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 207
   mindmap, mcp server, artifact

847. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 207
   CAD MCP Server

848. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 206
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

849. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 206
   A Multi-modal MCP client for voice powered agentic workflows

850. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 206
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

851. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 206
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

852. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 206
   SpringAI，LLM，MCP，Embedding

853. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 206
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

854. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 205
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

855. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 205
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

856. **[lokka](https://github.com/merill/lokka)** - ⭐ 205
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

857. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 205
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

858. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 204
   MCP security wrapper

859. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 204
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

860. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 204
   AWS MCP Proxy Server

861. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 203
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

862. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 203
   Model Context Protocol tool support for LangChain

863. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 203
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

864. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 202
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

865. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 202
   Volcengine MCP Servers

866. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 201
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

867. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 201
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP & STDIO) enabling cross-platform AI memory,   multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that  evolves with your work.

868. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 201
   Playwright MCP fork that works with Cloudflare Browser Rendering

869. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 201
   Model Context Protocol Servers for Milvus

870. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 201
   Lightweight MCP Server for interacting with Android Operating System.

871. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 200
   Lightweight C++ MCP (Model Context Protocol) SDK

872. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 200

873. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 199

874. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 199
   Zerodha Kite MCP server

875. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 198
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

876. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 198
   Run and monitor MCP servers locally

877. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 198
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

878. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 198
   An MCP server to use Sora video generation APIs

879. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 198
   MCP server for Claude to access Outlook data via Microsoft Graph API

880. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 198
   Standalone Roblox Studio MCP Server

881. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 197
   A Tiny Terminal Chat App for AI Models with MCP Client Support

882. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 197
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

883. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 196
   Lightweight MCP server for Spotify

884. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

885. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 195
   A MCP Server for the RAG Web Browser Actor

886. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 195
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

887. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 195
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

888. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 194
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

889. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 194
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

890. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 193
   Pure Rust implementation of MCP server for headless terminal 

891. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 192
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

892. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 192
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

893. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 192
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

894. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 192
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

895. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 192
   R MCP Server

896. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 192
   Java AI（智能体） 全场景应用开发框架（LLM，Function Call，RAG，Embedding，Reranking，Flow，MCP Server，Mcp Client，Mcp Proxy）。同时兼容 java8 ~ java25。也可嵌入到 SpringBoot2、jFinal、Vert.x 等框架中使用。。支持 MCP_2025_03_26（mcp streamable）

897. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 191
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

898. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 191
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

899. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 191
   🔎 A MCP server for Unsplash image search.

900. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 191

901. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 191
   Penpot MCP server

902. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 190
   Absurdly easy Model Context Protocol Servers in Typescript

903. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 190
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

904. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 190
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

905. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 190
   MCP server for Anki via AnkiConnect

906. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 189
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

907. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 189
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

908. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 189
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

909. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 189
   Lean Theorem Prover MCP

910. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 188
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

911. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 188
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

912. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

913. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

914. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

915. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 187
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

916. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 187
   MCP server for Claude / Cursor building n8n workflow 

917. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 187
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

918. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 187
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

919. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 186

920. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 186
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

921. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 186
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

922. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 186
   MCP server for searching and retrieving Claude Agent Skills using vector search

923. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 185
   多平台 文生图/图生图 等能力接入MCP

924. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 185
   Manage / Proxy / Secure your MCP Servers

925. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 185
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

926. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

927. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 184
   MCP for Proxmox integration in Cline

928. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 184
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

929. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 184
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

930. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 183
   Supabase MCP server created in Python.

931. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 183
   A SEC EDGAR MCP (Model Context Protocol) Server

932. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 183
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

933. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 182
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

934. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

935. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

936. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 182
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

937. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 182
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

938. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 181
   A TypeScript framework for building MCP servers elegantly

939. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 181
   MCP server for Dynatrace Observability

940. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 181
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

941. **[siconos](https://github.com/siconos/siconos)** - ⭐ 180
   Simulation framework for nonsmooth dynamical systems

942. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 179
   这是一个专为开发企业级MCP server而设计的通用开发框架

943. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 179
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

944. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 178
   Model Context Protocol Servers in Quarkus

945. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

946. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 178
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

947. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

948. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 178
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

949. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 176
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

950. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 176
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

951. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 173
   A mongo db server for the model context protocol (MCP)

952. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 173
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

953. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 173
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

954. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 172
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

955. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 166
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

956. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 166
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

957. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 164
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

958. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 164
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

959. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 163
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

960. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 161
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

961. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 160
   MCP (Model Context Protocol) server for Weaviate

962. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 157
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

963. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 156
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

964. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 156
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

965. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 155
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

966. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 155
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

967. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 155
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

968. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 154
   Sketchup Model Context Protocol

969. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 153
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

970. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 149
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

971. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 149
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

972. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 148
   Let LLMs control embedded devices via the Model Context Protocol.

973. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 148
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

974. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 147
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

975. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 147
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

976. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 145
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

977. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 144
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

978. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 144
   Model Context Protocol server implementation for Figma API

979. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 143
   Model Context Protocol (MCP) server for constraint optimization and solving"

980. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 143
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

981. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 141
   Connect any Open Data to any LLM with Model Context Protocol.

982. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 141
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

983. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 139
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

984. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 139
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

985. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 139
   Model Context Protocol For R

986. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 138
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

987. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 137
   A Model Context Protocol server for MySQL database operations

988. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 136
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

989. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 136
   A Model Context Protocol server for calculating.

990. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 133
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

991. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 132
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

992. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 132
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

993. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 132
   StarRocks MCP (Model Context Protocol) Server

994. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 131
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

995. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 131
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

996. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 131
   A list of MCP (Model Context Protocol) servers for developer tools and services

997. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 129
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

998. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 129
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

999. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 128
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1000. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 128
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1001. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 126
   A Model Context Protocol server implementation for operations on AWS resources

1002. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 125
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1003. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 124
   Buttplug.io Model Context Protocol (MCP) Server

1004. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 124
   Model Context Protocol (MCP) server for the Zotero API, in Python

1005. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 124
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1006. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 123
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1007. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 123
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1008. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 122
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1009. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 122
   Dart AI Model Context Protocol (MCP) server

1010. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 122
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1011. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 122

1012. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 120
   A Model Context Protocol server that provides access to BigQuery

1013. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 120
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1014. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 120
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1015. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 119
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1016. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 119
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1017. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 118
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1018. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 117
   Model Context Protocol (MCP) with TikTok integration

1019. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 117
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1020. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 117
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1021. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 114
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1022. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 114
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1023. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1024. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 113
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

1025. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 112
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1026. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) for Jupyter Notebook

1027. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1028. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 111
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1029. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1030. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 110
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1031. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 109
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1032. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 109
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1033. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 109
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1034. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 109
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1035. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 108
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1036. **[modex](https://github.com/theronic/modex)** - ⭐ 108
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1037. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 107
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1038. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 107
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1039. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 107
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1040. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 106
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1041. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 106
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1042. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 105
   Model Context Protocol Server for Swift

1043. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1044. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 104
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1045. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 103
   A Model Context Protocol Server to manipulate *.xcodeproj

1046. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 103
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1047. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 103
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1048. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 103
   MariaDB MCP (Model Context Protocol) server implementation

1049. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 102
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1050. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1051. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 102
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1052. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 102
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1053. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 101
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1054. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 101
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1055. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 101
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1056. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 100
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1057. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 100
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1058. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 99
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1059. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1060. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 98
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1061. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 98
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1062. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 98
   Collection of examples of how to use Model Context Protocol with AWS.

1063. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 97
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1064. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 97
   💎 A Ruby implementation of the Model Context Protocol

1065. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 97
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1066. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 97
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1067. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 96
   Node.js Client Implementation for Model Context Protocol (MCP)

1068. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 96
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1069. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 96
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1070. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 96
   A Google Tasks Model Context Protocol Server for Claude

1071. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 95
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1072. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 94
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1073. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 94
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1074. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 94
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1075. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 94
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1076. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 94
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1077. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 94
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1078. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 94
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1079. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 93
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1080. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 93
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1081. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 92
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1082. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 92
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1083. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 91
   This is a Ruby implementation of MCP (Model Context Protocol) client

1084. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 91
   Model Context Protocol server for Replicate's API

1085. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1086. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 89
   Model Context Protocol (MCP) server for the Webflow Data API.

1087. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 89
   A Model Context Protocol (MCP) server for square

1088. **[mcp-web-ui](https://github.com/MegaGrindStone/mcp-web-ui)** - ⭐ 88
   MCP Web UI is a web-based user interface that serves as a Host within the Model Context Protocol (MCP) architecture. It provides a powerful and user-friendly interface for interacting with Large Language Models (LLMs) while managing context aggregation and coordination between clients and servers.

1089. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 87
   A Model Context Protocol (MCP) server providing access to Google Search Console

1090. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 87
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1091. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 87
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1092. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 86
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1093. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 86
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1094. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 85
   A model-context-protocol server for molecules.

1095. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1096. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1097. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 85
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1098. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 84
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1099. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 84
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1100. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 84
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1101. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 83
   Ragie Model Context Protocol Server

1102. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 83
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1103. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 83
   A Model Context Protocol server that provides knowledge graph management capabilities.

1104. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 83
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1105. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 82
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1106. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 82
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1107. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 82
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1108. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 82
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1109. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 81
   Model Context Protocol (MCP) Server for the Keboola Platform

1110. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1111. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1112. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 81
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1113. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 81
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1114. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 79
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1115. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 78
   A model context protocol server that connects to Anki through AnkiConnect

1116. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 78
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1117. **[identity](https://github.com/agntcy/identity)** - ⭐ 78
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1118. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 78
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1119. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 78
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1120. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 78
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1121. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 77
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1122. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 77
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1123. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 76
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1124. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 76
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1125. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 75
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1126. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1127. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 75
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1128. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 75
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1129. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 74
   Model Context Protocol (MCP) Client for Apify's Actors

1130. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 74
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1131. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 74
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1132. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1133. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 74
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1134. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 73
   A WooCommerce (MCP) Model Context Protocol server

1135. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 73
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1136. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 73
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1137. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 73
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1138. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 73
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1139. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1140. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 71
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1141. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 71
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1142. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 71
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1143. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 71
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1144. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 70
   Model Context Protocol implementation for retrieving codebases using RepoMix

1145. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 70
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1146. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 70
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1147. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 69
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1148. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 69
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1149. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 68
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1150. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 68
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1151. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1152. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1153. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 67
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1154. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1155. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 67
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1156. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 66
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1157. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 66
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1158. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 66
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1159. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 65
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1160. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 65
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1161. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 65
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1162. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 65
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1163. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 65
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1164. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 64
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1165. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1166. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 64
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1167. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1168. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 63
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1169. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 63
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1170. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 63
   A Model Context Protocol server for Hopper Disassembler

1171. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 63
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1172. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 63
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1173. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 63
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1174. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 63
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1175. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 63
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1176. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 63
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1177. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 62
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1178. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1179. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 62
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1180. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 62
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1181. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 62
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1182. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1183. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 61
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1184. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1185. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 61
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1186. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1187. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 61
   Model Context Protocol(MCP) 中文教程讲解

1188. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 61
   A Model Context Protocol implementation for FHIR

1189. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 61
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1190. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1191. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 60
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1192. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 60
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1193. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 59
   Miro integration for Model Context Protocol

1194. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1195. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server for Rember.

1196. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 59
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1197. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 59
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1198. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 58
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1199. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

1200. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 58
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1201. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

1202. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 58
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1203. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 58
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1204. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 57
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1205. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 57
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

1206. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 57
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

1207. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 57
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1208. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

1209. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

1210. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1211. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 56
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1212. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

1213. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 55
   MKP is a Model Context Protocol (MCP) server for Kubernetes

1214. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 55
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1215. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 55
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1216. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 55
   Model Context Protocol for Actual Budget API

1217. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 55
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

1218. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 55
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1219. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

1220. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

1221. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 54
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1222. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1223. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 54
   Model Context Protocol for x64dbg & x32dbg

1224. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 54
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1225. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 53
   Model Context Protocol Servers for Azure AI Search

1226. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 53
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

1227. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 53
   A Model Context Protocol server for Ashra

1228. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

1229. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 52
   Index of all Model Context Protocol (MCP) clients and their capabilities

1230. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 52
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1231. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server for Microsoft Clarity

1232. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 52
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

1233. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 51
   OCaml implementation of the Model Context Protocol (MCP)

1234. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 51
   A Nasdaq Data Link MCP (Model Context Protocol) Server

1235. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 51
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1236. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 51
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

1237. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 51
   Model Context Protocol for YNAB (you need a budget)

1238. **[client](https://github.com/php-mcp/client)** - ⭐ 50
   Core PHP implementation for the Model Context Protocol (MCP) Client

1239. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 50
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

1240. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 50
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

1241. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

1242. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

1243. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 50
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

1244. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 50
   MCP (Model Context Protocol) server plugin for CAP NodeJS

1245. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 50
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

1246. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1247. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

1248. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 49
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

1249. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 49
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

1250. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 49
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

1251. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 48
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

1252. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 48
   Anthropic’s Model Context Protocol implementation for Oat++

1253. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

1254. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

1255. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 48
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

1256. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 48
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

1257. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 48
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

1258. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 48
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

1259. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 48
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

1260. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 48
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

1261. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 48
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

1262. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the AnySite API, enabling not only data retrieval but also robust management of user accounts.

1263. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 48
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

1264. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 48
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

1265. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 48
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1266. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

1267. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 47
   An implementation of the Model Context Protocol in Ruby.

1268. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 47
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

1269. **[mcp](https://github.com/goplus/mcp)** - ⭐ 47
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

1270. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

1271. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 47
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

1272. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 47
   ABAP MCP - Model Context Protocol - Server SDK

1273. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 47
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

1274. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 47
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

1275. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 46
   Inkdrop Model Context Protocol Server

1276. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 46
   OpenAPI Schema Model Context Protocol Server

1277. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 46
   A Model Context Protocol server that validates and renders Mermaid diagrams.

1278. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 46
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

1279. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

1280. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 46
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

1281. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

1282. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

1283. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 45
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

1284. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

1285. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

1286. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 45
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

1287. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

1288. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1289. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 45
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

1290. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 45
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

1291. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 45
   vMCP - Virtual Model Context Protocol

1292. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 44
   Model Context Protocol to fetch youtube transcript

1293. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 44
   Model Context Protocol server for Flight Tracking

1294. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 44
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

1295. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 44
   A Model-Context-Protocol (MCP) Server for Active Directory

1296. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 44
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

1297. **[go-mcp](https://github.com/MegaGrindStone/go-mcp)** - ⭐ 44
   A Go implementation of the Model Context Protocol (MCP) - an open protocol that enables seamless integration between LLM applications and external data sources and tools.

1298. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

1299. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 44
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

1300. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 44
   📚 An intelligent toolkit to automatically parse, complete, and format academic references, with Model Context Protocol (MCP) support.

1301. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 44
   Model Context Protocol Platform，统一管理你的MCP服务

1302. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 44
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

1303. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 43
   An opinionated starter template for making Model Context Protocol (MCP) servers

1304. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

1305. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 43
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

1306. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

1307. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

1308. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 43
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1309. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

1310. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

1311. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 43
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1312. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 43
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1313. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 42
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

1314. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

1315. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 42
   Model Context Protocol server for Salesforce REST API integration

1316. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 42
   GraphQL Schema Model Context Protocol Server

1317. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

1318. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

1319. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 42
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

1320. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 42
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

1321. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 42
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

1322. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 42
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

1323. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 42
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

1324. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 42
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

1325. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 42
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

1326. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

1327. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 42
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

1328. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 42
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1329. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 41
   A Model Context Protocol server implementation for Kagi's API

1330. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 41
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

1331. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 41
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

1332. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 41
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

1333. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 41
   A production-ready Model Context Protocol (MCP) server for semantic memory management

1334. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

1335. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 41
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

1336. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 41
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

1337. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

1338. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 41
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

1339. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 41
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

1340. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 41
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

1341. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

1342. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 41
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

1343. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 41
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

1344. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 41
   Amadeus MCP(Model Context Protocol) Server

1345. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 40
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

1346. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 40
   A Model Context Protocol server for Dify

1347. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 40
   An implementation of the Model Context Protocol for the World Bank open data API

1348. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 40
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

1349. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

1350. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

1351. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

1352. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 40
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

1353. **[mcp](https://github.com/40ants/mcp)** - ⭐ 40
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

1354. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 40
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

1355. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

1356. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 40
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

1357. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

1358. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 40
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

1359. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 40
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1360. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

1361. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 40
   MCP (Model Context Protocol) server for the Contentful Management API

1362. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 40
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

1363. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

1364. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 39
   A Model Context Protocol server for Zendesk

1365. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

1366. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 39
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

1367. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

1368. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 39
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

1369. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 39
   Model Context Protocol server for OpenStreetMap data

1370. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 39
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

1371. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 39
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

1372. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 39
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

1373. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 39
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

1374. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 38
   Algorand Model Context Protocol (Server & Client)

1375. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 38
   Implementation of Model Context Protocol server for Mailgun APIs

1376. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 38
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

1377. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 38
   It shows how to use model-context-protocol. 

1378. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

1379. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 38
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

1380. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 38
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

1381. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 38
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

1382. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 38
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

1383. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

1384. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

1385. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 38
   Build tools for LLMs in Rust using Model Context Protocol

1386. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 38
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

1387. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 38
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

1388. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 38
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

1389. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 38
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

1390. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 38
   A Model Context Protocol server for Go developers

1391. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 38
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

1392. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 37
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

1393. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

1394. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

1395. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 37
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

1396. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 37
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

1397. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 37
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

1398. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1399. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 37
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

1400. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

1401. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 37
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

1402. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

1403. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 36
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

1404. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

1405. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 36
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

1406. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 36
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

1407. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 36
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

1408. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

1409. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 36
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

1410. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

1411. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 36
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

1412. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 36
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

1413. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 36
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

1414. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 36
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1415. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

1416. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 35
   Bluesky MCP (Model Context Protocol) Server

1417. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 35
   Model Context Protocol Minecraft Server

1418. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 35
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

1419. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 35
   Model Context Protocol (MCP) implementation for iOS simulators

1420. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

1421. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 35
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

1422. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 35
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

1423. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 35
   Model Context Protocol server to let LLMs write and execute matlab scripts 

1424. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 35
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

1425. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

1426. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 35
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

1427. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 35
   Model Context Protocol Clojure support including REPL integration with development tools.

1428. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 35
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

1429. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 35
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

1430. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 35
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

1431. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 35
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

1432. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 35
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

1433. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 35
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1434. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 35
   Model Context Protocol server for Sitecore

1435. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 35
   Attio Model Context Protocol (MCP) server implementation

1436. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 34
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

1437. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 34
   Model Context Protocol server written in Scala

1438. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 34
   A Model Context Protocol server that provides access to Shodan API functionality

1439. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

1440. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

1441. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 34
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

1442. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 34
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

1443. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

1444. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 34
   A Model Context Protocol for checking domain name registration status in bulk.

1445. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 34
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

1446. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 34
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

1447. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

1448. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 34
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

1449. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

1450. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 34
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

1451. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine via Remote Control API. Built with TypeScript and designed for game development automation.

1452. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 34
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

1453. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 33
   Model Context Protocol server for ActivityWatch time tracking data

1454. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 33
   Model Context Protocol Server for Apache OpenDAL™

1455. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 33
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

1456. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 33
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

1457. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 33
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

1458. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

1459. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 33
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

1460. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 33
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

1461. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

1462. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

1463. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 33
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

1464. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

1465. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 33
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

1466. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 33
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

1467. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 33
   Privacy-first local RAG server for Cursor, Claude Code, and Codex — powered by the Model Context Protocol.

1468. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

1469. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 33
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

1470. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 33
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1471. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

1472. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 32
   Model Context Protocol (MCP) server implementation for Autodesk Maya

1473. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 32
   IMAP Model Context Protocol server for interactive email processing

1474. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 32
   Model Context Protocol (MCP) Server for Mistral OCR API

1475. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 32
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

1476. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

1477. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 32
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

1478. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

1479. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

1480. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 32
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

1481. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 32
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

1482. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 32
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

1483. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 32
   A powerful Model Context Protocol server for LinkedIn API integration

1484. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

1485. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 31
   Altium Model Context Protocol server and Altium API script

1486. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 31
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

1487. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 31
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

1488. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 31
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

1489. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 31
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

1490. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

1491. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 31
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

1492. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

1493. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

1494. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 31
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

1495. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 31
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

1496. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 31
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

1497. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

1498. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 31
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

1499. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 31
   Model Context Protocol (MCP) server for LinkedIn API integration

1500. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 31
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

1501. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

1502. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

1503. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 31
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1504. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Nostr capabilities to LLMs like Claude.

1505. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

1506. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

1507. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 30
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

1508. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 30
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

1509. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 30
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

1510. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 30
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features intelligent caching, response optimization, and comprehensive data access tools. Featured on Claude.

1511. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 30
   About A Model Context Protocol server that executes commands in the current WezTerm session

1512. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 30
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

1513. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

1514. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 30
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

1515. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 29
   Claude Unified Model Context Interaction Protocol

1516. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

1517. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 29
   Model Context Protocol (MCP) server for openBIM

1518. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

1519. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 29
   Model Context Protocol server for Cyclops

1520. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

1521. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 29
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

1522. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 29
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

1523. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 29
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

1524. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 29
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

1525. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

1526. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 29
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

1527. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

1528. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 29
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

1529. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 29
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

1530. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 29
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

1531. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 29
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

1532. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

1533. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 29
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

1534. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 29
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

1535. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 29
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

1536. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 28
   Model Context Server Protocol for your HANA DB

1537. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 28
   Emacs Lisp implementation of the Model Context Protocol

1538. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

1539. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

1540. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

1541. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

1542. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

1543. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 28
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

1544. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

1545. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 28
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

1546. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 28
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

1547. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 28
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

1548. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 28
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

1549. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

1550. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 28
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) technology with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

1551. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

1552. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 28
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

1553. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 28
   Model Context Protocol server for Directus

1554. **[mcp](https://github.com/fastly/mcp)** - ⭐ 28
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

1555. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

1556. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

1557. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 27
   Model Context Protocol Server of Rod

1558. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 27
   Asterisk Model Context Protocol (MCP) server.

1559. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 27
   MCP (Model Context Protocol) server for biothings

1560. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 27
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

1561. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 27
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

1562. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 27
   Model Context Protocol (MCP) server that interacts with a Debugger

1563. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

1564. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

1565. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 27
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

1566. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

1567. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 27
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

1568. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

1569. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 27
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

1570. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 27
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

1571. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

1572. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 27
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

1573. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

1574. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 27
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

1575. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 27
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

1576. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 27
   This Model Context Protocol (MCP) server provides a bridge between Claude and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

1577. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

1578. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 26
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

1579. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

1580. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 26
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

1581. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 26
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

1582. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 26
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

1583. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

1584. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 26
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

1585. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 26
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

1586. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 26
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

1587. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

1588. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 26
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

1589. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 26
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

1590. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

1591. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 26
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

1592. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 26
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

1593. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 26
   An implementation of Giphy integration with Model Context Protocol

1594. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 26
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

1595. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

1596. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

1597. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 25
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

1598. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

1599. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

1600. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 25
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

1601. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 25
   Model Context Protocol to bridge in Substack writings to Claude.

1602. **[mcp-advisor](https://github.com/olaservo/mcp-advisor)** - ⭐ 25
   MCP Server to assist LLMs and humans on Model Context Protocol spec compliance and understanding

1603. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

1604. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 25
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

1605. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

1606. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

1607. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 25
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

1608. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

1609. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 25
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

1610. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 25
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

1611. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

1612. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

1613. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

1614. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

1615. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 25
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

1616. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

1617. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 24
   A Model Context Protocol Server for Interacting with Slack

1618. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 24
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

1619. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 24
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

1620. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

1621. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 24
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

1622. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 24
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

1623. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

1624. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

1625. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 24
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

1626. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 24
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

1627. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

1628. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 24
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

1629. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

1630. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

1631. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

1632. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

1633. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 24
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

1634. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 24
   Model Context Protocol Server for NebulaGraph 3.x

1635. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

1636. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for GreptimeDB

1637. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 23
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

1638. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 23
   MCP (Model Context Protocol) Server for postgres Database

1639. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 23
   A simple Model Context Protocol (MCP) server for Clay.

1640. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

1641. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 23
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

1642. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 23
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

1643. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 23
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

1644. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 23
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

1645. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 23
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

1646. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 23
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

1647. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 23
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

1648. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 23
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

1649. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 23
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

1650. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 23
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

1651. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

1652. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 23
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

1653. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 23
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

1654. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

1655. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 23
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

1656. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 23
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

1657. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 23
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

1658. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 23
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

1659. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 23
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

1660. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 23
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

1661. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

1662. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 23
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

1663. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 22
   Model Context Protocol Server for Accessing twitter

1664. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

1665. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 22
   A MCP(Model Context Protocol) server that accesses to Lightdash

1666. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 22
   A personal assistant AI agent built with the Model Context Protocol (MCP)

1667. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 22
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

1668. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

1669. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

1670. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 22
   Model Context Protocol SDK implemented in Lua for OpenResty

1671. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 22
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

1672. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

1673. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

1674. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 22
   Sync MCP (Model Context Protocol) configurations across AI tools

1675. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

1676. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

1677. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 22
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

1678. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 22
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

1679. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

1680. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 22
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

1681. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 22
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

1682. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

1683. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 22
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

1684. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 22
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

1685. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

1686. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 22
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

1687. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 22
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

1688. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 22
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1689. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

1690. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 22
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

1691. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 22
   Python-based MCP server for BlazeMeter API — orchestrate performance-test lifecycle (create, configure, run, analyze) and manage tests, workspaces, projects & accounts via Model Context Protocol

1692. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

1693. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

1694. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

1695. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 21
   PowerPlatform Model Context Protocol server

1696. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 21
   model context protocol for Autodesk Revit

1697. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

1698. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 21
   Model Context Protocol server for Github Repo // Reading Github Repo

1699. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

1700. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 21
   A Fastify plugin to run Model Context Protocol (MCP) servers

1701. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 21
   MCP (model context protocol) server for interacting with dbt Docs

1702. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 21
   A Model Context Protocol server for 3D Slicer integration

1703. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 21
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

1704. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

1705. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 21
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

1706. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

1707. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 21
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

1708. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

1709. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 21
   Zillow MCP Server for real estate data access via the Model Context Protocol

1710. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 21
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

1711. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

1712. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 21
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

1713. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 21
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

1714. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 21
   Model Context Protocol server for querying Cursor chat history

1715. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

1716. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 21
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

1717. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

1718. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 21
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

1719. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 21
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

1720. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 21
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

1721. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 40,048
   基于大模型搭建的聊天机器人，同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入，可选择ChatGPT/Claude/DeepSeek/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Kimi/LinkAI，能处理文本、语音和图片，访问操作系统和互联网，支持基于自有知识库进行定制企业智能客服。

2. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 14,365
   AgentScope: Agent-Oriented Programming for Building LLM Applications

3. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 9,925
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 7,368
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,519
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

6. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,302
   extendable code review and QA agent 🚢

7. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,627

8. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,564
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

9. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 851
   ChatGPT CLI is a versatile tool for interacting with LLMs through OpenAI, Azure, and other popular providers like Perplexity AI and Llama. It supports prompt files, history tracking, and live data injection via MCP (Model Context Protocol), making it ideal for both casual users and developers seeking a powerful, customizable GPT experience.

10. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 758
   OpenTelemetry Instrumentation for AI Observability

11. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 735
   A code repository indexing tool to supercharge your LLM experience.

12. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 705
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

13. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 577
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

14. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 528
   The easiest way to discover and install MCPs

15. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 504
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

16. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 490
   VoiceMode MCP brings natural conversations to Claude Code

17. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 383
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

18. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 317
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

19. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 94
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

20. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

21. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 162,118
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,357
   🦍 The Cloud-Native Gateway for APIs & AI

3. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 26,537
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

4. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,192
   Your ultimate Go microservices framework for the cloud-native era.

5. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,025
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

6. **[plate](https://github.com/udecode/plate)** - ⭐ 15,594
   Rich-text editor with AI, MCP, and shadcn/ui

7. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

8. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 14,087
   ✨ Agentic IM ChatBot Infrastructure — 聊天智能体基础设施 ✨ 多消息平台集成（QQ / Telegram / 企微 / 飞书 / 钉钉等），强大易用的插件系统，支持 OpenAI / Gemini / Anthropic / Dify / Coze / 阿里云百炼 / 知识库 / Agent 智能体

9. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,165
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

10. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,388
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

11. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,155
   A cross-platform Markdown AI note-taking software.

12. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 9,921
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

13. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,199
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

14. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,722
   Agent Framework For Fintech and Banks

15. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 7,503
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

16. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,457
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

17. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,213
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

18. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 5,356
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

19. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,146
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,615
   Adversary simulation and Red teaming platform with AI

21. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,385
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,113
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,076
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 3,920
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/pAbnFJrkgZ

25. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,517
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

26. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,674
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

27. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 2,386
   Intelligent Router for Mixture-of-Models

28. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,363
   A highly opinionated, zero-configuration linter and formatter.

29. **[harbor](https://github.com/av/harbor)** - ⭐ 2,182
   Effortlessly run LLM backends, APIs, frontends, and services with one command.

30. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,843
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

31. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,686
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

32. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,648
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

33. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,435
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

34. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,382
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

35. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,253
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

36. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,251
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

37. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,219
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

38. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,048
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

39. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,045
   A single interface to use and evaluate different agent frameworks 

40. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 980
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

41. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 965
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

42. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 948
   Arduino MCP2515 CAN interface library

43. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 933
   Korea Investment & Securities Open API Github

44. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 910
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

45. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 891
   AIPex: AI browser automation assistant, no migration and privacy first. ChatGPT Atlas Alternative, Alternative to Manus Browser Operator.

46. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 759
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

47. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 718
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

48. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 682
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

49. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 673
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

50. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 672
   Solidity Static Analyzer that easily integrates into your editor

51. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 604
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

52. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 569
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

53. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 431
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

54. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

55. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 380
   Minecraft: Pi Edition API Python Library

56. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 379
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

57. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 374
   Arduino Library for Adafruit MCP23017

58. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 369
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

59. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 364
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

60. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 356
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"搜索+借鉴+AI+创意"四重能力，多种超绝玩法，内容创作充满无限可能。

61. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 343
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

62. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 341
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

63. **[exograph](https://github.com/exograph/exograph)** - ⭐ 337
   Build production-ready backends in minutes

64. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 335
   Python toolkit for building graph-enhanced GenAI applications

65. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 329
   Blender python addon to increase workflow for creating minecraft renders and animations

66. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 322
   MCP for Unreal Engine 5

67. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 321
   A personal AI assistant for everyone

68. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

69. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 313
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

70. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 307
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

71. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 291
   Software architecture tooling for the AI age

72. **[depyler](https://github.com/paiml/depyler)** - ⭐ 286
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

73. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 264
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

74. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

75. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 246
   An in-depth book and reference on building agentic systems like Claude Code

76. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 241
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

77. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 238
   AI for Ethical Hacking - Workshop

78. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 237
   Public facing repo for MCP SRG mappings.

79. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 230
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

80. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 230
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

81. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 221
   An introduction to the world of AI Agents

82. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 219
   A website to generate Minecraft profile pictures

83. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 219
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

84. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

85. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 210
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

86. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 206
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

87. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 199
   Re-usable multi part components built on React Aria and TailwindCSS. 

88. **[amical](https://github.com/amicalhq/amical)** - ⭐ 190
   🎙️ Open Source and Local-first AI Dictation App ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

89. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 189
   Fully working & decompiled MCP for Minecraft 1.8.9 

90. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 188

91. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 185
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

92. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 185
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

93. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 181
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

94. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 64
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

95. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 47
   Houdini integration through the Model Context Protocol

96. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

97. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

### Examples

*Example projects demonstrating MCP usage*

1. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,605
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 6,574
   Specification and documentation for the Model Context Protocol

2. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,824
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，支持 MCP 调用，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

3. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 872
   程序员鱼皮的 AI 资源导航，汇总热门的 AI 大模型和工具，比如 Deepseek 使用指南、提示词技巧、知识干货、应用场景、AI 变现、行业资讯、教程资源等一系列内容，帮助你快速掌握 AI 技术，走在时代前沿。涉及大模型 ChatGPT、Claude、Gemini、Deepseek、QWEN、GROK 等；涉及技术 Spring AI、LangChain、RAG、MCP、A2A 等；涉及 Cursor、TRAE 等工具。本项目为开源文档版本，已升级为鱼皮AI导航网站

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 354
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

5. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 198
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

6. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 24
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

