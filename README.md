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

## 📚 Projects (2093 total)

> Last updated: **2025-12-31**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 124,199
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 119,333
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 89,192
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 77,873
   A collection of MCP servers.

5. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,187
   The fastest path to AI-powered full stack observability, even for lean teams.

6. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 75,264
   Model Context Protocol Servers

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 70,659
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 69,644
   🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers, Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.

9. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 52,717
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

10. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 44,878
   🔥AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

11. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 41,623
   🎯 告别信息过载，AI 助你看懂新闻资讯热点，支持 RSS 订阅，简单的舆情监控分析 - 多平台热点聚合+基于 MCP 的AI分析工具。监控35个平台（抖音、知乎、B站、华尔街见闻、财联社等），智能筛选+自动推送+AI对话分析（用自然语言深度挖掘新闻：趋势追踪、情感分析、相似检索等20种工具）。支持企业微信/个人微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 推送，30秒快速部署，1分钟手机通知，无需编程。支持Docker部署，支持数据远程云存储⭐ 让算法为你服务，用AI理解热点

12. **[context7](https://github.com/upstash/context7)** - ⭐ 40,519
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

13. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,139
   Query Engine for AI - The only MCP Server you'll ever need

14. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 32,755
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

15. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 32,665
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

16. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,461
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

17. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 30,950
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

18. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 26,249
   Composio equips your AI agents & LLMs with 100+ high-quality integrations via function calling

19. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 25,533
   GitHub's official MCP Server

20. **[goose](https://github.com/block/goose)** - ⭐ 25,239
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

21. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 24,939
   Playwright MCP server

22. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 24,658
   An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations.

23. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 24,243
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

24. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 22,775
   An MCP-based chatbot | 一个基于MCP的聊天机器人

25. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 21,570
   🚀 The fast, Pythonic way to build MCP servers and clients

26. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 20,892
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

27. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 20,873
   The official Python SDK for Model Context Protocol servers and clients

28. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 20,301
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

29. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,139
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

30. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 19,679
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

31. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 19,046
   The TypeScript AI agent framework. ⚡ Assistants, RAG, observability. Supports any LLM: GPT-4, Claude, Gemini, Llama.

32. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 18,279
   Chrome DevTools for coding agents

33. **[agentic](https://github.com/transitive-bullshit/agentic)** - ⭐ 18,073
   Your API ⇒ Paid MCP. Instantly.

34. **[serena](https://github.com/oraios/serena)** - ⭐ 17,915
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

35. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 14,680

36. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 13,913
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

37. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,289
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, WebDAV, Git, and more

38. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,163
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

39. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 12,800
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

40. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 12,365
   MCP server to provide Figma layout information to AI coding agents like Cursor

41. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 11,998
   MCP Toolbox for Databases is an open source MCP server for databases.

42. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,315
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

43. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,170
   The official TypeScript SDK for Model Context Protocol servers and clients

44. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 11,166
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

45. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 10,980
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.

46. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 10,691
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

47. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,239
   Yet another WebUI for Nginx

48. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,177
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

49. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

50. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 9,734
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

51. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 9,576
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书无水印作品文件

52. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 8,792
   mcp-use is the easiest way to interact with mcp servers with custom agents

53. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 8,362
   🕷️ An undetectable, powerful, flexible, high-performance Python library to make Web Scraping Easy and Effortless as it should be!

54. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 8,250
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex & Gemini CLI.

55. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 8,126
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

56. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,101
   Visual testing tool for MCP servers

57. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,075
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

58. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 7,902
   Build effective agents using Model Context Protocol and simple workflow patterns

59. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 7,895
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

60. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 7,750
   MCP for xiaohongshu.com

61. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 7,749
   AWS MCP Servers — helping you get the most out of AWS, wherever you use MCP.

62. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,295
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

63. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,135
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

64. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 6,942
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

65. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 6,875
   MCP Server for Ghidra

66. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,188
   A community driven registry service for Model Context Protocol (MCP) servers.

67. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,141
   A collection of MCP clients.

68. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 5,837
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

69. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 5,805
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

70. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,565
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

71. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 5,500
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

72. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 5,442
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

73. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 5,430
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

74. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,305
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

75. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,177
   WhatsApp MCP server

76. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,154
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

77. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,144
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

78. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,100
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

79. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,033
   Awesome MCP Servers - A curated list of Model Context Protocol servers

80. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,010
   Install, run and deploy your own decentralized AI agent service

81. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 4,892
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

82. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 4,887
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

83. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 4,808
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

84. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 4,772
   A model-driven approach to building AI agents in just a few lines of code.

85. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,695
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

86. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 4,695
   A context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

87. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 4,561
   Open Source TypeScript AI Agent Framework with built-in LLM Observability

88. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,506
   Easily build AI systems with Evals, RAG, Agents, fine-tuning, synthetic data, and more.

89. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 4,479
   An MCP server that allows MCP clients like Claude Desktop or Cursor to perform actions in the Unity Editor

90. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,360
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

91. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,281
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

92. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,272
   opensource self-hosted sandboxes for ai agent

93. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,234
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

94. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 4,154
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

95. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,063
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

96. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 3,932
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

97. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 3,871
   MCP server for Atlassian tools (Confluence, Jira)

98. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,852
   The Cursor & Windsurf community, find rules and MCPs

99. **[Olares](https://github.com/beclab/Olares)** - ⭐ 3,812
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

100. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,789
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

101. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 3,786
   A simple, secure MCP-to-OpenAPI proxy server

102. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 3,764
   MCP Server for Computer Use in Windows

103. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,734
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

104. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,640
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

105. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,636
   Official Notion MCP Server

106. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,591
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

107. **[core](https://github.com/opensumi/core)** - ⭐ 3,579
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

108. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,562
   Define, Prompt and Test MCP enabled Agents and Workflows

109. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,520
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

110. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,516
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

111. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,487
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

112. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,475
   Exa MCP for web search and web crawling!

113. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,469
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

114. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,444
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

115. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,395
   🤖 A visualization mcp contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

116. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,384
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

117. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,303
   GOWA - WhatsApp REST API with support for UI, Webhooks, and MCP. Built with Golang for efficient memory use. 

118. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,283
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

119. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,278
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

120. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,234
   LangChain 🔌 MCP

121. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,233

122. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,227
   Model Context Protocol(MCP) 编程极速入门

123. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 3,214
   A Model Context Protocol (MCP) server that provides Xcode-related tools for integration with AI assistants and other MCP clients.

124. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,196
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

125. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,190
   A curated list of Model Context Protocol (MCP) servers

126. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 3,159
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

127. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 3,139
   Memory infrastructure for LLMs and AI agents

128. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,062
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

129. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,037
   A Model Context Protocol server for Excel file manipulation

130. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,030
   A Model Context Protocol (MCP) Gateway & Registry. Serves as a central management point for tools, resources, and prompts that can be accessed by MCP-compatible LLM applications. Converts REST API endpoints to MCP, composes virtual MCP servers with added security and observability, and converts between protocols (stdio, SSE, Streamable HTTP).

131. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,015
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

132. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,011
   Learn AI and LLMs from scratch using free resources

133. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,007
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

134. **[boost](https://github.com/laravel/boost)** - ⭐ 2,998
   Laravel-focused MCP server for augmenting your AI powered local development experience.

135. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 2,997
   Allow LLMs to control a browser with Browserbase and Stagehand

136. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 2,987
   An Autonomous Agentic Framework for Reflective PowerPoint Generation

137. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,944
   AI agent microservice

138. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,937
   n8n custom node for MCP

139. **[apple-mcp](https://github.com/supermemoryai/apple-mcp)** - ⭐ 2,932
   Collection of apple-native tools for the model context protocol.

140. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,854
   A TypeScript framework for building MCP servers.

141. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 2,839
   Full guide on claude tips and tricks and how you can optimise your claude code the best & strive to find every command possible even hidden ones!

142. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 2,807
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

143. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 2,801
   The missing macOS LLM server. Run local or cloud models with OpenAI & Anthropic compatible APIs. MCP server for Cursor & Claude Desktop, menu bar chat, plugins, and dev tools. Native Apple Silicon.

144. **[mcp](https://github.com/google/mcp)** - ⭐ 2,773
   Google 💚 MCP

145. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 2,768
   The official Rust SDK for the Model Context Protocol

146. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 2,765
   RikkaHub is an Android APP that supports for multiple LLM providers.

147. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,707
   A.I.G (AI-Infra-Guard) is a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

148. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,611
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

149. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,567
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

150. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

151. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,523
   A CLI tool for building Go applications.

152. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 2,392
   UltraRAG v2: A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

153. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,368
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

154. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,351
   Connect Supabase to your AI assistants

155. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,344
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

156. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,328
   A Model Context Protocol server for converting almost anything to Markdown

157. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,294
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

158. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,172
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

159. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,153
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

160. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,123
   A bridge between Streamable HTTP and stdio MCP transports

161. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,097
   Claude Code Subagents & Commands Collection + CLI Tool

162. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,082

163. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,051
   MCP server for Grafana

164. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,047
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

165. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,045
   DDGS | Dux Distributed Global Search. A metasearch library that aggregates results from diverse web search services

166. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,020
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3, Claude, Grok, DeepSeek, OpenRouter, Kimi, GLM, SiliconFlow, GPT-oss, Gemma 3, Qwen 3

167. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,000
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

168. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 1,992
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

169. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 1,985
   A Model Context Protocol server for searching and analyzing arXiv papers

170. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 1,977
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

171. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,963
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

172. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,952
   directory for Awesome MCP Servers

173. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 1,940
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

174. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 1,938
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

175. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 1,934
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

176. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,879
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

177. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,857
   The official MCP server implementation for the Perplexity API Platform

178. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 1,839
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

179. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 1,836
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

180. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 1,823
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

181. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 1,812
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

182. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,807
   Witsy: desktop AI assistant / universal MCP client

183. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 1,791
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

184. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,789

185. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,780
   A secure low code honeypot framework, leveraging AI for System Virtualization.

186. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,776
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

187. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,748
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

188. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,747
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

189. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 1,728
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

190. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,680
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

191. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,678
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

192. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,662
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

193. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,662
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

194. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,651
   Interactive User Feedback MCP

195. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,616
   Desktop Extensions: One-click local MCP server installation in desktop apps

196. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,607
   Make RSS 📰 great again with AI 🧠✨!!

197. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,588
   Coding assistant MCP for Claude Desktop

198. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,575
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

199. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,530
   MCP server that provides tools and resources for interacting with n8n API

200. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,522
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

201. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,522
   Build ChatGPT Apps and MCP servers locally.

202. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,510
   Next Generation Agentic Proxy for AI Agents and MCP servers

203. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,507
   🧩 The ultimate toolkit for working with APIs. 🎅🏼 HO. HO. HO.

204. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,501
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

205. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,486
   An MCP server that installs other MCP servers for you

206. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,478
   ToolHive makes deploying MCP servers easy, secure and fun

207. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 1,469
   Fastest LLM gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

208. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,467
   A Unified MCP Server Management App (MCP Manager).

209. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,462
   ⭐All-in-one AI Companion!  AI Desktop Companion + AI Virtual Streamer + AI Social App Bot + AI Interactive UI Interface + Digital Human Broadcasting + AI Games  and all the features you can imagine! ⭐全能型AI伴侣！AI桌面女友 + AI虚拟主播 + AI社交APP机器人 + AI交互式UI界面 + 数字人播报 + AI游戏 等你能想到的一切功能！

210. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,425
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

211. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,423
   Standards for building agents, better

212. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,418
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

213. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,387
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

214. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,374
   Constrain, log and scan your MCP connections for security vulnerabilities.

215. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,368
   MCP server for interacting with the iOS simulator

216. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,358
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

217. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,350
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

218. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,321
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

219. **[nerve](https://github.com/evilsocket/nerve)** - ⭐ 1,313
   The Simple Agent Development Kit.

220. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,285
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

221. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,284
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

222. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,281
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

223. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,264
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

224. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,259
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

225. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,250
   A connector for Claude Desktop to read and search an Obsidian vault.

226. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,245
   Make your own story. User-friendly software for LLM roleplaying

227. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,244
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

228. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,239
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

229. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,237
   MCP Server for kubernetes management commands

230. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,236
   Damn Vulnerable MCP Server

231. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,232
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

232. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,227
   An MCP server that autonomously evaluates web applications. 

233. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

234. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

235. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,221
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

236. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,211
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

237. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,207
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

238. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

239. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,199
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

240. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,199
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

241. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,196
   The Grafbase GraphQL Federation Gateway

242. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,184

243. **[ai](https://github.com/stripe/ai)** - ⭐ 1,177
   One-stop shop for building AI-powered products and businesses with Stripe.

244. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,173
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for OpenAI, Gemini, Claude, Deepseek and Grok interoperability

245. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,172
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

246. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,162
   The TypeScript MCP framework

247. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,150
   An official Qdrant Model Context Protocol (MCP) server implementation

248. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,149
   The AI toolkit for the AI developer

249. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,148
   The official Swift SDK for Model Context Protocol servers and clients.

250. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,139
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

251. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,139
   Like gmail for your coding agents. Lets various different agents communicate and coordinate with each other.

252. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,122
   The official ElevenLabs MCP server

253. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,118
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

254. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,115
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

255. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,115
   告别AI提前终止烦恼，助力AI更加持久

256. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,112
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

257. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,109
   A Ruby Implementation of the Model Context Protocol

258. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,107
   docker mcp CLI plugin / MCP Gateway

259. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,099
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

260. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 1,089
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

261. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,084
   Build, evaluate and train General Multi-Agent Assistance with ease

262. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,059
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

263. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,055
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

264. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,051
   A web UI for Claude Code agents

265. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,047
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

266. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,042
   The most powerful MCP Slack Server with no permission requirements, Apps support, multiple transports Stdio and SSE, DMs, Group DMs and smart history fetch logic.

267. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,039
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server

268. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,034
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

269. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,034
   Stop re-explaining your project to AI every session. Automatic context memory for Claude, VS Code, Cursor, and 13+ AI tools.

270. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,032
   Production ready MCP server with real-time search, extract, map & crawl.

271. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,030
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

272. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,026
   Query and Summarize your chat messages.

273. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

274. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,025
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

275. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,024
   On-premises conversational RAG with configurable containers

276. **[use-mcp](https://github.com/modelcontextprotocol/use-mcp)** - ⭐ 1,015

277. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,014
   MCP Python Tutorial 

278. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,011

279. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 997
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

280. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 995
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

281. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 981
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

282. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 972
   Claude Code as one-shot MCP server to have an agent in your agent.

283. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 971
   Plugin for JADX to integrate MCP server

284. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 962
   Remote MCP Servers

285. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 959
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

286. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 953
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

287. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 952
   Bringing the power of MCP to the web

288. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 949
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

289. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 947
   MCP server for fetch web page content using Playwright headless browser.

290. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 939
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

291. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 935
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

292. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 932
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

293. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 932
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

294. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 926
   A repository of servers and clients from the Model Context Protocol tutorials

295. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 925
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

296. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 918
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

297. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

298. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 901
   Connect AI models like Claude & GPT with robots using MCP and ROS.

299. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 891
   Expose llms-txt to IDEs for development

300. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 889
   A framework for writing MCP (Model Context Protocol) servers in Typescript

301. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 887
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

302. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 883
   A middleware to provide an openAI compatible endpoint that can call MCP tools

303. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 881
   MCP server helping models to understand your Vite/Nuxt app better.

304. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 881
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

305. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 880
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

306. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 879
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

307. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 874
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

308. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 873
   Model Context Protocol for WinDBG

309. **[tools](https://github.com/strands-agents/tools)** - ⭐ 870
   A set of tools that gives agents powerful capabilities.

310. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 869
   A library for communication with a Minecraft client/server.

311. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 869
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

312. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 867
   Allow AI to wade through complex OpenAPIs using Simple Language

313. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 866
   Grounded Docs MCP Server: Enhance Your AI Coding Assistant 

314. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 862

315. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 859
   Neo4j Labs Model Context Protocol servers

316. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 858

317. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 858
   A security scanner for your LLM agentic workflows

318. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 853
   A concise list for mcp servers

319. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 853
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

320. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 853
   First gitlab mcp for you

321. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 848
   MCP integration for Google Calendar to manage events.

322. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 847
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

323. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 844
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

324. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 842

325. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 839
   Hundreds of Claude Code plugins with embedded AI skills. Learn via interactive Jupyter tutorials.

326. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 835
   The Context Operating System for AI Apps. Build, manage, and deploy AI-optimized Context Graphs.

327. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

328. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 833
   APIM ❤️ AI - This repo contains experiments on Azure API Management's AI capabilities, integrating with Azure OpenAI, AI Foundry, and much more 🚀 . New workshop experience at https://aka.ms/ai-gateway/workshop

329. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 832
   🪐 ✨ Model Context Protocol (MCP) Server for Jupyter.

330. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 828
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

331. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 824
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

332. **[agents](https://github.com/inkeep/agents)** - ⭐ 822
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

333. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 821
   A minimalistic MCP client with a good feature set.

334. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 817
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

335. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 813
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

336. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 808
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

337. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 808

338. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 808
   Simple, modular, and observable Go framework for backend applications.

339. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 806
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

340. **[context-space](https://github.com/context-space/context-space)** - ⭐ 797
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

341. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 795
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

342. **[server](https://github.com/php-mcp/server)** - ⭐ 794
   Core PHP implementation for the Model Context Protocol (MCP) server

343. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 791
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

344. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 789
   Browse the web, directly from Cursor etc.

345. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 788
   OpenAPI Tool Servers

346. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 788
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

347. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 785
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

348. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 784
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

349. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 783
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

350. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 779
   The best way to create, deploy, and share MCP Servers

351. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 773
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

352. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 769
   MAI-UI: Real-World Centric Foundation GUI Agents.

353. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 761
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

354. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 760
   Self-hosted MCP Gateway and Registry for AI agents

355. **[Context](https://github.com/indragiek/Context)** - ⭐ 756
   Native macOS client for Model Context Protocol (MCP)

356. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 754
   Vibetest MCP - automated QA testing using Browser-Use agents

357. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 754
   一个将ACE(Augment Context Engine) 做成MCP的项目

358. **[runno](https://github.com/taybenlor/runno)** - ⭐ 753
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

359. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 752
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

360. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 750
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

361. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 749
   Chat with your Kubernetes Cluster using AI tools and IDEs like Claude and Cursor!

362. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 745
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

363. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 744
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

364. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 742
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

365. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 738
   LLDB MCP Integration + other helpful commands

366. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 738
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

367. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 733
   The better playwright MCP: works as a browser extension. No context bloat. More capable.

368. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 729
   Scan MCP servers for potential threats & security findings.

369. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 725
   An MCP server for interacting with the Financial Datasets stock market API.

370. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 725
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

371. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 715
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

372. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 709
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

373. **[wordpress-mcp](https://github.com/Automattic/wordpress-mcp)** - ⭐ 708
   WordPress MCP — This repository will be deprecated as stable releases of mcp-adapter become available. Please use https://github.com/WordPress/mcp-adapter for ongoing development and support.

374. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 703
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

375. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 696
   A secure local sandbox to run LLM-generated code using Apple containers

376. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 693
   All in one vscode plugin for mcp developer

377. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 690
   Build MCP Agents

378. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 688
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

379. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 687
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

380. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 685
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

381. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 684
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

382. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 677
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

383. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 673
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles and companies, get your recommended jobs, and perform job searches.

384. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 668
   A MCP server implementation for hyperbrowser

385. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 667
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

386. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 667
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

387. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 666
   The official Ruby SDK for the Model Context Protocol. Maintained in collaboration with Shopify.

388. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 664
   MCP server for Docker

389. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 663
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

390. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 662
   A flexible HTTP fetching Model Context Protocol server.

391. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 661
   Clojure MCP

392. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 659
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

393. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 657
   A simple CLI to run LLM prompt and implement MCP client.

394. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

395. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 655
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

396. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 645
   A curated list of Model Context Protocol (MCP) servers 

397. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 644
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

398. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 642
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

399. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

400. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 640
   Laravel API for Ai Agents and humans.

401. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 639
   EnrichMCP is a python framework for building data driven MCP servers

402. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 638
   Querying local documents, powered by LLM

403. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 635
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

404. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 632
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

405. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 630
   Connect ClickHouse to your AI assistants.

406. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 627
   Shell and coding agent on claude desktop app

407. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 627
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

408. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 624
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

409. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 621
   An MCP server that provides control over Android devices via adb

410. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 617
   Talk to a Cloudflare Worker from Claude Desktop!

411. **[mcp](https://github.com/laravel/mcp)** - ⭐ 617
   Rapidly build MCP servers for your Laravel applications.

412. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 617
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

413. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 616
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

414. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 613
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

415. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 612
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

416. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 611
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

417. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 610
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

418. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 608
   A simple MCP server for Obsidian

419. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 607
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

420. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 596
   mem-agent mcp server

421. **[samples](https://github.com/strands-agents/samples)** - ⭐ 591
   Agent samples built using the Strands Agents SDK.

422. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 590
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

423. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 589
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

424. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 589
   Convert Any OpenAPI V3 API to MCP Server

425. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 586
   gcloud MCP server

426. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 584
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

427. **[tome](https://github.com/runebookai/tome)** - ⭐ 582
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

428. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 581
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

429. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 580

430. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 579
   Daydreams is a set of tools for building agents for commerce

431. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 574
   MCP Server For Turkish Legal Databases

432. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 574
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

433. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 573
   The Intelligence Layer for AI agents. Connect your models, tools, and data to create agentic apps that can think, act and talk to you.

434. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 571
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

435. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 567
   LangGraph solution template for MCP

436. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 565
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

437. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 554
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

438. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 549
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

439. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 548
   MCP to connect your LLM with Spotify.

440. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 547

441. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 546

442. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 542
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

443. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 540
   Security scanner for MCP servers

444. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 538

445. **[obot](https://github.com/obot-platform/obot)** - ⭐ 535
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

446. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 533

447. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 533
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

448. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 531
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

449. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 531

450. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 531
   MCP server for interacting with Neon Management API and databases

451. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 531
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

452. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 529

453. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 528
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

454. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 528
   The .NET library to build AI agents with 25+ built-in connectors.

455. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 521
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

456. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 521
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

457. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 520
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

458. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 519
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

459. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 519
   An MCP Multimodal AI Agent with eyes and ears!

460. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 519
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

461. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 517
   An MCP server to query any Postgres database in natural language.

462. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 517

463. **[ethora](https://github.com/dappros/ethora)** - ⭐ 516
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

464. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

465. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 515
   An Mcp client inside Emacs

466. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 513
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

467. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 508
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

468. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

469. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 506
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

470. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 506
   Draw.io Model Context Protocol (MCP) Server

471. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 505
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

472. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 505
   A MCP server for Home Assistant

473. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 505
   MCP server for querying Apple Health data with natural language and SQL

474. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 505
   提取抖音无水印视频链接，视频文案，douyin-mcp-server

475. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 503
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

476. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 503
   Open Source Voice Agent Platform

477. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 503
   A Model Context Protocol server for IDA

478. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 502
   MCP server to deploy apps to Cloud Run

479. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 501
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

480. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 500
   A comprehensive collection of Model Context Protocol (MCP) servers

481. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 500
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

482. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 499
   Yes Mcp server in bash

483. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 499
   微信读书MCP

484. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 498

485. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 496
   A tool that converts OpenAPI specifications to MCP server

486. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

487. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 490
   An MCP server for interacting with Sentry via LLMs.

488. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 489
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

489. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 486
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

490. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 485

491. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 485
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

492. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 485
   Next.js Development for Coding Agent

493. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 483
   MCP Monitoring with eBPF

494. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 482
   A Model-Context Protocol Server for YouTube

495. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 480
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

496. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 477
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

497. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 473
   MCP server for document format conversion using pandoc.

498. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 470
   Aser is a lightweight, self-assembling AI Agent frame.

499. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 469
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

500. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 468
   MCP Server to interact with Google Gsuite prodcuts

501. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 467
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

502. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 466
   An SDK building Laravel MCP servers

503. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 466
   MCP to allow AI agents to control Unreal

504. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 462
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

505. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 461
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

506. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 460
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

507. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 457
   Install, manage and develop MCP servers

508. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 456
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

509. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 453
   A powerful VSCode extension that lets you find and install MCP servers to use with GitHub Copilot, Claude Code, and Codex CLI.

510. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 453
   LLM + MCP + RAG = Magic

511. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 451
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

512. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 450
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

513. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 449
   MCP server integration for DaVinci Resolve

514. **[argo](https://github.com/xark-argo/argo)** - ⭐ 449
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

515. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 449
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, dynamic model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model parameters configuration, custom system prompt and saved preferences. Built for developers working with local LLMs.

516. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 448
   A MCP (Model Context Protocol) server for interacting with dbt.

517. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 447

518. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 447
   "AnyTool: Universal Tool-Use Layer for AI Agents"

519. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 445
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, and comprehensive lifecycle management capabilities.

520. **[director](https://github.com/director-run/director)** - ⭐ 443
   MCP Playbooks for AI agents

521. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 443
   Govern & Secure your AI

522. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 439
   A docker MCP Server (modelcontextprotocol)

523. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 437
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

524. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 437
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

525. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 436

526. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 435
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

527. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 434
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

528. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 431
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

529. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 431
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

530. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 429
   FreeCAD MCP(Model Context Protocol) server

531. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 427
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

532. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 427
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

533. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 426
   GitOps on Autopilot Mode

534. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 425
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STEAMABLEHTTP access protocols to deploy MCP。

535. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 424
   MCP Server for Turkish & American Stock Exchange and Fund Data

536. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 423
   MCP configuration to connect AI agent to a Linux machine.

537. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 421
   Send emails directly from Cursor with this email sending MCP server

538. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 421
   A simple, locally hosted Web Search MCP server for use with Local LLMs

539. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 418
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

540. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 418

541. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 417
   Spec-Driven Development MCP Server, not just Vibe Coding

542. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 417
   Make your meetings accessible to AI Agents

543. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 416
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

544. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 415
   小红书MCP服务 x-s x-t js逆向

545. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 414
   Unlock 650+ MCP servers tools in your favorite agentic framework.

546. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 414
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

547. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 414
   MCP Server for Burp

548. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 412
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

549. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 411
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

550. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 409
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

551. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 406
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

552. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 406
   基于NET搭建-AI智能体-现代化Saas企业级前后端分离架构-开启智能应用的无限可能：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR验证码识别、API多版本兼容、单元集成测试、RabbitMQ、代码生成器

553. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 405
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

554. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 403
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

555. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 401
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

556. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 400
   The safest way to make REST calls in C# with an MCP Generator

557. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 400
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

558. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 400
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

559. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 400
   A CLI inspector for the Model Context Protocol

560. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 398
   MCP Server for Metasploit

561. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 398
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

562. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 396
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

563. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 395
   An experiment in software planning using MCP

564. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 394
   MCP server that execute applescript giving you full control of your Mac

565. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 390
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

566. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 389
   Enterprise-ready MCP gateway, MCP registry & orchestrator

567. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 388
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

568. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 388
   MCP server for DuckDB and MotherDuck

569. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 388
   An MCP extension for Ghidra

570. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 386
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

571. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 383
   MCP-NixOS - Model Context Protocol Server for NixOS resources

572. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 382
   Memento MCP: A Knowledge Graph Memory System for LLMs

573. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 382
   Official Docker MCP registry 

574. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 380
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

575. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 380
   BioMCP: Biomedical Model Context Protocol

576. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 379
   Local Groq Desktop chat app with MCP support

577. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 379
   Official Jina AI Remote MCP Server

578. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 378
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

579. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 378
   Baidu Map MCP Server

580. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 378
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

581. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 378
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

582. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 377
   lunar.dev: Agent native MCP Gateway for governance and security

583. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 376
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

584. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 375
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

585. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 374
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

586. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 373
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

587. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 372
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

588. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 370
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

589. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 370
   MCP Server for SearXNG

590. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 369
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

591. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 368
   Model Context Protocol (MCP) Server for Graphlit Platform

592. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 368
   MCP server connecting to Kubernetes

593. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 366
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

594. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 366
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

595. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 365
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

596. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 365
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

597. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 364
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

598. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 364
   MCP Server for code graph analysis and visualization by CodeGPT

599. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 362
   Model Context Protocol SDK for PHP

600. **[station](https://github.com/cloudshipai/station)** - ⭐ 362
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

601. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 361
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

602. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 360
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Cognito integration.

603. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 357
   Making docling agentic through MCP

604. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 356
   MCP integration platforms making AI-Agents developers focusing on their own tasks

605. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 356
   A fully functional MCP server and CLI for YouTube

606. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 356
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

607. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 355
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

608. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 355
   Up-to-date Documentation for AI Agents.

609. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 354
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

610. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 354
   A model-driven approach to building AI agents in just a few lines of code. 

611. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 353
   Search Airbnb using your AI Agent

612. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 352
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

613. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 351
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

614. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 350
   MCP server that provides LLMs with tools for interacting with EVM networks

615. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 350
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

616. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 349
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

617. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 349
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的专有领域智能聊天助手

618. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 349
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

619. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 349
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

620. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 348
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! Supports Claude Desktop, Dashscope & Cursor.

621. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 346
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

622. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 345
   MCP Server implementation for Ableton Live OSC control

623. **[mcpr](https://github.com/conikeec/mcpr)** - ⭐ 344
   Model Context Protocol (MCP) implementation in Rust

624. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 344
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

625. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 343
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

626. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 342
   MCP server for Todoist integration enabling natural language task management with Claude

627. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 342
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

628. **[daan](https://github.com/pluveto/daan)** - ⭐ 341
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

629. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 341
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

630. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 341
   Model Context Protocol server for GraphQL

631. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 341
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

632. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 341
   AI-based stock analysis and trading system

633. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 339
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

634. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 339
   MCP Server implementation for Xcode integration

635. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 339
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

636. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

637. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 336
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

638. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 335
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

639. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 335
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

640. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 335
   F2C MCP Server

641. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 335
   A macOS AppleScript MCP server

642. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 335
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

643. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 333
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

644. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 333
   SonarQube MCP Server

645. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 333
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

646. **[codexia](https://github.com/milisp/codexia)** - ⭐ 332
   A powerfull GUI/IDE and Toolkit for Codex CLI + Claude Code. FileTree + prompt notepad + git worktree and more

647. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 331
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

648. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 331
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

649. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 330
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

650. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 330
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

651. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 330
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

652. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 328
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

653. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 328
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

654. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 327
   Elixir Model Context Protocol (MCP) SDK

655. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 327
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

656. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 325

657. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 324
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models. v0.2.8

658. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 324
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

659. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 324
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

660. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 323
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

661. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 323
   飞书/Lark官方 OpenAPI MCP

662. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 322
   An MCP implementation for Selenium WebDriver

663. **[moling](https://github.com/gojue/moling)** - ⭐ 321
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

664. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 321
   Nuwax AI - Easily build and deploy your private Agentic AI solutions.  智能体智能应用一站式搭建平台，无需编程基础，构建你的MCP、工作流、智能体，还可一句话生成智能应用，从想法到实现只差1分钟.

665. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 321

666. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 319
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

667. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 319
   Control your Android devices with AI using Model Context Protocol

668. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 319

669. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 318
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

670. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 318
   AI-Powered Revit Modeling

671. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 318
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

672. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 317
   This is a Minecraft Base Client

673. **[emcee](https://github.com/mattt/emcee)** - ⭐ 315
   MCP generator for OpenAPIs 🫳🎤💥

674. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 314
   Repo of skills for autogen studio using model context protocol (mcp)

675. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 314
   An MCP server for Azure DevOps

676. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 314
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

677. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 313
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

678. **[mcp](https://github.com/IBM/mcp)** - ⭐ 311
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

679. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 311
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

680. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 311
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

681. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 310
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

682. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 310
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

683. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 309
   Xiaozhi MCP sample program

684. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 307
   MCP server to expose VS Code editing features to an LLM for AI coding

685. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 306
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

686. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 305
   Professional development environment for Claude Code with spec-driven workflow, TDD enforcement, cross-session memory, semantic search, quality hooks, and modular rules 🛠️

687. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 302
   A working pattern for SSE-based MCP clients and servers

688. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 301
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

689. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 301
   Turn any openapi file into an mcp server, with just the tools you need.

690. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 301
   deep, reliable and confidential coding-context

691. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 300
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

692. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 299
   api router for MCP Servers

693. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 299
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

694. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 297
   A Model Context Protocol server for building an investor agent

695. **[mcp-nodejs-debugger](https://github.com/workbackai/mcp-nodejs-debugger)** - ⭐ 297
   🐞 MCP Node.js debugger

696. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 296
   Mapbox Model Context Protocol (MCP) server

697. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 296

698. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 295
   MCP implementation of Claude Code capabilities and more

699. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 295
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

700. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 294
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

701. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 294
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

702. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 294
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

703. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 293
   An MCP server for loading skills (shim for non-claude clients).

704. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 293
   An MCP server that indexes local code into a graph database to provide context to AI assistants.

705. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 292

706. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 292
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

707. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 291
   An implementation of Model Context Protocol (MCP) server for Argo CD.

708. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 291
   Agentic RAG for any scenario. Customize sources, depth, and width

709. **[gemini-flow](https://github.com/clduab11/gemini-flow)** - ⭐ 290
   rUv's Claude-Flow, translated to the new Gemini CLI; transforming it into an autonomous AI development team.

710. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 288
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

711. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 288
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

712. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 287

713. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 286
   Model Context Protocol server for DeepSeek's advanced language models

714. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

715. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 286
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

716. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 286
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

717. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 286
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

718. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 286
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

719. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 284
   Minimal MCP Server for Aider

720. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

721. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 283
   hydra-ai

722. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 283
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

723. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 283
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

724. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 282
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

725. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 282
   A Production-Ready Runtime Framework for Agent Deployment and Tool Sandbox

726. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

727. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 281
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

728. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 281
   Discover Exceptional MCP Servers

729. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 281

730. **[generator](https://github.com/context-hub/generator)** - ⭐ 281
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

731. **[mesh](https://github.com/decocms/mesh)** - ⭐ 281
   One secure endpoint for every MCP server. Deploy anywhere.

732. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 280
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

733. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 280

734. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 280
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (GitHub Copilot, Cursor, etc.) to interact directly with Figma

735. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 279
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

736. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 278
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

737. **[consult7](https://github.com/szeider/consult7)** - ⭐ 278
   MCP server to consult a language model with large context size

738. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 278
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

739. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 278
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

740. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 277
   The specification for the Universal Tool Calling Protocol

741. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 277
   MaverickMCP - Personal Stock Analysis MCP Server

742. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 276
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

743. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 276
   simple web ui to manage mcp (model context protocol) servers in the claude app

744. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 276
   First AI‑enabled open-source Human Capital Management system that you can start using today.

745. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 275
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

746. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 275
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

747. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 275
   Model Context Protocol (MCP) Server for dify workflows

748. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 273
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

749. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 272
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

750. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 272
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

751. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 272
   MCP server for browser automation using Playwright

752. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 272
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

753. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 271
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

754. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 271
   A Model Context Protocol Server for MongoDB

755. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

756. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 270
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

757. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 270
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

758. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 268
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

759. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 268
   Proximity is a MCP security scanner powered with NOVA

760. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 268
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

761. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 268
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

762. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 267
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

763. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 267
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

764. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 266
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

765. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 264
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

766. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 263
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

767. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 262
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

768. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 262
   Obsidian MCP (Model Context Protocol) Server

769. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 262
   Source code of minecraft 1.12

770. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 262
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

771. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 262
   OpenSkills: Run Claude Skills Locally using any LLM

772. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 261
   MCP server for Windows OS automation

773. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 261

774. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 261
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

775. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 260
   An MCP server providing tools for image processing operations

776. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 258
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

777. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 258
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

778. **[mq](https://github.com/harehare/mq)** - ⭐ 258
   jq-like command-line tool for markdown processing

779. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 257
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

780. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 256
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

781. **[mcp](https://github.com/oracle/mcp)** - ⭐ 255
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

782. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 254
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

783. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

784. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 252
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

785. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 252
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

786. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 252
   Home Assistant MCP Server

787. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 251
   MCP Server for Odoo

788. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 251
   MCP server for JADX-AI Plugin

789. **[api200](https://github.com/API-200/api200)** - ⭐ 248
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

790. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 248
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

791. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 247
   MCP server(s) for Aipolabs ACI.dev

792. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 247
   A code reasoning MCP server, a fork of sequential-thinking

793. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 247
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

794. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 246
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

795. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 246
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

796. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 246
   Model Context Protocol server implementation for Reddit

797. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 244
   MCP server implementation for Google's Gemini API

798. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 244
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

799. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 243
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

800. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 243
   Apollo MCP Server

801. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 242
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

802. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 241
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

803. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 241
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

804. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 241
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

805. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 241
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

806. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 240
   Pixelize the real world on-chain

807. **[app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server)** - ⭐ 240

808. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 240
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

809. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 239
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

810. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 238
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

811. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 238
   Apache Doris MCP Server

812. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 237
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

813. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 236
   Easy guide to installing Claude Code MCPs globally on your machine.

814. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 236
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

815. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 236
   MCP Server for interacting with Salesforce instances

816. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 236
   MCP Interface for Video Jungle

817. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 236
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

818. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

819. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 235
   Simplified Gemini for Claude Code. 

820. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 235
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

821. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 235

822. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 235
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

823. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 234
   Turn any MCP server into a Python module

824. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 234
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

825. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 234
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

826. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 233
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

827. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 232

828. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 232
   Code Runner MCP Server

829. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 232
   Creates a simple MCP tool server with "streaming" HTTP.

830. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 232
   The evaluation benchmark on MCP servers

831. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 232
   🔥 Model Context Protocol (MCP) server for Firebase.

832. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 232
   An MCP server for Massive.com Financial Market Data

833. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 231
   小智AI客户端，目前主要用于MCP的对接

834. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 230
   MCP Server for Tree-sitter

835. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 230
   MCP server for Bazi (八字) information

836. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 229
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

837. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 228
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

838. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 228
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

839. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 226
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

840. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 226
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

841. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 226
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

842. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 226
   A Model Context Protocol (MCP) server that enables natural language queries to databases

843. **[dat](https://github.com/hexinfo/dat)** - ⭐ 226
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

844. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 226
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

845. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 225
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

846. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 224
   An experimental MCP Server for foundry built for Solidity devs

847. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 224
   MCP Server for Telegram

848. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 224
   Lightweight MCP Server for interacting with Android Operating System.

849. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 223
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

850. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 223
   A collection of MCP servers

851. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 223
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

852. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 222
   SpringAI，LLM，MCP，Embedding

853. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 221
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

854. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 220

855. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 219
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

856. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 219

857. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

858. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 219
   Semantic code searcher and codebase utility with AI memory onboard

859. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 219
   Model Context Protocol server to run commands

860. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 219
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

861. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 219
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

862. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 218
   A TypeScript SSE proxy for MCP servers that use stdio transport.

863. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 218
   Standardized environment infrastructure for Agentic AI development.

864. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

865. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 217
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

866. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 217
   AWS MCP Proxy Server

867. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 216
   A Model Context Protocol (MCP) server for interacting with Twitter.

868. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 216
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

869. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 215
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

870. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 215
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

871. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 215
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

872. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 214
   Standalone Roblox Studio MCP Server

873. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 213
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

874. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

875. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 212

876. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 212
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

877. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 212
   CAD MCP Server

878. **[tentix](https://github.com/labring/tentix)** - ⭐ 212
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

879. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 212
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

880. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 211
   A ReAct-Based Highly Robust Autonomous Agent Framework.

881. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 211
   Agent MCP for ffmpeg

882. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 211
   Razorpay's Official MCP Server

883. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 211

884. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 211
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

885. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 211
   Volcengine MCP Servers

886. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 211
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

887. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 210
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

888. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 210

889. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 210
   ModelContextProtocol for Figma's REST API

890. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 210
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

891. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 210
   Playwright MCP fork that works with Cloudflare Browser Rendering

892. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 210
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

893. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 209
   mindmap, mcp server, artifact

894. **[lokka](https://github.com/merill/lokka)** - ⭐ 209
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

895. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 209
   Lean Theorem Prover MCP

896. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 208
   A Multi-modal MCP client for voice powered agentic workflows

897. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 208

898. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 208
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

899. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 208
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

900. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 208
   Lightweight C++ MCP (Model Context Protocol) SDK

901. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 208
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

902. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 207
   Model Context Protocol Servers for Milvus

903. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 207
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

904. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 207
   MCP server for searching and retrieving Claude Agent Skills using vector search

905. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 206
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

906. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

907. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 205
   MCP security wrapper

908. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 205
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

909. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 205

910. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 205
   MCP server for Claude to access Outlook data via Microsoft Graph API

911. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 205
   Penpot MCP server

912. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 204
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

913. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 204
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

914. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 204
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

915. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 204
   interactive programming of melodies, producing MIDI 

916. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 204

917. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 203
   Model Context Protocol tool support for LangChain

918. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 203
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

919. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 203
   An MCP server to use Sora video generation APIs

920. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 202
   Lightweight MCP server for Spotify

921. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 201
   Zerodha Kite MCP server

922. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 200
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

923. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 200
   The Unofficial and Awesome Home Assistant MCP Server

924. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 199
   Run and monitor MCP servers locally

925. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 199
   A Tiny Terminal Chat App for AI Models with MCP Client Support

926. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 199
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

927. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 198
   MCP server for Anki via AnkiConnect

928. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 198
   A centralized proxy platform for MCP servers, accessible via a single HTTP server,featuring a web-based management interface. 

929. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 198
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

930. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 198
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

931. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 197
   Java AI（智能体） 全场景应用开发框架（LLM，Function Call，RAG，Embedding，Reranking，Flow，MCP Server，Mcp Client，Mcp Proxy）。同时兼容 java8 ~ java25。也可嵌入到 SpringBoot2、jFinal、Vert.x 等框架中使用。。支持 MCP_2025_06_18（mcp streamable）

932. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 196

933. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 196
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

934. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

935. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 196
   A MCP Server for the RAG Web Browser Actor

936. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 196
   🔎 A MCP server for Unsplash image search.

937. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

938. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 195
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

939. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 195
   Pure Rust implementation of MCP server for headless terminal 

940. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 195
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

941. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 195
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

942. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 195
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

943. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 194
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

944. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 194
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

945. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 194
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

946. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 193
   R MCP Server

947. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 193

948. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 192
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

949. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 192
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

950. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 191
   Absurdly easy Model Context Protocol Servers in Typescript

951. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 191
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

952. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 191
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

953. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 191
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

954. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 191
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

955. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 191
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

956. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

957. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 190
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

958. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 189

959. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 189
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

960. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 189
   Manage / Proxy / Secure your MCP Servers

961. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 189
   A SEC EDGAR MCP (Model Context Protocol) Server

962. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 189
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

963. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 189
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

964. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 189
   Things.app MCP Server

965. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 189
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

966. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 189
   Context-Engine: MCP retrieval stack for AI coding assistants. Hybrid code search (dense + lexical + reranker), ReFRAG micro-chunking, local LLM prompt enhancement, and dual SSE/RMCP endpoints. One command deploys Qdrant-powered indexing for Cursor, Windsurf, Roo, Cline, Codex, and any MCP client.

967. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 188
   Homeassistant MCP server for 小智AI

968. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

969. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

970. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

971. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 187
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

972. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 187
   MCP server for Dynatrace Observability

973. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 187
   Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs and allows claude to make direct edits and formatting. Use cases include writing notes, letters, resumes, creating tables, etc. 

974. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

975. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 186
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

976. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 186
   Self-hosted AI RAG + MCP Platform

977. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 186
   这是一个专为开发企业级MCP server而设计的通用开发框架

978. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 186
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

979. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 185
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

980. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

981. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 184
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

982. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 184
   Supabase MCP server created in Python.

983. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 184
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

984. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 184
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

985. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 184
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

986. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 183
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

987. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 183
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

988. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

989. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

990. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 182
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

991. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 182
   A TypeScript framework for building MCP servers elegantly

992. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 182
   Platform to create, curate and host MCP servers ⚒️ Build production quality tools for your agents.

993. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 181
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

994. **[siconos](https://github.com/siconos/siconos)** - ⭐ 180
   Simulation framework for nonsmooth dynamical systems

995. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 180
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

996. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 179
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

997. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 179
   Model Context Protocol Servers in Quarkus

998. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 179
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

999. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 179
   A MCP server for our beloved terminal multiplexer tmux.

1000. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 179
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1001. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1002. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1003. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 178
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1004. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 178
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1005. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 178
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1006. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 178
   The Power BI Desktop MCP Server is a tool that lets AI assistants like Claude interact with your Power BI models programmatically. It enables Claude to read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1007. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 177
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1008. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 177
   An MCP server for Anki

1009. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1010. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 177

1011. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 177
   MCP Server for ServiceNow

1012. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1013. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 174
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1014. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 173
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1015. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 173
   MCP Server for the Bilibili API, supporting various operations.

1016. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 173
   This extension enables developers to implement the MCP server features easily.

1017. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 173
   Google Search Console Insights with Claude AI for SEOs

1018. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 172
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1019. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 172
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1020. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 170

1021. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 170
   MCP for calling Siri Shorcuts from LLMs

1022. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 169
   Examples of using Pipedream's MCP server in your app or AI agent.

1023. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 169
   pctx is the execution layer for agentic tool calls. It exposes custom tools and MCP servers as code that runs in secure sandboxes for token-efficient calls.

1024. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 169
   Hugging Face MCP Server

1025. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 168
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1026. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 168
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

1027. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 167
   A MCP server to search for accurate academic articles.

1028. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 166
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1029. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 166
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1030. **[command](https://github.com/scopecraft/command)** - ⭐ 165
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1031. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 165
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1032. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 165
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1033. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 165
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1034. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 164
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1035. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 164
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1036. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 164
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1037. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 164
   MCP stdio server for frida

1038. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 163
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1039. **[mcp-run-python](https://github.com/pydantic/mcp-run-python)** - ⭐ 163
   MCP server to run Python code in a sandbox.

1040. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 163
   Turn any website or doc into an MCP server

1041. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 162
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1042. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 162
   One MCP Server, All Your Apps, Privacy First

1043. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 162
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1044. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 161
   MCP (Model Context Protocol) server for Weaviate

1045. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 161
   MCP server to work with Telegram through MTProto

1046. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 161
   Discord MCP Server for Claude Integration

1047. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 161
   Official Magic UI MCP server.

1048. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 160
   MCP server for TouchDesigner

1049. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 160
   A list of open-source AI projects you can use to generate income easily.

1050. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 159
   An MCP server for fetching URLs / Youtube video transcript.

1051. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 159
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1052. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 159
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1053. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 159
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1054. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 159
   Turn a web server into an MCP server in one click without making any code changes.

1055. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 158
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1056. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 158
   Command line interface for MCP clients with secure execution and customizable security policies

1057. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 158
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1058. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1059. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 157
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1060. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 157
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1061. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 157
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1062. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 157
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1063. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 156

1064. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 156
   MCP Server for Wazuh SIEM

1065. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 156
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1066. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 156
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1067. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 155
   Sketchup Model Context Protocol

1068. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 155
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1069. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 155
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1070. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 155
   Learn how to use MCP Servers with GitHub Copilot

1071. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 155
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1072. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 155
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1073. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 154
   MCP server retrieving transcripts of YouTube videos

1074. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 153
   MCP server implementation for Google's Gemini API

1075. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 153
   ToolSDK.ai's Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1076. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 153
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1077. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 153
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

1078. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 152
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1079. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 151
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1080. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 151
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1081. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 151
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1082. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 151
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1083. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 151
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1084. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 150

1085. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 150
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1086. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 149
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1087. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 149
   Let LLMs control embedded devices via the Model Context Protocol.

1088. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 149
   An MCP server to search for flights.

1089. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 148
   Desktop APP for Discover and Install MCP Servers

1090. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 148
   Deep Research for crypto - free & fully local

1091. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 148
   MCP Server for AI Summarization

1092. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 148
   MCP Server for Postgres

1093. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 148
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1094. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 148
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1095. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 147
   Make MCP Server

1096. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 147
   MCP server for searching and querying PubMed medical papers/research database

1097. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 147
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1098. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 147
   A gateway demo for MCP SSE Server

1099. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 147
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1100. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 146
   MCP Server for using any LLM as a Tool

1101. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 146
   A simple MCP server to search for documentation (tutorial)

1102. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 146
   MCP server to download entire websites

1103. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 146
   Instagram Direct messages MCP

1104. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 146
   Typescript SDK to build MCP servers in an agnostic way

1105. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 146
   Model Context Protocol For R

1106. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 145
   Model Context Protocol (MCP) server for constraint optimization and solving"

1107. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 145
   Connect any Open Data to any LLM with Model Context Protocol.

1108. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 145
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

1109. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 144
   Model Context Protocol server implementation for Figma API

1110. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 144
   Goku is an HTTP load testing application written in Rust 

1111. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 144
   An MCP server that provides access to Postman.

1112. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 144

1113. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 144
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1114. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 143
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1115. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 143
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1116. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 143
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1117. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 142
   A PubMed MCP server.

1118. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 142
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1119. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 142
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1120. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 142
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1121. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 141

1122. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 141
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1123. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 141
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1124. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 140
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1125. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 140
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1126. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 140
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1127. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 140
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1128. **[kom](https://github.com/weibaohui/kom)** - ⭐ 140
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1129. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 139
   Simple MCP Server Implementation

1130. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 139
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1131. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 139
   A list of MCP (Model Context Protocol) servers for developer tools and services

1132. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 139
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1133. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 138
   MCP server for Israel Government Data

1134. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 138
   A Model Context Protocol server for calculating.

1135. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 138
   A MCP Server for creating Powerpoint Presentations

1136. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 138
   Catch MCP server issues before your agents do.

1137. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 138
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1138. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 137
   A Model Context Protocol server for MySQL database operations

1139. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 137
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1140. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 137
   Neo4j official MCP Server

1141. **[eion](https://github.com/eiondb/eion)** - ⭐ 136
   Shared Memory Storage for Multi-Agent Systems

1142. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 136
   MCP server for discord bot

1143. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 136
   StarRocks MCP (Model Context Protocol) Server

1144. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 136
   MCP Server for Google Slides

1145. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 136
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1146. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 135
   MCP server for seamless document format conversion and processing

1147. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 135
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1148. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1149. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 134
   An MCP server implementing the think tool for Claude

1150. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 134
   Fastest way to build multi-agent system, agent-to-agent communication, MCPs, production ready serverless environment.

1151. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 134
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1152. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 134
   Persistent AI memory for coding assistants - MCP server providing context persistence across sessions for Claude, Cursor, Windsurf.  MCP Tools for task tracking, workflow automation, and AI memory. Eliminates context loss between sessions.

1153. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 134
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1154. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 134
   Persistent Intelligence Infrastructure for AI Agents

1155. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 133
   MSSQL Server MCP implementation written in C#

1156. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1157. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 133
   Dynamically expose tools from proxied servers based on an Agent Persona

1158. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 132
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1159. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 132
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1160. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 132
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1161. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 132
   Serper MCP Server supporting search and webpage scraping

1162. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 132
   A simple CLI to install MCP servers into any client - auth included!

1163. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 132
   MCP server for AutoCAD LT: AI agents translate natural language into AutoLISP code for geometry, 600+ ISA 5.1 P&ID symbols, block attributes, and layer management—generating technical drawings with 80% performance improvement via batch operations.

1164. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 132
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1165. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 131
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1166. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 131
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1167. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 131
   mcp server for gitingest

1168. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 131
   Graphiti MCP Server

1169. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 131
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1170. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 131
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1171. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 130
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1172. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 130
   Manage Your Kubernetes Cluster with k8s mcp-server

1173. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 130
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1174. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 129
   The Ultimate Model Context Protocol (MCP) Server, providing unified access to a wide variety of useful and powerful tools.

1175. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 129
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1176. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 129
   DataForSEO API modelcontextprotocol server 

1177. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 129
   Connect your AI to your APIs on Postman

1178. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 129

1179. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 129
   The Logfire MCP Server is here! :tada:

1180. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 129
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1181. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 129
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1182. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 128
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1183. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 128
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1184. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 128
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1185. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 128
   MCP server for understanding AWS spend

1186. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 128
   A collection of crypto MCP servers.

1187. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 128
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1188. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 127
   A Model Context Protocol server implementation for operations on AWS resources

1189. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 127
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1190. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 127
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1191. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 127
   FrontMCP Framework

1192. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 126
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1193. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 126
   JetBrains MCP Server Plugin

1194. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 126
   MCP server to access Garmin data

1195. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 126

1196. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 126
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1197. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 125
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1198. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 125
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1199. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 125
   IMAP and SMTP via MCP Server

1200. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 125
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1201. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 125
   A local Apple Documentation crawler and MCP server. Written in Swift.

1202. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1203. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 124
   Model Context Protocol (MCP) server for the Zotero API, in Python

1204. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 124
   Dart AI Model Context Protocol (MCP) server

1205. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 124
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1206. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 124
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1207. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 124
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1208. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1209. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 124
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1210. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 123
   Buttplug.io Model Context Protocol (MCP) Server

1211. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 123
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1212. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 123
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1213. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 123
   High-performance CCXT MCP server for cryptocurrency exchange integration

1214. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 123

1215. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 123
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1216. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 123
   🚀🎬 Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1217. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 122
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1218. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 122
   Intelligent spec workflow management MCP server

1219. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 122
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1220. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 122
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1221. **[magg](https://github.com/sitbon/magg)** - ⭐ 122
   Magg: The MCP Aggregator

1222. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 121
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1223. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 121
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1224. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 121

1225. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 121
   a private MCP server for accessing Linear

1226. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 121
   An MCP Server for Ollama

1227. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 121
   🐉 The fast, PHP way to build MCP servers

1228. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 121
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1229. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 121
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1230. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 120
   A Model Context Protocol server that provides access to BigQuery

1231. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 120
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1232. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 120
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1233. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 120
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1234. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 120
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1235. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 120
   MCP Servers SDK for TypeScript

1236. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 120
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1237. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 119
   MCP server implementation for n8n workflow automation

1238. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 119
   MCP server for Unreal Engine 5

1239. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 118
   Model Context Protocol (MCP) with TikTok integration

1240. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 118
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1241. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 117
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1242. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 113
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

1243. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 113
   A Model Context Protocol (MCP) for Jupyter Notebook

1244. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 113
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1245. **[cli](https://github.com/mcpgod/cli)** - ⭐ 112
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1246. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 112
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1247. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 112
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1248. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 111
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1249. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 110
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1250. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1251. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1252. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 110
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1253. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 110
   MariaDB MCP (Model Context Protocol) server implementation

1254. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 109
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1255. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 109
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1256. **[modex](https://github.com/theronic/modex)** - ⭐ 108
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1257. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 108
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1258. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 108
   Model Context Protocol Server for Swift

1259. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 107
   A Model Context Protocol Server to manipulate *.xcodeproj

1260. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 107
   Production-grade TypeScript template for Model Context Protocol (MCP) servers. Ships with declarative tools/resources, robust error handling, DI, easy auth, optional OpenTelemetry, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1261. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 106
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1262. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 106
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1263. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 105
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1264. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 105
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1265. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 105
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1266. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 104
   simple web ui to manage mcp (model context protocol) servers in the claude app

1267. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 104
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1268. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 104
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1269. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 103
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1270. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 103
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1271. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1272. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 102
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1273. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 102
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1274. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 101
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1275. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 101
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1276. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 101
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1277. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 100
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1278. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 100
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1279. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 99
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1280. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 99
   Collection of examples of how to use Model Context Protocol with AWS.

1281. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1282. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 98
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1283. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 98
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1284. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 97
   💎 A Ruby implementation of the Model Context Protocol

1285. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 97
   Node.js Client Implementation for Model Context Protocol (MCP)

1286. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 97
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1287. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 97
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1288. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 97
   A Google Tasks Model Context Protocol Server for Claude

1289. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 97
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1290. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 96
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1291. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 96
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1292. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 95
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1293. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 95
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1294. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 95
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1295. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 94
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1296. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 94
   Model Context Protocol (MCP) server for the Webflow Data API.

1297. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1298. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 93
   This is a Ruby implementation of MCP (Model Context Protocol) client

1299. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 92
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1300. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 92
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1301. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 92
   Model Context Protocol server for Replicate's API

1302. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 92
   A Model Context Protocol (MCP) server providing access to Google Search Console

1303. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 92
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1304. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 91
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1305. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for square

1306. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 90
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1307. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 90
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1308. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 89
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1309. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 89
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1310. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 89
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1311. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 89
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1312. **[mcp-web-ui](https://github.com/MegaGrindStone/mcp-web-ui)** - ⭐ 87
   MCP Web UI is a web-based user interface that serves as a Host within the Model Context Protocol (MCP) architecture. It provides a powerful and user-friendly interface for interacting with Large Language Models (LLMs) while managing context aggregation and coordination between clients and servers.

1313. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 87
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1314. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 87
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1315. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 86
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1316. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 86
   A model-context-protocol server for molecules.

1317. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 86
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1318. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1319. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 85
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1320. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 84
   Ragie Model Context Protocol Server

1321. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 84
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1322. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 83
   A Model Context Protocol server that provides knowledge graph management capabilities.

1323. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 83
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1324. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 83
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1325. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1326. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 81
   Model Context Protocol (MCP) CLI server template for Rust

1327. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1328. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1329. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 80
   Model Context Protocol (MCP) Server for the Keboola Platform

1330. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 80
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1331. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 79
   A model context protocol server that connects to Anki through AnkiConnect

1332. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 79
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1333. **[identity](https://github.com/agntcy/identity)** - ⭐ 79
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1334. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 79
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1335. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 78
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1336. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 78
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1337. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 78
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1338. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 78
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1339. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 78
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1340. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 78
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1341. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 78
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1342. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 77
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1343. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 77
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1344. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 77
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1345. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 77
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1346. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 75
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1347. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 75
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1348. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 75
   Model Context Protocol (MCP) Client for Apify's Actors

1349. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 75
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1350. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 75
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1351. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 75
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1352. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 74
   A Model Context Protocol Server to perform Kafka client operations

1353. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 74
   A WooCommerce (MCP) Model Context Protocol server

1354. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 74
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1355. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 74
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1356. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 73
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1357. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 72
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1358. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 72
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1359. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 72
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1360. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 71
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1361. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 70
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1362. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

1363. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 70
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1364. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 70
   Model Context Protocol for Actual Budget API

1365. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 69
   Model Context Protocol implementation for retrieving codebases using RepoMix

1366. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 69
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1367. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 69
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1368. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 69
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1369. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 69
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1370. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 68
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

1371. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 68
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1372. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 68
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1373. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 68
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1374. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 68
   A Model Context Protocol server for Hopper Disassembler

1375. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 68
   An extensible Model Context Protocol (MCP) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search research.

1376. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

1377. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

1378. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 67
   Model Context Protocol (MCP) server for Gmail

1379. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 67
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

1380. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

1381. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 67
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

1382. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 66
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

1383. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 66
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1384. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 66
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1385. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 66
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

1386. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 66
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1387. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 65
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

1388. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 65
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

1389. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 65
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

1390. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 65
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

1391. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 65
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

1392. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 65
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1393. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 65
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

1394. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 65
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1395. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 65
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1396. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 65
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1397. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 64
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1398. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

1399. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 64
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

1400. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 64
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1401. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 64
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

1402. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 63
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

1403. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 63
   Model Context Protocol(MCP) 中文教程讲解

1404. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 63
   A Model Context Protocol implementation for FHIR

1405. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1406. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 62
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

1407. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 62
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

1408. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 62
   Model Context Protocol for x64dbg & x32dbg

1409. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

1410. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 61
   Model Context Protocol server and client for R

1411. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 61
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

1412. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 61
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

1413. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 61
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

1414. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 60
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

1415. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 60
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

1416. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 60
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

1417. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 60
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

1418. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 60
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1419. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 60
   Index of all Model Context Protocol (MCP) clients and their capabilities

1420. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 59
   Miro integration for Model Context Protocol

1421. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

1422. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server for Rember.

1423. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 59
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

1424. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1425. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 58
   A curated list of awesome Model Context Protocol (MCP) servers.

1426. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

1427. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 58
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1428. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 58
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1429. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 57
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

1430. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 57
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

1431. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 57
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

1432. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 57
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

1433. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 57
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

1434. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 57
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1435. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 57
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

1436. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

1437. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

1438. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 56
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

1439. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 56
   Model Context Protocol for YNAB (you need a budget)

1440. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 55
   A model context protocol  (MCP) server for Umbraco 

1441. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 55
   MKP is a Model Context Protocol (MCP) server for Kubernetes

1442. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 55
   A Model Context Protocol server for Ashra

1443. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 55
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

1444. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 55
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

1445. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

1446. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

1447. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 54
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

1448. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 53
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

1449. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 53
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

1450. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 53
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

1451. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 53
   A Model Context Protocol (MCP) server for Microsoft Clarity

1452. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 53
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

1453. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 53
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

1454. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 52
   Model Context Protocol Servers for Azure AI Search

1455. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 52
   Unofficial Golang SDK for Anthropic Model Context Protocol

1456. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 52
   A Nasdaq Data Link MCP (Model Context Protocol) Server

1457. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 52
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

1458. **[client](https://github.com/php-mcp/client)** - ⭐ 52
   Core PHP implementation for the Model Context Protocol (MCP) Client

1459. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 52
   MCP (Model Context Protocol) server plugin for CAP NodeJS

1460. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 52
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

1461. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

1462. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 52
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

1463. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 51
   OCaml implementation of the Model Context Protocol (MCP)

1464. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 51
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

1465. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 51
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1466. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 51
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

1467. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 51
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

1468. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 51
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

1469. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 51
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1470. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

1471. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 50
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

1472. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 50
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

1473. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 50
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

1474. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 50
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

1475. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 50
   ABAP MCP - Model Context Protocol - Server SDK

1476. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 49
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

1477. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 49
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

1478. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 49
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

1479. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 49
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

1480. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 49
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

1481. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 49
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

1482. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 49
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

1483. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 49
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

1484. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 49
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

1485. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 49
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

1486. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 49
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

1487. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 48
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

1488. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 48
   Anthropic’s Model Context Protocol implementation for Oat++

1489. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

1490. **[mcp](https://github.com/goplus/mcp)** - ⭐ 48
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

1491. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 48
   A Model Context Protocol server that validates and renders Mermaid diagrams.

1492. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 48
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

1493. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 48
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

1494. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

1495. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 48
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

1496. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

1497. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 47
   An implementation of the Model Context Protocol in Ruby.

1498. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

1499. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 47
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

1500. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 47
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

1501. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 47
   vMCP - Virtual Model Context Protocol

1502. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 47
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

1503. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 47
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1504. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 46
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

1505. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 46
   Inkdrop Model Context Protocol Server

1506. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 46
   OpenAPI Schema Model Context Protocol Server

1507. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 46
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

1508. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 46
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

1509. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 46
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

1510. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 46
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

1511. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 46
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

1512. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 46
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

1513. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 46
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

1514. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

1515. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

1516. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

1517. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

1518. **[go-mcp](https://github.com/MegaGrindStone/go-mcp)** - ⭐ 45
   A Go implementation of the Model Context Protocol (MCP) - an open protocol that enables seamless integration between LLM applications and external data sources and tools.

1519. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 45
   A Model-Context-Protocol (MCP) Server for Active Directory

1520. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 45
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

1521. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 45
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

1522. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 45
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

1523. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

1524. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 45
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

1525. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

1526. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 45
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

1527. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 45
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

1528. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 44
   Model Context Protocol to fetch youtube transcript

1529. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 44
   Model Context Protocol server for Flight Tracking

1530. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

1531. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 44
   📚 An intelligent toolkit to automatically parse, complete, and format academic references, with Model Context Protocol (MCP) support.

1532. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

1533. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 44
   An opinionated starter template for making Model Context Protocol (MCP) servers

1534. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 44
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

1535. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 44
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

1536. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 44
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

1537. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 44
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

1538. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 44
   A Model Context Protocol server for Zendesk

1539. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

1540. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 43
   Model Context Protocol for WeChat

1541. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 43
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

1542. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 43
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

1543. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

1544. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 43
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

1545. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 43
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

1546. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 43
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

1547. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 43
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

1548. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 43
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

1549. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

1550. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 42
   Model Context Protocol server for Salesforce REST API integration

1551. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 42
   GraphQL Schema Model Context Protocol Server

1552. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

1553. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

1554. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 42
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

1555. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 42
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

1556. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 42
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

1557. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

1558. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 42
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

1559. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 42
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

1560. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 42
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

1561. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 42
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

1562. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 42
   Amadeus MCP(Model Context Protocol) Server

1563. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 42
   An implementation of the Model Context Protocol for the World Bank open data API

1564. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 42
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

1565. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 42
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

1566. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 42
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

1567. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 42
   A Model Context Protocol server implementation for Kagi's API

1568. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 42
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

1569. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 41
   A generic, modular server for implementing the Model Context Protocol (MCP). 

1570. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 41
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

1571. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 41
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

1572. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

1573. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   An MCP (Model Context Protocol) server that enables ✨ AI platforms to interact with 🤖 YepCode's infrastructure.  Turn your YepCode processes into powerful tools that AI assistants can use 🚀

1574. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 41
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

1575. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 41
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

1576. **[mcp](https://github.com/40ants/mcp)** - ⭐ 41
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

1577. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 41
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

1578. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 41
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

1579. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 41
   A Model Context Protocol server for Go developers

1580. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 40
   A production-ready Model Context Protocol (MCP) server for semantic memory management

1581. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 40
   A Model Context Protocol server for Dify

1582. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 40
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

1583. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

1584. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

1585. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

1586. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 40
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

1587. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

1588. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

1589. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 40
   MCP (Model Context Protocol) server for the Contentful Management API

1590. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 40
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

1591. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 40
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

1592. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 40
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

1593. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 40
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

1594. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 40
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

1595. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

1596. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

1597. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

1598. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 40
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

1599. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 40
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

1600. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 40
   Model Context Protocol Clojure support including REPL integration with development tools.

1601. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 39
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

1602. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

1603. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 39
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

1604. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

1605. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 39
   Model Context Protocol server for OpenStreetMap data

1606. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 39
   Implementation of Model Context Protocol server for Mailgun APIs

1607. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 39
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

1608. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 39
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

1609. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 39
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

1610. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

1611. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 39
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

1612. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 39
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

1613. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 39
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

1614. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 39
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1615. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 38
   Algorand Model Context Protocol (Server & Client)

1616. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 38
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

1617. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 38
   It shows how to use model-context-protocol. 

1618. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

1619. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 38
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

1620. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

1621. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 38
   Build tools for LLMs in Rust using Model Context Protocol

1622. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 38
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

1623. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 38
   A Model Context Protocol (MCP) Server providing LLM tools for the official ClinicalTrials.gov REST API. Search and retrieve clinical trial data, including study details and more

1624. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 38
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

1625. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 38
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

1626. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 38
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

1627. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

1628. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 37
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

1629. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 37
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

1630. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

1631. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 37
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

1632. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 37
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

1633. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 37
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

1634. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 37
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

1635. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 37
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

1636. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 37
   Attio Model Context Protocol (MCP) server implementation

1637. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 37
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

1638. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 37
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

1639. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 37
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

1640. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 37
   Model Context Protocol server for Sitecore

1641. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 36
   OpenAI Code Assistant Model Context Protocol (MCP) Server

1642. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 36
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

1643. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

1644. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 36
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

1645. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

1646. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

1647. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

1648. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 36
   Model Context Protocol Minecraft Server

1649. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 36
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

1650. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 36
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

1651. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 36
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

1652. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

1653. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 36
   A Model Context Protocol server that provides access to Shodan API functionality

1654. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 36
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

1655. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 36
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

1656. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 36
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

1657. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 36
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

1658. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

1659. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 35
   Bluesky MCP (Model Context Protocol) Server

1660. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 35
   Model Context Protocol (MCP) implementation for iOS simulators

1661. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

1662. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 35
   Model Context Protocol server to let LLMs write and execute matlab scripts 

1663. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 35
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

1664. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

1665. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 35
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

1666. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 35
   Privacy-first local RAG server for Cursor, Claude Code, and more — powered by the Model Context Protocol.

1667. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 35
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

1668. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 35
   A Model Context Protocol for checking domain name registration status in bulk.

1669. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 35
   Model Context Protocol server for ActivityWatch time tracking data

1670. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 35
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

1671. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 35
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1672. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 34
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

1673. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 34
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

1674. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 34
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

1675. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 34
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

1676. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 34
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

1677. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 34
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

1678. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 34
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

1679. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

1680. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 34
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

1681. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

1682. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 34
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

1683. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 34
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

1684. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 34
   Model Context Protocol (MCP) Server for Mistral OCR API

1685. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 34
   Model Context Protocol (MCP) server for LinkedIn API integration

1686. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 34
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

1687. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 34
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

1688. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 33
   Model Context Protocol server written in Scala

1689. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 33
   Model Context Protocol Server for Apache OpenDAL™

1690. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 33
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

1691. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

1692. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 33
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

1693. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

1694. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 33
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

1695. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

1696. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 33
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

1697. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 33
   IMAP Model Context Protocol server for interactive email processing

1698. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 33
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

1699. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

1700. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 33
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

1701. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 33
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

1702. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 33
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

1703. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 32
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

1704. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 32
   A Model Context Protocol (MCP) server for NATS messaging system integration

1705. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 32
   Model Context Protocol (MCP) server implementation for Autodesk Maya

1706. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

1707. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

1708. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 32
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

1709. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 32
   A powerful Model Context Protocol server for LinkedIn API integration

1710. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 32
   Altium Model Context Protocol server and Altium API script

1711. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 32
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

1712. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

1713. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 32
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

1714. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

1715. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 32
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

1716. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 32
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

1717. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 31
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

1718. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 31
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

1719. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

1720. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 31
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

1721. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 31
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

1722. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 31
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

1723. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 31
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

1724. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 31
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

1725. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

1726. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

1727. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 31
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

1728. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 31
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

1729. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 31
   About A Model Context Protocol server that executes commands in the current WezTerm session

1730. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 31
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

1731. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 31
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

1732. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 31
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

1733. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 31
   Claude Unified Model Context Interaction Protocol

1734. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

1735. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

1736. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 30
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

1737. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 30
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

1738. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 30
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

1739. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 30
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

1740. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

1741. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 30
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

1742. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

1743. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 30
   Model Context Protocol (MCP) server for openBIM

1744. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 30
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

1745. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 30
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

1746. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 30
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

1747. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 30
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

1748. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 30
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

1749. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 30
   Emacs Lisp implementation of the Model Context Protocol

1750. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 30
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

1751. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 30
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

1752. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 30
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

1753. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 30
   Model Context Server Protocol for your HANA DB

1754. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 30
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

1755. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 29
   A Model Context Protocol server starter template

1756. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

1757. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 29
   Model Context Protocol server for Cyclops

1758. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

1759. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 29
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

1760. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 29
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

1761. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 29
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

1762. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

1763. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 29
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

1764. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

1765. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 29
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

1766. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

1767. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 29
   Model Context Protocol (MCP) server that interacts with a Debugger

1768. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 29
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

1769. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 29
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

1770. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 29
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

1771. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 29
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

1772. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 29
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

1773. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 29
   Sync MCP (Model Context Protocol) configurations across AI tools

1774. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

1775. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

1776. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

1777. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 28
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

1778. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

1779. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 28
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

1780. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 28
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

1781. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 28
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

1782. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 28
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

1783. **[mcp](https://github.com/fastly/mcp)** - ⭐ 28
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

1784. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

1785. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 28
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

1786. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 28
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

1787. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 28
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

1788. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 28
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

1789. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 28
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

1790. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 28
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

1791. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 28
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

1792. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 27
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

1793. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

1794. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 27
   Model Context Protocol Server of Rod

1795. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 27
   Asterisk Model Context Protocol (MCP) server.

1796. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 27
   MCP (Model Context Protocol) server for biothings

1797. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 27
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

1798. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

1799. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

1800. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

1801. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 27
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

1802. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

1803. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

1804. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 27
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

1805. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 27
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

1806. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 27
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

1807. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 27
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

1808. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 27
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

1809. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 27
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

1810. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 27
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

1811. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 27
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

1812. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

1813. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 27
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

1814. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 27
   A Model Context Protocol (MCP) server for Polymarket prediction markets, providing real-time market data, prices, and AI-powered analysis tools for Claude Desktop integration.

1815. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

1816. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

1817. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 26
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

1818. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

1819. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 26
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

1820. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 26
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

1821. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

1822. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 26
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

1823. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 26
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

1824. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 26
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

1825. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 26
   An implementation of Giphy integration with Model Context Protocol

1826. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 26
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

1827. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

1828. **[mcp-advisor](https://github.com/olaservo/mcp-advisor)** - ⭐ 26
   MCP Server to assist LLMs and humans on Model Context Protocol spec compliance and understanding

1829. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 26
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

1830. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 26
   MCP (Model Context Protocol) Server for postgres Database

1831. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 26
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

1832. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 26
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

1833. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

1834. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

1835. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 25
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

1836. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

1837. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

1838. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 25
   Model Context Protocol to bridge in Substack writings to Claude.

1839. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

1840. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 25
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

1841. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

1842. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

1843. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 25
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

1844. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 25
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

1845. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 25
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

1846. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 25
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

1847. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

1848. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 25
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

1849. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 25
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

1850. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 25
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

1851. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 25
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

1852. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 25
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

1853. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 25
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

1854. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 25
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

1855. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 25
   Learn Model Context Protocol with Python, published by Packt

1856. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 25
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

1857. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 25
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

1858. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

1859. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 24
   A Model Context Protocol Server for Interacting with Slack

1860. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

1861. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 24
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

1862. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

1863. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 24
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

1864. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

1865. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

1866. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 24
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

1867. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

1868. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

1869. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 24
   Model Context Protocol Server for NebulaGraph 3.x

1870. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

1871. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 24
   A simple Model Context Protocol (MCP) server for Clay.

1872. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

1873. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 24
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

1874. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 24
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

1875. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 24
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

1876. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 24
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

1877. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 24
   Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from data.gouv.fr, the French national Open Data platform, directly through conversation.

1878. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 24
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

1879. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

1880. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 24
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

1881. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 24
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

1882. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

1883. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 24
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

1884. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 24
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

1885. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 24
   Headless IDA Pro binary analysis via Model Context Protocol

1886. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

1887. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 23
   A Model Context Protocol (MCP) server for GreptimeDB

1888. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 23
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

1889. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

1890. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 23
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

1891. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 23
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

1892. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 23
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

1893. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 23
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

1894. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

1895. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 23
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

1896. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

1897. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 23
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

1898. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

1899. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 23
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

1900. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

1901. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

1902. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 23
   A Fastify plugin to run Model Context Protocol (MCP) servers

1903. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 23
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

1904. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 23
   Model Context Protocol SDK implemented in Lua for OpenResty

1905. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 23
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

1906. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 23
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

1907. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 23
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

1908. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

1909. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 23
   A Model Context Protocol server for 3D Slicer integration

1910. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 23
   ElysiaJS plugin for Model Context Protocol with HTTP transport

1911. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 23
   PowerPlatform Model Context Protocol server

1912. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 23
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

1913. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

1914. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 22
   A MCP(Model Context Protocol) server that accesses to Lightdash

1915. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 22
   A personal assistant AI agent built with the Model Context Protocol (MCP)

1916. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

1917. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

1918. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

1919. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

1920. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

1921. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 22
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

1922. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

1923. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

1924. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 22
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

1925. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

1926. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

1927. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 22
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

1928. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 22
   Python-based MCP server for BlazeMeter API — orchestrate performance-test lifecycle (create, configure, run, analyze) and manage tests, workspaces, projects & accounts via Model Context Protocol

1929. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

1930. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 22
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

1931. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 22
   Model Context Protocol server for querying Cursor chat history

1932. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 22
   model context protocol for Autodesk Revit

1933. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 22
   Model Context Protocol server for Github Repo // Reading Github Repo

1934. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 22
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

1935. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 22
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

1936. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

1937. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

1938. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

1939. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 22
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

1940. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 22
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

1941. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 22
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1942. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

1943. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

1944. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

1945. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 21
   MCP (model context protocol) server for interacting with dbt Docs

1946. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

1947. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

1948. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 21
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

1949. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

1950. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 21
   Zillow MCP Server for real estate data access via the Model Context Protocol

1951. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

1952. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 21
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

1953. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

1954. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 21
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

1955. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

1956. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

1957. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 40,364
   基于大模型搭建的聊天机器人，同时支持 微信公众号、企业微信应用、飞书、钉钉 等接入，可选择ChatGPT/Claude/DeepSeek/文心一言/讯飞星火/通义千问/ Gemini/GLM-4/Kimi/LinkAI，能处理文本、语音和图片，访问操作系统和互联网，支持基于自有知识库进行定制企业智能客服。

2. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 14,997
   AgentScope: Agent-Oriented Programming for Building LLM Applications

3. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,083
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

4. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 7,836
   ValueCell is a community-driven, multi-agent platform for financial applications.

5. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,258
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

6. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,597
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

7. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,576
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

8. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,315
   extendable code review and QA agent 🚢

9. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,633

10. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,575
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

11. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 855
   ChatGPT CLI is a versatile tool for interacting with LLMs through OpenAI, Azure, and other popular providers like Perplexity AI and Llama. It supports prompt files, history tracking, and live data injection via MCP (Model Context Protocol), making it ideal for both casual users and developers seeking a powerful, customizable GPT experience.

12. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 787
   OpenTelemetry Instrumentation for AI Observability

13. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 760
   A code repository indexing tool to supercharge your LLM experience.

14. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 704
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

15. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 579
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

16. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 545
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

17. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 531
   The easiest way to discover and install MCPs

18. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 530
   VoiceMode MCP brings natural conversations to Claude Code

19. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 391
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

20. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 322
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

21. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 252
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

22. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 94
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

23. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

24. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 165,660
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,463
   🦍 The Cloud-Native Gateway for APIs & AI

3. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 40,896
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement for OpenAI,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

4. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 26,734
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

5. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,277
   Your ultimate Go microservices framework for the cloud-native era.

6. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,141
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

7. **[plate](https://github.com/udecode/plate)** - ⭐ 15,687
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 14,626
   ✨ Agentic IM ChatBot Infrastructure — 聊天智能体基础设施 ✨ 多消息平台集成（QQ / 企微 / 飞书 / 钉钉 / Discord 等），强大易用的插件系统，支持 OpenAI / Gemini / Anthropic / Dify / Coze / 阿里云百炼 / 知识库 / Agent 智能体

9. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

10. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

11. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,436
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

12. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,341
   A cross-platform Markdown AI note-taking software.

13. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,178
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

14. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,313
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

15. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 8,305
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,739
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,506
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[adk-go](https://github.com/google/adk-go)** - ⭐ 6,505
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

19. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 6,444
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

20. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,630
   Adversary simulation and Red teaming platform with AI

21. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,424
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,139
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,103
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

24. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 3,996
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/pAbnFJrkgZ

25. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 3,633
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

26. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,247
   Shadcn/ui components library for building ChatGPT Apps

27. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,686
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

28. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 2,612
   System Level Intelligent Router for Mixture-of-Models

29. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,458
   A highly opinionated, zero-configuration linter and formatter.

30. **[harbor](https://github.com/av/harbor)** - ⭐ 2,213
   Effortlessly run LLM backends, APIs, frontends, and services with one command.

31. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,860
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

32. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,704
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

33. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,693
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

34. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,450
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

35. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,404
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

36. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

37. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,273
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

38. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,257
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

39. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,217
   Paper Debugger is the best overleaf companion

40. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,085
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

41. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,057
   A single interface to use and evaluate different agent frameworks 

42. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,057
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

43. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 992
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

44. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 973
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

45. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 973
   AIPex: AI browser automation assistant, no migration and privacy first. ChatGPT Atlas Alternative, Alternative to Manus Browser Operator, Alternative to Claude Chrome

46. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 950
   Arduino MCP2515 CAN interface library

47. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 948
   Korea Investment & Securities Open API Github

48. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 760
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

49. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 724
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

50. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 692
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

51. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 689
   Solidity Static Analyzer that easily integrates into your editor

52. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 683
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

53. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 646
   A personal AI assistant for everyone

54. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 612
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

55. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 578
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

56. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 476
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

57. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 449
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

58. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

59. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 421
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

60. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 400
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

61. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 383
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

62. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 382
   Minecraft: Pi Edition API Python Library

63. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 376
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

64. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 376
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

65. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 374
   Arduino Library for Adafruit MCP23017

66. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 352
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

67. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 342
   Python toolkit for building graph-enhanced GenAI applications

68. **[exograph](https://github.com/exograph/exograph)** - ⭐ 339
   Build production-ready backends in minutes

69. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 333
   Blender python addon to increase workflow for creating minecraft renders and animations

70. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 329
   MCP for Unreal Engine 5

71. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 329
   Don't search your code. Research it.

72. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

73. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 317
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

74. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 308
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

75. **[depyler](https://github.com/paiml/depyler)** - ⭐ 295
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

76. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 292
   Software architecture tooling for the AI age

77. **[amical](https://github.com/amicalhq/amical)** - ⭐ 288
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

78. **[edumcp](https://github.com/aieducations/edumcp)** - ⭐ 265
   EDUMCP is a protocol that integrates the Model Context Protocol (MCP) with applications in the education field, dedicated to achieving seamless interconnection and interoperability among different AI models, educational applications, smart hardware, and teaching AGENTs.

79. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 263
   An in-depth book and reference on building agentic systems like Claude Code

80. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

81. **[MCPMappingViewer](https://github.com/bspkrs/MCPMappingViewer)** - ⭐ 243
   A small GUI for viewing the mappings from Minecraft obfuscated code names to MCP code names.

82. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 241
   AI for Ethical Hacking - Workshop

83. **[MCPConfig](https://github.com/MinecraftForge/MCPConfig)** - ⭐ 238
   Public facing repo for MCP SRG mappings.

84. **[MCP-Defender](https://github.com/MCP-Defender/MCP-Defender)** - ⭐ 236
   Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor, Claude, VS Code and Windsurf.

85. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 232
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

86. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 230
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

87. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 229
   An IOS Simulator Skill for ClaudeCode. Also contains skills for building your Xcode project, and optimises sim screenshots before passing to your agent, but navigates via accessibility if available.

88. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 226
   An introduction to the world of AI Agents

89. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 225
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

90. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 219
   A website to generate Minecraft profile pictures

91. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

92. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 211
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

93. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 208
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

94. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 200
   Re-usable multi part components built on React Aria and TailwindCSS. 

95. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

96. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

97. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 185
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

98. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 183
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

99. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

100. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 63
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

101. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 47
   Houdini integration through the Model Context Protocol

102. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

103. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

104. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 24
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具与 Wireshark 进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

105. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 22
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,614
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

### Documentation

*Documentation, tutorials, and learning resources*

1. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 6,764
   Specification and documentation for the Model Context Protocol

2. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,848
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，支持 MCP 调用，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

3. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 914
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

