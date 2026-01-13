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

## 📚 Projects (2775 total)

> Last updated: **2026-01-13**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 125,707
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 120,447
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 90,679
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 78,730
   A collection of MCP servers.

5. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,322
   The fastest path to AI-powered full stack observability, even for lean teams.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 76,073
   Model Context Protocol Servers

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 71,336
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,056
   🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers, Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.

9. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 53,223
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

10. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 44,996
   🔥AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

11. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 42,868
   🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。 AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测。支持 Docker 一键部署，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。⭐

12. **[context7](https://github.com/upstash/context7)** - ⭐ 41,716
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

13. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,249
   Federated Query Engine for AI - The only MCP Server you'll ever need

14. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

15. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 33,017
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

16. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 32,833
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

17. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,509
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

18. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 31,245
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

19. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,357
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

20. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 25,894
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

21. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 25,848
   GitHub's official MCP Server

22. **[goose](https://github.com/block/goose)** - ⭐ 25,770
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

23. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 25,458
   Playwright MCP server

24. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 24,824
   An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations.

25. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 23,281
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

26. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 23,148
   An MCP-based chatbot | 一个基于MCP的聊天机器人

27. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 21,893
   🚀 The fast, Pythonic way to build MCP servers and clients

28. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 21,157
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

29. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 21,078
   The official Python SDK for Model Context Protocol servers and clients

30. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 20,635
   Chrome DevTools for coding agents

31. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,315
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

32. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 19,811
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

33. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 19,271
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

34. **[serena](https://github.com/oraios/serena)** - ⭐ 18,544
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

35. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,091
   Your API ⇒ Paid MCP. Instantly.

36. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 15,101

37. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 14,022
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

38. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,403
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

39. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,278
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

40. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 12,917
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

41. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 12,500
   MCP server to provide Figma layout information to AI coding agents like Cursor

42. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 12,393
   MCP Toolbox for Databases is an open source MCP server for databases.

43. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 11,759
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

44. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 11,594
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

45. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,361
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

46. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,294
   The official TypeScript SDK for Model Context Protocol servers and clients

47. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 10,828
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex & Gemini CLI.

48. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 10,819
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

49. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,384
   Yet another WebUI for Nginx

50. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,260
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

51. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 9,904
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

52. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

53. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 9,739
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书无水印作品文件

54. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 8,895
   mcp-use is the easiest way to interact with mcp servers with custom agents

55. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,766
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

56. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 8,479
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

57. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,253
   Visual testing tool for MCP servers

58. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,244
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

59. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 7,999
   MCP for xiaohongshu.com

60. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 7,962
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

61. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 7,938
   Build effective agents using Model Context Protocol and simple workflow patterns

62. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 7,846
   AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.

63. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,372
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

64. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

65. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,265
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

66. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 7,049
   MCP Server for Ghidra

67. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 6,971
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

68. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 6,541
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

69. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,249
   A community driven registry service for Model Context Protocol (MCP) servers.

70. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,191
   A collection of MCP clients.

71. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 5,911
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

72. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 5,893
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

73. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 5,669
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

74. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,588
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

75. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,588
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

76. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,423
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

77. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,247
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

78. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,231
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

79. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,201
   WhatsApp MCP server

80. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,137
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

81. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,062
   Awesome MCP Servers - A curated list of Model Context Protocol servers

82. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,028
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

83. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,027
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

84. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,009
   Install, run and deploy your own decentralized AI agent service

85. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 4,996
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

86. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 4,945
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

87. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 4,860
   A model-driven approach to building AI agents in just a few lines of code.

88. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 4,850
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno) —or use via CLI, REST API, or MCP server.

89. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 4,822
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

90. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 4,782
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

91. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,700
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

92. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,533
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

93. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 4,474
   Memory infrastructure for LLMs and AI agents

94. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,387
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

95. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,369
   opensource self-hosted sandboxes for ai agents

96. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,310
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

97. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,240
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

98. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,107
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

99. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,011
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

100. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 3,951
   MCP server for Atlassian tools (Confluence, Jira)

101. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 3,907
   MCP Server for Computer Use in Windows

102. **[Olares](https://github.com/beclab/Olares)** - ⭐ 3,901
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

103. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,872
   The Cursor & Windsurf community, find rules and MCPs

104. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,860
   A simple, secure MCP-to-OpenAPI proxy server

105. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,836
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

106. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,807
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

107. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,780
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

108. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,698
   Official Notion MCP Server

109. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,695
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

110. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,684
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

111. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,634
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

112. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 3,612
   A Model Context Protocol (MCP) server that provides Xcode-related tools for integration with AI assistants and other MCP clients.

113. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,603
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

114. **[core](https://github.com/opensumi/core)** - ⭐ 3,589
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

115. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,584
   Define, Prompt and Test MCP enabled Agents and Workflows

116. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,538
   Exa MCP for web search and web crawling!

117. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,512
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

118. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,501
   🤖 A visualization mcp contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

119. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,471
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

120. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

121. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,428
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

122. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,349
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP. Built with Golang for efficient memory use. 

123. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,330
   A curated list of Model Context Protocol (MCP) servers

124. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,294
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

125. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 3,290
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

126. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,277

127. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,264
   LangChain 🔌 MCP

128. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,257
   Model Context Protocol(MCP) 编程极速入门

129. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,203
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

130. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,137
   An Autonomous Agentic Framework for Reflective PowerPoint Generation

131. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,115
   A Model Context Protocol server for Excel file manipulation

132. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,092
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

133. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,086
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

134. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,082
   Learn AI and LLMs from scratch using free resources

135. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,061
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

136. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,053
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

137. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 3,050
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

138. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,044
   Allow LLMs to control a browser with Browserbase and Stagehand

139. **[boost](https://github.com/laravel/boost)** - ⭐ 3,038
   Laravel-focused MCP server for augmenting your AI powered local development experience.

140. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,026
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

141. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 3,002
   Master Claude Code with this Guide! Includes: Setup, SKILL.md files, Agents, Commands, workflows and tricks making Claude's potential skyrocket!

142. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,953
   n8n custom node for MCP

143. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,946
   AI agent microservice

144. **[mcp](https://github.com/google/mcp)** - ⭐ 2,918
   Google 💚 MCP

145. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 2,877
   RikkaHub is an Android APP that supports for multiple LLM providers.

146. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,873
   A TypeScript framework for building MCP servers.

147. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,823
   The official Rust SDK for the Model Context Protocol

148. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,762
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

149. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,692
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

150. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,593
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

151. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

152. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,530
   A CLI tool for building Go applications.

153. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 2,420
   UltraRAG v2: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

154. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,420
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

155. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,379
   Connect Supabase to your AI assistants

156. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,360
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

157. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,346
   A Model Context Protocol server for converting almost anything to Markdown

158. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,346
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

159. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,233
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code

160. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,206
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

161. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,159
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

162. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,152
   A bridge between Streamable HTTP and stdio MCP transports

163. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,130

164. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,108
   MCP server for Grafana

165. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

166. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,072
   DDGS | Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services

167. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,064
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

168. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,037
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi, GLM, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

169. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,034
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

170. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,031
   A Model Context Protocol server for searching and analyzing arXiv papers

171. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,009
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

172. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 2,005
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

173. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 1,997
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

174. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 1,995
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

175. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,970
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

176. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 1,966
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

177. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,956
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

178. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,955
   directory for Awesome MCP Servers

179. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 1,895
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

180. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 1,891
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

181. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 1,887
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

182. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,881
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

183. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,876
   The official MCP server implementation for the Perplexity API Platform

184. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,832
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

185. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,820
   Witsy: desktop AI assistant / universal MCP client

186. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,811
   A secure low code honeypot framework, leveraging AI for System Virtualization.

187. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,811

188. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,809
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

189. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,804
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

190. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,785
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

191. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,751
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

192. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,710
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

193. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,702
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

194. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 1,696
   The better playwright MCP: works as a browser extension. No context bloat. More capable.

195. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,690
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

196. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,677
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

197. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 1,659
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

198. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,653
   Interactive User Feedback MCP

199. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,639
   Desktop Extensions: One-click local MCP server installation in desktop apps

200. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,616
   Make RSS 📰 great again with AI 🧠✨!!

201. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,595
   Coding assistant MCP for Claude Desktop

202. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,586
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

203. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

204. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,567
   ⭐ All-in-one AI Companion! AI Desktop Girlfriend + AI Virtual Streamer + AI Social App Bot + AI Browser + AI Smart Home + AI Gaming — and every feature you can imagine!⭐全能型AI伴侣！AI桌面女友 + AI虚拟主播 + AI社交APP机器人 + AI浏览器 + AI智能家居 + AI游戏 等你能想到的一切功能！

205. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,566
   Local inspector for ChatGPT apps & MCP apps (ext-apps)

206. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,555
   Next Generation Agentic Proxy for AI Agents and MCP servers

207. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,547
   A Unified MCP Server Management App (MCP Manager).

208. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,542
   MCP server that provides tools and resources for interacting with n8n API

209. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,540
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

210. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,520
   ToolHive makes deploying MCP servers easy, secure and fun

211. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,519
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

212. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,513
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

213. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,493
   An MCP server that installs other MCP servers for you

214. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,444
   Standards for building agents, better

215. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,439
   MCP server for interacting with the iOS simulator

216. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,439
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

217. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,437
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

218. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,437
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

219. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,420
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

220. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,404
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

221. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,400
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

222. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,398
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

223. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,390
   Constrain, log and scan your MCP connections for security vulnerabilities.

224. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,389
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

225. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,379
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

226. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,374
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

227. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,363
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

228. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,316
   The Simple Agent Development Kit.

229. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,300
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

230. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,279
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

231. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,275
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

232. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,274
   Make your own story. User-friendly software for LLM roleplaying

233. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,274
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

234. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,271
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

235. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,269
   A connector for Claude Desktop to read and search an Obsidian vault.

236. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,257
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

237. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,257
   MCP Server for kubernetes management commands

238. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,256
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

239. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,240
   Damn Vulnerable MCP Server

240. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,235
   An MCP server that autonomously evaluates web applications. 

241. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

242. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

243. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,214
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

244. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,213
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

245. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,212
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

246. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,212
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

247. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,208

248. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,200
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

249. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,200
   The Grafbase GraphQL Federation Gateway

250. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 1,195
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

251. **[ai](https://github.com/stripe/ai)** - ⭐ 1,192
   One-stop shop for building AI-powered products and businesses with Stripe.

252. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,179
   The TypeScript MCP framework

253. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,175
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

254. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,175
   The official Swift SDK for Model Context Protocol servers and clients.

255. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,169
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

256. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,163
   The AI toolkit for the AI developer

257. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,163
   An official Qdrant Model Context Protocol (MCP) server implementation

258. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,152
   告别AI提前终止烦恼，助力AI更加持久

259. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,151
   docker mcp CLI plugin / MCP Gateway

260. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,145
   The official ElevenLabs MCP server

261. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,142
   Stop re-explaining your project to AI every session. Automatic context memory for Claude, VS Code, Cursor, and 13+ AI tools.

262. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,141
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

263. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,129
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

264. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,118
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

265. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,117
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

266. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,117
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server

267. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,116
   A Ruby Implementation of the Model Context Protocol

268. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 1,099
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

269. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 1,098
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

270. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,095
   The most powerful MCP Slack Server with no permission requirements, Apps support, multiple transports Stdio and SSE, DMs, Group DMs and smart history fetch logic.

271. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,094
   Build, evaluate and train General Multi-Agent Assistance with ease

272. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,085
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

273. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,084

274. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,073
   Production ready MCP server with real-time search, extract, map & crawl.

275. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,070
   A web UI for Claude Code agents

276. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,064
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

277. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,059
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

278. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,058
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

279. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,058
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

280. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,052
   Plugin for JADX to integrate MCP server

281. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,036
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

282. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,028
   Query and Summarize your chat messages.

283. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

284. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,023
   On-premises conversational RAG with configurable containers

285. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,020
   MCP Python Tutorial 

286. **[use-mcp](https://github.com/modelcontextprotocol/use-mcp)** - ⭐ 1,020

287. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,010
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

288. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 997
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

289. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 995
   Claude Code as one-shot MCP server to have an agent in your agent.

290. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 987
   The Context Graph Factory for AI. Build, manage, and deploy AI-optimized Context Graphs.

291. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 985
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

292. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 981
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

293. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 979
   Remote MCP Servers

294. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 977
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

295. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 974
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

296. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 959
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

297. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 957
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

298. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 955
   A curated list of Model Context Protocol (MCP) servers 

299. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 954
   Hundreds of Claude Code plugins with embedded AI skills. Learn via interactive Jupyter tutorials.

300. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 953
   Bringing the power of MCP to the web

301. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 952
   A repository of servers and clients from the Model Context Protocol tutorials

302. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 949
   MCP server for fetch web page content using Playwright headless browser.

303. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 938
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

304. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 937
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

305. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 929
   Connect AI models like Claude & GPT with robots using MCP and ROS.

306. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 926
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

307. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 924
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

308. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 922
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

309. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 919
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

310. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 918
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

311. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 914
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

312. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 912
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

313. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

314. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 907
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

315. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 905
   Model Context Protocol for WinDBG

316. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 904
   Expose llms-txt to IDEs for development

317. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 893
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

318. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 891
   A framework for writing MCP (Model Context Protocol) servers in Typescript

319. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 891
   A middleware to provide an openAI compatible endpoint that can call MCP tools

320. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 890
   MCP server helping models to understand your Vite/Nuxt app better.

321. **[tools](https://github.com/strands-agents/tools)** - ⭐ 888
   A set of tools that gives agents powerful capabilities.

322. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 888
   First gitlab mcp for you

323. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 884
   MCP integration for Google Calendar to manage events.

324. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 880
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

325. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 879
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

326. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 871
   Allow AI to wade through complex OpenAPIs using Simple Language

327. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 871
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

328. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 870
   A security scanner for your LLM agentic workflows

329. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 870
   Neo4j Labs Model Context Protocol servers

330. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 869
   A library for communication with a Minecraft client/server.

331. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 867

332. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 867

333. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 861
   ChatGPT CLI is a versatile tool for interacting with LLMs through OpenAI, Azure, and other popular providers like Perplexity AI and Llama. It supports prompt files, history tracking, and live data injection via MCP (Model Context Protocol), making it ideal for both casual users and developers seeking a powerful, customizable GPT experience.

334. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 857
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

335. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 855
   A concise list for mcp servers

336. **[agents](https://github.com/inkeep/agents)** - ⭐ 851
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

337. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 851
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

338. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 844

339. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 843
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

340. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 839
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

341. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 837
   APIM ❤️ AI - This repo contains experiments on Azure API Management's AI capabilities, integrating with Azure OpenAI, AI Foundry, and much more 🚀 . New workshop experience at https://aka.ms/ai-gateway/workshop

342. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

343. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

344. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

345. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 827
   A minimalistic MCP client with a good feature set.

346. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 824
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

347. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 817

348. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 815
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

349. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 815
   Simple, modular, and observable Go framework for backend applications.

350. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 812
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

351. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 811
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

352. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

353. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 808
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

354. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 807
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

355. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 802
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

356. **[server](https://github.com/php-mcp/server)** - ⭐ 800
   Core PHP implementation for the Model Context Protocol (MCP) server

357. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 800
   OpenAPI Tool Servers

358. **[context-space](https://github.com/context-space/context-space)** - ⭐ 799
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

359. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 795
   Browse the web, directly from Cursor etc.

360. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 795
   Self-hosted MCP Gateway and Registry for AI agents

361. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 789
   The best way to create, deploy, and share MCP Servers

362. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 787
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

363. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 776
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

364. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 775
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

365. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 767
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

366. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 766
   一个将ACE(Augment Context Engine) 做成MCP的项目

367. **[Context](https://github.com/indragiek/Context)** - ⭐ 762
   Native macOS client for Model Context Protocol (MCP)

368. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 762
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

369. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 759
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

370. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 757
   Vibetest MCP - automated QA testing using Browser-Use agents

371. **[vllora](https://github.com/vllora/vllora)** - ⭐ 756
   Debug your AI agents

372. **[runno](https://github.com/taybenlor/runno)** - ⭐ 755
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

373. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 753
   Chat with your Kubernetes Cluster using AI tools and IDEs like Claude and Cursor!

374. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 753
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

375. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 748
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

376. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 748
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

377. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 743
   Scan MCP servers for potential threats & security findings.

378. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 740
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

379. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 738
   LLDB MCP Integration + other helpful commands

380. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 736
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

381. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 731
   An MCP server for interacting with the Financial Datasets stock market API.

382. **[wordpress-mcp](https://github.com/Automattic/wordpress-mcp)** - ⭐ 724
   WordPress MCP — This repository will be deprecated as stable releases of mcp-adapter become available. Please use https://github.com/WordPress/mcp-adapter for ongoing development and support.

383. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 721
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

384. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 717
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

385. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 714
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

386. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 709
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

387. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 709
   A secure local sandbox to run LLM-generated code using Apple containers

388. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 709
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and perform job searches.

389. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 708
   All in one vscode plugin for mcp developer

390. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 705
   A MCP server implementation for hyperbrowser

391. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 704
   Build MCP Agents

392. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 699
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

393. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 696
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

394. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 694
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

395. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 693
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

396. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 689
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

397. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 685
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

398. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 681
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

399. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 679
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

400. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 679
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

401. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 678
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

402. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 674
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

403. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 671
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

404. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 671
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

405. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 669
   A flexible HTTP fetching Model Context Protocol server.

406. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 666
   MCP server for Docker

407. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 662
   Clojure MCP

408. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 659
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

409. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 658
   A simple CLI to run LLM prompt and implement MCP client.

410. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

411. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 655
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

412. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 647
   Connect ClickHouse to your AI assistants.

413. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 646
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

414. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

415. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 641
   Laravel API for Ai Agents and humans.

416. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 640
   Querying local documents, powered by LLM

417. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 640
   EnrichMCP is a python framework for building data driven MCP servers

418. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 636
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

419. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 635
   An MCP server that provides control over Android devices via adb

420. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 635
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

421. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 634
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

422. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 633
   Shell and coding agent on claude desktop app

423. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 629
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

424. **[mcp](https://github.com/laravel/mcp)** - ⭐ 629
   Rapidly build MCP servers for your Laravel applications.

425. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 626
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

426. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 624
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

427. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 620
   A simple MCP server for Obsidian

428. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 616
   Talk to a Cloudflare Worker from Claude Desktop!

429. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 615
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

430. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 610
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

431. **[samples](https://github.com/strands-agents/samples)** - ⭐ 607
   Agent samples built using the Strands Agents SDK.

432. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 605
   gcloud MCP server

433. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 600
   mem-agent mcp server

434. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 596
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

435. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 596

436. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 592
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

437. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 592
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

438. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 592

439. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 589
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

440. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 588
   Convert Any OpenAPI V3 API to MCP Server

441. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 584
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

442. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 583
   MCP Server For Turkish Legal Databases

443. **[tome](https://github.com/runebookai/tome)** - ⭐ 582
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

444. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 581
   Daydreams is a set of tools for building agents for commerce

445. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 580
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

446. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 574
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

447. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 573
   Dexto is a general-purpose agent harness for building and orchestrating agentic applications.

448. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 572
   VoiceMode MCP brings natural conversations to Claude Code

449. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 571
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

450. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 570
   LangGraph solution template for MCP

451. **[obot](https://github.com/obot-platform/obot)** - ⭐ 562
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

452. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 556
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

453. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 556

454. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 555
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

455. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 554
   MCP to connect your LLM with Spotify.

456. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 553
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

457. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 553

458. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 549
   Draw.io Model Context Protocol (MCP) Server

459. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 548
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

460. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 545
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

461. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 542
   Security scanner for MCP servers

462. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 541
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

463. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 535

464. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 535
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

465. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 534
   The .NET library to build AI agents with 25+ built-in connectors.

466. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 534
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

467. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 534
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

468. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 533
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

469. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 532

470. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 532
   MCP server for interacting with Neon Management API and databases

471. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 531
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

472. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 531

473. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 530
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STEAMABLEHTTP access protocols to deploy MCP。

474. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 527
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

475. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 526
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

476. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 524
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

477. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 523
   An MCP Multimodal AI Agent with eyes and ears!

478. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 523
   提取抖音无水印视频链接，视频文案，douyin-mcp-server

479. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 523
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

480. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 522
   An Mcp client inside Emacs

481. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 521

482. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 519
   A comprehensive collection of Model Context Protocol (MCP) servers

483. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 518
   An MCP server to query any Postgres database in natural language.

484. **[ethora](https://github.com/dappros/ethora)** - ⭐ 518
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

485. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 515
   Open Source Voice Agent Platform

486. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

487. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 515
   A MCP server for Home Assistant

488. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 513
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

489. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 512
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

490. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 512
   MCP server to deploy apps to Cloud Run

491. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 512
   Next.js Development for Coding Agent

492. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 511
   A Model Context Protocol server for IDA

493. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 511
   MCP server for querying Apple Health data with natural language and SQL

494. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 508
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

495. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 508
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

496. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

497. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 507

498. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 504
   微信读书MCP

499. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 501

500. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 501
   A tool that converts OpenAPI specifications to MCP server

501. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 501
   Yes Mcp server in bash

502. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 498
   An MCP server for interacting with Sentry via LLMs.

503. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 495
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

504. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 494
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

505. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

506. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

507. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 491

508. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 489
   MCP Monitoring with eBPF

509. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 489
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

510. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 487
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

511. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 487
   A Model-Context Protocol Server for YouTube

512. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 483
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, and comprehensive lifecycle management capabilities.

513. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 483
   Lighweight CLI to interact with MCP servers

514. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 482
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

515. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 478
   MCP server for document format conversion using pandoc.

516. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 476
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

517. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 474
   MCP to allow AI agents to control Unreal

518. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 473
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

519. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 471
   Aser is a lightweight, self-assembling AI Agent frame.

520. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 470
   MCP Server to interact with Google Gsuite prodcuts

521. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 469
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

522. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 469
   "AnyTool: Universal Tool-Use Layer for AI Agents"

523. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 468
   Install, manage and develop MCP servers

524. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 467
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

525. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 465
   An SDK building Laravel MCP servers

526. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 462
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

527. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 462
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

528. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 462
   MCP server integration for DaVinci Resolve

529. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 461
   LLM + MCP + RAG = Magic

530. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 461
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

531. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

532. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 458
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

533. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 456
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

534. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 454
   A MCP (Model Context Protocol) server for interacting with dbt.

535. **[argo](https://github.com/xark-argo/argo)** - ⭐ 453
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

536. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 451
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

537. **[director](https://github.com/director-run/director)** - ⭐ 451
   MCP Playbooks for AI agents

538. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 446
   FreeCAD MCP(Model Context Protocol) server

539. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

540. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 446
   im busy building ai agents so why not let an ai talk to my girlfriend? 

541. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 445
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

542. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 445
   MCP Server for Turkish & American Stock Exchange and Fund Data

543. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 444
   GitOps on Autopilot Mode

544. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 444
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

545. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 444

546. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 444
   A simple, locally hosted Web Search MCP server for use with Local LLMs

547. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 443
   A docker MCP Server (modelcontextprotocol)

548. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 442
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

549. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 442
   MCP configuration to connect AI agent to a Linux machine.

550. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 441
   Delegate tasks to Codex GPT 5.2 directly from within Claude Code.

551. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 439
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

552. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 435
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

553. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 434
   A structural code search engine for Al agents.

554. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 433
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

555. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 431
   This is the official website for TuriX Computer-use-Agent

556. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 428
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

557. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 425
   Send emails directly from Cursor with this email sending MCP server

558. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 423
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

559. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 422

560. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 422
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

561. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 421
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

562. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 421
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

563. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 420
   Spec-Driven Development MCP Server, not just Vibe Coding

564. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 420
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

565. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 420
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

566. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 420
   MCP Server for Burp

567. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 419
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

568. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 419
   MCP Server for Metasploit

569. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 418
   Make your meetings accessible to AI Agents

570. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 417
   小红书MCP服务 x-s x-t js逆向

571. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 416
   Enterprise-ready MCP gateway, MCP registry & orchestrator

572. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 416
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

573. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 415
   Unlock 650+ MCP servers tools in your favorite agentic framework.

574. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 415
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

575. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 411
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

576. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 411
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

577. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 409
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

578. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 408
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

579. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 406
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

580. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 405
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

581. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 405
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

582. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 403
   A CLI inspector for the Model Context Protocol

583. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 403
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

584. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 401
   基于NET搭建-AI智能体-现代化Saas企业级前后端分离架构-开启智能应用的无限可能：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR验证码识别、API多版本兼容、单元集成测试、RabbitMQ、代码生成器

585. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 401
   The safest way to make REST calls in C# with an MCP Generator

586. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 401
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

587. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 400
   Official Jina AI Remote MCP Server

588. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 398
   MCP server that execute applescript giving you full control of your Mac

589. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 396
   An MCP extension for Ghidra

590. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 396
   Official Docker MCP registry 

591. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 394
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

592. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 393
   An experiment in software planning using MCP

593. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 393
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

594. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 391
   MCP server for DuckDB and MotherDuck

595. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 391
   MCP-NixOS - Model Context Protocol Server for NixOS resources

596. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 391
   BioMCP: Biomedical Model Context Protocol

597. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 390
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

598. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 388
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

599. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 388
   MCP Server for SearXNG

600. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 386
   Memento MCP: A Knowledge Graph Memory System for LLMs

601. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 386
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

602. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 385
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

603. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 385
   A model-driven approach to building AI agents in just a few lines of code. 

604. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 384
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

605. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 383
   lunar.dev: Agent native MCP Gateway for governance and security

606. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 381
   Local Groq Desktop chat app with MCP support

607. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 380
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

608. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 380
   Baidu Map MCP Server

609. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 378
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

610. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 378
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Cognito integration.

611. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 377
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

612. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 377
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

613. **[station](https://github.com/cloudshipai/station)** - ⭐ 376
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

614. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 375
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

615. **[docfork](https://github.com/docfork/docfork)** - ⭐ 374
   Docfork - Up-to-date Docs for AI Agents.

616. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

617. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 372
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

618. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 370
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

619. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 370
   MCP Server for code graph analysis and visualization by CodeGPT

620. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 369
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

621. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 369
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

622. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 369
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

623. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 369
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

624. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 368
   MCP server connecting to Kubernetes

625. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 367
   Model Context Protocol (MCP) Server for Graphlit Platform

626. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 365
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

627. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 365
   Making docling agentic through MCP

628. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 363
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

629. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 362
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

630. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 361
   Model Context Protocol SDK for PHP

631. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 361
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

632. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 360
   A fully functional MCP server and CLI for YouTube

633. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 360
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

634. **[codexia](https://github.com/milisp/codexia)** - ⭐ 360
   A powerfull GUI and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

635. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 359
   Search Airbnb using your AI Agent

636. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 359
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

637. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 359
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

638. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 358
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

639. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 357
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs, OpenRouter, Groq, Dashscope & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

640. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 356
   Professional Development Environment for Claude Code with Endless Mode, Spec-Driven Development, TDD, LSP, Persistent Memory, Semantic Search, Quality Hooks and Modular Rules 🛠️

641. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 355
   飞书/Lark官方 OpenAPI MCP

642. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 354
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的专有领域智能聊天助手

643. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 353
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

644. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 353
   MCP server that provides LLMs with tools for interacting with EVM networks

645. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 353
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

646. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 352
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

647. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 352
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

648. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 351
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

649. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 349
   AI-based stock analysis and trading system

650. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 349
   Model Context Protocol (MCP) implementation in Rust

651. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 348
   MCP server for Todoist integration enabling natural language task management with Claude

652. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 348
   Model Context Protocol server for GraphQL

653. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 348
   MCP Server implementation for Ableton Live OSC control

654. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 348
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

655. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 347
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

656. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 346
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

657. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 346
   A macOS AppleScript MCP server

658. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 345
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

659. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 344
   SonarQube MCP Server

660. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 343
   MCP Server implementation for Xcode integration

661. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 343
   F2C MCP Server

662. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 343
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

663. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 342
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

664. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 342
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

665. **[daan](https://github.com/pluveto/daan)** - ⭐ 342
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

666. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 342
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

667. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 342
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

668. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 342
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

669. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 338
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

670. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 338
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

671. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 338
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  全球首个通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

672. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 337
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

673. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 337
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

674. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 337
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

675. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 336
   Example of an MCP server with custom tools that can be called directly from cursor

676. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 336
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

677. **[devopness](https://github.com/devopness/devopness)** - ⭐ 335
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

678. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 334
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

679. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 334
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

680. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 333
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

681. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 332
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

682. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 332
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

683. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

684. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 331
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

685. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 330
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

686. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 330
   Elixir Model Context Protocol (MCP) SDK

687. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 330
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

688. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 330
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

689. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 329

690. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 328
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

691. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 327
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

692. **[gemini-flow](https://github.com/clduab11/gemini-flow)** - ⭐ 327
   rUv's Claude-Flow, translated to the new Gemini CLI; transforming it into an autonomous AI development team.

693. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 326
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models. v0.2.8

694. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 326
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

695. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 326

696. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 325
   Control your Android devices with AI using Model Context Protocol

697. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 325
   An MCP implementation for Selenium WebDriver

698. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 324
   AI-Powered Revit Modeling

699. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 323

700. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 323
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

701. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 323
   A Production-Ready Runtime Framework for Agent Deployment and Tool Sandbox

702. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

703. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 322
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

704. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 322
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

705. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 322
   An MCP server for loading skills (shim for non-claude clients).

706. **[moling](https://github.com/gojue/moling)** - ⭐ 321
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

707. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 321
   Xiaozhi MCP sample program

708. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 321
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

709. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 317
   This is a Minecraft Base Client

710. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 317
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

711. **[emcee](https://github.com/mattt/emcee)** - ⭐ 316
   MCP generator for OpenAPIs 🫳🎤💥

712. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 315
   An MCP server for Azure DevOps

713. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 314
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

714. **[mcp](https://github.com/IBM/mcp)** - ⭐ 314
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

715. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 313
   Repo of skills for autogen studio using model context protocol (mcp)

716. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 313
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

717. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 312
   MCP server to expose VS Code editing features to an LLM for AI coding

718. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 310
   deep, reliable and confidential coding-context

719. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 310
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

720. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 309
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

721. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 307
   Lightweight MCP Server for interacting with Android Operating System.

722. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 306
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

723. **[mesh](https://github.com/decocms/mesh)** - ⭐ 305
   One secure endpoint for every MCP server. Deploy anywhere.

724. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 305
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

725. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 304
   A working pattern for SSE-based MCP clients and servers

726. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 303
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

727. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 302
   api router for MCP Servers

728. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 302
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

729. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 301
   Turn any openapi file into an mcp server, with just the tools you need.

730. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

731. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 301
   Mapbox Model Context Protocol (MCP) server

732. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 300
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

733. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 300
   MaverickMCP - Personal Stock Analysis MCP Server

734. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 298
   An implementation of Model Context Protocol (MCP) server for Argo CD.

735. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 297

736. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 297

737. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 296
   A Model Context Protocol server for building an investor agent

738. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 296
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

739. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 296
   MCP implementation of Claude Code capabilities and more

740. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 296
   OpenSkills: Run Claude Skills Locally using any LLM

741. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 293
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

742. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 293
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

743. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 292
   Agentic RAG for any scenario. Customize sources, depth, and width

744. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 292
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

745. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 289
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

746. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 289
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

747. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 289
   Model Context Protocol server for DeepSeek's advanced language models

748. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 288
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

749. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 288
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

750. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 287
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

751. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 287

752. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 287
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

753. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 286
   Minimal MCP Server for Aider

754. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 285
   MCP server for OpenAI o3 web search

755. **[generator](https://github.com/context-hub/generator)** - ⭐ 284
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

756. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 284
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

757. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 283

758. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

759. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 283
   hydra-ai

760. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 283

761. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 283
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

762. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 282
   Discover Exceptional MCP Servers

763. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 282
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

764. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

765. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 281
   The specification for the Universal Tool Calling Protocol

766. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 281
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

767. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 281
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

768. **[consult7](https://github.com/szeider/consult7)** - ⭐ 280
   MCP server to consult a language model with large context size

769. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 280
   First AI‑enabled open-source Human Capital Management system that you can start using today.

770. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 280
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

771. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 278
   simple web ui to manage mcp (model context protocol) servers in the claude app

772. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 278
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

773. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 277
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

774. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 277
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

775. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 277
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

776. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 276
   MCP integration platforms making AI-Agents developers focusing on their own tasks

777. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 276
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

778. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 276
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

779. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 275
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

780. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 274
   Model Context Protocol (MCP) Server for dify workflows

781. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 274
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

782. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 274
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

783. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 274
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

784. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 274
   MCP server for browser automation using Playwright

785. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 274
   MCP server retrieving transcripts of YouTube videos

786. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 273
   A Model Context Protocol Server for MongoDB

787. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 272
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

788. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 272
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

789. **[mq](https://github.com/harehare/mq)** - ⭐ 271
   jq-like command-line tool for markdown processing

790. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 271

791. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

792. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 270
   MCP server for Windows OS automation

793. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

794. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 268
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

795. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 268
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

796. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 268
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

797. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 267
   An MCP server providing tools for image processing operations

798. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 267
   Obsidian MCP (Model Context Protocol) Server

799. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 267
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

800. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 267
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

801. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 266
   Source code of minecraft 1.12

802. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 266

803. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 264
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

804. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 264
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

805. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 263
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

806. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 263
   MCP server for JADX-AI Plugin

807. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 262
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

808. **[app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server)** - ⭐ 261

809. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 260
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

810. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 260
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

811. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 260
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

812. **[mcp](https://github.com/oracle/mcp)** - ⭐ 260
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

813. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 260
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

814. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 260
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

815. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 259
   MCP server for searching and retrieving Claude Agent Skills using vector search

816. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 258
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

817. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 258
   Home Assistant MCP Server

818. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 258
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

819. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 257
   BrowserWing turns your browser actions into MCP commands, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

820. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 256
   MCP Server for Odoo

821. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 255
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

822. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

823. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 253
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

824. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 253
   Model Context Protocol server implementation for Reddit

825. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 252
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

826. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 252
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

827. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 251
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

828. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 251
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

829. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 251
   Java AI（智能体） 全场景应用开发框架（LLM，Function Call，RAG，Embedding，Reranking，Flow，MCP Server，Mcp Client，Mcp Proxy）。同时兼容 java8 ~ java25。也可嵌入到 SpringBoot2、jFinal、Vert.x 等框架中使用。。支持 MCP_2025_06_18（mcp streamable）

830. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 250
   MCP server(s) for Aipolabs ACI.dev

831. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 250
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

832. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 250
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

833. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 250
   Context-Engine: MCP retrieval stack for AI coding assistants. Hybrid code search (dense + lexical + reranker), ReFRAG micro-chunking, local LLM prompt enhancement, and dual SSE/RMCP endpoints. One command deploys Qdrant-powered indexing for Cursor, Windsurf, Roo, Cline, Codex, and any MCP client.

834. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 249
   Apollo MCP Server

835. **[api200](https://github.com/API-200/api200)** - ⭐ 248
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

836. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 248
   A code reasoning MCP server, a fork of sequential-thinking

837. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 246
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

838. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 246
   Apache Doris MCP Server

839. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 245
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

840. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 244
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

841. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 244
   MCP server implementation for Google's Gemini API

842. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 242
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

843. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 242
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

844. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 242
   MCP Server for interacting with Salesforce instances

845. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 241
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

846. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

847. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 241
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

848. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 241
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

849. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 241
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

850. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 241
   MCP Server for Tree-sitter

851. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 240
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

852. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 240
   An MCP server for Massive.com Financial Market Data

853. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

854. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 238
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

855. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 238

856. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 238
   Simplified Gemini for Claude Code. 

857. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 237
   Standardized environment infrastructure for Agentic AI development.

858. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 237
   MCP Interface for Video Jungle

859. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 237
   小智AI客户端，目前主要用于MCP的对接

860. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 236
   MCP server for Bazi (八字) information

861. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 236
   Easy guide to installing Claude Code MCPs globally on your machine.

862. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 236
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

863. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

864. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 235
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

865. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 235
   The evaluation benchmark on MCP servers

866. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 234
   Turn any MCP server into a Python module

867. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 234

868. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 234
   Code Runner MCP Server

869. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 234
   🔥 Model Context Protocol (MCP) server for Firebase.

870. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 233
   Creates a simple MCP tool server with "streaming" HTTP.

871. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 233
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

872. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 233
   The Unofficial and Awesome Home Assistant MCP Server

873. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 233
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

874. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 231
   SpringAI，LLM，MCP，Embedding

875. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 230
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

876. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 230
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

877. **[dat](https://github.com/hexinfo/dat)** - ⭐ 229
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

878. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 229
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

879. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 228
   A Model Context Protocol (MCP) server that enables natural language queries to databases

880. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 228
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

881. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 228
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

882. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

883. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 227
   An experimental MCP Server for foundry built for Solidity devs

884. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 227
   MCP Server for Telegram

885. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 227
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

886. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 226
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

887. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 226
   A collection of MCP servers

888. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 226
   Standalone Roblox Studio MCP Server

889. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 225
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

890. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 225
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

891. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 223
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

892. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 223
   Semantic code searcher and codebase utility with AI memory onboard

893. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 221
   AWS MCP Proxy Server

894. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 221
   Volcengine MCP Servers

895. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 221
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

896. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 221
   Lean Theorem Prover MCP

897. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 220
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

898. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 220

899. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 220
   Model Context Protocol server to run commands

900. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

901. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 219
   A TypeScript SSE proxy for MCP servers that use stdio transport.

902. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 219
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

903. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 218

904. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 218
   A Model Context Protocol (MCP) server for interacting with Twitter.

905. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 218
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

906. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

907. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 217
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

908. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 217
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

909. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 217
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

910. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 217

911. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 216
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

912. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 216
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

913. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 216
   CAD MCP Server

914. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 216
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

915. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 216
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

916. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 215
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

917. **[tentix](https://github.com/labring/tentix)** - ⭐ 214
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

918. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 214
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

919. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 214
   MCP server for Claude to access Outlook data via Microsoft Graph API

920. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 214
   Lightweight MCP server for Spotify

921. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 213
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

922. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

923. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 213
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

924. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 213
   Playwright MCP fork that works with Cloudflare Browser Rendering

925. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 212
   Agent MCP for ffmpeg

926. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 212
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

927. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 212
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

928. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 212
   Things.app MCP Server

929. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 212
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

930. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 211
   A ReAct-Based Highly Robust Autonomous Agent Framework.

931. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 211
   Razorpay's Official MCP Server

932. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 211

933. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 211
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

934. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 211
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

935. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 210
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

936. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 210
   ModelContextProtocol for Figma's REST API

937. **[lokka](https://github.com/merill/lokka)** - ⭐ 210
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

938. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 210
   Model Context Protocol Servers for Milvus

939. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 210
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

940. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 209
   Lightweight C++ MCP (Model Context Protocol) SDK

941. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 209
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

942. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 209

943. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 209
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

944. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 208
   Penpot MCP server

945. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 208
   A Multi-modal MCP client for voice powered agentic workflows

946. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 208
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

947. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 208
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

948. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 208

949. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 207
   mindmap, mcp server, artifact

950. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 207
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

951. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 207
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

952. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 207
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to make direct edits and formatting.

953. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

954. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 206
   Zerodha Kite MCP server

955. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 206
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

956. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

957. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

958. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 205
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

959. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 204
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

960. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 204
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

961. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 204
   interactive programming of melodies, producing MIDI 

962. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 204
   An MCP server to use Sora video generation APIs

963. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 204
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

964. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 204
   Universal command-line client for MCP. Supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for scripting and code mode, proxy for AI sandboxes, and more.

965. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 203
   Model Context Protocol tool support for LangChain

966. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 203
   MCP server for Anki via AnkiConnect

967. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 203
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

968. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 202
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

969. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 202

970. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 201
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

971. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 201
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

972. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

973. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 200
   A Tiny Terminal Chat App for AI Models with MCP Client Support

974. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 200
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

975. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 199
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

976. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 199
   Run and monitor MCP servers locally

977. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 199
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

978. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 198
   🤖 An MCP server for surfacing useful Claude Code conversation history

979. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 198
   🔎 A MCP server for Unsplash image search.

980. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 198
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

981. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 198

982. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 198
   Pure Rust implementation of MCP server for headless terminal 

983. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 198
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

984. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 198
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

985. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 198
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

986. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 197
   A MCP Server for the RAG Web Browser Actor

987. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 197
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

988. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

989. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 196
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

990. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

991. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 196
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

992. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

993. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 195
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

994. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 195
   R MCP Server

995. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 195
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

996. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 195
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

997. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 194
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

998. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 194
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

999. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 194
   Homeassistant MCP server for 小智AI

1000. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 193
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1001. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 193
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1002. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 193
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1003. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 193
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

1004. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 192
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1005. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 192
   A SEC EDGAR MCP (Model Context Protocol) Server

1006. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 192
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1007. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 191
   Absurdly easy Model Context Protocol Servers in Typescript

1008. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 191
   Manage / Proxy / Secure your MCP Servers

1009. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 191
   A MCP server for our beloved terminal multiplexer tmux.

1010. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 191
   Self-hosted AI RAG + MCP Platform

1011. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1012. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 190

1013. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 190
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1014. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 190
   Platform to create, curate and host MCP servers ⚒️ Build production quality tools for your agents.

1015. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 189
   MCP server for Dynatrace Observability

1016. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 189
   这是一个专为开发企业级MCP server而设计的通用开发框架

1017. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 189
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1018. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 187
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1019. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1020. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1021. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1022. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 187
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1023. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 187
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1024. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1025. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 186
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1026. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 186
   Supabase MCP server created in Python.

1027. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 186
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

1028. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 185
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1029. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 185
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1030. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 185
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1031. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 185
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1032. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1033. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 184
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1034. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 184

1035. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 183
   A TypeScript framework for building MCP servers elegantly

1036. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 183
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1037. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1038. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1039. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 182
   The Power BI Desktop MCP Server is a tool that lets AI assistants like Claude interact with your Power BI models programmatically. It enables Claude to read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1040. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 182
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1041. **[siconos](https://github.com/siconos/siconos)** - ⭐ 181
   Simulation framework for nonsmooth dynamical systems

1042. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 181
   Hugging Face MCP Server

1043. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 181
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1044. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 180
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1045. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 180

1046. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 180
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1047. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 180
   MCP Server for ServiceNow

1048. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 180
   Google Search Console Insights with Claude AI for SEOs

1049. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 179
   Model Context Protocol Servers in Quarkus

1050. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 179
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1051. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1052. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1053. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 178
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1054. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 178
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

1055. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 178
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1056. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1057. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 177
   An MCP server for Anki

1058. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 177
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1059. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 176
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

1060. **[mcp-run-python](https://github.com/pydantic/mcp-run-python)** - ⭐ 175
   MCP server to run Python code in a sandbox.

1061. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 174
   This extension enables developers to implement the MCP server features easily.

1062. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 174
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1063. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1064. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 174
   MCP Server for the Bilibili API, supporting various operations.

1065. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 173
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1066. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 171
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1067. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 171

1068. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 171
   MCP for calling Siri Shorcuts from LLMs

1069. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 171
   pctx is the execution layer for agentic tool calls. It exposes custom tools and MCP servers as code that runs in secure sandboxes for token-efficient calls.

1070. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 171
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1071. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 171
   A self-hosted web UI that simplifies AI experimentation and testing for Java developers. It provides playgrounds for all major vector databases and MCP tools, supports intuitive interaction with LLMs, and enables rapid development and testing of RAG workflows, MCP integrations, and unified chat experiences.

1072. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 170
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1073. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 170
   Examples of using Pipedream's MCP server in your app or AI agent.

1074. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 170
   MCP stdio server for frida

1075. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 170
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1076. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 170
   A list of open-source AI projects you can use to generate income easily.

1077. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 170
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1078. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 170
   Built-in MCP client–powered document/news management tool with daily auto summaries, document interaction, user-defined notifications (email, apns, etc.), and customizable model support.内置 MCP 客户端的文档/资讯管理工具，支持每日自动总结、文档交互、自定义通知（邮箱、APNS等）以及模型自定义。

1079. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 169
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1080. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 168
   A MCP server to search for accurate academic articles.

1081. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 168
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1082. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 168
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1083. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 168
   Turn any website or doc into an MCP server

1084. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 168
   MCP server for TouchDesigner

1085. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 168
   A Tiny Web Chat App for AI Models with MCP Client Support

1086. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 167
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1087. **[command](https://github.com/scopecraft/command)** - ⭐ 167
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1088. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 166
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1089. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 166
   Discord MCP Server for Claude Integration

1090. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 165
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1091. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 165
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1092. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 165
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1093. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 164
   A desktop application that adds powerful tools to Claude and AI platforms

1094. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 164
   One MCP Server, All Your Apps, Privacy First

1095. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 164
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1096. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 164
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1097. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 164
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1098. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 163
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1099. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 162
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1100. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 162
   MCP (Model Context Protocol) server for Weaviate

1101. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 162
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1102. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 162
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1103. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 162
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1104. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 162
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1105. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 161
   MCP server to work with Telegram through MTProto

1106. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 161
   MCP Server for Wazuh SIEM

1107. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 160
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1108. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 160
   c4 GenAI Suite

1109. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 160
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1110. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 160
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1111. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 159
   Official Magic UI MCP server.

1112. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 159
   Command line interface for MCP clients with secure execution and customizable security policies

1113. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 159
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1114. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 159
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1115. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 159
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1116. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 159
   Turn a web server into an MCP server in one click without making any code changes.

1117. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1118. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 158
   Sketchup Model Context Protocol

1119. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 158
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1120. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 158
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1121. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 157
   An MCP server for fetching URLs / Youtube video transcript.

1122. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 157
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1123. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 157
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1124. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 157
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1125. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 157
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1126. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 156
   A simple CLI to install MCP servers into any client - auth included!

1127. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 156
   ToolSDK.ai's Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1128. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 156

1129. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 156
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1130. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 155
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1131. **[Companion](https://github.com/mattt/Companion)** - ⭐ 155
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1132. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 155
   Your own Claude Code UI, local sandbox, in-browser VS Code, terminal, multi-provider support (Max, Z.AI, OpenRouter), custom skills, and MCP servers.

1133. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 154
   Learn how to use MCP Servers with GitHub Copilot

1134. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 154
   Simple Slackbot MCP Client

1135. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 154
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1136. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 154
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1137. **[recall](https://github.com/joseairosa/recall)** - ⭐ 154
   Give Claude perfect recall - Redis-powered persistent memory for LLMs

1138. **[docs](https://github.com/strands-agents/docs)** - ⭐ 154
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1139. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 154
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1140. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 153
   An MCP server to search for flights.

1141. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 153
   A list of MCP (Model Context Protocol) servers for developer tools and services

1142. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 152
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1143. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 152
   MCP Salesforce connector

1144. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 152
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1145. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 152
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1146. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 152
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1147. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 152
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1148. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 152
   MCP Server for AI Summarization

1149. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 151
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1150. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 151

1151. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 151
   Deep Research for crypto - free & fully local

1152. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 151
   MCP Server for Postgres

1153. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 150
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1154. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 150
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1155. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 150
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1156. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1157. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 149
   Desktop APP for Discover and Install MCP Servers

1158. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 149
   Typescript SDK to build MCP servers in an agnostic way

1159. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 149
   MCP server for searching and querying PubMed medical papers/research database

1160. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 149
   Instagram Direct messages MCP

1161. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 149
   Fast-track AI innovation with a centralized, trusted, curated registry

1162. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 148
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1163. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 148
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1164. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 148
   A simple MCP server to search for documentation (tutorial)

1165. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 148
   A gateway demo for MCP SSE Server

1166. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 148
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1167. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 148
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1168. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 147
   Model Context Protocol For R

1169. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 147
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1170. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 147
   Model Context Protocol (MCP) server for constraint optimization and solving"

1171. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 147
   Make MCP Server

1172. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 146
   MCP server implementation for Google's Gemini API

1173. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 146
   MCP Server for using any LLM as a Tool

1174. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 146
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1175. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 146
   ChatGPT Copilot Extension for Visual Studio Code

1176. **[relay](https://github.com/prism-php/relay)** - ⭐ 145
   An MCP client tool for Prism

1177. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 145

1178. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 145
   Model Context Protocol server implementation for Figma API

1179. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 145
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1180. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 145
   An MCP server that provides access to Postman.

1181. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 145
   Scrapeless Mcp Server

1182. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 145
   Neo4j official MCP Server

1183. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 145
   Connect your AI to your APIs on Postman

1184. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 145
   Appium MCP on Steroids!

1185. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 144
   MCP server to download entire websites

1186. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 144
   Connect any Open Data to any LLM with Model Context Protocol.

1187. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 144
   Goku is an HTTP load testing application written in Rust 

1188. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 144
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1189. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 144
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1190. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 144
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1191. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 144
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1192. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 143
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1193. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 143
   Persistent AI memory for coding assistants - MCP server providing context persistence across sessions for Claude, Cursor, Windsurf.  MCP Tools for task tracking, workflow automation, and AI memory. Eliminates context loss between sessions.

1194. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 143
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1195. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 143
   🚀🎬 Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1196. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 142
   A PubMed MCP server.

1197. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 142

1198. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1199. **[kom](https://github.com/weibaohui/kom)** - ⭐ 141
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1200. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 141
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1201. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 141
   Persistent Intelligence Infrastructure for AI Agents

1202. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 141
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1203. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 141
   A Model Context Protocol server for MySQL database operations

1204. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 141
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1205. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 141
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1206. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 141
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1207. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 140
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1208. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 140
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1209. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 140
   A MCP Server for creating Powerpoint Presentations

1210. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 140
   Dynamically expose tools from proxied servers based on an Agent Persona

1211. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 140
   Quickstart, build, test, and ship your ChatGPT App locally with the sunpeak ChatGPT App framework.

1212. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 139
   Simple MCP Server Implementation

1213. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 139
   MCP server for discord bot

1214. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 139
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1215. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 139
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1216. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 139
   A Model Context Protocol server for calculating.

1217. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 139
   MCP Server for Google Slides

1218. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 138
   MCP server for Israel Government Data

1219. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 138
   Catch MCP server issues before your agents do.

1220. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 138
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1221. **[eion](https://github.com/eiondb/eion)** - ⭐ 138
   Shared Memory Storage for Multi-Agent Systems

1222. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 138
   StarRocks MCP (Model Context Protocol) Server

1223. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 137
   MSSQL Server MCP implementation written in C#

1224. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 137
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1225. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 137
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1226. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 136
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1227. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 136
   MCP server for seamless document format conversion and processing

1228. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 136
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1229. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 136
   MCP server for AutoCAD LT: AI agents translate natural language into AutoLISP code for geometry, 600+ ISA 5.1 P&ID symbols, block attributes, and layer management—generating technical drawings with 80% performance improvement via batch operations.

1230. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 136
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1231. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 135
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1232. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 135
   MCP server to access Garmin data

1233. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 135
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1234. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1235. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 134
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1236. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 134
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1237. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 134
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1238. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 134
   A local Apple Documentation crawler and MCP server. Written in Swift.

1239. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 134
   A guide on how to use the Figma MCP server

1240. **[refref](https://github.com/refrefhq/refref)** - ⭐ 134
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1241. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1242. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 133
   Serper MCP Server supporting search and webpage scraping

1243. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 133
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1244. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 133
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1245. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 133
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1246. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 133
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1247. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 133
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1248. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 133

1249. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 133
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1250. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 133
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1251. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 133
   An MCP server implementing the think tool for Claude

1252. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 133
   DataForSEO API modelcontextprotocol server 

1253. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 133
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1254. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 132
   mcp server for gitingest

1255. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 132
   Graphiti MCP Server

1256. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 132
   IMAP and SMTP via MCP Server

1257. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 132
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1258. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 131
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1259. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 131
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1260. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 131
   The Logfire MCP Server is here! :tada:

1261. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 131
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1262. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 131
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1263. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 131
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1264. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 130
   Manage Your Kubernetes Cluster with k8s mcp-server

1265. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 130
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1266. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 130
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1267. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 130
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1268. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 130
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1269. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 129
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1270. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 129
   Chat application with multi-agents system supports multi-models and MCP

1271. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 129
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1272. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 129
   A collection of crypto MCP servers.

1273. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 128
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

1274. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 128
   Model Context Protocol (MCP) server for the Zotero API, in Python

1275. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 128
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1276. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 128
   MCP server for understanding AWS spend

1277. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 128
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1278. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1279. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 128
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1280. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 128
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1281. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 128
   Open Source AI platform to build Agentic services, ChatGPT Apps and MCP Servers

1282. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 128
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1283. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 127

1284. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1285. **[magg](https://github.com/sitbon/magg)** - ⭐ 127
   Magg: The MCP Aggregator

1286. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 127
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1287. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 126
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1288. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 126
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1289. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 126

1290. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1291. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 126

1292. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 126
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1293. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 126
   Intelligent spec workflow management MCP server

1294. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 126
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1295. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 126
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1296. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 125
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1297. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1298. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 125
   Dart AI Model Context Protocol (MCP) server

1299. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 125
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1300. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 125
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1301. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 125
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1302. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1303. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 124
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1304. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 124
   High-performance CCXT MCP server for cryptocurrency exchange integration

1305. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 124
   Buttplug.io Model Context Protocol (MCP) Server

1306. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 124
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1307. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 124
   Penpot's official MCP Server

1308. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 123
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1309. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 123
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1310. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 123
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1311. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 123
   An MCP Server for Ollama

1312. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 123
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1313. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 122
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1314. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 122
   a private MCP server for accessing Linear

1315. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 122
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1316. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 122
   It's time to push beyond MCP Servers... Right?

1317. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 122
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1318. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 122
   🐉 The fast, PHP way to build MCP servers

1319. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 122
   MCP stdio server for radare2

1320. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 122
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1321. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1322. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 121
   MCP server for Unreal Engine 5

1323. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 121
   Model Context Protocol (MCP) with TikTok integration

1324. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 121
   MCP Server for Searching Turkish Legislation

1325. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 121
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1326. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 121
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1327. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 121
   A Model Context Protocol server that provides access to BigQuery

1328. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 121
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1329. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 120
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1330. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 120
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1331. **[openapi](https://github.com/samchon/openapi)** - ⭐ 120
   OpenAPI definitions, converters and LLM function calling schema composer.

1332. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 120
   Toolkit for Coding Agents to work reliably with repo of any size.

1333. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 120
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1334. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 120
   Lightweight agent orchestration dev tool that lives in your repo

1335. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 120
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1336. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 120
   This repository provides the companion Jupyter Notebooks for the book Context-Engineering for Multi-Agent Systems. It technically details the progressive construction of a Context Engine moving from simple prompts to foundational concepts to a production-ready system semantic blueprint.  The code is a guide to building Multi-Agent Systems (MAS)

1337. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 119
   MCP server implementation for n8n workflow automation

1338. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 119
   An MCP server for FFmpeg

1339. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 119
   An MCP server that provides LLMs with the latest stable package versions when coding

1340. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 119
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1341. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 119
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1342. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 118

1343. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 117
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1344. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 117
   Salesforce MCP Server

1345. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 116
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1346. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 116

1347. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 116
   BrowserStack's Official MCP Server

1348. **[kodit](https://github.com/helixml/kodit)** - ⭐ 115
   👩‍💻 MCP server to index external repositories

1349. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 115
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1350. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 115
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1351. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 115
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1352. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 115
   Codex Mcp Server 

1353. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 115
   Tools to allow LLM clients to interact with Linux systems remotely

1354. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 114
   A Model Context Protocol (MCP) for Jupyter Notebook

1355. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 114
   A proxy to use HTTP/SSE MCPs from STDIO clients

1356. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 114
   A modular MCP server that provides commonly used developer tools for AI coding agents

1357. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 114
   Vector-search powered agent memory MCP server

1358. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 114
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1359. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 114
   💻 Give AI models complete control of your computer (probably a bad idea)

1360. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 114
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1361. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 113
   Fast and super efficient Minecraft Server written in C++

1362. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 113
   An MCP server for InterviewReady

1363. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 113
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1364. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1365. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 113

1366. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 113
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1367. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 113
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1368. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 113
   MariaDB MCP (Model Context Protocol) server implementation

1369. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 113
   Docker Hub MCP Server

1370. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 112
   Swagger to MCP server

1371. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 112
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1372. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 112
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1373. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 112
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1374. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 112
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1375. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 112
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1376. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 112
   MCP server implementation for the UniFi network application

1377. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 112
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1378. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 112
   TOON encoding for Laravel. Encode data for AI/LLMs with 40-60% fewer tokens than JSON.

1379. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 111
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1380. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1381. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 111
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1382. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1383. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 111
   Azure API Management as AI Gateway to Remote MCP servers.

1384. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

1385. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 111
   Model Context Protocol Server for Swift

1386. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 111
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1387. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 111
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1388. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1389. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1390. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 110
   Google Sheets MCP Server 📊🤖

1391. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 110
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1392. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 110
   MCP server for Oura API integration

1393. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 110

1394. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 110
   A Model Context Protocol Server to manipulate *.xcodeproj

1395. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 109
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1396. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 109
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1397. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 109
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1398. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 109
   MCP server for connecting agentic systems to search systems via searXNG

1399. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 109
   MCP server for interaction with Bitwarden.

1400. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 109
   Supercharge AI Agents, Safely

1401. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 109
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1402. **[modex](https://github.com/theronic/modex)** - ⭐ 108
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1403. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1404. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1405. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 108
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1406. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 108
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1407. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 108
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1408. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 108
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1409. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

1410. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 107
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1411. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 107
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1412. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 107
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1413. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 107
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1414. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 107
   The coding agent for professionals

1415. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 106
   A Slack MCP server

1416. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 106
   Control WordPress using WP-CLI, AI, and MCP.

1417. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 106
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1418. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 106
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1419. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 106
   A redmine MCP server covering close to 100% of redmines API

1420. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 106
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1421. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 105
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1422. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 105
   Payload CMS MCP Server

1423. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 105
   MCP Client Implementation using Python, LangGraph and Gemini

1424. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 105
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1425. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 105
   blazigly fast gRPC/MCP client & server implementation in zig

1426. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1427. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1428. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 105
   An MCP client for Node.js.

1429. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 105
   MCP Server for working with large Oracle databases

1430. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 105
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1431. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 105
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1432. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 105
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1433. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

1434. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1435. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 104
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1436. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 104
   An MCP Server for your Self Hosted Supabase

1437. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 104
   MCP for semantic code search & navigation that reduces token waste

1438. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 104
   Open Source MCP Servers for Scientific Research

1439. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 104
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1440. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 104
   MCP server for Dash, the macOS documentation browser

1441. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 104
   Isaac Simulation MCP Extension and Server

1442. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 103

1443. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1444. **[mcp](https://github.com/frappe/mcp)** - ⭐ 103
   Frappe MCP allows Frappe apps to function as MCP servers

1445. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1446. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 103
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1447. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 103
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1448. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 103
   fast, secure c# runner

1449. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 103
   MCP server for interacting with the Aseprite API

1450. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 103
      Convert any MCP server into a Claude Skill with 90% context savings

1451. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 103
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1452. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 103
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

1453. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 103
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

1454. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

1455. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 102
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1456. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1457. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1458. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 102
   Raindrop MCP Server

1459. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 102
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1460. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 102
   MCP Server for EMRs with FHIR

1461. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 102
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1462. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 102
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1463. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 102
   Official Railway MCP Server for interacting with your Railway account

1464. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 102
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1465. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 102
   MCP Server for PolyMarket API

1466. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 102
   MCP server for Coolify

1467. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 102
   Enable AI Agents to Control Unity

1468. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 101
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1469. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 101
   Official Vectorize MCP Server

1470. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 101
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1471. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 101
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1472. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 101
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1473. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1474. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 101
    AI-powered security operations with Wazuh SIEM + Claude Desktop. Natural language threat detection, automated incident response & compliance. Real-time monitoring, ML anomaly detection. Transform your SOC with conversational security analysis. Production-ready MCP server.

1475. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1476. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1477. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 100
   Portainer MCP server

1478. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1479. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 100
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1480. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1481. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1482. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 100
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1483. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 99
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1484. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 99
   Collection of examples of how to use Model Context Protocol with AWS.

1485. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1486. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1487. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1488. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1489. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 99
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1490. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 99
   MCP server for querying the Shodan API

1491. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 99
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1492. **[mcp](https://github.com/taskade/mcp)** - ⭐ 98
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1493. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 98
   claude mcp sse demo with server and client(cli、web)

1494. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 98
   💎 A Ruby implementation of the Model Context Protocol

1495. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

1496. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 98
   Node.js Client Implementation for Model Context Protocol (MCP)

1497. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 98
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1498. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 97
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1499. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 97
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1500. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 97
   A Google Tasks Model Context Protocol Server for Claude

1501. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 97
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1502. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 97
   first gemini based desktop client for MCP

1503. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1504. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 97
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

1505. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 97
   Quickly screenshots webpages and converts to an LLM friendly size

1506. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 96
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1507. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 96
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1508. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 96
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1509. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 96
   MCP server for natural language interaction with Power BI datasets

1510. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 96
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1511. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 96
   go doc mcp server

1512. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 96
   lapras.com 公式MCP Server

1513. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 96
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

1514. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 96

1515. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 95
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1516. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 95
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1517. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 95
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1518. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 95
   Model Context Protocol (MCP) server for the Webflow Data API.

1519. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 94
   This is a Ruby implementation of MCP (Model Context Protocol) client

1520. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 94
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1521. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 94
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1522. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 94
    Official Go implementation of the UTCP 

1523. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 94
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1524. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1525. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 93
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1526. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 93
   A Model Context Protocol (MCP) server providing access to Google Search Console

1527. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 93
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1528. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 92
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1529. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 92
   Model Context Protocol server for Replicate's API

1530. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 92
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1531. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for square

1532. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1533. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1534. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 90
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1535. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 90
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1536. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 89
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search and News Search capabilities

1537. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 89
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1538. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 89
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1539. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 88
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1540. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 88
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1541. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 88
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

1542. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 88
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1543. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 87
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1544. **[mcp-web-ui](https://github.com/MegaGrindStone/mcp-web-ui)** - ⭐ 87
   MCP Web UI is a web-based user interface that serves as a Host within the Model Context Protocol (MCP) architecture. It provides a powerful and user-friendly interface for interacting with Large Language Models (LLMs) while managing context aggregation and coordination between clients and servers.

1545. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 87
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1546. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 87
   A model-context-protocol server for molecules.

1547. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 87
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1548. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 87
   Nextcloud MCP Server

1549. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 86
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1550. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 86
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

1551. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 86
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

1552. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 86
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1553. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 85
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1554. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1555. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 85
   CLI & API for MCP management

1556. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 85
   Ragie Model Context Protocol Server

1557. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 85
   Rails Engine with MCP compliant Spec.

1558. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 85
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1559. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 84
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1560. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 83
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1561. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 83
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1562. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 83
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1563. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 82
   A Model Context Protocol server that provides knowledge graph management capabilities.

1564. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 82
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1565. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1566. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1567. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1568. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1569. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 81
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1570. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 81
   MCP server for Mikrotik

1571. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 80
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1572. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 80
   Model Context Protocol (MCP) Server for the Keboola Platform

1573. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 80
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1574. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 80
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1575. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 80
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1576. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 80
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1577. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 80
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

1578. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 80
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1579. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 79
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1580. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 79
   A model context protocol server that connects to Anki through AnkiConnect

1581. **[identity](https://github.com/agntcy/identity)** - ⭐ 79
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1582. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 79
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1583. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 79
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1584. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 79
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1585. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 79
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1586. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 79
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1587. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 78
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1588. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 78
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1589. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 78
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

1590. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 78
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1591. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 77
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1592. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 77
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1593. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 76
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1594. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 76
   Model Context Protocol (MCP) Client for Apify's Actors

1595. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1596. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 76
   Official Oxylabs MCP integration

1597. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 76
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1598. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1599. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 75
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1600. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 75
   A WooCommerce (MCP) Model Context Protocol server

1601. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 75
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1602. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 75
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

1603. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 75
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1604. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 74
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1605. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1606. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 74
   Model Context Protocol for Actual Budget API

1607. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 73
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1608. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1609. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 72
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1610. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 72
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1611. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 72
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1612. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 72
   The Privacy Firewall for LLMs

1613. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 72
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1614. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 72
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1615. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 72
   [WIP] web GUI for securely managing local Opencode configuration

1616. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 71
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1617. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 71
   An md file as a chat interface and editable history in one.

1618. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 71
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1619. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 71
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1620. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 71
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1621. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 71
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1622. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1623. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 70
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1624. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 70
   An unofficial and community-built MCP server for integrating with https://railway.app

1625. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 70
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1626. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 70
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

1627. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 70
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1628. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 69
   Model Context Protocol implementation for retrieving codebases using RepoMix

1629. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 69
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1630. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1631. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 69
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1632. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 69
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

1633. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 69
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1634. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 68
   A Model Context Protocol server for Hopper Disassembler

1635. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

1636. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 68
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1637. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 68
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

1638. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1639. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1640. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1641. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 67
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1642. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1643. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 67
   MCP client for local ollama models

1644. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 67
   An extension of MCP for SillyTavern.

1645. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 67
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1646. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 67
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1647. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 67

1648. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 66
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1649. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 66
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1650. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 66
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

1651. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 66
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1652. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 66
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1653. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 66
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1654. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 66
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1655. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 66
   Open Models MCP for Blender Using Ollama

1656. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 66
   AniList MCP server for accessing anime and manga data

1657. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 66
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1658. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 65
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1659. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 65
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1660. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 65
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1661. **[ViaMCP](https://github.com/ViaVersionMCP/ViaMCP)** - ⭐ 65
   Client-side Implementation of the Via* projects for MCP

1662. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 65
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1663. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 65
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1664. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 65
   Model Context Protocol(MCP) 中文教程讲解

1665. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 65
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

1666. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 65
   From Java Dev to AI Engineer: Spring AI Fast Track

1667. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 65
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1668. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 64
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1669. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1670. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1671. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

1672. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

1673. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 64
   The official MCP server for SurrealDB

1674. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 63
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1675. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 63
   A Model Context Protocol implementation for FHIR

1676. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 63
   Model Context Protocol for x64dbg & x32dbg

1677. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 63
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1678. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 63
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

1679. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 63
   Model Context Protocol for YNAB (you need a budget)

1680. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 63
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1681. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1682. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 62
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1683. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

1684. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 62
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resources for client-side exploration.

1685. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 62
   Index of all Model Context Protocol (MCP) clients and their capabilities

1686. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 62
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1687. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 61
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1688. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1689. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1690. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 61
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1691. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 61
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1692. **[kollektiv-mcp](https://github.com/alexander-zuev/kollektiv-mcp)** - ⭐ 61
   Kollektiv MCP enables you to chat with and query your own documents directly from IDEs and MCP clients. Private, secure, and integrated into your favorite code editor

1693. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 61
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1694. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1695. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 61
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

1696. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 61
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1697. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 61
   A full featured, enterprise grade rust MCP SDK

1698. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 61
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

1699. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 60
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1700. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1701. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 60
   Python 实现 MCP client / service

1702. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 60
   Python code execution sandbox with programmatic MCP tool calling (PTC)

1703. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 60
   Miro integration for Model Context Protocol

1704. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 60
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

1705. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 60
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1706. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1707. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server for Rember.

1708. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 59
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1709. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 59
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1710. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

1711. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

1712. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 58
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1713. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 58
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

1714. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 58
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

1715. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 58
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1716. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 58
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1717. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 58
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1718. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 58
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

1719. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 58
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1720. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

1721. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 57
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

1722. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

1723. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 57
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

1724. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 57
   A Clojure SDK to create MCP servers (and eventually clients)

1725. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 57
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1726. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 56
   MCP router and Web Based MCP client

1727. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 56
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

1728. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

1729. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1730. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

1731. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 56
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1732. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 56
   A Model Context Protocol server for Ashra

1733. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 56
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

1734. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 56
   Open-source FRED MCP Server (Federal Reserve Economic Data)

1735. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 56
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source.

1736. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server for Microsoft Clarity

1737. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

1738. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 55
   MKP is a Model Context Protocol (MCP) server for Kubernetes

1739. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 55
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

1740. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 55
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

1741. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 55
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

1742. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 55
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

1743. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 55
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

1744. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 54
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

1745. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

1746. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

1747. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

1748. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 54
   可视化的配置和管理，给xiaozhi接入mcp

1749. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 54
   MCP server for Slither static analysis of Solidity smart contracts

1750. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 54
   MCP server for *arr media management suite

1751. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 54
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1752. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

1753. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 53
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

1754. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 53
   Quantum-proof MCP Server and Client Interactions

1755. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 53
   Universal MCP Server Configuration Manager

1756. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

1757. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 53
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1758. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 52
   Model Context Protocol Servers for Azure AI Search

1759. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

1760. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 52
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

1761. **[client](https://github.com/php-mcp/client)** - ⭐ 52
   Core PHP implementation for the Model Context Protocol (MCP) Client

1762. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 52
   MCP (Model Context Protocol) server plugin for CAP NodeJS

1763. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

1764. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 52
   OCaml implementation of the Model Context Protocol (MCP)

1765. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 52
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

1766. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

1767. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 52
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

1768. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 52
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

1769. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 52
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

1770. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 52
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

1771. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 52
   MCP Memory Server with DuckDB backend

1772. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 52
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

1773. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 52
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

1774. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 52
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1775. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 52
   A Nasdaq Data Link MCP (Model Context Protocol) Server

1776. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

1777. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 51
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1778. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 51
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

1779. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 51
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

1780. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 51
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

1781. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 51
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

1782. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 51
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

1783. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 51
   MCP Server for IBKR Client

1784. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 51
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

1785. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 50
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

1786. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

1787. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

1788. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 50
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

1789. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 50
   ABAP MCP - Model Context Protocol - Server SDK

1790. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 50
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

1791. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 50
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

1792. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

1793. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 50
   MCP Guard secures your MCP client from prompt injection attacks and more.

1794. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 50
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

1795. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 50
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

1796. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 50
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

1797. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 50
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

1798. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 49
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

1799. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 49
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

1800. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 49
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

1801. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

1802. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 49
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1803. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 49
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

1804. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 49
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

1805. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

1806. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 48
   Anthropic’s Model Context Protocol implementation for Oat++

1807. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

1808. **[mcp](https://github.com/goplus/mcp)** - ⭐ 48
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

1809. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 48
   A Model Context Protocol server that validates and renders Mermaid diagrams.

1810. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

1811. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

1812. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 48
   Unblock, scrape, and search tools for MCP clients

1813. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 48
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1814. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 48
   vMCP - Virtual Model Context Protocol

1815. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 48
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

1816. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 48
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

1817. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 48
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

1818. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 48
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

1819. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 48
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

1820. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 48
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

1821. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 47
   An implementation of the Model Context Protocol in Ruby.

1822. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

1823. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 47
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

1824. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 47
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

1825. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

1826. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

1827. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 47
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

1828. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 47
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

1829. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 47
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

1830. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 47
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

1831. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

1832. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 47
   Official Rust implementation of the UTCP

1833. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 47
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

1834. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 46
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

1835. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 46
   Inkdrop Model Context Protocol Server

1836. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 46
   OpenAPI Schema Model Context Protocol Server

1837. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

1838. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 46
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

1839. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

1840. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

1841. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 46
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1842. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

1843. **[go-mcp](https://github.com/MegaGrindStone/go-mcp)** - ⭐ 46
   A Go implementation of the Model Context Protocol (MCP) - an open protocol that enables seamless integration between LLM applications and external data sources and tools.

1844. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 46
   Sample MCP Server and MCP client with Aspire

1845. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 46
   A Model Context Protocol server for Zendesk

1846. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 46
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

1847. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 46
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

1848. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 46
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

1849. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

1850. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

1851. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 45
   A Model-Context-Protocol (MCP) Server for Active Directory

1852. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 45
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

1853. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

1854. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 45
   Un-official Serper Google search server for Cline and other MCP clients

1855. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 45
   MCPcat is an analytics platform for MCP server owners 🐱.

1856. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

1857. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 45
   共学《MCP极简开发》项目代码

1858. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 45
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

1859. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 45
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

1860. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 45
   Model Context Protocol to fetch youtube transcript

1861. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 45
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1862. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 45
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

1863. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 45
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

1864. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

1865. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 44
   Model Context Protocol server for Flight Tracking

1866. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

1867. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

1868. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 44
   An opinionated starter template for making Model Context Protocol (MCP) servers

1869. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 44
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

1870. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 44
   Model Context Protocol for WeChat

1871. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 44
   Generic MCP Client to use any MCP tool in a chat

1872. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

1873. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

1874. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 44
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

1875. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 44
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

1876. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 44
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

1877. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 44
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

1878. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 44
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

1879. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 44
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1880. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

1881. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 44
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

1882. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 44
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

1883. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

1884. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

1885. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

1886. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 43
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

1887. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 43
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

1888. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 43
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

1889. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 43
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

1890. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

1891. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 43
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

1892. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 43
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

1893. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 43
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

1894. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

1895. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

1896. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 43
   An implementation of the Model Context Protocol for the World Bank open data API

1897. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

1898. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 42
   GraphQL Schema Model Context Protocol Server

1899. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

1900. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

1901. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 42
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

1902. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 42
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

1903. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 42
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

1904. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 42
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

1905. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 42
   Amadeus MCP(Model Context Protocol) Server

1906. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 42
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

1907. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 42
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

1908. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 42
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

1909. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

1910. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 42
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

1911. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 42
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

1912. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 42
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

1913. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 42
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

1914. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 42
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

1915. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 42
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

1916. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 42
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

1917. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 42
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

1918. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 42
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

1919. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 41
   Model Context Protocol server for Salesforce REST API integration

1920. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

1921. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

1922. **[mcp](https://github.com/40ants/mcp)** - ⭐ 41
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

1923. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

1924. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 41
   A Model Context Protocol server for Go developers

1925. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 41
   A production-ready Model Context Protocol (MCP) server for semantic memory management

1926. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 41
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

1927. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 41
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

1928. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

1929. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 41
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

1930. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

1931. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

1932. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 41
   MCP Management Platform - Centralized credential vault, governance, and token optimization for developers and enterprises.

1933. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 41
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

1934. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 41
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

1935. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 41
   Attio Model Context Protocol (MCP) server implementation

1936. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 40
   A Model Context Protocol server for Dify

1937. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

1938. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

1939. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

1940. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

1941. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

1942. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 40
   MCP (Model Context Protocol) server for the Contentful Management API

1943. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 40
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

1944. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 40
   Model Context Protocol Clojure support including REPL integration with development tools.

1945. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 40
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

1946. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 40
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

1947. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 40
   A simple NextJS MCP client with sensible keybindings

1948. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 40
   Implementation of Model Context Protocol server for Mailgun APIs

1949. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

1950. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 40
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

1951. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 40
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1952. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 40
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

1953. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 40
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

1954. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

1955. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 40
   Go SDK for interacting with the MCP Toolbox for Databases.

1956. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 40
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

1957. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 39
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

1958. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

1959. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

1960. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

1961. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

1962. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 39
   Model Context Protocol server for OpenStreetMap data

1963. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

1964. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 39
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

1965. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 39
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

1966. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

1967. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

1968. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 39
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

1969. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 39
   It shows how to use model-context-protocol. 

1970. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 39
   Model Context Protocol server for ActivityWatch time tracking data

1971. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 39
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

1972. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

1973. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 39
   A package manager to manage all your mcp servers across platforms

1974. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

1975. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

1976. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

1977. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 38
   Algorand Model Context Protocol (Server & Client)

1978. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

1979. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 38
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

1980. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

1981. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 38
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

1982. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 38
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

1983. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 38
   MCP server for anki

1984. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 38
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

1985. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 38
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

1986. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 38
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash。为不支持图片理解的 AI 编码模型提供视觉处理能力。

1987. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 38
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

1988. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 37
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

1989. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

1990. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

1991. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 37
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

1992. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1993. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 37
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

1994. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 37
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

1995. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 37
   Model Context Protocol server for Sitecore

1996. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 37
   A Model Context Protocol server that provides access to Shodan API functionality

1997. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 37
   An MCP server for querying Solana transactions using natural language with Solscan API

1998. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 37
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

1999. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 37
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2000. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 37
   A Chat Client for LLMs, written in Compose Multiplatform.

2001. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 37
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2002. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 37
   Model Context Protocol server to let LLMs write and execute matlab scripts 

2003. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 37
   Bluesky MCP (Model Context Protocol) Server

2004. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2005. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 37
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2006. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 37
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

2007. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

2008. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 37
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2009. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 37
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

2010. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 36
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

2011. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

2012. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 36
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2013. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

2014. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 36
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

2015. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

2016. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

2017. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

2018. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 36
   Model Context Protocol Minecraft Server

2019. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

2020. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 36
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2021. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 36
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

2022. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

2023. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 36
   Model Context Protocol (MCP) implementation for iOS simulators

2024. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

2025. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 36
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2026. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 36
   mcp server to run scripts on adobe illustrator

2027. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

2028. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2029. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 36
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2030. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 36
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

2031. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 36
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2032. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

2033. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

2034. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 35
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

2035. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 35
   Privacy-first local RAG server for Cursor, Claude Code, and more — powered by the Model Context Protocol.

2036. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 35
   Model Context Protocol (MCP) server for LinkedIn API integration

2037. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 35
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

2038. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

2039. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 35
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

2040. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2041. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 35
   Altium Model Context Protocol server and Altium API script

2042. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2043. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 35
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

2044. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 35
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

2045. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 35
   Model Context Protocol (MCP) Server for Mistral OCR API

2046. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 35
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

2047. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 35
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

2048. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

2049. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

2050. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

2051. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

2052. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 34
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

2053. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 34
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2054. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2055. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2056. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 34
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

2057. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 34
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2058. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 34
   IMAP Model Context Protocol server for interactive email processing

2059. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 34
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2060. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

2061. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 34
   Rimworld Coding RAG MCP server

2062. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2063. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 34
   A super simple Starter to build your own MCP Server

2064. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 34
   A simple note-taking MCP server for recording and managing notes with AI models.

2065. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 34
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

2066. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 34
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

2067. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 34
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2068. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

2069. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 33
   Model Context Protocol server written in Scala

2070. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 33
   Model Context Protocol Server for Apache OpenDAL™

2071. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 33
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

2072. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

2073. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

2074. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 33
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

2075. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 33
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2076. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 33
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2077. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 33
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

2078. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 33
   A powerful Model Context Protocol server for LinkedIn API integration

2079. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 33
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

2080. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 33
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

2081. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2082. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 33
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

2083. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 33
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2084. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 33
   Turn any MCP Client into a "multi-agent" system (via prompting)

2085. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 33
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2086. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 33
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2087. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 33
   An open source implementation of the Claude built-in text editor tool

2088. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 33
   MCP Server connects with claude code local command.

2089. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 33
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2090. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 33
   About A Model Context Protocol server that executes commands in the current WezTerm session

2091. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

2092. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

2093. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

2094. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

2095. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 32
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

2096. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 32
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

2097. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 32
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

2098. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

2099. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 32
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

2100. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 32
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2101. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 32
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

2102. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 32
   Claude Unified Model Context Interaction Protocol

2103. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 32
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

2104. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 31
   MCP client for Discourse sites

2105. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 31
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

2106. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 31
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2107. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

2108. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 31
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2109. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

2110. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 31
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2111. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

2112. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 31
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2113. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 31
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

2114. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

2115. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 31
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2116. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 31
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

2117. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 31
   Emacs Lisp implementation of the Model Context Protocol

2118. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 31
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2119. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

2120. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 31
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2121. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 31
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2122. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 31
   Model Context Protocol (MCP) server for openBIM

2123. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 30
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

2124. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

2125. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

2126. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

2127. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 30
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

2128. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 30
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

2129. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 30
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

2130. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 30
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2131. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 30
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

2132. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 30
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

2133. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 30
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

2134. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 30
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

2135. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

2136. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 30
   Model Context Server Protocol for your HANA DB

2137. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

2138. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 30
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

2139. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

2140. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 30
   List of Awesome MCP Servers and Clients for building Agentic Devops 

2141. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 30
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

2142. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 30
   Query model running with Ollama from within Claude Desktop or other MCP clients

2143. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2144. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 30
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2145. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 30
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2146. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server for Polymarket prediction markets, providing real-time market data, prices, and AI-powered analysis tools for Claude Desktop integration.

2147. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 30
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2148. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 30
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2149. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 30
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2150. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2151. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 30
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2152. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 30
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2153. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 30
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2154. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 30
   A collection of MCP server examples developed by various Java SDKs

2155. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 30
   The observability layer that AI agents want to use.

2156. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

2157. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 30
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2158. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 29
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

2159. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

2160. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2161. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2162. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 29
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2163. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2164. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2165. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2166. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 29
   Model Context Protocol (MCP) server that interacts with a Debugger

2167. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 29
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2168. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 29
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2169. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 29
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2170. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 29
   Sync MCP (Model Context Protocol) configurations across AI tools

2171. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2172. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2173. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2174. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 29
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2175. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 29
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2176. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 29
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2177. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 29
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2178. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 29
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2179. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 29
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2180. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 29
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

2181. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 29
   Model Context Protocol Server of Rod

2182. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 29
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2183. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 29
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

2184. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 28
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2185. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

2186. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

2187. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

2188. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

2189. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 28
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2190. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 28
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2191. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2192. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 28
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2193. **[mcp](https://github.com/fastly/mcp)** - ⭐ 28
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2194. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

2195. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2196. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2197. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 28
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2198. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 28
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2199. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 28
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2200. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 28
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2201. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 28
   Tools for building modern & secure MCP integrations across the client and server side

2202. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

2203. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 28
   Asterisk Model Context Protocol (MCP) server.

2204. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 28
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2205. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 28
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2206. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2207. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 28
   MCP (Model Context Protocol) server for biothings

2208. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 28
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2209. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 28
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2210. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2211. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 28
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2212. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 28
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2213. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 28
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2214. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 27
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

2215. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

2216. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2217. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

2218. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2219. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 27
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

2220. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

2221. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 27
   Fast rust MCP proxy between stdio and SSE

2222. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 27
   Learn Model Context Protocol with Python, published by Packt

2223. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 27
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

2224. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

2225. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 27
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2226. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 27
   MCP (Model Context Protocol) Server for postgres Database

2227. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 27
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2228. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 27
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2229. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 27
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2230. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 27
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2231. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 27
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2232. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 27
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

2233. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2234. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

2235. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 27
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2236. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 27
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2237. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 26
   Model Context Protocol server for Directus

2238. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

2239. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

2240. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

2241. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

2242. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 26
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

2243. **[mcp-advisor](https://github.com/olaservo/mcp-advisor)** - ⭐ 26
   MCP Server to assist LLMs and humans on Model Context Protocol spec compliance and understanding

2244. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 26
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2245. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 26
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

2246. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

2247. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

2248. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 26
   a web logging proxy for MCP client-server communication

2249. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

2250. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 26
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

2251. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 26
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2252. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 26
   Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from data.gouv.fr, the French national Open Data platform, directly through conversation.

2253. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 26
   An implementation of Giphy integration with Model Context Protocol

2254. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 26
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2255. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 26
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2256. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 25
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2257. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

2258. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

2259. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 25
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

2260. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

2261. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 25
   Model Context Protocol to bridge in Substack writings to Claude.

2262. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

2263. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

2264. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

2265. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 25
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

2266. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2267. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

2268. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

2269. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 25
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

2270. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 25
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

2271. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 25
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2272. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

2273. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 25
   Headless IDA Pro binary analysis via Model Context Protocol

2274. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 25
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2275. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2276. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

2277. **[levante](https://github.com/levante-hub/levante)** - ⭐ 25
   Levante - Personal, Secure, Free, Local AI, MCP Client

2278. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 25
   Azure AI Foundry - Agents related sample code

2279. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 25
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

2280. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

2281. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

2282. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 25
   A generic mcp server fuzzer

2283. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

2284. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 25
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

2285. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 25
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

2286. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 25
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2287. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 25
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

2288. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 25
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

2289. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 25
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2290. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 25
   PowerPlatform Model Context Protocol server

2291. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 25
   Zillow MCP Server for real estate data access via the Model Context Protocol

2292. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

2293. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 25
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

2294. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

2295. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

2296. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 24
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

2297. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

2298. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

2299. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

2300. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2301. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

2302. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 24
   Model Context Protocol Server for NebulaGraph 3.x

2303. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

2304. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 24
   A simple Model Context Protocol (MCP) server for Clay.

2305. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

2306. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 24
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2307. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 24
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

2308. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

2309. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 24
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

2310. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

2311. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 24
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

2312. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 24
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2313. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

2314. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 24
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2315. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 24
   Simple MCP Client for remote MCP Servers 🌐

2316. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 24
   A Curated List of MCP Servers, Clients and Toolkits

2317. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 24
   Educational repo for MCP streamable HTTP servers and clients

2318. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

2319. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 24
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

2320. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 24
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2321. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 24
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

2322. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

2323. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 24
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2324. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

2325. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

2326. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for GreptimeDB

2327. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 23
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2328. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

2329. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 23
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2330. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

2331. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2332. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

2333. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 23
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

2334. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

2335. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

2336. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 23
   A Fastify plugin to run Model Context Protocol (MCP) servers

2337. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 23
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

2338. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 23
   Model Context Protocol SDK implemented in Lua for OpenResty

2339. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 23
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

2340. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

2341. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 23
   A Model Context Protocol server for 3D Slicer integration

2342. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 23
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2343. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 23
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

2344. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 23
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2345. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 23
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2346. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 23
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

2347. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 23
   CLI that uses DSPy to interact with MCP servers.

2348. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

2349. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 23
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

2350. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 23
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

2351. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 23
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

2352. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 23
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2353. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

2354. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 23
   model context protocol for Autodesk Revit

2355. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

2356. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

2357. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2358. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 23
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2359. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 23
   Model Context Protocol server for Github Repo // Reading Github Repo

2360. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 23
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

2361. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 23
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2362. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2363. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 22
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

2364. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

2365. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

2366. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 22
   A MCP(Model Context Protocol) server that accesses to Lightdash

2367. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

2368. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

2369. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

2370. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

2371. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

2372. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

2373. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

2374. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

2375. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

2376. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 22
   Python-based MCP server for BlazeMeter API — orchestrate performance-test lifecycle (create, configure, run, analyze) and manage tests, workspaces, projects & accounts via Model Context Protocol

2377. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

2378. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 22
   Model Context Protocol server for querying Cursor chat history

2379. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 22
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2380. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

2381. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

2382. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 22
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

2383. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 22
   Tanzu Platform Chat

2384. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

2385. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

2386. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

2387. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 22
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

2388. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 22
   Model Context Protocol server for CODESYS automation platform

2389. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

2390. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

2391. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2392. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

2393. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

2394. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

2395. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

2396. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 21
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

2397. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

2398. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

2399. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

2400. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

2401. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 21
   An MCP client for slack in Typescript

2402. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 21
   MCP agent/client/server implementation for private knowledge base

2403. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 21
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

2404. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 21
   A collection of mcp servers/client/sdks

2405. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

2406. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 21
   Simple MCP SDK in Java

2407. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 21
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

2408. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 21
   CLI for calling successive MCP Server tools

2409. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 21
   Command-line interface for any Model Context Protocol (MCP) server.

2410. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 21
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

2411. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 20
   Memory Cache Server for use with supported MCP API Clients.

2412. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 20
   Haskell server/client for MCP (Model Context Protocol)

2413. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 20
   MCP server to expose local zotero repository to MCP clients 

2414. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 20
   Minimal Metals stand alone client that allows running the metals mcp server

2415. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 20
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

2416. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

2417. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 20
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

2418. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 20
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

2419. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 20
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

2420. **[plux](https://github.com/milisp/plux)** - ⭐ 20
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

2421. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 20
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

2422. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

2423. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 20
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

2424. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 20
   Rust MCP framework for building AI agents

2425. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 19
   An MCP Server and client for communicating with Nifi (v1.28)

2426. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 19
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

2427. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 19
   deepseek 结合 mcp 场景，最小用例，包括 client and server

2428. **[starbase](https://github.com/metorial/starbase)** - ⭐ 19
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

2429. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 19
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

2430. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 19
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

2431. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 19
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

2432. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 19
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

2433. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

2434. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 18
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

2435. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 18
   MCP server and client for running Linux commands

2436. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 18
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

2437. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 18

2438. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

2439. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

2440. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 18
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

2441. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 18
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

2442. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 18
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

2443. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

2444. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 18
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

2445. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 18
   The Decodo MCP server which enables MCP clients to interface with services.

2446. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

2447. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

2448. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 17
   Pre-release - Model Context Protocol server for Rollbar

2449. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

2450. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 17
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

2451. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 17
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

2452. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 17
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

2453. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 17
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

2454. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 17
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, and Slides. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

2455. **[gno](https://github.com/gmickel/gno)** - ⭐ 17
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2456. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 17
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

2457. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 16
   An extensible AI agents framework

2458. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 16
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

2459. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 16
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

2460. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

2461. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 16
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

2462. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 16
   A model-agnostic MCP Client-Server for .Net and Unity

2463. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 16
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

2464. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

2465. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

2466. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 16
   LLM Function Calling Library and CLI with Support for MCP Servers

2467. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 16
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

2468. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 16
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

2469. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

2470. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

2471. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 16
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

2472. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 16
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

2473. **[daiv](https://github.com/srtab/daiv)** - ⭐ 16
   Async SWE agents seamlessly integrated on your git platform to automate code issues implementation, reviews, and pipeline repairs.

2474. **[ACP-MCP-Server](https://github.com/GongRzhe/ACP-MCP-Server)** - ⭐ 16
   A bridge server that connects Agent Communication Protocol (ACP) agents with Model Context Protocol (MCP) clients, enabling seamless integration between ACP-based AI agents and MCP-compatible tools like Claude Desktop.

2475. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 15

2476. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 15
   An MCP server to read MCP logs to debug directly inside the client

2477. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 15
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

2478. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

2479. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 15
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

2480. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 15

2481. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 15
   Connect to any MCP servers using agents

2482. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 15
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

2483. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

2484. **[Open-MCP-Client](https://github.com/GongRzhe/Open-MCP-Client)** - ⭐ 14
   ChatMCP is a powerful command-line chat interface that connects to multiple LLM providers (OpenAI, Anthropic, Groq, etc.) and extends their capabilities with tools using the Model Context Protocol (MCP).

2485. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 14
   An MCP client that uses signal for sending and receiving messages.

2486. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 14
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

2487. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 14
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

2488. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 14
   An MCP server and client for LLMs to interact with Unity Projects

2489. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 14
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

2490. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

2491. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

2492. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 14
   MCP host app w/ textual user interface, in Python

2493. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 14
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

2494. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 14
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

2495. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

2496. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

2497. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

2498. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

2499. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 13

2500. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

2501. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 13
   A web-based client for connecting to MCP servers with OAuth support

2502. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 13
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

2503. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

2504. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

2505. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 13
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

2506. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

2507. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

2508. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 13
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

2509. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 13
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

2510. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 13
   Peta core: The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2511. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 12
   MCP server and client for Frontapp

2512. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 12
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

2513. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 12
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

2514. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 12
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

2515. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

2516. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 12
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

2517. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

2518. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 12
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

2519. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

2520. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 12
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

2521. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 12
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

2522. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

2523. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 12
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

2524. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

2525. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 12
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

2526. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 12
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

2527. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 12
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

2528. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 12
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

2529. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 12
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

2530. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

2531. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 11
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

2532. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

2533. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 11
   MCP server to manage Spotify from MCP clients

2534. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 11
   MCP Client for Gemma-3

2535. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

2536. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

2537. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 11
   MCP server to give client the ability to access Wikipedia pages

2538. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 11
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

2539. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

2540. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

2541. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

2542. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

2543. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

2544. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 11
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

2545. **[goldrush-mcp-server](https://github.com/covalenthq/goldrush-mcp-server)** - ⭐ 11
   This project provides a MCP (Model Context Protocol) server that exposes Covalent's GoldRush APIs as MCP resources and tools. It is implemented in TypeScript using @modelcontextprotocol/sdk and @covalenthq/client-sdk.

2546. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 11
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

2547. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

2548. **[muster](https://github.com/giantswarm/muster)** - ⭐ 11
   MCP tool management and workflow proxy

2549. **[claude_autoapprove](https://github.com/PyneSys/claude_autoapprove)** - ⭐ 11
   Autoapprove support for claude

2550. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

2551. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 11
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

2552. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 11
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

2553. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 11
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

2554. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

2555. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 10
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

2556. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 10
   Documentation

2557. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

2558. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

2559. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

2560. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 10
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

2561. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

2562. **[server](https://github.com/mcpfinder/server)** - ⭐ 10
   MCPfinder 🔧🤖 is a service that enables LLMs, running through client applications that support the MCP protocol, to dynamically discover and access new tools, features, and capabilities. When a user requests functionality the AI doesn’t have, it can simply ask MCP Finder to locate relevant MCP servers, expanding its toolset in real time.

2563. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 10
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

2564. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

2565. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 10
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

2566. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 10
   A TUI to probe the calls between MCP client and server

2567. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 10
   tool management service for performing vector tool calling at scale.

2568. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

2569. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 10
   Simple template project for controlling Unity via MCP

2570. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 10
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

2571. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 10
   A multi-agent CLI tool powered by Swarms-rs and Composio

2572. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 10
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

2573. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 10
   Awesome list of MCP servers for interacting with hardware and the physical world.

2574. **[polaris](https://github.com/octu0/polaris)** - ⭐ 10
   Distributed AI Agent Framework

2575. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

2576. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 10
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

2577. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 10
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

2578. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 10
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 40,566
   基于大模型搭建的聊天机器人，同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入，可选择ChatGPT/Claude/DeepSeek/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Kimi/LinkAI，能处理文本、语音和图片，访问操作系统和互联网，支持基于自有知识库进行定制企业智能客服。

2. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 15,408
   AgentScope: Agent-Oriented Programming for Building LLM Applications

3. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,200
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 8,099
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,338
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

6. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,646
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

7. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,610
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

8. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,321
   extendable code review and QA agent 🚢

9. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,636

10. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,585
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

11. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 804
   OpenTelemetry Instrumentation for AI Observability

12. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 770
   A code repository indexing tool to supercharge your LLM experience.

13. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 707
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

14. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 580
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

15. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 562
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

16. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 553
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

17. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 531
   The easiest way to discover and install MCPs

18. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 410
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

19. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 278
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

20. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 154
   Python SDK for interacting with the MCP Toolbox for Databases. 

21. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 146
   Reverse engineer web apps

22. **[ai](https://github.com/WordPress/ai)** - ⭐ 107
   Demonstrate and deliver AI features by combining all AI Building Blocks into a unified WordPress experience.

23. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

24. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 95
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

25. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 70
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

26. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

27. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 59
   Javascript SDK for interacting with the MCP Toolbox for Databases.

28. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 53

29. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 44
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

30. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 41
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

31. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

32. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

33. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 26
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

34. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

35. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

36. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

37. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 17
   A desktop client with MCP support for Mistral LLMs

38. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

39. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 168,544
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,515
   🦍 The Cloud-Native Gateway for APIs & AI

3. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 41,322
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 26,846
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,327
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,184
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 15,752
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 14,923
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI features. ✨

9. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

10. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

11. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,446
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,503
   A cross-platform Markdown AI note-taking software.

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,346
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

14. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,485
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

15. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,411
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,741
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,546
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 7,157
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

19. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,635
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,649
   Adversary simulation and Red teaming platform with AI

21. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,437
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,153
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,114
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,044
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

25. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,001
   Bulk port forwarding Kubernetes services for local development.

26. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 3,868
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

27. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,261
   A shadcn/ui library for building ChatGPT Apps

28. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,068
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

29. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 2,762
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

30. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,689
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

31. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,541
   A highly opinionated, zero-configuration linter and formatter.

32. **[harbor](https://github.com/av/harbor)** - ⭐ 2,287
   Effortlessly run LLM backends, APIs, frontends, and services with one command.

33. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,873
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

34. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,733
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

35. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,698
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

36. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,460
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

37. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,416
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

38. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,394
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

39. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

40. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,305
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

41. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,270
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

42. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,264
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

43. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,162
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

44. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,102
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

45. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,075
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

46. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,066
   A single interface to use and evaluate different agent frameworks 

47. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,006
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

48. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,002
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

49. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 977
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

50. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 965
   Korea Investment & Securities Open API Github

51. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 953
   Arduino MCP2515 CAN interface library

52. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 767
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

53. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 725
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

54. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 701
   Solidity Static Analyzer that easily integrates into your editor

55. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 700
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

56. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 691
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

57. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 660
   A personal AI assistant for everyone

58. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 623
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

59. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 581
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

60. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 529
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

61. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 489
   Marmot helps teams discover, understand, and leverage their data with powerful search and lineage visualisation tools. It's designed to make data accessible for everyone.

62. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 452
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

63. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 451
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

64. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

65. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 423
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

66. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 423
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

67. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 413
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

68. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 386
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

69. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 384
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

70. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 384
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

71. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 383
   Minecraft: Pi Edition API Python Library

72. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 382
   Local first codebase intelligence

73. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 381
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

74. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

75. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 346
   Python toolkit for building graph-enhanced GenAI applications

76. **[bridle](https://github.com/neiii/bridle)** - ⭐ 342
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose)

77. **[exograph](https://github.com/exograph/exograph)** - ⭐ 340
   Build production-ready backends in minutes

78. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 335
   Blender python addon to increase workflow for creating minecraft renders and animations

79. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 331
   MCP for Unreal Engine 5

80. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 321
   Sega Master System / Game Gear / SG-1000 emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

81. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 321
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

82. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 321
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

83. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

84. **[amical](https://github.com/amicalhq/amical)** - ⭐ 316
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

85. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 309
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

86. **[depyler](https://github.com/paiml/depyler)** - ⭐ 298
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

87. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 292
   Software architecture tooling for the AI age

88. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 291
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

89. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 271
   An in-depth book and reference on building agentic systems like Claude Code

90. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 266
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

91. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 260
   Android App: 漢字古今中外讀音查詢

92. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 243
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

93. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 243
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

94. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 243
   AI for Ethical Hacking - Workshop

95. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 239
   Public facing repo for MCP SRG mappings.

96. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 238
   An introduction to the world of AI Agents

97. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 234
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

98. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 234
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

99. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 230
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

100. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 230
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

101. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 219
   A website to generate Minecraft profile pictures

102. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

103. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 215
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

104. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

105. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 201
   Re-usable multi part components built on React Aria and TailwindCSS. 

106. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

107. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

108. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 185
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

109. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 183
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

110. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 177
   Python Deep Agent framework built on top of Pydantic-AI designed to help you quickly build production-grade autonomous agents with planning, filesystem operations, subagent delegation, and skills.

111. **[weam](https://github.com/weam-ai/weam)** - ⭐ 173
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

112. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 164
   Beautiful UI components for AI tool calls

113. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 159
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

114. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 156
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

115. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

116. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 130
   ☕ Community-driven Java implementation of TOON

117. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 125
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

118. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 124
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

119. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 124
   A curated list of open source repositories for AI Engineers

120. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 120
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

121. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 119
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

122. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 119
   wanna develop an app ❓

123. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 109
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

124. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 109
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

125. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 107
   Solid Tumor Associative Modeling in Pathology

126. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 107
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

127. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 105
   5-Day Gen AI Intensive Course with Google

128. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 101
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

129. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 101
   x for mcp

130. **[linggen](https://github.com/linggen/linggen)** - ⭐ 100
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

131. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 99
   Scalable and extensible reinforcement learning for LM agents.

132. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 72
   A lightweight, open, and extensible multi-LLM interaction studio.

133. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 72
   Unity plugin for Coplay

134. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 69
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

135. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 63
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

136. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 61
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

137. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 58
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

138. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 48
   Houdini integration through the Model Context Protocol

139. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 47
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

140. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

141. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 34
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

142. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 31
   Prompt-driven automation platform - Transform natural language into executable workflows

143. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 31
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

144. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

145. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 26
   Build AI Agent using Google ADK , MCP and Gemma 3 model

146. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 26
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具与 Wireshark 进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

147. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

148. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 24
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

149. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

150. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 14
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

151. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 13
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,618
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 6,880
   Specification and documentation for the Model Context Protocol

2. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,865
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

3. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 1,091
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

