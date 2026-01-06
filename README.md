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

## 📚 Projects (2423 total)

> Last updated: **2026-01-06**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 124,832
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 119,768
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 89,781
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 78,178
   A collection of MCP servers.

5. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,241
   The fastest path to AI-powered full stack observability, even for lean teams.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 75,570
   Model Context Protocol Servers

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 70,945
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 69,818
   🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers, Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.

9. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 52,949
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

10. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 44,928
   🔥AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

11. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 42,367
   🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测。支持 Docker 一键部署，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。⭐

12. **[context7](https://github.com/upstash/context7)** - ⭐ 40,946
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

13. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,193
   Query Engine for AI - The only MCP Server you'll ever need

14. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,300
   🍒 Cherry Studio is a desktop client that supports for multiple LLM providers.

15. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 32,865
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

16. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 32,721
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

17. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,483
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

18. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 31,058
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

19. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,288
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

20. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 25,651
   GitHub's official MCP Server

21. **[goose](https://github.com/block/goose)** - ⭐ 25,495
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

22. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 25,112
   Playwright MCP server

23. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 24,737
   An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations.

24. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 24,720
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

25. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 22,921
   An MCP-based chatbot | 一个基于MCP的聊天机器人

26. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 21,715
   🚀 The fast, Pythonic way to build MCP servers and clients

27. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 20,992
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

28. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 20,966
   The official Python SDK for Model Context Protocol servers and clients

29. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 20,406
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

30. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,225
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

31. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 19,724
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

32. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 19,139
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

33. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 18,707
   Chrome DevTools for coding agents

34. **[serena](https://github.com/oraios/serena)** - ⭐ 18,124
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

35. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,085
   Your API ⇒ Paid MCP. Instantly.

36. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 14,812

37. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 13,962
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

38. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,360
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

39. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,214
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

40. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 12,852
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

41. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 12,405
   MCP server to provide Figma layout information to AI coding agents like Cursor

42. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 12,208
   MCP Toolbox for Databases is an open source MCP server for databases.

43. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 11,371
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

44. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,342
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

45. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,207
   The official TypeScript SDK for Model Context Protocol servers and clients

46. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 11,147
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

47. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 10,747
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

48. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,328
   Yet another WebUI for Nginx

49. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,204
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

50. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

51. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 9,782
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

52. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 9,649
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书无水印作品文件

53. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 9,378
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex & Gemini CLI.

54. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 8,821
   mcp-use is the easiest way to interact with mcp servers with custom agents

55. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,405
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

56. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 8,189
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

57. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,172
   Visual testing tool for MCP servers

58. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,153
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

59. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 7,923
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

60. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 7,907
   Build effective agents using Model Context Protocol and simple workflow patterns

61. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 7,847
   MCP for xiaohongshu.com

62. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 7,797
   AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.

63. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,324
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

64. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

65. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,196
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

66. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 6,997
   MCP Server for Ghidra

67. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 6,960
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

68. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,212
   A community driven registry service for Model Context Protocol (MCP) servers.

69. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,154
   A collection of MCP clients.

70. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 6,127
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

71. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 5,854
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

72. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 5,627
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

73. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,583
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

74. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,580
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

75. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 5,492
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

76. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,351
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

77. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,200
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

78. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,186
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

79. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,184
   WhatsApp MCP server

80. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,112
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

81. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,044
   Awesome MCP Servers - A curated list of Model Context Protocol servers

82. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,011
   Install, run and deploy your own decentralized AI agent service

83. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 4,938
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

84. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 4,903
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

85. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 4,893
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

86. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 4,802
   A model-driven approach to building AI agents in just a few lines of code.

87. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 4,786
   A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

88. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,695
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

89. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 4,683
   Open Source TypeScript AI Agent Framework with built-in LLM Observability

90. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 4,593
   An MCP server that allows MCP clients like Claude Desktop or Cursor to perform actions in the Unity Editor

91. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,520
   Easily build AI systems with Evals, RAG, Agents, fine-tuning, synthetic data, and more.

92. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,368
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

93. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,304
   opensource self-hosted sandboxes for ai agents

94. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,301
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

95. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,237
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

96. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,078
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

97. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 3,964
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

98. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 3,892
   MCP server for Atlassian tools (Confluence, Jira)

99. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,864
   The Cursor & Windsurf community, find rules and MCPs

100. **[Olares](https://github.com/beclab/Olares)** - ⭐ 3,863
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

101. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,838
   A simple, secure MCP-to-OpenAPI proxy server

102. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 3,808
   MCP Server for Computer Use in Windows

103. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,802
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

104. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,750
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

105. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,663
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

106. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,656
   Official Notion MCP Server

107. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,625
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

108. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,616
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

109. **[core](https://github.com/opensumi/core)** - ⭐ 3,585
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

110. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,576
   Define, Prompt and Test MCP enabled Agents and Workflows

111. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,560
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

112. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,555
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

113. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,507
   Exa MCP for web search and web crawling!

114. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,497
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

115. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,462
   🤖 A visualization mcp contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

116. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,453
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

117. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,399
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

118. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 3,394
   A Model Context Protocol (MCP) server that provides Xcode-related tools for integration with AI assistants and other MCP clients.

119. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,368
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

120. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,331
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP. Built with Golang for efficient memory use. 

121. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 3,293
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, PHP, Elixir, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

122. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,290
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

123. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,254

124. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,244
   LangChain 🔌 MCP

125. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,241
   Model Context Protocol(MCP) 编程极速入门

126. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,227
   A curated list of Model Context Protocol (MCP) servers

127. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,201
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

128. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,075
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

129. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,072
   A Model Context Protocol server for Excel file manipulation

130. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,063
   Learn AI and LLMs from scratch using free resources

131. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,058
   An Autonomous Agentic Framework for Reflective PowerPoint Generation

132. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,054
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

133. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,030
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

134. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,029
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

135. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,009
   Allow LLMs to control a browser with Browserbase and Stagehand

136. **[boost](https://github.com/laravel/boost)** - ⭐ 3,007
   Laravel-focused MCP server for augmenting your AI powered local development experience.

137. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 2,953
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

138. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,948
   n8n custom node for MCP

139. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 2,947
   The missing macOS LLM server. Run local or cloud models with OpenAI & Anthropic compatible APIs. MCP server for Cursor & Claude Desktop, menu bar chat, plugins, and dev tools. Native Apple Silicon.

140. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,943
   AI agent microservice

141. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 2,900
   Full guide on claude tips and tricks and how you can optimise your claude code the best & strive to find every command possible even hidden ones!

142. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,861
   A TypeScript framework for building MCP servers.

143. **[mcp](https://github.com/google/mcp)** - ⭐ 2,855
   Google 💚 MCP

144. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 2,814
   RikkaHub is an Android APP that supports for multiple LLM providers.

145. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,790
   The official Rust SDK for the Model Context Protocol

146. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,733
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

147. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,645
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

148. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,581
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

149. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

150. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,525
   A CLI tool for building Go applications.

151. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 2,406
   UltraRAG v2: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

152. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,388
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

153. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,367
   Connect Supabase to your AI assistants

154. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,351
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

155. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,333
   A Model Context Protocol server for converting almost anything to Markdown

156. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,313
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

157. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,186
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

158. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,154
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

159. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,133
   A bridge between Streamable HTTP and stdio MCP transports

160. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,127
   Claude Skills, Agents, Commands, Hooks, Plugins, Marketplaces Collection for Claude Code

161. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,120

162. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

163. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,077
   MCP server for Grafana

164. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,060
   DDGS | Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services

165. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,055
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

166. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,025
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi, GLM, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

167. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,005
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

168. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,003
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

169. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,002
   A Model Context Protocol server for searching and analyzing arXiv papers

170. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 1,984
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

171. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,966
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

172. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 1,961
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

173. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,954
   directory for Awesome MCP Servers

174. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 1,952
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

175. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,946
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

176. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 1,901
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

177. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,877
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

178. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 1,863
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

179. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,860
   The official MCP server implementation for the Perplexity API Platform

180. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 1,844
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

181. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 1,844
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

182. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,814
   Witsy: desktop AI assistant / universal MCP client

183. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,805
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

184. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,801
   A secure low code honeypot framework, leveraging AI for System Virtualization.

185. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,793

186. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,789
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

187. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,768
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

188. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,765
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

189. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,750
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

190. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,689
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

191. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,683
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

192. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,666
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

193. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,663
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

194. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,652
   Interactive User Feedback MCP

195. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,628
   Desktop Extensions: One-click local MCP server installation in desktop apps

196. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,613
   Make RSS 📰 great again with AI 🧠✨!!

197. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,592
   Coding assistant MCP for Claude Desktop

198. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,577
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

199. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 1,544
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

200. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,540
   Build ChatGPT Apps and MCP servers locally.

201. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,535
   MCP server that provides tools and resources for interacting with n8n API

202. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,531
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

203. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,524
   Next Generation Agentic Proxy for AI Agents and MCP servers

204. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,512
   🧩 The ultimate toolkit for working with APIs.

205. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,509
   ⭐All-in-one AI Companion!  AI Desktop Companion + AI Virtual Streamer + AI Social App Bot + AI Interactive UI Interface + Digital Human Broadcasting + AI Games  and all the features you can imagine! ⭐全能型AI伴侣！AI桌面女友 + AI虚拟主播 + AI社交APP机器人 + AI交互式UI界面 + 数字人播报 + AI游戏 等你能想到的一切功能！

206. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,506
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

207. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,496
   A Unified MCP Server Management App (MCP Manager).

208. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,494
   ToolHive makes deploying MCP servers easy, secure and fun

209. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,491
   An MCP server that installs other MCP servers for you

210. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,488
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

211. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,435
   Standards for building agents, better

212. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,430
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

213. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,425
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

214. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,395
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

215. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,392
   MCP server for interacting with the iOS simulator

216. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 1,386
   The better playwright MCP: works as a browser extension. No context bloat. More capable.

217. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,380
   Constrain, log and scan your MCP connections for security vulnerabilities.

218. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,375
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

219. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,364
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

220. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,339
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

221. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,328
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

222. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,328
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

223. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,322
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

224. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,313
   The Simple Agent Development Kit.

225. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,294
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

226. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,272
   MAI-UI: Real-World Centric Foundation GUI Agents.

227. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,268
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

228. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,263
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

229. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,258
   A connector for Claude Desktop to read and search an Obsidian vault.

230. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,256
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

231. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,255
   Make your own story. User-friendly software for LLM roleplaying

232. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,254
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

233. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,247
   MCP Server for kubernetes management commands

234. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,245
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

235. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,244
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

236. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,237
   Damn Vulnerable MCP Server

237. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,235
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

238. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,231
   An MCP server that autonomously evaluates web applications. 

239. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

240. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

241. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,214
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

242. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,206
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

243. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,203
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

244. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

245. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,198
   The Grafbase GraphQL Federation Gateway

246. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,191

247. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,190
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for OpenAI, Gemini, Claude, Deepseek and Grok interoperability

248. **[ai](https://github.com/stripe/ai)** - ⭐ 1,183
   One-stop shop for building AI-powered products and businesses with Stripe.

249. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,173
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

250. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,166
   The TypeScript MCP framework

251. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,164
   The official Swift SDK for Model Context Protocol servers and clients.

252. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,156
   The AI toolkit for the AI developer

253. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,153
   An official Qdrant Model Context Protocol (MCP) server implementation

254. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,153
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

255. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,130
   The official ElevenLabs MCP server

256. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,124
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

257. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,122
   告别AI提前终止烦恼，助力AI更加持久

258. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,121
   docker mcp CLI plugin / MCP Gateway

259. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,120
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

260. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,116
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

261. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,113
   A Ruby Implementation of the Model Context Protocol

262. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,107
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

263. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 1,091
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

264. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,088
   Build, evaluate and train General Multi-Agent Assistance with ease

265. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,072
   Stop re-explaining your project to AI every session. Automatic context memory for Claude, VS Code, Cursor, and 13+ AI tools.

266. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,066
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

267. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,062
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server

268. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,061
   The most powerful MCP Slack Server with no permission requirements, Apps support, multiple transports Stdio and SSE, DMs, Group DMs and smart history fetch logic.

269. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,060
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

270. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,060
   A web UI for Claude Code agents

271. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,058
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

272. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,049
   Production ready MCP server with real-time search, extract, map & crawl.

273. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,044
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

274. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,043

275. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,035
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

276. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,033
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

277. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,027
   Query and Summarize your chat messages.

278. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

279. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,025
   On-premises conversational RAG with configurable containers

280. **[use-mcp](https://github.com/modelcontextprotocol/use-mcp)** - ⭐ 1,019

281. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,019
   MCP Python Tutorial 

282. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,017
   Plugin for JADX to integrate MCP server

283. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 1,011
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

284. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,005
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

285. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 997
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

286. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 988
   Claude Code as one-shot MCP server to have an agent in your agent.

287. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 984
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

288. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 972
   Remote MCP Servers

289. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 965
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

290. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 964
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

291. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 952
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

292. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 952
   Bringing the power of MCP to the web

293. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 952
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

294. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 947
   MCP server for fetch web page content using Playwright headless browser.

295. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 946
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

296. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 938
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

297. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 937
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

298. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 934
   A repository of servers and clients from the Model Context Protocol tutorials

299. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 926
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

300. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 919
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

301. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 913
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

302. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 910
   Connect AI models like Claude & GPT with robots using MCP and ROS.

303. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

304. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 898
   Expose llms-txt to IDEs for development

305. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 897
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

306. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 897
   The Context Graph Factory for AI. Build, manage, and deploy AI-optimized Context Graphs.

307. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 896
   Hundreds of Claude Code plugins with embedded AI skills. Learn via interactive Jupyter tutorials.

308. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 895
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

309. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 892
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

310. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 891
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

311. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 890
   A framework for writing MCP (Model Context Protocol) servers in Typescript

312. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 884
   A middleware to provide an openAI compatible endpoint that can call MCP tools

313. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 884
   MCP server helping models to understand your Vite/Nuxt app better.

314. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 883
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

315. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 883
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

316. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 880
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

317. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 880
   Model Context Protocol for WinDBG

318. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 880
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

319. **[tools](https://github.com/strands-agents/tools)** - ⭐ 875
   A set of tools that gives agents powerful capabilities.

320. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 872
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

321. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 868
   Allow AI to wade through complex OpenAPIs using Simple Language

322. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 867
   A library for communication with a Minecraft client/server.

323. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 865
   Neo4j Labs Model Context Protocol servers

324. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 864

325. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 864

326. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 863
   A security scanner for your LLM agentic workflows

327. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 863
   MCP integration for Google Calendar to manage events.

328. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 856
   First gitlab mcp for you

329. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 855
   ChatGPT CLI is a versatile tool for interacting with LLMs through OpenAI, Azure, and other popular providers like Perplexity AI and Llama. It supports prompt files, history tracking, and live data injection via MCP (Model Context Protocol), making it ideal for both casual users and developers seeking a powerful, customizable GPT experience.

330. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 855
   A concise list for mcp servers

331. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 851
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

332. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 845

333. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 842
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

334. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 840
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

335. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

336. **[agents](https://github.com/inkeep/agents)** - ⭐ 835
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

337. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 832
   APIM ❤️ AI - This repo contains experiments on Azure API Management's AI capabilities, integrating with Azure OpenAI, AI Foundry, and much more 🚀 . New workshop experience at https://aka.ms/ai-gateway/workshop

338. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 832
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

339. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 824
   A minimalistic MCP client with a good feature set.

340. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 819
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

341. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 817
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

342. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 812
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

343. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 810

344. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

345. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 809
   Simple, modular, and observable Go framework for backend applications.

346. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 807
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

347. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 800
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

348. **[context-space](https://github.com/context-space/context-space)** - ⭐ 798
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

349. **[server](https://github.com/php-mcp/server)** - ⭐ 798
   Core PHP implementation for the Model Context Protocol (MCP) server

350. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 794
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

351. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 794
   OpenAPI Tool Servers

352. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 792
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

353. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 791
   Browse the web, directly from Cursor etc.

354. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 785
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

355. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 785
   A curated list of Model Context Protocol (MCP) servers 

356. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 783
   The best way to create, deploy, and share MCP Servers

357. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 776
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

358. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 767
   Self-hosted MCP Gateway and Registry for AI agents

359. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 765
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

360. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 764
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

361. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 757
   一个将ACE(Augment Context Engine) 做成MCP的项目

362. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 757
   Vibetest MCP - automated QA testing using Browser-Use agents

363. **[Context](https://github.com/indragiek/Context)** - ⭐ 757
   Native macOS client for Model Context Protocol (MCP)

364. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 755
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

365. **[runno](https://github.com/taybenlor/runno)** - ⭐ 754
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

366. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 750
   Chat with your Kubernetes Cluster using AI tools and IDEs like Claude and Cursor!

367. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 750
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

368. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 749
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

369. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 745
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

370. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 738
   LLDB MCP Integration + other helpful commands

371. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 738
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

372. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 733
   Scan MCP servers for potential threats & security findings.

373. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 730
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

374. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 725
   An MCP server for interacting with the Financial Datasets stock market API.

375. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 715
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

376. **[wordpress-mcp](https://github.com/Automattic/wordpress-mcp)** - ⭐ 714
   WordPress MCP — This repository will be deprecated as stable releases of mcp-adapter become available. Please use https://github.com/WordPress/mcp-adapter for ongoing development and support.

377. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 712
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

378. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 710
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

379. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 709
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

380. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 704
   A secure local sandbox to run LLM-generated code using Apple containers

381. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 696
   All in one vscode plugin for mcp developer

382. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 693
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

383. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 690
   Build MCP Agents

384. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 690
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

385. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 689
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

386. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 683
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles and companies, get your recommended jobs, and perform job searches.

387. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 682
   A MCP server implementation for hyperbrowser

388. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 679
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

389. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 676
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

390. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 673
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

391. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 671
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

392. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 670
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

393. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 665
   MCP server for Docker

394. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 665
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

395. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 665
   A flexible HTTP fetching Model Context Protocol server.

396. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 662
   Clojure MCP

397. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 657
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

398. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 656
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

399. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 655
   A simple CLI to run LLM prompt and implement MCP client.

400. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

401. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 655
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

402. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 649
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

403. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 648
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

404. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

405. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 640
   Laravel API for Ai Agents and humans.

406. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 640
   EnrichMCP is a python framework for building data driven MCP servers

407. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 638
   Querying local documents, powered by LLM

408. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 638
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

409. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 634
   Connect ClickHouse to your AI assistants.

410. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 633
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

411. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 629
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

412. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 629
   Shell and coding agent on claude desktop app

413. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 626
   An MCP server that provides control over Android devices via adb

414. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 625
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

415. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 623
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

416. **[mcp](https://github.com/laravel/mcp)** - ⭐ 618
   Rapidly build MCP servers for your Laravel applications.

417. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 617
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

418. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 617
   Talk to a Cloudflare Worker from Claude Desktop!

419. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 613
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

420. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 612
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

421. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 612
   A simple MCP server for Obsidian

422. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 611
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

423. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 605
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

424. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 598
   mem-agent mcp server

425. **[samples](https://github.com/strands-agents/samples)** - ⭐ 596
   Agent samples built using the Strands Agents SDK.

426. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 594
   gcloud MCP server

427. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 592
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

428. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 590
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

429. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 590
   Convert Any OpenAPI V3 API to MCP Server

430. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 588
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

431. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 583

432. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 582
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

433. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 582
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

434. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 581
   MCP Server For Turkish Legal Databases

435. **[tome](https://github.com/runebookai/tome)** - ⭐ 580
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

436. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 580
   Daydreams is a set of tools for building agents for commerce

437. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 572
   The Intelligence Layer for AI agents. Connect your models, tools, and data to create agentic apps that can think, act and talk to you.

438. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 572
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

439. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 570
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

440. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 567

441. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 566
   LangGraph solution template for MCP

442. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 557
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

443. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 551
   MCP to connect your LLM with Spotify.

444. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 551

445. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 550
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

446. **[obot](https://github.com/obot-platform/obot)** - ⭐ 548
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

447. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 544
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

448. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 543

449. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 541
   Security scanner for MCP servers

450. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 535
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

451. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 534
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

452. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 533

453. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 532
   The .NET library to build AI agents with 25+ built-in connectors.

454. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 532
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

455. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 532
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

456. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 532
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

457. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 531
   MCP server for interacting with Neon Management API and databases

458. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 531

459. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 531
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

460. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 530

461. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 526
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

462. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 524
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

463. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 523
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

464. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 521
   Draw.io Model Context Protocol (MCP) Server

465. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 520
   An MCP Multimodal AI Agent with eyes and ears!

466. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 520

467. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 519
   An Mcp client inside Emacs

468. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 518
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

469. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 517
   An MCP server to query any Postgres database in natural language.

470. **[ethora](https://github.com/dappros/ethora)** - ⭐ 516
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

471. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 516
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

472. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

473. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 514
   提取抖音无水印视频链接，视频文案，douyin-mcp-server

474. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 510
   A comprehensive collection of Model Context Protocol (MCP) servers

475. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 509
   A MCP server for Home Assistant

476. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 509
   MCP server for querying Apple Health data with natural language and SQL

477. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 508
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

478. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

479. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 507
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STEAMABLEHTTP access protocols to deploy MCP。

480. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 507
   MCP server to deploy apps to Cloud Run

481. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 506
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

482. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 506
   Open Source Voice Agent Platform

483. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 506
   A Model Context Protocol server for IDA

484. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 506
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

485. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 505
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

486. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 503
   微信读书MCP

487. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 499

488. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 499
   A tool that converts OpenAPI specifications to MCP server

489. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 498
   Yes Mcp server in bash

490. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 498
   Next.js Development for Coding Agent

491. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 494
   An MCP server for interacting with Sentry via LLMs.

492. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

493. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 492
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

494. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 491
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

495. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 487
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

496. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 486

497. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 485
   MCP Monitoring with eBPF

498. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 484
   A Model-Context Protocol Server for YouTube

499. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 482
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

500. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 481
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

501. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 480
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

502. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 480

503. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 478
   MCP server for document format conversion using pandoc.

504. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 472
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

505. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 470
   Aser is a lightweight, self-assembling AI Agent frame.

506. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 469
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

507. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 468
   MCP Server to interact with Google Gsuite prodcuts

508. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 468
   MCP to allow AI agents to control Unreal

509. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 465
   An SDK building Laravel MCP servers

510. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 462
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

511. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 462
   Install, manage and develop MCP servers

512. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 462
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, and comprehensive lifecycle management capabilities.

513. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 461
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

514. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

515. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 457
   LLM + MCP + RAG = Magic

516. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 457
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

517. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 457
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

518. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 455
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

519. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 455
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

520. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 455
   "AnyTool: Universal Tool-Use Layer for AI Agents"

521. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 455
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

522. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 452
   MCP server integration for DaVinci Resolve

523. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 451
   A MCP (Model Context Protocol) server for interacting with dbt.

524. **[argo](https://github.com/xark-argo/argo)** - ⭐ 450
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

525. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 447
   Govern & Secure your AI

526. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 447
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

527. **[director](https://github.com/director-run/director)** - ⭐ 444
   MCP Playbooks for AI agents

528. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 442
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

529. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 440
   A docker MCP Server (modelcontextprotocol)

530. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 440

531. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 438
   FreeCAD MCP(Model Context Protocol) server

532. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 437
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

533. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 436
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

534. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 436
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

535. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 435
   MCP Server for Turkish & American Stock Exchange and Fund Data

536. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 434
   MCP configuration to connect AI agent to a Linux machine.

537. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 433
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

538. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 432
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

539. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 429
   GitOps on Autopilot Mode

540. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 425
   A simple, locally hosted Web Search MCP server for use with Local LLMs

541. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 423
   Send emails directly from Cursor with this email sending MCP server

542. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 418
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

543. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 418

544. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 418
   Make your meetings accessible to AI Agents

545. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 418
   Spec-Driven Development MCP Server, not just Vibe Coding

546. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 417
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

547. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 417
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

548. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 417
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

549. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 416
   小红书MCP服务 x-s x-t js逆向

550. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 416
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

551. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 415
   MCP Server for Burp

552. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 415
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

553. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 415
   Unlock 650+ MCP servers tools in your favorite agentic framework.

554. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 410
   基于NET搭建-AI智能体-现代化Saas企业级前后端分离架构-开启智能应用的无限可能：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR验证码识别、API多版本兼容、单元集成测试、RabbitMQ、代码生成器

555. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 409
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

556. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 409
   MCP Server for Metasploit

557. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 408
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

558. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 406
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

559. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 406
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

560. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 404
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

561. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 403
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

562. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 402
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

563. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 402
   Enterprise-ready MCP gateway, MCP registry & orchestrator

564. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 401
   A CLI inspector for the Model Context Protocol

565. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 401
   The safest way to make REST calls in C# with an MCP Generator

566. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 399
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

567. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 397
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

568. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 395
   MCP server that execute applescript giving you full control of your Mac

569. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 394
   An experiment in software planning using MCP

570. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 394
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

571. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 392
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

572. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 391
   An MCP extension for Ghidra

573. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 390
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

574. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 389
   Official Jina AI Remote MCP Server

575. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 388
   MCP server for DuckDB and MotherDuck

576. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 388
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

577. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 388
   Official Docker MCP registry 

578. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 384
   MCP-NixOS - Model Context Protocol Server for NixOS resources

579. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 384
   Memento MCP: A Knowledge Graph Memory System for LLMs

580. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 382
   BioMCP: Biomedical Model Context Protocol

581. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 382
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

582. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 382
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

583. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 381
   Local Groq Desktop chat app with MCP support

584. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 381
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

585. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 381
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

586. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 381
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

587. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 378
   Baidu Map MCP Server

588. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 378
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

589. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 378
   MCP Server for SearXNG

590. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 377
   lunar.dev: Agent native MCP Gateway for governance and security

591. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 376
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

592. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 375
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

593. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 374
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

594. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 371
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

595. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 370
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

596. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 370
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

597. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 369
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

598. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 369
   A model-driven approach to building AI agents in just a few lines of code. 

599. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 368
   Model Context Protocol (MCP) Server for Graphlit Platform

600. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 368
   MCP server connecting to Kubernetes

601. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 368
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

602. **[station](https://github.com/cloudshipai/station)** - ⭐ 367
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

603. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 366
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

604. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 365
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

605. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 364
   MCP Server for code graph analysis and visualization by CodeGPT

606. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 363
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

607. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 363
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Cognito integration.

608. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 362
   Up-to-date Documentation for AI Agents.

609. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 361
   Model Context Protocol SDK for PHP

610. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 360
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

611. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 359
   A fully functional MCP server and CLI for YouTube

612. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 358
   Making docling agentic through MCP

613. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 358
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

614. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 357
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

615. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 357
   MCP integration platforms making AI-Agents developers focusing on their own tasks

616. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 357
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

617. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 357
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

618. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 355
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

619. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 354
   Search Airbnb using your AI Agent

620. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 353
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

621. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 353
   MCP server that provides LLMs with tools for interacting with EVM networks

622. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 353
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs, OpenRouter, Groq, Dashscope & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

623. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 352
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

624. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 352
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

625. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 351
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

626. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 350
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

627. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 349
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的专有领域智能聊天助手

628. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 349
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

629. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 346
   MCP Server implementation for Ableton Live OSC control

630. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 346
   Model Context Protocol (MCP) implementation in Rust

631. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 345
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

632. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 344
   MCP server for Todoist integration enabling natural language task management with Claude

633. **[codexia](https://github.com/milisp/codexia)** - ⭐ 344
   A powerfull GUI/IDE and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

634. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 343
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

635. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 343
   AI-based stock analysis and trading system

636. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 343
   Model Context Protocol server for GraphQL

637. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 342
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

638. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 342
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

639. **[daan](https://github.com/pluveto/daan)** - ⭐ 341
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

640. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 341
   A macOS AppleScript MCP server

641. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 340
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

642. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 340
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

643. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 340
   MCP Server implementation for Xcode integration

644. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 339
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

645. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 338
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

646. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 338
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

647. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 338
   F2C MCP Server

648. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 338
   飞书/Lark官方 OpenAPI MCP

649. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

650. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 337
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

651. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 337
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

652. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 337
   Professional Development Environment for Claude Code with Spec-Driven Workflow, TDD, LSP, Cross-Session Memory, Semantic Search, Quality Hooks and Modular Rules System 🛠️

653. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 336
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

654. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 336
   SonarQube MCP Server

655. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 336
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

656. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 334
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

657. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 334
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

658. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 333
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

659. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 332
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

660. **[devopness](https://github.com/devopness/devopness)** - ⭐ 332
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

661. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 332
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

662. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 331
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

663. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 328
   Elixir Model Context Protocol (MCP) SDK

664. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 327
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

665. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 327
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

666. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 327
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

667. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 326

668. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 326
   Nuwax AI - Easily build and deploy your private Agentic AI solutions.  智能体智能应用一站式搭建平台，无需编程基础，构建你的MCP、工作流、智能体，还可一句话生成智能应用，从想法到实现只差1分钟.

669. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 325
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models. v0.2.8

670. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 325
   An MCP implementation for Selenium WebDriver

671. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 324
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

672. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 323
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

673. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 323

674. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 322
   Control your Android devices with AI using Model Context Protocol

675. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 322
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

676. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

677. **[moling](https://github.com/gojue/moling)** - ⭐ 321
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

678. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 321

679. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 319
   AI-Powered Revit Modeling

680. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 319
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

681. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 318
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

682. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 317
   This is a Minecraft Base Client

683. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 317
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

684. **[emcee](https://github.com/mattt/emcee)** - ⭐ 316
   MCP generator for OpenAPIs 🫳🎤💥

685. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 316
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

686. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 315
   An MCP server for Azure DevOps

687. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 315
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

688. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 315
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

689. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 314
   Xiaozhi MCP sample program

690. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 313
   Repo of skills for autogen studio using model context protocol (mcp)

691. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 313
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

692. **[mcp](https://github.com/IBM/mcp)** - ⭐ 312
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

693. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 309
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

694. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 309
   deep, reliable and confidential coding-context

695. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 307
   MCP server to expose VS Code editing features to an LLM for AI coding

696. **[gemini-flow](https://github.com/clduab11/gemini-flow)** - ⭐ 305
   rUv's Claude-Flow, translated to the new Gemini CLI; transforming it into an autonomous AI development team.

697. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 305
   A Production-Ready Runtime Framework for Agent Deployment and Tool Sandbox

698. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 303
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

699. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 303
   An MCP server for loading skills (shim for non-claude clients).

700. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 302
   A working pattern for SSE-based MCP clients and servers

701. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 302
   Turn any openapi file into an mcp server, with just the tools you need.

702. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

703. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 301
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

704. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 301
   api router for MCP Servers

705. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 301
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

706. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 300
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

707. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 300
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

708. **[mesh](https://github.com/decocms/mesh)** - ⭐ 299
   One secure endpoint for every MCP server. Deploy anywhere.

709. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 299
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

710. **[mcp-nodejs-debugger](https://github.com/workbackai/mcp-nodejs-debugger)** - ⭐ 298
   🐞 MCP Node.js debugger

711. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 298
   Mapbox Model Context Protocol (MCP) server

712. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 296
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

713. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 296
   A Model Context Protocol server for building an investor agent

714. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 296

715. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 296
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

716. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 295
   MCP implementation of Claude Code capabilities and more

717. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 294
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

718. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 294

719. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 293
   An implementation of Model Context Protocol (MCP) server for Argo CD.

720. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 293
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

721. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 292
   Agentic RAG for any scenario. Customize sources, depth, and width

722. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 291
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

723. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 290
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

724. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 288
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

725. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 288
   MaverickMCP - Personal Stock Analysis MCP Server

726. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 288
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

727. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 287
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

728. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 287

729. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 287
   Model Context Protocol server for DeepSeek's advanced language models

730. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 286
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

731. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 285
   MCP server for OpenAI o3 web search

732. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 285
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

733. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 284
   Minimal MCP Server for Aider

734. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

735. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 283
   hydra-ai

736. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 283
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

737. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 282
   Discover Exceptional MCP Servers

738. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 282

739. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 282

740. **[generator](https://github.com/context-hub/generator)** - ⭐ 282
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

741. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

742. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 281
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

743. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 280
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

744. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 280
   The specification for the Universal Tool Calling Protocol

745. **[consult7](https://github.com/szeider/consult7)** - ⭐ 279
   MCP server to consult a language model with large context size

746. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 279
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

747. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 279
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

748. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 279
   OpenSkills: Run Claude Skills Locally using any LLM

749. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 278
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

750. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 277
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

751. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 277
   simple web ui to manage mcp (model context protocol) servers in the claude app

752. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 277
   First AI‑enabled open-source Human Capital Management system that you can start using today.

753. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 276
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

754. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 276
   Model Context Protocol (MCP) Server for dify workflows

755. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 275
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

756. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 273
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

757. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 273
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

758. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 273
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

759. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 272
   MCP server for browser automation using Playwright

760. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 272
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

761. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 272
   A Model Context Protocol Server for MongoDB

762. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 272
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

763. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 272
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

764. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 271
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

765. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 271
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

766. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 271
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

767. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

768. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 270
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

769. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 270
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

770. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

771. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 268
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

772. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 268
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

773. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 265
   Source code of minecraft 1.12

774. **[mq](https://github.com/harehare/mq)** - ⭐ 265
   jq-like command-line tool for markdown processing

775. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 265
   im busy building ai agents so why not let an ai talk to my girlfriend? 

776. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 264
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

777. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 264
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

778. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 264
   Obsidian MCP (Model Context Protocol) Server

779. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 262
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

780. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 262
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

781. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 262

782. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 262
   An MCP server providing tools for image processing operations

783. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 262
   MCP server for Windows OS automation

784. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 262
   Lightweight MCP Server for interacting with Android Operating System.

785. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 260
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

786. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 258
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

787. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 258
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

788. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 258
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

789. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 258
   MCP server for JADX-AI Plugin

790. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 258
   MCP server retrieving transcripts of YouTube videos

791. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 256
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

792. **[mcp](https://github.com/oracle/mcp)** - ⭐ 256
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

793. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 254
   Home Assistant MCP Server

794. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

795. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 253
   MCP Server for Odoo

796. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 253
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

797. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 253
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

798. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 253
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

799. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 252
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

800. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 252
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

801. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 251
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

802. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 250
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

803. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 248
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

804. **[api200](https://github.com/API-200/api200)** - ⭐ 248
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

805. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 248
   Model Context Protocol server implementation for Reddit

806. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 247
   MCP server(s) for Aipolabs ACI.dev

807. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 247
   A code reasoning MCP server, a fork of sequential-thinking

808. **[app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server)** - ⭐ 247

809. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 246
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

810. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 245
   Apollo MCP Server

811. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 245
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

812. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 244
   MCP server implementation for Google's Gemini API

813. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 244
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

814. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 244
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

815. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 242
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

816. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 241
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

817. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

818. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 241
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

819. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 241
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

820. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 240
   Pixelize the real world on-chain

821. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 240
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

822. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 240
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

823. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 240
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

824. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 240
   Apache Doris MCP Server

825. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 239
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

826. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 239
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

827. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 239
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

828. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 238
   MCP Server for interacting with Salesforce instances

829. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 238
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

830. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 238
   MCP Interface for Video Jungle

831. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 237

832. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 236
   Easy guide to installing Claude Code MCPs globally on your machine.

833. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 236
   An MCP server for Massive.com Financial Market Data

834. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 236
   Simplified Gemini for Claude Code. 

835. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

836. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 234
   Turn any MCP server into a Python module

837. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 234
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

838. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 234
   🔥 Model Context Protocol (MCP) server for Firebase.

839. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 233
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

840. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 233

841. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 233
   小智AI客户端，目前主要用于MCP的对接

842. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 233
   Code Runner MCP Server

843. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 233
   The evaluation benchmark on MCP servers

844. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 232
   Creates a simple MCP tool server with "streaming" HTTP.

845. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 232
   MCP Server for Tree-sitter

846. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 231
   MCP server for Bazi (八字) information

847. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 231
   MCP server for searching and retrieving Claude Agent Skills using vector search

848. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 228
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

849. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 228
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

850. **[dat](https://github.com/hexinfo/dat)** - ⭐ 228
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

851. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

852. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 227
   An experimental MCP Server for foundry built for Solidity devs

853. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 226
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

854. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 226
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

855. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 226
   A Model Context Protocol (MCP) server that enables natural language queries to databases

856. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 226
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

857. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 226
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

858. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 225
   MCP Server for Telegram

859. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 225
   SpringAI，LLM，MCP，Embedding

860. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 225
   Standardized environment infrastructure for Agentic AI development.

861. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 224
   A collection of MCP servers

862. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 224
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

863. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 223
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

864. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 222
   Standalone Roblox Studio MCP Server

865. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 221
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

866. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 221
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

867. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 221
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

868. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 221
   Semantic code searcher and codebase utility with AI memory onboard

869. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 220

870. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 220
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

871. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 220
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

872. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 219

873. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

874. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 219
   Model Context Protocol server to run commands

875. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 219
   AWS MCP Proxy Server

876. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 219
   Context-Engine: MCP retrieval stack for AI coding assistants. Hybrid code search (dense + lexical + reranker), ReFRAG micro-chunking, local LLM prompt enhancement, and dual SSE/RMCP endpoints. One command deploys Qdrant-powered indexing for Cursor, Windsurf, Roo, Cline, Codex, and any MCP client.

877. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 218
   A TypeScript SSE proxy for MCP servers that use stdio transport.

878. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

879. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 217
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

880. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 216
   A Model Context Protocol (MCP) server for interacting with Twitter.

881. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 216
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

882. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 216
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

883. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 216
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

884. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 216
   Volcengine MCP Servers

885. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 216
   The Unofficial and Awesome Home Assistant MCP Server

886. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 214
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

887. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 214
   CAD MCP Server

888. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 213
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

889. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

890. **[tentix](https://github.com/labring/tentix)** - ⭐ 213
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

891. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 212
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

892. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 212
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

893. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 212
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

894. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 212

895. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 212
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

896. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 211
   A ReAct-Based Highly Robust Autonomous Agent Framework.

897. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 211
   Agent MCP for ffmpeg

898. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 211
   Razorpay's Official MCP Server

899. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 211

900. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 211
   Lean Theorem Prover MCP

901. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 211
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

902. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 210
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

903. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 210
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

904. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 210
   ModelContextProtocol for Figma's REST API

905. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 210
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

906. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 210
   Playwright MCP fork that works with Cloudflare Browser Rendering

907. **[lokka](https://github.com/merill/lokka)** - ⭐ 210
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

908. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 210
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

909. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 210
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

910. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 210
   mindmap, mcp server, artifact

911. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 210
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

912. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 209

913. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 209
   Lightweight C++ MCP (Model Context Protocol) SDK

914. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 208
   A Multi-modal MCP client for voice powered agentic workflows

915. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 208
   Model Context Protocol Servers for Milvus

916. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 207
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

917. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 207
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

918. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 207
   Penpot MCP server

919. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 206
   MCP server for Claude to access Outlook data via Microsoft Graph API

920. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 206
   Lightweight MCP server for Spotify

921. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

922. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 205

923. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 205
   An MCP server to use Sora video generation APIs

924. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

925. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 204
   MCP security wrapper

926. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 204
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

927. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 204
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

928. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 204
   interactive programming of melodies, producing MIDI 

929. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 204

930. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 204
   Zerodha Kite MCP server

931. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 203
   Model Context Protocol tool support for LangChain

932. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 203
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

933. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 203
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

934. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 203
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

935. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 203
   Java AI（智能体） 全场景应用开发框架（LLM，Function Call，RAG，Embedding，Reranking，Flow，MCP Server，Mcp Client，Mcp Proxy）。同时兼容 java8 ~ java25。也可嵌入到 SpringBoot2、jFinal、Vert.x 等框架中使用。。支持 MCP_2025_06_18（mcp streamable）

936. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 201
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

937. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

938. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 200
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

939. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 200

940. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 199
   Run and monitor MCP servers locally

941. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 199
   A Tiny Terminal Chat App for AI Models with MCP Client Support

942. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 199
   MCP server for Anki via AnkiConnect

943. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 199
   Things.app MCP Server

944. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 198
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

945. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 198

946. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 198
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

947. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 198
   🔎 A MCP server for Unsplash image search.

948. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 197
   A MCP Server for the RAG Web Browser Actor

949. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 197
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

950. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 196
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

951. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

952. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 196
   Pure Rust implementation of MCP server for headless terminal 

953. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 196
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

954. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

955. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 195
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

956. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 195
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

957. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 195
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

958. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 195
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

959. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 195
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

960. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 195
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

961. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 195
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

962. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 194
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

963. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 194
   R MCP Server

964. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 194
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

965. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 194
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

966. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 194
   Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs and allows claude to make direct edits and formatting. Use cases include writing notes, letters, resumes, creating tables, etc. 

967. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 193
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

968. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 192
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

969. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 192
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

970. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 192
   Homeassistant MCP server for 小智AI

971. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 192
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

972. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 191
   Absurdly easy Model Context Protocol Servers in Typescript

973. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 191
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

974. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 191
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

975. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 191
   A SEC EDGAR MCP (Model Context Protocol) Server

976. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 191
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

977. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

978. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 190
   Manage / Proxy / Secure your MCP Servers

979. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 189

980. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 188
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

981. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 188
   MCP server for Dynatrace Observability

982. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

983. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

984. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

985. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 187
   这是一个专为开发企业级MCP server而设计的通用开发框架

986. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

987. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 186
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

988. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 186
   Self-hosted AI RAG + MCP Platform

989. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 186
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

990. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 186
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

991. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 185
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

992. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 185
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

993. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

994. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 184
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

995. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 184
   Supabase MCP server created in Python.

996. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 184
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

997. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 184
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

998. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 183
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

999. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 183
   Platform to create, curate and host MCP servers ⚒️ Build production quality tools for your agents.

1000. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 183
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1001. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 183
   A MCP server for our beloved terminal multiplexer tmux.

1002. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1003. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1004. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 182
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1005. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 182
   A TypeScript framework for building MCP servers elegantly

1006. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 182
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1007. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 181
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1008. **[siconos](https://github.com/siconos/siconos)** - ⭐ 180
   Simulation framework for nonsmooth dynamical systems

1009. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 180
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1010. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 180

1011. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 180
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1012. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 179
   Model Context Protocol Servers in Quarkus

1013. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 179
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1014. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1015. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1016. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 178
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1017. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 178
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1018. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 178
   The Power BI Desktop MCP Server is a tool that lets AI assistants like Claude interact with your Power BI models programmatically. It enables Claude to read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1019. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 178
   Hugging Face MCP Server

1020. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 177
   An MCP server for Anki

1021. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1022. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 177
   MCP Server for ServiceNow

1023. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 176
   Google Search Console Insights with Claude AI for SEOs

1024. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 175
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1025. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 174
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1026. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 173
   A mongo db server for the model context protocol (MCP)

1027. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 173
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1028. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 173
   MCP Server for the Bilibili API, supporting various operations.

1029. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 173
   This extension enables developers to implement the MCP server features easily.

1030. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 173
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1031. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 172
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

1032. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 170

1033. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 170
   MCP for calling Siri Shorcuts from LLMs

1034. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 169
   pctx is the execution layer for agentic tool calls. It exposes custom tools and MCP servers as code that runs in secure sandboxes for token-efficient calls.

1035. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 169
   Examples of using Pipedream's MCP server in your app or AI agent.

1036. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 168
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1037. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 168
   A MCP server to search for accurate academic articles.

1038. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 167
   Built-in MCP client–powered document/news management tool with daily auto summaries, document interaction, user-defined notifications (email, apns, etc.), and customizable model support.内置 MCP 客户端的文档/资讯管理工具，支持每日自动总结、文档交互、自定义通知（邮箱、APNS等）以及模型自定义。

1039. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 167
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1040. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 167
   A Tiny Web Chat App for AI Models with MCP Client Support

1041. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 167
   MCP stdio server for frida

1042. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 166
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1043. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 166
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1044. **[command](https://github.com/scopecraft/command)** - ⭐ 166
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1045. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 166
   Turn any website or doc into an MCP server

1046. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 166
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1047. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 165
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1048. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 165
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1049. **[mcp-run-python](https://github.com/pydantic/mcp-run-python)** - ⭐ 165
   MCP server to run Python code in a sandbox.

1050. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 165
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1051. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 165
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1052. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 165
   A list of open-source AI projects you can use to generate income easily.

1053. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 164
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1054. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 164
   MCP server for TouchDesigner

1055. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 163
   One MCP Server, All Your Apps, Privacy First

1056. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 163
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1057. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 162
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1058. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 162
   Discord MCP Server for Claude Integration

1059. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1060. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 161
   MCP server to work with Telegram through MTProto

1061. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 161
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1062. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 161
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

1063. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 160
   Official Magic UI MCP server.

1064. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 160
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1065. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 160
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1066. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 160
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1067. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 159
   An MCP server for fetching URLs / Youtube video transcript.

1068. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 159
   Turn a web server into an MCP server in one click without making any code changes.

1069. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 159
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1070. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 159
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1071. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 159
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1072. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 158
   Command line interface for MCP clients with secure execution and customizable security policies

1073. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1074. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 158
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1075. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 158
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1076. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 158
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1077. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 158
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1078. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 157
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1079. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 157
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1080. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 157
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1081. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 157
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1082. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 157
   ToolSDK.ai's Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1083. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 156

1084. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 156
   MCP Server for Wazuh SIEM

1085. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 156
   Sketchup Model Context Protocol

1086. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 155
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1087. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 155
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1088. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 155
   Learn how to use MCP Servers with GitHub Copilot

1089. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 155
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1090. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 155
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1091. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 154
   Simple Slackbot MCP Client

1092. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 154
   MCP server implementation for Google's Gemini API

1093. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 154
   A simple CLI to install MCP servers into any client - auth included!

1094. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 153
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1095. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 152
   An MCP server to search for flights.

1096. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 152
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1097. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 151
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1098. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 150
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1099. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 150
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1100. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 150

1101. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 150
   MCP Server for AI Summarization

1102. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 149
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1103. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 149
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1104. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1105. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 149
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1106. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 149
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1107. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 148
   Desktop APP for Discover and Install MCP Servers

1108. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 148
   Deep Research for crypto - free & fully local

1109. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 148
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1110. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 148
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1111. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 148
   MCP server for searching and querying PubMed medical papers/research database

1112. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 147
   MCP Server for Postgres

1113. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 147
   Make MCP Server

1114. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 147
   A gateway demo for MCP SSE Server

1115. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 147
   Model Context Protocol For R

1116. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 147
   Instagram Direct messages MCP

1117. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 147
   Typescript SDK to build MCP servers in an agnostic way

1118. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 146
   MCP Server for using any LLM as a Tool

1119. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 146
   A simple MCP server to search for documentation (tutorial)

1120. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 146
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1121. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 146

1122. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 146
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

1123. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 145
   Model Context Protocol (MCP) server for constraint optimization and solving"

1124. **[relay](https://github.com/prism-php/relay)** - ⭐ 145
   An MCP client tool for Prism

1125. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 145
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1126. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 144
   MCP server to download entire websites

1127. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 144
   Connect any Open Data to any LLM with Model Context Protocol.

1128. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 144
   Model Context Protocol server implementation for Figma API

1129. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 144
   Goku is an HTTP load testing application written in Rust 

1130. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 144
   An MCP server that provides access to Postman.

1131. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 144

1132. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 144
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1133. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 143
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1134. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 143
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1135. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 143
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1136. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 143
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1137. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 142
   A PubMed MCP server.

1138. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 142
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1139. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 142
   A list of MCP (Model Context Protocol) servers for developer tools and services

1140. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 142
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1141. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 141

1142. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 140
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1143. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 140
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1144. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 140
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1145. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 140
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1146. **[kom](https://github.com/weibaohui/kom)** - ⭐ 140
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1147. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 140
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1148. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 140
   Neo4j official MCP Server

1149. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 139
   Simple MCP Server Implementation

1150. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 139
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1151. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 139
   A Model Context Protocol server for MySQL database operations

1152. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 138
   MCP server for Israel Government Data

1153. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 138
   A Model Context Protocol server for calculating.

1154. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 138
   A MCP Server for creating Powerpoint Presentations

1155. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 138
   Catch MCP server issues before your agents do.

1156. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 138
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1157. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 138
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1158. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 138
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1159. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 138
   Fastest way to build multi-agent system, agent-to-agent communication, MCPs, production ready serverless environment.

1160. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 137
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1161. **[eion](https://github.com/eiondb/eion)** - ⭐ 137
   Shared Memory Storage for Multi-Agent Systems

1162. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 137
   Connect your AI to your APIs on Postman

1163. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 137
   StarRocks MCP (Model Context Protocol) Server

1164. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 137
   Persistent Intelligence Infrastructure for AI Agents

1165. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 137
   Scrapeless Mcp Server

1166. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 136
   MCP server for discord bot

1167. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 136
   MCP Server for Google Slides

1168. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 136
   Dynamically expose tools from proxied servers based on an Agent Persona

1169. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 135
   MCP server for seamless document format conversion and processing

1170. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 135
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1171. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 135
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1172. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 135
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1173. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 135
   Persistent AI memory for coding assistants - MCP server providing context persistence across sessions for Claude, Cursor, Windsurf.  MCP Tools for task tracking, workflow automation, and AI memory. Eliminates context loss between sessions.

1174. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1175. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 134
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1176. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1177. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 133
   MSSQL Server MCP implementation written in C#

1178. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1179. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 133
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1180. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 133
   Serper MCP Server supporting search and webpage scraping

1181. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 133
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1182. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 133
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1183. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 132
   MCP server for AutoCAD LT: AI agents translate natural language into AutoLISP code for geometry, 600+ ISA 5.1 P&ID symbols, block attributes, and layer management—generating technical drawings with 80% performance improvement via batch operations.

1184. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 132
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1185. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 132
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1186. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 132
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1187. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 132
   MCP server to access Garmin data

1188. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 132
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1189. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 131
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1190. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 131
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1191. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 131
   mcp server for gitingest

1192. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 131
   Graphiti MCP Server

1193. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 131
   A local Apple Documentation crawler and MCP server. Written in Swift.

1194. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 131
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1195. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 131
   DataForSEO API modelcontextprotocol server 

1196. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 131
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1197. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 131
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1198. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 130
   Manage Your Kubernetes Cluster with k8s mcp-server

1199. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 130
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1200. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 130
   FrontMCP Framework

1201. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 130
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1202. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 130
   The Logfire MCP Server is here! :tada:

1203. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 130

1204. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 129
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

1205. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 129
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1206. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 129
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1207. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 129
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1208. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 129
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1209. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 129
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1210. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 128
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1211. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 128
   MCP server for understanding AWS spend

1212. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 128
   A collection of crypto MCP servers.

1213. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 128
   IMAP and SMTP via MCP Server

1214. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 127
   A Model Context Protocol server implementation for operations on AWS resources

1215. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 127
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1216. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 127
   Chat application with multi-agents system supports multi-models and MCP

1217. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

1218. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 126
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1219. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 126
   JetBrains MCP Server Plugin

1220. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 126
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1221. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 126
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1222. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 126
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1223. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 126
   🚀🎬 Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1224. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 126
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1225. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 126
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1226. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1227. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 125
   Model Context Protocol (MCP) server for the Zotero API, in Python

1228. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 125
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1229. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 125
   Dart AI Model Context Protocol (MCP) server

1230. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 125

1231. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 125
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1232. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 124
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1233. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 124
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1234. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1235. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 124
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1236. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 124
   High-performance CCXT MCP server for cryptocurrency exchange integration

1237. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 124
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1238. **[magg](https://github.com/sitbon/magg)** - ⭐ 124
   Magg: The MCP Aggregator

1239. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 124
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1240. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 123
   Buttplug.io Model Context Protocol (MCP) Server

1241. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 123
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1242. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 123
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1243. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 123

1244. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 123
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1245. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 122
   Intelligent spec workflow management MCP server

1246. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 122
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1247. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 122
   An MCP Server for Ollama

1248. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 122
   a private MCP server for accessing Linear

1249. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 122
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1250. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 122
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1251. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 122
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1252. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 122
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1253. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 122
   A guide on how to use the Figma MCP server

1254. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 121
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1255. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 121
   🐉 The fast, PHP way to build MCP servers

1256. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 121
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1257. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 121
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1258. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 121
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1259. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 121
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1260. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 120
   A Model Context Protocol server that provides access to BigQuery

1261. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 120
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1262. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 120
   MCP Servers SDK for TypeScript

1263. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 120
   MCP server for Unreal Engine 5

1264. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 120
   Model Context Protocol (MCP) with TikTok integration

1265. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 120
   It's time to push beyond MCP Servers... Right?

1266. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 120
   Your own Claude Code UI — local or cloud sandbox, in-browser VS Code, terminal, multi-provider support (Max, Z.AI, OpenRouter), custom skills, and MCP servers.

1267. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 119
   MCP server implementation for n8n workflow automation

1268. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 119
   An MCP server for FFmpeg

1269. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 119
   An MCP server that provides LLMs with the latest stable package versions when coding

1270. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 119
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1271. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 119
   Toolkit for Coding Agents to work reliably with repo of any size.

1272. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 119
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1273. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 119
   MCP Server for Searching Turkish Legislation

1274. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 118
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1275. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 118
   MCP stdio server for radare2

1276. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 118
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1277. **[kodit](https://github.com/helixml/kodit)** - ⭐ 116
   👩‍💻 MCP server to index external repositories

1278. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 116
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1279. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 116
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1280. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 116

1281. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 115
   Salesforce MCP Server

1282. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 115

1283. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 115
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1284. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 115
   Penpot's official MCP Server

1285. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 114
   BrowserStack's Official MCP Server

1286. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) for Jupyter Notebook

1287. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 114
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1288. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 114
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1289. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 114
   A proxy to use HTTP/SSE MCPs from STDIO clients

1290. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 113
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

1291. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 113
   An MCP server for InterviewReady

1292. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 113
   Fast and super efficient Minecraft Server written in C++

1293. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 113
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1294. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 113
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1295. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 113
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1296. **[cli](https://github.com/mcpgod/cli)** - ⭐ 112
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1297. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 112
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1298. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 112

1299. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 112
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1300. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 112
   Vector-search powered agent memory MCP server

1301. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 112
   Swagger to MCP server

1302. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 112
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1303. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1304. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 111
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1305. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1306. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1307. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 111
   Azure API Management as AI Gateway to Remote MCP servers.

1308. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 111
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1309. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 111
   Codex Mcp Server 

1310. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 111
   A modular MCP server that provides commonly used developer tools for AI coding agents

1311. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1312. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1313. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1314. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 110
   MariaDB MCP (Model Context Protocol) server implementation

1315. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 110
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1316. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 110
   Google Sheets MCP Server 📊🤖

1317. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 110
   Authentication for MCP Servers

1318. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 110
   💻 Give AI models complete control of your computer (probably a bad idea)

1319. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 110
   MCP server implementation for the UniFi network application

1320. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 109
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1321. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

1322. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 109
   MCP server for Oura API integration

1323. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 109
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1324. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 109
   Model Context Protocol Server for Swift

1325. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 109
   The AI platform to build Agentic workflows, MCP servers and ChatGPT apps 

1326. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 109
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1327. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 109
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1328. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 109
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1329. **[modex](https://github.com/theronic/modex)** - ⭐ 108
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1330. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 108
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1331. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1332. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1333. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 108
   MCP server for connecting agentic systems to search systems via searXNG

1334. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 108
   A Model Context Protocol Server to manipulate *.xcodeproj

1335. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 108
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1336. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 108
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1337. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 107
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1338. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 107
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1339. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 107
   Docker Hub MCP Server

1340. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 107
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1341. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 107
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1342. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 107
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1343. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 106
   A Slack MCP server

1344. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 106
   MCP server for interaction with Bitwarden.

1345. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 106
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1346. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 106
   Supercharge AI Agents, Safely

1347. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 106
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1348. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 106
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1349. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 106
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1350. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 105
   A redmine MCP server covering close to 100% of redmines API

1351. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 105
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1352. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 105
   Payload CMS MCP Server

1353. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 105
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1354. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 105
   MCP Client Implementation using Python, LangGraph and Gemini

1355. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 105
   Lightweight agent orchestration dev tool that lives in your repo

1356. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 105
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1357. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 104
   blazigly fast gRPC/MCP client & server implementation in zig

1358. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1359. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 104
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1360. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 104
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1361. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 104
   An MCP Server for your Self Hosted Supabase

1362. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 104

1363. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 104
   Control WordPress using WP-CLI, AI, and MCP.

1364. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 104
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1365. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 104
   An MCP client for Node.js.

1366. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 104
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1367. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 104
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1368. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 104
   Tools to allow LLM clients to interact with Linux systems remotely

1369. **[mcp](https://github.com/frappe/mcp)** - ⭐ 103
   Frappe MCP allows Frappe apps to function as MCP servers

1370. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1371. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 103
   MCP for semantic code search & navigation that reduces token waste

1372. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 103
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1373. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 103
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1374. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 102
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1375. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 102
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1376. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 102
   fast, secure c# runner

1377. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 102
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1378. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 102
   Open Source MCP Servers for Scientific Research

1379. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 101
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1380. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 101
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1381. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 101
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1382. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 101
   Official Vectorize MCP Server

1383. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 101
   Raindrop MCP Server

1384. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 101
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1385. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 101
   Isaac Simulation MCP Extension and Server

1386. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 101
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1387. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 101
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1388. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 101
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1389. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 101
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1390. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 101
   MCP Server for EMRs with FHIR

1391. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 101
   MCP Server for working with large Oracle databases

1392. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 101
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1393. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 100
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1394. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 100
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1395. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1396. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1397. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 100
    AI-powered security operations with Wazuh SIEM + Claude Desktop. Natural language threat detection, automated incident response & compliance. Real-time monitoring, ML anomaly detection. Transform your SOC with conversational security analysis. Production-ready MCP server.

1398. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 100
   Portainer MCP server

1399. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 100
   MCP server for interacting with the Aseprite API

1400. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 100
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1401. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 100
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1402. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 100
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1403. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 99
   Collection of examples of how to use Model Context Protocol with AWS.

1404. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1405. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 99
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1406. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1407. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1408. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1409. **[mcp](https://github.com/taskade/mcp)** - ⭐ 99
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1410. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 99
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1411. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1412. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 98
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1413. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 98
   claude mcp sse demo with server and client(cli、web)

1414. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 98
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1415. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 98
   MCP server for Dash, the macOS documentation browser

1416. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

1417. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 98
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1418. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 98
   Official Railway MCP Server for interacting with your Railway account

1419. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 98
   MCP Server for PolyMarket API

1420. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 98
      Convert any MCP server into a Claude Skill with 90% context savings

1421. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 97
   Node.js Client Implementation for Model Context Protocol (MCP)

1422. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 97
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1423. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 97
   A Google Tasks Model Context Protocol Server for Claude

1424. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 97
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1425. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 97
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1426. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 97
   MCP server for querying the Shodan API

1427. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 96
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1428. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 96
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1429. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1430. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 95
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1431. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 95
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1432. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 95
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1433. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 95
   first gemini based desktop client for MCP

1434. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 94
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1435. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 94
   Model Context Protocol (MCP) server for the Webflow Data API.

1436. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 94
   This is a Ruby implementation of MCP (Model Context Protocol) client

1437. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1438. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 93
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1439. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 93
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1440. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 93
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1441. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 92
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1442. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 92
   Model Context Protocol server for Replicate's API

1443. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 92
   A Model Context Protocol (MCP) server providing access to Google Search Console

1444. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 92
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1445. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 91
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1446. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for square

1447. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1448. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 89
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1449. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 89
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1450. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 89
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1451. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 89
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1452. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 89
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1453. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 88
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1454. **[mcp-web-ui](https://github.com/MegaGrindStone/mcp-web-ui)** - ⭐ 87
   MCP Web UI is a web-based user interface that serves as a Host within the Model Context Protocol (MCP) architecture. It provides a powerful and user-friendly interface for interacting with Large Language Models (LLMs) while managing context aggregation and coordination between clients and servers.

1455. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 87
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1456. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 87
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1457. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 87
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1458. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 86
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1459. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 86
   A model-context-protocol server for molecules.

1460. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 86
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1461. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 86
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1462. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 86
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1463. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1464. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 85
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1465. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 85
   CLI & API for MCP management

1466. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 85
   Ragie Model Context Protocol Server

1467. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 84
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1468. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 84
   Rails Engine with MCP compliant Spec.

1469. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 83
   A Model Context Protocol server that provides knowledge graph management capabilities.

1470. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 83
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1471. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 83
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1472. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1473. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1474. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1475. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1476. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1477. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 81
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1478. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 80
   Model Context Protocol (MCP) Server for the Keboola Platform

1479. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 80
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1480. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 80
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1481. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 80
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1482. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 80
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1483. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 80
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1484. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 79
   A model context protocol server that connects to Anki through AnkiConnect

1485. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 79
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1486. **[identity](https://github.com/agntcy/identity)** - ⭐ 79
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1487. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 79
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1488. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 79
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1489. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 79
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1490. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 79
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1491. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 79
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1492. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 78
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1493. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 78
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1494. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 78
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1495. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 78
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1496. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 77
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1497. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 77
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1498. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 76
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1499. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 76
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1500. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 76
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1501. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1502. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 75
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1503. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 75
   Model Context Protocol (MCP) Client for Apify's Actors

1504. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 75
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1505. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 75
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1506. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 75
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1507. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1508. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 74
   A WooCommerce (MCP) Model Context Protocol server

1509. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 73
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1510. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 73
   Model Context Protocol for Actual Budget API

1511. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1512. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 72
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1513. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 72
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1514. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 72
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1515. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 72
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1516. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 71
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1517. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 71
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1518. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 71
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1519. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 71
   An md file as a chat interface and editable history in one.

1520. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1521. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 69
   Model Context Protocol implementation for retrieving codebases using RepoMix

1522. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 69
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1523. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 69
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1524. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 69
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1525. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 68
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1526. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 68
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1527. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 68
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1528. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 68
   A Model Context Protocol server for Hopper Disassembler

1529. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 68
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1530. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1531. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1532. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1533. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 67
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1534. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1535. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 67
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1536. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 67
   MCP client for local ollama models

1537. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 67
   An extension of MCP for SillyTavern.

1538. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 67
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

1539. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 67
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1540. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 67
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1541. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 67
   Universal command-line client for MCP. Supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for scripting and code mode, proxy for AI sandboxes, and more.

1542. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 66
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1543. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 66
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1544. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 66
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1545. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 66
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

1546. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 66
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1547. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 66
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1548. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 66

1549. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 66
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1550. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 65
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1551. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 65
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1552. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 65
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1553. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 65
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1554. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 65
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1555. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 65
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1556. **[ViaMCP](https://github.com/ViaVersionMCP/ViaMCP)** - ⭐ 65
   Client-side Implementation of the Via* projects for MCP

1557. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 64
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1558. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 64
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

1559. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 64
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1560. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1561. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1562. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 64
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1563. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 64
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1564. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

1565. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 63
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1566. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 63
   Model Context Protocol(MCP) 中文教程讲解

1567. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 63
   A Model Context Protocol implementation for FHIR

1568. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1569. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 62
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1570. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 62
   Model Context Protocol for x64dbg & x32dbg

1571. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 62
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1572. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

1573. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 62
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resources for client-side exploration.

1574. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 62
   From Java Dev to AI Engineer: Spring AI Fast Track

1575. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 62
   A CLI tool for easy installation of MCP servers and managing their configuration

1576. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 62
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1577. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 62
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1578. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1579. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1580. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 61
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1581. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 61
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1582. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 61
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1583. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 61
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1584. **[kollektiv-mcp](https://github.com/alexander-zuev/kollektiv-mcp)** - ⭐ 61
   Kollektiv MCP enables you to chat with and query your own documents directly from IDEs and MCP clients. Private, secure, and integrated into your favorite code editor

1585. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1586. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 60
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1587. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 60
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1588. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 60
   Index of all Model Context Protocol (MCP) clients and their capabilities

1589. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 60
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1590. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 59
   Miro integration for Model Context Protocol

1591. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1592. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server for Rember.

1593. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 59
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1594. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 59
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1595. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 59
   Python 实现 MCP client / service

1596. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 59
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

1597. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 59
   A full featured, enterprise grade rust MCP SDK

1598. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 59
   Model Context Protocol for YNAB (you need a budget)

1599. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

1600. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

1601. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 58
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1602. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 58
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1603. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 58
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

1604. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 58
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

1605. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 57
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

1606. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 57
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1607. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

1608. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

1609. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 57
   MCP router and Web Based MCP client

1610. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 57
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

1611. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 57
   A Clojure SDK to create MCP servers (and eventually clients)

1612. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 57
   Python code execution sandbox with programmatic MCP tool calling (PTC)

1613. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 56
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

1614. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

1615. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1616. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 56
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1617. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 56
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1618. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 56
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1619. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 56
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

1620. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 56
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

1621. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

1622. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 55
   MKP is a Model Context Protocol (MCP) server for Kubernetes

1623. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 55
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

1624. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 55
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1625. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 55
   Build multi-model chatbots and agents from intent.

1626. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 55
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

1627. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 54
   A Model Context Protocol server for Ashra

1628. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

1629. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

1630. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 54
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

1631. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 54
   A Model Context Protocol (MCP) server for Microsoft Clarity

1632. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 54
   可视化的配置和管理，给xiaozhi接入mcp

1633. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 54
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1634. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 53
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

1635. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 53
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

1636. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 53
   Quantum-proof MCP Server and Client Interactions

1637. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

1638. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

1639. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 53
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1640. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 52
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

1641. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 52
   Model Context Protocol Servers for Azure AI Search

1642. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

1643. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 52
   A Nasdaq Data Link MCP (Model Context Protocol) Server

1644. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 52
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

1645. **[client](https://github.com/php-mcp/client)** - ⭐ 52
   Core PHP implementation for the Model Context Protocol (MCP) Client

1646. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 52
   MCP (Model Context Protocol) server plugin for CAP NodeJS

1647. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

1648. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 52
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

1649. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 52
   OCaml implementation of the Model Context Protocol (MCP)

1650. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 52
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

1651. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 52
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1652. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

1653. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 51
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

1654. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 51
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1655. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 51
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

1656. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 51
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

1657. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

1658. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 51
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

1659. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 51
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1660. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

1661. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

1662. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 50
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

1663. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 50
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

1664. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 50
   ABAP MCP - Model Context Protocol - Server SDK

1665. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 50
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

1666. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 50
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

1667. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1668. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

1669. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 50
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

1670. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 50
   MCP Server for IBKR Client

1671. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 50
   MCP Guard secures your MCP client from prompt injection attacks and more.

1672. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 50
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

1673. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 50
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

1674. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

1675. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 49
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

1676. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 49
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

1677. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 49
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

1678. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

1679. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 49
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

1680. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 49
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

1681. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

1682. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 48
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

1683. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 48
   Anthropic’s Model Context Protocol implementation for Oat++

1684. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

1685. **[mcp](https://github.com/goplus/mcp)** - ⭐ 48
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

1686. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 48
   A Model Context Protocol server that validates and renders Mermaid diagrams.

1687. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 48
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

1688. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 48
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1689. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

1690. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

1691. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 48
   Unblock, scrape, and search tools for MCP clients

1692. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 48
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1693. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 48
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

1694. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

1695. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 47
   An implementation of the Model Context Protocol in Ruby.

1696. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

1697. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 47
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

1698. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 47
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

1699. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 47
   vMCP - Virtual Model Context Protocol

1700. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 47
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

1701. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 47
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1702. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

1703. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 47
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

1704. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 46
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

1705. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 46
   Inkdrop Model Context Protocol Server

1706. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 46
   OpenAPI Schema Model Context Protocol Server

1707. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 46
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

1708. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

1709. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 46
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

1710. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 46
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

1711. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

1712. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 46
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

1713. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 46
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

1714. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 46
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

1715. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

1716. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

1717. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 46
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

1718. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

1719. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

1720. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

1721. **[go-mcp](https://github.com/MegaGrindStone/go-mcp)** - ⭐ 45
   A Go implementation of the Model Context Protocol (MCP) - an open protocol that enables seamless integration between LLM applications and external data sources and tools.

1722. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 45
   A Model-Context-Protocol (MCP) Server for Active Directory

1723. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 45
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

1724. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 45
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

1725. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

1726. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 45
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

1727. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 45
   A Model Context Protocol server for Zendesk

1728. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 45
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

1729. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 45
   Sample MCP Server and MCP client with Aspire

1730. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 45
   Un-official Serper Google search server for Cline and other MCP clients

1731. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 45
   MCPcat is an analytics platform for MCP server owners 🐱.

1732. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

1733. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 45
   共学《MCP极简开发》项目代码

1734. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 45
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

1735. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 45
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1736. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 44
   Model Context Protocol to fetch youtube transcript

1737. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 44
   Model Context Protocol server for Flight Tracking

1738. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

1739. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 44
   📚 An intelligent toolkit to automatically parse, complete, and format academic references, with Model Context Protocol (MCP) support.

1740. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

1741. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 44
   An opinionated starter template for making Model Context Protocol (MCP) servers

1742. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 44
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

1743. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 44
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1744. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 44
   Model Context Protocol for WeChat

1745. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 44
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

1746. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

1747. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

1748. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 44
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

1749. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

1750. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 44
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

1751. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

1752. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

1753. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 43
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

1754. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

1755. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 43
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

1756. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 43
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

1757. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 43
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

1758. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 43
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

1759. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 43
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1760. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 43
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

1761. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

1762. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 43
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

1763. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

1764. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 42
   Model Context Protocol server for Salesforce REST API integration

1765. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 42
   GraphQL Schema Model Context Protocol Server

1766. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

1767. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

1768. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 42
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

1769. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 42
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

1770. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 42
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

1771. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 42
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

1772. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 42
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

1773. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 42
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

1774. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

1775. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 42
   Amadeus MCP(Model Context Protocol) Server

1776. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 42
   An implementation of the Model Context Protocol for the World Bank open data API

1777. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 42
   A Model Context Protocol server implementation for Kagi's API

1778. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 42
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

1779. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 42
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

1780. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 42
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

1781. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 42
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

1782. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 42
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

1783. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

1784. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 41
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

1785. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

1786. **[mcp](https://github.com/40ants/mcp)** - ⭐ 41
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

1787. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 41
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

1788. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

1789. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 41
   A Model Context Protocol server for Go developers

1790. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

1791. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 41
   A production-ready Model Context Protocol (MCP) server for semantic memory management

1792. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 41
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

1793. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 41
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

1794. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 41
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

1795. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 40
   A Model Context Protocol server for Dify

1796. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

1797. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

1798. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

1799. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

1800. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 40
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

1801. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

1802. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

1803. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 40
   MCP (Model Context Protocol) server for the Contentful Management API

1804. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 40
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

1805. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 40
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

1806. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 40
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

1807. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

1808. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

1809. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

1810. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 40
   Model Context Protocol Clojure support including REPL integration with development tools.

1811. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 40
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

1812. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 40
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

1813. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 40
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

1814. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 40
   A simple NextJS MCP client with sensible keybindings

1815. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 40
   Dynamic Shell Command MCP Server

1816. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 40
   Implementation of Model Context Protocol server for Mailgun APIs

1817. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 40
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

1818. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 40
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

1819. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 40
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1820. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

1821. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

1822. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

1823. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 39
   Model Context Protocol server for OpenStreetMap data

1824. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 39
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

1825. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 39
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

1826. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 39
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

1827. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

1828. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 39
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1829. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 39
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

1830. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

1831. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 39
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

1832. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 39
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

1833. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 39
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

1834. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

1835. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 39
   A MCP client for browser-use

1836. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 39
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

1837. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

1838. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 38
   Algorand Model Context Protocol (Server & Client)

1839. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 38
   It shows how to use model-context-protocol. 

1840. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

1841. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 38
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

1842. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

1843. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 38
   Build tools for LLMs in Rust using Model Context Protocol

1844. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

1845. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 38
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

1846. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 38
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

1847. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 38
   Model Context Protocol server for ActivityWatch time tracking data

1848. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 38
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

1849. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 38
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

1850. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 38
   MCP server for anki

1851. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 38
   Learn how to implement MCP client with SwiftUI and Anthropic API

1852. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 38
   Go SDK for interacting with the MCP Toolbox for Databases.

1853. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

1854. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 38
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

1855. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 37
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

1856. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1857. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 37
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

1858. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 37
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

1859. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 37
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

1860. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 37
   Attio Model Context Protocol (MCP) server implementation

1861. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 37
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

1862. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 37
   Model Context Protocol server for Sitecore

1863. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 37
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

1864. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 37
   A Model Context Protocol server that provides access to Shodan API functionality

1865. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 37
   An MCP server for querying Solana transactions using natural language with Solscan API

1866. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 37
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

1867. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 37
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

1868. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 37
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

1869. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 36
   A Chat Client for LLMs, written in Compose Multiplatform.

1870. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

1871. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 36
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

1872. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

1873. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 36
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

1874. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

1875. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

1876. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

1877. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 36
   Model Context Protocol Minecraft Server

1878. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 36
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

1879. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 36
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

1880. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

1881. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

1882. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 36
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

1883. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 36
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

1884. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 36
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

1885. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 36
   Bluesky MCP (Model Context Protocol) Server

1886. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 36
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

1887. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

1888. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

1889. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 35
   Model Context Protocol (MCP) implementation for iOS simulators

1890. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

1891. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 35
   Model Context Protocol server to let LLMs write and execute matlab scripts 

1892. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

1893. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 35
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

1894. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 35
   Privacy-first local RAG server for Cursor, Claude Code, and more — powered by the Model Context Protocol.

1895. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 35
   A Model Context Protocol for checking domain name registration status in bulk.

1896. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 35
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

1897. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 35
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

1898. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 35
   Model Context Protocol (MCP) Server for Mistral OCR API

1899. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 35
   Model Context Protocol (MCP) server for LinkedIn API integration

1900. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 35
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

1901. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 35
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

1902. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

1903. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 35
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

1904. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 34
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

1905. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

1906. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

1907. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 34
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

1908. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

1909. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 34
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

1910. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

1911. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

1912. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 34
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

1913. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 34
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

1914. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 34
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

1915. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 34
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

1916. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

1917. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 34
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

1918. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

1919. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

1920. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 34
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

1921. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 33
   Model Context Protocol server written in Scala

1922. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 33
   Model Context Protocol Server for Apache OpenDAL™

1923. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 33
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

1924. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

1925. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

1926. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

1927. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 33
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

1928. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 33
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

1929. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 33
   IMAP Model Context Protocol server for interactive email processing

1930. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 33
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

1931. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 33
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

1932. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 33
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

1933. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

1934. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 33
   A powerful Model Context Protocol server for LinkedIn API integration

1935. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 33
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

1936. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 33
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

1937. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

1938. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 33
   Altium Model Context Protocol server and Altium API script

1939. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

1940. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 32
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

1941. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

1942. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 32
   Model Context Protocol (MCP) server implementation for Autodesk Maya

1943. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

1944. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

1945. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 32
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

1946. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 32
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

1947. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 32
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

1948. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 32
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

1949. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

1950. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 32
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

1951. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

1952. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 32
   Turn any MCP Client into a "multi-agent" system (via prompting)

1953. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 32
   Rimworld Coding RAG MCP server

1954. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 31
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

1955. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

1956. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

1957. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 31
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

1958. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 31
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

1959. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

1960. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 31
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

1961. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

1962. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

1963. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 31
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

1964. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 31
   About A Model Context Protocol server that executes commands in the current WezTerm session

1965. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 31
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

1966. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 31
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

1967. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 31
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

1968. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 31
   Claude Unified Model Context Interaction Protocol

1969. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

1970. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 31
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

1971. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 31
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

1972. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 31
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

1973. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 31
   MCP client for Discourse sites

1974. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

1975. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

1976. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 30
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

1977. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 30
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

1978. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 30
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

1979. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

1980. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 30
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

1981. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server for openBIM

1982. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 30
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

1983. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 30
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

1984. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 30
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

1985. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 30
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

1986. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 30
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

1987. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 30
   Emacs Lisp implementation of the Model Context Protocol

1988. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

1989. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 30
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

1990. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 30
   Model Context Server Protocol for your HANA DB

1991. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 30
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

1992. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

1993. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 30
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

1994. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 30
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

1995. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

1996. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 30
   List of Awesome MCP Servers and Clients for building Agentic Devops 

1997. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 30
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

1998. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 30
   Query model running with Ollama from within Claude Desktop or other MCP clients

1999. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 30
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2000. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2001. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 30
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2002. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 30
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2003. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 30
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2004. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 29
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2005. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

2006. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2007. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 29
   Model Context Protocol server for Cyclops

2008. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2009. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 29
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2010. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2011. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 29
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2012. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2013. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2014. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 29
   Model Context Protocol (MCP) server that interacts with a Debugger

2015. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 29
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2016. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 29
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2017. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 29
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2018. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 29
   Sync MCP (Model Context Protocol) configurations across AI tools

2019. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2020. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 29
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2021. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2022. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2023. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 29
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2024. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

2025. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

2026. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

2027. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

2028. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 28
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2029. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 28
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2030. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2031. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 28
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2032. **[mcp](https://github.com/fastly/mcp)** - ⭐ 28
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2033. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

2034. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2035. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2036. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 28
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2037. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 28
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2038. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 28
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2039. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 28
   Model Context Protocol Server of Rod

2040. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 28
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2041. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 28
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2042. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 28
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2043. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 28
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2044. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2045. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 28
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2046. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 28
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2047. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2048. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2049. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 28
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2050. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 27
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

2051. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 27
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

2052. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

2053. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 27
   Asterisk Model Context Protocol (MCP) server.

2054. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 27
   MCP (Model Context Protocol) server for biothings

2055. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

2056. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2057. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2058. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 27
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2059. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2060. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

2061. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2062. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 27
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

2063. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 27
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2064. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 27
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2065. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for Polymarket prediction markets, providing real-time market data, prices, and AI-powered analysis tools for Claude Desktop integration.

2066. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2067. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

2068. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 27
   Tools for building modern & secure MCP integrations across the client and server side

2069. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 27
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2070. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 27
   Fast rust MCP proxy between stdio and SSE

2071. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 27
   Learn Model Context Protocol with Python, published by Packt

2072. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 27
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

2073. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

2074. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

2075. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 26
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2076. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

2077. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 26
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

2078. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 26
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

2079. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

2080. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 26
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2081. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 26
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

2082. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 26
   An implementation of Giphy integration with Model Context Protocol

2083. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 26
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2084. **[mcp-advisor](https://github.com/olaservo/mcp-advisor)** - ⭐ 26
   MCP Server to assist LLMs and humans on Model Context Protocol spec compliance and understanding

2085. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 26
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2086. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 26
   MCP (Model Context Protocol) Server for postgres Database

2087. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 26
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2088. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 26
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2089. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 26
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2090. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 26
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

2091. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

2092. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

2093. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 26
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2094. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 26
   a web logging proxy for MCP client-server communication

2095. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

2096. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 25
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2097. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

2098. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

2099. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 25
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

2100. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

2101. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

2102. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 25
   Model Context Protocol to bridge in Substack writings to Claude.

2103. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

2104. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

2105. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

2106. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 25
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2107. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

2108. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 25
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

2109. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2110. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

2111. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

2112. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 25
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

2113. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 25
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

2114. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 25
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

2115. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 25
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2116. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 25
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2117. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 25
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2118. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 25
   Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from data.gouv.fr, the French national Open Data platform, directly through conversation.

2119. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

2120. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 25
   Headless IDA Pro binary analysis via Model Context Protocol

2121. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 25
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2122. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2123. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 25
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

2124. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

2125. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 25
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2126. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 25
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2127. **[levante](https://github.com/levante-hub/levante)** - ⭐ 25
   Levante - Personal, Secure, Free, Local AI, MCP Client

2128. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 25
   Azure AI Foundry - Agents related sample code

2129. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 25
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2130. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 25
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

2131. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

2132. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 25
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2133. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

2134. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 25
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

2135. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 25
   A generic mcp server fuzzer

2136. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 24
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

2137. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

2138. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 24
   A Model Context Protocol Server for Interacting with Slack

2139. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 24
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

2140. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

2141. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

2142. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

2143. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2144. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2145. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 24
   Model Context Protocol Server for NebulaGraph 3.x

2146. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

2147. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 24
   A simple Model Context Protocol (MCP) server for Clay.

2148. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

2149. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 24
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2150. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 24
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

2151. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 24
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

2152. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 24
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2153. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

2154. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 24
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

2155. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

2156. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 24
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

2157. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 24
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2158. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

2159. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 24
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

2160. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 24
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2161. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 24
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2162. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 24
   Simple MCP Client for remote MCP Servers 🌐

2163. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 24
   A Curated List of MCP Servers, Clients and Toolkits

2164. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 24
   Educational repo for MCP streamable HTTP servers and clients

2165. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

2166. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 24
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

2167. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

2168. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for GreptimeDB

2169. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 23
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2170. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

2171. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 23
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2172. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 23
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2173. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 23
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

2174. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

2175. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2176. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 23
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2177. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

2178. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 23
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

2179. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

2180. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

2181. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 23
   A Fastify plugin to run Model Context Protocol (MCP) servers

2182. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 23
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

2183. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 23
   Model Context Protocol SDK implemented in Lua for OpenResty

2184. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 23
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

2185. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

2186. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 23
   A Model Context Protocol server for 3D Slicer integration

2187. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 23
   PowerPlatform Model Context Protocol server

2188. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 23
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2189. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 23
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2190. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 23
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2191. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 23
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2192. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2193. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 23
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2194. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 23
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

2195. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 23
   CLI that uses DSPy to interact with MCP servers.

2196. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

2197. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 23
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

2198. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 23
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

2199. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 23
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

2200. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

2201. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

2202. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

2203. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 22
   A MCP(Model Context Protocol) server that accesses to Lightdash

2204. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 22
   A personal assistant AI agent built with the Model Context Protocol (MCP)

2205. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

2206. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

2207. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

2208. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

2209. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

2210. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

2211. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

2212. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

2213. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

2214. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 22
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

2215. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 22
   Python-based MCP server for BlazeMeter API — orchestrate performance-test lifecycle (create, configure, run, analyze) and manage tests, workspaces, projects & accounts via Model Context Protocol

2216. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

2217. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 22
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

2218. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 22
   Model Context Protocol server for querying Cursor chat history

2219. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 22
   model context protocol for Autodesk Revit

2220. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 22
   Model Context Protocol server for Github Repo // Reading Github Repo

2221. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 22
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2222. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 22
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

2223. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2224. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

2225. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

2226. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 22
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2227. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 22
   Zillow MCP Server for real estate data access via the Model Context Protocol

2228. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 22
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

2229. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2230. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 22
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2231. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 22
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

2232. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 22
   Tanzu Platform Chat

2233. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

2234. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

2235. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

2236. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 22
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

2237. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 22
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

2238. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

2239. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2240. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

2241. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 21
   MCP (model context protocol) server for interacting with dbt Docs

2242. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

2243. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

2244. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

2245. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 21
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

2246. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

2247. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

2248. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

2249. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

2250. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 21
   An MCP client for slack in Typescript

2251. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 21
   MCP agent/client/server implementation for private knowledge base

2252. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 21
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

2253. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 21
   A collection of mcp servers/client/sdks

2254. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 21
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

2255. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

2256. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 21
   Simple MCP SDK in Java

2257. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 21
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

2258. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 20
   Memory Cache Server for use with supported MCP API Clients.

2259. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 20
   Haskell server/client for MCP (Model Context Protocol)

2260. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 20
   MCP server to expose local zotero repository to MCP clients 

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 40,453
   基于大模型搭建的聊天机器人，同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入，可选择ChatGPT/Claude/DeepSeek/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Kimi/LinkAI，能处理文本、语音和图片，访问操作系统和互联网，支持基于自有知识库进行定制企业智能客服。

2. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 15,205
   AgentScope: Agent-Oriented Programming for Building LLM Applications

3. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,135
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 7,936
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,310
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

6. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,621
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

7. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,592
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

8. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,317
   extendable code review and QA agent 🚢

9. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,636

10. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,583
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

11. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 792
   OpenTelemetry Instrumentation for AI Observability

12. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 764
   A code repository indexing tool to supercharge your LLM experience.

13. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 707
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

14. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 579
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

15. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 558
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

16. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 535
   VoiceMode MCP brings natural conversations to Claude Code

17. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 531
   The easiest way to discover and install MCPs

18. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 396
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

19. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 333
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

20. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 265
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

21. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 153
   Python SDK for interacting with the MCP Toolbox for Databases. 

22. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 94
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

23. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 68
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

24. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

25. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 56
   Javascript SDK for interacting with the MCP Toolbox for Databases.

26. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 53

27. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 43
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

28. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 41
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

29. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

30. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

31. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 26
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

32. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

33. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

34. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 166,732
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,488
   🦍 The Cloud-Native Gateway for APIs & AI

3. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 41,069
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 26,775
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,302
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,151
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 15,713
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 14,765
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI features. ✨

9. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

10. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

11. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,442
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,435
   A cross-platform Markdown AI note-taking software.

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,253
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

14. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,487
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

15. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,343
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,736
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,523
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 6,765
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

19. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,565
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,635
   Adversary simulation and Red teaming platform with AI

21. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,428
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,146
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,108
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,016
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

25. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 3,761
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

26. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 3,292
   Memory infrastructure for LLMs and AI agents

27. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,254
   Shadcn/ui components library for building ChatGPT Apps

28. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,687
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

29. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 2,638
   System Level Intelligent Router for Mixture-of-Models

30. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,507
   A highly opinionated, zero-configuration linter and formatter.

31. **[harbor](https://github.com/av/harbor)** - ⭐ 2,235
   Effortlessly run LLM backends, APIs, frontends, and services with one command.

32. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,866
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

33. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,720
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

34. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,694
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

35. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,456
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

36. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,409
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

37. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,385
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

38. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

39. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,285
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

40. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,258
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

41. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,246
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

42. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,110
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

43. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,090
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

44. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,071
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

45. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,062
   A single interface to use and evaluate different agent frameworks 

46. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 998
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

47. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 983
   AIPex: AI browser automation assistant, no migration and privacy first. ChatGPT Atlas Alternative, Alternative to Manus Browser Operator, Alternative to Claude Chrome

48. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 974
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

49. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 958
   Korea Investment & Securities Open API Github

50. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 953
   Arduino MCP2515 CAN interface library

51. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 761
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

52. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 724
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

53. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 693
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

54. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 692
   Solidity Static Analyzer that easily integrates into your editor

55. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 686
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

56. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 653
   A personal AI assistant for everyone

57. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 618
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

58. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 581
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

59. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 515
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

60. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 450
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

61. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 439
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

62. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

63. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 410
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

64. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 396
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

65. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 394
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

66. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 383
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

67. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 382
   Minecraft: Pi Edition API Python Library

68. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 380
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

69. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 379
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

70. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

71. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 351
   Local first codebase intelligence

72. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 344
   Python toolkit for building graph-enhanced GenAI applications

73. **[exograph](https://github.com/exograph/exograph)** - ⭐ 340
   Build production-ready backends in minutes

74. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 334
   Blender python addon to increase workflow for creating minecraft renders and animations

75. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 330
   MCP for Unreal Engine 5

76. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 321
   Sega Master System / Game Gear / SG-1000 emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

77. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

78. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 319
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

79. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 308
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

80. **[amical](https://github.com/amicalhq/amical)** - ⭐ 303
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

81. **[depyler](https://github.com/paiml/depyler)** - ⭐ 298
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

82. **[bridle](https://github.com/neiii/bridle)** - ⭐ 297
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose)

83. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 295
   This is the official website for TuriX Computer-use-Agent

84. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 292
   Software architecture tooling for the AI age

85. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 268
   An in-depth book and reference on building agentic systems like Claude Code

86. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 265
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

87. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

88. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 257
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

89. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 253
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

90. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 243
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

91. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 243
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

92. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 242
   AI for Ethical Hacking - Workshop

93. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 238
   Public facing repo for MCP SRG mappings.

94. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 233
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

95. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 230
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

96. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 228
   An introduction to the world of AI Agents

97. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 226
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

98. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 219
   A website to generate Minecraft profile pictures

99. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

100. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 213
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

101. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 208
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

102. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 201
   Re-usable multi part components built on React Aria and TailwindCSS. 

103. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

104. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

105. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 185
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

106. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 183
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

107. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

108. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 118
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

109. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 104
   Solid Tumor Associative Modeling in Pathology

110. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 98
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

111. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 71
   A lightweight, open, and extensible multi-LLM interaction studio.

112. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 68
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

113. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 63
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

114. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 61
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

115. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 48
   Houdini integration through the Model Context Protocol

116. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

117. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 30
   Prompt-driven automation platform - Transform natural language into executable workflows

118. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

119. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 26
   Build AI Agent using Google ADK , MCP and Gemma 3 model

120. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 25
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具与 Wireshark 进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

121. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

122. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 23
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,614
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 6,822
   Specification and documentation for the Model Context Protocol

2. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,854
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

3. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 925
   程序员鱼皮的 AI 资源导航，汇总热门的 AI 大模型和工具，比如 Deepseek 使用指南、提示词技巧、知识干货、应用场景、AI 变现、行业资讯、教程资源等一系列内容，帮助你快速掌握 AI 技术，走在时代前沿。涉及大模型 ChatGPT、Claude、Gemini、Deepseek、QWEN、GROK 等；涉及技术 Spring AI、LangChain、RAG、MCP、A2A 等；涉及 Cursor、TRAE 等工具。本项目为开源文档版本，已升级为鱼皮AI导航网站

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 356
   One-stop handbook for building, deploying, and understanding LLM agents with 60+ skeletons, tutorials, ecosystem guides, and evaluation tools.

5. **[codedox](https://github.com/chriswritescode-dev/codedox)** - ⭐ 26
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

