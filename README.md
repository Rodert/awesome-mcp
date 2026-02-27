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

## 📚 Projects (3846 total)

> Last updated: **2026-02-27**

### MCP Servers

*MCP server implementations that provide protocol services*

1. **[dify](https://github.com/langgenius/dify)** - ⭐ 130,515
   Production-ready platform for agentic workflow development.

2. **[open-webui](https://github.com/open-webui/open-webui)** - ⭐ 125,097
   User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

3. **[gemini-cli](https://github.com/google-gemini/gemini-cli)** - ⭐ 95,840
   An open-source AI agent that brings the power of Gemini directly into your terminal.

4. **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** - ⭐ 81,684
   A collection of MCP servers.

5. **[servers](https://github.com/modelcontextprotocol/servers)** - ⭐ 79,519
   Model Context Protocol Servers

6. **[netdata](https://github.com/netdata/netdata)** - ⭐ 77,899
   The fastest path to AI-powered full stack observability, even for lean teams.

7. **[ragflow](https://github.com/infiniflow/ragflow)** - ⭐ 73,814
   RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

8. **[lobehub](https://github.com/lobehub/lobehub)** - ⭐ 72,719
   The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

9. **[lobe-chat](https://github.com/lobehub/lobe-chat)** - ⭐ 70,553
   :exploding_head: LobeHub - The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

10. **[anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - ⭐ 55,104
   The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

11. **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** - ⭐ 53,620
   Complete Claude Code configuration collection - agents, skills, hooks, commands, rules, MCPs. Battle-tested configs from an Anthropic hackathon winner.

12. **[TrendRadar](https://github.com/sansan0/TrendRadar)** - ⭐ 47,427
   ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。

13. **[context7](https://github.com/upstash/context7)** - ⭐ 47,067
   Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

14. **[JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** - ⭐ 45,281
   【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

15. **[LocalAI](https://github.com/mudler/LocalAI)** - ⭐ 43,101
   :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

16. **[mindsdb](https://github.com/mindsdb/mindsdb)** - ⭐ 38,590
   Federated Query Engine for AI - The only MCP Server you'll ever need

17. **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** - ⭐ 38,237
   A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

18. **[cherry-studio](https://github.com/CherryHQ/cherry-studio)** - ⭐ 37,347
   Cherry Studio boosts your productivity with unified AI access, Agent capabilities, and 300+ assistants in one desktop application.

19. **[LibreChat](https://github.com/danny-avila/LibreChat)** - ⭐ 34,166
   Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

20. **[1Panel](https://github.com/1Panel-dev/1Panel)** - ⭐ 33,113
   🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server.

21. **[nacos](https://github.com/alibaba/nacos)** - ⭐ 32,662
   an easy-to-use dynamic service discovery, configuration and service management platform for building AI cloud native applications.

22. **[PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)** - ⭐ 31,923
   [EMNLP 2025 Demo] PDF scientific paper translation with preserved formats - 基于 AI 完整保留排版的 PDF 文档全文双语翻译，支持 Google/DeepL/Ollama/OpenAI 等服务，提供 CLI/GUI/MCP/Docker/Zotero

23. **[goose](https://github.com/block/goose)** - ⭐ 31,328
   an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

24. **[ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** - ⭐ 30,791
   In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

25. **[UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)** - ⭐ 28,341
   The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

26. **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** - ⭐ 27,782
   Playwright MCP server

27. **[github-mcp-server](https://github.com/github/github-mcp-server)** - ⭐ 27,287
   GitHub's official MCP Server

28. **[composio](https://github.com/ComposioHQ/composio)** - ⭐ 27,201
   Composio powers 1000+ toolkits, tool search, context management, authentication, and a sandboxed workbench to help you build AI agents that turn intent into action.

29. **[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** - ⭐ 26,854
   Chrome DevTools for coding agents

30. **[gpt-researcher](https://github.com/assafelovic/gpt-researcher)** - ⭐ 25,452
   An autonomous agent that conducts deep research on any data using any LLM providers.

31. **[gin-vue-admin](https://github.com/flipped-aurora/gin-vue-admin)** - ⭐ 24,344
   🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

32. **[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** - ⭐ 24,256
   An MCP-based chatbot | 一个基于MCP的聊天机器人

33. **[fastmcp](https://github.com/PrefectHQ/fastmcp)** - ⭐ 23,198
   🚀 The fast, Pythonic way to build MCP servers and clients.

34. **[fastmcp](https://github.com/jlowin/fastmcp)** - ⭐ 22,902
   🚀 The fast, Pythonic way to build MCP servers and clients

35. **[repomix](https://github.com/yamadashy/repomix)** - ⭐ 22,118
   📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

36. **[python-sdk](https://github.com/modelcontextprotocol/python-sdk)** - ⭐ 21,857
   The official Python SDK for Model Context Protocol servers and clients

37. **[mastra](https://github.com/mastra-ai/mastra)** - ⭐ 21,464
   From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

38. **[activepieces](https://github.com/activepieces/activepieces)** - ⭐ 20,976
   AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents

39. **[cc-switch](https://github.com/farion1231/cc-switch)** - ⭐ 20,962
   A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode & Gemini CLI.

40. **[serena](https://github.com/oraios/serena)** - ⭐ 20,715
   A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

41. **[MaxKB](https://github.com/1Panel-dev/MaxKB)** - ⭐ 20,179
   🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。

42. **[blender-mcp](https://github.com/ahujasid/blender-mcp)** - ⭐ 17,366

43. **[Scrapling](https://github.com/D4Vinci/Scrapling)** - ⭐ 17,130
   🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

44. **[agentscope](https://github.com/agentscope-ai/agentscope)** - ⭐ 16,531
   Build and run agents you can see, understand and trust.

45. **[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** - ⭐ 16,180
   The Ultimate Collection of 900+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

46. **[claude-flow](https://github.com/ruvnet/claude-flow)** - ⭐ 15,103
   🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

47. **[mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** - ⭐ 14,499
   This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration.

48. **[n8n-mcp](https://github.com/czlonkowski/n8n-mcp)** - ⭐ 14,045
   A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you 

49. **[trigger.dev](https://github.com/triggerdotdev/trigger.dev)** - ⭐ 13,874
   Trigger.dev – build and deploy fully‑managed AI agents and workflows

50. **[electerm](https://github.com/electerm/electerm)** - ⭐ 13,641
   📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(linux, mac, win)

51. **[filestash](https://github.com/mickael-kerjean/filestash)** - ⭐ 13,423
   :file_folder: What Dropbox should have been if it was based on SFTP, S3, FTP, SMB, NFS, WebDAV, Git, and more

52. **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - ⭐ 13,416
   Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

53. **[Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** - ⭐ 13,274
   MCP server to provide Figma layout information to AI coding agents like Cursor

54. **[genai-toolbox](https://github.com/googleapis/genai-toolbox)** - ⭐ 13,196
   MCP Toolbox for Databases is an open source MCP server for databases.

55. **[casdoor](https://github.com/casdoor/casdoor)** - ⭐ 13,076
   An open-source AI-first Identity and Access Management (IAM) /AI MCP gateway and auth server with web UI supporting MCP, A2A, OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD

56. **[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)** - ⭐ 11,683
   The official TypeScript SDK for Model Context Protocol servers and clients

57. **[fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)** - ⭐ 11,595
   Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth!

58. **[pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** - ⭐ 11,146
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

59. **[memU](https://github.com/NevaMind-AI/memU)** - ⭐ 11,119
   Memory for 24/7 proactive agents like openclaw (moltbot, clawdbot).

60. **[nginx-ui](https://github.com/0xJacky/nginx-ui)** - ⭐ 10,744
   Yet another WebUI for Nginx

61. **[gateway](https://github.com/Portkey-AI/gateway)** - ⭐ 10,726
   A blazing fast AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

62. **[mcp-chrome](https://github.com/hangwin/mcp-chrome)** - ⭐ 10,508
   Chrome MCP Server is a Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants like Claude, enabling complex browser automation, content analysis, and semantic search.

63. **[XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader)** - ⭐ 10,186
   小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件

64. **[Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)** - ⭐ 9,919
   Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection

65. **[zen-mcp-server](https://github.com/BeehiveInnovations/zen-mcp-server)** - ⭐ 9,890
   The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

66. **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** - ⭐ 9,374
   MCP for xiaohongshu.com

67. **[mcp-use](https://github.com/mcp-use/mcp-use)** - ⭐ 9,288
   The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents.

68. **[awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)** - ⭐ 9,058
   A collection of projects showcasing RAG, agents, workflows, and other AI use cases

69. **[inspector](https://github.com/modelcontextprotocol/inspector)** - ⭐ 8,820
   Visual testing tool for MCP servers

70. **[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)** - ⭐ 8,679
   本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.

71. **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)** - ⭐ 8,467
   Official, Anthropic-managed directory of high quality Claude Code Plugins.

72. **[mcp](https://github.com/awslabs/mcp)** - ⭐ 8,270
   Official MCP Servers for AWS

73. **[mcp-go](https://github.com/mark3labs/mcp-go)** - ⭐ 8,232
   A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

74. **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** - ⭐ 8,063
   Build effective agents using Model Context Protocol and simple workflow patterns

75. **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** - ⭐ 7,725
   MCP Server for Ghidra

76. **[git-mcp](https://github.com/idosal/git-mcp)** - ⭐ 7,655
   Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

77. **[awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** - ⭐ 7,586
   🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources. 

78. **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** - ⭐ 7,289
   #1 OpenCode Plugin- Battery included. ASYNC SUBAGENTS (YES LIKE CLAUDE CODE) · Curated agents with proper models · Crafted tools like LSP/AST included · Curated MCPs · Claude Code Compatible Layer — Steroids for your OpenCode. The Best LLM Agent Experience is Here.

79. **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** - ⭐ 7,118
   HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities.

80. **[browser-tools-mcp](https://github.com/AgentDeskAI/browser-tools-mcp)** - ⭐ 7,092
   Monitor browser logs directly from Cursor and other MCP compatible IDEs.

81. **[registry](https://github.com/modelcontextprotocol/registry)** - ⭐ 6,483
   A community driven registry service for Model Context Protocol (MCP) servers.

82. **[astron-rpa](https://github.com/iflytek/astron-rpa)** - ⭐ 6,401
   Agent-ready RPA suite with out-of-the-box automation tools. Built for individuals and enterprises.

83. **[cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** - ⭐ 6,360
   TalkToFigma: MCP integration between Cursor and Figma, allowing Cursor Agentic AI to communicate with Figma for reading designs and modifying them programmatically.

84. **[unity-mcp](https://github.com/CoplayDev/unity-mcp)** - ⭐ 6,330
   Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity.

85. **[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients)** - ⭐ 6,303
   A collection of MCP clients.

86. **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** - ⭐ 6,273
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 76+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server.

87. **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** - ⭐ 6,262
   MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients

88. **[voltagent](https://github.com/VoltAgent/voltagent)** - ⭐ 6,206
   AI Agent Engineering Platform built on an Open Source TypeScript AI Agent Framework

89. **[refly](https://github.com/refly-ai/refly)** - ⭐ 6,135
   The first open-source agent skills builder. 🦞

90. **[mcp](https://github.com/BrowserMCP/mcp)** - ⭐ 5,876
   Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser

91. **[ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** - ⭐ 5,834
   AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP.

92. **[klavis](https://github.com/Klavis-AI/klavis)** - ⭐ 5,645
   Klavis AI (YC X25):  MCP integration platforms that let AI agents use tools reliably at any scale

93. **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** - ⭐ 5,609
   🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.

94. **[Everywhere](https://github.com/DearVa/Everywhere)** - ⭐ 5,565
   Context-aware AI assistant for your desktop. Ready to respond intelligently, seamlessly integrating multiple LLMs and MCP tools.

95. **[DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** - ⭐ 5,545
   This is MCP server for Claude that gives it terminal control, file system search and diff file editing capabilities

96. **[claude-context](https://github.com/zilliztech/claude-context)** - ⭐ 5,466
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent.

97. **[whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)** - ⭐ 5,362
   WhatsApp MCP server

98. **[UltraRAG](https://github.com/OpenBMB/UltraRAG)** - ⭐ 5,329
   A Low-Code MCP Framework for Building Complex and Innovative RAG Pipelines

99. **[mcp-playwright](https://github.com/executeautomation/mcp-playwright)** - ⭐ 5,255
   Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

100. **[sdk-python](https://github.com/strands-agents/sdk-python)** - ⭐ 5,207
   A model-driven approach to building AI agents in just a few lines of code.

101. **[awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** - ⭐ 5,183
   Awesome MCP Servers - A curated list of Model Context Protocol servers

102. **[5ire](https://github.com/nanbingxyz/5ire)** - ⭐ 5,046
   5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers .

103. **[gaianet-node](https://github.com/GaiaNet-AI/gaianet-node)** - ⭐ 5,006
   Install, run and deploy your own decentralized AI agent service

104. **[microsandbox](https://github.com/zerocore-ai/microsandbox)** - ⭐ 4,857
   opensource self-hosted sandboxes for ai agents

105. **[aci](https://github.com/aipotheosis-labs/aci)** - ⭐ 4,723
   ACI.dev is the open source tool-calling platform that hooks up 600+ tools into any agentic IDE or custom AI agent through direct function calling or a unified MCP server. The birthplace of VibeOps.

106. **[Kiln](https://github.com/Kiln-AI/Kiln)** - ⭐ 4,680
   Build, Evaluate, and Optimize AI Systems. Includes evals, RAG, agents, fine-tuning, synthetic data generation, dataset management, MCP, and more.

107. **[XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP)** - ⭐ 4,468
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

108. **[mcp-ui](https://github.com/MCP-UI-Org/mcp-ui)** - ⭐ 4,462
   UI over MCP. Create next-gen UI experiences with the protocol and SDK!

109. **[deep-research](https://github.com/u14app/deep-research)** - ⭐ 4,452
   Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server.

110. **[casibase](https://github.com/casibase/casibase)** - ⭐ 4,451
   ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com

111. **[Windows-MCP](https://github.com/CursorTouch/Windows-MCP)** - ⭐ 4,435
   MCP Server for Computer Use in Windows

112. **[mcp-atlassian](https://github.com/sooperset/mcp-atlassian)** - ⭐ 4,404
   MCP server for Atlassian tools (Confluence, Jira)

113. **[magic-mcp](https://github.com/21st-dev/magic-mcp)** - ⭐ 4,311
   It's like v0 but in your Cursor/WindSurf/Cline. 21st dev Magic MCP server for working with your frontend like Magic

114. **[httprunner](https://github.com/httprunner/httprunner)** - ⭐ 4,259
   HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。

115. **[XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP)** - ⭐ 4,145
   A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

116. **[Olares](https://github.com/beclab/Olares)** - ⭐ 4,136
   Olares: An Open-Source Personal Cloud to Reclaim Your Data

117. **[mcpo](https://github.com/open-webui/mcpo)** - ⭐ 4,002
   A simple, secure MCP-to-OpenAPI proxy server

118. **[csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)** - ⭐ 3,957
   The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

119. **[notion-mcp-server](https://github.com/makenotion/notion-mcp-server)** - ⭐ 3,947
   Official Notion MCP Server

120. **[go-sdk](https://github.com/modelcontextprotocol/go-sdk)** - ⭐ 3,945
   The official Go SDK for Model Context Protocol servers and clients. Maintained in collaboration with Google.

121. **[learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)** - ⭐ 3,927
   Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern and Agent-Native Cloud Technologies: OpenAI Agents SDK, Memory, MCP, A2A, Knowledge Graphs, Dapr, Rancher Desktop, and Kubernetes.

122. **[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** - ⭐ 3,925
   A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

123. **[directories](https://github.com/leerob/directories)** - ⭐ 3,908
   The Cursor & Windsurf community, find rules and MCPs

124. **[directories](https://github.com/pontusab/directories)** - ⭐ 3,896
   The Cursor & Windsurf community, find rules and MCPs

125. **[exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)** - ⭐ 3,886
   Exa MCP for web search and web crawling!

126. **[learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering)** - ⭐ 3,841
   Learn AI and LLMs from scratch using free resources

127. **[telegram-search](https://github.com/groupultra/telegram-search)** - ⭐ 3,774
   🔍 导出并模糊搜索 Telegram 聊天记录 | Export and fuzzy search your Telegram chat history

128. **[atmosphere](https://github.com/Atmosphere/atmosphere)** - ⭐ 3,735
   Stream Real Time and LLM response data over WebSocket, SSE, and the MCP protocol

129. **[wanwu](https://github.com/UnicomAI/wanwu)** - ⭐ 3,732
   China Unicom's Yuanjing Wanwu Agent Platform is an enterprise-grade, multi-tenant AI agent development platform. It helps users build applications such as intelligent agents, workflows, and rag, and also supports model management. The platform features a developer-friendly license, and we welcome all developers to build upon the platform.

130. **[mcp-server-chart](https://github.com/antvis/mcp-server-chart)** - ⭐ 3,719
   🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.

131. **[MemOS](https://github.com/MemTensor/MemOS)** - ⭐ 3,710
   Build memory-native AI agents with Memory OS — an open-source framework for long-term memory, retrieval, and adaptive learning in large language models. Agent Memory | Memory  System | Memory Management | Memory MCP | MCP System | LLM Memory | Agents Memory System | 

132. **[fast-agent](https://github.com/evalstate/fast-agent)** - ⭐ 3,688
   Define, Prompt and Test MCP enabled Agents and Workflows

133. **[awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)** - ⭐ 3,659
   A curated list of Model Context Protocol (MCP) servers

134. **[ciso-assistant-community](https://github.com/intuitem/ciso-assistant-community)** - ⭐ 3,610
   CISO Assistant is a one-stop-shop GRC platform for Risk Management, AppSec, Compliance & Audit, TPRM, Privacy, and Reporting. It supports 100+ global frameworks with automatic control mapping, including ISO 27001, NIST CSF, SOC 2, CIS, PCI DSS, NIS2, DORA, GDPR, HIPAA, CMMC, and more.

135. **[core](https://github.com/opensumi/core)** - ⭐ 3,606
   A framework helps you quickly build AI Native IDE products. MCP Client, supports Model Context Protocol (MCP) tools via MCP server.

136. **[go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)** - ⭐ 3,592
   GOWA - WhatsApp REST API with support for UI, Multi Account, Webhooks, and MCP, and Chatwoot. Built with Golang for efficient memory use. 

137. **[osaurus](https://github.com/osaurus-ai/osaurus)** - ⭐ 3,588
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

138. **[mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced)** - ⭐ 3,581
   Enhanced MCP server for interactive user feedback and command execution in AI-assisted development, featuring dual interface support (Web UI and Desktop Application) with intelligent environment detection and cross-platform compatibility.

139. **[mobile-mcp](https://github.com/mobile-next/mobile-mcp)** - ⭐ 3,574
   Model Context Protocol Server for Mobile Automation and Scraping (iOS, Android, Emulators, Simulators and Real Devices)

140. **[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** - ⭐ 3,570
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

141. **[archestra](https://github.com/archestra-ai/archestra)** - ⭐ 3,566
   Secure cloud-native MCP registry, gateway & orchestrator

142. **[osaurus](https://github.com/dinoki-ai/osaurus)** - ⭐ 3,548
   AI edge infrastructure for macOS. Run local or cloud models, share tools across apps via MCP, and power AI workflows with a native, always-on runtime.

143. **[cipher](https://github.com/campfirein/cipher)** - ⭐ 3,542
   Byterover Cipher is an opensource memory layer specifically designed for coding agents. Compatible with Cursor, Codex, Claude Code, Windsurf, Cline, Claude Desktop, Gemini CLI, AWS's Kiro, VS Code, Roo Code, Trae, Amp Code and Warp through MCP. Built by https://byterover.dev/

144. **[claude-code-guide](https://github.com/zebbern/claude-code-guide)** - ⭐ 3,471
   Claude Code Guide - Setup, Commands, workflows, agents, skills & tips-n-tricks 

145. **[mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - ⭐ 3,466

146. **[AionUi](https://github.com/iOfficeAI/AionUi)** - ⭐ 3,452
   Free, local, open-source GUI app for Gemini CLI, Claude Code, Codex, Qwen Code, Goose Cli, Auggie, and more — Enhanced Chat UI, WebUI, Multi-Agent & Multi-LLM, MCP Integration | 🌟 Star if you like it!

147. **[octelium](https://github.com/octelium/octelium)** - ⭐ 3,420
   A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA platform, API/AI/MCP gateway, a PaaS, an ngrok-alternative and a homelab infrastructure.

148. **[PPTAgent](https://github.com/icip-cas/PPTAgent)** - ⭐ 3,391
   An Agentic Framework for Reflective PowerPoint Generation

149. **[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)** - ⭐ 3,383
   LangChain 🔌 MCP

150. **[excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)** - ⭐ 3,377
   A Model Context Protocol server for Excel file manipulation

151. **[MCP-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** - ⭐ 3,337
   Model Context Protocol(MCP) 编程极速入门

152. **[mcp-context-forge](https://github.com/IBM/mcp-context-forge)** - ⭐ 3,335
   An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins.

153. **[PeopleInSpace](https://github.com/joreilly/PeopleInSpace)** - ⭐ 3,308
   Kotlin Multiplatform sample with SwiftUI, Jetpack Compose, Compose for Wear, Compose for Desktop, and Compose for Web clients along with Ktor backend.

154. **[mcp](https://github.com/google/mcp)** - ⭐ 3,301
   Google 💚 MCP

155. **[rikkahub](https://github.com/rikkahub/rikkahub)** - ⭐ 3,300
   RikkaHub is an Android APP that supports for multiple LLM providers.

156. **[boost](https://github.com/laravel/boost)** - ⭐ 3,295
   Laravel-focused MCP server for augmenting your AI powered local development experience.

157. **[metorial](https://github.com/metorial/metorial)** - ⭐ 3,223
   Connect any AI model to 600+ integrations; powered by MCP 📡 🚀

158. **[java-sdk](https://github.com/modelcontextprotocol/java-sdk)** - ⭐ 3,199
   The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

159. **[py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi)** - ⭐ 3,191
   A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware.

160. **[mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase)** - ⭐ 3,159
   Allow LLMs to control a browser with Browserbase and Stagehand

161. **[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)** - ⭐ 3,065
   The official Rust SDK for the Model Context Protocol

162. **[AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)** - ⭐ 2,993
   A.I.G (AI-Infra-Guard) is a full-stack AI Red Teaming platform developed by Tencent Zhuque Lab that secures your AI ecosystem from infrastructure to agents.

163. **[n8n-nodes-mcp](https://github.com/nerding-io/n8n-nodes-mcp)** - ⭐ 2,986
   n8n custom node for MCP

164. **[core](https://github.com/cheshire-cat-ai/core)** - ⭐ 2,972
   AI agent microservice

165. **[fastmcp](https://github.com/punkpeye/fastmcp)** - ⭐ 2,963
   A TypeScript framework for building MCP servers.

166. **[playwriter](https://github.com/remorses/playwriter)** - ⭐ 2,947
   Chrome extension to let agents control your browser. Runs Playwright snippets in a stateful sandbox. Available as CLI or MCP

167. **[mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** - ⭐ 2,904
   MCP server that interacts with Obsidian via the Obsidian rest API community plugin

168. **[easy-vibe](https://github.com/datawhalechina/easy-vibe)** - ⭐ 2,849
   vibe coding from 0 to 1 ｜深入浅出 AI 编程 ｜ vibecoding 零基础教程

169. **[excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)** - ⭐ 2,776
   Fast and streamable Excalidraw MCP App

170. **[sandbox](https://github.com/agent-infra/sandbox)** - ⭐ 2,667
   All-in-One Sandbox for AI Agents that combines Browser, Shell, File, MCP and VSCode Server in a single Docker container.

171. **[shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)** - ⭐ 2,663
   A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native

172. **[mcp](https://github.com/microsoft/mcp)** - ⭐ 2,658
   Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

173. **[bifrost](https://github.com/maximhq/bifrost)** - ⭐ 2,580
   Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.

174. **[basic-memory](https://github.com/basicmachines-co/basic-memory)** - ⭐ 2,569
   AI conversations that actually remember. Never re-explain your project to your AI again. Join our Discord: https://discord.gg/tyvKNccgqN

175. **[kreuzberg](https://github.com/Goldziher/kreuzberg)** - ⭐ 2,561
   A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 50+ formats. Available for Rust, Python, Ruby, Go, and TypeScript/Node.js—or use via CLI, REST API, or MCP server.

176. **[nunu](https://github.com/go-nunu/nunu)** - ⭐ 2,548
   A CLI tool for building Go applications.

177. **[openfang](https://github.com/RightNow-AI/openfang)** - ⭐ 2,526
   Open-source Agent Operating System

178. **[buildwithclaude](https://github.com/davepoon/buildwithclaude)** - ⭐ 2,498
   A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

179. **[supabase-mcp](https://github.com/supabase-community/supabase-mcp)** - ⭐ 2,490
   Connect Supabase to your AI assistants

180. **[awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)** - ⭐ 2,488
   A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Antigravity, Copilot, VS Code)

181. **[supergateway](https://github.com/supercorp-ai/supergateway)** - ⭐ 2,450
   Run MCP stdio servers over SSE and SSE over stdio. AI gateway.

182. **[slackdump](https://github.com/rusq/slackdump)** - ⭐ 2,432
   Save or export your private and public Slack messages, threads, files, and users locally without admin privileges.

183. **[Peekaboo](https://github.com/steipete/Peekaboo)** - ⭐ 2,426
   Peekaboo is a macOS CLI & optional MCP server that enables AI agents to capture screenshots of applications, or the entire system, with optional visual question answering through local or remote AI models.

184. **[markdownify-mcp](https://github.com/zcaceres/markdownify-mcp)** - ⭐ 2,421
   A Model Context Protocol server for converting almost anything to Markdown

185. **[mcp-grafana](https://github.com/grafana/mcp-grafana)** - ⭐ 2,416
   MCP server for Grafana

186. **[MCP-SuperAssistant](https://github.com/srbhptl39/MCP-SuperAssistant)** - ⭐ 2,309
   Brings MCP to ChatGPT, DeepSeek, Perplexity, Grok, Gemini, Google AI Studio, OpenRouter, DeepSeek, T3 Chat and more...

187. **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** - ⭐ 2,292
   A bridge between Streamable HTTP and stdio MCP transports

188. **[EverMemOS](https://github.com/EverMind-AI/EverMemOS)** - ⭐ 2,276
   Long-term memory OS for your agents across LLMs and platforms.

189. **[ableton-mcp](https://github.com/ahujasid/ableton-mcp)** - ⭐ 2,263

190. **[lemonade](https://github.com/lemonade-sdk/lemonade)** - ⭐ 2,260
   Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk

191. **[kagent](https://github.com/kagent-dev/kagent)** - ⭐ 2,252
   Cloud Native Agentic AI | Discord: https://bit.ly/kagentdiscord

192. **[ddgs](https://github.com/deedy5/ddgs)** - ⭐ 2,240
   A metasearch library that aggregates results from diverse web search services

193. **[arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)** - ⭐ 2,228
   A Model Context Protocol server for searching and analyzing arXiv papers

194. **[mcporter](https://github.com/steipete/mcporter)** - ⭐ 2,208
   Call MCPs via TypeScript, masquerading as simple TypeScript API. Or package them as cli.

195. **[postgres-mcp](https://github.com/crystaldba/postgres-mcp)** - ⭐ 2,202
   Postgres MCP Pro provides configurable read/write access and performance analysis for you and your AI agents.

196. **[dbhub](https://github.com/bytebase/dbhub)** - ⭐ 2,191
   Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

197. **[chatmcp](https://github.com/daodao97/chatmcp)** - ⭐ 2,175
   ChatMCP is an AI chat client implementing the Model Context Protocol (MCP).

198. **[papersgpt-for-zotero](https://github.com/papersgpt/papersgpt-for-zotero)** - ⭐ 2,134
   A powerful Zotero AI and MCP plugin with ChatGPT, Gemini 3.1, Claude, Grok, DeepSeek, OpenRouter, Kimi 2.5, GLM 5, SiliconFlow, GPT-oss, Gemma 3, Qwen 3.5

199. **[comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party)** - ⭐ 2,112
   LLM Agent Framework in ComfyUI includes MCP sever, Omost,GPT-sovits, ChatTTS,GOT-OCR2.0, and FLUX prompt nodes,access to Feishu,discord,and adapts to all llms with similar openai / aisuite interfaces, such as o1,ollama, gemini, grok, qwen, GLM, deepseek, kimi,doubao. Adapted to local llms, vlm, gguf such as llama-3.3 Janus-Pro, Linkage graphRAG

200. **[claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection)** - ⭐ 2,098
   Claude Code Subagents & Commands Collection + CLI Tool

201. **[brightdata-mcp](https://github.com/brightdata/brightdata-mcp)** - ⭐ 2,061
   A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.

202. **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** - ⭐ 2,060
   Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

203. **[solace-agent-mesh](https://github.com/SolaceLabs/solace-agent-mesh)** - ⭐ 2,054
   An event-driven framework designed to build and orchestrate multi-agent AI systems. It enables seamless integration of AI agents with real-world data sources and systems, facilitating complex, multi-step workflows.

204. **[metamcp](https://github.com/metatool-ai/metamcp)** - ⭐ 2,054
   MCP Aggregator, Orchestrator, Middleware, Gateway in one docker

205. **[superset](https://github.com/superset-sh/superset)** - ⭐ 2,048
   IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

206. **[Unla](https://github.com/AmoyLab/Unla)** - ⭐ 2,040
   🧩 MCP Gateway - A lightweight gateway service that instantly transforms existing MCP Servers and APIs into MCP servers with zero code changes. Features Docker deployment and management UI, requiring no infrastructure modifications.

207. **[DevDocs](https://github.com/cyberagiinc/DevDocs)** - ⭐ 2,035
   Completely free, private, UI based Tech Documentation MCP server. Designed for coders and software developers in mind. Easily integrate into Cursor, Windsurf, Cline, Roo Code, Claude Desktop App 

208. **[mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager)** - ⭐ 2,033
   Shrimp Task Manager is a task tool built for AI Agents, emphasizing chain-of-thought, reflection, and style consistency. It converts natural language into structured dev tasks with dependency tracking and iterative refinement, enabling agent-like developer behavior in reasoning AI systems.

209. **[gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)** - ⭐ 2,011
   MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding

210. **[mcp-crawl4ai-rag](https://github.com/coleam00/mcp-crawl4ai-rag)** - ⭐ 2,010
   Web Crawling and RAG Capabilities for AI Agents and AI Coding Assistants

211. **[superglue](https://github.com/superglue-ai/superglue)** - ⭐ 1,989
   superglue (YC W25) builds integrations and tools from natural language. Get production-grade tools for long tail and enterprise systems.

212. **[modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol)** - ⭐ 1,983
   The official MCP server implementation for the Perplexity API Platform

213. **[godot-mcp](https://github.com/Coding-Solo/godot-mcp)** - ⭐ 1,976
   MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output.

214. **[mcpso](https://github.com/chatmcp/mcpso)** - ⭐ 1,970
   directory for Awesome MCP Servers

215. **[Aix-DB](https://github.com/apconw/Aix-DB)** - ⭐ 1,965
   Aix-DB 基于 LangChain/LangGraph 框架，结合 MCP Skills 多智能体协作架构，实现自然语言到数据洞察的端到端转换。

216. **[code-graph-rag](https://github.com/vitali87/code-graph-rag)** - ⭐ 1,961
   The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

217. **[mcp-cli](https://github.com/IBM/mcp-cli)** - ⭐ 1,893

218. **[mcp-cli](https://github.com/chrishayuk/mcp-cli)** - ⭐ 1,891

219. **[yomo](https://github.com/yomorun/yomo)** - ⭐ 1,885
   🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

220. **[agentset](https://github.com/agentset-ai/agentset)** - ⭐ 1,885
   The open-source RAG platform: built-in citations, deep research, 22+ file formats, partitions, MCP server, and more.

221. **[witsy](https://github.com/nbonamy/witsy)** - ⭐ 1,880
   Witsy: desktop AI assistant / universal MCP client

222. **[beelzebub](https://github.com/mariocandela/beelzebub)** - ⭐ 1,853
   A secure low code honeypot framework, leveraging AI for System Virtualization.

223. **[mcphub](https://github.com/samanhappy/mcphub)** - ⭐ 1,830
   A unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies

224. **[sanic-web](https://github.com/apconw/sanic-web)** - ⭐ 1,817
   一个轻量级、支持全链路且易于二次开发的大模型应用项目(Large Model Data Assistant) 支持DeepSeek/Qwen3等大模型 基于 Dify 、LangChain/LangGraph、Ollama&Vllm、Sanic 和 Text2SQL 📊 等技术构建的一站式大模型应用开发项目，采用 Vue3、TypeScript 和 Vite 5 打造现代UI。它支持通过 ECharts 📈 实现基于大模型的数据图形化问答，具备处理 CSV 文件 📂 表格问答的能力。同时，能方便对接第三方开源 RAG 系统 检索系统 🌐等，以支持广泛的通用知识问答。

225. **[agentgateway](https://github.com/agentgateway/agentgateway)** - ⭐ 1,816
   Next Generation Agentic Proxy for AI Agents and MCP servers

226. **[esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** - ⭐ 1,800
   An AI-enabled NAT Router/Firewall for the ESP32

227. **[opendia](https://github.com/aaronjmars/opendia)** - ⭐ 1,779
   Connect your browser to AI models. Just use Dia on Chrome, Arc or Firefox.

228. **[mcp-router](https://github.com/mcp-router/mcp-router)** - ⭐ 1,777
   A Unified MCP Server Management App (MCP Manager).

229. **[inspector](https://github.com/MCPJam/inspector)** - ⭐ 1,765
   Test & Debug MCP servers, ChatGPT apps, and MCP Apps (ext-apps)

230. **[super-agent-party](https://github.com/heshengtao/super-agent-party)** - ⭐ 1,763
   ⭐ All-in-one AI companion! Desktop girlfriend + virtual streamer + IM bot + browser control + smart home control + computer control + virtual reality, and everything else you can imagine!⭐全能型AI伴侣！桌面女友 + 虚拟主播 + 即时通讯机器人 + 浏览器控制 + 智能家居控制 + 电脑控制 + 虚拟现实 等你能想到的一切功能！

231. **[AIaW](https://github.com/NitroRCr/AIaW)** - ⭐ 1,756
   AI as Workspace - An elegant AI chat client. Full-featured, lightweight. Support multiple workspaces, plugin system, cross-platform, local first + real-time cloud sync, Artifacts, MCP | 更好的 AI 客户端

232. **[Dive](https://github.com/OpenAgentPlatform/Dive)** - ⭐ 1,738
   Dive is an open-source MCP Host Desktop Application that seamlessly integrates with any LLMs supporting function calling capabilities. ✨

233. **[mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)** - ⭐ 1,737
   Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite

234. **[mcphub.nvim](https://github.com/ravitemer/mcphub.nvim)** - ⭐ 1,733
   An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins.

235. **[mcpb](https://github.com/modelcontextprotocol/mcpb)** - ⭐ 1,731
   Desktop Extensions: One-click local MCP server installation in desktop apps

236. **[notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)** - ⭐ 1,728

237. **[ext-apps](https://github.com/modelcontextprotocol/ext-apps)** - ⭐ 1,719
   Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers

238. **[yu-ai-agent](https://github.com/liyupi/yu-ai-agent)** - ⭐ 1,707
   编程导航 2025 年 AI 开发实战新项目，基于 Spring Boot 3 + Java 21 + Spring AI 构建 AI 恋爱大师应用和 ReAct 模式自主规划智能体YuManus，覆盖 AI 大模型接入、Spring AI 核心特性、Prompt 工程和优化、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、AI Agent 开发（Manas Java 实现）、Cursor AI 工具等核心知识。用一套教程将程序员必知必会的 AI 技术一网打尽，帮你成为 AI 时代企业的香饽饽，给你的简历和求职大幅增加竞争力。

239. **[plik](https://github.com/root-gg/plik)** - ⭐ 1,701
   Plik is a temporary file upload system (Wetransfer like) in Go.

240. **[vexa](https://github.com/Vexa-ai/vexa)** - ⭐ 1,694
   Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS.

241. **[MAI-UI](https://github.com/Tongyi-MAI/MAI-UI)** - ⭐ 1,691
   MAI-UI: Real-World Centric Foundation GUI Agents ranging from 2B to 235B

242. **[interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)** - ⭐ 1,675
   Interactive User Feedback MCP

243. **[ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp)** - ⭐ 1,671
   MCP server for interacting with the iOS simulator

244. **[zenfeed](https://github.com/glidea/zenfeed)** - ⭐ 1,653
   Make RSS 📰 great again with AI 🧠✨!! [网页监控工具-预定送会员：https://waitlist.dingding.glidea.app]

245. **[Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** - ⭐ 1,646
   A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities.

246. **[py-gpt](https://github.com/szczyglis-dev/py-gpt)** - ⭐ 1,642
   Desktop AI Assistant powered by GPT-5, GPT-4, o1, o3, Gemini, Claude, Ollama, DeepSeek, Perplexity, Grok, Bielik, chat, vision, voice, RAG, image and video generation, agents, tools, MCP, plugins, speech synthesis and recognition, web search, memory, presets, assistants,and more. Linux, Windows, Mac

247. **[kubb](https://github.com/kubb-labs/kubb)** - ⭐ 1,630
   🧩 The Ultimate Toolkit for Generating Type-Safe API Clients, Hooks, and Validators.

248. **[anyquery](https://github.com/julien040/anyquery)** - ⭐ 1,626
   Query anything (GitHub, Notion, +40 more) with SQL and let LLMs (ChatGPT, Claude) connect to using MCP

249. **[toolhive](https://github.com/stacklok/toolhive)** - ⭐ 1,619
   ToolHive makes deploying MCP servers easy, secure and fun

250. **[codemcp](https://github.com/ezyang/codemcp)** - ⭐ 1,608
   Coding assistant MCP for Claude Desktop

251. **[agent-scan](https://github.com/snyk/agent-scan)** - ⭐ 1,604
   Security scanner for AI agents, MCP servers and agent skills.

252. **[moltis](https://github.com/moltis-org/moltis)** - ⭐ 1,584
   A Rust-native claw you can trust. One binary — sandboxed, secure, auditable. Voice, memory, MCP tools, and multi-channel access built-in.

253. **[Continuous-Claude-v2](https://github.com/parcadei/Continuous-Claude-v2)** - ⭐ 1,575
   Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

254. **[pg-aiguide](https://github.com/timescale/pg-aiguide)** - ⭐ 1,570
   MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

255. **[n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server)** - ⭐ 1,569
   MCP server that provides tools and resources for interacting with n8n API

256. **[mcphost](https://github.com/mark3labs/mcphost)** - ⭐ 1,565
   A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).

257. **[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)** - ⭐ 1,557
   Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool

258. **[Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** - ⭐ 1,542
   A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol.

259. **[zotero-mcp](https://github.com/54yyyu/zotero-mcp)** - ⭐ 1,525
   Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

260. **[skills](https://github.com/microsoft/skills)** - ⭐ 1,522
   Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

261. **[mcp-installer](https://github.com/anaisbetts/mcp-installer)** - ⭐ 1,507
   An MCP server that installs other MCP servers for you

262. **[mcptools](https://github.com/f/mcptools)** - ⭐ 1,495
   A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

263. **[claudian](https://github.com/YishenTu/claudian)** - ⭐ 1,493
   An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

264. **[oh-my-pi](https://github.com/can1357/oh-my-pi)** - ⭐ 1,477
   ⌥  AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

265. **[better-agents](https://github.com/langwatch/better-agents)** - ⭐ 1,474
   Standards for building agents, better

266. **[MCP-Reborn](https://github.com/Hexeption/MCP-Reborn)** - ⭐ 1,459
   MCP-Reborn is an MCP (Mod Coder Pack) for Minecraft for making modded clients and researching its code. (1.13-1.21.4)

267. **[mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)** - ⭐ 1,458
   Security scanner for AI agents, MCP servers and agent skills.

268. **[mcp-language-server](https://github.com/isaacphi/mcp-language-server)** - ⭐ 1,458
   mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics.

269. **[unreal-mcp](https://github.com/chongdashu/unreal-mcp)** - ⭐ 1,451
   Enable AI assistant clients like Cursor, Windsurf and Claude Desktop to control Unreal Engine through natural language using the Model Context Protocol (MCP).

270. **[pilot-shell](https://github.com/maxritter/pilot-shell)** - ⭐ 1,447
   The professional development environment for Claude Code. Claude Code is powerful. Pilot Shell makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

271. **[claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills)** - ⭐ 1,444
   270+ Claude Code plugins with 739 agent skills. Production orchestration patterns, interactive tutorials (11 Jupyter notebooks), and CCPI package manager. 4.13.0

272. **[rulego](https://github.com/rulego/rulego)** - ⭐ 1,432
   ⛓️RuleGo is a lightweight, high-performance, embedded, next-generation component orchestration rule engine framework for Go.

273. **[claude-pilot](https://github.com/maxritter/claude-pilot)** - ⭐ 1,418
   Claude Code is powerful. Pilot makes it reliable. Start a task, grab a coffee, come back to production-grade code. Tests enforced. Context preserved. Quality automated.

274. **[NagaAgent](https://github.com/RTGS2017/NagaAgent)** - ⭐ 1,409
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

275. **[slack-mcp-server](https://github.com/korotovsky/slack-mcp-server)** - ⭐ 1,400
   The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic.

276. **[mcp](https://github.com/MicrosoftDocs/mcp)** - ⭐ 1,395
   Official Microsoft Learn MCP Server – powering LLMs and AI agents with real-time, trusted Microsoft docs & code samples.

277. **[mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** - ⭐ 1,387
   Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation.

278. **[php-sdk](https://github.com/modelcontextprotocol/php-sdk)** - ⭐ 1,375
   The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

279. **[docker-mcp-tutorial](https://github.com/theNetworkChuck/docker-mcp-tutorial)** - ⭐ 1,363
   Complete tutorial materials for building MCP servers with Docker - from NetworkChuck's video

280. **[mcp-unity](https://github.com/CoderGamester/mcp-unity)** - ⭐ 1,360
   Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs

281. **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** - ⭐ 1,355

282. **[code-mode](https://github.com/universal-tool-calling-protocol/code-mode)** - ⭐ 1,338
   🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution. 

283. **[grepai](https://github.com/yoanbernabeu/grepai)** - ⭐ 1,338
   Semantic Search & Call Graphs for AI Agents (100% Local)

284. **[Risuai](https://github.com/kwaroran/Risuai)** - ⭐ 1,335
   Make your own story. User-friendly software for LLM roleplaying

285. **[hotpath-rs](https://github.com/pawurb/hotpath-rs)** - ⭐ 1,330
   Rust Performance Profiler & Channels Monitoring Toolkit (TUI, MCP)

286. **[mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - ⭐ 1,327
   MCP Server for kubernetes management commands

287. **[azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp)** - ⭐ 1,319
   The MCP server for Azure DevOps, bringing the power of Azure DevOps directly to your agents.

288. **[ai](https://github.com/stripe/ai)** - ⭐ 1,314
   One-stop shop for building AI-powered products and businesses with Stripe.

289. **[LitterBox](https://github.com/BlackSnufkin/LitterBox)** - ⭐ 1,313
   A secure sandbox environment for malware developers and red teamers to test payloads against detection mechanisms before deployment. Integrates with LLM agents via MCP for enhanced analysis capabilities.

290. **[Claude-Code-Development-Kit](https://github.com/peterkrueck/Claude-Code-Development-Kit)** - ⭐ 1,312
   Handle context at scale - my custom Claude Code workflow including hooks, mcp and sub agents

291. **[mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian)** - ⭐ 1,312
   A connector for Claude Desktop to read and search an Obsidian vault.

292. **[jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** - ⭐ 1,298
   Plugin for JADX to integrate MCP server

293. **[mcp-remote](https://github.com/geelen/mcp-remote)** - ⭐ 1,287

294. **[MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** - ⭐ 1,278
   Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

295. **[kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)** - ⭐ 1,271
   The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains

296. **[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)** - ⭐ 1,268
   The official Swift SDK for Model Context Protocol servers and clients.

297. **[deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)** - ⭐ 1,266
   📖 MCP server for fetch deepwiki.com and get latest knowledge in Cursor and other Code Editors

298. **[damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** - ⭐ 1,261
   Damn Vulnerable MCP Server

299. **[mcp-gateway](https://github.com/docker/mcp-gateway)** - ⭐ 1,259
   docker mcp CLI plugin / MCP Gateway

300. **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** - ⭐ 1,253
   Production ready MCP server with real-time search, extract, map & crawl.

301. **[terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)** - ⭐ 1,248
   The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

302. **[mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant)** - ⭐ 1,244
   An official Qdrant Model Context Protocol (MCP) server implementation

303. **[mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)** - ⭐ 1,238
   A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

304. **[web-eval-agent](https://github.com/refreshdotdev/web-eval-agent)** - ⭐ 1,235
   An MCP server that autonomously evaluates web applications. 

305. **[elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp)** - ⭐ 1,235
   The official ElevenLabs MCP server

306. **[sre](https://github.com/SmythOS/sre)** - ⭐ 1,232
   The SmythOS Runtime Environment (SRE) is an open-source, cloud-native runtime for agentic AI. Secure, modular, and production-ready, it lets developers build, run, and manage intelligent agents across local, cloud, and edge environments.

307. **[web-eval-agent](https://github.com/withRefresh/web-eval-agent)** - ⭐ 1,226
   An MCP server that autonomously evaluates web applications. 

308. **[OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)** - ⭐ 1,225
   Humans and AI agents, building knowledge bases together. Self-hosted document annotation, version control, semantic search, and MCP.

309. **[RisuAI](https://github.com/kwaroran/RisuAI)** - ⭐ 1,222
   Make your own story. User-friendly software for LLM roleplaying

310. **[grafbase](https://github.com/grafbase/grafbase)** - ⭐ 1,214
   The Grafbase GraphQL Federation Gateway

311. **[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** - ⭐ 1,214

312. **[xmcp](https://github.com/basementstudio/xmcp)** - ⭐ 1,211
   The TypeScript MCP framework

313. **[npcpy](https://github.com/NPC-Worldwide/npcpy)** - ⭐ 1,210
   The python library for research and development in NLP, multimodal LLMs, Agents, ML, Knowledge Graphs, and more.

314. **[kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server)** - ⭐ 1,207
   Model Context Protocol (MCP) server for Kubernetes and OpenShift

315. **[cunzhi](https://github.com/imhuso/cunzhi)** - ⭐ 1,203
   告别AI提前终止烦恼，助力AI更加持久

316. **[A2V](https://github.com/Devin-AXIS/A2V)** - ⭐ 1,201
   A2V: Next-Gen AI Value Compute Protocol.                                                                                 

317. **[mcp-golang](https://github.com/metoro-io/mcp-golang)** - ⭐ 1,198
   Write Model Context Protocol servers in few lines of go code. Docs at https://mcpgolang.com . Created by https://metoro.io

318. **[cli](https://github.com/TanStack/cli)** - ⭐ 1,188
   The official TanStack CLI - Project Scaffolding, MCP Server, Agent Skills Installation, etc

319. **[Agent-MCP](https://github.com/rinadelph/Agent-MCP)** - ⭐ 1,173
   Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.

320. **[iMCP](https://github.com/mattt/iMCP)** - ⭐ 1,172
   A macOS app that provides an MCP server to your Messages, Contacts, Reminders and more

321. **[xhs-toolkit](https://github.com/aki66938/xhs-toolkit)** - ⭐ 1,158
   📕 小红书创作者MCP工具包 - 支持与AI客户端集成的内容创作和发布工具

322. **[xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java)** - ⭐ 1,148
   小智ESP32的Java企业级管理平台，提供设备监控、音色定制、角色切换和对话记录管理的前后端及服务端一体化解决方案

323. **[trustgraph](https://github.com/trustgraph-ai/trustgraph)** - ⭐ 1,147
   Programmable Context for the AI Stack. Build. Version. Deploy. The full lifecycle platform for Context Graphs.

324. **[fast-mcp](https://github.com/yjacquin/fast-mcp)** - ⭐ 1,142
   A Ruby Implementation of the Model Context Protocol

325. **[mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server)** - ⭐ 1,142
   A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases

326. **[claude-code-mcp](https://github.com/steipete/claude-code-mcp)** - ⭐ 1,140
   Claude Code as one-shot MCP server to have an agent in your agent.

327. **[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins)** - ⭐ 1,133
   A curated list of Plugins that let you extend Claude Code with custom commands, agents, hooks, and MCP servers through the plugin system.

328. **[tuui](https://github.com/AI-QL/tuui)** - ⭐ 1,129
   A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration.

329. **[cui](https://github.com/wbopan/cui)** - ⭐ 1,128
   A web UI for Claude Code agents

330. **[Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** - ⭐ 1,101
   AI-powered bridge connecting LLMs and advanced AI agents to the Unity Editor via the Model Context Protocol (MCP). Chat with AI to generate code, debug errors, and automate game development tasks directly within your project.

331. **[agent-deck](https://github.com/asheshgoplani/agent-deck)** - ⭐ 1,099
   Terminal session manager for AI coding agents. One TUI for Claude, Gemini, OpenCode, Codex, and more.

332. **[gitlab-mcp](https://github.com/zereight/gitlab-mcp)** - ⭐ 1,094
   First gitlab mcp for you

333. **[nanobot](https://github.com/nanobot-ai/nanobot)** - ⭐ 1,085
   Build MCP Agents

334. **[claude-init](https://github.com/cfrs2005/claude-init)** - ⭐ 1,081
   Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境。一键安装完整中文化体验，集成 MCP 服务器、智能上下文管理、安全扫描，支持免翻墙访问。让 AI 编程更简单。

335. **[todo-for-ai](https://github.com/todo-for-ai/todo-for-ai)** - ⭐ 1,080
   🤖 A comprehensive task management system specifically designed for AI assistants. Supports project management, task tracking, team collaboration, and seamless AI integration through MCP (Model Context Protocol). Built with modern tech stack including React, Flask, and Docker. Try it now at https://todo4ai.org/

336. **[flock](https://github.com/Onelevenvy/flock)** - ⭐ 1,073
   Flock is a workflow-based low-code platform for rapidly building chatbots, RAG, and coordinating multi-agent teams, powered by LangGraph, Langchain, FastAPI, and NextJS.（Flock 是一个基于workflow工作流的低代码平台，用于快速构建聊天机器人、RAG、Agent和Muti-Agent应用，采用 LangGraph、Langchain、FastAPI 和 NextJS 构建。）

337. **[docs-mcp-server](https://github.com/arabold/docs-mcp-server)** - ⭐ 1,072
   Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools

338. **[apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp)** - ⭐ 1,058
   MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

339. **[ApeRAG](https://github.com/apecloud/ApeRAG)** - ⭐ 1,054
   ApeRAG: Production-ready GraphRAG with multi-modal indexing, AI agents, MCP support, and scalable K8s deployment

340. **[wenyan-mcp](https://github.com/caol64/wenyan-mcp)** - ⭐ 1,045
   文颜 MCP Server 可以让 AI 自动将 Markdown 文章排版后发布至微信公众号。

341. **[SearChat](https://github.com/sear-chat/SearChat)** - ⭐ 1,041
   Search + Chat = SearChat(AI Chat with Search), Support OpenAI/Anthropic/VertexAI/Gemini, DeepResearch, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

342. **[minima](https://github.com/dmayboroda/minima)** - ⭐ 1,039
   On-premises conversational RAG with configurable containers

343. **[mcp-windbg](https://github.com/svnscha/mcp-windbg)** - ⭐ 1,039
   Model Context Protocol for WinDBG

344. **[ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)** - ⭐ 1,036
   Connect AI models like Claude & GPT with robots using MCP and ROS.

345. **[lets-learn-mcp-python](https://github.com/microsoft/lets-learn-mcp-python)** - ⭐ 1,033
   MCP Python Tutorial 

346. **[Gmail-MCP-Server](https://github.com/GongRzhe/Gmail-MCP-Server)** - ⭐ 1,033
   A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions.

347. **[notebooklm-mcp](https://github.com/PleasePrompto/notebooklm-mcp)** - ⭐ 1,033
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

348. **[mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)** - ⭐ 1,032
   Query and Summarize your chat messages.

349. **[better-chatbot](https://github.com/cgoinglove/better-chatbot)** - ⭐ 1,028
   Just a Better Chatbot. Powered by Agent & MCP & Workflows.

350. **[Awesome-MCP-Servers](https://github.com/YuzeHao2023/Awesome-MCP-Servers)** - ⭐ 1,026
   A curated list of Model Context Protocol (MCP) servers 

351. **[search_with_ai](https://github.com/yokingma/search_with_ai)** - ⭐ 1,025
   AI Search Chat , Support DeepResearch, OpenAI/Anthropic/VertexAI/Gemini, SearXNG, Docker.  AI对话式搜索引擎，支持DeepResearch, 支持OpenAI/Anthropic/VertexAI/Gemini接口、聚合搜索引擎SearXNG，支持Docker一键部署。

352. **[WebMCP](https://github.com/MiguelsPizza/WebMCP)** - ⭐ 1,025
   Bringing the power of MCP to the web

353. **[google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)** - ⭐ 1,016
   MCP integration for Google Calendar to manage events.

354. **[mcp-boilerplate](https://github.com/iannuttall/mcp-boilerplate)** - ⭐ 1,009
   A remote Cloudflare MCP server boilerplate with user authentication and Stripe for paid tools.

355. **[awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers)** - ⭐ 1,008
   Remote MCP Servers

356. **[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** - ⭐ 1,001
   The ultimate all-in-one guide to mastering Claude Code. From setup, prompt engineering, commands, hooks, workflows, automation, and integrations, to MCP servers, tools, and the BMAD method—packed with step-by-step tutorials, real-world examples, and expert strategies to make this the global go-to repo for Claude mastery.

357. **[quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources)** - ⭐ 1,000
   A repository of servers and clients from the Model Context Protocol tutorials

358. **[fetcher-mcp](https://github.com/jae-jae/fetcher-mcp)** - ⭐ 992
   MCP server for fetch web page content using Playwright headless browser.

359. **[short-video-maker](https://github.com/gyoridavid/short-video-maker)** - ⭐ 987
   Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API.

360. **[ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** - ⭐ 987
   Helping coding agents never make mistakes working with public or private libraries without wasting the context window.

361. **[paperbanana](https://github.com/llmsresearch/paperbanana)** - ⭐ 987
   Open source implementation and extension of Google Research’s PaperBanana for automated academic figures, diagrams, and research visuals, expanded to new domains like slide generation.

362. **[ai-dev-tools-zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)** - ⭐ 986
   AI Dev Tools Zoomcamp is a free course that helps you use AI tools to write better code, faster. We're starting the first cohort of this course on November 18, 2025! Sign up here to join us 👇🏼

363. **[RedNote-MCP](https://github.com/iFurySt/RedNote-MCP)** - ⭐ 979
   🚀MCP server for accessing RedNote(XiaoHongShu, xhs).

364. **[ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** - ⭐ 971
   The Unofficial and Awesome Home Assistant MCP Server

365. **[ollama-mcp-bridge](https://github.com/patruff/ollama-mcp-bridge)** - ⭐ 966
   Bridge between Ollama and MCP servers, enabling local LLMs to use Model Context Protocol tools

366. **[agents](https://github.com/inkeep/agents)** - ⭐ 963
   Create AI Agents in a No-Code Visual Builder or TypeScript SDK with full 2-way sync. For shipping AI assistants and multi-agent AI workflows.

367. **[CloudBase-MCP](https://github.com/TencentCloudBase/CloudBase-MCP)** - ⭐ 961
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app. 

368. **[gemini-nexus](https://github.com/yeahhe365/gemini-nexus)** - ⭐ 956
   Gemini Nexus 是一款深度集成 Google Gemini 能力的 Chrome 扩展程序。它不仅仅是一个侧边栏插件，而是通过注入式的悬浮工具栏、强大的图像 AI 处理以及前沿的浏览器控制协议 (MCP)，将 AI 的触角伸向网页浏览的每一个交互细节。

369. **[awesome-devops-mcp-servers](https://github.com/rohitg00/awesome-devops-mcp-servers)** - ⭐ 949
   A curated list of awesome MCP servers focused on DevOps tools and capabilities.

370. **[tools](https://github.com/strands-agents/tools)** - ⭐ 946
   A set of tools that gives agents powerful capabilities.

371. **[mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains)** - ⭐ 943
   A model context protocol server to work with JetBrains IDEs: IntelliJ, PyCharm, WebStorm, etc. Also, works with Android Studio

372. **[linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)** - ⭐ 940
   This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and perform job searches.

373. **[mcpdoc](https://github.com/langchain-ai/mcpdoc)** - ⭐ 931
   Expose llms-txt to IDEs for development

374. **[trpc-agent-go](https://github.com/trpc-group/trpc-agent-go)** - ⭐ 931
   trpc-agent-go is a powerful Go framework for building intelligent agent systems using large language models (LLMs) and tools.

375. **[Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)** - ⭐ 927
   An Open-Source Multimodal AIGC Solution based on ComfyUI + MCP + LLM  https://pixelle.ai

376. **[mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server)** - ⭐ 927
   A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters.

377. **[MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** - ⭐ 916
   A middleware to provide an openAI compatible endpoint that can call MCP tools

378. **[agentic-radar](https://github.com/splx-ai/agentic-radar)** - ⭐ 915
   A security scanner for your LLM agentic workflows

379. **[amical](https://github.com/amicalhq/amical)** - ⭐ 912
   🎙️ AI Dictation App - Open Source and Local-first ⚡ Type 3x faster, no keyboard needed. 🆓 Powered by open source models, works offline, fast and accurate.

380. **[jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server)** - ⭐ 912
   🪐 🔧 Model Context Protocol (MCP) Server for Jupyter.

381. **[mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)** - ⭐ 911
   Neo4j Labs Model Context Protocol servers

382. **[mcp-cli](https://github.com/philschmid/mcp-cli)** - ⭐ 910
   Lighweight CLI to interact with MCP servers

383. **[CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit)** - ⭐ 909
      CloudBase MCP - Connect CloudBase to your AI Agent.     Go from AI prompt to live app in one click.

384. **[mcp-framework](https://github.com/QuantGeekDev/mcp-framework)** - ⭐ 903
   A framework for writing MCP (Model Context Protocol) servers in Typescript

385. **[mcp-browser-use](https://github.com/Saik0s/mcp-browser-use)** - ⭐ 902

386. **[nuxt-mcp-dev](https://github.com/antfu/nuxt-mcp-dev)** - ⭐ 897
   MCP server helping models to understand your Vite/Nuxt app better.

387. **[mcpm.sh](https://github.com/pathintegral-institute/mcpm.sh)** - ⭐ 895
   CLI MCP package manager & registry for all platforms and all clients. Search & configure MCP servers. Advanced Router & Profile features.

388. **[chatgpt-cli](https://github.com/kardolus/chatgpt-cli)** - ⭐ 890
   ChatGPT CLI is a powerful, multi-provider command-line interface for working with modern LLMs. It supports OpenAI, Azure, Perplexity, LLaMA, and more, with features like streaming, interactive chat, prompt files, image/audio I/O, MCP tool calls, and an experimental agent mode for safe, multi-step automation.

389. **[browserwing](https://github.com/browserwing/browserwing)** - ⭐ 889
   BrowserWing turns your browser actions into MCP commands Or Claude Skill, allowing AI agents to control browsers efficiently and reliably. Say goodbye to slow, token-heavy LLM interactions — let agents call commands directly for faster automation. Perfect for AI-driven tasks, browser automation, and boosting productivity.

390. **[himarket](https://github.com/higress-group/himarket)** - ⭐ 886
   HiMarket is an enterprise-level "AI Capability Marketplace and Developer Ecosystem Hub." It is not merely a simple aggregation of traditional APIs, but rather a comprehensive platform that packages, publishes, manages, and operates core AI assets such as enterprise Model APIs, MCP Servers, Agent APIs, etc., through standardized product formats.

391. **[MCProtocolLib](https://github.com/GeyserMC/MCProtocolLib)** - ⭐ 882
   A library for communication with a Minecraft client/server.

392. **[mix.core](https://github.com/mixcore/mix.core)** - ⭐ 881
   🚀 A future-proof enterprise web CMS supporting both headless and decoupled approaches. Build any type of app with customizable APIs on ASP.NET Core/.NET Core. Completely open-source and designed for flexibility.

393. **[shellfirm](https://github.com/kaplanelad/shellfirm)** - ⭐ 881
   Terminal guardrails for humans and AI agents — intercepts dangerous commands with context-aware challenges before the damage is done.

394. **[openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server)** - ⭐ 880
   Allow AI to wade through complex OpenAPIs using Simple Language

395. **[excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)** - ⭐ 876
   Excalidraw MCP App Server — hand-drawn diagrams for Claude

396. **[MCPJungle](https://github.com/mcpjungle/MCPJungle)** - ⭐ 876
   Self-hosted MCP Gateway for AI agents

397. **[AI-Gateway](https://github.com/Azure-Samples/AI-Gateway)** - ⭐ 875
   Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft Foundry 🚀

398. **[mcp-course](https://github.com/huggingface/mcp-course)** - ⭐ 872

399. **[memory-bank-mcp](https://github.com/alioshr/memory-bank-mcp)** - ⭐ 868
   A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank.

400. **[hyper-mcp](https://github.com/hyper-mcp-rs/hyper-mcp)** - ⭐ 865
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

401. **[awesome-mcp-list](https://github.com/MobinX/awesome-mcp-list)** - ⭐ 865
   A concise list for mcp servers

402. **[OpenDerisk](https://github.com/derisk-ai/OpenDerisk)** - ⭐ 861
   AI-Native Risk Intelligence Systems, OpenDeRisk——Your application system risk intelligent manager provides 7* 24-hour comprehensive and in-depth protection.

403. **[claude-delegator](https://github.com/jarrodwatts/claude-delegator)** - ⭐ 860
   Delegate tasks to Codex GPT 5.2 directly from within Claude Code.

404. **[mcp-notion-server](https://github.com/suekou/mcp-notion-server)** - ⭐ 859

405. **[excel-mcp-server](https://github.com/negokaz/excel-mcp-server)** - ⭐ 856
   A Model Context Protocol (MCP) server that reads and writes MS Excel data

406. **[CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)** - ⭐ 851
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

407. **[claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)** - ⭐ 850
   Personal AI CLI configuration for academic research & software development. Supports Claude Code, OpenCode, and Codex CLI — covering the full research lifecycle from ideation to publication.

408. **[openapi-servers](https://github.com/open-webui/openapi-servers)** - ⭐ 847
   OpenAPI Tool Servers

409. **[wassette](https://github.com/microsoft/wassette)** - ⭐ 846
   Wassette: A security-oriented runtime that runs WebAssembly Components via MCP

410. **[mcp-sequential-thinking](https://github.com/arben-adm/mcp-sequential-thinking)** - ⭐ 844

411. **[kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server)** - ⭐ 838
   A Model Context Protocol (MCP) server for Kubernetes. Install: npx kubectl-mcp-server or pip install kubectl-mcp-server

412. **[CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI)** - ⭐ 838
   CyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.

413. **[hyper-mcp](https://github.com/tuananh/hyper-mcp)** - ⭐ 835
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

414. **[hyper-mcp](https://github.com/joseph-wortmann/hyper-mcp)** - ⭐ 834
   📦️ A fast, secure MCP server that extends its capabilities through WebAssembly plugins.

415. **[scira-mcp-chat](https://github.com/zaidmukaddam/scira-mcp-chat)** - ⭐ 830
   A minimalistic MCP client with a good feature set.

416. **[yokai](https://github.com/ankorstore/yokai)** - ⭐ 822
   Simple, modular, and observable Go framework for backend applications.

417. **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** - ⭐ 819
   Scan MCP servers for potential threats & security findings.

418. **[statespace](https://github.com/statespace-tech/statespace)** - ⭐ 818
   Interactive web apps for AI agents

419. **[duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)** - ⭐ 818
   A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing.

420. **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** - ⭐ 817
   The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store.

421. **[arcade-mcp](https://github.com/ArcadeAI/arcade-mcp)** - ⭐ 815
   The best way to create, deploy, and share MCP Servers

422. **[supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server)** - ⭐ 813
   Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more.

423. **[server](https://github.com/php-mcp/server)** - ⭐ 813
   Core PHP implementation for the Model Context Protocol (MCP) server

424. **[golf](https://github.com/golf-mcp/golf)** - ⭐ 811
   Production-Ready MCP Server Framework • Build, deploy & scale secure AI agent infrastructure • Includes Auth, Observability, Debugger, Telemetry & Runtime • Run real-world MCPs powering AI Agents 

425. **[MassGen](https://github.com/massgen/MassGen)** - ⭐ 810
   🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. | Join us on Discord: discord.massgen.ai

426. **[toolfront](https://github.com/statespace-tech/toolfront)** - ⭐ 809
   Turn your data into shareable RAG apps in minutes. All in pure Markdown. Zero boilerplate.

427. **[browser-use-mcp-server](https://github.com/kontext-dev/browser-use-mcp-server)** - ⭐ 806
   Browse the web, directly from Cursor etc.

428. **[DeepMCPAgent](https://github.com/cryxnet/DeepMCPAgent)** - ⭐ 804
   Model-agnostic plug-n-play LangChain/LangGraph agents powered entirely by MCP tools over HTTP/SSE.

429. **[MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)** - ⭐ 804
   A comprehensive security checklist for MCP-based AI tools. Built by SlowMist to safeguard LLM plugin ecosystems.

430. **[context-space](https://github.com/context-space/context-space)** - ⭐ 802
   Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations

431. **[mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph)** - ⭐ 800
   MCP server enabling persistent memory for Claude through a local knowledge graph - fork focused on local development

432. **[qgis_mcp](https://github.com/jjsantos01/qgis_mcp)** - ⭐ 800
   Model Context Protocol (MCP) that allows LLMs to use QGIS Desktop

433. **[acemcp](https://github.com/qy527145/acemcp)** - ⭐ 798
   一个将ACE(Augment Context Engine) 做成MCP的项目

434. **[bank-api](https://github.com/erwinkramer/bank-api)** - ⭐ 796
   The Bank API is a design reference project suitable to bootstrap development for a compliant and modern API.

435. **[code-index-mcp](https://github.com/johnhuang316/code-index-mcp)** - ⭐ 793
   A Model Context Protocol (MCP) server that helps large language models index, search, and analyze code repositories with minimal setup

436. **[agent-kit](https://github.com/inngest/agent-kit)** - ⭐ 791
   AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP.

437. **[k8m](https://github.com/weibaohui/k8m)** - ⭐ 788
   一款轻量级、跨平台的 Mini Kubernetes AI Dashboard，支持大模型+智能体+MCP(支持设置操作权限)，集成多集群管理、智能分析、实时异常检测等功能，支持多架构并可单文件部署，助力高效集群管理与运维优化。

438. **[coderunner](https://github.com/instavm/coderunner)** - ⭐ 786
   A secure local sandbox to run LLM-generated code using Apple containers

439. **[drawio-mcp](https://github.com/jgraph/drawio-mcp)** - ⭐ 780

440. **[vllora](https://github.com/vllora/vllora)** - ⭐ 779
   Debug your AI agents

441. **[heurist-agent-framework](https://github.com/heurist-network/heurist-agent-framework)** - ⭐ 779
   A flexible multi-interface AI agent framework for building agents with reasoning, tool use, memory, deep research, blockchain interaction, MCP, and agents-as-a-service.

442. **[Context](https://github.com/indragiek/Context)** - ⭐ 778
   Native macOS client for Model Context Protocol (MCP)

443. **[glean](https://github.com/LeslieLeung/glean)** - ⭐ 776
   A self-hosted RSS reader and personal knowledge management tool.

444. **[vibetest-use](https://github.com/browser-use/vibetest-use)** - ⭐ 768
   Vibetest MCP - automated QA testing using Browser-Use agents

445. **[runno](https://github.com/taybenlor/runno)** - ⭐ 760
   Sandboxed runtime for programming languages and WASI binaries. Works in the browser, on your server, or via MCP.

446. **[mcp-server](https://github.com/financial-datasets/mcp-server)** - ⭐ 758
   An MCP server for interacting with the Financial Datasets stock market API.

447. **[drift](https://github.com/dadbodgeoff/drift)** - ⭐ 754
   Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI.

448. **[mcp-marketplace](https://github.com/cline/mcp-marketplace)** - ⭐ 753
   This is the official repository for submitting MCP servers to be included in Cline's MCP Marketplace. If you’ve built an MCP server and want it to be discoverable and easily installable by millions of developers using Cline, submit your server here.

449. **[AITreasureBox](https://github.com/superiorlu/AITreasureBox)** - ⭐ 749
   🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎 

450. **[context-portal](https://github.com/GreatScottyMac/context-portal)** - ⭐ 748
   Context Portal (ConPort): A memory bank MCP server building a project-specific knowledge graph to supercharge AI assistants. Enables powerful Retrieval Augmented Generation (RAG) for context-aware development in your IDE.

451. **[telegram-mcp](https://github.com/chigwell/telegram-mcp)** - ⭐ 743
   Telegram MCP server powered by Telethon to let MCP clients read chats, manage groups, and send/modify messages, media, contacts, and settings.

452. **[annas-mcp](https://github.com/iosifache/annas-mcp)** - ⭐ 742
   MCP server and CLI tool for searching and downloading documents from Anna's Archive

453. **[lisa.py](https://github.com/ant4g0nist/lisa.py)** - ⭐ 740
   LLDB MCP Integration + other helpful commands

454. **[mcp](https://github.com/hyperbrowserai/mcp)** - ⭐ 738
   A MCP server implementation for hyperbrowser

455. **[octocode-mcp](https://github.com/bgauryy/octocode-mcp)** - ⭐ 735
   MCP server for semantic code research and context generation on real-time using LLM patterns | Search naturally across public & private repos based on your permissions | Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows | Find real implementations and live docs from anywhere

456. **[ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)** - ⭐ 733
   The official Ruby SDK for the Model Context Protocol.

457. **[12306-mcp](https://github.com/Joooook/12306-mcp)** - ⭐ 731
   This is a 12306 ticket search server based on the Model Context Protocol (MCP).

458. **[openmcp-client](https://github.com/LSTM-Kirigaya/openmcp-client)** - ⭐ 728
   All in one vscode plugin for mcp developer

459. **[drawio-mcp-server](https://github.com/lgazo/drawio-mcp-server)** - ⭐ 726
   Draw.io Model Context Protocol (MCP) Server

460. **[just-prompt](https://github.com/disler/just-prompt)** - ⭐ 717
   just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)

461. **[passage-of-time-mcp](https://github.com/jlumbroso/passage-of-time-mcp)** - ⭐ 713
   🤖🕰️ An MCP server that gives language models temporal awareness and time calculation abilities. Teaching AI the significance of the passage of time through collaborative tool development.

462. **[llm-functions](https://github.com/sigoden/llm-functions)** - ⭐ 712
   Easily create LLM tools and agents using plain Bash/JavaScript/Python functions.

463. **[paper-search-mcp](https://github.com/openags/paper-search-mcp)** - ⭐ 712
   A MCP for searching and downloading academic papers from multiple sources like arXiv, PubMed, bioRxiv, etc.

464. **[mcpcan](https://github.com/Kymo-MCP/mcpcan)** - ⭐ 705
   MCPCAN is a centralized management platform for MCP services. It deploys each MCP service using a container deployment method. The platform supports container monitoring and MCP service token verification, solving security risks and enabling rapid deployment of MCP services. It uses SSE, STDIO, and STREAMABLEHTTP access protocols to deploy MCP。

465. **[burp-ai-agent](https://github.com/six2dez/burp-ai-agent)** - ⭐ 705
   Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls, passive and active scanning and more

466. **[mcp-google-sheets](https://github.com/xing5/mcp-google-sheets)** - ⭐ 704
   This MCP server integrates with your Google Drive and Google Sheets, to enable creating and modifying spreadsheets.

467. **[llm-server-docs](https://github.com/varunvasudeva1/llm-server-docs)** - ⭐ 702
   End-to-end documentation to set up your own local & fully private LLM server on Debian. Equipped with chat, web search, RAG, model management, MCP servers, image generation, and TTS.

468. **[fetch-mcp](https://github.com/zcaceres/fetch-mcp)** - ⭐ 696
   A flexible HTTP fetching Model Context Protocol server.

469. **[mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse)** - ⭐ 695
   Connect ClickHouse to your AI assistants.

470. **[HowToCook-mcp](https://github.com/worryzyy/HowToCook-mcp)** - ⭐ 694
   基于Anduin2017 / HowToCook （程序员在家做饭指南）的mcp server

471. **[brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)** - ⭐ 694

472. **[awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw)** - ⭐ 693
   A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations.

473. **[clojure-mcp](https://github.com/bhauman/clojure-mcp)** - ⭐ 692
   Clojure MCP

474. **[macos-automator-mcp](https://github.com/steipete/macos-automator-mcp)** - ⭐ 690
   An MCP server to run AppleScript and JXA (JavaScript for Automation) to macOS.

475. **[langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)** - ⭐ 688
   LangGraph-powered ReAct agent with Model Context Protocol (MCP) integration. A Streamlit web interface for dynamically configuring, deploying, and interacting with AI agents capable of accessing various data sources and APIs through MCP tools.

476. **[gcloud-mcp](https://github.com/googleapis/gcloud-mcp)** - ⭐ 685
   gcloud MCP server

477. **[mcp](https://github.com/laravel/mcp)** - ⭐ 683
   Rapidly build MCP servers for your Laravel applications.

478. **[cuga-agent](https://github.com/cuga-project/cuga-agent)** - ⭐ 682
   CUGA is an open-source generalist agent for the enterprise, supporting complex task execution on web and APIs, OpenAPI/MCP integrations, composable architecture, reasoning modes, and policy-aware features.

479. **[nuwax](https://github.com/nuwax-ai/nuwax)** - ⭐ 681
   Nuwax Agent OS - The world's first universal agent operating system, building your private vertical general-purpose agent.  全球首个通用智能体操作系统，打造你私有的垂类通用智能体。新一代AI应用设计、开发、实践平台，无需代码，轻松创建，适合各类人群，支持多种端发布及API，提供完善的工作流、插件以及应用开发能力，RAG知识库与数据表存储能力，MCP接入以及开放能力。

480. **[mcp-server-docker](https://github.com/ckreiling/mcp-server-docker)** - ⭐ 678
   MCP server for Docker

481. **[open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent)** - ⭐ 673
   An open source implementation of code execution with MCP (Programatic Tool Calling) 

482. **[android-mcp-server](https://github.com/minhalvp/android-mcp-server)** - ⭐ 672
   An MCP server that provides control over Android devices via adb

483. **[mcp-client-cli](https://github.com/adhikasp/mcp-client-cli)** - ⭐ 667
   A simple CLI to run LLM prompt and implement MCP client.

484. **[go-mcp](https://github.com/ThinkInAIXYZ/go-mcp)** - ⭐ 666
   Go-MCP is a powerful Go(Golang) version of the MCP SDK that implements the Model Context Protocol (MCP) to facilitate seamless communication between external systems and AI applications. 

485. **[figma-console-mcp](https://github.com/southleft/figma-console-mcp)** - ⭐ 662
   Your design system as an API. Connect AI to Figma for extraction, creation, and debugging.

486. **[awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)** - ⭐ 658
   🔥🔒 Awesome MCP (Model Context Protocol) Security 🖥️

487. **[yacy_grid_mcp](https://github.com/yacy/yacy_grid_mcp)** - ⭐ 655
   The YaCy Grid Master Connect Program

488. **[mcp-mem0](https://github.com/coleam00/mcp-mem0)** - ⭐ 651
   MCP server for long term agent memory with Mem0. Also useful as a template to get you started building your own MCP server with Python!

489. **[laravel-restify](https://github.com/BinarCode/laravel-restify)** - ⭐ 649
   Laravel API for Ai Agents and humans.

490. **[next-devtools-mcp](https://github.com/vercel/next-devtools-mcp)** - ⭐ 649
   Next.js Development for Coding Agent

491. **[llm-search](https://github.com/snexus/llm-search)** - ⭐ 649
   Querying local documents, powered by LLM

492. **[mcp-proxy](https://github.com/tbxark/mcp-proxy)** - ⭐ 645
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

493. **[wcgw](https://github.com/rusiaaman/wcgw)** - ⭐ 645
   Shell and coding agent on mcp clients

494. **[samples](https://github.com/strands-agents/samples)** - ⭐ 644
   Agent samples built using the Strands Agents SDK.

495. **[skybridge](https://github.com/alpic-ai/skybridge)** - ⭐ 644
   Skybridge is a framework for building ChatGPT & MCP Apps

496. **[enrichmcp](https://github.com/featureform/enrichmcp)** - ⭐ 642
   EnrichMCP is a python framework for building data driven MCP servers

497. **[obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** - ⭐ 642
   A simple MCP server for Obsidian

498. **[claude-code-plugins-plus](https://github.com/jeremylongshore/claude-code-plugins-plus)** - ⭐ 641
   Claude Code Plugins Hub — browse and install 243 plugins (175 with Agent Skills v1.2.0). First 100% compliant with Anthropic 2025 Skills schema.

499. **[TuriX-CUA](https://github.com/TurixAI/TuriX-CUA)** - ⭐ 639
   This is the official website for TuriX Computer-use-Agent

500. **[RAGLight](https://github.com/Bessouat40/RAGLight)** - ⭐ 638
   RAGLight is a modular framework for Retrieval-Augmented Generation (RAG). It makes it easy to plug in different LLMs, embeddings, and vector stores, and now includes seamless MCP integration to connect external tools and data sources.

501. **[python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)** - ⭐ 637
   Official python implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

502. **[douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)** - ⭐ 631
   提取抖音无水印视频链接，视频文案，douyin-mcp-server，mcp，claude skill

503. **[workers-mcp](https://github.com/cloudflare/workers-mcp)** - ⭐ 628
   Talk to a Cloudflare Worker from Claude Desktop!

504. **[mcp-proxy](https://github.com/TBXark/mcp-proxy)** - ⭐ 624
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single HTTP server.

505. **[notebooklm-mcp](https://github.com/jacob-bd/notebooklm-mcp)** - ⭐ 624

506. **[obot](https://github.com/obot-platform/obot)** - ⭐ 623
   Complete MCP Platform -- Hosting, Registry, Gateway, and Chat Client

507. **[headroom](https://github.com/chopratejas/headroom)** - ⭐ 621
   The Context Optimization Layer for LLM Applications

508. **[a-share-mcp-is-just-i-need](https://github.com/24mlight/a-share-mcp-is-just-i-need)** - ⭐ 618

509. **[yargi-mcp](https://github.com/saidsurucu/yargi-mcp)** - ⭐ 615
   MCP Server For Turkish Legal Databases

510. **[mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** - ⭐ 615

511. **[vibe](https://github.com/mondaycom/vibe)** - ⭐ 614
   🎨 Vibe Design System - Official monday.com UI resources for application development in React.js

512. **[phpMyFAQ](https://github.com/thorsten/phpMyFAQ)** - ⭐ 610
   phpMyFAQ - Open Source FAQ web application for PHP 8.3+ and MySQL, PostgreSQL and other databases

513. **[mem-agent-mcp](https://github.com/firstbatchxyz/mem-agent-mcp)** - ⭐ 610
   mem-agent mcp server

514. **[reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant)** - ⭐ 607
   MCP server for reverse engineering tasks in Ghidra 👩‍💻

515. **[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** - ⭐ 607
   Add Obsidian integrations like semantic search and custom Templater prompts to Claude or any MCP client.

516. **[awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit)** - ⭐ 604
   The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+15,000 via SkillKit), 42 commands, 120 plugins, 19 hooks, 15 rules, 7 templates, 6 MCP configs, and more.

517. **[mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** - ⭐ 603
   Go server implementing Model Context Protocol (MCP) for filesystem operations.

518. **[mem0-mcp](https://github.com/mem0ai/mem0-mcp)** - ⭐ 603

519. **[mcp-link](https://github.com/automation-ai-labs/mcp-link)** - ⭐ 600
   Convert Any OpenAPI V3 API to MCP Server

520. **[FofaMap](https://github.com/asaotomo/FofaMap)** - ⭐ 600
   FofaMap v2.0 是一款基于 Python3 开发的全网首个 AI 驱动红队资产测绘智能体。在延续原有 FOFA 数据采集、存活检测、统计聚合、图标 Hash 及批量查询等核心功能的基础上，2.0 版本原生支持 MCP 协议，可无缝接入 Cursor、Claude 等 AI 平台。其核心内置了 AI 自我反思机制，能根据查询结果自动调优语法，并智能联动 Nuclei 推荐精准扫描策略，实现从“被动采集”到“主动智能决策”的红队作业进化。

521. **[daydreams](https://github.com/daydreamsai/daydreams)** - ⭐ 599
   Daydreams is a set of tools for building agents for commerce

522. **[Wax](https://github.com/christopherkarani/Wax)** - ⭐ 596
   🍯 Memory layer for on-device AI Agents. Replace complex RAG pipelines with a serverless, single-file memory layer. 

523. **[awesome-web3-mcp-servers](https://github.com/demcp/awesome-web3-mcp-servers)** - ⭐ 595
   DeMCP is the first Decentralized MCP network, offering SSE proxies for MCP services and mainstream LLMs, tackling trust and security with TEE and blockchain.

524. **[flow-like](https://github.com/TM9657/flow-like)** - ⭐ 594
   Flow-Like: Strongly Typed Enterprise Scale Workflows. Built for scalability, speed, seamless AI integration and rich customization.

525. **[FantasyPremierLeague](https://github.com/joreilly/FantasyPremierLeague)** - ⭐ 593
   Fantasy Premier League Kotlin/Compose Multiplatform sample 

526. **[tome](https://github.com/runebookai/tome)** - ⭐ 590
   a magical LLM desktop client that makes it easy for *anyone* to use LLMs and MCP

527. **[cupertino](https://github.com/mihaelamj/cupertino)** - ⭐ 589
   A local Apple Documentation crawler and MCP server. Written in Swift.

528. **[FLUJO](https://github.com/mario-andreschak/FLUJO)** - ⭐ 588
   MCP-Hub and -Inspector, Multi-Model Workflow and Chat Interface 

529. **[MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** - ⭐ 587
   A NestJS module to effortlessly create Model Context Protocol (MCP) servers for exposing AI tools, resources, and prompts.

530. **[mcp-adapter](https://github.com/WordPress/mcp-adapter)** - ⭐ 587
   An MCP adapter that bridges the Abilities API to the Model Context Protocol, enabling MCP clients to discover and invoke WordPress plugin, theme, and core abilities programmatically.

531. **[dexto](https://github.com/truffle-ai/dexto)** - ⭐ 584
   A coding agent and general agent harness for building and orchestrating agentic applications.

532. **[blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp)** - ⭐ 581
   Diagram generation for understanding codebases and system architecture using Nano Banana Pro.

533. **[spotify-mcp](https://github.com/varunneal/spotify-mcp)** - ⭐ 579
   MCP to connect your LLM with Spotify.

534. **[langgraph-mcp](https://github.com/esxr/langgraph-mcp)** - ⭐ 575
   LangGraph solution template for MCP

535. **[sentry-mcp](https://github.com/getsentry/sentry-mcp)** - ⭐ 572
   An MCP server for interacting with Sentry via LLMs.

536. **[cclsp](https://github.com/ktnyt/cclsp)** - ⭐ 571
   Claude Code LSP: enhance your Claude Code experience with non-IDE dependent LSP integration.

537. **[mcp-sequentialthinking-tools](https://github.com/spences10/mcp-sequentialthinking-tools)** - ⭐ 567
   🧠 An adaptation of the MCP Sequential Thinking Server to guide tool usage. This server provides recommendations for which MCP tools would be most effective at each stage.

538. **[mcp-handler](https://github.com/vercel/mcp-handler)** - ⭐ 567
   Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more

539. **[Overture](https://github.com/SixHq/Overture)** - ⭐ 565
   Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. 

540. **[mcp-pointer](https://github.com/etsd-tech/mcp-pointer)** - ⭐ 564
   MCP tool: let you point at DOM elements for your favorite agentic coding tool. Let AI see what you see.

541. **[mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian)** - ⭐ 564
   A lightweight Model Context Protocol (MCP) server for safe Obsidian vault access

542. **[manim-mcp-server](https://github.com/abhiemj/manim-mcp-server)** - ⭐ 563

543. **[apple-doc-mcp](https://github.com/MightyDillah/apple-doc-mcp)** - ⭐ 562
   MCP server providing seamless access to Apple Developer Documentation with smart search and wildcard support

544. **[MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe)** - ⭐ 561
   MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents

545. **[LLMTornado](https://github.com/lofcz/LLMTornado)** - ⭐ 561
   The .NET library to build AI agents with 30+ built-in connectors.

546. **[generative-ui](https://github.com/CopilotKit/generative-ui)** - ⭐ 560
   Generative UI examples for: AG-UI, A2UI/Open-JSON-UI, and MCP Apps.

547. **[web-search-mcp](https://github.com/mrkrsl/web-search-mcp)** - ⭐ 560
   A simple, locally hosted Web Search MCP server for use with Local LLMs

548. **[davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)** - ⭐ 559
   MCP server integration for DaVinci Resolve

549. **[wren-engine](https://github.com/Canner/wren-engine)** - ⭐ 558
   🤖 The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents 🔥 

550. **[mcp-for-security](https://github.com/cyproxio/mcp-for-security)** - ⭐ 558
   MCP for Security: A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

551. **[mcp-server-neon](https://github.com/neondatabase/mcp-server-neon)** - ⭐ 557
   MCP server for interacting with Neon Management API and databases

552. **[caswaf](https://github.com/casbin/caswaf)** - ⭐ 555
   Casbin AI & MCP security gateway for HTTP, online demo: https://door.caswaf.com

553. **[awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers)** - ⭐ 554
   A comprehensive collection of Model Context Protocol (MCP) servers

554. **[google-search](https://github.com/web-agent-master/google-search)** - ⭐ 553
   A Playwright-based Node.js tool that bypasses search engine anti-scraping mechanisms to execute Google searches. Local alternative to SERP APIs with MCP server integration.

555. **[freecad-mcp](https://github.com/neka-nat/freecad-mcp)** - ⭐ 553
   FreeCAD MCP(Model Context Protocol) server

556. **[evo-ai](https://github.com/EvolutionAPI/evo-ai)** - ⭐ 552
   Evo AI is an open-source platform for creating and managing AI agents, enabling integration with different AI models and services.

557. **[mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)** - ⭐ 552
   A text-based user interface (TUI) client for interacting with MCP servers using Ollama. Features include agent mode, multi-server, model switching, streaming responses, tool management, human-in-the-loop, thinking mode, model params config, MCP prompts, custom system prompt and saved preferences. Built for developers working with local LLMs.

558. **[homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp)** - ⭐ 547
   A MCP server for Home Assistant

559. **[vite-plugin-vue-mcp](https://github.com/webfansplz/vite-plugin-vue-mcp)** - ⭐ 546
   Vite plugin that enables a MCP server helping models to understand your Vue app better.

560. **[mcp.el](https://github.com/lizqwerscott/mcp.el)** - ⭐ 546
   An Mcp client inside Emacs

561. **[mcp-shield](https://github.com/riseandignite/mcp-shield)** - ⭐ 545
   Security scanner for MCP servers

562. **[multimodal-agents-course](https://github.com/the-ai-merge/multimodal-agents-course)** - ⭐ 543
   An MCP Multimodal AI Agent with eyes and ears!

563. **[echokit_server](https://github.com/second-state/echokit_server)** - ⭐ 543
   Open Source Voice Agent Platform

564. **[cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)** - ⭐ 542
   MCP server to deploy apps to Cloud Run

565. **[AnyTool](https://github.com/HKUDS/AnyTool)** - ⭐ 542
   "AnyTool: Universal Tool-Use Layer for AI Agents"

566. **[FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline)** - ⭐ 541
   FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestration. It facilitates transparent, human-in-the-loop creation with reusable Style Skills for consistent, professional storytelling.

567. **[Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)** - ⭐ 539
   A structural code search engine for Al agents.

568. **[tda](https://github.com/irockel/tda)** - ⭐ 537
   TDA - Thread Dump Analyzer (for Java). Analyze your Thread Dumps with a GUI or use it as MCP Server.

569. **[universal-db-mcp](https://github.com/Anarkh-Lee/universal-db-mcp)** - ⭐ 537
   通用数据库 MCP 连接器：支持 MySQL、PostgreSQL、Oracle、MongoDB 等 17 种数据库，支持 Claude Desktop、Cursor、Windsurf、VS Code、ChatGPT 等 50+ 平台，用自然语言查询和分析数据

570. **[fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)** - ⭐ 536
   A modern template for agentic orchestration — built for rapid iteration and scalable deployment using highly customizable, community-supported tools like MCP, LangGraph, and more.

571. **[pg-mcp-server](https://github.com/stuzero/pg-mcp-server)** - ⭐ 535

572. **[cli](https://github.com/smithery-ai/cli)** - ⭐ 532
   Install, manage and develop MCP servers and skills for agents

573. **[dolphin-mcp](https://github.com/QuixiAI/dolphin-mcp)** - ⭐ 531

574. **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** - ⭐ 531
   MCP server to manage Facebook and Instagram Ads (Meta Ads)

575. **[iterm-mcp](https://github.com/ferrislucas/iterm-mcp)** - ⭐ 529
   A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance

576. **[mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)** - ⭐ 526

577. **[alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)** - ⭐ 525
   Alpaca’s official MCP Server lets you trade stocks, ETFs, crypto, and options, run data analysis, and build strategies in plain English directly from your favorite LLM tools and IDEs

578. **[openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator)** - ⭐ 525
   A tool that converts OpenAPI specifications to MCP server

579. **[WebMCP](https://github.com/jasonjmcghee/WebMCP)** - ⭐ 525
   Early WebMCP proposal / implementation - since evolved and worked on by much more capable folks that develop the web: https://github.com/webmachinelearning/webmcp

580. **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** - ⭐ 524
   MCP server that integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.

581. **[pgmcp](https://github.com/subnetmarco/pgmcp)** - ⭐ 523
   An MCP server to query any Postgres database in natural language.

582. **[pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp)** - ⭐ 523
   📄 Production-ready MCP server for PDF processing - 5-10x faster with parallel processing and 94%+ test coverage

583. **[awesome-a2a](https://github.com/ai-boost/awesome-a2a)** - ⭐ 522
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place.

584. **[ethora](https://github.com/dappros/ethora)** - ⭐ 521
   Open-source engine for chat 💬, AI assistants 🤖 & wallets 🪪. React, Typescript, Python, XMPP. Build future apps with chat, AI agents and web3.

585. **[ida-mcp-server](https://github.com/MxIris-Reverse-Engineering/ida-mcp-server)** - ⭐ 520
   A Model Context Protocol server for IDA

586. **[mcp-server-weread](https://github.com/freestylefly/mcp-server-weread)** - ⭐ 520
   微信读书MCP

587. **[apple-health-mcp](https://github.com/neiltron/apple-health-mcp)** - ⭐ 518
   MCP server for querying Apple Health data with natural language and SQL

588. **[gateway](https://github.com/centralmind/gateway)** - ⭐ 517
   Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.

589. **[flux-operator](https://github.com/controlplaneio-fluxcd/flux-operator)** - ⭐ 516
   GitOps on Autopilot Mode

590. **[engram](https://github.com/Gentleman-Programming/engram)** - ⭐ 516
   Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

591. **[ghostcrew](https://github.com/GH05TCREW/ghostcrew)** - ⭐ 515
   GhostCrew is an AI agent framework for bug bounty hunting, red-team operations, pentesting, and operator education. It integrates LLM autonomy, multi-agent coordination, and MCP extensibility with a minimal core toolset, supported by RAG for context-aware reasoning, a persistent internal state, reproducible workflows, and interactive assistance.

592. **[UnrealMCP](https://github.com/kvick-games/UnrealMCP)** - ⭐ 515
   MCP to allow AI agents to control Unreal

593. **[work-iq-mcp](https://github.com/microsoft/work-iq-mcp)** - ⭐ 514
   MCP Server and CLI for accessing Work IQ

594. **[mineru-tianshu](https://github.com/magicyuan876/mineru-tianshu)** - ⭐ 513
   天枢 - 企业级 AI 一站式数据预处理平台 | PDF/Office转Markdown | 支持MCP协议AI助手集成 | Vue3+FastAPI全栈方案 | 文档解析 | 多模态信息提取

595. **[bm.md](https://github.com/miantiao-me/bm.md)** - ⭐ 510
   更好用的 Markdown 排版助手｜一键适配微信公众号、网页与图片。

596. **[MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP)** - ⭐ 509
   MCP Server for Metasploit

597. **[talk-to-girlfriend-ai](https://github.com/arlanrakh/talk-to-girlfriend-ai)** - ⭐ 508
   im busy building ai agents so why not let an ai talk to my girlfriend? (i am single) 

598. **[awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins)** - ⭐ 508
   Awesome Claude Code plugins — a curated list of slash commands, subagents, MCP servers, and hooks for Claude Code

599. **[multimodal-agents-course](https://github.com/multi-modal-ai/multimodal-agents-course)** - ⭐ 507
   An MCP Multimodal AI Agent with eyes and ears!

600. **[unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp)** - ⭐ 507
   Control Unreal Engine 5.5+ through AI with natural language. Build incredible 3D worlds and architectural masterpieces using MCP. Create entire towns, medieval castles, modern mansions, challenging mazes, and complex structures with AI-powered commands.

601. **[mcp-get](https://github.com/michaellatman/mcp-get)** - ⭐ 506

602. **[MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server)** - ⭐ 506
   MCP configuration to connect AI agent to a Linux machine.

603. **[rails-mcp-server](https://github.com/maquina-app/rails-mcp-server)** - ⭐ 504
   A Ruby gem implementation of a Model Context Protocol (MCP) server for Rails projects. This server allows LLMs (Large Language Models) to interact with Rails projects through the Model Context Protocol.

604. **[UnityMCP](https://github.com/jackwrichards/UnityMCP)** - ⭐ 504

605. **[mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)** - ⭐ 502
   Yes Mcp server in bash

606. **[mcp-pandoc](https://github.com/vivekVells/mcp-pandoc)** - ⭐ 501
   MCP server for document format conversion using pandoc.

607. **[borsa-mcp](https://github.com/saidsurucu/borsa-mcp)** - ⭐ 501
   MCP Server for Turkish & American Stock Exchange and Fund Data

608. **[mcp-server](https://github.com/PortSwigger/mcp-server)** - ⭐ 501
   MCP Server for Burp

609. **[MCPSpy](https://github.com/alex-ilgayev/MCPSpy)** - ⭐ 498
   MCP Monitoring with eBPF

610. **[chroma-mcp](https://github.com/chroma-core/chroma-mcp)** - ⭐ 498
   A Model Context Protocol (MCP) server implementation that provides database capabilities for Chroma

611. **[dbt-mcp](https://github.com/dbt-labs/dbt-mcp)** - ⭐ 496
   A MCP (Model Context Protocol) server for interacting with dbt.

612. **[mcp-youtube](https://github.com/anaisbetts/mcp-youtube)** - ⭐ 495
   A Model-Context Protocol Server for YouTube

613. **[cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server)** - ⭐ 494
   一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start.

614. **[PentestAgent](https://github.com/GH05TCREW/PentestAgent)** - ⭐ 493
   All-in-one offensive security toolbox with AI agent and MCP architecture. Integrates tools like Nmap, Metasploit, FFUF, SQLMap. Enables pentesting, bug bounty hunting, threat hunting, and reporting. RAG-based responses with local knowledge base support.

615. **[GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP)** - ⭐ 493
   An MCP extension for Ghidra

616. **[web-agent-protocol](https://github.com/OTA-Tech-AI/web-agent-protocol)** - ⭐ 492
   🌐Web Agent Protocol (WAP) - Record and replay user interactions in the browser with MCP support

617. **[llm-mcp-rag](https://github.com/KelvinQiu802/llm-mcp-rag)** - ⭐ 492
   LLM + MCP + RAG = Magic

618. **[UnityMCP](https://github.com/Arodoid/UnityMCP)** - ⭐ 491

619. **[sdk-typescript](https://github.com/strands-agents/sdk-typescript)** - ⭐ 491
   A model-driven approach to building AI agents in just a few lines of code. 

620. **[n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder)** - ⭐ 490
   AI assistant integration for n8n workflow automation through Model Context Protocol (MCP). Connect Claude Desktop, ChatGPT, and other AI assistants to n8n for natural language workflow management.

621. **[ai-trader](https://github.com/whchien/ai-trader)** - ⭐ 490
   Backtrader-powered backtesting framework for algorithmic trading, featuring 20+ strategies, multi-market support, CLI tools, and an integrated MCP server for professional traders.

622. **[minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server)** - ⭐ 489
   A Minecraft MCP Server powered by Mineflayer API. It allows to control a Minecraft character in real-time, allowing AI assistants to build structures, explore the world, and interact with the game environment through natural language instruction

623. **[MCP](https://github.com/jina-ai/MCP)** - ⭐ 489
   Official Jina AI Remote MCP Server

624. **[mcp-gateway](https://github.com/microsoft/mcp-gateway)** - ⭐ 489
   MCP Gateway is a reverse proxy and management layer for MCP servers, enabling scalable, session-aware stateful routing and lifecycle management of MCP servers in Kubernetes environments.

625. **[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server)** - ⭐ 489
   A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API

626. **[haiku.rag](https://github.com/ggozad/haiku.rag)** - ⭐ 488
   Opinionated agentic RAG powered by LanceDB, Pydantic AI, and Docling

627. **[lanhu-mcp](https://github.com/dsphper/lanhu-mcp)** - ⭐ 488
   ⚡ 需求分析效率提升 200%！全球首个为 AI 编程时代设计的团队协作 MCP 服务器，自动分析需求自动编写前后端代码，下载切图

628. **[claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you)** - ⭐ 487
   Enable any LLM (e.g. Claude) to interactively debug any language for you via MCP and a VS Code Extension

629. **[mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng)** - ⭐ 487
   MCP Server for SearXNG

630. **[mcpe](https://github.com/ReMinecraftPE/mcpe)** - ⭐ 486
   ReMinecraftPE - A custom experience based on Minecraft PE as of 2011.

631. **[adb-mcp](https://github.com/mikechambers/adb-mcp)** - ⭐ 482

632. **[tsidp](https://github.com/tailscale/tsidp)** - ⭐ 481
   A simple OIDC / OAuth Identity Provider (IdP) server for your tailnet.

633. **[mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** - ⭐ 481
   This is an MCP server that allows you to directly download transcripts of YouTube videos.

634. **[concierge](https://github.com/concierge-hq/concierge)** - ⭐ 479
   🚀 Universal SDK for building next-gen MCP servers

635. **[argo](https://github.com/xark-argo/argo)** - ⭐ 478
   ARGO is an open-source AI Agent platform that brings Local Manus to your desktop. With one-click model downloads, seamless closed LLM integration, and offline-first RAG knowledge bases, ARGO becomes a DeepResearch powerhouse for autonomous thinking, task planning, and 100% of your data stays locally. Support Win/Mac/Docker.

636. **[mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** - ⭐ 476
   MCP Server to interact with Google Gsuite prodcuts

637. **[agentscope-runtime](https://github.com/agentscope-ai/agentscope-runtime)** - ⭐ 476
   A production-ready runtime framework for agent apps with secure tool sandboxing, Agent-as-a-Service APIs, scalable deployment, full-stack observability, and broad framework compatibility.

638. **[open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)** - ⭐ 473
   The open-source multi-agent chat interface that lets you manage multiple agents in one dynamic conversation and add MCP servers for deep research

639. **[vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server)** - ⭐ 473
   Vibe Check is a tool that provides mentor-like feedback to AI Agents, preventing tunnel-vision, over-engineering and reasoning lock-in for complex and long-horizon agent workflows. KISS your over-eager AI Agents goodbye! Effective for: Coding, Ambiguous Tasks, High-Risk tasks

640. **[lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)** - ⭐ 473
   飞书/Lark官方 OpenAPI MCP

641. **[prism-insight](https://github.com/dragon1086/prism-insight)** - ⭐ 472
   AI-based stock analysis and trading system

642. **[Godot-MCP](https://github.com/ee0pdt/Godot-MCP)** - ⭐ 472
   An MCP for Godot that lets you create and edit games in the Godot game engine with tools like Claude

643. **[laravel](https://github.com/php-mcp/laravel)** - ⭐ 470
   An SDK building Laravel MCP servers

644. **[aser](https://github.com/AmeNetwork/aser)** - ⭐ 469
   Aser is a lightweight, self-assembling AI Agent frame.

645. **[copilot-mcp](https://github.com/VikashLoomba/copilot-mcp)** - ⭐ 469
   A VSCode extension that lets you find and install Agent Skills and MCP Apps to use with GitHub Copilot, Claude Code, and Codex CLI.

646. **[atlas-mcp-server](https://github.com/cyanheads/atlas-mcp-server)** - ⭐ 468
   A Model Context Protocol (MCP) server for ATLAS, a Neo4j-powered task management system for LLM Agents - implementing a three-tier architecture (Projects, Tasks, Knowledge) to manage complex workflows. Now with Deep Research.

647. **[nexus](https://github.com/Nexus-Router/nexus)** - ⭐ 465
   Govern & Secure your AI

648. **[director](https://github.com/director-run/director)** - ⭐ 464
   MCP Playbooks for AI agents

649. **[probe](https://github.com/probelabs/probe)** - ⭐ 463
   AI-friendly semantic code search engine for large codebases. Combines ripgrep speed with tree-sitter AST parsing. Powers AI coding assistants with precise, context-aware code understanding.

650. **[doctor](https://github.com/sisig-ai/doctor)** - ⭐ 462
   Doctor is a tool for discovering, crawl, and indexing web sites to be exposed as an MCP server for LLM agents.

651. **[mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use)** - ⭐ 462
   The only general AI agent that does NOT requires extra API key, giving you full control on your local and remote MacOs from Claude Desktop App

652. **[mcp-nixos](https://github.com/utensils/mcp-nixos)** - ⭐ 457
   MCP-NixOS - Model Context Protocol Server for NixOS resources

653. **[codexia](https://github.com/milisp/codexia)** - ⭐ 457
   Cross-platform GUI/IDE & Toolkit for Codex CLI + Claude Code — with task scheduler, file tree editor, git worktrees & headless remote access

654. **[mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)** - ⭐ 457
   Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration.

655. **[Feishu-MCP](https://github.com/cso1z/Feishu-MCP)** - ⭐ 455
   为 Cursor、Windsurf、Cline 和其他 AI 驱动的编码工具提供访问、编辑和结构化处理飞书文档的能力，基于 Model Context Protocol 服务器实现。

656. **[mcp-mermaid](https://github.com/hustcc/mcp-mermaid)** - ⭐ 454
   ❤️ Generate mermaid diagram and chart with AI MCP dynamically.

657. **[home-assistant-vibecode-agent](https://github.com/Coolver/home-assistant-vibecode-agent)** - ⭐ 453
   Home Assistant MCP server agent. Enable Cursor, VS Code, Claude Code, or any MCP-enabled IDE to help you vibe-code and manage Home Assistant: create and debug automations, design dashboards, tweak themes, modify configs, and deploy changes using natural language

658. **[MCP-Zero](https://github.com/xfey/MCP-Zero)** - ⭐ 453
   MCP-Zero: Active Tool Discovery for Autonomous LLM Agents

659. **[FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)** - ⭐ 452
   这是一个金融领域相关的mcp,本项目通过集成 Tushare API 和 Binance API 为语言模型（如Claude）提供全面的实时金融数据访问能力，支持股票、基金、债券、宏观经济指标、稳定币、虚拟货币等多维度金融数据分析。其中也包含了金融数据查询、财经新闻查询、国家统计局数据查询等

660. **[resend-mcp](https://github.com/resend/resend-mcp)** - ⭐ 452
   The official MCP server to send emails and interact with Resend

661. **[mcp-bench](https://github.com/Accenture/mcp-bench)** - ⭐ 451
   MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers

662. **[youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** - ⭐ 450
   MCP Server for YouTube API, enabling video management, Shorts creation, and advanced analytics

663. **[docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** - ⭐ 450
   A docker MCP Server (modelcontextprotocol)

664. **[vllm-mlx](https://github.com/waybarrios/vllm-mlx)** - ⭐ 449
   OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA) with continuous batching, MCP tool calling, and multimodal support. Native MLX backend, 400+ tok/s. Works with Claude Code.

665. **[nexus](https://github.com/grafbase/nexus)** - ⭐ 446
   Govern & Secure your AI

666. **[nexus](https://github.com/nexus-ai-labs/nexus)** - ⭐ 446
   Govern & Secure your AI

667. **[mcp-security](https://github.com/google/mcp-security)** - ⭐ 446

668. **[mcp-send-email](https://github.com/resend/mcp-send-email)** - ⭐ 444
   Send emails directly from Cursor with this email sending MCP server

669. **[mcp-hub](https://github.com/ravitemer/mcp-hub)** - ⭐ 444
   A centralized manager for Model Context Protocol (MCP) servers with dynamic server management and monitoring

670. **[xhs-mcp](https://github.com/jobsonlook/xhs-mcp)** - ⭐ 444
   小红书MCP服务 x-s x-t js逆向

671. **[AgentX](https://github.com/lucky-aeon/AgentX)** - ⭐ 443
   AgentX 致力于让小白也能无门槛通过自然语言打造属于自己的 Agent。AgentX 采用了自研 MCP 网关，模型高可用组件打造高可用

672. **[room](https://github.com/quoroom-ai/room)** - ⭐ 442
   Open-source swarm intelligence engine. A self-governing collective of AI agents — queen, workers, quorum voting. Runs locally via MCP. Works with Claude Code, Codex, or any pay-per-use API.

673. **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** - ⭐ 440
   Google Search Console Insights with Claude AI for SEOs

674. **[claude-codex-settings](https://github.com/fcakyon/claude-codex-settings)** - ⭐ 439
   My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

675. **[joinly](https://github.com/joinly-ai/joinly)** - ⭐ 435
   Make your meetings accessible to AI Agents

676. **[CoexistAI](https://github.com/SPThole/CoexistAI)** - ⭐ 434
   CoexistAI is a modular, developer-friendly research assistant framework . It enables you to build, search, summarize, and automate research workflows using LLMs, web search, Reddit, YouTube, and mapping tools—all with simple MCP tool calls or API calls or Python functions. 

677. **[mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** - ⭐ 434
   A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap, Ghidra, Nuclei, SQLMap, Hashcat and more.

678. **[GrokSearch](https://github.com/GuDaStudio/GrokSearch)** - ⭐ 434
   Integrate Grok's powerful real-time search capabilities into Claude via the MCP protocol!

679. **[learn-low-code-agentic-ai](https://github.com/panaversity/learn-low-code-agentic-ai)** - ⭐ 433
   Low-Code Full-Stack Agentic AI Development using LLMs, n8n, Loveable, UXPilot, Supabase and MCP. Class Videos: https://www.youtube.com/playlist?list=PL0vKVrkG4hWq5T6yqCtUL7ol9rDuEyzBH

680. **[biomcp](https://github.com/genomoncology/biomcp)** - ⭐ 432
   BioMCP: Biomedical Model Context Protocol

681. **[mcp-redis](https://github.com/redis/mcp-redis)** - ⭐ 432
   The official Redis MCP Server is a natural language interface designed for agentic applications to manage and search data in Redis efficiently

682. **[kmcp](https://github.com/kagent-dev/kmcp)** - ⭐ 431
   CLI tool and Kubernetes Controller for building, testing and deploying MCP servers

683. **[powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)** - ⭐ 431
   The Power BI Modeling MCP Server, brings Power BI semantic modeling capabilities to your AI agents.

684. **[claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** - ⭐ 429
   A Model Context Protocol (MCP) that allows Claude Desktop and other AI tools (Claude Code, Cursor, Antigravity, etc.) to read, analyze, and modify Figma designs

685. **[mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck)** - ⭐ 427
   Local MCP server for DuckDB and MotherDuck

686. **[docling-mcp](https://github.com/docling-project/docling-mcp)** - ⭐ 427
   Making docling agentic through MCP

687. **[kratos-transport](https://github.com/tx7do/kratos-transport)** - ⭐ 426
   kratos transport layer extension, support: rabbitmq,kafka,rocketmq,activemq,apollo,mcp,tcp,websocket...

688. **[mcp-server-spec-driven-development](https://github.com/formulahendry/mcp-server-spec-driven-development)** - ⭐ 426
   Spec-Driven Development MCP Server, not just Vibe Coding

689. **[mcp-registry](https://github.com/docker/mcp-registry)** - ⭐ 425
   Official Docker MCP registry 

690. **[docfork](https://github.com/docfork/docfork)** - ⭐ 425
   Docfork - Up-to-date Docs for AI Agents.

691. **[applescript-mcp](https://github.com/peakmojo/applescript-mcp)** - ⭐ 425
   MCP server that execute applescript giving you full control of your Mac

692. **[mcpstore](https://github.com/whillhill/mcpstore)** - ⭐ 424
   开盒即用的优雅管理mcp服务 | 结合Agent框架 | 作者听劝 | 已发布pypi | Vue页面demo 

693. **[airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server)** - ⭐ 424
   🗂️🤖 Airtable Model Context Protocol Server, for allowing AI systems to interact with your Airtable bases

694. **[awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools)** - ⭐ 423
   A curated list of developer tools, SDKs, libraries, and testing utilities for Model Context Protocol (MCP) server development.

695. **[NetCoreKevin](https://github.com/junkai-li/NetCoreKevin)** - ⭐ 423
   基于NET搭建-AI知识库智能体-现代化Saas企业级前后端分离架构：前端Vue3、IDS4单点登录、多缓存、自动任务、分布式、一库多租户、日志、授权和鉴权、CAP集成事件、SignalR、领域事件、ESL、MCP协议服务、IOC模块化注入、Cors、Quartz自动任务、多短信集成、AI、AgentFramework智能体、AISemanticKernel集成、RAG检索增强、OCR识别、API多版本、单元测试、RabbitMQ、代码生成器、AI知识库、AI联网搜索

696. **[claude-codepro](https://github.com/maxritter/claude-codepro)** - ⭐ 422
   Production-Grade Development Environment for Claude Code. Quality automated. Context optimized. Testing enforced. Ship with confidence. ✔️

697. **[mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** - ⭐ 422
   An MCP tool that connects Google Ads with Claude AI/Cursor and others, allowing you to analyze your advertising data through natural language conversations. This integration gives you access to campaign information, performance metrics, keyword analytics, and ad management—all through simple chat with Claude, Cursor or Windsurf.

698. **[deeppowers](https://github.com/deeppowers/deeppowers)** - ⭐ 421
   DEEPPOWERS is a Fully Homomorphic Encryption (FHE) framework built for MCP (Model Context Protocol), aiming to provide end-to-end privacy protection and high-efficiency computation for the upstream and downstream ecosystem of the MCP protocol.

699. **[Android-MCP](https://github.com/CursorTouch/Android-MCP)** - ⭐ 421
   MCP Server for interacting with Android Devices.

700. **[shinkai-local-ai-agents](https://github.com/dcSpark/shinkai-local-ai-agents)** - ⭐ 419
   Shinkai is a two click install App that allows you to create Local AI agents in 5 minutes or less using a simple UI.  Supports: MCPs, Remote and Local AI, Crypto and Payments.

701. **[mcpadapt](https://github.com/grll/mcpadapt)** - ⭐ 417
   Unlock 650+ MCP servers tools in your favorite agentic framework.

702. **[azure-ai-travel-agents](https://github.com/Azure-Samples/azure-ai-travel-agents)** - ⭐ 416
   A robust enterprise application sample (deployed on ACA) that leverages MCP and multiple AI agents orchestrated by Langchain.js, Llamaindex.TS and Microsoft Agent Framework.

703. **[mcp-cli](https://github.com/wong2/mcp-cli)** - ⭐ 414
   A CLI inspector for the Model Context Protocol

704. **[UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport)** - ⭐ 412
   An Unreal Engine plugin for LLM/GenAI models & MCP UE5 server. Includes OpenAI's GPT 5.1, Deepseek V3.1, Claude Sonnet 4.5 APIs, Gemini 3, Alibaba Qwen, Kimi and Grok 4.1, with plans to add Gemini, audio tts, elevenlabs, OpenRouter, Groq, Dashscope & realtime APIs soon. UnrealMCP is also here!! Automatic scene generation from AI!! 

705. **[mcp](https://github.com/baidu-maps/mcp)** - ⭐ 405
   Baidu Map MCP Server

706. **[zypher-agent](https://github.com/corespeed-io/zypher-agent)** - ⭐ 404
   A minimal yet powerful framework for creating AI agents with full control over tools, providers, and execution flow.

707. **[OpenContext](https://github.com/0xranx/OpenContext)** - ⭐ 404
   A personal context store for AI agents and assistants—reuse your existing coding agent CLI (Codex/Claude/OpenCode) with built‑in Skills/tools and a desktop GUI to capture, search, and reuse project knowledge across agents and repos.

708. **[RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net)** - ⭐ 403
   The safest way to make REST calls in C# with an MCP Generator

709. **[aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol](https://github.com/microsoft/aitour26-WRK540-unlock-your-agents-potential-with-model-context-protocol)** - ⭐ 403

710. **[lunar](https://github.com/TheLunarCompany/lunar)** - ⭐ 402
   lunar.dev: Agent native MCP Gateway for governance and security

711. **[chatluna](https://github.com/ChatLunaLab/chatluna)** - ⭐ 401
   多平台模型接入，可扩展，多种输出格式，提供大语言模型聊天服务的插件 | A bot plugin for LLM chat with multi-model integration, extensibility, and various output formats

712. **[memento-mcp](https://github.com/gannonh/memento-mcp)** - ⭐ 401
   Memento MCP: A Knowledge Graph Memory System for LLMs

713. **[puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server)** - ⭐ 401
   This MCP server provides browser automation capabilities through Puppeteer, allowing interaction with both new browser instances and existing Chrome windows.

714. **[Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)** - ⭐ 400
   An experiment in software planning using MCP

715. **[tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp)** - ⭐ 400
    Advanced TradingView MCP Server for AI-powered market analysis. Real-time crypto & stock screening, technical indicators, Bollinger Band intelligence, and candlestick patterns. Works with Claude Desktop & AI assistants. Multi-exchange support (Binance, KuCoin, Bybit+). Open source trading toolkit.

716. **[edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp)** - ⭐ 396
   An MCP service designed for deploying HTML content to EdgeOne Pages and obtaining an accessible public URL.

717. **[better-icons](https://github.com/better-auth/better-icons)** - ⭐ 396
   Skill and MCP server for searching and retrieving icons

718. **[sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)** - ⭐ 395
   SonarQube MCP Server

719. **[mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy)** - ⭐ 393
   A MCP (model context protocol) server that gives the LLM access to and knowledge about relational databases like SQLite, Postgresql, MySQL & MariaDB, Oracle, and MS-SQL.

720. **[Redbook-Search-Comment-MCP2.0](https://github.com/chenningling/Redbook-Search-Comment-MCP2.0)** - ⭐ 392
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client（如Claude for Desktop），帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布AI生成评论等操作。

721. **[kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)** - ⭐ 389
   Model Context Protocol server for KiCad on Mac, Windows, and Linux

722. **[speakeasy](https://github.com/speakeasy-api/speakeasy)** - ⭐ 389
   Build APIs your users love ❤️ with Speakeasy. ✨ Polished and type-safe SDKs. 🌐 Terraform providers, MCP servers, CLIs and Contract Tests for your API. OpenAPI native. 

723. **[MCP-SecurityTools](https://github.com/Ta0ing/MCP-SecurityTools)** - ⭐ 388
   MCP-SecurityTools 是一个专注于收录和更新网络安全领域 MCP 的开源项目，旨在汇总、整理和优化各类与 MCP 相关的安全工具、技术及实战经验。

724. **[mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb)** - ⭐ 387
   Search Airbnb using your AI Agent

725. **[ai4j](https://github.com/LnYo-Cly/ai4j)** - ⭐ 387
   一款JavaSDK用于快速接入AI大模型应用，整合多平台大模型，如OpenAi、智谱Zhipu(ChatGLM)、深度求索DeepSeek、月之暗面Moonshot(Kimi)、腾讯混元Hunyuan、零一万物(01)等等，提供统一的输入输出(对齐OpenAi)消除差异化，优化函数调用(Tool Call)，优化RAG调用、支持向量数据库(Pinecone)、内置联网增强，并且支持JDK1.8，为用户提供快速整合AI的能力。

726. **[mcpmark](https://github.com/eval-sys/mcpmark)** - ⭐ 387
   MCPMark is a comprehensive, stress-testing MCP benchmark designed to evaluate model and agent capabilities in real-world MCP use.

727. **[reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy)** - ⭐ 386
   Clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.

728. **[vestige](https://github.com/samvallad33/vestige)** - ⭐ 386
   Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

729. **[agent-builder](https://github.com/strands-agents/agent-builder)** - ⭐ 385
   An example agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

730. **[minion-agent](https://github.com/femto/minion-agent)** - ⭐ 385
   A simple agent framework that's capable of browser use + mcp + auto instrument + plan + deep  research + more

731. **[station](https://github.com/cloudshipai/station)** - ⭐ 385
   Station is our open-source runtime that lets teams deploy agents on their own infrastructure with full control.

732. **[agent](https://github.com/1mcp-app/agent)** - ⭐ 385
   A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.

733. **[yutu](https://github.com/eat-pray-ai/yutu)** - ⭐ 383
   A fully functional MCP server and CLI for YouTube

734. **[mcp-hfspace](https://github.com/evalstate/mcp-hfspace)** - ⭐ 382
   MCP Server to Use HuggingFace spaces, easy configuration and Claude Desktop mode. 

735. **[groq-desktop-beta](https://github.com/groq/groq-desktop-beta)** - ⭐ 382
   Local Groq Desktop chat app with MCP support

736. **[mcp-server](https://github.com/e2b-dev/mcp-server)** - ⭐ 381
   Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

737. **[zotero-mcp](https://github.com/cookjohn/zotero-mcp)** - ⭐ 381
   Zotero MCP Plugin 是一个 Zotero 插件，通过 MCP协议实现 AI 助手与 Zotero深度集成。插件支持文献检索、元   数据管理、全文分析和智能问答等功能，让 Claude、ChatGPT 等 AI 工具能够直接访问和操作您的文献库。 Zotero MCP Plugin enables integration between AI assistants and Zotero through MCP. 

738. **[mcp-code-graph](https://github.com/JudiniLabs/mcp-code-graph)** - ⭐ 380
   MCP Server for code graph analysis and visualization by CodeGPT

739. **[obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** - ⭐ 380
   Obsidian Knowledge-Management MCP (Model Context Protocol) server that enables AI agents and development tools to interact with an Obsidian vault. It provides a comprehensive suite of tools for reading, writing, searching, and managing notes, tags, and frontmatter, acting as a bridge to the Obsidian Local REST API plugin.

740. **[Agentfy](https://github.com/Agentfy-io/Agentfy)** - ⭐ 379
   🤖 Agentfy is a modular microservices architecture designed to process user requests and execute workflows across multiple social media platforms.  ASK ONCE, LET THE AGENT DO THE REST!

741. **[labs-ai-tools-for-devs](https://github.com/docker/labs-ai-tools-for-devs)** - ⭐ 379
   Your trusted home for discovering MCP tools – seamlessly integrated into Docker

742. **[datagouv-mcp](https://github.com/datagouv/datagouv-mcp)** - ⭐ 379
   Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

743. **[open-skills](https://github.com/instavm/open-skills)** - ⭐ 378
   OpenSkills: Run Claude Skills Locally using any LLM

744. **[prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** - ⭐ 376
   A Model Context Protocol (MCP) server that enables AI agents and LLMs to query and analyze Prometheus metrics through standardized interfaces.

745. **[mcp](https://github.com/mondaycom/mcp)** - ⭐ 375
   Enable AI agents to work reliably - giving them secure access to structured data, tools to take action, and the context needed to make smart decisions.

746. **[automation-mcp](https://github.com/ashwwwin/automation-mcp)** - ⭐ 375
   Control your Mac with detailed mouse, keyboard, screen, and window management capabilities.

747. **[claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)** - ⭐ 375
   The complete guide to Claude Code: CLAUDE.md, hooks, skills, MCP servers, and commands

748. **[mcp-k8s-go](https://github.com/strowk/mcp-k8s-go)** - ⭐ 374
   MCP server connecting to Kubernetes

749. **[graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)** - ⭐ 373
   Model Context Protocol (MCP) Server for Graphlit Platform

750. **[Anemoi](https://github.com/Coral-Protocol/Anemoi)** - ⭐ 373
   Anemoi: A Semi-Centralized Multi-agent Systems Based on Agent-to-Agent Communication MCP server from Coral Protocol

751. **[docfork-mcp](https://github.com/docfork/docfork-mcp)** - ⭐ 372
   Docfork MCP - Up-to-date Docs for AI Agents.

752. **[bagel](https://github.com/Extelligence-ai/bagel)** - ⭐ 372
   Chat with your robotics, drone, and IoT data — ChatGPT for the physical world.

753. **[mnemo](https://github.com/MnemoAI/mnemo)** - ⭐ 371
   A MCP-Ready Intelligence Engine for Data & Agent-as-a-Service.

754. **[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** - ⭐ 371
   Claude Skill: Multi-source content processor for NotebookLM. Supports WeChat articles, web pages, YouTube, PDF, Markdown, search queries → Podcast/PPT/MindMap/Quiz etc.

755. **[todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** - ⭐ 369
   MCP server for Todoist integration enabling natural language task management with Claude

756. **[maverick-mcp](https://github.com/wshobson/maverick-mcp)** - ⭐ 368
   MaverickMCP - Personal Stock Analysis MCP Server

757. **[mcp-selenium](https://github.com/angiejones/mcp-selenium)** - ⭐ 368
   An MCP implementation for Selenium WebDriver

758. **[skillz](https://github.com/intellectronica/skillz)** - ⭐ 367
   An MCP server for loading skills (shim for non-claude clients).

759. **[AgentChat](https://github.com/Shy2593666979/AgentChat)** - ⭐ 366
   AgentChat 是一个基于 LLM 的智能体交流平台，内置默认 Agent 并支持用户自定义 Agent。通过多轮对话和任务协作，Agent 可以理解并协助完成复杂任务。项目集成 LangChain、Function Call、MCP 协议、RAG、Memory、Milvus 和 ElasticSearch 等技术，实现高效的知识检索与工具调用，使用 FastAPI 构建高性能后端服务。

760. **[VTCode](https://github.com/vinhnx/VTCode)** - ⭐ 365
   VT Code - Semantic coding agent in the terminal

761. **[KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** - ⭐ 365
   KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design.

762. **[pinion-os](https://github.com/chu2bard/pinion-os)** - ⭐ 364
   Client SDK, Claude plugin and skill framework for the Pinion protocol. x402 micropayments on Base.

763. **[evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server)** - ⭐ 364
   MCP server that provides LLMs with tools for interacting with EVM networks

764. **[mcp-graphql](https://github.com/blurrah/mcp-graphql)** - ⭐ 364
   Model Context Protocol server for GraphQL

765. **[mcp-sdk-php](https://github.com/logiscape/mcp-sdk-php)** - ⭐ 363
   Model Context Protocol SDK for PHP

766. **[ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server)** - ⭐ 363
   MCP Server implementation for Ableton Live OSC control

767. **[studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server)** - ⭐ 363
   Standalone Roblox Studio MCP Server

768. **[daymon](https://github.com/daymonio/daymon)** - ⭐ 362
   Daymon puts your favorite AI to work 24/7. It schedules, remembers, and orchestrates your own virtual team. Free.

769. **[mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes)** - ⭐ 362
   Talk with your notes in Claude. RAG over your Apple Notes using Model Context Protocol.

770. **[f2c-mcp](https://github.com/f2c-ai/f2c-mcp)** - ⭐ 361
   F2C MCP Server

771. **[mcp2mqtt](https://github.com/mcp2everything/mcp2mqtt)** - ⭐ 361
   本项目通过将 MCP 协议转换为 MQTT 协议，我们能够利用强大的大型语言模型（LLMs），就能轻松操控您的智能家居、机器人或其他硬件设备。

772. **[twitter-mcp](https://github.com/EnesCinr/twitter-mcp)** - ⭐ 361
   A Model Context Protocol server allows to interact with Twitter, enabling posting tweets and searching Twitter.

773. **[applescript-mcp](https://github.com/joshrutkowski/applescript-mcp)** - ⭐ 359
   A macOS AppleScript MCP server

774. **[WireMCP](https://github.com/0xKoda/WireMCP)** - ⭐ 359
   An MCP for WireShark (tshark). Empower LLM's with realtime network traffic analysis capability

775. **[Lynkr](https://github.com/Fast-Editor/Lynkr)** - ⭐ 359
   Streamline your workflow with Lynkr, a CLI tool that acts as an HTTP proxy for efficient code interactions using Claude Code CLI.

776. **[claude-code-statusline](https://github.com/rz1989s/claude-code-statusline)** - ⭐ 359
   Transform your Claude Code terminal with atomic precision statusline. Features flexible layouts, real-time cost tracking, MCP monitoring, prayer times, and beautiful themes.

777. **[MCPSharp](https://github.com/afrise/MCPSharp)** - ⭐ 358
   MCPSharp is a .NET library that helps you build Model Context Protocol (MCP) servers and clients - the standardized API protocol used by AI assistants and models.

778. **[devopness](https://github.com/devopness/devopness)** - ⭐ 358
   DevOps Happiness: 1-click or 1-prompt MCP. Deploy apps + infra + CI/CD on your cloud. Happy humans + reliable agents. 🚀

779. **[mcp-aktools](https://github.com/aahl/mcp-aktools)** - ⭐ 358
   📈 提供股票、加密货币的数据查询和分析功能MCP服务器

780. **[xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server)** - ⭐ 358
   MCP Server implementation for Xcode integration

781. **[MoltBrain](https://github.com/nhevers/MoltBrain)** - ⭐ 356
   Long-term memory layer for OpenClaw & MoltBook agents that learns and recalls your project context automatically.

782. **[vtcode](https://github.com/vinhnx/vtcode)** - ⭐ 355
   VT Code - Semantic coding agent in the terminal

783. **[tfmcp](https://github.com/nwiizo/tfmcp)** - ⭐ 355
   🌍 Terraform Model Context Protocol (MCP) Tool - An experimental CLI tool that enables AI assistants to manage and operate Terraform environments. Supports reading Terraform configurations, analyzing plans, applying configurations, and managing state with Claude Desktop integration. ⚡️

784. **[mcp-reddit](https://github.com/adhikasp/mcp-reddit)** - ⭐ 355
   A Model Context Protocol (MCP) server that provides tools for fetching and analyzing Reddit content.

785. **[atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)** - ⭐ 355
   Remote MCP Server that securely connects Jira and Confluence with your LLM, IDE, or agent platform of choice.

786. **[mcp-teams-server](https://github.com/InditexTech/mcp-teams-server)** - ⭐ 354
   An MCP (Model Context Protocol) server implementation for Microsoft Teams integration, providing capabilities to read messages, create messages, reply to messages, mention members.

787. **[RetroMCP-Java](https://github.com/MCPHackers/RetroMCP-Java)** - ⭐ 353
   A rewrite of MCP to provide support for many versions of Minecraft which were never supported by original MCP

788. **[droidmind](https://github.com/hyperb1iss/droidmind)** - ⭐ 351
   Control your Android devices with AI using Model Context Protocol

789. **[mcp-gateway](https://github.com/lasso-security/mcp-gateway)** - ⭐ 349
   A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it enterprise-grade agents.

790. **[run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)** - ⭐ 348
   Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

791. **[revit-mcp](https://github.com/revit-mcp/revit-mcp)** - ⭐ 347
   AI-Powered Revit Modeling

792. **[Construction-Hazard-Detection](https://github.com/yihong1120/Construction-Hazard-Detection)** - ⭐ 347
   Enhances construction site safety using YOLO for object detection, identifying hazards like workers without helmets or safety vests, and proximity to machinery or vehicles. HDBSCAN clusters safety cone coordinates to create monitored zones. Post-processing algorithms improve detection accuracy.

793. **[mcp-calculator](https://github.com/78/mcp-calculator)** - ⭐ 347
   Xiaozhi MCP sample program

794. **[db-mcp-server](https://github.com/FreePeak/db-mcp-server)** - ⭐ 346
   A powerful multi-database server implementing the Model Context Protocol (MCP) to provide AI assistants with structured access to databases.

795. **[ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** - ⭐ 346
   A MCP server that supports mainstream eBook formats including EPUB, PDF and more. Simplify your eBook user experience with LLM.

796. **[Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)** - ⭐ 346
   Context-Engine MCP - Agentic Context Compression Suite

797. **[one-mcp](https://github.com/burugo/one-mcp)** - ⭐ 345
   A centralized reverse-proxy platform for MCP servers — manage, group, and export as Skills from a single endpoint.

798. **[hermes-mcp](https://github.com/cloudwalk/hermes-mcp)** - ⭐ 345
   Elixir Model Context Protocol (MCP) SDK

799. **[ast-grep-mcp](https://github.com/ast-grep/ast-grep-mcp)** - ⭐ 345

800. **[roam-code](https://github.com/Cranot/roam-code)** - ⭐ 345
   Architectural intelligence layer for AI coding agents — structural graph, architecture governance, multi-agent orchestration, vulnerability mapping. 94 commands, 26 languages, 100% local.

801. **[linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)** - ⭐ 344
   A server that integrates Linear's project management system with the Model Context Protocol (MCP) to allow LLMs to interact with Linear.

802. **[mcp-for-next.js](https://github.com/vercel-labs/mcp-for-next.js)** - ⭐ 344

803. **[stealth-browser-mcp](https://github.com/vibheksoni/stealth-browser-mcp)** - ⭐ 344
   The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat.

804. **[x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer)** - ⭐ 344
   x64DbgMCPServer made from c# with Claude, Windsurf and Cursor support

805. **[axon](https://github.com/harshkedia177/axon)** - ⭐ 343
   Graph-powered code intelligence engine — indexes codebases into a knowledge graph, exposed via MCP tools for AI agents and a CLI for developers.

806. **[agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)** - ⭐ 341
   ACP is the Agent Control Plane - a distributed agent scheduler optimized for simplicity, clarity, and control. It is designed for outer-loop agents that run without supervision, and make asynchronous tool calls like requesting human feedback on key operations. Full MCP support.

807. **[agent-skills](https://github.com/microsoft/agent-skills)** - ⭐ 340
   Skills, MCP servers, Custom Coding Agents, Agents.md for SDKs to ground Coding Agents

808. **[CAAL](https://github.com/CoreWorxLab/CAAL)** - ⭐ 340
   Local voice assistant that learns new abilities via auto-discovered n8n workflows exposed as tools via MCP

809. **[todoist-ai](https://github.com/Doist/todoist-ai)** - ⭐ 340
   A set of tools to connect to AI agents, to allow them to use Todoist on a user's behalf. Includes MCP support.

810. **[mcsmcp](https://github.com/microsoft/mcsmcp)** - ⭐ 339
   Lab for creating an MCP Server and using it in Microsoft Copilot Studio.

811. **[base-mcp](https://github.com/base/base-mcp)** - ⭐ 339
   A Model Context Protocol (MCP) server that provides onchain tools for LLMs, allowing them to interact with the Base network and Coinbase API.

812. **[devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp)** - ⭐ 339
   An MCP server exposing full Chrome DevTools Protocol debugging: breakpoints, step/run, call stacks, eval, and source maps.

813. **[PlanExe](https://github.com/PlanExeOrg/PlanExe)** - ⭐ 339
   Create a plan from a description in minutes

814. **[mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops)** - ⭐ 339
   An MCP server for Azure DevOps

815. **[mcp](https://github.com/IBM/mcp)** - ⭐ 338
   A collection of Model Context Protocol (MCP) servers, clients and developer tools by IBM.

816. **[awesome-cursor-mpc-server](https://github.com/kleneway/awesome-cursor-mpc-server)** - ⭐ 337
   Example of an MCP server with custom tools that can be called directly from cursor

817. **[interactive-mcp](https://github.com/ttommyth/interactive-mcp)** - ⭐ 336
   Vibe coding should have human in the loop! interactive-mcp: Local, cross-platform MCP server for interact with your AI Agent

818. **[BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI)** - ⭐ 336
   BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol, allowing security professionals to analyze Active Directory attack paths using natural language instead of complex Cypher queries.

819. **[mesh](https://github.com/decocms/mesh)** - ⭐ 336
   One secure endpoint for every MCP server. Deploy anywhere.

820. **[daan](https://github.com/pluveto/daan)** - ⭐ 335
   ✨Lightweight LLM Client with MCP 🔌 & Characters 👤

821. **[mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd)** - ⭐ 334
   An implementation of Model Context Protocol (MCP) server for Argo CD.

822. **[open-mcp](https://github.com/wegotdocs/open-mcp)** - ⭐ 333

823. **[vscode-mcp-server](https://github.com/juehang/vscode-mcp-server)** - ⭐ 333
   MCP server to expose VS Code editing features to an LLM for AI coding

824. **[MemoryMesh](https://github.com/CheMiguel23/MemoryMesh)** - ⭐ 333
   A knowledge graph server that uses the Model Context Protocol (MCP) to provide structured memory persistence for AI models.

825. **[boltmcp](https://github.com/boltmcp/boltmcp)** - ⭐ 333

826. **[paws-on-mcp](https://github.com/hemanth/paws-on-mcp)** - ⭐ 332
   A comprehensive Model Context Protocol (MCP) server implementing the latest specification.

827. **[CodeGraphContext](https://github.com/Shashankss1205/CodeGraphContext)** - ⭐ 331
   An MCP server plus a CLI tool that indexes local code into a graph database to provide context to AI assistants.

828. **[Ace-Mcp-Node](https://github.com/yeuxuan/Ace-Mcp-Node)** - ⭐ 331
   Acemcp 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供代码库索引和语义搜索能力。通过 Acemcp，AI 助手可以：  🔍 快速搜索和理解大型代码库 📊 获取带行号的精确代码片段 🤖 自动增量更新索引 🌐 通过 Web 界面管理和调试

829. **[laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server)** - ⭐ 330
   A Laravel package for implementing secure Model Context Protocol servers using Streamable HTTP and SSE transport, providing real-time communication and a scalable tool system for enterprise environments.

830. **[css-mcp](https://github.com/stolinski/css-mcp)** - ⭐ 329

831. **[google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** - ⭐ 329
   The Ultimate Google Docs, Sheets & Drive MCP Server. Google Docs MCP is an MCP server (primarily for use in Claude Desktop) that gains full access to your google docs, etc. and allows claude to make direct edits and formatting.

832. **[stitch-mcp](https://github.com/davideast/stitch-mcp)** - ⭐ 328
   A CLI for moving AI-generated UI designs from Google’s Stitch platform into your development workflow.

833. **[moling](https://github.com/gojue/moling)** - ⭐ 327
   MoLing is a computer-use and browser-use based MCP server. It is a locally deployed, dependency-free office AI assistant.

834. **[mcp-cli](https://github.com/apify/mcp-cli)** - ⭐ 327
   mcpc is a CLI client for MCP. It supports persistent sessions, stdio/HTTP, OAuth 2.1, JSON output for code mode, proxy for AI sandboxes, and much more.

835. **[abcoder](https://github.com/cloudwego/abcoder)** - ⭐ 326
   deep, reliable and confidential coding-context

836. **[things-mcp](https://github.com/hald/things-mcp)** - ⭐ 326
   Things.app MCP Server

837. **[claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp)** - ⭐ 325
   MCP server for searching and retrieving Claude Agent Skills using vector search

838. **[redd-archiver](https://github.com/19-84/redd-archiver)** - ⭐ 324
   A PostgreSQL-backed archive generator that creates browsable HTML archives from link aggregator platforms including Reddit, Voat, and Ruqqus.

839. **[skillport](https://github.com/gotalab/skillport)** - ⭐ 324
   Bring Agent Skills to Any AI Agent and Coding Agent — via CLI or MCP. Manage once, serve anywhere.

840. **[gptr-mcp](https://github.com/assafelovic/gptr-mcp)** - ⭐ 323
   MCP server for enabling LLM applications to perform deep research via the MCP protocol

841. **[ShipSwift](https://github.com/signerlabs/ShipSwift)** - ⭐ 323
   AI-native SwiftUI component library with full-stack recipes — connect via MCP for instant access.

842. **[Rube](https://github.com/ComposioHQ/Rube)** - ⭐ 322
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

843. **[skylos](https://github.com/duriantaco/skylos)** - ⭐ 322
   High-precision Python SAST & Dead Code Remover. Finds unused functions, secrets, and security flaws with hybrid static analysis + local LLM agents. Privacy-first & low noise. MCP server for SAST too. Docs: https://docs.skylos.dev/

844. **[ClimateTraceKMP](https://github.com/joreilly/ClimateTraceKMP)** - ⭐ 321
   Kotlin/Compose Multiplatform project to show climate related emission data from https://climatetrace.org/data.

845. **[tinystruct](https://github.com/tinystruct/tinystruct)** - ⭐ 321
   A lightweight, modular Java application framework for web and CLI development,         designed for AI integration and plugin-based architecture.         Enabling developers to create robust solutions with ease for building efficient and scalable applications.

846. **[a2a-directory](https://github.com/sing1ee/a2a-directory)** - ⭐ 320
   Agent2Agent (A2A) – AgentCards, Servers, Clients, Docs

847. **[langconnect-client](https://github.com/teddynote-lab/langconnect-client)** - ⭐ 320
   A Modern GUI Interface for Vector Database Management(Supports MCP integration)

848. **[claude-emporium](https://github.com/Vvkmnn/claude-emporium)** - ⭐ 319
   🏛 [UNDER CONSTRUCTION] A (roman) claude plugin marketplace 

849. **[Minecraft-Hack-BaseClient](https://github.com/OxideWaveLength/Minecraft-Hack-BaseClient)** - ⭐ 318
   This is a Minecraft Base Client

850. **[cheatengine-mcp-bridge](https://github.com/miscusi-peek/cheatengine-mcp-bridge)** - ⭐ 317
   Connect Cursor, Copilot & Claude directly to Cheat Engine via MCP. Automate reverse engineering, pointer scanning, and memory analysis using natural language.

851. **[emcee](https://github.com/mattt/emcee)** - ⭐ 316
   MCP generator for OpenAPIs 🫳🎤💥

852. **[mcp-server](https://github.com/mapbox/mcp-server)** - ⭐ 315
   Mapbox Model Context Protocol (MCP) server

853. **[mssql_mcp_server](https://github.com/RichardHan/mssql_mcp_server)** - ⭐ 315
   A Model Context Protocol (MCP) server for Microsoft SQL Server that enables secure database interactions through a controlled interface. Allows AI assistants to safely list tables, read data, and execute SQL queries while maintaining security and structure.

854. **[mq](https://github.com/harehare/mq)** - ⭐ 315
   jq-like command-line tool for markdown processing

855. **[autogenstudio-skills](https://github.com/madtank/autogenstudio-skills)** - ⭐ 314
   Repo of skills for autogen studio using model context protocol (mcp)

856. **[code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp)** - ⭐ 314
   An MCP server to create secure code sandbox environment for executing code within Docker containers. This MCP server provides AI applications with a safe and isolated environment for running code while maintaining security through containerization.

857. **[mcp-servers-hub](https://github.com/apappascs/mcp-servers-hub)** - ⭐ 314
   Discover the most comprehensive and up-to-date collection of MCP servers in the market. This repository serves as a centralized hub, offering an extensive catalog of open-source and proprietary MCP servers, complete with features, documentation links, and contributors.

858. **[mcp-server-code-execution-mode](https://github.com/elusznik/mcp-server-code-execution-mode)** - ⭐ 314
   An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

859. **[deep-research-mcp](https://github.com/teelaitila/deep-research-mcp)** - ⭐ 313

860. **[mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript)** - ⭐ 313
   MCP server retrieving transcripts of YouTube videos

861. **[investor-agent](https://github.com/ferdousbhai/investor-agent)** - ⭐ 312
   A Model Context Protocol server for building an investor agent

862. **[kagimcp](https://github.com/kagisearch/kagimcp)** - ⭐ 312
   The Official Model Context Protocol (MCP) server for Kagi search & other tools.

863. **[MaaMCP](https://github.com/MAA-AI/MaaMCP)** - ⭐ 311
   基于 MaaFramework 的 MCP 服务器 为 AI 助手提供 Android 设备和 Windows 桌面自动化能力

864. **[anytype-mcp](https://github.com/anyproto/anytype-mcp)** - ⭐ 311
   An MCP server enabling AI assistants to interact with Anytype - your encrypted, local and collaborative wiki - to organize objects, lists, and more through natural language.

865. **[mcp-database-server](https://github.com/executeautomation/mcp-database-server)** - ⭐ 310
   MCP Database Server is a new MCP Server which helps connect with Sqlite, SqlServer and Posgresql Databases

866. **[deep-research-mcp](https://github.com/Ozamatash/deep-research-mcp)** - ⭐ 309

867. **[ssh-mcp](https://github.com/tufantunc/ssh-mcp)** - ⭐ 307
   MCP server exposing SSH control for Linux servers via Model Context Protocol.

868. **[solon-ai](https://github.com/opensolon/solon-ai)** - ⭐ 306
   Java AI application development framework (supports LLM-tool,skill; RAG; MCP; Agent-ReAct,Team-Agent). Compatible with java8 ~ java25. It can also be embedded in SpringBoot, jFinal, Vert.x, Quarkus, and other frameworks.

869. **[Unreal_mcp](https://github.com/ChiR24/Unreal_mcp)** - ⭐ 305
   A comprehensive Model Context Protocol (MCP) server that enables AI assistants to control Unreal Engine through the native C++ Automation Bridge plugin. Built with TypeScript, C++, and Rust (WebAssembly) for ultra-high-performance game development automation.

870. **[mcp-sse](https://github.com/sidharthrajaram/mcp-sse)** - ⭐ 304
   A working pattern for SSE-based MCP clients and servers

871. **[sdk](https://github.com/smithery-ai/sdk)** - ⭐ 304
   Smithery helps AI agents access external services via a unified gateway.

872. **[AI-Kline](https://github.com/QuantML-C/AI-Kline)** - ⭐ 304
   Python-based stock analysis tool that combines traditional technical analysis with AI prediction capabilities.  Providing comprehensive stock analysis and forecasting using K-line charts, technical indicators, financial data, and news data. With CMD/WEB/MCP supported.

873. **[mcprouter](https://github.com/chatmcp/mcprouter)** - ⭐ 303
   api router for MCP Servers

874. **[openmcp](https://github.com/getdatanaut/openmcp)** - ⭐ 303
   Turn any openapi file into an mcp server, with just the tools you need.

875. **[mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search)** - ⭐ 303

876. **[rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** - ⭐ 303
   RhinoMCP connects Rhino 3D to AI Agent through the Model Context Protocol (MCP)

877. **[automcp](https://github.com/NapthaAI/automcp)** - ⭐ 302
   Easily convert tool, agents and orchestrators from existing agent frameworks to MCP servers

878. **[mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts)** - ⭐ 302

879. **[apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server)** - ⭐ 302
   A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites)

880. **[generator](https://github.com/context-hub/generator)** - ⭐ 301
   CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.

881. **[mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest)** - ⭐ 301
   A Model Context Protocol (MCP) server that helps read GitHub repository structure and important files.

882. **[jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server)** - ⭐ 301
   MCP server for JADX-AI Plugin

883. **[deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server)** - ⭐ 299
   Model Context Protocol server for DeepSeek's advanced language models

884. **[iam-policy-autopilot](https://github.com/awslabs/iam-policy-autopilot)** - ⭐ 297
   IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create baseline AWS IAM policies that you can refine as your application evolves. This tool is available as a command-line utility and MCP server for use within AI coding assistants for quickly building IAM policies.

885. **[mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code)** - ⭐ 296
   MCP implementation of Claude Code capabilities and more

886. **[mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb)** - ⭐ 296
   A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators through natural language commands.

887. **[safe-mcp](https://github.com/safe-agentic-framework/safe-mcp)** - ⭐ 296
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

888. **[DeepWideResearch](https://github.com/puppyone-ai/DeepWideResearch)** - ⭐ 295
   Agentic RAG for any scenario. Customize sources, depth, and width

889. **[llm-context.py](https://github.com/cyberchitta/llm-context.py)** - ⭐ 295
   Share code with LLMs via Model Context Protocol or clipboard. Rule-based customization enables easy switching between different tasks (like code review and documentation). Includes smart code outlining.

890. **[mcp-linker](https://github.com/milisp/mcp-linker)** - ⭐ 295
   mcp store manager, add & syncs MCP server configurations across clients like Claude code, Cursor💡 build-in Codex agent use ChatGPT subscription, mcphub

891. **[mcp](https://github.com/oracle/mcp)** - ⭐ 293
   Repository containing MCP (Model Context Protocol) servers that provides a suite of tools for managing and interacting with Oracle products.

892. **[tabularis](https://github.com/debba/tabularis)** - ⭐ 293
   A lightweight, developer-focused database management tool. Supports MySQL, PostgreSQL and SQLite. Hackable with plugins. Built for speed, security, and aesthetics.

893. **[mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server)** - ⭐ 292
   Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

894. **[mcpsvr](https://github.com/nanbingxyz/mcpsvr)** - ⭐ 292
   Discover Exceptional MCP Servers

895. **[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp)** - ⭐ 292
   Obsidian MCP (Model Context Protocol) Server

896. **[aider-mcp-server](https://github.com/disler/aider-mcp-server)** - ⭐ 292
   Minimal MCP Server for Aider

897. **[aws-mcp](https://github.com/RafalWilinski/aws-mcp)** - ⭐ 291
   Talk with your AWS using Claude. Model Context Protocol (MCP) server for AWS. Better Amazon Q alternative.

898. **[minthcm](https://github.com/minthcm/minthcm)** - ⭐ 291
   First AI‑enabled open-source Human Capital Management system that you can start using today.

899. **[imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)** - ⭐ 291
   An MCP server providing tools for image processing operations

900. **[mcp](https://github.com/salesforcecli/mcp)** - ⭐ 291
   MCP Server for interacting with Salesforce instances

901. **[blender-mcp-vxai](https://github.com/VxASI/blender-mcp-vxai)** - ⭐ 290

902. **[consult7](https://github.com/szeider/consult7)** - ⭐ 290
   MCP server to consult a language model with large context size

903. **[MCPControl](https://github.com/claude-did-this/MCPControl)** - ⭐ 290
   MCP server for Windows OS automation

904. **[lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)** - ⭐ 290
   Lean Theorem Prover MCP

905. **[utcp-specification](https://github.com/universal-tool-calling-protocol/utcp-specification)** - ⭐ 289
   The specification for the Universal Tool Calling Protocol

906. **[telegram-mcp](https://github.com/chaindead/telegram-mcp)** - ⭐ 289
   Telegram MCP for managing dialogs, messages, drafts, read statuses, and more.

907. **[mcp-server-mas-sequential-thinking](https://github.com/FradSer/mcp-server-mas-sequential-thinking)** - ⭐ 288
   An advanced sequential thinking process using a Multi-Agent System (MAS) built with the Agno framework and served via MCP.

908. **[mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server)** - ⭐ 288
   MCP Documentation Server - Bridge the AI Knowledge Gap.  ✨ Features: Document management • Gemini integration • AI-powered semantic search • File uploads • Smart chunking • Multilingual support • Zero-setup  🎯 Perfect for: New frameworks • API docs • Internal guides 

909. **[lets-learn-mcp-csharp](https://github.com/microsoft/lets-learn-mcp-csharp)** - ⭐ 288

910. **[nova-proximity](https://github.com/Nova-Hunting/nova-proximity)** - ⭐ 287
   Nova-Proximity is a MCP and Agent Skills security scanner powered with NOVA

911. **[o3-search-mcp](https://github.com/yoshiko-pg/o3-search-mcp)** - ⭐ 286
   MCP server for OpenAI o3 web search

912. **[remote-mcp-server-with-auth](https://github.com/coleam00/remote-mcp-server-with-auth)** - ⭐ 286
   Template for a remote MCP server with GitHub OAuth - following best practices for building MCP servers so you can take this as a starting point for any MCP server you want to build!

913. **[ddddocr](https://github.com/86maid/ddddocr)** - ⭐ 286
   ddddocr rust 版本，ocr_api_server rust 版本，二进制版本，验证码识别，不依赖 opencv 库，跨平台运行，AI MCP 支持，a simple OCR API server, very easy to deploy。

914. **[safe-mcp](https://github.com/SAFE-MCP/safe-mcp)** - ⭐ 285
   SAFE-MCP is a comprehensive security framework for documenting and mitigating threats in the AI Agent ecosystem.

915. **[mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)** - ⭐ 284
   Model Context Protocol (MCP) server that supports secure interaction with MySQL databases and has anomaly analysis capabilities.更加牛逼！更加好用！不仅止于mysql的增删改查功能； 还包含了数据库异常分析能力；且便于开发者们进行个性化的工具扩展 

916. **[chrome-devtools-mcp](https://github.com/benjaminr/chrome-devtools-mcp)** - ⭐ 284
   An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

917. **[geminimcp](https://github.com/GuDaStudio/geminimcp)** - ⭐ 284
   Gemini-MCP is an MCP server that encapsulates Google's Gemini CLI tool into a standard MCP protocol interface, enabling Claude Code to invoke Gemini for AI-assisted programming tasks.

918. **[private-journal-mcp](https://github.com/obra/private-journal-mcp)** - ⭐ 284
   A lightweight MCP server that provides Claude with a private journaling capability to process feelings and thoughts

919. **[meGPT](https://github.com/adrianco/meGPT)** - ⭐ 283
   Code to process many kinds of content by an author into an MCP server

920. **[perplexity-mcp](https://github.com/DaInfernalCoder/perplexity-mcp)** - ⭐ 283
   A Model Context Protocol (MCP) server for research and documentation assistance using Perplexity AI. Won 1st @ Cline Hackathon

921. **[mcp-server-12306](https://github.com/drfccv/mcp-server-12306)** - ⭐ 283
   12306 MCP Server​​ 是一个基于 ​​Model Context Protocol (MCP)​​ 的高性能火车票查询后端系统。它通过标准化接口提供官方 12306 的实时数据服务，包括余票查询、车站信息、列车经停站、中转换乘方案等核心功能。

922. **[perplexity-mcp](https://github.com/jsonallen/perplexity-mcp)** - ⭐ 283
   A Model Context Protocol (MCP) server that provides web search functionality using Perplexity AI's API.

923. **[1c_mcp](https://github.com/vladimir-kharin/1c_mcp)** - ⭐ 283
   Инструмент для создания MCP-серверов в 1С:Предприятие путем разработки расширения конфигурации. Позволяет интегрировать данные и функциональность 1С с AI-ассистентами (Claude, Cursor и т.д.). Включает Python-прокси и пример расширения 1С с готовыми инструментами.

924. **[swiss-ai-call-agent](https://github.com/Chrissotino/swiss-ai-call-agent)** - ⭐ 283
   Enterprise-grade AI Call Agent for the Swiss market – inbound & outbound calls, multilingual (DE/FR/IT), MCP architecture, Claude AI decision engine, real-time dashboard

925. **[mcp-manager](https://github.com/amxv/mcp-manager)** - ⭐ 282
   simple web ui to manage mcp (model context protocol) servers in the claude app

926. **[DeepWideResearch](https://github.com/PuppyAgent/DeepWideResearch)** - ⭐ 281
   Agentic RAG for any scenario. Customize sources, depth, and width

927. **[MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright)** - ⭐ 281
   MCP server for browser automation using Playwright

928. **[mcp-manager](https://github.com/zueai/mcp-manager)** - ⭐ 280
   simple web ui to manage mcp (model context protocol) servers in the claude app

929. **[MCP-handle](https://github.com/WeatherPal-AI/MCP-handle)** - ⭐ 280
   MCP integration platforms making AI-Agents developers focusing on their own tasks

930. **[FileScopeMCP](https://github.com/admica/FileScopeMCP)** - ⭐ 280
   Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores per file, helping AI assistants understand the codebase. Automatically parses popular programming languages such as Python, C, C++, Rust, Zig, Lua.

931. **[real-estate-mcp](https://github.com/tae0y/real-estate-mcp)** - ⭐ 280
   Ask Claude about Korean apartment prices — powered by MOLIT's open API

932. **[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** - ⭐ 279
   One-command setup for AI-powered Laravel development with Claude Code and MCP servers

933. **[mcp940](https://github.com/WangTingZheng/mcp940)** - ⭐ 279
   Source code of minecraft 1.12

934. **[mcp-server-guide](https://github.com/figma/mcp-server-guide)** - ⭐ 279
   A guide on how to use the Figma MCP server

935. **[opennews-mcp](https://github.com/6551Team/opennews-mcp)** - ⭐ 279
   Crypto News Aggregation · AI Ratings · Trading Signals · Real-time Updates

936. **[gemini-cli-desktop](https://github.com/Piebald-AI/gemini-cli-desktop)** - ⭐ 278
   Web/desktop UI for Gemini CLI/Qwen Code.  Manage projects, switch between tools, search across past conversations, and manage MCP servers, all from one multilingual interface, locally or remotely.

937. **[metorial-index](https://github.com/metorial/metorial-index)** - ⭐ 277
   Metorial MCP Index - An ever growing list of open source MCP servers 📁 🎉

938. **[hass-mcp](https://github.com/voska/hass-mcp)** - ⭐ 277
   Home Assistant MCP Server

939. **[django-mcp-server](https://github.com/gts360/django-mcp-server)** - ⭐ 277
   Django MCP Server is a Django extensions to easily enable AI Agents to interact with Django Apps through the Model Context Protocol it works equally well on WSGI and ASGI

940. **[mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)** - ⭐ 276
   A Model Context Protocol Server for MongoDB

941. **[Context-Engine](https://github.com/m1rl0k/Context-Engine)** - ⭐ 276
   Context-Engine MCP - Agentic Context Compression Suite

942. **[next-lens](https://github.com/1weiho/next-lens)** - ⭐ 276
   A CLI that scans Next.js routes and provides quick insights from your terminal, web UI, and MCP.

943. **[mcp-reasoner](https://github.com/Jacck/mcp-reasoner)** - ⭐ 276
   A systematic reasoning MCP server implementation for Claude Desktop with beam search and thought evaluation.

944. **[dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server)** - ⭐ 275
   Model Context Protocol (MCP) Server for dify workflows

945. **[AetherLink](https://github.com/1600822305/AetherLink)** - ⭐ 275
   AetherLink is a cross-platform AI assistant application that supports multiple mainstream AI models (OpenAI, Google Gemini, Anthropic Claude, Grok, etc.). Built with React, TypeScript, and Capacitor, it delivers a seamless conversational experience. Key features include customizable model configurations, multi-topic chat management, AI reasoning vi

946. **[ai-agent-team](https://github.com/peterfei/ai-agent-team)** - ⭐ 275
   AI Agent Team-拥有24/7专业AI开发团队：产品经理、前端开发、后端开发、测试工程师、DevOps工程师、技术负责人。一键安装，支持中英文命令，大幅提升开发效率！

947. **[mcp-odoo](https://github.com/tuanle96/mcp-odoo)** - ⭐ 275
   MCP Server for Odoo

948. **[mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** - ⭐ 272
   🔍 A Model Context Protocol (MCP) server providing unified access to multiple search engines (Tavily, Brave, Kagi), AI tools (Perplexity, FastGPT), and content processing services (Jina AI, Kagi). Combines search, AI responses, content processing, and enhancement features through a single interface.

949. **[claude-modular](https://github.com/oxygen-fragment/claude-modular)** - ⭐ 272
   Production-ready modular Claude Code framework with 30+ commands, token optimization, and MCP server integration. Achieves 2-10x productivity gains through   systematic command organization and hierarchical configuration.

950. **[mcp-ical](https://github.com/Omar-V2/mcp-ical)** - ⭐ 272
   A Model Context Protocol Server that allows you to interact with your MacOS Calendar through natural language.

951. **[proximity](https://github.com/Nova-Hunting/proximity)** - ⭐ 271
   Proximity is a MCP security scanner powered with NOVA

952. **[stitch](https://github.com/gemini-cli-extensions/stitch)** - ⭐ 271
   The Stitch extension for Gemini CLI enables you to interact with the Stitch MCP server using natural language commands. 

953. **[jinni](https://github.com/smat-dev/jinni)** - ⭐ 270
   Bring your project into LLM context - tool and MCP server

954. **[proximity](https://github.com/fr0gger/proximity)** - ⭐ 269
   Proximity is a MCP security scanner powered with NOVA

955. **[model-context-protocol-resources](https://github.com/cyanheads/model-context-protocol-resources)** - ⭐ 269
   Exploring the Model Context Protocol (MCP) through practical guides, clients, and servers I've built while learning about this new protocol.

956. **[ultra-mcp](https://github.com/RealMikeChong/ultra-mcp)** - ⭐ 269
   100x Your Claude Code, Gemini CLI, Cursor and/or any coding tools with MCP client support

957. **[mcp-gdrive](https://github.com/isaacphi/mcp-gdrive)** - ⭐ 268
   Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets

958. **[reddit-mcp](https://github.com/Arindam200/reddit-mcp)** - ⭐ 267
   Model Context Protocol server implementation for Reddit

959. **[mcp-server-tree-sitter](https://github.com/wrale/mcp-server-tree-sitter)** - ⭐ 266
   MCP Server for Tree-sitter

960. **[deepcontext-mcp](https://github.com/Wildcard-Official/deepcontext-mcp)** - ⭐ 266
   DeepContext is an MCP server that adds symbol-aware semantic search to Claude Code, Codex CLI, and other agents for faster, smarter context on large codebases.

961. **[apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server)** - ⭐ 265
   Apollo MCP Server

962. **[bazi-mcp](https://github.com/cantian-ai/bazi-mcp)** - ⭐ 265
   MCP server for Bazi (八字) information

963. **[wexin-read-mcp](https://github.com/Bwkyd/wexin-read-mcp)** - ⭐ 265
   能够让大模型阅读微信公众号文章，使用浏览器模拟绕过反爬虫。

964. **[xiaozhi-client](https://github.com/shenjingnan/xiaozhi-client)** - ⭐ 260
   小智AI客户端，目前主要用于MCP的对接

965. **[mcp-server](https://github.com/strands-agents/mcp-server)** - ⭐ 259
   This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

966. **[doris-mcp-server](https://github.com/apache/doris-mcp-server)** - ⭐ 259
   Apache Doris MCP Server

967. **[osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools)** - ⭐ 258
   A Model Context Protocol (MCP) server that empowers LLMs to use some of Open Srategy Partners' core writing and product marketing techniques.

968. **[mcp_massive](https://github.com/massive-com/mcp_massive)** - ⭐ 258
   An MCP server for Massive.com Financial Market Data

969. **[enterprise-mcp-course](https://github.com/decodingai-magazine/enterprise-mcp-course)** - ⭐ 258
   Learn to build from scratch an AI PR reviewer integrated with GitHub, Slack and Asana that scales within your organization.

970. **[api200](https://github.com/API-200/api200)** - ⭐ 257
   API 200 is an open source API gateway to simplify 3rd-party integrations. Import endpoints, set up caching, retries, and mocks. Access all services via one URL. Monitor logs, track errors, and get alerts on API incidents.

971. **[sandboxed.sh](https://github.com/Th0rgal/sandboxed.sh)** - ⭐ 257
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

972. **[rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server)** - ⭐ 256
   🦀 Prevents outdated Rust code suggestions from AI assistants. This MCP server fetches current crate docs, uses embeddings/LLMs, and provides accurate context via a tool call.

973. **[project-nova](https://github.com/dujonwalker/project-nova)** - ⭐ 254
   A multi-agent AI architecture that connects 25+ specialized agents through n8n and MCP servers. Project NOVA routes requests to domain-specific experts, enabling control of applications from knowledge bases to DAWs, home automation to development tools. Includes system prompts, Dockerfiles, and workflows for a complete AI assistant ecosystem.

974. **[spring-ai-summary](https://github.com/java-ai-tech/spring-ai-summary)** - ⭐ 254
   SpringAI，LLM，MCP，Embedding

975. **[code-reasoning](https://github.com/mettamatt/code-reasoning)** - ⭐ 254
   A code reasoning MCP server, a fork of sequential-thinking

976. **[mcp_flutter](https://github.com/Arenukvern/mcp_flutter)** - ⭐ 254
   MCP server and MCP Toolkit  for Flutter and Dart VM - supports dynamic tooling

977. **[admin](https://github.com/decocms/admin)** - ⭐ 253
   Define and compose secure MCPs in TypeScript. Generate AI workflows and agents with React + Tailwind UI. Deploy anywhere.

978. **[elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server)** - ⭐ 253
   A Model Context Protocol (MCP) server implementation that provides Elasticsearch and OpenSearch interaction.

979. **[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** - ⭐ 253
   MCP to help Defenders Detection Engineer Harder and Smarter

980. **[codex-mcp-server](https://github.com/tuannvm/codex-mcp-server)** - ⭐ 253
   MCP server wrapper for OpenAI Codex CLI that enables Claude Code to leverage Codex's AI capabilities directly.

981. **[hydra-mcp-solana](https://github.com/hydra-mcp/hydra-mcp-solana)** - ⭐ 252
   hydra-ai

982. **[AEnvironment](https://github.com/inclusionAI/AEnvironment)** - ⭐ 252
   Standardized environment infrastructure for Agentic AI development.

983. **[outlook-mcp](https://github.com/ryaker/outlook-mcp)** - ⭐ 252
   MCP server for Claude to access Outlook data via Microsoft Graph API

984. **[g-search-mcp](https://github.com/jae-jae/g-search-mcp)** - ⭐ 251
   A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.

985. **[agents](https://github.com/astronomer/agents)** - ⭐ 251
   AI agent tooling for data engineering workflows.

986. **[lingti-bot](https://github.com/ruilisi/lingti-bot)** - ⭐ 251
   🐕⚡ 「极简至上 效率为王 一次编译 到处执行 极速接入」的 AI Bot

987. **[aci-mcp](https://github.com/aipotheosis-labs/aci-mcp)** - ⭐ 250
   MCP server(s) for Aipolabs ACI.dev

988. **[MARM-Systems](https://github.com/Lyellr88/MARM-Systems)** - ⭐ 250
   Turn AI into a persistent, memory-powered collaborator. Universal MCP Server (supports HTTP, STDIO, and WebSocket) enabling cross-platform AI memory, multi-agent coordination, and context sharing. Built with MARM protocol for structured reasoning that evolves with your work.

989. **[strava-mcp](https://github.com/r-huijts/strava-mcp)** - ⭐ 250
   A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs

990. **[mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini)** - ⭐ 248
   MCP server implementation for Google's Gemini API

991. **[video-editing-mcp](https://github.com/burningion/video-editing-mcp)** - ⭐ 248
   MCP Interface for Video Jungle

992. **[CAD-MCP](https://github.com/daobataotie/CAD-MCP)** - ⭐ 248
   CAD MCP Server

993. **[gemini-kit](https://github.com/nth5693/gemini-kit)** - ⭐ 248
   🚀 19 AI Agents + 44 Commands for Gemini CLI - Code 10x faster with auto planning, testing, review & security

994. **[claude-recall](https://github.com/nhevers/claude-recall)** - ⭐ 247
   Long-term memory layer for MoltBot & Claude Code that learns and recalls your project context automatically

995. **[suppr-mcp](https://github.com/WildDataX/suppr-mcp)** - ⭐ 247
    超能文献|AI驱动的文档翻译与学术搜索服务。支持PDF、DOCX、PPTX等多格式文档的高质量翻译（支持11种语言），特别优化了数学公式翻译。同时提供PubMed学术文献智能搜索功能。更多访问：https://suppr.wilddata.cn

996. **[browser-control-mcp](https://github.com/eyalzh/browser-control-mcp)** - ⭐ 247
   MCP server paired with a browser extension that enables AI agents to control the user's browser.

997. **[mcp-server](https://github.com/volcengine/mcp-server)** - ⭐ 246
   Volcengine MCP Servers

998. **[ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)** - ⭐ 245
   MCP server that interacts with TickTick (Dida 365) via the TickTick Open API

999. **[obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** - ⭐ 245
   High-performance Model Context Protocol (MCP) server for Obsidian that provides AI tools with direct vault access through semantic operations and HTTP transport.

1000. **[mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** - ⭐ 245
   A Model Context Protocol (MCP) server that provides tools for interacting with Trello boards.

1001. **[Windows-MCP.Net](https://github.com/shuyu-labs/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1002. **[Windows-MCP.Net](https://github.com/AIDotNet/Windows-MCP.Net)** - ⭐ 244
   A .NET-based Windows desktop automation MCP (Model Context Protocol) server that provides AI assistants with the ability to interact with the Windows desktop environment.

1003. **[mcp-chatbot](https://github.com/3choff/mcp-chatbot)** - ⭐ 244
   A simple CLI chatbot that demonstrates the integration of the Model Context Protocol (MCP).

1004. **[chat-mcp](https://github.com/AI-QL/chat-mcp)** - ⭐ 243
   A Desktop Chat App that leverages MCP(Model Context Protocol) to interface with other LLMs.

1005. **[human-mcp](https://github.com/mrgoonie/human-mcp)** - ⭐ 243

1006. **[embodied-claude](https://github.com/lifemate-ai/embodied-claude)** - ⭐ 243
   Claudeに身体性を与えるMCP群

1007. **[binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp)** - ⭐ 243
   A Binary Ninja plugin containing an MCP server that enables seamless integration with your favorite LLM/MCP client.

1008. **[awesome-mcp-servers](https://github.com/PipedreamHQ/awesome-mcp-servers)** - ⭐ 243
   A collection of MCP servers

1009. **[mcp-feedback-collector](https://github.com/sanshao85/mcp-feedback-collector)** - ⭐ 242
   一个现代化的 Model Context Protocol (MCP) 服务器，为AI助手提供交互式用户反馈收集功能。

1010. **[mcp](https://github.com/Snowflake-Labs/mcp)** - ⭐ 242
   MCP Server for Snowflake including Cortex AI, object management, SQL orchestration, semantic view consumption, and more

1011. **[mcp-prompt-server](https://github.com/gdli6177/mcp-prompt-server)** - ⭐ 241
   这是一个基于Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地使用。

1012. **[MCPBench](https://github.com/modelscope/MCPBench)** - ⭐ 241
   The evaluation benchmark on MCP servers

1013. **[Mimir](https://github.com/orneryd/Mimir)** - ⭐ 241
   Mimir - Fully open and customizable memory bank with semantic vector search capabilities for locally indexed files (Code Intelligence) and stored memories that are shared across sessions and chat contexts allowing worker agent to learn from errors in past runs. Includes Drag and Drop multi-agent orchestration

1014. **[mcp2py](https://github.com/MaximeRivest/mcp2py)** - ⭐ 240
   Turn any MCP server into a Python module

1015. **[claude-code-mcpinstall](https://github.com/undeadpickle/claude-code-mcpinstall)** - ⭐ 240
   Easy guide to installing Claude Code MCPs globally on your machine.

1016. **[foundry-mcp-server](https://github.com/PraneshASP/foundry-mcp-server)** - ⭐ 240
   An experimental MCP Server for foundry built for Solidity devs

1017. **[spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server)** - ⭐ 240
   Lightweight MCP server for Spotify

1018. **[claude_code-gemini-mcp](https://github.com/RaiAnsar/claude_code-gemini-mcp)** - ⭐ 239
   Simplified Gemini for Claude Code. 

1019. **[weather-mcp-server](https://github.com/ezh0v/weather-mcp-server)** - ⭐ 239
   A lightweight Model Context Protocol (MCP) server that enables AI assistants like Claude to retrieve and interpret real-time weather data. Discuss on Hacker News:

1020. **[PIXRA](https://github.com/dodufish/PIXRA)** - ⭐ 239
   Pixelize the real world on-chain

1021. **[mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws)** - ⭐ 239
   AWS MCP Proxy Server

1022. **[dat](https://github.com/hexinfo/dat)** - ⭐ 239
   Asking yours data in a natural language way through pre-modeling (data models and semantic models).

1023. **[firebase-mcp](https://github.com/gannonh/firebase-mcp)** - ⭐ 239
   🔥 Model Context Protocol (MCP) server for Firebase.

1024. **[mcp-server-code-runner](https://github.com/formulahendry/mcp-server-code-runner)** - ⭐ 238
   Code Runner MCP Server

1025. **[mcp-on-vercel](https://github.com/vercel-labs/mcp-on-vercel)** - ⭐ 238

1026. **[mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** - ⭐ 238
   An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.

1027. **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** - ⭐ 237
   A TypeScript streamable HTTP and SSE proxy for MCP servers that use stdio transport.

1028. **[facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server)** - ⭐ 237

1029. **[mcp_chatbot](https://github.com/keli-wen/mcp_chatbot)** - ⭐ 236
   A chatbot implementation compatible with MCP (terminal / streamlit supported)

1030. **[octocode](https://github.com/Muvon/octocode)** - ⭐ 236
   Semantic code searcher and codebase utility

1031. **[NFTIAI](https://github.com/Axarb/NFTIAI)** - ⭐ 235
   NFTI AI — NFTI your AI Agents & Virtual IP. Bridging intelligent agents, MCP protocols, and RWA to create a new era of digital sovereignty.

1032. **[mcp-foundry](https://github.com/microsoft-foundry/mcp-foundry)** - ⭐ 235
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1033. **[openapi-to-mcpserver](https://github.com/higress-group/openapi-to-mcpserver)** - ⭐ 235
   A tool&lib that can automatically convert OpenAPI documents into Higress remote MCP server configurations.

1034. **[c2sagent](https://github.com/C2SAgent/c2sagent)** - ⭐ 233
   C2S Agent is an lightweight AI Agent construction platform that provides configurable online Agents and MCP services, You can configure any HTTP request interface as an MCP tool. C2S Agent 是一个轻量级的AI Agent构建平台，提供在线可配置的Agent，MCP，您可以一个HTTP请求的接口配置成为一个MCP工具，Agent之间可以进行自交流。并提供了单端口多A2A服务，MCP服务的解决方案

1035. **[mcp-telegram](https://github.com/dryeab/mcp-telegram)** - ⭐ 233
   MCP Server for Telegram

1036. **[nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** - ⭐ 233
   一个基于uri而不是RAG的轻量级、可回滚、可视化的 **AI 外挂MCP记忆库**。让你的 AI 拥有跨模型，跨会话，跨工具的持久的结构化记忆。

1037. **[MCP-connect](https://github.com/EvalsOne/MCP-connect)** - ⭐ 232
   Enables cloud-based AI services to access local Stdio based MCP servers via HTTP requests

1038. **[omnicoreagent](https://github.com/omnirexflora-labs/omnicoreagent)** - ⭐ 232
   OmniCoreAgent is a powerful Python framework for building autonomous AI agents that think, reason, and execute complex tasks. Production-ready agents that use tools, manage memory, coordinate workflows, and handle real-world business logic.

1039. **[TradingAgents-MCPmode](https://github.com/guangxiangdebizi/TradingAgents-MCPmode)** - ⭐ 232
   TradingAgents-MCPmode 是一个创新的多智能体交易分析系统，集成了 Model Context Protocol (MCP) 工具，实现了智能化的股票分析和交易决策流程。系统通过多个专业化智能体的协作，提供全面的市场分析、投资建议和风险管理。

1040. **[Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server)** - ⭐ 232
   A MCP Server for Google Scholar: 🔍 Enable AI assistants to search and access Google Scholar papers through a simple MCP interface.

1041. **[pageindex-mcp](https://github.com/VectifyAI/pageindex-mcp)** - ⭐ 232
   MCP server for PageIndex. PageIndex is a vectorless reasoning-based RAG system which uses multi-step reasoning and tree search to retrieve information like a human expert would.

1042. **[api-agent](https://github.com/agoda-com/api-agent)** - ⭐ 232
   Universal MCP server for GraphQL/REST APIs

1043. **[Lambda-MCP-Server](https://github.com/mikegc-aws/Lambda-MCP-Server)** - ⭐ 231
   Creates a simple MCP tool server with "streaming" HTTP.

1044. **[xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server)** - ⭐ 231
   A Model Context Protocol (MCP) server that enables natural language queries to databases

1045. **[sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers)** - ⭐ 230
   Sample implementations of AI Agents and MCP Servers running on AWS Serverless compute

1046. **[playwright-mcp](https://github.com/cloudflare/playwright-mcp)** - ⭐ 230
   Playwright MCP fork that works with Cloudflare Browser Rendering

1047. **[MiroRL](https://github.com/MiroMindAI/MiroRL)** - ⭐ 229
   MiroRL is  an MCP-first reinforcement learning framework for deep research agent.

1048. **[vulnerable-mcp-servers-lab](https://github.com/appsecco/vulnerable-mcp-servers-lab)** - ⭐ 229
   A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers.

1049. **[tmux-mcp](https://github.com/nickgnd/tmux-mcp)** - ⭐ 228
   A MCP server for our beloved terminal multiplexer tmux.

1050. **[remote-swe-agents](https://github.com/aws-samples/remote-swe-agents)** - ⭐ 228
   Autonomous SWE agent working in the cloud! (a.k.a. Vibe coding with Bedrock)

1051. **[mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)** - ⭐ 227
   A MCP Server for Azure AI Foundry: it's now moved to cloud, check the new Foundry MCP Server

1052. **[cobolt](https://github.com/platinum-hill/cobolt)** - ⭐ 227
   This is a cross-platform desktop application that allows you to chat with locally hosted LLMs and enjoy features like MCP support

1053. **[mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret)** - ⭐ 227
   MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. 

1054. **[mcp-openapi-server](https://github.com/ivo-toby/mcp-openapi-server)** - ⭐ 227
   MCP Server (Model Context Protocol) for turning OpenAPI specifications into a MCP Resource

1055. **[mcp-compass](https://github.com/liuyoshio/mcp-compass)** - ⭐ 227
   MCP Discovery & Recommendation Service - Find the right MCP server for your needs

1056. **[Alice](https://github.com/pmbstyle/Alice)** - ⭐ 226
   Alice is a voice-first desktop AI assistant application built with Vue.js, Vite, and Electron. Advanced memory system, function calling, MCP support, optional fully local use, and more.

1057. **[mcp-server-commands](https://github.com/g0t4/mcp-server-commands)** - ⭐ 225
   Model Context Protocol server to run commands (tool: `runProcess`)

1058. **[antd-components-mcp](https://github.com/zhixiaoqiang/antd-components-mcp)** - ⭐ 225
   An MCP service for Ant Design components query | 一个减少 Ant Design 组件代码生成幻觉的 MCP 服务，包含系统提示词、组件文档、API 文档、代码示例和更新日志查询

1059. **[kite-mcp-server](https://github.com/zerodha/kite-mcp-server)** - ⭐ 225
   Zerodha Kite MCP server

1060. **[claude-historian-mcp](https://github.com/Vvkmnn/claude-historian-mcp)** - ⭐ 225
   📜 An MCP server for conversation history search and retrieval in Claude Code

1061. **[data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers)** - ⭐ 224
   Korea public data portal (data.go.kr) API MCP servers

1062. **[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** - ⭐ 224
   This is a Model Context Protocol (MCP) server that provides comprehensive financial data from Yahoo Finance. It allows you to retrieve detailed information about stocks, including historical prices, company information, financial statements, options data, and market news.

1063. **[ruby_llm-mcp](https://github.com/patvice/ruby_llm-mcp)** - ⭐ 224
   Full-featured MCP support for Ruby and RubyLLM—making it easy to build structured, composable LLM workflows in pure Ruby.

1064. **[claude-context-mode](https://github.com/mksglu/claude-context-mode)** - ⭐ 224
   Stop losing context to large outputs.

1065. **[mcp-twikit](https://github.com/adhikasp/mcp-twikit)** - ⭐ 223
   A Model Context Protocol (MCP) server for interacting with Twitter.

1066. **[life-sciences](https://github.com/anthropics/life-sciences)** - ⭐ 223
   Repo for the Claude Code Marketplace to use with the Claude for Life Sciences Launch. This will continue to host the marketplace.json long-term, but not the actual MCP servers.

1067. **[cpp-mcp](https://github.com/hkr04/cpp-mcp)** - ⭐ 223
   Lightweight C++ MCP (Model Context Protocol) SDK

1068. **[llamacloud-mcp](https://github.com/run-llama/llamacloud-mcp)** - ⭐ 222

1069. **[langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)** - ⭐ 222
   A template for building WhatsApp agents using LangGraph and Twilio. This project enables you to deploy AI agents that interact with users via WhatsApp, process messages and images, and invoke custom graph-based agents. It integrates with MCP and runs on the LangGraph Platform.

1070. **[effect-mcp](https://github.com/tim-smart/effect-mcp)** - ⭐ 222

1071. **[anki-mcp-server](https://github.com/nailuoGG/anki-mcp-server)** - ⭐ 222
   MCP server for Anki via AnkiConnect

1072. **[mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)** - ⭐ 222
   A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images

1073. **[penpot-mcp](https://github.com/montevive/penpot-mcp)** - ⭐ 222
   Penpot MCP server

1074. **[garmin_mcp](https://github.com/Taxuspt/garmin_mcp)** - ⭐ 222
   MCP server to access Garmin data

1075. **[robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp)** - ⭐ 222
   Create agentic AI workflows in ROBLOX Studio

1076. **[agent-mcp-lab](https://github.com/WaveSpeedAI/agent-mcp-lab)** - ⭐ 221

1077. **[smart-tree](https://github.com/8b-is/smart-tree)** - ⭐ 221
   Smart Tree: not just a tree, a philosophy. A context-aware, AI-crafted replacement for 20+ tools with MEM8 quantum compression, semantic search, AST-smart editing, and partnership memory. Crafted with care by human + AI—accept no knock-offs.

1078. **[learn-agentic-ai-from-low-code-to-code](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code)** - ⭐ 221
   Build production-grade agents with OpenAI AgentKit, a no-code platfrom.

1079. **[mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)** - ⭐ 221
   基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务

1080. **[lokka](https://github.com/merill/lokka)** - ⭐ 220
   MCP (Model Context Protocol) for Microsoft 365. Includes support for Microsoft Graph and other services

1081. **[Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)** - ⭐ 220
   MCP Server built for use with Claude Code, Claude Desktop, VS Code, Cline  - enable google search and ability to follow links and research websites

1082. **[plate-playground-template](https://github.com/udecode/plate-playground-template)** - ⭐ 220
   Plate AI template with React 19, Next 16, Tailwind 4, MCP.

1083. **[composer-trade-mcp](https://github.com/invest-composer/composer-trade-mcp)** - ⭐ 220
   Composer's MCP server lets MCP-enabled LLMs like Claude backtest trading ideas and automatically invest in them for you

1084. **[home-assistant-cursor-agent](https://github.com/Coolver/home-assistant-cursor-agent)** - ⭐ 219
   Enable Cursor AI, VS Code, or any MCP-enabled IDE to help you manage Home Assistant: create automations, modify configs, and deploy changes using natural language

1085. **[claude-config-editor](https://github.com/gagarinyury/claude-config-editor)** - ⭐ 219
   Claude Config Editor is a lightweight web tool that helps you clean and optimize your Claude Code/Desktop config files (.claude.json). Analyze project sizes, bulk delete chat histories, export data for backup, manage servers visually, and speed up Claude—all locally, with auto-backup, no dependencies, and cross-platform support.

1086. **[human-in-the-loop](https://github.com/KOBA789/human-in-the-loop)** - ⭐ 218
   An MCP (Model Context Protocol) server that allows AI assistants to ask questions to humans via Discord.

1087. **[domainstack.io](https://github.com/jakejarvis/domainstack.io)** - ⭐ 217
   🧰 All-in-one domain name intelligence as a service

1088. **[yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)** - ⭐ 217
   A Model Context Protocol (MCP) server that bridges Video & Audio content with Large Language Models using yt-dlp.

1089. **[image-gen-server](https://github.com/fengin/image-gen-server)** - ⭐ 217
   一个能与Cursor集成的图片生成mcp server工具，实现调用即梦逆向接口

1090. **[MakeMoneyWithAI](https://github.com/garylab/MakeMoneyWithAI)** - ⭐ 217
   A list of open-source AI projects you can use to generate income easily.

1091. **[tentix](https://github.com/labring/tentix)** - ⭐ 216
   TenTix (10x Efficiency) - An AI native customer service platform with 10x accelerated resolution. Support MCP extension, and AI knowlage base system.

1092. **[mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server)** - ⭐ 216
   mindmap, mcp server, artifact

1093. **[overseer](https://github.com/dmmulroy/overseer)** - ⭐ 216
   CLI & Codemode MCP server for agent task management

1094. **[after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp)** - ⭐ 216
   MCP Server for Adobe After Effects. Enables remote control (compositions, text, shapes, solids, properties) via the Model Context Protocol using ExtendScript.

1095. **[frida-mcp](https://github.com/dnakov/frida-mcp)** - ⭐ 216
   MCP stdio server for frida

1096. **[mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus)** - ⭐ 215
   Model Context Protocol Servers for Milvus

1097. **[mcp_code_executor](https://github.com/bazinga012/mcp_code_executor)** - ⭐ 215
   The MCP Code Executor is an MCP server that allows LLMs to execute Python code within a specified Conda environment.

1098. **[uber-eats-mcp-server](https://github.com/ericzakariasson/uber-eats-mcp-server)** - ⭐ 215

1099. **[vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp)** - ⭐ 214
   Agent MCP for ffmpeg

1100. **[razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server)** - ⭐ 214
   Razorpay's Official MCP Server

1101. **[lihil](https://github.com/raceychan/lihil)** - ⭐ 213
   2X faster ASGI web framework for python, offering high-level development, low-level performance.

1102. **[claudex](https://github.com/Mng-dev-ai/claudex)** - ⭐ 213
   Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

1103. **[sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp)** - ⭐ 213
   A SEC EDGAR MCP (Model Context Protocol) Server

1104. **[gibber-mcp](https://github.com/antonpk1/gibber-mcp)** - ⭐ 212
   Tiny MCP server with cryptography tools, sufficient to establish end-to-end encryption between LLM agents

1105. **[gram](https://github.com/speakeasy-api/gram)** - ⭐ 212
   Context layer for your product. Connect your agents and chat to 1st and 3rd party MCP servers!

1106. **[skyll](https://github.com/assafelovic/skyll)** - ⭐ 212
   A tool for AI agents to discover and learn skills autonomously

1107. **[mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)** - ⭐ 211
   MasterGo Magic MCP is a standalone MCP (Model Context Protocol) service designed to connect MasterGo design tools with AI models.

1108. **[jebmcp](https://github.com/dawnslab/jebmcp)** - ⭐ 211

1109. **[mathom](https://github.com/stephenlacy/mathom)** - ⭐ 211
   Run and monitor MCP servers locally

1110. **[mcp-taskmanager](https://github.com/kazuph/mcp-taskmanager)** - ⭐ 210

1111. **[multimodal-mcp-client](https://github.com/Ejb503/multimodal-mcp-client)** - ⭐ 210
   A Multi-modal MCP client for voice powered agentic workflows

1112. **[mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder)** - ⭐ 210
   AI-powered n8n workflow automation through natural language. MCP server enabling Claude AI & Cursor IDE to create, manage, and monitor workflows via Model Context Protocol. Multi-instance support, 17 tools, comprehensive docs. Build workflows conversationally without manual JSON editing.

1113. **[automagik-genie](https://github.com/namastexlabs/automagik-genie)** - ⭐ 210
   🧞 Automagik Genie – bootstrap, update, and roll back AI agent workspaces with a single CLI + MCP toolkit.

1114. **[sora-mcp](https://github.com/Doriandarko/sora-mcp)** - ⭐ 210
   An MCP server to use Sora video generation APIs

1115. **[Autono](https://github.com/vortezwohl/Autono)** - ⭐ 209
   A ReAct-Based Highly Robust Autonomous Agent Framework.

1116. **[figma-mcp](https://github.com/MatthewDailey/figma-mcp)** - ⭐ 209
   ModelContextProtocol for Figma's REST API

1117. **[ha-mcp-for-xiaozhi](https://github.com/c1pher-cn/ha-mcp-for-xiaozhi)** - ⭐ 209
   Homeassistant MCP server for 小智AI

1118. **[mcp-echarts](https://github.com/hustcc/mcp-echarts)** - ⭐ 209
   🧬 Generate visual charts using ECharts with AI MCP dynamically, used for chart generation and data analysis.

1119. **[servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp)** - ⭐ 209
   MCP Server for ServiceNow

1120. **[flyto-core](https://github.com/flytohub/flyto-core)** - ⭐ 209
   The open-source execution engine for AI agents. 412 modules, MCP-native, triggers, queue, versioning, metering.

1121. **[mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research)** - ⭐ 208

1122. **[jetski](https://github.com/hyprmcp/jetski)** - ⭐ 208
   Authentication, analytics, and prompt visibility for MCP servers with zero code changes. Supports OAuth2.1, DCR, real-time logs, and client onboarding out of the box

1123. **[MimikaStudio](https://github.com/BoltzmannEntropy/MimikaStudio)** - ⭐ 208
   MimikaStudio - A local-first application for macOS (Apple Silicon) + Agentic MCP Support

1124. **[lyraios](https://github.com/GalaxyLLMCI/lyraios)** - ⭐ 207
   LYRAI is a Model Context Protocol (MCP) operating system for multi-AI AGENTs designed to extend the functionality of AI applications by enabling them to interact with financial networks and blockchain public chains. The server offers a range of advanced AI assistants, including blockchain public chain operations (SOLANA,ETH,BSC,etc.)

1125. **[ht-mcp](https://github.com/memextech/ht-mcp)** - ⭐ 207
   Pure Rust implementation of MCP server for headless terminal 

1126. **[mcp-servers-nix](https://github.com/natsukium/mcp-servers-nix)** - ⭐ 207
   A Nix-based configuration framework for Model Control Protocol (MCP) servers with ready-to-use packages.

1127. **[mcp-context-protector](https://github.com/trailofbits/mcp-context-protector)** - ⭐ 206
   MCP security wrapper

1128. **[Remote-MCP](https://github.com/ssut/Remote-MCP)** - ⭐ 206
   A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.

1129. **[melrose](https://github.com/emicklei/melrose)** - ⭐ 206
   interactive programming of melodies, producing MIDI 

1130. **[penpot-mcp](https://github.com/penpot/penpot-mcp)** - ⭐ 206
   Penpot's official MCP Server

1131. **[pctx](https://github.com/portofcontext/pctx)** - ⭐ 206
   pctx is the execution layer for agentic tool calls. It auto-converts agent tools and MCP servers into code that runs in secure sandboxes for token-efficient workflows.

1132. **[cocoindex-code](https://github.com/cocoindex-io/cocoindex-code)** - ⭐ 206
   A super light-weight embedded code mcp (AST based) that just works - saves 70% token and improves speed for coding agent. 🌟 Star if you like it!

1133. **[mcp-rb](https://github.com/funwarioisii/mcp-rb)** - ⭐ 205
   A lightweight Ruby framework for building MCP servers with a Sinatra-like DSL

1134. **[OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)** - ⭐ 205

1135. **[notion_mcp](https://github.com/danhilse/notion_mcp)** - ⭐ 205
   A simple MCP integration that allows Claude to read and manage a personal Notion todo list

1136. **[AutomatedEmulation](https://github.com/iknowjason/AutomatedEmulation)** - ⭐ 205
   An automated Adversary Emulation lab with terraform and MCP server.  Build Caldera techniques and operations assisted with LLMs.  Built for IaC stability, consistency, and speed.

1137. **[phone-mcp](https://github.com/hao-cyber/phone-mcp)** - ⭐ 205
   A phone control plugin for MCP that allows you to control your Android phone through ADB commands to connect any human

1138. **[BifrostMCP](https://github.com/biegehydra/BifrostMCP)** - ⭐ 205
   VSCode Extension with an MCP server that exposes semantic tools like Find Usages and Rename to LLMs

1139. **[langchain-mcp](https://github.com/rectalogic/langchain-mcp)** - ⭐ 205
   Model Context Protocol tool support for LangChain

1140. **[unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)** - ⭐ 205
   🔎 A MCP server for Unsplash image search.

1141. **[sqrl](https://github.com/DataSQRL/sqrl)** - ⭐ 205
   Data Pipeline Automation Framework to build MCP servers, data APIs, and data lakes with SQL.

1142. **[dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** - ⭐ 205
   MCP server for Dynatrace Observability

1143. **[appium-mcp](https://github.com/appium/appium-mcp)** - ⭐ 205
   Appium MCP on Steroids!

1144. **[claude-self-reflect](https://github.com/ramakay/claude-self-reflect)** - ⭐ 204
   Claude forgets everything. This fixes that. 🔗 www.npmjs.com/package/claude-self-reflect

1145. **[touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp)** - ⭐ 204
   MCP server for TouchDesigner

1146. **[comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server)** - ⭐ 204
   lightweight Python-based MCP (Model Context Protocol) server for local ComfyUI

1147. **[ai-infrastructure-agent](https://github.com/VersusControl/ai-infrastructure-agent)** - ⭐ 203
   AI Infrastructure Agent is an intelligent system that allows you to manage AWS infrastructure using natural language commands.

1148. **[mcp-servers](https://github.com/cursor/mcp-servers)** - ⭐ 203
   A list of MCP (Model Context Protocol) servers for developer tools and services

1149. **[y-cli](https://github.com/luohy15/y-cli)** - ⭐ 202
   A Tiny Terminal Chat App for AI Models with MCP Client Support

1150. **[figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp)** - ⭐ 202
   An MCP server that provides the coding agents Figma's design token to write Flutter code.

1151. **[nosia](https://github.com/dilolabs/nosia)** - ⭐ 201
   Self-hosted AI RAG + MCP Platform

1152. **[airbroke](https://github.com/icoretech/airbroke)** - ⭐ 201
   🔥 Lightweight, Airbrake/Sentry-compatible, PostgreSQL-based Open Source Error Catcher

1153. **[metorial-platform](https://github.com/metorial/metorial-platform)** - ⭐ 201
   The engine powering hundreds of thousands of MCP connections 🤖 🔥

1154. **[pbi-desktop-mcp-public](https://github.com/maxanatsko/pbi-desktop-mcp-public)** - ⭐ 201
   The MCP Engine is a Power BI tool that lets AI assistants like Claude interact with your Power BI models programmatically: read your model structure, run DAX queries, create and modify measures, manage relationships, and perform advanced analytics - all through natural conversation.

1155. **[k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server)** - ⭐ 201
   K8s-mcp-server is a Model Context Protocol (MCP) server that enables AI assistants like Claude to securely execute Kubernetes commands. It provides a bridge between language models and essential Kubernetes CLI tools including kubectl, helm, istioctl, and argocd, allowing AI systems to assist with cluster management, troubleshooting, and deployments

1156. **[persistent-ai-memory](https://github.com/savantskie/persistent-ai-memory)** - ⭐ 201
   A persistent local memory for AI, LLMs, or Copilot in VS Code.

1157. **[mcp](https://github.com/hopx-ai/mcp)** - ⭐ 200

1158. **[mcp-launchpad](https://github.com/kenneth-liao/mcp-launchpad)** - ⭐ 200
   A lightweight CLI for efficiently discovering (search) and executing tools from multiple MCP (Model Context Protocol) servers.

1159. **[goclaw](https://github.com/nextlevelbuilder/goclaw)** - ⭐ 200
   Multi-agent AI gateway with teams, delegation & orchestration. Single Go binary, 11+ LLM providers, 5 channels.

1160. **[mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** - ⭐ 199
   A MCP Server for the RAG Web Browser Actor

1161. **[mongodb-lens](https://github.com/furey/mongodb-lens)** - ⭐ 199
   🍃🔎 MongoDB Lens: Full Featured MCP Server for MongoDB Databases

1162. **[AIDA](https://github.com/Vasco0x4/AIDA)** - ⭐ 199
   AI-Driven Security Assessment - Connect AI to 400+ pentesting tools via MCP

1163. **[rmcp](https://github.com/finite-sample/rmcp)** - ⭐ 198
   R MCP Server

1164. **[opik-mcp](https://github.com/comet-ml/opik-mcp)** - ⭐ 198
   Model Context Protocol (MCP) implementation for Opik enabling seamless IDE integration and unified access to prompts, projects, traces, and metrics. 

1165. **[wavefront](https://github.com/rootflo/wavefront)** - ⭐ 198
   🔥🔥🔥 Enterprise AI middleware, alternative to unifyapps, n8n, lyzr

1166. **[sudocode](https://github.com/sudocode-ai/sudocode)** - ⭐ 198
   Lightweight agent orchestration dev tool that lives in your repo

1167. **[mcp-proxy-server](https://github.com/adamwattis/mcp-proxy-server)** - ⭐ 197
   An MCP proxy server that aggregates and serves multiple MCP resource servers through a single interface

1168. **[hf-mcp-server](https://github.com/huggingface/hf-mcp-server)** - ⭐ 197
   Hugging Face MCP Server

1169. **[nano-agent](https://github.com/disler/nano-agent)** - ⭐ 197
   A MCP Server for a small scale engineering agents with multi-provider LLM support.

1170. **[ProxmoxMCP](https://github.com/canvrno/ProxmoxMCP)** - ⭐ 196
   MCP for Proxmox integration in Cline

1171. **[waldzell-mcp](https://github.com/waldzellai/waldzell-mcp)** - ⭐ 196
   Waldzell AI's monorepo of MCP servers. Use in Claude Desktop, Cline, Roo Code, and more!

1172. **[mcp_forge](https://github.com/mlzoo/mcp_forge)** - ⭐ 196
   这是一个专为开发企业级MCP server而设计的通用开发框架

1173. **[cognition-wheel](https://github.com/Hormold/cognition-wheel)** - ⭐ 196
   A Model Context Protocol (MCP) server that implements a "wisdom of crowds" approach to AI reasoning by consulting multiple state-of-the-art language models in parallel and synthesizing their responses.

1174. **[mcp-logseq](https://github.com/ergut/mcp-logseq)** - ⭐ 196
   MCP server to interact with LogSeq via its Local HTTP API - enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph.

1175. **[mcp-portal-transparencia](https://github.com/dutradotdev/mcp-portal-transparencia)** - ⭐ 195
   MCP para orquestração automatizada de chamadas à API do Portal da Transparência do Governo Federal brasileiro

1176. **[EdgeBox](https://github.com/BIGPPWONG/EdgeBox)** - ⭐ 195
   A fully-featured, GUI-powered local LLM Agent sandbox with complete MCP protocol support.   Features both CLI and full desktop environment, enabling AI agents to operate browsers, terminal, and other desktop applications just like humans. Based on E2B oss code.

1177. **[burp-mcp-agents](https://github.com/six2dez/burp-mcp-agents)** - ⭐ 194
   Practical setup guides and helpers to connect Burp Suite MCP Server to multiple AI backends (Codex, Gemini, Ollama, ...).

1178. **[gcp-mcp](https://github.com/eniayomi/gcp-mcp)** - ⭐ 193
   A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Google Cloud Platform environment. This allows for natural language querying and management of your GCP resources during conversations.

1179. **[claude-context-local](https://github.com/FarhanAliRaza/claude-context-local)** - ⭐ 193
   Code search MCP for Claude Code. Make entire codebase the context for any coding agent. Embeddings are created and stored locally. No API cost. 

1180. **[PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor)** - ⭐ 193
   Free, open-source SQL Server performance monitoring. Full Edition (server-installed, 30 collectors) and Lite Edition (standalone, DuckDB). Built-in MCP server for AI integration.

1181. **[mcp-guardian](https://github.com/eqtylab/mcp-guardian)** - ⭐ 192
   Manage / Proxy / Secure your MCP Servers

1182. **[easy-mcp](https://github.com/zcaceres/easy-mcp)** - ⭐ 192
   Absurdly easy Model Context Protocol Servers in Typescript

1183. **[MCP-server-client-computer-use-ai-sdk](https://github.com/mediar-ai/MCP-server-client-computer-use-ai-sdk)** - ⭐ 192

1184. **[RelaMind](https://github.com/El-12stu/RelaMind)** - ⭐ 192
   基于 AI 的个人成长轨迹分析系统，通过记录生活、回顾历史、分析模式帮助用户更好地理解自己，实现持续成长。包含智能路由、RAG 检索、自主任务智能体等功能。

1185. **[AutoDocs](https://github.com/TrySita/AutoDocs)** - ⭐ 192
   We handle what engineers and IDEs won't: generating and maintaining technical documentation for your codebase, while also providing search with dependency-aware context to help your AI tools understand your codebase and its conventions.

1186. **[utcp-mcp](https://github.com/universal-tool-calling-protocol/utcp-mcp)** - ⭐ 192
   All-in-one MCP server that can connect your AI agents to any native endpoint, powered by UTCP

1187. **[mcp-fusion](https://github.com/vinkius-labs/mcp-fusion)** - ⭐ 192
   Create your MCP server at lightspeed - The MVA framework for the Model Context Protocol. Build production-grade MCP servers with type safety, behavioral governance, and zero boilerplate.

1188. **[mcp-agent-graph](https://github.com/keta1930/mcp-agent-graph)** - ⭐ 191
   MCP Agent Graph is a Multi-Agent System built on the principles of Context Engineering

1189. **[xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server)** - ⭐ 191
   An MCP server that integrates with the MCP protocol. https://modelcontextprotocol.io/introduction

1190. **[seo-mcp](https://github.com/cnych/seo-mcp)** - ⭐ 190
   A free SEO tool MCP (Model Control Protocol) service based on Ahrefs data. Includes features such as backlinks, keyword ideas, and more.

1191. **[mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** - ⭐ 190
   A Model Context Protocol (MCP) server that provides tools to interact with LinkedIn's Feeds and Job API.

1192. **[armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp)** - ⭐ 190
   The MCP server for interacting with Blockchain, Swaps, Strategic Planning and more.

1193. **[ai-counsel](https://github.com/blueman82/ai-counsel)** - ⭐ 190
   True deliberative consensus MCP server where AI models debate and refine positions across multiple rounds

1194. **[discord-mcp](https://github.com/SaseQ/discord-mcp)** - ⭐ 190
   A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.

1195. **[Geargrafx](https://github.com/drhelius/Geargrafx)** - ⭐ 189
   PC Engine / TurboGrafx-16 / SuperGrafx / PCE CD-ROM² emulator, debugger, and embedded MCP server for macOS, Windows, Linux, BSD and RetroArch.

1196. **[supabase-mcp](https://github.com/coleam00/supabase-mcp)** - ⭐ 189
   Supabase MCP server created in Python.

1197. **[wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp)** - ⭐ 189
   A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

1198. **[auto-mcp](https://github.com/brizzai/auto-mcp)** - ⭐ 189
   Transform any OpenAPI/Swagger definition into a fully-featured Model Context Protocol (MCP) server

1199. **[ssh-mcp-server](https://github.com/classfang/ssh-mcp-server)** - ⭐ 189
   基于 SSH 的 MCP 服务器 🧙‍♀️。已被MCP官方收录 🎉。 SSH MCP Server 🧙‍♀️. It has been included in the community MCP repository 🎉.

1200. **[smart-coding-mcp](https://github.com/omar-haris/smart-coding-mcp)** - ⭐ 188
   An extensible Model Context Protocol (MCP-Local-MRL-RAG-AST) server that provides intelligent semantic code search for AI assistants. Built with local AI models, inspired by Cursor's semantic search.

1201. **[claudepro-directory](https://github.com/JSONbored/claudepro-directory)** - ⭐ 188
   Claude Pro Directory is a searchable collection of pre-built configurations, MCP servers, and custom rules designed to enhance Claude AI's performance for specific tasks.

1202. **[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** - ⭐ 188
   🤖 AI-Powered MCP Server for Polymarket - Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features

1203. **[code-sandbox-mcp](https://github.com/philschmid/code-sandbox-mcp)** - ⭐ 187

1204. **[mcp-usecase](https://github.com/teddynote-lab/mcp-usecase)** - ⭐ 187

1205. **[mcp-injection-experiments](https://github.com/invariantlabs-ai/mcp-injection-experiments)** - ⭐ 187
   Code snippets to reproduce MCP tool poisoning attacks.

1206. **[gistpad-mcp](https://github.com/lostintangent/gistpad-mcp)** - ⭐ 187
   📓 An MCP server for managing your personal knowledge, daily notes, and re-usable prompts via GitHub Gists

1207. **[protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp)** - ⭐ 187
   Go protobuf compiler extension to turn any gRPC service into an MCP server

1208. **[tableau-mcp](https://github.com/tableau/tableau-mcp)** - ⭐ 187
   Official Tableau MCP server, providing a suite of tools that make it easier for developers to build and configure AI applications that integrate with Tableau Cloud and Server.

1209. **[mcp-proxy-server](https://github.com/ptbsare/mcp-proxy-server)** - ⭐ 187
   This server acts as a central hub for Model Context Protocol (MCP) resource servers.

1210. **[bluebox](https://github.com/VectorlyApp/bluebox)** - ⭐ 187
   Index the world's undocumented APIs

1211. **[Omni-Adapter](https://github.com/HuChundong/Omni-Adapter)** - ⭐ 186
   多平台 文生图/图生图 等能力接入MCP

1212. **[mcp-google-map](https://github.com/cablate/mcp-google-map)** - ⭐ 186
   A powerful Model Context Protocol (MCP) server providing comprehensive Google Maps API integration with LLM processing capabilities.

1213. **[MCP-Checklists](https://github.com/MCP-Manager/MCP-Checklists)** - ⭐ 186

1214. **[coolify-mcp](https://github.com/StuMason/coolify-mcp)** - ⭐ 186
   MCP server for Coolify — 38 optimized tools for managing self-hosted PaaS through AI assistants

1215. **[litemcp](https://github.com/wong2/litemcp)** - ⭐ 185
   A TypeScript framework for building MCP servers elegantly

1216. **[git-mcp-server](https://github.com/cyanheads/git-mcp-server)** - ⭐ 185
   An MCP (Model Context Protocol) server enabling LLMs and AI agents to interact with Git repositories. Provides tools for comprehensive Git operations including clone, commit, branch, diff, log, status, push, pull, merge, rebase, worktree, tag management, and more, via the MCP standard. STDIO & HTTP.

1217. **[matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server)** - ⭐ 185
   Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code.

1218. **[a2a_mcp-example](https://github.com/ishanExtreme/a2a_mcp-example)** - ⭐ 184
   An example showing how A2A and MCP can be used together

1219. **[quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers)** - ⭐ 184
   Model Context Protocol Servers in Quarkus

1220. **[ida-mcp-server-plugin](https://github.com/taida957789/ida-mcp-server-plugin)** - ⭐ 184
   IDA Pro Plugin for serving MCP SSE server for cursor / claude

1221. **[agentregistry](https://github.com/agentregistry-dev/agentregistry)** - ⭐ 184
   Fast-track AI innovation with a centralized, trusted, curated registry

1222. **[dify-plugin-tools-mcp_sse](https://github.com/junjiem/dify-plugin-tools-mcp_sse)** - ⭐ 183
   Dify 1.0 Plugin MCP HTTP with SSE or Streamable HTTP transport Tools

1223. **[facebook-ads-library-mcp](https://github.com/talknerdytome-labs/facebook-ads-library-mcp)** - ⭐ 183
   MCP Server for Facebook ADs Library - Get instant answers from FB's ad library

1224. **[siconos](https://github.com/siconos/siconos)** - ⭐ 182
   Simulation framework for nonsmooth dynamical systems

1225. **[thinkchain](https://github.com/martinbowling/thinkchain)** - ⭐ 182
   🧠 Advanced Claude streaming interface with interleaved thinking, dynamic tool discovery, and MCP integration. Watch Claude think through problems in real-time while executing tools with live progress updates.

1226. **[mcp-openai-gemini-llama-example](https://github.com/philschmid/mcp-openai-gemini-llama-example)** - ⭐ 182

1227. **[mcp](https://github.com/neo4j/mcp)** - ⭐ 182
   Neo4j official MCP Server

1228. **[google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp)** - ⭐ 182
   Google Analytics 4 MCP Server for Claude, Cursor, Windsurf etc - Access GA4 data through natural language with 200+ dimensions & metrics

1229. **[4D-ARE](https://github.com/ybeven/4D-ARE)** - ⭐ 181
   Build LLM agents that explain why, not just what. Attribution-driven agent requirements engineering framework. Based on the 4D-ARE Paper - https://arxiv.org/abs/2601.04556

1230. **[mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts)** - ⭐ 181
   MCP for calling Siri Shorcuts from LLMs

1231. **[quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server)** - ⭐ 180
   This extension enables developers to implement the MCP server features easily.

1232. **[postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)** - ⭐ 180
   Connect your AI to your APIs on Postman

1233. **[drawio2go](https://github.com/Menghuan1918/drawio2go)** - ⭐ 179
   A modern DrawIO editor application.  AI-Powered, Human-AI Collaboration | AI 加持，人机共绘drawio

1234. **[mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server)** - ⭐ 179

1235. **[mcp-text-editor](https://github.com/tumf/mcp-text-editor)** - ⭐ 178

1236. **[claude-code-mcp](https://github.com/auchenberg/claude-code-mcp)** - ⭐ 178
   claude-code-mcp

1237. **[bilibili-mcp-server](https://github.com/huccihuang/bilibili-mcp-server)** - ⭐ 178
   MCP Server for the Bilibili API, supporting various operations.

1238. **[mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh)** - ⭐ 178
   MCP Server for Wazuh SIEM

1239. **[sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)** - ⭐ 178
   Sketchup Model Context Protocol

1240. **[aws-mcp-server](https://github.com/alexei-led/aws-mcp-server)** - ⭐ 178
   A lightweight service that enables AI assistants to execute AWS CLI commands (in safe containerized environment) through the Model Context Protocol (MCP). Bridges Claude, Cursor, and other MCP-aware AI tools with AWS CLI for enhanced cloud infrastructure management.

1241. **[linux-mcp-server](https://github.com/rhel-lightspeed/linux-mcp-server)** - ⭐ 178
   Tools to allow LLM clients to interact with Linux systems remotely

1242. **[markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)** - ⭐ 178
   An MCP server for converting Markdown to interactive mind maps with export support (PNG/JPG/SVG).

1243. **[tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)** - ⭐ 177
   Official MCP server for Tripo

1244. **[spring-ai-playground](https://github.com/JM-Lab/spring-ai-playground)** - ⭐ 177
   A self-hosted web UI that simplifies AI experimentation and testing for Java developers. It provides playgrounds for all major vector databases and MCP tools, supports intuitive interaction with LLMs, and enables rapid development and testing of RAG workflows, MCP integrations, and unified chat experiences.

1245. **[Context-Engineering-for-Multi-Agent-Systems](https://github.com/Denis2054/Context-Engineering-for-Multi-Agent-Systems)** - ⭐ 177
   Save thousands of lines of code by building universal, domain-agnostic Multi-Agent Systems (MAS) through high-level semantic orchestration. This repository provides a production-ready blueprint for the Agentic Era, allowing you to replace rigid, hard-coded workflows with a dynamic transparent Context Engine that provides 100% transparency.

1246. **[anki-mcp-server](https://github.com/scorzeth/anki-mcp-server)** - ⭐ 176
   An MCP server for Anki

1247. **[mcp](https://github.com/magicuidesign/mcp)** - ⭐ 176
   Official Magic UI MCP server.

1248. **[discordmcp](https://github.com/v-3/discordmcp)** - ⭐ 175
   Discord MCP Server for Claude Integration

1249. **[mcp-chat](https://github.com/PipedreamHQ/mcp-chat)** - ⭐ 175
   Examples of using Pipedream's MCP server in your app or AI agent.

1250. **[tomcp](https://github.com/Ami3466/tomcp)** - ⭐ 175
   Turn any website or doc into an MCP server

1251. **[forgetful](https://github.com/ScottRBK/forgetful)** - ⭐ 175
   Opensource Memory for Agents

1252. **[aws-finops-mcp-server](https://github.com/ravikiranvm/aws-finops-mcp-server)** - ⭐ 174
   An MCP (Model Context Protocol) server that brings powerful AWS FinOps capabilities directly into your AI assistant. Analyze cloud costs, audit for waste, and get budget insights using natural language, all while keeping your credentials secure on your local machine.

1253. **[mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp)** - ⭐ 174
   A mongo db server for the model context protocol (MCP)

1254. **[Revornix](https://github.com/Qingyon-AI/Revornix)** - ⭐ 174
   Built-in MCP client–powered document/news management tool with daily auto summaries, document interaction, user-defined notifications (email, apns, etc.), and customizable model support.内置 MCP 客户端的文档/资讯管理工具，支持每日自动总结、文档交互、自定义通知（邮箱、APNS等）以及模型自定义。

1255. **[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server)** - ⭐ 174
   IMAP and SMTP via MCP Server

1256. **[unifi-network-mcp](https://github.com/sirkirby/unifi-network-mcp)** - ⭐ 174
   MCP server implementation for the UniFi network application

1257. **[mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb)** - ⭐ 173
   A Model Context Protocol (MCP) server implementation for DuckDB, providing database interaction capabilities

1258. **[integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)** - ⭐ 173
   Learn how to use MCP Servers with GitHub Copilot

1259. **[DrissionPageMCP](https://github.com/wxhzhwxhzh/DrissionPageMCP)** - ⭐ 173
   基于DrissionPage和FastMCP的浏览器自动化MCP服务器，提供丰富的浏览器操作API供AI调用

1260. **[openapi-mcp](https://github.com/ckanthony/openapi-mcp)** - ⭐ 172
   Dockerized MCP Server to allow your AI agent to access any API with existing api docs

1261. **[install-mcp](https://github.com/supermemoryai/install-mcp)** - ⭐ 172
   A simple CLI to install MCP servers into any client - auth included!

1262. **[command](https://github.com/scopecraft/command)** - ⭐ 172
   Scopecraft Command - A CLI and MCP server for Markdown-Driven Task Management (MDTM)

1263. **[skunit](https://github.com/mehrandvd/skunit)** - ⭐ 171
   skUnit is a testing tool for AI units, such as IChatClient, MCP Servers and agents.

1264. **[mcp-scholarly](https://github.com/adityak74/mcp-scholarly)** - ⭐ 171
   A MCP server to search for accurate academic articles.

1265. **[meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp)** - ⭐ 171
   A Model Context Protocol (MCP) server for interacting with Meilisearch through LLM interfaces.

1266. **[medusa](https://github.com/Pantheon-Security/medusa)** - ⭐ 171
   AI-first security scanner with 76 analyzers, 4,000+ detection rules, 508 FP filters (96.8% reduction), and 133 CVE detections for AI/ML, LLM agents, and MCP servers

1267. **[Text2Sql.Net](https://github.com/AIDotNet/Text2Sql.Net)** - ⭐ 170
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1268. **[docs](https://github.com/strands-agents/docs)** - ⭐ 170
   Documentation for the Strands Agents SDK. A model-driven approach to building AI agents in just a few lines of code. 

1269. **[photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server)** - ⭐ 170
   A Model Context Protocol (MCP) server that interfaces with Adobe Photoshop's Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands and context-aware interactions.

1270. **[y-gui](https://github.com/luohy15/y-gui)** - ⭐ 169
   A Tiny Web Chat App for AI Models with MCP Client Support

1271. **[keyboard-local](https://github.com/keyboard-dev/keyboard-local)** - ⭐ 169
   One MCP Server, All Your Apps, Privacy First

1272. **[mcp-use-ts](https://github.com/mcp-use/mcp-use-ts)** - ⭐ 169
   mcp-use is the framework for MCP with the best DX - Build AI agents, create MCP   servers with UI widgets, and debug with built-in inspector. Includes client SDK, server SDK, React hooks, and powerful dev tools.

1273. **[mcp-agent-langchainjs](https://github.com/Azure-Samples/mcp-agent-langchainjs)** - ⭐ 169
   Serverless AI agent using LangChain.js and Model Context Protocol (MCP) integration to order burgers from a burger restaurant

1274. **[lucid-agents](https://github.com/daydreamsai/lucid-agents)** - ⭐ 169
   Lucid Agents Commerce SDK. Bootstrap AI agents in 60 seconds that can pay, sell, and participate in agentic commerce supply chains. Our protocol agnostic SDK provides CLI-generated templates and drop-in adapters for Hono, Express, Next.js, and TanStack, giving you instant access to crypto/fiat payment rails (AP2, A2A, x402, ERC8004).

1275. **[Chanakya-Local-Friend](https://github.com/Rishabh-Bajpai/Chanakya-Local-Friend)** - ⭐ 169
   Chanakya is an advanced, open-source, and self-hostable voice assistant designed for privacy, power, and flexibility. It leverages local AI/ML models to ensure your data stays with you. It Integrates with 1000+ third-party MCP servers including Home Assistant. 

1276. **[opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)** - ⭐ 169
   Unified MCP server for querying OpenTelemetry traces across multiple backends (Jaeger, Tempo, Traceloop, etc.), enabling AI agents to analyze distributed traces for automated debugging and observability.

1277. **[mcp-shell-server](https://github.com/tumf/mcp-shell-server)** - ⭐ 169

1278. **[aleph](https://github.com/Hmbown/aleph)** - ⭐ 169
   Skill + MCP server to turn your agent into an RLM. Load context, iterate with search/code/think tools, converge on answers.

1279. **[kindly-web-search-mcp-server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)** - ⭐ 169
   Kindly Web Search MCP Server: Web search + robust content retrieval for AI coding tools (Claude Code, Codex, Cursor, GitHub Copilot, Gemini, etc.) and AI agents (Claude Desktop, OpenClaw, etc.). Supports Serper, Tavily, and SearXNG.

1280. **[mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** - ⭐ 169
   A Model Context Protocol (MCP) server that enables AI assistants to securely interact with Odoo ERP systems through standardized resources and tools for data retrieval and manipulation.

1281. **[mcp-access-point](https://github.com/sxhxliang/mcp-access-point)** - ⭐ 168
   Turn a web server into an MCP server in one click without making any code changes.

1282. **[mcp-telegram](https://github.com/sparfenyuk/mcp-telegram)** - ⭐ 168
   MCP server to work with Telegram through MTProto

1283. **[marionette_mcp](https://github.com/leancodepl/marionette_mcp)** - ⭐ 168
   MCP server enabling AI agents to interact with Flutter apps at runtime - let them inspect widgets, simulate taps, enter text, scroll, and take screenshots.

1284. **[lsp-mcp](https://github.com/jonrad/lsp-mcp)** - ⭐ 167
   An Model Context Protocol (MCP) server that provides LLMs/AI Agents with the capabilities of a language server protocol (LSP) server. This gives the AI the ability to get language aware context from the codebase.

1285. **[mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc)** - ⭐ 167
   A Model Context Protocol (MCP) server providing access to Google Search Console

1286. **[superset-mcp](https://github.com/aptro/superset-mcp)** - ⭐ 167
   connect to 50+ data stores via superset mcp server. Can use with open ai agent sdk, Claude app, cursor, windsurf

1287. **[obsidian-claude-code-mcp](https://github.com/iansinnott/obsidian-claude-code-mcp)** - ⭐ 167
   Connect Claude Code and other AI tools to your Obsidian notes using Model Context Protocol (MCP)

1288. **[Text2Sql.Net](https://github.com/shuyu-labs/Text2Sql.Net)** - ⭐ 166
   Text2Sql.Net 是一个使用DotNet和Semantic Kernel开发的Text2Sql工具

1289. **[toolbase](https://github.com/Toolbase-AI/toolbase)** - ⭐ 166
   A desktop application that adds powerful tools to Claude and AI platforms

1290. **[flights-mcp](https://github.com/ravinahp/flights-mcp)** - ⭐ 166
   An MCP server to search for flights.

1291. **[uLoopMCP](https://github.com/hatayama/uLoopMCP)** - ⭐ 166
   Your Unity project's AI autopilot. Compile, test, debug, repeat—until it just works.

1292. **[c4-genai-suite](https://github.com/codecentric/c4-genai-suite)** - ⭐ 165
   c4 GenAI Suite

1293. **[pg-mcp-server](https://github.com/ericzakariasson/pg-mcp-server)** - ⭐ 165
   MCP Server for Postgres

1294. **[tmcp](https://github.com/paoloricciuti/tmcp)** - ⭐ 165
   Typescript SDK to build MCP servers in an agnostic way

1295. **[gbox](https://github.com/babelcloud/gbox)** - ⭐ 164
   Cli and MCP for gbox. Enable AI agents to operate Android/Browser/Desktop like human.

1296. **[open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp)** - ⭐ 164
   An OpenStreetMap MCP server implementation that enhances LLM capabilities with location-based services and geospatial data.

1297. **[toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry)** - ⭐ 164
   MCPSDK.dev(ToolSDK.ai)'s Awesome MCP Servers and Packages Registry and Database with Structured JSON configurations. Supports OAuth2.1, DCR...

1298. **[MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server)** - ⭐ 164
   MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter)

1299. **[metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server)** - ⭐ 164
   Model Context Protocol (MCP) to enable AI LLMs to trade using MetaTrader platform

1300. **[jmap-mcp](https://github.com/wyattjoh/jmap-mcp)** - ⭐ 164
   A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.

1301. **[AutoRedTeam-Orchestrator](https://github.com/Coff0xc/AutoRedTeam-Orchestrator)** - ⭐ 164
   AI-Driven Automated Red Team Orchestration Framework | AI驱动的自动化红队编排框架 | 101 MCP Tools | 2000+ Payloads | Full ATT&CK Coverage | MCTS Attack Planner | Knowledge Graph | Cross-platform

1302. **[dify-mcp-client](https://github.com/3dify-project/dify-mcp-client)** - ⭐ 163
   MCP Client as an Agent Strategy Plugin. Support GUI operation via UI-TARS-SDK.

1303. **[gate22](https://github.com/aipotheosis-labs/gate22)** - ⭐ 163
   Open-source MCP gateway and control plane for teams to govern which tools agents can use, what they can do, and how it’s audited—across agentic IDEs like Cursor, or other agents and AI tools.

1304. **[cli-mcp-server](https://github.com/MladenSU/cli-mcp-server)** - ⭐ 163
   Command line interface for MCP clients with secure execution and customizable security policies

1305. **[UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP)** - ⭐ 163
   UnityNaturalMCP is an MCP server implementation for Unity that aims for a "natural" user experience.

1306. **[Companion](https://github.com/mattt/Companion)** - ⭐ 163
   Your neighborhood friendly MCP utility for macOS, iOS, and visionOS

1307. **[dbt-llm-agent](https://github.com/pragunbhutani/dbt-llm-agent)** - ⭐ 163
   LLM based AI Agent to automate Data Analysis for dbt projects with remote MCP server

1308. **[plane-mcp-server](https://github.com/makeplane/plane-mcp-server)** - ⭐ 163
   Plane's Official Model Context Protocol Server 🔌 ⌨️ 🔥

1309. **[strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server)** - ⭐ 163
   A Model Context Protocol (MCP) server that gives Claude direct control over Strudel.cc for AI-assisted music generation and live coding.

1310. **[SharpToolsMCP](https://github.com/kooshi/SharpToolsMCP)** - ⭐ 162
   A suite of MCP tools for AIs to analyze and modify C# solutions with high signal, Roslyn powered context.

1311. **[task-orchestrator](https://github.com/jpicklyk/task-orchestrator)** - ⭐ 162
   A light touch MCP task orchestration server for AI agents. Persistent work tracking and context storage across sessions and agents.  Defines planning floors through composable notes with optional gating transitions.   Coordinates multi-agent execution without prescribing how agents do their work.

1312. **[slack-mcp-client](https://github.com/tuannvm/slack-mcp-client)** - ⭐ 161
   A Slack bot and MCP client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

1313. **[MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** - ⭐ 161
   MCP Salesforce connector

1314. **[NornicDB](https://github.com/orneryd/NornicDB)** - ⭐ 161
   NornicDB is a high-performance graph + vector database built for AI agents and knowledge systems. It speaks Neo4j's (Bolt + Cypher) and qdrant's (gRPC) languages so you can use Nornic with zero code changes, while adding intelligent features including a graphql endpoint, air-gapped embeddings, GPU accelerated search, and other intelligent features.

1315. **[mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate)** - ⭐ 160
   MCP (Model Context Protocol) server for Weaviate

1316. **[zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server)** - ⭐ 160
   🔌 Complete MCP server for Zabbix integration - Connect AI assistants to Zabbix monitoring with 40+ tools for hosts, items, triggers, templates, problems, and more. Features read-only mode and comprehensive API coverage.

1317. **[mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition)** - ⭐ 160
   MCP server providing access to the comprehensive OpenNutrition food database with 300,000+ food items, nutritional data, and barcode lookups

1318. **[PolyMCP](https://github.com/poly-mcp/PolyMCP)** - ⭐ 159
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1319. **[recall](https://github.com/joseairosa/recall)** - ⭐ 159
   Persistent cross-session memory for Claude & AI agents. Self-host on Redis/Valkey, or use the managed SaaS at recallmcp.com.

1320. **[memory-graph](https://github.com/memory-graph/memory-graph)** - ⭐ 159
   A graph DB-based MCP memory server for coding agents with intelligent relationship tracking

1321. **[autocad-mcp](https://github.com/puran-water/autocad-mcp)** - ⭐ 159
   MCP server for AutoCAD LT v3.1: freehand AutoLISP execution, 8 consolidated tools, File IPC + ezdxf backends, focus-free dispatch, undo/redo, P&ID symbols, and robust IPC with ESC prefix and UTF-8 fallback. Companion agent skill: puran-water/autocad-drafting

1322. **[intervals-mcp-server](https://github.com/mvilanova/intervals-mcp-server)** - ⭐ 159
   Model Context Protocol (MCP) server for connecting Claude and ChatGPT with the Intervals.icu API.

1323. **[opencode-studio](https://github.com/Microck/opencode-studio)** - ⭐ 158
   web GUI for securely managing local OpenCode configuration

1324. **[Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)** - ⭐ 158
   A Model Context Protocol server for generating charts using QuickChart.io  . It allows you to create various types of charts through MCP tools.

1325. **[remote-mcp-server](https://github.com/gleanwork/remote-mcp-server)** - ⭐ 158
   Remote MCP Server that securely connects Enterprise context with your LLM, IDE, or agent platform of choice.

1326. **[compliant-llm](https://github.com/fiddlecube/compliant-llm)** - ⭐ 158
   Build Secure and Compliant AI agents and MCP Servers. YC W23

1327. **[mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)** - ⭐ 158
   MCP server for searching and querying PubMed medical papers/research database

1328. **[spotinfo](https://github.com/alexei-led/spotinfo)** - ⭐ 158
   CLI for exploring AWS EC2 Spot inventory. Inspect AWS Spot instance types, saving, price, and interruption frequency.

1329. **[awesome-claude-dxt](https://github.com/milisp/awesome-claude-dxt)** - ⭐ 158
   Awesome Claude Desktop Extensions (dxt) (not only Claude) mcpb

1330. **[mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)** - ⭐ 158
   Connects MCP to major 3D printer APIs (Orca, Bambu, OctoPrint, Klipper, Duet, Repetier, Prusa, Creality). Control prints, monitor status, and perform advanced STL operations like scaling, rotation, sectional editing, and base extension. Includes slicing and visualization.

1331. **[fetch-mcp](https://github.com/egoist/fetch-mcp)** - ⭐ 157
   An MCP server for fetching URLs / Youtube video transcript.

1332. **[mcp-client-slackbot](https://github.com/sooperset/mcp-client-slackbot)** - ⭐ 157
   Simple Slackbot MCP Client

1333. **[awesome-a2a](https://github.com/pab1it0/awesome-a2a)** - ⭐ 157
   Agent2Agent (A2A) – awesome A2A agents, tools, servers & clients, all in one place. 

1334. **[mcp-shark](https://github.com/mcp-shark/mcp-shark)** - ⭐ 157
   Wireshark-like forensic analysis for Model Context Protocol communications  Capture, inspect, and investigate all HTTP requests and responses between your IDE and MCP servers

1335. **[agentor](https://github.com/CelestoAI/agentor)** - ⭐ 157
   Fastest way to build and deploy reliable AI agents, MCP tools and  agent-to-agent. Deploy in a production ready serverless environment.

1336. **[mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse)** - ⭐ 156
   Model Context Protocol (MCP) Server for Langfuse Prompt Management. This server allows you to access and manage your Langfuse prompts through the Model Context Protocol.

1337. **[mcptools](https://github.com/posit-dev/mcptools)** - ⭐ 156
   Model Context Protocol For R

1338. **[scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server)** - ⭐ 156
   Scrapeless Mcp Server

1339. **[rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk)** - ⭐ 156
   A high-performance, asynchronous toolkit for building MCP servers and clients in Rust.

1340. **[alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server)** - ⭐ 155

1341. **[XPack-MCP-Marketplace](https://github.com/xpack-ai/XPack-MCP-Marketplace)** - ⭐ 155
   The world’s first open-source MCP monetization platform, to quickly create and sell your own MCP server in just minutes. | XPack 是全球首个开源 MCP 交易平台，帮助你在10分钟内快速搭建自己的 MCP 商店并立刻开始销售 MCP 服务。

1342. **[mcp-summarizer](https://github.com/0xshellming/mcp-summarizer)** - ⭐ 155
   MCP Server for AI Summarization

1343. **[mcp-dotnet-samples](https://github.com/microsoft/mcp-dotnet-samples)** - ⭐ 155
   A comprehensive set of samples of creating and using MCP servers and clients with .NET

1344. **[Frappe_Assistant_Core](https://github.com/buildswithpaul/Frappe_Assistant_Core)** - ⭐ 155
   Infrastructure that connects LLMs to ERPNext. Frappe Assistant Core works with the Model Context Protocol (MCP) to expose ERPNext functionality to any compatible Language Model

1345. **[ida-mcp-rs](https://github.com/blacktop/ida-mcp-rs)** - ⭐ 155
   Headless IDA Pro MCP Server

1346. **[dedalus-mcp-python](https://github.com/dedalus-labs/dedalus-mcp-python)** - ⭐ 154
   A simple and performant Model Context Protocol framework for Python.

1347. **[python-mcp-server-client](https://github.com/GobinFan/python-mcp-server-client)** - ⭐ 154
   支持查询主流agent框架技术文档的MCP server（支持stdio和sse两种传输协议）, 支持 langchain、llama-index、autogen、agno、openai-agents-sdk、mcp-doc、camel-ai 和 crew-ai

1348. **[code-assistant](https://github.com/stippi/code-assistant)** - ⭐ 154
   An LLM-powered, autonomous coding assistant. Also offers an MCP and ACP mode.

1349. **[osint-tools-mcp-server](https://github.com/frishtik/osint-tools-mcp-server)** - ⭐ 154
   MCP server exposing multiple OSINT tools for AI assistants like Claude

1350. **[mcp-solver](https://github.com/szeider/mcp-solver)** - ⭐ 154
   Model Context Protocol (MCP) server for constraint optimization and solving"

1351. **[radare2-mcp](https://github.com/radareorg/radare2-mcp)** - ⭐ 154
   MCP stdio server for radare2

1352. **[AgentCrew](https://github.com/saigontechnology/AgentCrew)** - ⭐ 154
   Chat application with multi-agents system supports multi-models and MCP

1353. **[google-slides-mcp](https://github.com/matteoantoci/google-slides-mcp)** - ⭐ 153
   MCP Server for Google Slides

1354. **[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server)** - ⭐ 153
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki, the spaced repetition flashcard application.

1355. **[idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)** - ⭐ 153
   MCP server that reality-checks your AI project idea against GitHub, Hacker News, npm, PyPI & Product Hunt. Returns a 0-100 reality signal.

1356. **[web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp)** - ⭐ 152
   Deep Research for crypto - free & fully local

1357. **[mcp-server-example](https://github.com/alejandro-ao/mcp-server-example)** - ⭐ 152
   A simple MCP server to search for documentation (tutorial)

1358. **[eShopLite](https://github.com/Azure-Samples/eShopLite)** - ⭐ 152
   eShopLite is a set of reference .NET applications implementing an eCommerce site with features like Semantic Search, MCP, Reasoning models and more.

1359. **[cursor-notebook-mcp](https://github.com/jbeno/cursor-notebook-mcp)** - ⭐ 152
   Model Context Protocol (MCP) server designed to allow AI agents within Cursor to interact with Jupyter Notebook (.ipynb) files

1360. **[make-mcp-server](https://github.com/integromat/make-mcp-server)** - ⭐ 152
   Make MCP Server

1361. **[In-Memoria](https://github.com/pi22by7/In-Memoria)** - ⭐ 152
   Persistent Intelligence Infrastructure for AI Agents

1362. **[chatgpt-copilot](https://github.com/feiskyer/chatgpt-copilot)** - ⭐ 152
   ChatGPT Copilot Extension for Visual Studio Code

1363. **[sunpeak](https://github.com/Sunpeak-AI/sunpeak)** - ⭐ 152
   Local-first MCP App framework for ChatGPT Apps, Claude, and more.

1364. **[mcp-gateway](https://github.com/lightconetech/mcp-gateway)** - ⭐ 151
   A gateway demo for MCP SSE Server

1365. **[mcp-server-metamcp](https://github.com/metatool-ai/mcp-server-metamcp)** - ⭐ 151
   MCP Server MetaMCP manages all your other MCPs in one MCP.

1366. **[mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server)** - ⭐ 151
   A Model Context Protocol server for MySQL database operations

1367. **[refref](https://github.com/refrefhq/refref)** - ⭐ 151
   🌟 Open Source Referral and Affiliate Marketing Platform - Launch your referral program in minutes!

1368. **[instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp)** - ⭐ 151
   Instagram Direct messages MCP

1369. **[solana-mcp](https://github.com/sendaifun/solana-mcp)** - ⭐ 151
   A Model Context Protocol server for interacting with the Solana blockchain, powered by the Solana Agent Kit (https://github.com/sendaifun/solana-agent-kit)

1370. **[mcp-client-go](https://github.com/yincongcyincong/mcp-client-go)** - ⭐ 150
   mcp client for Go (Golang). Integrate multiple  Model Context Protocol (MCP) servers

1371. **[GEmojiSharp](https://github.com/hlaueriksson/GEmojiSharp)** - ⭐ 150
   :octocat: GitHub Emoji for C#, dotnet and beyond

1372. **[Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP)** - ⭐ 150
   A Model Context Protocol (MCP) server that provides AI assistants access to AWS CloudWatch Logs for analysis, searching, and correlation

1373. **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** - ⭐ 150
   DataForSEO API modelcontextprotocol server 

1374. **[open-responses-server](https://github.com/teabranch/open-responses-server)** - ⭐ 150
   Wraps any OpenAI API interface as Responses with MCPs support so it supports Codex. Adding any missing stateful features. Ollama and Vllm compliant.

1375. **[logfire-mcp](https://github.com/pydantic/logfire-mcp)** - ⭐ 150
   The Logfire MCP Server is here! :tada:

1376. **[mcp-server-weread](https://github.com/ChenyqThu/mcp-server-weread)** - ⭐ 150

1377. **[memov](https://github.com/memovai/memov)** - ⭐ 150
   Give git-like & traceable memory to OpenClaw and any coding agents. By https://memov.ai/ aka Entire CLI for every coding agents by MCP.

1378. **[mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks)** - ⭐ 149
   StarRocks MCP (Model Context Protocol) Server

1379. **[relay](https://github.com/prism-php/relay)** - ⭐ 149
   An MCP client tool for Prism

1380. **[Express-REST-API-and-MCP-Server-Framework](https://github.com/iolufemi/Express-REST-API-and-MCP-Server-Framework)** - ⭐ 149
   Express REST API and MCP Server Framework is a comprehensive development framework for building RESTful APIs and MCP servers with Express.js. It provides a complete template for creating production-ready APIs using Node.js, Express, Mongoose (MongoDB), and Sequelize (SQL databases).

1381. **[CreatorBox](https://github.com/xiesx123/CreatorBox)** - ⭐ 149
   🚀🎬灵活、高效、可扩展，专属剪辑配音工具箱，释放创作潜力 . Flexible, efficient, and scalable toolbox for editing and dubbing, unleashing creative potential

1382. **[tinymcp](https://github.com/golioth/tinymcp)** - ⭐ 148
   Let LLMs control embedded devices via the Model Context Protocol.

1383. **[any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp)** - ⭐ 148
   MCP Server for using any LLM as a Tool

1384. **[website-downloader](https://github.com/pskill9/website-downloader)** - ⭐ 148
   MCP server to download entire websites

1385. **[agentql-mcp](https://github.com/tinyfish-io/agentql-mcp)** - ⭐ 148
   Model Context Protocol server that integrates AgentQL's data extraction capabilities.

1386. **[k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server)** - ⭐ 148
   Manage Your Kubernetes Cluster with k8s mcp-server

1387. **[seo-research-mcp](https://github.com/egebese/seo-research-mcp)** - ⭐ 148
   A free SEO research tool using Model Context Protocol (MCP) powered by Ahrefs data. Get backlink analysis, keyword research, traffic estimation, and more — directly in your AI-powered IDE.

1388. **[Axon.MCP.Server](https://github.com/ali-kamali/Axon.MCP.Server)** - ⭐ 148
   Transform your codebase into an intelligent knowledge base for AI-powered development with Cursor IDE, Google AntiGravity, and MCP-enabled assistants

1389. **[MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop)** - ⭐ 147
   Desktop APP for Discover and Install MCP Servers

1390. **[ultimate_mcp_client](https://github.com/Dicklesworthstone/ultimate_mcp_client)** - ⭐ 147
   Async Python client for the Model Context Protocol with interactive CLI and reactive Web UI, connecting AI models to MCP servers via stdio and SSE

1391. **[backlog-mcp-server](https://github.com/nulab/backlog-mcp-server)** - ⭐ 147

1392. **[hypertool-mcp](https://github.com/toolprint/hypertool-mcp)** - ⭐ 147
   Dynamically expose tools from proxied servers based on an Agent Persona

1393. **[ghost-mcp](https://github.com/MFYDev/ghost-mcp)** - ⭐ 147
   A Model Context Protocol (MCP) server for interacting with Ghost CMS through LLM interfaces like Claude. Allow you to control your Ghost blog by simply asking Claude etc.

1394. **[bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js)** - ⭐ 147
   Bilibili video search MCP (Model Context Protocol) service - 哔哩哔哩视频搜索MCP服务

1395. **[xiaoi](https://github.com/xvhuan/xiaoi)** - ⭐ 147
   小爱音箱语音通知工具：提供 CLI/TUI/MCP/Webhook 一键播报与控制音量，支持 PM2 常驻部署，支持docker部署。

1396. **[memorizer](https://github.com/petabridge/memorizer)** - ⭐ 147
   Vector-search powered agent memory MCP server

1397. **[decipher-research-agent](https://github.com/mtwn105/decipher-research-agent)** - ⭐ 146
   Turn topics, links, and files into AI-generated research notebooks — summarize, explore, and ask anything.

1398. **[figma-mcp-server](https://github.com/TimHolden/figma-mcp-server)** - ⭐ 146
   Model Context Protocol server implementation for Figma API

1399. **[freecad_mcp](https://github.com/bonninr/freecad_mcp)** - ⭐ 146
   FreecadMCP connects Freecad to Claude AI and other MCP-ready tools like Cursor through the Model Context Protocol (MCP), allowing Claude to directly interact with and control Freecad. This integration enables prompt assisted CAD 3d Design.

1400. **[mcp-discord](https://github.com/hanweg/mcp-discord)** - ⭐ 146
   MCP server for discord bot

1401. **[kom](https://github.com/weibaohui/kom)** - ⭐ 146
   kom 是一个用于 Kubernetes 操作的工具，SDK级的kubectl、client-go的使用封装。并且支持作为管理k8s 的 MCP server。 它提供了一系列功能来管理 Kubernetes 资源，包括创建、更新、删除和获取资源，甚至使用SQL查询k8s资源。这个项目支持多种 Kubernetes 资源类型的操作，并能够处理自定义资源定义（CRD）。 通过使用 kom，你可以轻松地进行资源的增删改查和日志获取以及操作POD内文件等动作。

1402. **[OmniFocus-MCP](https://github.com/themotionmachine/OmniFocus-MCP)** - ⭐ 146
   Let LLMs interface with your tasks and projects through the Model Context Protocol. Add, organize, and query your OmniFocus database with natural language commands.

1403. **[bocha-search-mcp](https://github.com/BochaAI/bocha-search-mcp)** - ⭐ 146
   Bocha Search MCP Server.

1404. **[goku](https://github.com/jcaromiq/goku)** - ⭐ 145
   Goku is an HTTP load testing application written in Rust 

1405. **[pubmearch](https://github.com/Darkroaster/pubmearch)** - ⭐ 145
   A PubMed MCP server.

1406. **[Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)** - ⭐ 145
   A powerful MCP Server that enables AI assistants like Claude to interact with humans through intuitive GUI dialogs. This server bridges the gap between automated AI processes and human decision-making by providing real-time user input tools, choices, confirmations, and feedback mechanisms.

1407. **[railway-mcp-server](https://github.com/railwayapp/railway-mcp-server)** - ⭐ 145
   Official Railway MCP Server for interacting with your Railway account

1408. **[quick-data-mcp](https://github.com/disler/quick-data-mcp)** - ⭐ 145
   Prompt focused MCP Server for .json and .csv agentic data analytics for Claude Code

1409. **[Gemini-mcp](https://github.com/LKbaba/Gemini-mcp)** - ⭐ 144
   MCP server implementation for Google's Gemini API

1410. **[postman-mcp-server](https://github.com/delano/postman-mcp-server)** - ⭐ 144
   An MCP server that provides access to Postman.

1411. **[uaip](https://github.com/concierge-hq/uaip)** - ⭐ 144
   Universal Agent Interactive Protocol (UAIP) is an open standard for ordered and verifiable interactions between autonomous services and AI agents.

1412. **[notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** - ⭐ 144
   **Notion MCP Server** is a Model Context Protocol (MCP) server implementation that enables AI assistants to interact with Notion's API. This production-ready server provides a complete set of tools.

1413. **[OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)** - ⭐ 144
   Connect any Open Data to any LLM with Model Context Protocol.

1414. **[node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)** - ⭐ 144
   A Node.js–based Model Context Protocol server that spins up disposable Docker containers to execute arbitrary JavaScript.

1415. **[aicode-toolkit](https://github.com/AgiFlow/aicode-toolkit)** - ⭐ 144
   Toolkit for Coding Agents to work reliably with repo of any size.

1416. **[eion](https://github.com/eiondb/eion)** - ⭐ 144
   Shared Memory Storage for Multi-Agent Systems

1417. **[mcp-interviewer](https://github.com/microsoft/mcp-interviewer)** - ⭐ 144
   Catch MCP server issues before your agents do.

1418. **[mcp-servers](https://github.com/charIesding/mcp-servers)** - ⭐ 143
   mcp server implementations

1419. **[frontmcp](https://github.com/agentfront/frontmcp)** - ⭐ 143
   TypeScript-first framework for the Model Context Protocol (MCP). You write clean, typed code; FrontMCP handles the protocol, transport, DI, session/auth, and execution flow.

1420. **[cachebro](https://github.com/glommer/cachebro)** - ⭐ 143
   File cache with diff tracking for AI coding agents. Drop-in MCP server that cuts token usage by 26%.

1421. **[codex-mcp-server](https://github.com/cexll/codex-mcp-server)** - ⭐ 143
   Codex Mcp Server 

1422. **[mcp-1panel](https://github.com/1Panel-dev/mcp-1panel)** - ⭐ 142
   mcp-1panel is an implementation of the Model Context Protocol (MCP) server for 1Panel.

1423. **[openagent](https://github.com/Th0rgal/openagent)** - ⭐ 142
   Self-hosted orchestrator for AI autonomous agents. Run Claude Code & Open Code in isolated linux workspaces. Manage your skills, configs and encrypted secrets with a git repo.

1424. **[wa_llm](https://github.com/ilanbenb/wa_llm)** - ⭐ 142
   A WhatsApp bot that can participate in group conversations, powered by AI. The bot monitors group messages and responds when mentioned.

1425. **[mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)** - ⭐ 142
   A Model Context Protocol server for calculating.

1426. **[powerpoint](https://github.com/supercurses/powerpoint)** - ⭐ 142
   A MCP Server for creating Powerpoint Presentations

1427. **[ReActMCP](https://github.com/mshojaei77/ReActMCP)** - ⭐ 141
   ReActMCP is a reactive MCP client that empowers AI assistants to instantly respond with real-time, Markdown-formatted web search insights powered by the Exa API.

1428. **[Polymcp](https://github.com/poly-mcp/Polymcp)** - ⭐ 141
   Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

1429. **[mcp-k8s](https://github.com/silenceper/mcp-k8s)** - ⭐ 141
   A Kubernetes MCP (Model Control Protocol) server that enables interaction with Kubernetes clusters through MCP tools.

1430. **[guidance-for-deploying-model-context-protocol-servers-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)** - ⭐ 141
   This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement industry-standard OAuth 2.0 authentication while protecting server deployments with multiple security layers, including content delivery networks and web application firewalls. 

1431. **[ollama-mcp](https://github.com/rawveg/ollama-mcp)** - ⭐ 141
   An MCP Server for Ollama

1432. **[mssql-mcp](https://github.com/Aaronontheweb/mssql-mcp)** - ⭐ 141
   MSSQL Server MCP implementation written in C#

1433. **[A2A-MCP-Server](https://github.com/GongRzhe/A2A-MCP-Server)** - ⭐ 140
   A mcp server that bridges the Model Context Protocol (MCP) with the Agent-to-Agent (A2A) protocol, enabling MCP-compatible AI assistants (like Claude) to seamlessly interact with A2A agents.

1434. **[mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** - ⭐ 140

1435. **[graphiti-mcp-server](https://github.com/gifflet/graphiti-mcp-server)** - ⭐ 140
   Graphiti MCP Server

1436. **[mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck)** - ⭐ 140
   An MCP server that acts as a bridge to query multiple OpenAI-compatible LLMs with MCP tool access. Just like rubber duck debugging, explain your problems to various AI "ducks" who can actually research and get different perspectives!

1437. **[claude-prompts](https://github.com/minipuft/claude-prompts)** - ⭐ 140
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1438. **[ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server)** - ⭐ 140
   Comprehensive MCP server exposing dozens of capabilities to AI agents: multi-provider LLM delegation, browser automation, document processing, vector ops, and cognitive memory systems

1439. **[mcp-server-manifest](https://github.com/Zomato/mcp-server-manifest)** - ⭐ 140

1440. **[freee-mcp](https://github.com/freee/freee-mcp)** - ⭐ 140
   Model Context Protocol (MCP) server for freee API integration

1441. **[systemprompt-code-orchestrator](https://github.com/systempromptio/systemprompt-code-orchestrator)** - ⭐ 139
     MCP server for orchestrating AI coding agents (Claude Code CLI & Gemini CLI). Features task management, process execution, Git integration, and dynamic resource discovery. Full TypeScript implementation with Docker support and Cloudflare Tunnel integration. 

1442. **[MCP-X](https://github.com/TimeCyber/MCP-X)** - ⭐ 139
   这是一个MCP客户端，让你轻松配置各个大模型，对接各种MCP Server而开发。This is an MCP client that allows you to easily configure various large models and develop interfaces with various MCP servers.

1443. **[agent-toolkit](https://github.com/datacommonsorg/agent-toolkit)** - ⭐ 139
   Tools and agents for interacting with the Data Commons Knowledge Graph using the Model Context Protocol (MCP).

1444. **[mcp-server-serper](https://github.com/marcopesani/mcp-server-serper)** - ⭐ 139
   Serper MCP Server supporting search and webpage scraping

1445. **[zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp)** - ⭐ 139
   A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, explore and synthesize atomic notes through Claude and other MCP-compatible clients.

1446. **[LMStudio-MCP](https://github.com/infinitimeless/LMStudio-MCP)** - ⭐ 139
   A Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via LM Studio.

1447. **[mcp-crash-course](https://github.com/emarco177/mcp-crash-course)** - ⭐ 139
   Hands-on crash course for the Model Context Protocol (MCP) with project-based branches on Streamable-HTTP, LangChain adapters, and Docker.

1448. **[gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp)** - ⭐ 139
   MCP Server that enables Claude code to interact with Gemini

1449. **[mcp-montano-server](https://github.com/lucasmontano/mcp-montano-server)** - ⭐ 138
   Simple MCP Server Implementation

1450. **[doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp)** - ⭐ 138
   MCP server for seamless document format conversion and processing

1451. **[SecureMCP](https://github.com/makalin/SecureMCP)** - ⭐ 138
   SecureMCP is a security auditing tool designed to detect vulnerabilities and misconfigurations in applications using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). It proactively identifies threats like OAuth token leakage, prompt injection vulnerabilities, rogue MCP servers, and tool poisoning attacks.

1452. **[datagov-mcp](https://github.com/aviveldan/datagov-mcp)** - ⭐ 138
   MCP server for Israel Government Data

1453. **[shopify-mcp](https://github.com/GeLi2001/shopify-mcp)** - ⭐ 138
   MCP server for Shopify api, usable on mcp hosts such as Claude and Cursor

1454. **[hayhooks](https://github.com/deepset-ai/hayhooks)** - ⭐ 137
   Easily deploy Haystack pipelines as REST APIs and MCP Tools.

1455. **[MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops)** - ⭐ 137
   🔍Professional MCP server for PostgreSQL operations & monitoring: 30+ extension-independent tools for performance analysis, table bloat detection, autovacuum monitoring, schema introspection, and database management. Supports PostgreSQL 12-17.

1456. **[seline](https://github.com/tercumantanumut/seline)** - ⭐ 137
   Seline is a local-first AI desktop application that brings together conversational AI, visual generation tools, vector search, and multi-channel connectivity in one place.

1457. **[ksail](https://github.com/devantler-tech/ksail)** - ⭐ 137
   Tool for creating, maintaining and operating Kubernetes clusters with ease.

1458. **[mcpd](https://github.com/mozilla-ai/mcpd)** - ⭐ 137
   Declaratively define and run required tools across environments, from local development to containerized cloud deployments.

1459. **[mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** - ⭐ 137

1460. **[codeql-mcp](https://github.com/JordyZomer/codeql-mcp)** - ⭐ 137
   This project runs a Model Context Protocol (MCP) server that wraps the CodeQL query server. It enables tools like [Cursor](https://cursor.sh/) or AI agents to interact with CodeQL through structured commands.

1461. **[pi-mcp-adapter](https://github.com/nicobailon/pi-mcp-adapter)** - ⭐ 137
   Token-efficient MCP adapter for Pi coding agent

1462. **[Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP)** - ⭐ 136
   mcp server for gitingest

1463. **[mcp-server-macos-use](https://github.com/mediar-ai/mcp-server-macos-use)** - ⭐ 136
   AI agent that controls computer with OS-level tools, MCP compatible, works with any model

1464. **[mcp-local-rag](https://github.com/shinpr/mcp-local-rag)** - ⭐ 136
   Local-first RAG server for developers using MCP. Semantic + keyword search for code and technical docs. Fully private, zero setup.

1465. **[claude-code-open](https://github.com/kill136/claude-code-open)** - ⭐ 136
   Open source AI coding platform with Web IDE, multi-agent system, 37+ tools, MCP protocol. MIT licensed.

1466. **[mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit)** - ⭐ 135
   A Model Context Protocol (MCP) server that provides tools for fetching Reddit content, including frontpage posts, subreddit information and hot posts, post details, and comments.

1467. **[esp-mcp](https://github.com/horw/esp-mcp)** - ⭐ 135
   Centralize ESP32 related commands and simplify getting started with seamless, LLM-driven interaction and help.

1468. **[computer-use-mcp](https://github.com/domdomegg/computer-use-mcp)** - ⭐ 135
   💻 Give AI models complete control of your computer (probably a bad idea)

1469. **[nextcloud-mcp-server](https://github.com/cbcoutinho/nextcloud-mcp-server)** - ⭐ 135
   Nextcloud MCP Server

1470. **[desktop](https://github.com/agentify-sh/desktop)** - ⭐ 135
   Agentify Desktop lets Codex/Claude/OpenCode  control your logged-in ChatGPT, Claude, AiStudio, Gemini, Grok, Perplexity web sessions via MCP, parallel hidden/visible tabs, file upload + image download

1471. **[vibing-steampunk](https://github.com/oisee/vibing-steampunk)** - ⭐ 135
   vs-punk: ADT to MCP bridge - Vibe code in ABAP / AMDP

1472. **[codemogger](https://github.com/glommer/codemogger)** - ⭐ 135
   Codemogger is a code indexing library and MCP server for AI coding agents

1473. **[mcp-think-tool](https://github.com/DannyMac180/mcp-think-tool)** - ⭐ 134
   An MCP server implementing the think tool for Claude

1474. **[jupyter-ai-agents](https://github.com/datalayer/jupyter-ai-agents)** - ⭐ 134
   🪐 🤖 AI Agents for JupyterLab with 🔧 MCP tools - Chat interface for optimized notebook interaction and code execution.

1475. **[mkinf](https://github.com/mkinf-io/mkinf)** - ⭐ 134
   mkinf SDK to interact with mkinf hub MCP servers

1476. **[xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server)** - ⭐ 134
   小红书MCP服务器 | 基于Electron+小红书Web API。一键安装运行、极速抓取笔记、评论、用户等数据并让AI智能分析、整理与导出

1477. **[mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast)** - ⭐ 134
   Quickly reads webpages and converts to markdown for fast, token efficient web scraping

1478. **[play-store-mcp](https://github.com/antoniolg/play-store-mcp)** - ⭐ 134
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1479. **[Multi-Source-Media-MCP-Server](https://github.com/Decade-qiu/Multi-Source-Media-MCP-Server)** - ⭐ 133
   An MCP Tool Implementation for Multi-Source Image Access & Generation

1480. **[mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server)** - ⭐ 133
   A Model Context Protocol (MCP) server that provides secure, read-only access to BigQuery datasets. Enables Large Language Models (LLMs) to safely query and analyze data through a standardized interface.

1481. **[mcp-chat](https://github.com/Flux159/mcp-chat)** - ⭐ 133
   Open Source Generic MCP Client for testing & evaluating mcp servers and agents

1482. **[Awesome-MCP](https://github.com/AlexMili/Awesome-MCP)** - ⭐ 133
   Awesome ModelContextProtocol resources - A curated list of MCP resources

1483. **[rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)** - ⭐ 133
   Blazing-fast, asynchronous MCP server for seamless filesystem operations.

1484. **[mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go)** - ⭐ 133
   Supercharge AI Agents, Safely

1485. **[zotero-mcp](https://github.com/kujenga/zotero-mcp)** - ⭐ 132
   Model Context Protocol (MCP) server for the Zotero API, in Python

1486. **[mcp-gateway](https://github.com/acehoss/mcp-gateway)** - ⭐ 132
   A flexible gateway server that bridges Model Context Protocol (MCP) STDIO servers to MCP HTTP+SSE and REST API, enabling multi-instance MCP servers to be exposed over HTTP.

1487. **[mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server)** - ⭐ 132
   MCP Server for Apache Spark History Server. The bridge between Agentic AI and Apache Spark.

1488. **[N8N2MCP](https://github.com/Super-Chain/N8N2MCP)** - ⭐ 132
   Convert N8N agent / workflow into MCP servers, you can use it in Claude / Cursor / Super Chain 

1489. **[zig-mcp](https://github.com/zig-wasm/zig-mcp)** - ⭐ 132
   Model Context Protocol (MCP) server that provides up-to-date documentation for the Zig programming language standard library and builtin functions

1490. **[unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp)** - ⭐ 132
   MCP server for Unreal Engine 5

1491. **[mcp-redmine](https://github.com/runekaagaard/mcp-redmine)** - ⭐ 132
   A redmine MCP server covering close to 100% of redmines API

1492. **[paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit)** - ⭐ 132
   Pragmatic AI Labs MCP Agent Toolkit - An MCP Server designed to make code with agents more deterministic

1493. **[tiktok-mcp](https://github.com/Seym0n/tiktok-mcp)** - ⭐ 132
   Model Context Protocol (MCP) with TikTok integration

1494. **[ChatPPT-MCP](https://github.com/YOOTeam/ChatPPT-MCP)** - ⭐ 132
   The AI-powered PPT generation service based on ChatPPT can create presentations based on themes, requirements, or uploaded documents, supporting online editing and downloading.基于chatppt进行的AI PPT生成服务，可以满足基于主题或者要求、以及上传文档进行生成ppt，以及美化换模板、修改配色字体等，支持在线编辑与下载。

1495. **[mcp_server_exe](https://github.com/shadowcz007/mcp_server_exe)** - ⭐ 132
   小智 & Cursor 的 MCP 启动器 - MCP For Cursor&xiaozhi。打包成可执行文件。Turn MCP server into an executable file

1496. **[mcp](https://github.com/MariaDB/mcp)** - ⭐ 132
   MariaDB MCP (Model Context Protocol) server implementation

1497. **[ragrabbit](https://github.com/madarco/ragrabbit)** - ⭐ 131
   Open Source, Self-Hosted, AI Search and LLM.txt for your website

1498. **[mcp-endpoint-server](https://github.com/xinnan-tech/mcp-endpoint-server)** - ⭐ 131
   xiaozhi mcp接入点服务器，用于自定义mcp服务注册，方便拓展小智服务端工具调用

1499. **[paperless-mcp](https://github.com/nloui/paperless-mcp)** - ⭐ 131
   An MCP (Model Context Protocol) server for interacting with a Paperless-NGX API server. This server provides tools for managing documents, tags, correspondents, and document types in your Paperless-NGX instance.

1500. **[crawl4ai-mcp-server](https://github.com/weidwonder/crawl4ai-mcp-server)** - ⭐ 130
   用于提供给本地开发者的 LLM的高效互联网搜索&内容获取的MCP Server， 节省你的token

1501. **[mcp-server](https://github.com/browserstack/mcp-server)** - ⭐ 130
   BrowserStack's Official MCP Server

1502. **[dify-plugin-agent-mcp_sse](https://github.com/junjiem/dify-plugin-agent-mcp_sse)** - ⭐ 130
   Dify 1.0 Plugin Support MCP Tools Agent strategies

1503. **[magg](https://github.com/sitbon/magg)** - ⭐ 130
   Magg: The MCP Aggregator

1504. **[mcp-linear](https://github.com/tacticlaunch/mcp-linear)** - ⭐ 130
   MCP server that enables AI assistants to interact with Linear project management system through natural language, allowing users to retrieve, create, and update issues, projects, and teams.

1505. **[mcp-todoist](https://github.com/greirson/mcp-todoist)** - ⭐ 130
   MCP server that connects Claude to Todoist for natural language task and project   management with bulk operations

1506. **[hevy-mcp](https://github.com/chrisdoc/hevy-mcp)** - ⭐ 130
   Manage your Hevy workouts, routines, folders, and exercise templates. Create and update sessions faster, organize plans, and search exercises to build workouts quickly. Stay synced with changes so your training log is always up to date.

1507. **[mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt)** - ⭐ 129
   High-performance CCXT MCP server for cryptocurrency exchange integration

1508. **[Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server)** - ⭐ 129
   AI-powered security operations for Wazuh SIEM—use any MCP-compatible client to ask security questions in plain English. Faster threat detection, incident triage, and compliance checks with real-time monitoring and anomaly spotting. Production-ready MCP server for conversational SOC workflows.

1509. **[beyond-mcp](https://github.com/disler/beyond-mcp)** - ⭐ 129
   It's time to push beyond MCP Servers... Right?

1510. **[isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)** - ⭐ 129
   Isaac Simulation MCP Extension and Server

1511. **[mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws)** - ⭐ 128
   A Model Context Protocol server implementation for operations on AWS resources

1512. **[ZotLink](https://github.com/TonybotNi/ZotLink)** - ⭐ 128
   Production‑ready MCP server for Zotero to save open preprints (arXiv, CVF, bio/med/chemRxiv) with rich metadata and smart PDF attachments — with upcoming support for publisher databases (Nature, Science, IEEE Xplore, Springer).

1513. **[mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1514. **[mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** - ⭐ 128
   Salesforce MCP Server

1515. **[mevzuat-mcp](https://github.com/saidsurucu/mevzuat-mcp)** - ⭐ 128
   MCP Server for Searching Turkish Legislation

1516. **[ClaudeR](https://github.com/IMNMV/ClaudeR)** - ⭐ 128
   Connect RStudio to Claude, Codex, Gemini, and other AI assistants via MCP. Multi-agent orchestration, async execution, and zero-config setup with uvx.

1517. **[CoWork-OS](https://github.com/CoWork-OS/CoWork-OS)** - ⭐ 128
   Operating System for your personal AI Agents with Security-first approach. Multi-channel (WhatsApp, Telegram, Discord, Slack, iMessage), multi-provider (Claude, GPT, Gemini, Ollama), fully self-hosted.

1518. **[mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** - ⭐ 128
   The implementation of Model Context Protocol (MCP) server for VictoriaMetrics

1519. **[mcp-bsl-platform-context](https://github.com/alkoleft/mcp-bsl-platform-context)** - ⭐ 128
   MCP сервер для AI-ассистентов (справка по синтаксису и объектной модели 1С:Предприятие)

1520. **[awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers)** - ⭐ 127
   A collection of crypto MCP servers.

1521. **[aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server)** - ⭐ 127
   MCP server for understanding AWS spend

1522. **[mcp-server-plugin](https://github.com/JetBrains/mcp-server-plugin)** - ⭐ 127
   JetBrains MCP Server Plugin

1523. **[laravel-loop](https://github.com/kirschbaum-development/laravel-loop)** - ⭐ 127
   Laravel Loop is a powerful Model Context Protocol (MCP) server designed specifically for Laravel applications. It connects your Laravel application with AI assistants using the MCP protocol.

1524. **[specs-workflow-mcp](https://github.com/kingkongshot/specs-workflow-mcp)** - ⭐ 127
   Intelligent spec workflow management MCP server

1525. **[dart-mcp-server](https://github.com/its-dart/dart-mcp-server)** - ⭐ 127
   Dart AI Model Context Protocol (MCP) server

1526. **[claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager)** - ⭐ 127
   GUI app to manage MCP servers for Claude Code

1527. **[FirstData](https://github.com/MLT-OSS/FirstData)** - ⭐ 127
   The World's Most Comprehensive, Authoritative, and Structured Open Source Data Source Knowledge Base

1528. **[hub-mcp](https://github.com/docker/hub-mcp)** - ⭐ 127
   Docker Hub MCP Server

1529. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** - ⭐ 127
   Devin's attempt at creating an OpenSCAD MCP Server that takes a user prompt and generates a preview image and 3d file.

1530. **[claude-prompts-mcp](https://github.com/minipuft/claude-prompts-mcp)** - ⭐ 126
   MCP prompt template server: hot-reload, thinking frameworks, quality gates

1531. **[mcp-devtools](https://github.com/sammcj/mcp-devtools)** - ⭐ 126
   A modular MCP server that provides commonly used developer tools for AI coding agents

1532. **[buttplug-mcp](https://github.com/ConAcademy/buttplug-mcp)** - ⭐ 126
   Buttplug.io Model Context Protocol (MCP) Server

1533. **[-mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter)** - ⭐ 126
      Convert any MCP server into a Claude Skill with 90% context savings

1534. **[awesome-x402](https://github.com/xpaysh/awesome-x402)** - ⭐ 126
   🚀 Curated list of x402 resources: HTTP 402 Payment Required protocol for blockchain payments, crypto micropayments, AI agents, API monetization. Includes SDKs (TypeScript, Python, Rust), examples, facilitators (Coinbase, Cloudflare), MCP integration, tutorials. Accept USDC payments with one line of code. Perfect for AI agent economy.

1535. **[think-mcp-server](https://github.com/PhillipRt/think-mcp-server)** - ⭐ 125

1536. **[play-store-mcp](https://github.com/devexpert-io/play-store-mcp)** - ⭐ 125
   An MCP server that connects to Play Store Console and release new App versions from an MCP Client

1537. **[mcp-evals](https://github.com/mclenhard/mcp-evals)** - ⭐ 125
   A Node.js package and GitHub Action for evaluating MCP (Model Context Protocol) tool implementations using LLM-based scoring. This helps ensure your MCP server's tools are working correctly and performing well.

1538. **[mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)** - ⭐ 125
   Example implementation of MCP Streamable HTTP client/server in Python and TypeScript.

1539. **[laravel-toon](https://github.com/mischasigtermans/laravel-toon)** - ⭐ 125
   TOON encoding for Laravel. Encode data for AI/LLMs with ~50% fewer tokens than JSON.

1540. **[raindrop-mcp](https://github.com/adeze/raindrop-mcp)** - ⭐ 125
   Raindrop MCP Server

1541. **[MakerAi](https://github.com/gustavoeenriquez/MakerAi)** - ⭐ 125
   The AI Operating System for Delphi. 100% native framework with RAG 2.0 for knowledge retrieval, autonomous agents with semantic memory, visual workflow orchestration, and universal LLM connector. Supports OpenAI, Claude, Gemini, Ollama, and more. Enterprise-grade AI for Delphi 10.3+

1542. **[meta_skill](https://github.com/Dicklesworthstone/meta_skill)** - ⭐ 124
   Local-first skill management platform for AI coding agents: dual SQLite+Git persistence, semantic search, bandit-optimized suggestions, and MCP integration

1543. **[mcp-client-server](https://github.com/willccbb/mcp-client-server)** - ⭐ 124
   An MCP Server that's also an MCP Client. Useful for letting Claude develop and test MCPs without needing to reset the application.

1544. **[mcp](https://github.com/pronskiy/mcp)** - ⭐ 124
   🐉 The fast, PHP way to build MCP servers

1545. **[aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook)** - ⭐ 124
   This repository provides a working, deployable, open source-based, serverless MCP server blueprint with an AWS Lambda function and AWS CDK Python code with all the best practices and a complete CI/CD pipeline.

1546. **[turbo-flow-claude](https://github.com/marcuspat/turbo-flow-claude)** - ⭐ 124
   Advanced Agentic Development Environment Supporting Devpods, Rackspace Spot Instances, Github Codespaces, Google Cloud Shell, and more!  Features 600+ AI agents, Claude Flow, SPARC methodology, and automatic context loading! Deploy intelligent multi-agent swarms, coordinate autonomous workflows.

1547. **[mcp-svelte-docs](https://github.com/spences10/mcp-svelte-docs)** - ⭐ 124
   🔍 MCP server that lets you search and access Svelte documentation with built-in caching

1548. **[UnityMCP](https://github.com/isuzu-shiranui/UnityMCP)** - ⭐ 124
   Unity Editor integration with Model Context Protocol (MCP) enabling AI assistants like Claude to interact with Unity projects. Features a TypeScript MCP server and C# Unity plugin with extensible command handler architecture, TCP/IP communication, and dynamic plugin discovery.

1549. **[apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server)** - ⭐ 124
   MCP server for querying Apple Health data with natural language using DuckDB under the hood.

1550. **[linear-mcp](https://github.com/cline/linear-mcp)** - ⭐ 124
   a private MCP server for accessing Linear

1551. **[ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended)** - ⭐ 124
   Ableton Live MCP (Model Context Protocol) server that allows control directly through AI assistants.

1552. **[mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery)** - ⭐ 123
   A Model Context Protocol server that provides access to BigQuery

1553. **[mcp-glootie](https://github.com/AnEntrypoint/mcp-glootie)** - ⭐ 123
   wanna develop an app ❓

1554. **[cloudflare-mcp](https://github.com/mattzcarey/cloudflare-mcp)** - ⭐ 123
   unofficial mcp server for cloudflare api

1555. **[mcp-watch](https://github.com/kapilduraphe/mcp-watch)** - ⭐ 123
   A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.

1556. **[openapi](https://github.com/samchon/openapi)** - ⭐ 123
   OpenAPI definitions, converters and LLM function calling schema composer.

1557. **[mcp-server](https://github.com/bitwarden/mcp-server)** - ⭐ 123
   MCP server for interaction with Bitwarden.

1558. **[memorix](https://github.com/AVIDS2/memorix)** - ⭐ 123
   Cross-Agent Memory Bridge  Persistent memory for AI coding agents across Cursor, Windsurf, Claude Code, Codex, Copilot, Kiro via MCP. Never re-explain your project again.

1559. **[mcp-gm](https://github.com/AnEntrypoint/mcp-gm)** - ⭐ 122
   wanna develop an app ❓

1560. **[mcp-memory](https://github.com/Puliczek/mcp-memory)** - ⭐ 122
   🔥🖥️ MCP Memory is a MCP Server that gives MCP Clients (Cursor, Claude, Windsurf and more) the ability to remember information about users (preferences, behaviors) across conversations.

1561. **[aseprite-mcp](https://github.com/diivi/aseprite-mcp)** - ⭐ 122
   MCP server for interacting with the Aseprite API

1562. **[pentest-mcp](https://github.com/DMontgomery40/pentest-mcp)** - ⭐ 122
   NOT for educational purposes: An MCP server for professional penetration testers including STDIO/HTTP/SSE support, nmap, go/dirbuster, nikto, JtR, hashcat, wordlist building, and more.

1563. **[MCP-Workspace-Server](https://github.com/answerlink/MCP-Workspace-Server)** - ⭐ 122
   🚀 Beyond Filesystem - Complete AI Development Environment - One MCP Server provides full Agent capability stack: web development, code execution, data processing, image generation. No need for multiple tools, configure once. Perfect support for Dify, FastGPT, Cherry Studio.       文件操作、Python/Node.js 代码执行、Web 应用一键部署（支持泛域名）、Excel 处理、图像生成。开箱即用

1564. **[nanobanana-mcp-server](https://github.com/zhongweili/nanobanana-mcp-server)** - ⭐ 122

1565. **[akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp)** - ⭐ 122
   MCP server that provides access to Chinese stock market data using akshare-one

1566. **[mcp-server-asana](https://github.com/roychri/mcp-server-asana)** - ⭐ 121

1567. **[muppet](https://github.com/muppet-dev/muppet)** - ⭐ 121
   MCP Servers SDK for TypeScript

1568. **[easy-code-reader](https://github.com/FangYuan33/easy-code-reader)** - ⭐ 121
   A powerful MCP (Model Context Protocol) server for intelligently reading Java source code.

1569. **[ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp)** - ⭐ 121
   Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback,clip, overlay, concat and other functions

1570. **[n8n-mcp-server](https://github.com/illuminaresolutions/n8n-mcp-server)** - ⭐ 121
   MCP server implementation for n8n workflow automation

1571. **[remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)** - ⭐ 121
   This is a quickstart template to easily build and deploy a custom remote MCP server to the cloud using Azure functions. You can clone/restore/run on your local machine with debugging, and `azd up` to have it in the cloud in a couple minutes.  The MCP server is secured by design using 

1572. **[pipelock](https://github.com/luckyPipewrench/pipelock)** - ⭐ 121
   Firewall for AI agents. DLP scanning, SSRF protection, bidirectional MCP scanning, tool poisoning detection, and workspace integrity monitoring.

1573. **[google-workspace-mcp](https://github.com/aaronsb/google-workspace-mcp)** - ⭐ 120
   A Model Context Protocol (MCP) server that provides authenticated access to Google Workspace APIs, offering integrated Authentication, Gmail, Calendar, and Drive functionality

1574. **[mcp-package-version](https://github.com/sammcj/mcp-package-version)** - ⭐ 120
   An MCP server that provides LLMs with the latest stable package versions when coding

1575. **[ffmpeg-mcp](https://github.com/egoist/ffmpeg-mcp)** - ⭐ 120
   An MCP server for FFmpeg

1576. **[jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp)** - ⭐ 120
   A Model Context Protocol (MCP) for Jupyter Notebook

1577. **[google-sheets-mcp](https://github.com/mkummer225/google-sheets-mcp)** - ⭐ 120
   Google Sheets MCP Server 📊🤖

1578. **[SwiftMCP](https://github.com/Cocoanetics/SwiftMCP)** - ⭐ 120
   Model Context Protocol Server for Swift

1579. **[netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server)** - ⭐ 120
   Model Context Protocol (MCP) server for read-only interaction with NetBox data in LLMs

1580. **[exstruct](https://github.com/harumiWeb/exstruct)** - ⭐ 120
   Conversion from Excel to structured JSON (tables, shapes, charts) for LLM/RAG pipelines, and autonomous Excel reading and writing by AI agents through MCP integration.

1581. **[teslamate-mcp](https://github.com/cobanov/teslamate-mcp)** - ⭐ 119
   A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.

1582. **[elevenlabs-mcp-server](https://github.com/mamertofabian/elevenlabs-mcp-server)** - ⭐ 119

1583. **[portainer-mcp](https://github.com/portainer/portainer-mcp)** - ⭐ 119
   Portainer MCP server

1584. **[comet-mcp](https://github.com/hanzili/comet-mcp)** - ⭐ 119
   MCP Server connecting to Perplexity Comet browser

1585. **[swiftlens](https://github.com/swiftlens/swiftlens)** - ⭐ 119
   SwiftLens is a Model Context Protocol (MCP) server that provides deep, semantic-level analysis of Swift codebases to any AI models. By integrating directly with Apple's SourceKit-LSP, SwiftLens enables AI models to understand Swift code with compiler-grade accuracy.

1586. **[Financial-Modeling-Prep-MCP-Server](https://github.com/imbenrabi/Financial-Modeling-Prep-MCP-Server)** - ⭐ 119
   A Model Context Protocol (MCP) implementation for Financial Modeling Prep, enabling AI assistants to access and analyze financial data, stock information, company fundamentals, and market insights.

1587. **[iphone-mcp](https://github.com/Lakr233/iphone-mcp)** - ⭐ 119
   A Model Context Protocol (MCP) server for automating iPhone tasks with Appium. Supports app control, UI interactions, and screenshot capture via streamable HTTP.

1588. **[memorizer-v1](https://github.com/petabridge/memorizer-v1)** - ⭐ 118
   Vector-search powered agent memory MCP server

1589. **[mcp-mianshiya-server](https://github.com/yuyuanweb/mcp-mianshiya-server)** - ⭐ 118
   基于 Spring AI 的面试鸭搜索题目的 MCP Server 服务，快速让 AI 搜索企业面试真题和答案

1590. **[Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)** - ⭐ 118
   这个项目是一个基于Model Context Protocol (MCP)的AutoCAD集成服务器，它允许通过自然语言与AutoCAD进行交互。通过这个服务器，用户可以使用Claude等大型语言模型来创建、修改和分析AutoCAD图纸，同时还可以存储和查询CAD元素的相关数据。目前制作参考学习，仅实现端到端之间的通信，具体工具函数尚未晚上

1591. **[polymarket-mcp](https://github.com/berlinbra/polymarket-mcp)** - ⭐ 118
   MCP Server for PolyMarket API

1592. **[typst-mcp](https://github.com/johannesbrandenburger/typst-mcp)** - ⭐ 118
   Typst MCP Server is an MCP (Model Context Protocol) implementation that helps AI models interact with Typst, a markup-based typesetting system. The server provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.

1593. **[xcodeproj-mcp-server](https://github.com/giginet/xcodeproj-mcp-server)** - ⭐ 118
   A Model Context Protocol Server to manipulate *.xcodeproj

1594. **[VisionCraft-MCP-Server](https://github.com/augmentedstartups/VisionCraft-MCP-Server)** - ⭐ 117
   VisionCraft MCP delivers up-to-date, specialized computer vision and Gen-AI knowledge directly to Claude and other AI assistants.

1595. **[mcp-ts-template](https://github.com/cyanheads/mcp-ts-template)** - ⭐ 117
   TypeScript template for building Model Context Protocol (MCP) servers. Ships with declarative tools/resources, pluggable auth, multi-backend storage, OpenTelemetry observability, and first-class support for both local and edge (Cloudflare Workers) runtimes.

1596. **[web-scout-mcp](https://github.com/pinkpixel-dev/web-scout-mcp)** - ⭐ 117
   A powerful MCP server extension providing web search and content extraction capabilities. Integrates DuckDuckGo search functionality and URL content extraction into your MCP environment, enabling AI assistants to search the web and extract webpage content programmatically.

1597. **[mcp-server](https://github.com/InterviewReady/mcp-server)** - ⭐ 117
   An MCP server for InterviewReady

1598. **[aks-mcp](https://github.com/Azure/aks-mcp)** - ⭐ 117
   A Model Context Protocol (MCP) server that enables AI assistants to interact with AKS clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and AKS.

1599. **[Hegelion](https://github.com/Hmbown/Hegelion)** - ⭐ 117
   Dialectical reasoning architecture for LLMs (Thesis → Antithesis → Synthesis)

1600. **[computer-control-mcp](https://github.com/AB498/computer-control-mcp)** - ⭐ 117
   MCP server that provides computer control capabilities, like mouse, keyboard, OCR, etc. using PyAutoGUI, RapidOCR, ONNXRuntime. Similar to 'computer-use' by Anthropic. With Zero External Dependencies.

1601. **[mcp-reticle](https://github.com/soth-ai/mcp-reticle)** - ⭐ 116
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1602. **[mcp_proxy_rust](https://github.com/tidewave-ai/mcp_proxy_rust)** - ⭐ 116
   A proxy to use HTTP/SSE MCPs from STDIO clients

1603. **[mcp-hubspot](https://github.com/peakmojo/mcp-hubspot)** - ⭐ 116
   A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while improving response times.

1604. **[mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket)** - ⭐ 116
   Node.js/TypeScript MCP server for Atlassian Bitbucket. Enables AI systems (LLMs) to interact with workspaces, repositories, and pull requests via tools (list, get, comment, search). Connects AI directly to version control workflows through the standard MCP interface.

1605. **[context-sync](https://github.com/Intina47/context-sync)** - ⭐ 116
   Local persistent memory store for LLM applications including continue.dev, cursor, claude desktop, github copilot, codex, antigravity, etc.

1606. **[ASI](https://github.com/vNeeL-code/ASI)** - ⭐ 116
   Android ✧ Gemma Integration into Android System Intelligence

1607. **[kodit](https://github.com/helixml/kodit)** - ⭐ 116
   👩‍💻 MCP server to index external repositories

1608. **[MCppServer](https://github.com/Noeli14/MCppServer)** - ⭐ 115
   Fast and super efficient Minecraft Server written in C++

1609. **[remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)** - ⭐ 115
   Azure API Management as AI Gateway to Remote MCP servers.

1610. **[oracle-mcp-server](https://github.com/danielmeppiel/oracle-mcp-server)** - ⭐ 115
   MCP Server for working with large Oracle databases

1611. **[narsil-mcp](https://github.com/postrv/narsil-mcp)** - ⭐ 115
   Rust MCP server for comprehensive code intelligence - 90 tools, 32 languages, security scanning, call graphs, and more

1612. **[x64dbgMCP](https://github.com/Wasdubya/x64dbgMCP)** - ⭐ 115
   Model Context Protocol for x64dbg & x32dbg

1613. **[server-google-news](https://github.com/ChanMeng666/server-google-news)** - ⭐ 114
   【Star-crossed coders unite!⭐️】Model Context Protocol (MCP) server implementation providing Google News search capabilities via SerpAPI, with automatic news categorization and multi-language support.

1614. **[swagger-mcp](https://github.com/dcolley/swagger-mcp)** - ⭐ 114
   Swagger to MCP server

1615. **[env-doctor](https://github.com/mitulgarg/env-doctor)** - ⭐ 114
   Debug your GPU, CUDA, and AI stacks across local, Docker, and CI/CD (CLI and MCP server)

1616. **[remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python)** - ⭐ 114
   Getting Started with Remote MCP Servers using Azure Functions (Python)

1617. **[toolhive-studio](https://github.com/stacklok/toolhive-studio)** - ⭐ 114
   ToolHive is an application that allows you to install, manage and run MCP servers and connect them to AI agents

1618. **[mcp-probe](https://github.com/conikeec/mcp-probe)** - ⭐ 114
   A Model Context Protocol (MCP) client library and debugging toolkit in Rust. This foundation provides both a production-ready SDK for building MCP integrations and the core architecture for an interactive debugger.

1619. **[mcp-local-rag](https://github.com/nkapila6/mcp-local-rag)** - ⭐ 114
   "primitive" RAG-like web search model context protocol (MCP) server that runs locally. ✨ no APIs ✨

1620. **[mcp](https://github.com/frappe/mcp)** - ⭐ 114
   Frappe MCP allows Frappe apps to function as MCP servers

1621. **[falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)** - ⭐ 114
   Connect AI agents to CrowdStrike Falcon for automated security analysis and threat hunting

1622. **[Dex](https://github.com/davekilleen/Dex)** - ⭐ 114
   Your AI Chief of Staff — a personal operating system starter kit that adapts to your role. No coding required.

1623. **[cli](https://github.com/mcpgod/cli)** - ⭐ 113
   Fine-grained control over model context protocol (MCP) clients, servers, and tools. Context is God.

1624. **[MCP-oura](https://github.com/YuzeHao2023/MCP-oura)** - ⭐ 113
   MCP server for Oura API integration

1625. **[foxy-contexts](https://github.com/strowk/foxy-contexts)** - ⭐ 113
   Foxy contexts is a library for building context servers supporting Model Context Protocol

1626. **[UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration)** - ⭐ 113
   Enable AI Agents to Control Unity

1627. **[mcp-toolkit](https://github.com/nuxt-modules/mcp-toolkit)** - ⭐ 113
   Create MCP servers directly in your Nuxt application. Define tools, resources, and prompts with a simple and intuitive API.

1628. **[notion-mcp](https://github.com/ccabanillas/notion-mcp)** - ⭐ 113
   A Model Context Protocol (MCP) server implementation for Notion integration, providing a standardized interface for interacting with Notion's API.

1629. **[diagram-mcp-server](https://github.com/andrewmoshu/diagram-mcp-server)** - ⭐ 113
   An MCP server that seamlessly creates infrastructure diagrams for AWS, Azure, GCP, Kubernetes and more

1630. **[crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp)** - ⭐ 112
   An MCP server providing a range of cryptocurrency technical analysis indicators and strategies.

1631. **[MCP2Lambda](https://github.com/danilop/MCP2Lambda)** - ⭐ 112
   Run any AWS Lambda function as a Large Language Model (LLM) tool without code changes using Anthropic's Model Context Protocol (MCP).

1632. **[punkpeye_awesome-mcp-servers](https://github.com/MCP-Mirror/punkpeye_awesome-mcp-servers)** - ⭐ 112
   Mirror of https://github.com/punkpeye/awesome-mcp-servers

1633. **[mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp)** - ⭐ 112
   MCP server for Mikrotik

1634. **[gis-mcp](https://github.com/mahdin75/gis-mcp)** - ⭐ 112
   A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform geospatial operations and transformations.

1635. **[pocketbase-mcp](https://github.com/mrwyndham/pocketbase-mcp)** - ⭐ 112
   MCP server for building PocketBase apps really quickly - Need a front end quick consider FastPocket

1636. **[design-systems-mcp](https://github.com/southleft/design-systems-mcp)** - ⭐ 112
   I'm your specialized design systems assistant. Ask me about components, tokens, patterns, and best practices.

1637. **[Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP](https://github.com/newideas99/Deepseek-Thinking-Claude-3.5-Sonnet-CLINE-MCP)** - ⭐ 111
   🧠 MCP server implementing RAT (Retrieval Augmented Thinking) - combines DeepSeek's reasoning with GPT-4/Claude/Mistral responses, maintaining conversation context between interactions.

1638. **[MCP-searxng](https://github.com/SecretiveShell/MCP-searxng)** - ⭐ 111
   MCP server for connecting agentic systems to search systems via searXNG

1639. **[spring-documentation-mcp-server](https://github.com/andrlange/spring-documentation-mcp-server)** - ⭐ 111
   Spring Boot based MCP Server provide full Spring Ecosystem Documentation for LLMs

1640. **[vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server)** - ⭐ 111
   Expose VSCode features such as file viewing and editing as MCP, enabling advanced AI-assisted coding directly from tools like Claude Desktop

1641. **[mcp-checkpoint](https://github.com/aira-security/mcp-checkpoint)** - ⭐ 111
   MCP Checkpoint continuously secures and monitors Model Context Protocol operations through static and dynamic scans, revealing hidden risks in agent-to-tool communications.

1642. **[mcpauth](https://github.com/mcpauth/mcpauth)** - ⭐ 111
   Authentication for MCP Servers

1643. **[gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server)** - ⭐ 111

1644. **[gRPC-zig](https://github.com/ziglana/gRPC-zig)** - ⭐ 111
   blazigly fast gRPC/MCP client & server implementation in zig

1645. **[mcp.science](https://github.com/pathintegral-institute/mcp.science)** - ⭐ 111
   Open Source MCP Servers for Scientific Research

1646. **[mcp-jfrog](https://github.com/jfrog/mcp-jfrog)** - ⭐ 111
   Model Context Protocol (MCP) Server for the JFrog Platform API, enabling repository management, build tracking, release lifecycle management, and more.

1647. **[Taiwan-Health-MCP](https://github.com/healthymind-tech/Taiwan-Health-MCP)** - ⭐ 111

1648. **[ATaC](https://github.com/ATaC-team/ATaC)** - ⭐ 111
   Recording and Replay AI Agent Trajectory.

1649. **[livebook_tools](https://github.com/thmsmlr/livebook_tools)** - ⭐ 110
   Powertools for livebook.dev — AI Code Editing, MCP Servers, and Running Livebooks from the CLI

1650. **[dash-mcp-server](https://github.com/Kapeli/dash-mcp-server)** - ⭐ 110
   MCP server for Dash, the macOS documentation browser

1651. **[code-pathfinder](https://github.com/shivasurya/code-pathfinder)** - ⭐ 110
   AI-Native Static Code Analysis for modern security teams. Built for finding vulnerabilities, advanced structural search, derive insights and supports MCP

1652. **[augments-mcp-server](https://github.com/augmnt/augments-mcp-server)** - ⭐ 110
   Comprehensive MCP server providing real-time framework documentation access for Claude Code with intelligent caching, multi-source integration, and context-aware assistance.

1653. **[ai-command](https://github.com/mcp-wp/ai-command)** - ⭐ 110
   Control WordPress using WP-CLI, AI, and MCP.

1654. **[DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)** - ⭐ 110
   Official DINO-X Model Context Protocol (MCP) server that empowers LLMs with real-world visual perception through image object detection, localization, and captioning APIs.

1655. **[modex](https://github.com/theronic/modex)** - ⭐ 110
   Modex is a Clojure MCP Library to augment your AI models with Tools, Resources & Prompts using Clojure (Model Context Protocol). Implements MCP Server & Client.

1656. **[template-repo](https://github.com/AndrewAltimit/template-repo)** - ⭐ 110
   Agent orchestration & security template featuring MCP tool building, agent2agent workflows, mechanistic interpretability on sleeper agents, and agent integration via CLI wrappers

1657. **[outline-mcp-server](https://github.com/mmmeff/outline-mcp-server)** - ⭐ 110
   It's an MCP server... for Outline (the documentation platform!)

1658. **[server-wp-mcp](https://github.com/emzimmer/server-wp-mcp)** - ⭐ 109

1659. **[game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp)** - ⭐ 109
   An MCP server for creating 2D/3D game assets from text using Hugging Face AI models.

1660. **[apple-rag-mcp](https://github.com/BingoWon/apple-rag-mcp)** - ⭐ 109
    MCP server providing AI agents with instant access to Apple developer documentation via RAG technology

1661. **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** - ⭐ 109
   A Model Context Protocol (MCP) server for querying the VirusTotal API.

1662. **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** - ⭐ 109
   MCP server for querying the Shodan API

1663. **[mcp](https://github.com/taskade/mcp)** - ⭐ 109
   🤖 Taskade MCP · Official MCP server and OpenAPI to MCP codegen. Build AI agent tools from any OpenAPI API and connect to Claude, Cursor, and more.

1664. **[google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp)** - ⭐ 109
   The Google Ads MCP Server is an implementation of the Model Context Protocol (MCP) that enables Large Language Models (LLMs), such as Gemini, to interact directly with the Google Ads API.

1665. **[google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server)** - ⭐ 109
   MCP server for Google Tag Manager

1666. **[idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform)** - ⭐ 109
   🟪 Open source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service. Supports: AG-UI, CopilotKit API, OpenTelemetry, MCP, memory, guardrails, SSO, RBAC.

1667. **[SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)** - ⭐ 108
   Universal database MCP server connecting to MySQL, PostgreSQL, SQL Server, MariaDB,DM8,Oracle,not only provides basic database connection such as OAuth 2.0 authentication , health checks, SQL optimization, and index health detection

1668. **[share-best-mcp](https://github.com/shareAI-lab/share-best-mcp)** - ⭐ 108
   世界上最好的MCP Servers的列表,The best mcp servers in the world.

1669. **[minesweeper-mcp-server](https://github.com/tonypan2/minesweeper-mcp-server)** - ⭐ 108
   An MCP server for playing Minesweeper

1670. **[mcp_client](https://github.com/theailanguage/mcp_client)** - ⭐ 108
   MCP Client Implementation using Python, LangGraph and Gemini

1671. **[asyncmcp](https://github.com/bh-rat/asyncmcp)** - ⭐ 108
   Async transport layers for MCP

1672. **[mcp-client](https://github.com/punkpeye/mcp-client)** - ⭐ 108
   An MCP client for Node.js.

1673. **[neurolink](https://github.com/juspay/neurolink)** - ⭐ 108
   Universal AI Development Platform with MCP server integration, multi-provider support, and professional CLI. Build, test, and deploy AI applications with multiple ai providers.

1674. **[browser-debugger-cli](https://github.com/szymdzum/browser-debugger-cli)** - ⭐ 108
   CLI tool for agents to quickly access browser telemetry (DOM, network, console) via Chrome DevTools Protocol.

1675. **[kibitz](https://github.com/nick1udwig/kibitz)** - ⭐ 107
   The coding agent for professionals

1676. **[slack-mcp-server](https://github.com/ubie-oss/slack-mcp-server)** - ⭐ 107
   A Slack MCP server

1677. **[selfhosted-supabase-mcp](https://github.com/HenkDz/selfhosted-supabase-mcp)** - ⭐ 107
   An MCP Server for your Self Hosted Supabase

1678. **[mcp-tool-kit](https://github.com/getfounded/mcp-tool-kit)** - ⭐ 107
   Agentic abstraction layer for building high precision vertical AI agents written in python for Model Context Protocol.

1679. **[payloadcmsmcp](https://github.com/disruption-hub/payloadcmsmcp)** - ⭐ 107
   Payload CMS MCP Server

1680. **[sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp)** - ⭐ 107
   MCP for semantic code search & navigation that reduces token waste

1681. **[mcp-prompts](https://github.com/sparesparrow/mcp-prompts)** - ⭐ 107
   Model Context Protocol server for managing, storing, and providing prompts and prompt templates for LLM interactions. 

1682. **[UnrealClaude](https://github.com/Natfii/UnrealClaude)** - ⭐ 107
   Claude Code CLI integration for Unreal Engine 5.7 - Get AI coding assistance with built-in UE5.7 documentation context directly in the editor.

1683. **[sap-skills](https://github.com/secondsky/sap-skills)** - ⭐ 107
   Production-ready Claude Code skills for SAP development - 35 skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more

1684. **[IntelliConnect](https://github.com/ruanrongman/IntelliConnect)** - ⭐ 106
   本项目为xiaozhi-esp32提供后端服务  |  A Powerful AI agent IoT platform core.

1685. **[csharp-runner](https://github.com/sdcb/csharp-runner)** - ⭐ 106
   fast, secure c# runner

1686. **[mcpm](https://github.com/MCP-Club/mcpm)** - ⭐ 106
   A command-line tool for managing MCP servers in Claude App. Also can run a MCP Server to help you manage all your MCP Servers

1687. **[arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp)** - ⭐ 106
   MCP server that uses arxiv-to-prompt to fetch and process arXiv LaTeX sources for precise interpretation of mathematical expressions in scientific papers.

1688. **[esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)** - ⭐ 106
   This repository consists of Source Code for Model Context Protocol (MCP) Pilot Project being undertaken by Ministry of Statistics and Programme Implementation and source code for the same is being shared under GNU General Public License.

1689. **[snippy](https://github.com/Azure-Samples/snippy)** - ⭐ 105
   🧩 Build AI-powered MCP Tools with Azure Functions, Durable Agents & Cosmos vector search. Features orchestrated multi-agent workflows using OpenAI.

1690. **[Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP)** - ⭐ 105
   A Model Context Protocol (MCP) server that enables AI assistants to securely access and analyze Microsoft Fabric Analytics data through authenticated API calls.

1691. **[flowlens-mcp-server](https://github.com/magentic/flowlens-mcp-server)** - ⭐ 105
   FlowLens is an open-source MCP server that gives your coding agent (Claude Code, Cursor, Copilot, Codex) full browser context for in-depth debugging and regression testing.

1692. **[typescript-utcp](https://github.com/universal-tool-calling-protocol/typescript-utcp)** - ⭐ 105
   Official typescript implementation of UTCP. UTCP is an open standard that lets AI agents call any API directly, without extra middleware.

1693. **[ZipAgent](https://github.com/JiayuXu0/ZipAgent)** - ⭐ 105
   轻量级AI Agent框架，让你5分钟构建专属智能助手。Lightweight AI Agent framework. Build your AI assistant in 5 minutes.

1694. **[GenesisCore](https://github.com/AIGODLIKE/GenesisCore)** - ⭐ 105
   One click installation! BlenderMCP tool that supports DeepSeek, Claude, and others, fully integrated into Blender!

1695. **[rust-docs-mcp](https://github.com/snowmead/rust-docs-mcp)** - ⭐ 105
   MCP server for agents to explore rust docs, analyze source code, and build with confidence

1696. **[yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)** - ⭐ 105

1697. **[awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering)** - ⭐ 105
   A curated list of awesome open-source libraries for context engineering (Long-term memory, MCP: Model Context Protocol, Prompt/RAG Compression, Multi-Agent)

1698. **[linggen-memory](https://github.com/linggen/linggen-memory)** - ⭐ 105
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1699. **[gtasks-mcp](https://github.com/zcaceres/gtasks-mcp)** - ⭐ 105
   A Google Tasks Model Context Protocol Server for Claude

1700. **[AgenticGoKit](https://github.com/AgenticGoKit/AgenticGoKit)** - ⭐ 105
   Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent agents. LLM-agnostic, event-driven, with multi-agent workflows, MCP tool discovery, and production-grade observability.

1701. **[agentcare-mcp](https://github.com/Kartha-AI/agentcare-mcp)** - ⭐ 104
   MCP Server for EMRs with FHIR

1702. **[freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp)** - ⭐ 104
   An MCP server that integrates with the Freqtrade cryptocurrency trading bot.

1703. **[linggen](https://github.com/linggen/linggen)** - ⭐ 104
   A local-first memory layer for AI (Cursor, Zed, Claude). Persistent architectural context via semantic search.

1704. **[a2a-mcp-tutorial](https://github.com/Tsadoq/a2a-mcp-tutorial)** - ⭐ 104
   A tutorial on how to use Model Context Protocol by Anthropic and Agent2Agent Protocol by Google

1705. **[MiniMax-MCP-JS](https://github.com/MiniMax-AI/MiniMax-MCP-JS)** - ⭐ 104
   Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.

1706. **[academic-search-mcp-server](https://github.com/afrise/academic-search-mcp-server)** - ⭐ 104
   Academic Paper Search MCP Server for Claude Desktop integration. Allows Claude to access data from Semantic Scholar and Crossref. 

1707. **[chat.md](https://github.com/rusiaaman/chat.md)** - ⭐ 104
   An md file as a chat interface and editable history in one.

1708. **[JavaSinkTracer_MCP](https://github.com/Zacarx/JavaSinkTracer_MCP)** - ⭐ 104
   基于函数级污点分析的 Java 源代码漏洞审计工具JavaSinkTracer，通过 Model Context Protocol (MCP) 为 AI 助手提供安全分析能力。

1709. **[flexible-graphrag](https://github.com/stevereiner/flexible-graphrag)** - ⭐ 104
   Flexible GraphRAG: Python, LlamaIndex, Docker Compose: 8 Graph dbs, 10 Vector dbs, OpenSearch, Elasticsearch, Alfresco. 13 data sources (9 auto-sync), KG auto-building, schemas, LLMs, Docling or LlamaParse doc processing, GraphRAG, RAG only, Hybrid search, AI chat. React, Vue, Angular frontends, FastAPI backend, REST API, MCP Server. Please 🌟 Star

1710. **[Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)** - ⭐ 104
   A Nano Banana MCP server, which you can integrate to cursor/claude code and any mcp client

1711. **[smileyCoin](https://github.com/fefergrgrgrg/smileyCoin)** - ⭐ 103
   simple web ui to manage mcp (model context protocol) servers in the claude app

1712. **[memory-bank-MCP](https://github.com/tuncer-byte/memory-bank-MCP)** - ⭐ 103
   Memory Bank is an MCP server that helps teams create, manage, and access structured project documentation. It generates and maintains a set of interconnected Markdown documents that capture different aspects of project knowledge, from high-level goals to technical details and day-to-day progress.

1713. **[solana-mcp](https://github.com/solanamcp/solana-mcp)** - ⭐ 103
   Solana Agent Kit MCP Server 

1714. **[ARIES](https://github.com/Chieko-Seren/ARIES)** - ⭐ 103
   顺便一提，我们支持 RWKV | 「Intel 2025 人工智能创新大赛」🚀AutoOPS: Provide the chaos brought by language models to the operation and maintenance industry! 🏆使用 LLM 提供的动力实现全自动运维，支持 Windows Server/Linux/macOS/Cisco IOS，可进行全网自动管理，让我们颠覆运维行业【带外管理/自动运维/IoT设备管理/WebHook监控/任意平台/全模态Workflow】

1715. **[http-oauth-mcp-server](https://github.com/NapthaAI/http-oauth-mcp-server)** - ⭐ 103
   Remote MCP server (SEE + Streamable HTTP) implementing the MCP spec's authorization extension. Use directly from your agents, or from Cursor / Claude with mcp-remote

1716. **[chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp)** - ⭐ 103
   MCP Server for Chronulus AI Forecasting and Prediction Agents

1717. **[memory-mcp-server](https://github.com/okooo5km/memory-mcp-server)** - ⭐ 103
   A Model Context Protocol server that provides knowledge graph management capabilities. 

1718. **[mcp-server](https://github.com/webflow/mcp-server)** - ⭐ 103
   Model Context Protocol (MCP) server for the Webflow Data API.

1719. **[sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)** - ⭐ 103
   An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.

1720. **[erickwendel-contributions-mcp](https://github.com/ErickWendel/erickwendel-contributions-mcp)** - ⭐ 103
   A Model Context Protocol (MCP) server that provides tools to query Erick Wendel's contributions across different platforms

1721. **[alibabacloud-ack-mcp-server](https://github.com/aliyun/alibabacloud-ack-mcp-server)** - ⭐ 103
   Alibaba Cloud's ack-mcp-server unifies container operations capabilities, enabling AI assistants and third-party AI agents to perform complex tasks via natural language through the MCP protocol, empowering container-native AIOps. DingTalk discussion group:  70080006301

1722. **[alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** - ⭐ 103
   AlibabaCloud CloudOps MCP Server

1723. **[mcp-outline](https://github.com/Vortiago/mcp-outline)** - ⭐ 103
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Outline documentation services.

1724. **[comfy-pilot](https://github.com/ConstantineB6/comfy-pilot)** - ⭐ 103
   MCP server + embedded terminal that lets Claude Code see and edit your ComfyUI workflows

1725. **[Matryoshka](https://github.com/yogthos/Matryoshka)** - ⭐ 103
   MCP server for token-efficient large document analysis via the use of REPL state

1726. **[mcp](https://github.com/cloudflare/mcp)** - ⭐ 103
   MCP server for the Cloudflare API

1727. **[vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)** - ⭐ 102
   Official Vectorize MCP Server

1728. **[remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions)** - ⭐ 102
   Landing page for Remote MCP Server efforts in Azure Functions with links to all language stack specific repos.

1729. **[deep-code-reasoning-mcp](https://github.com/haasonsaas/deep-code-reasoning-mcp)** - ⭐ 102
   A Model Context Protocol (MCP) server that provides advanced code analysis and reasoning capabilities powered by Google's Gemini AI

1730. **[godoc-mcp](https://github.com/mrjoshuak/godoc-mcp)** - ⭐ 102
   go doc mcp server

1731. **[gemini-desktop](https://github.com/kkrishnan90/gemini-desktop)** - ⭐ 101
   The MCP Gemini Electron App is a cross-platform desktop application that creates a seamless chat interface for Google's Gemini AI models with extensible capabilities through a Model Context Protocol (MCP) framework.

1732. **[btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server)** - ⭐ 101
   BTP CloudFoundry Node.js MCP server for SAP OData services integration

1733. **[powerbi-mcp](https://github.com/sulaiman013/powerbi-mcp)** - ⭐ 101
   MCP server for natural language interaction with Power BI datasets

1734. **[mcp-windows-desktop-automation](https://github.com/mario-andreschak/mcp-windows-desktop-automation)** - ⭐ 101
   A Model Context Protocol (MCP) server for Windows desktop automation using AutoIt.

1735. **[mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast)** - ⭐ 101
   Quickly screenshots webpages and converts to an LLM friendly size

1736. **[shodh-memory](https://github.com/varun29ankuS/shodh-memory)** - ⭐ 101
   Cognitive brain for Claude, AI agents & edge devices — learns with use, runs offline, single binary. Neuroscience-grounded 3-tier architecture with Hebbian learning.

1737. **[EDT-MCP](https://github.com/DitriXNew/EDT-MCP)** - ⭐ 101
   MCP for 1C:EDT

1738. **[paper-search-mcp-nodejs](https://github.com/Dianel555/paper-search-mcp-nodejs)** - ⭐ 101
   A Node.js implementation of the Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including **Web of Science**, arXiv, and more.

1739. **[claude-code-mcp-enhanced](https://github.com/grahama1970/claude-code-mcp-enhanced)** - ⭐ 100
   Enhanced Claude Code MCP server with orchestration capabilities, reliability improvements, and self-contained execution patterns

1740. **[mcp-hono-stateless](https://github.com/mhart/mcp-hono-stateless)** - ⭐ 100
   An example Hono MCP server using Streamable HTTP

1741. **[AgentBoard](https://github.com/igrigorik/AgentBoard)** - ⭐ 100
   A switchboard for AI in your browser: wire in any model, script WebMCP tools, connect remote MCP servers, bring your commands.

1742. **[autodev-codebase](https://github.com/anrgct/autodev-codebase)** - ⭐ 100
   A vector embedding-based code semantic search tool with MCP server and multi-model integration. Can be used as a pure CLI tool. Supports Ollama for fully local embedding and reranking, enabling complete offline operation and privacy protection for your code repository

1743. **[complete-intro-to-mcp](https://github.com/btholt/complete-intro-to-mcp)** - ⭐ 100
   The Complete Intro to MCP Servers, as taught for Frontend Masters by Brian Holt

1744. **[sample-agentic-ai-demos](https://github.com/aws-samples/sample-agentic-ai-demos)** - ⭐ 100
   Collection of examples of how to use Model Context Protocol with AWS.

1745. **[mcp-client-nodejs](https://github.com/ConardLi/mcp-client-nodejs)** - ⭐ 100
   Node.js Client Implementation for Model Context Protocol (MCP)

1746. **[go-utcp](https://github.com/universal-tool-calling-protocol/go-utcp)** - ⭐ 100
    Official Go implementation of the UTCP 

1747. **[github-stars](https://github.com/miantiao-me/github-stars)** - ⭐ 100
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1748. **[awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** - ⭐ 100
   A curated list of awesome MCP (Model Context Protocol) tools, platforms, and services for enterprises.

1749. **[brave-search-mcp](https://github.com/mikechao/brave-search-mcp)** - ⭐ 100
   An MCP Server implementation that integrates the Brave Search API, providing, Web Search, Local Points of Interest Search, Image Search, Video Search and News Search capabilities

1750. **[next-mcp-server](https://github.com/vertile-ai/next-mcp-server)** - ⭐ 99
   Help LLMs to understand your Next apps better

1751. **[turbular](https://github.com/raeudigerRaeffi/turbular)** - ⭐ 99
   A MCP server allowing LLM agents to easily connect and retrieve data from any database

1752. **[pywss](https://github.com/czasg/pywss)** - ⭐ 99
   一个轻量级的 Python Web 框架，一站式集成 MCP SSE、StreamHTTP 和 MCPO 协议，助你轻松构建MCP Server🔥

1753. **[mighty-security](https://github.com/NineSunsInc/mighty-security)** - ⭐ 99
   Don't Simply Trust MCP Server Code, Validate and Scan

1754. **[terminal-controller-mcp](https://github.com/GongRzhe/terminal-controller-mcp)** - ⭐ 99
   A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface.

1755. **[lapras-mcp-server](https://github.com/lapras-inc/lapras-mcp-server)** - ⭐ 99
   lapras.com 公式MCP Server

1756. **[wanaku](https://github.com/wanaku-ai/wanaku)** - ⭐ 99
   Wanaku MCP Router

1757. **[heimdall-mcp-server](https://github.com/lcbcFoo/heimdall-mcp-server)** - ⭐ 99
   Your AI Coding Assistant's Long-Term Memory

1758. **[mysql-mcp-server-sse](https://github.com/mangooer/mysql-mcp-server-sse)** - ⭐ 99
   MySQL query server based on the MCP sse.Multi-level SQL risk control & injection protection Docker support for quick deployment

1759. **[octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server)** - ⭐ 99
   A free MCP server to analyze and extract insights from public filings, earnings transcripts, financial metrics, stock market data, private market transactions, and deep web-based research within Claude Desktop and other popular MCP clients.

1760. **[FNewsCrawler](https://github.com/noimank/FNewsCrawler)** - ⭐ 99
   一个专门为大模型设计的财经信息MCP（Model Context Protocol）服务，通过高效的爬虫技术从各大财经网站（同花顺、东方财富等）获取实时资讯，为AI模型提供准确、及时的财经数据支持。

1761. **[forge-orchestrator](https://github.com/nxtg-ai/forge-orchestrator)** - ⭐ 99
   Forge Orchestrator: Multi-AI task coordination. File locking, knowledge capture, drift detection. Rust.

1762. **[mpm-vibe-coding](https://github.com/halflifezyf2680/mpm-vibe-coding)** - ⭐ 99
   MPM is an MCP context-engineering layer for Vibe Coding, focused on three delivery bottlenecks: context loss, uncontrolled changes, and non-verifiable outcomes.

1763. **[mcp-graphiti](https://github.com/rawr-ai/mcp-graphiti)** - ⭐ 99
   Graphiti Model Context Protocol (MCP) Server - An MCP server for knowledge graph management via Graphiti

1764. **[perfetto-mcp](https://github.com/antarikshc/perfetto-mcp)** - ⭐ 99
   This is a Model Context Protocol (MCP) server that gets answers from your Perfetto Traces. It turns natural‑language prompts into focused Perfetto analyses.

1765. **[forgemax](https://github.com/postrv/forgemax)** - ⭐ 99
   Code Mode inspired local sandboxed MCP Gateway — collapses N servers x M tools into 2 tools (~1,000 tokens)

1766. **[atomic-red-team-mcp](https://github.com/cyberbuff/atomic-red-team-mcp)** - ⭐ 98
   MCP server for Atomic Red Team

1767. **[mcp-typescript-sdk](https://github.com/emqx/mcp-typescript-sdk)** - ⭐ 98
   A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js environments.

1768. **[all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol)** - ⭐ 98
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows

1769. **[langgraph-ai](https://github.com/piyushagni5/langgraph-ai)** - ⭐ 98
   LangGraph AI Repository

1770. **[editor-mcp-server](https://github.com/playcanvas/editor-mcp-server)** - ⭐ 98
   MCP Server for AI automation of the PlayCanvas Editor

1771. **[systemprompt-mcp-server](https://github.com/systempromptio/systemprompt-mcp-server)** - ⭐ 98
   A complete, production-ready implementation of a Model Context Protocol (MCP) server demonstrating OAuth 2.1, tools, prompts, resources, sampling, and notifications using Reddit as a real-world integration example.

1772. **[Vibe-Coder-MCP](https://github.com/freshtechbro/Vibe-Coder-MCP)** - ⭐ 98
    Vibe-Coder-MCP server extends AI assistants with specialized software development tools.

1773. **[xclaude-plugin](https://github.com/conorluddy/xclaude-plugin)** - ⭐ 98
   iOS development ClaudeCode plugin for mindful token and context usage. Contains modular MCPs that group various Xcode/IDB tools based on your current workflow.

1774. **[mcp_on_ruby](https://github.com/rubyonai/mcp_on_ruby)** - ⭐ 97
   💎 A Ruby implementation of the Model Context Protocol

1775. **[mcp-sse-demo](https://github.com/cnych/mcp-sse-demo)** - ⭐ 97
   claude mcp sse demo with server and client(cli、web)

1776. **[sandbox-mcp](https://github.com/pottekkat/sandbox-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) server that enables LLMs to run ANY code safely in isolated Docker containers.

1777. **[openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp)** - ⭐ 97
   A Model Context Protocol (MCP) tool server for OpenAI's GPT-4o/gpt-image-1 image generation and editing APIs.

1778. **[claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes)** - ⭐ 97
   Claude Desktop extension with bundled MCP Server for Bear note taking app

1779. **[bitbucket-mcp](https://github.com/MatanYemini/bitbucket-mcp)** - ⭐ 97
   Bitbucket MCP - A Model Context Protocol (MCP) server for integrating with Bitbucket Cloud and Server APIs

1780. **[finance-trading-ai-agents-mcp](https://github.com/aitrados/finance-trading-ai-agents-mcp)** - ⭐ 96
   A comprehensive, free MCP server designed specifically for financial analysis and quantitative trading. This specialized platform offers one-click local deployment with a sophisticated department-based architecture that mirrors real financial company operations.

1781. **[gemini-mcp-desktop-client](https://github.com/duke7able/gemini-mcp-desktop-client)** - ⭐ 96
   first gemini based desktop client for MCP

1782. **[searxng-mul-mcp](https://github.com/jae-jae/searxng-mul-mcp)** - ⭐ 96
   A Model Context Protocol (MCP) server for SearXNG search engine with multi-query parallel search support

1783. **[mcp-kit](https://github.com/my-mcp-hub/mcp-kit)** - ⭐ 96
   A CLI tool to create MCP (Model Context Protocol) applications with ease.

1784. **[api2mcp4j](https://github.com/TheEterna/api2mcp4j)** - ⭐ 96
   This is a revolutionary AI MCP plugin with excellent pluggable and encapsulated features. With just a few lines of configuration, it can easily integrate into your Spring boot web program and give it MCP capabilities,inheriting the powerful engineering capabilities of the Spring series framework

1785. **[opencv-mcp-server](https://github.com/GongRzhe/opencv-mcp-server)** - ⭐ 96
   OpenCV MCP Server  provides OpenCV's image and video processing capabilities through the Model Context Protocol (MCP). Access powerful computer vision tools for tasks ranging from basic image manipulation to advanced object detection and tracking.

1786. **[gossiphs](https://github.com/williamfzc/gossiphs)** - ⭐ 96
   "Zero setup" & "Blazingly fast" general code file relationship analysis. With Python & Rust. Based on tree-sitter and git analysis. Support MCP and ready for AI🤖

1787. **[ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer)** - ⭐ 96
   The Gemini CLI confirmed that the MCP server built with Google Apps Script (GAS), a low-code platform, offers immense possibilities. If you've created snippets for GAS, these could be revitalized and/or leveraged in new ways by using them as the MCP server. The Gemini CLI and other MCP clients will be useful in achieving this.

1788. **[IB_MCP](https://github.com/rcontesti/IB_MCP)** - ⭐ 96
   This project provides an Interactive Brokers (IB) API interface using the Model Context Protocol (MCP).

1789. **[sparql-llm](https://github.com/sib-swiss/sparql-llm)** - ⭐ 96
   🦜✨ Chat system, MCP server, and reusable components to improve LLMs capabilities when generating SPARQL queries

1790. **[zed-mcp-server-context7](https://github.com/akbxr/zed-mcp-server-context7)** - ⭐ 96
   Context7 MCP Server for Zed

1791. **[mcp-memory-keeper](https://github.com/mkreyman/mcp-memory-keeper)** - ⭐ 96
   MCP server for persistent context management in AI coding assistants

1792. **[needle-mcp](https://github.com/needle-ai/needle-mcp)** - ⭐ 96
   Needle MCP Server for easy RAG.Long-term memory for LLMs.

1793. **[fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)** - ⭐ 96
   FHIR MCP Server – helping you expose any FHIR Server or API as a MCP Server.

1794. **[a2ajava](https://github.com/vishalmysore/a2ajava)** - ⭐ 95
   Pure java implementation of Google A2A protocol. Integrate your spring boot java applications with A2A protocol , includes client and sever both. Any agent built with a2ajava will also be exposed as MCP tool automatically

1795. **[z-image-studio](https://github.com/iconben/z-image-studio)** - ⭐ 95
   A Cli, a webUI, and a MCP server for the Z-Image-Turbo text-to-image generation model (Tongyi-MAI/Z-Image-Turbo base model as well as quantized models)

1796. **[nowledge-mem](https://github.com/nowledge-co/nowledge-mem)** - ⭐ 95
   Memory and context manager just works.

1797. **[spring-ai-playground](https://github.com/spring-ai-community/spring-ai-playground)** - ⭐ 95
   Spring AI Playground is a self-hosted web UI for low-code AI tool development with live MCP server registration. It includes MCP server inspection, agentic chat, and integrated LLM and RAG workflows, enabling real-time experimentation and evolution of tool-enabled AI systems without redeployment.

1798. **[bouvet](https://github.com/vrn21/bouvet)** - ⭐ 94
   Sandbox for Agents 

1799. **[semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)** - ⭐ 94
   A FastMCP server implementation for the Semantic Scholar API, providing comprehensive access to academic paper data, author information, and citation networks.

1800. **[ruby-mcp-client](https://github.com/simonx1/ruby-mcp-client)** - ⭐ 94
   This is a Ruby implementation of MCP (Model Context Protocol) client

1801. **[model-context-protocol-mcp-hands-on-with-agentic-ai-2034200](https://github.com/LinkedInLearning/model-context-protocol-mcp-hands-on-with-agentic-ai-2034200)** - ⭐ 94
   This is a code repository for the LinkedIn Learning course Model Context Protocol (MCP): Hands-On with Agentic AI [ASI] [TEXT] [MODELS]

1802. **[mcp-server-idapro](https://github.com/fdrechsler/mcp-server-idapro)** - ⭐ 94
   A Model Context Protocol (MCP) server that enables AI assistants to interact with IDA Pro for reverse engineering and binary analysis tasks.

1803. **[healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)** - ⭐ 94
   A Model Context Protocol (MCP) server providing AI assistants with access to healthcare data and medical information tools, including FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM metadata, and a medical calculator.

1804. **[schedcp](https://github.com/eunomia-bpf/schedcp)** - ⭐ 93
   MCP Server for Linux Scheduler Management and Auto optimization

1805. **[infobus-mcp](https://github.com/simovilab/infobus-mcp)** - ⭐ 93
   Model Context Protocol server enabling AI assistants to access transit information through standardized interfaces

1806. **[elektron-mcp](https://github.com/zerubeus/elektron-mcp)** - ⭐ 93
   MCP sever for controlling Elektron devices using LLMs

1807. **[MasterMCP](https://github.com/slowmist/MasterMCP)** - ⭐ 93
   A demonstration toolkit revealing potential security vulnerabilities in MCP (Model Context Protocol) frameworks through data poisoning, JSON injection, function overriding, and cross-MCP call attacks, exposing AI security issues while providing defense recommendations. For educational and research purposes only.

1808. **[mcp-replicate](https://github.com/deepfates/mcp-replicate)** - ⭐ 93
   Model Context Protocol server for Replicate's API

1809. **[gospy](https://github.com/monsterxx03/gospy)** - ⭐ 93
   Non-Invasive goroutine inspector

1810. **[pluggedin-app](https://github.com/VeriTeknik/pluggedin-app)** - ⭐ 93
   The Crossroads for AI Data Exchanges. A unified, self-hostable web interface for discovering, configuring, and managing Model Context Protocol (MCP) servers—bringing together AI tools, workspaces, prompts, and logs from multiple MCP sources (Claude, Cursor, etc.) under one roof.

1811. **[leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)** - ⭐ 93
   An MCP server enabling automated access to LeetCode's problems, solutions, and public data with optional authentication for user-specific features, supporting leetcode.com & leetcode.cn sites.

1812. **[mcp-trino](https://github.com/tuannvm/mcp-trino)** - ⭐ 93
   A high-performance Model Context Protocol (MCP) server for Trino implemented in Go.

1813. **[AgentUp](https://github.com/always-further/AgentUp)** - ⭐ 93
   Portable , scalable , secure AI Agents

1814. **[mcp-server](https://github.com/OctopusDeploy/mcp-server)** - ⭐ 92
   Octopus Deploy Official MCP Server

1815. **[open-mcp-auth-proxy](https://github.com/wso2/open-mcp-auth-proxy)** - ⭐ 92
   Authentication and Authorization Proxy for MCP Servers

1816. **[splunk-mcp](https://github.com/livehybrid/splunk-mcp)** - ⭐ 92
   A Model Context Protocol (MCP) implementation for Splunk Enterprise and Cloud integration with Cursor IDE or Claude

1817. **[mcpcat-typescript-sdk](https://github.com/MCPCat/mcpcat-typescript-sdk)** - ⭐ 92
   MCPcat is an analytics platform for MCP server owners 🐱.

1818. **[deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server)** - ⭐ 92
   A Model Context Protocol (MCP) server that provides translation capabilities using the DeepL API.

1819. **[square-mcp-server](https://github.com/square/square-mcp-server)** - ⭐ 92
   A Model Context Protocol (MCP) server for square

1820. **[tiger-cli](https://github.com/timescale/tiger-cli)** - ⭐ 92
   Tiger CLI is the command-line interface for Tiger Cloud. It includes an MCP server for helping coding agents write production-level Postgres code.

1821. **[action_mcp](https://github.com/seuros/action_mcp)** - ⭐ 92
   Rails Engine with MCP compliant Spec.

1822. **[actual-mcp](https://github.com/s-stefanov/actual-mcp)** - ⭐ 92
   Model Context Protocol for Actual Budget API

1823. **[awesome-mcp-servers-devops](https://github.com/WagnerAgent/awesome-mcp-servers-devops)** - ⭐ 92
   A curated, DevOps-focused list of Model Context Protocol (MCP) servers—covering source control, IaC, Kubernetes, CI/CD, cloud, observability, security, and collaboration—with a bias toward maintained, production-ready integrations.

1824. **[loki-mcp](https://github.com/grafana/loki-mcp)** - ⭐ 92
   An MCP ( Model Context Protocol ) Server for Grafana Loki

1825. **[anubis-mcp](https://github.com/zoedsoupe/anubis-mcp)** - ⭐ 92
   Elixir Model Context Protocol (MCP) SDK (hermes-mcp fork)

1826. **[litegraph](https://github.com/litegraphdb/litegraph)** - ⭐ 91
   Lightweight graph database with relational, vector, and MCP support, designed to power knowledge and artificial intelligence persistence and retrieval.

1827. **[vibe](https://github.com/michiosw/vibe)** - ⭐ 91
   Open-Source AI-powered web browser. Browse the web with your own LLM API key. Alternative to Dia / Comet.

1828. **[awsome_kali_MCPServers](https://github.com/ccq1/awsome_kali_MCPServers)** - ⭐ 91
   awsome kali MCPServers is a set of MCP servers tailored for Kali Linux

1829. **[QMT-MCP](https://github.com/guangxiangdebizi/QMT-MCP)** - ⭐ 91
    QMT-MCP 模块化量化交易助手

1830. **[stock-mcp](https://github.com/huweihua123/stock-mcp)** - ⭐ 91
   专业的金融市场数据 MCP 服务器 - 支持A股/美股/加密货币，原生 MCP 协议，AI Agent 友好

1831. **[generative-ui-playground](https://github.com/CopilotKit/generative-ui-playground)** - ⭐ 91
   Interact with all three types of generative UI, all in one interface

1832. **[mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)** - ⭐ 90
   MCP Python Interpreter: run python code. Python-mcp-server, mcp-python-server, Code Executor

1833. **[pinescript-mcp-server](https://github.com/cklose2000/pinescript-mcp-server)** - ⭐ 90
   A Model Context Protocol (MCP) server for working with TradingView PineScript

1834. **[agent-toolkit](https://github.com/sanity-io/agent-toolkit)** - ⭐ 90
   Collection of resources to help AI agents build better with Sanity.

1835. **[molecule-mcp](https://github.com/ChatMol/molecule-mcp)** - ⭐ 89
   A model-context-protocol server for molecules.

1836. **[mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw)** - ⭐ 88
   An MCP stdio to HTTP SSE transport gateway with example server and MCP client

1837. **[mcp-rest-api](https://github.com/dkmaker/mcp-rest-api)** - ⭐ 88
   A TypeScript-based MCP server that enables testing of REST APIs through Cline. This tool allows you to test and interact with any REST API endpoints directly from your development environment.

1838. **[apps-sdk-template](https://github.com/alpic-ai/apps-sdk-template)** - ⭐ 88
   A minimalist Typescript ChatGPT App based on the Skybridge framework

1839. **[mcp-ui](https://github.com/machaojin1917939763/mcp-ui)** - ⭐ 88
   基于MCP(Model Context Protocol)的智能聊天应用，支持Web和桌面环境。集成OpenAI/Anthropic API，提供MCP服务器的所有工具能力。简洁现代的UI设计，支持跨平台部署。

1840. **[amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)** - ⭐ 88
   高德地图MCP Server，支持stdio, sse和streamable-http

1841. **[mcp-agent](https://github.com/Haohao-end/mcp-agent)** - ⭐ 88
   A modular Python framework implementing the Model Context Protocol (MCP). It features a standardized client-server architecture over StdIO, integrating LLMs with external tools, real-time weather data fetching, and an advanced RAG (Retrieval-Augmented Generation) system.

1842. **[mcpgen](https://github.com/lyeslabs/mcpgen)** - ⭐ 88
   Generate Go MCP server boilerplate from OpenAPI 3 specifications

1843. **[chat-ui](https://github.com/AI-QL/chat-ui)** - ⭐ 88
   Single-File AI Chatbot UI with Multimodal & MCP Support: An All-in-One HTML File for a Streamlined Chatbot Conversational Interface

1844. **[mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite)** - ⭐ 88
   🐇 Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities

1845. **[mcp-metatrader5-server](https://github.com/Qoyyuum/mcp-metatrader5-server)** - ⭐ 88
   A Model Context Protocol (MCP) server for interacting with the MetaTrader 5 trading platform. This server provides AI assistants with tools and resources to access market data, perform trading operations, and analyze trading history.

1846. **[spring-ai](https://github.com/eazybytes/spring-ai)** - ⭐ 88
   From Java Dev to AI Engineer: Spring AI Fast Track

1847. **[mem0-mcp](https://github.com/pinkpixel-dev/mem0-mcp)** - ⭐ 87
   ✨ mem0 MCP Server: A memory system using mem0 for AI applications with model context protocl (MCP) integration. Enables long-term memory for AI agents as a drop-in MCP server.

1848. **[achatbot](https://github.com/ai-bot-pro/achatbot)** - ⭐ 87
   An open source chat bot architecture for voice/vision (and multimodal) assistants,  local(CPU/GPU bound) and remote(I/O bound) to run.

1849. **[awesome-openid-connect](https://github.com/cerberauth/awesome-openid-connect)** - ⭐ 87
   OpenID Connect, the authentication protocol and identity layer on top of OAuth 2.0 used in many SSO and adopted in many social logins (Apple, Facebook, Google, ...etc). Find this curated list of providers, services, libraries, and resources to adopt it and know more about existing specs.

1850. **[slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)** - ⭐ 87
   mcp server for slidev to make web ppt quickly and elegantly

1851. **[memory-mcp-server-go](https://github.com/okooo5km/memory-mcp-server-go)** - ⭐ 87
   A Model Context Protocol server that provides knowledge graph management capabilities.

1852. **[reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp)** - ⭐ 87
   Turn Reddit's chaos into structured insights with full citations. MCP server for competitive analysis, customer discovery, and market research. Zero-setup hosted solution with semantic search across 20,000+ subreddits.

1853. **[cve-search_mcp](https://github.com/roadwy/cve-search_mcp)** - ⭐ 87
   A Model Context Protocol (MCP) server for querying the CVE-Search API

1854. **[mcp-jenkins](https://github.com/lanbaoshen/mcp-jenkins)** - ⭐ 87
   The Model Context Protocol (MCP) is an open-source implementation that bridges Jenkins with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Jenkins tools while maintaining data privacy and security.

1855. **[mcp-dbutils](https://github.com/donghao1393/mcp-dbutils)** - ⭐ 87
   数读 是一件可以让你的大模型安全连接到数据库的MCP工具。| DButils is an all-in-one MCP service that enables your AI to do data analysis by harnessing versatile types of database (sqlite, mysql, postgres, and more) within a unified configuration of multiple connections in a secured way (like SSL and controlled write access).

1856. **[monarch-mcp-server](https://github.com/robcerda/monarch-mcp-server)** - ⭐ 87
   MCP Server for use with Monarch Money

1857. **[Delphi-MCP-Server](https://github.com/GDKsoftware/Delphi-MCP-Server)** - ⭐ 87
   Native Delphi Server implementation of the Model Context Protocol (MCP)

1858. **[react-agent-hooks](https://github.com/chuanqisun/react-agent-hooks)** - ⭐ 86
   Turn React hooks into LLM tools

1859. **[mcp-server-llamacloud](https://github.com/run-llama/mcp-server-llamacloud)** - ⭐ 86
   A MCP server connecting to managed indexes on LlamaCloud

1860. **[vggt-mps](https://github.com/jmanhype/vggt-mps)** - ⭐ 86
   VGGT 3D Vision Agent optimized for Apple Silicon with Metal Performance Shaders

1861. **[FrontAgent](https://github.com/ceilf6/FrontAgent)** - ⭐ 86
   AI agent platform for frontend engineering with SDD constraints & MCP-controlled automation. | 面向前端工程的企业级 AI Agent 平台

1862. **[furi](https://github.com/ashwwwin/furi)** - ⭐ 86
   CLI & API for MCP management

1863. **[agent-tool-protocol](https://github.com/mondaycom/agent-tool-protocol)** - ⭐ 86
   Agent Tool Protocol

1864. **[ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server)** - ⭐ 86
   Ragie Model Context Protocol Server

1865. **[legion-mcp](https://github.com/TheRaLabs/legion-mcp)** - ⭐ 86
   A server that helps people access and query data in databases using the Legion Query Runner with Model Context Protocol (MCP) in Python.

1866. **[identity](https://github.com/agntcy/identity)** - ⭐ 86
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

1867. **[oxylabs-mcp](https://github.com/oxylabs/oxylabs-mcp)** - ⭐ 86
   Official Oxylabs MCP integration

1868. **[awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)** - ⭐ 86
   A curated list of OSINT MCP servers. Pull requests are welcomed!

1869. **[meta-mcp](https://github.com/brijr/meta-mcp)** - ⭐ 86
   MCP Server for connecting to the Meta Marketing API

1870. **[github-stars](https://github.com/ccbikai/github-stars)** - ⭐ 85
   A Cloudflare-powered MCP (Model Context Protocol) Server that allows you to search and query your GitHub starred repositories using natural language.

1871. **[mcp](https://github.com/twilio-labs/mcp)** - ⭐ 85
   Monorepo providing 1) OpenAPI to MCP Tool generator 2) Exposing all of Twilio's API as MCP Tools

1872. **[arbor](https://github.com/Anandb71/arbor)** - ⭐ 85
   Graph-native code intelligence that replaces embedding-based RAG with deterministic program understanding.

1873. **[mcp-dockmaster](https://github.com/dcSpark/mcp-dockmaster)** - ⭐ 84
   MCP Dockmaster allows you to easily install and manage MCP servers. Available for Mac, Windows and Linux as a Desktop App, CLI and a library.

1874. **[spiceflow](https://github.com/remorses/spiceflow)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1875. **[spiceflow-framework](https://github.com/remorses/spiceflow-framework)** - ⭐ 84
   Super Simple API framework, type safe, automatic OpenAPI, MCP support, client RPC, streaming with SSE

1876. **[cursor-rust-tools](https://github.com/terhechte/cursor-rust-tools)** - ⭐ 84
   A MCP server to allow the LLM in Cursor to access Rust Analyzer, Crate Docs and Cargo Commands.

1877. **[mcp-server](https://github.com/cap-js/mcp-server)** - ⭐ 84
   MCP server for AI-assisted development of CAP applications

1878. **[math-mcp](https://github.com/EthanHenrickson/math-mcp)** - ⭐ 84
   A Model Context Protocol (MCP) server that provides basic mathematical and statistical functions to Large Language Models (LLMs). This server enables LLMs to perform accurate numerical calculations through a simple API.

1879. **[github-chat-mcp](https://github.com/AsyncFuncAI/github-chat-mcp)** - ⭐ 84
   A Model Context Protocol (MCP) for analyzing and querying GitHub repositories using the GitHub Chat API.

1880. **[mcp-github-project-manager](https://github.com/kunwarVivek/mcp-github-project-manager)** - ⭐ 83
   a mcp server to manage github project's functionality 

1881. **[mcp-node](https://github.com/algolia/mcp-node)** - ⭐ 83
   MCP server for interacting with Algolia

1882. **[claude-swarm](https://github.com/cj-vana/claude-swarm)** - ⭐ 83
   MCP server for orchestrating parallel Claude Code worker swarms with protocol-based behavioral governance, persistent state, and real-time monitoring dashboard

1883. **[xiaozhi-mcp-ha](https://github.com/mac8005/xiaozhi-mcp-ha)** - ⭐ 83
   A Home Assistant Custom Integration (HACS) that connects Xiaozhi ESP32 AI chatbot to Home Assistant via MCP

1884. **[viper](https://github.com/ozanunal0/viper)** - ⭐ 83
   🛡️ VIPER: Stay ahead of threats with AI-driven vulnerability intelligence. Prioritize CVEs effectively using NVD, EPSS, CISA KEV, and Google Gemini insights, all on an interactive dashboard

1885. **[mcp-gateway](https://github.com/hyprmcp/mcp-gateway)** - ⭐ 83
   MCP OAuth Proxy incl. dynamic client registration (DCR), MCP prompt analytics and MCP firewall to build enterprise grade MCP servers.

1886. **[mcp-excel-server](https://github.com/yzfly/mcp-excel-server)** - ⭐ 83
   The Excel MCP Server is a powerful tool that enables natural language interaction with Excel files through the Model Context Protocol (MCP). It provides a comprehensive set of capabilities for reading, analyzing, visualizing, and writing Excel data.

1887. **[mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** - ⭐ 83
   Version 2.2 - 54 tools available - an MCP server for interacting with the Canvas LMS API. This server allows you to manage courses, assignments, enrollments, and grades within Canvas.

1888. **[fabric-mcp](https://github.com/ksylvan/fabric-mcp)** - ⭐ 83
   Fabric MCP Server: Seamlessly integrate Fabric AI capabilities into MCP-enabled tools like IDEs and chat interfaces.

1889. **[fullstack-langgraph-nextjs-agent](https://github.com/agentailor/fullstack-langgraph-nextjs-agent)** - ⭐ 83
     Production-ready Next.js template for building AI agents with LangGraph.js. Features MCP integration for dynamic tool loading, human-in-the-loop tool approval, persistent conversation memory   with PostgreSQL, and real-time streaming responses. Built with TypeScript, React, Prisma, and Tailwind CSS.

1890. **[mcp-server-tauri](https://github.com/hypothesi/mcp-server-tauri)** - ⭐ 83
   A Model Context Protocol (MCP) server and plugin for Tauri v2 development

1891. **[Awesome-Claude-MCP-Servers](https://github.com/win4r/Awesome-Claude-MCP-Servers)** - ⭐ 82
   A curated list of Model Context Protocol (MCP) servers optimized for Claude AI assistants.

1892. **[mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder)** - ⭐ 82
   🪄 MCP server for programmatic creation and management of n8n workflows. Enables AI assistants to build, modify, and manage workflows without direct user intervention through a comprehensive set of tools and resources for interacting with n8n's REST API.

1893. **[agentic-stock-research-system](https://github.com/rooneyrulz/agentic-stock-research-system)** - ⭐ 82
   A sophisticated multi-agent AI system for analyzing Indian NSE-listed stocks using real-time data, technical indicators, news sentiment, and advanced AI reasoning.

1894. **[dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)** - ⭐ 82
   Model Context Protocol (MCP) for interacting with dicom servers (PACS etc.)

1895. **[ramparts](https://github.com/highflame-ai/ramparts)** - ⭐ 82
   mcp scan that scans any mcp server for indirect attack vectors and security or configuration vulnerabilities

1896. **[mcp-rs-template](https://github.com/linux-china/mcp-rs-template)** - ⭐ 82
   Model Context Protocol (MCP) CLI server template for Rust

1897. **[rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp)** - ⭐ 82
   MCP server that lets you shop groceries across the Rohlik Group platforms (Rohlik.cz, Knuspr.de, Gurkerl.at, Kifli.hu, Sezamo.ro)

1898. **[gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp)** - ⭐ 82
   Interact seamlessly with GitLab repositories to manage merge requests and issues. Fetch details, add comments, and streamline your code review process with ease.

1899. **[surrealmcp](https://github.com/surrealdb/surrealmcp)** - ⭐ 82
   The official MCP server for SurrealDB

1900. **[ols4](https://github.com/EBISPOT/ols4)** - ⭐ 82
   The EMBL-EBI Ontology Lookup Service (OLS)

1901. **[deterministic-agent-control-protocol](https://github.com/elliot35/deterministic-agent-control-protocol)** - ⭐ 81
   Governance gateway for AI agents — bounded, auditable, session-aware control with MCP proxy, shell proxy & HTTP API. Works with Cursor, Claude Code, Codex, and any MCP-compatible agent.

1902. **[office-editor-mcp](https://github.com/theWDY/office-editor-mcp)** - ⭐ 81
   基于MCP(Model Context Protocol)的Office文档处理助手，支持在MCP Client中创建和编辑Word、Excel、Powerpoint文档。

1903. **[mcp-memory-libsql](https://github.com/spences10/mcp-memory-libsql)** - ⭐ 81
   🧠 High-performance persistent memory system for Model Context Protocol (MCP) powered by libSQL. Features vector search, semantic knowledge storage, and efficient relationship management - perfect for AI agents and knowledge graph applications.

1904. **[node-candidate-mcp-server](https://github.com/jhgaylor/node-candidate-mcp-server)** - ⭐ 81
   A Model Context Protocol (MCP) server library that gives LLMs access to information about a candidate.

1905. **[sh-disney-mcp](https://github.com/syyuan14/sh-disney-mcp)** - ⭐ 81
   sh-disney-mcp 是一个基于 Model Context Protocol (MCP) 的mcp server，旨在通过标准化的接口，帮助大模型快速获取上海迪士尼乐园的门票价格和售卖状态信息

1906. **[mcphub](https://github.com/Cognitive-Stack/mcphub)** - ⭐ 81
   MCPHub is an embeddable Model Context Protocol (MCP) solution for AI services. Seamlessly integrate MCP servers with OpenAI Agents, LangChain, and Autogen frameworks through a unified interface. Simplifies configuration, setup, and management of MCP tools across different AI applications.

1907. **[anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server)** - ⭐ 81
   A model context protocol server that connects to Anki through AnkiConnect

1908. **[mcp-server](https://github.com/keboola/mcp-server)** - ⭐ 81
   Model Context Protocol (MCP) Server for the Keboola Platform

1909. **[aws-security-mcp](https://github.com/groovyBugify/aws-security-mcp)** - ⭐ 81
   A Model Context Protocol server that connects AI assistants like Claude to AWS security services, allowing them to autonomously query, inspect, and analyze AWS infrastructure for security issues and misconfigurations.

1910. **[mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery)** - ⭐ 81
   A command-line tool written in Rust for discovering and documenting MCP Server capabilities.

1911. **[NASA-MCP-server](https://github.com/ProgramComputer/NASA-MCP-server)** - ⭐ 81
   A Model Context Protocol (MCP) server for NASA APIs, providing a standardized interface for AI models to interact with NASA's vast array of data sources.

1912. **[advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp)** - ⭐ 81
   Public repository for Advanced Unity MCP by Code Maestro (www.code-maestro.com).

1913. **[mcp-openapi](https://github.com/ReAPI-com/mcp-openapi)** - ⭐ 81
   OpenAPI specification MCP server.

1914. **[mcp-hetzner](https://github.com/dkruyt/mcp-hetzner)** - ⭐ 81
   A Model Context Protocol (MCP) server for interacting with the Hetzner Cloud API. This server allows language models to manage Hetzner Cloud resources through structured functions.

1915. **[zed-mcp-server-github](https://github.com/LoamStudios/zed-mcp-server-github)** - ⭐ 81
   A GitHub MCP Server extension for Zed

1916. **[XActions](https://github.com/nirholas/XActions)** - ⭐ 81
   ⚡ The Complete X/Twitter Automation Toolkit — Scrapers, MCP server for AI agents (Claude/GPT), CLI, browser scripts. No API fees. Open source. Unfollow people who don't follow back. Monitor real-time analytics. Auto follow, like, comment, scrape, without API.

1917. **[gopher-mcp](https://github.com/GopherSecurity/gopher-mcp)** - ⭐ 81
   MCP C++ SDK - Model Context Protocol implementation in CPP with enterprise-grade security, visibility and connectivity.

1918. **[mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai)** - ⭐ 80
   MCP Server integrating MCP Clients with Stability AI-powered image manipulation functionalities: generate, edit, upscale, and more.

1919. **[MCPay](https://github.com/microchipgnu/MCPay)** - ⭐ 80
   Open-source Infrastructure for MCP and x402

1920. **[woocommerce-mcp-server](https://github.com/techspawn/woocommerce-mcp-server)** - ⭐ 80
   A WooCommerce (MCP) Model Context Protocol server

1921. **[code-to-tree](https://github.com/micl2e2/code-to-tree)** - ⭐ 80
   A runtime-free MCP server that converts source code into AST🌲, regardless of language.

1922. **[mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi)** - ⭐ 80
   A MCP server that enables Claude to discover and call any API endpoint through semantic search. Intelligently chunks OpenAPI specifications to handle large API documentation, with built-in request execution capabilities. Perfect for integrating private APIs with Claude Desktop.

1923. **[mcp-forge](https://github.com/achetronic/mcp-forge)** - ⭐ 80
   A complete MCP server template that include vitamins (oauth authentication included)

1924. **[agentic-tools-mcp](https://github.com/Pimzino/agentic-tools-mcp)** - ⭐ 80
   A comprehensive Model Context Protocol (MCP) server providing AI assistants with powerful task management and agent memories capabilities with project-specific storage.

1925. **[mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci)** - ⭐ 80
   A specialized server implementation for the Model Context Protocol (MCP) designed to integrate with CircleCI's development workflow. This project serves as a bridge between CircleCI's infrastructure and the Model Context Protocol, enabling enhanced AI-powered development experiences.

1926. **[Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp)** - ⭐ 80
   generate lyrics, song and background music(instrumental). Model Context Protocol (MCP) server.

1927. **[fastmcp-boilerplate](https://github.com/punkpeye/fastmcp-boilerplate)** - ⭐ 79
   A simple MCP server built using FastMCP, TypeScript, ESLint, and Prettier.

1928. **[codemirror-mcp](https://github.com/marimo-team/codemirror-mcp)** - ⭐ 79
   CodeMirror extension to hook up a Model Context Provider (MCP)

1929. **[jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** - ⭐ 79
   A Go-based MCP (Model Control Protocol) connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

1930. **[ls-mcp](https://github.com/lirantal/ls-mcp)** - ⭐ 79
   List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

1931. **[mcp-monitor](https://github.com/seekrays/mcp-monitor)** - ⭐ 79
   A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.

1932. **[glif-mcp-server](https://github.com/glifxyz/glif-mcp-server)** - ⭐ 79
   Easily run glif.app AI workflows inside your LLM: image generators, memes, selfies, and more. Glif supports all major multimedia AI models inside one app

1933. **[mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops)** - ⭐ 79
   A Model Context Protocol (MCP) server enabling AI assistants to interact with Azure DevOps services via Python SDK.

1934. **[youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp)** - ⭐ 79
   Model Context Protocol Server for YouTrack - Multi-platform support (ARM64/Apple Silicon + AMD64) with comprehensive API integration

1935. **[google-ai-mode-mcp](https://github.com/PleasePrompto/google-ai-mode-mcp)** - ⭐ 79
   MCP server for free Google AI Mode search with citations. Query optimization, CAPTCHA handling, multi-agent support. Works with Claude Code, Cursor, Cline, Windsurf.

1936. **[one-search-mcp](https://github.com/yokingma/one-search-mcp)** - ⭐ 79
   🚀 OneSearch MCP Server: Web Search & Scraper & Extract,  Support agent-browser, SearXNG, Tavily, DuckDuckGo, Bing, etc.

1937. **[django-ai-boost](https://github.com/vintasoftware/django-ai-boost)** - ⭐ 78
   A MCP server for Django applications, inspired by Laravel Boost.

1938. **[rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** - ⭐ 78
   rtfmbro provides always-up-to-date, version-specific package documentation as context for coding agents. An alternative to context7

1939. **[quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** - ⭐ 78
   The QuickBooks MCP Server lets AI assistants access QuickBooks data via a standard interface. It uses the Model Context Protocol to expose QBO features as callable tools, enabling developers to build AI apps that fetch real-time QBO data through MCP.

1940. **[ig-mcp](https://github.com/jlbadano/ig-mcp)** - ⭐ 77
   A production-ready Model Context Protocol (MCP) server that enables AI applications to seamlessly interact with Instagram Business accounts.

1941. **[lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp)** - ⭐ 77
   AI-powered code quality analysis using MCP to help AI assistants review code more effectively. Analyze git changes for complexity, security issues, and more through structured prompts.

1942. **[visual-ui-debug-agent-mcp](https://github.com/samihalawa/visual-ui-debug-agent-mcp)** - ⭐ 77
   VUDA is an autonomous debugging agent that empowers AI models to visually analyze, test, and debug web

1943. **[devex](https://github.com/ParthKapoor-dev/devex)** - ⭐ 77
   ⚡️ Devex — A Fast, Secure, and Scalable Repl-as-a-Service Platform built for Developers 🚀

1944. **[tester-mcp-client](https://github.com/apify/tester-mcp-client)** - ⭐ 77
   Model Context Protocol (MCP) Client for Apify's Actors

1945. **[terminal_server](https://github.com/theailanguage/terminal_server)** - ⭐ 77
   MCP server that can execute terminal commands

1946. **[mcp-reticle](https://github.com/LabTerminal/mcp-reticle)** - ⭐ 77
   Reticle intercepts, visualizes, and profiles JSON-RPC traffic between your LLM and MCP servers in real-time, with zero latency overhead. Stop debugging blind. Start seeing everything.

1947. **[mcp-llm](https://github.com/sammcj/mcp-llm)** - ⭐ 77
    An MCP server that provides LLMs access to other LLMs

1948. **[bridge4simulator](https://github.com/AppGram/bridge4simulator)** - ⭐ 77
   An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates with Claude Desktop, Cursor, Claude Code, and other MCP-compatible clients.

1949. **[ExternalAttacker-MCP](https://github.com/MorDavid/ExternalAttacker-MCP)** - ⭐ 77
   A modular external attack surface mapping tool integrating tools for automated reconnaissance and bug bounty workflows.

1950. **[bing-search-mcp](https://github.com/leehanchung/bing-search-mcp)** - ⭐ 77
   MCP Server for Bing Search API

1951. **[sample-agents-with-nova-act-and-mcp](https://github.com/aws-samples/sample-agents-with-nova-act-and-mcp)** - ⭐ 77
   Discover how to build agents that can perform actions on websites by combining Amazon Nova Act with Model Context Protocol (MCP).

1952. **[mcp](https://github.com/vuetifyjs/mcp)** - ⭐ 77
   🤖 A Model Context Protocol (MCP) library for use with Agentic chat bots

1953. **[wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server)** - ⭐ 77
   A Python server implementation for WeCom (WeChat Work) bot that follows the Model Context Protocol (MCP). This server provides a standardized interface for handling automated messaging and context-aware interactions within enterprise WeChat environments.

1954. **[ophis](https://github.com/njayp/ophis)** - ⭐ 77
   Transform any Cobra CLI into an MCP server

1955. **[ynab-mcp-server](https://github.com/calebl/ynab-mcp-server)** - ⭐ 77
   Model Context Protocol for YNAB (you need a budget)

1956. **[NetworkOps_Platform](https://github.com/E-Conners-Lab/NetworkOps_Platform)** - ⭐ 77
   AI-powered network automation via Model Context Protocol (MCP). 178 tools for multi-vendor infrastructure   management, self-healing agents, drift detection, and a real-time web dashboard.

1957. **[google-cloud-mcp](https://github.com/krzko/google-cloud-mcp)** - ⭐ 76
   🤖 A Model Context Protocol (MCP) server for Google Cloud (GCP)

1958. **[mcp-gemini-google-search](https://github.com/yukukotani/mcp-gemini-google-search)** - ⭐ 76
   MCP server for Google Search integration using Gemini's built-in search capabilities

1959. **[codeglide-mcpgen](https://github.com/CodeGlide/codeglide-mcpgen)** - ⭐ 76
   Generation of Secure MCP (Model Context Protocol) Servers from API source code at Scale

1960. **[ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server)** - ⭐ 76
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the ChEMBL chemical database.

1961. **[cursor10x-mcp](https://github.com/aiurda/cursor10x-mcp)** - ⭐ 76
   The Cursor10x MCP is a persistent multi-dimensional memory system for Cursor that enhances AI assistants with conversation context, project history, and code relationships across sessions.

1962. **[HopperMCP](https://github.com/MxIris-Reverse-Engineering/HopperMCP)** - ⭐ 76
   A Model Context Protocol server for Hopper Disassembler

1963. **[mcp-kafka](https://github.com/kanapuli/mcp-kafka)** - ⭐ 76
   A Model Context Protocol Server to perform Kafka client operations

1964. **[mcpc](https://github.com/mcpc-tech/mcpc)** - ⭐ 76
   Build agentic-MCP servers by composing existing MCP tools.

1965. **[jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server)** - ⭐ 76
   This is an implementation project of a JVM-based MCP (Model Context Protocol) server. The project aims to provide a standardized MCP server implementation for the JVM platform, enabling AI models to better interact with the Java ecosystem.

1966. **[imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** - ⭐ 75
   An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP). This server is built with the FastMCP framework and the imessagedb library, enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling.

1967. **[agentic-coding](https://github.com/sammcj/agentic-coding)** - ⭐ 75
   Agentic Coding Rules, Templates etc...

1968. **[mcp-llms-txt-explorer](https://github.com/thedaviddias/mcp-llms-txt-explorer)** - ⭐ 75
   MCP to explore websites with llms.txt files

1969. **[rust-mcp-schema](https://github.com/rust-mcp-stack/rust-mcp-schema)** - ⭐ 75
   A type-safe implementation of the official Model Context Protocol (MCP) schema in Rust.

1970. **[choturobo](https://github.com/vishalmysore/choturobo)** - ⭐ 75
   Integrate Arduino-based robotics (using the NodeMCU ESP32 or Arduino Nano 368 board) with AI using the MCP (Model Context Protocol) framework from Claude Anthropic

1971. **[slither-mcp](https://github.com/trailofbits/slither-mcp)** - ⭐ 75
   MCP server for Slither static analysis of Solidity smart contracts

1972. **[lazy-mcp](https://github.com/voicetreelab/lazy-mcp)** - ⭐ 75
     MCP proxy server with lazy loading support - reduces context usage through on-demand tool activation

1973. **[windbg-ext-mcp](https://github.com/NadavLor/windbg-ext-mcp)** - ⭐ 75
   WinDbg-ext-MCP bridges your favorite LLM client (like Cursor, Claude, or VS Code) with WinDbg, enabling real-time, AI assisted kernel debugging. Write prompts in your AI coding assistant and receive instant, context-aware analysis and insights from your live kernel debugging session.

1974. **[perplexity-mcp-zerver](https://github.com/wysh3/perplexity-mcp-zerver)** - ⭐ 75
   MCP web search using perplexity without any API KEYS 

1975. **[WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP)** - ⭐ 75
   WeChat-MCP: let Claude/ChatGPT and other AI assistants read and reply to WeChat for you

1976. **[SillyTavern-MCP-Client](https://github.com/bmen25124/SillyTavern-MCP-Client)** - ⭐ 74
   An extension of MCP for SillyTavern.

1977. **[ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp)** - ⭐ 74
   CCXT MCP Server bridges the gap between AI models and cryptocurrency trading by providing a standardized interface through the Model Context Protocol. Created to empower automated trading strategies, this tool allows AI assistants like Claude and GPT to directly interact with over 100 cryptocurrency exchanges without requiring users to write comple

1978. **[mcp-fal](https://github.com/am0y/mcp-fal)** - ⭐ 74
   A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

1979. **[masquerade](https://github.com/postralai/masquerade)** - ⭐ 74
   The Privacy Firewall for LLMs

1980. **[claude-mermaid](https://github.com/veelenga/claude-mermaid)** - ⭐ 74
   MCP Server to previewing mermaid diagrams

1981. **[bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp)** - ⭐ 73
   Bitcoin & Lightning Network MCP Server.

1982. **[conductor-tasks](https://github.com/hridaya423/conductor-tasks)** - ⭐ 73
   A task management system designed for AI development

1983. **[mcp-client-capabilities](https://github.com/apify/mcp-client-capabilities)** - ⭐ 73
   Index of all Model Context Protocol (MCP) clients and their capabilities

1984. **[airtable-mcp](https://github.com/rashidazarang/airtable-mcp)** - ⭐ 73
   Airtable integration for AI-powered applications via Anthropic's Model Context Protocol (MCP)

1985. **[unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server)** - ⭐ 73
   The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.

1986. **[openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server)** - ⭐ 73
   LLM-powered OpenFOAM MCP server for intelligent CFD education with Socratic questioning and expert error resolution

1987. **[tauri-plugin-mcp](https://github.com/P3GLEG/tauri-plugin-mcp)** - ⭐ 73
   Allows AI agents (e.g., Cursor, Claude Code) to debug within Tauri apps via screenshot capture, window management, DOM access, and simulated user inputs.

1988. **[unreal-mcp](https://github.com/runreal/unreal-mcp)** - ⭐ 73
   MCP server for Unreal Engine that uses Unreal Python Remote Execution

1989. **[codebase-mcp](https://github.com/DeDeveloper23/codebase-mcp)** - ⭐ 72
   Model Context Protocol implementation for retrieving codebases using RepoMix

1990. **[ytt-mcp](https://github.com/cottongeeks/ytt-mcp)** - ⭐ 72
   MCP server to fetch YouTube transcripts

1991. **[Custom-MCP-Server](https://github.com/Sharan-Kumar-R/Custom-MCP-Server)** - ⭐ 72
   MCP server for scraping LinkedIn, Facebook, Instagram profiles and Google search.

1992. **[sanity-mcp-server](https://github.com/sanity-io/sanity-mcp-server)** - ⭐ 72
   Deprecated: Use the remote MCP server at https://mcp.sanity.io instead.

1993. **[github-brain](https://github.com/wham/github-brain)** - ⭐ 72
   An experimental GitHub MCP server with local database.

1994. **[BurpSuite-MCP-Server](https://github.com/X3r0K/BurpSuite-MCP-Server)** - ⭐ 72
   BurpSuite MCP Server:  A powerful Model Context Protocol (MCP) server implementation for BurpSuite, providing programmatic access to Burp's core functionalities.

1995. **[junos-mcp-server](https://github.com/Juniper/junos-mcp-server)** - ⭐ 72
   This is a Junos Model Context Protocol (MCP) Server project that provides a bridge between MCP-compatible clients (like Claude Desktop) and Juniper Junos network devices.

1996. **[raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server)** - ⭐ 72
   An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).

1997. **[ncp](https://github.com/portel-dev/ncp)** - ⭐ 72
   Natural Context Provider (NCP). Your MCPs, supercharged. Find any tool instantly, load on demand, run on schedule, ready for any   client. Smart loading saves tokens and energy.

1998. **[uml-mcp](https://github.com/antoinebou12/uml-mcp)** - ⭐ 72
   UML-MCP Server is a UML diagram generation tool based on MCP (Model Context Protocol), which can help users generate various types of UML diagrams through natural language description or directly writing PlantUML and Mermaid and Kroki

1999. **[mcp-openmemory](https://github.com/baryhuang/mcp-openmemory)** - ⭐ 72
   Simple standalone MCP server giving Claude the ability to remember your conversations and learn from them over time.

2000. **[MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha)** - ⭐ 71
   Connect your chat repl to wolfram alpha computational intelligence

2001. **[template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server)** - ⭐ 71
   Template to quickly set up your own MCP server 

2002. **[mcp-server-email](https://github.com/Shy2593666979/mcp-server-email)** - ⭐ 71
   一个基于 MCP (Model Context Protocol) 的邮件服务，支持 LLM 发送带附件的电子邮件及在指定目录中搜索文件。提供安全的 SMTP 传输、多收件人支持和附件模式匹配搜索功能，适用于 Gmail、Outlook、Yahoo、QQ 邮箱和网易 126 邮箱等主流邮箱服务。

2003. **[mcp-arr](https://github.com/aplaceforallmystuff/mcp-arr)** - ⭐ 71
   MCP server for *arr media management suite

2004. **[gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot)** - ⭐ 71
   A MCP server integration for Godot Engine that allows Claude, Cursor, Windsurf, VSCode, etc to perform actions like creating scenes, resources, scripts, reading errors and much more.

2005. **[trading-mcp](https://github.com/netanelavr/trading-mcp)** - ⭐ 70
   The MCP server that will help you trade smarter (or at least try)

2006. **[airtable-mcp](https://github.com/felores/airtable-mcp)** - ⭐ 70
   Search, create and update Airtable bases, tables, fields, and records using Claude Desktop and MCP (Model Context Protocol) clients

2007. **[railway-mcp](https://github.com/jason-tan-swe/railway-mcp)** - ⭐ 70
   An unofficial and community-built MCP server for integrating with https://railway.app

2008. **[OmniMCP](https://github.com/OpenAdaptAI/OmniMCP)** - ⭐ 70
   OmniMCP uses Microsoft OmniParser and Model Context Protocol (MCP) to provide AI models with rich UI context and powerful interaction capabilities.

2009. **[blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp)** - ⭐ 70
   Open Models MCP for Blender Using Ollama

2010. **[anilist-mcp](https://github.com/yuna0x0/anilist-mcp)** - ⭐ 70
   AniList MCP server for accessing anime and manga data

2011. **[mcp-velociraptor](https://github.com/mgreen27/mcp-velociraptor)** - ⭐ 70
   VelociraptorMCP is a Model Context Protocol bridge for exposing LLMs to MCP clients.

2012. **[turbomcp](https://github.com/Epistates/turbomcp)** - ⭐ 70
   A full featured, enterprise grade rust MCP SDK

2013. **[MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)** - ⭐ 69
   A Model Context Protocol (MCP) server implementation connecting Claude Desktop with DeepSeek's language models (R1/V3)

2014. **[mcp-client-python](https://github.com/alejandro-ao/mcp-client-python)** - ⭐ 69

2015. **[markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** - ⭐ 69
   A Model Context Protocol (MCP) server that converts various file formats to Markdown using the MarkItDown utility.

2016. **[ollama-mcp-client](https://github.com/mihirrd/ollama-mcp-client)** - ⭐ 69
   MCP client for local ollama models

2017. **[mcp-discord](https://github.com/barryyip0625/mcp-discord)** - ⭐ 69
   Implement Discord MCP server enabling AI assistants to interact with the Discord platform.

2018. **[tradingview-chart-mcp](https://github.com/ertugrul59/tradingview-chart-mcp)** - ⭐ 69
   MCP server that captures TradingView chart images via Selenium — supports any ticker/interval with browser pooling for concurrent performance

2019. **[joplin-mcp](https://github.com/alondmnt/joplin-mcp)** - ⭐ 69
   MCP server for the Joplin note taking app

2020. **[mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha)** - ⭐ 69
   A Python-powered Model Context Protocol MCP server and client that uses Wolfram Alpha via API.

2021. **[piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server)** - ⭐ 69
   A TypeScript implementation of a Model Context Protocol (MCP) server that integrates with PiAPI's API. PiAPI makes user able to generate media content with Midjourney/Flux/Kling/LumaLabs/Udio/Chrip/Trellis directly from Claude or any other MCP-compatible apps.

2022. **[wasmcp](https://github.com/wasmcp/wasmcp)** - ⭐ 69
   Build MCP servers with WebAssembly components

2023. **[mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy)** - ⭐ 69
   MCP Auth Proxy is a secure OAuth 2.1 authentication proxy for Model Context Protocol (MCP) servers

2024. **[fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp)** - ⭐ 69
   A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

2025. **[sub-agents-mcp](https://github.com/shinpr/sub-agents-mcp)** - ⭐ 69
   Define task-specific AI sub-agents in Markdown for any MCP-compatible tool.

2026. **[ClueoMCP](https://github.com/ClueoFoundation/ClueoMCP)** - ⭐ 68
   🎭 The Personality Layer for LLMs- Transform any MCP-compatible AI with rich, consistent personalities powered by Clueo's Big Five personality engine.

2027. **[vibe-blocks-mcp](https://github.com/majidmanzarpour/vibe-blocks-mcp)** - ⭐ 68
   Connects Roblox Studio to AI coding editors via the Model Context Protocol (MCP), enabling AI-assisted game development within your Roblox Studio environment.

2028. **[agenite](https://github.com/subeshb1/agenite)** - ⭐ 68
   🤖 Build powerful AI agents with TypeScript. Agenite makes it easy to create, compose, and control AI agents with first-class support for tools, streaming, and multi-agent architectures. Switch seamlessly between providers like OpenAI, Anthropic, AWS Bedrock, and Ollama.

2029. **[gmail-mcp-server](https://github.com/jasonsum/gmail-mcp-server)** - ⭐ 68
   Model Context Protocol (MCP) server for Gmail

2030. **[mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub)** - ⭐ 68
   The official Model Context Protocol (MCP) server for DataHub (https://datahub.com)

2031. **[boilerplate-mcp-server](https://github.com/aashari/boilerplate-mcp-server)** - ⭐ 68
   TypeScript Model Context Protocol (MCP) server boilerplate providing IP lookup tools/resources. Includes CLI support and extensible structure for connecting AI systems (LLMs) to external data sources like ip-api.com. Ideal template for creating new MCP integrations via Node.js.

2032. **[ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp)** - ⭐ 68
   An MCP server built on ableton-js enables AI assistants to control Ableton Live in real time, including Arrangement View operations such as song management, track control, MIDI editing, and audio recording, along with other capabilities.

2033. **[interactive-brokers-mcp](https://github.com/code-rabi/interactive-brokers-mcp)** - ⭐ 68
   Interactive Brokers MCP Server

2034. **[m3](https://github.com/rafiattrach/m3)** - ⭐ 68
   🏥🤖 Query MIMIC-IV medical data using natural language through Model Context Protocol (MCP). Transform healthcare research with AI-powered database interactions - supports both local MIMIC-IV SQLite demo dataset and full BigQuery datasets.

2035. **[mcp-server-node](https://github.com/lucianoayres/mcp-server-node)** - ⭐ 68
   MCP Server implemented in JavaScript using Node.js that demonstrates how to build an MCP server with a custom prompt and custom tools, including one that loads an environment variable from a configuration file, to integrate seamlessly with AI-assisted environments like Cursor IDE.

2036. **[xiaohongshu-mcp-python](https://github.com/luyike221/xiaohongshu-mcp-python)** - ⭐ 68
   xiaohongshu-mcp-python是一个基于现代Python技术栈开发的小红书内容自动化发布工具，通过Model Context Protocol (MCP)协议为AI客户端提供强大的小红书操作能力。  项目核心功能包括小红书账户登录管理、图文内容发布、视频内容发布、内容搜索与获取、帖子详情查看以及评论互动等。支持多种图片格式（JPG、PNG、GIF）和视频格式（MP4、MOV、AVI），既可处理本地文件路径，也支持HTTP/HTTPS链接，为用户提供灵活的内容发布方案。   该工具特别适合内容创作者、营销人员和开发者使用，能够显著提升小红书内容发布的效率和自动化程度。通过标准化的MCP接口，用户可以轻松地将小红书操作能力集成到各种AI工作流中，实现智能化的内容管理和发布。

2037. **[lc2mcp](https://github.com/xiaotonng/lc2mcp)** - ⭐ 68
   Convert LangChain tools to FastMCP tools

2038. **[ipybox](https://github.com/gradion-ai/ipybox)** - ⭐ 68
   Python code execution sandbox with programmatic MCP tool calling (PTC)

2039. **[mcp-bridge](https://github.com/firekula/mcp-bridge)** - ⭐ 68
   这是一个为 Cocos Creator 设计的 MCP (Model Context Protocol) 桥接插件，用于连接外部 AI 工具与 Cocos Creator 编辑器，实现对场景、节点等资源的自动化操作。

2040. **[MCPhoenix](https://github.com/jmanhype/MCPhoenix)** - ⭐ 67
   A simplified implementation of the Model Context Protocol (MCP) server using Elixir's Phoenix Framework.

2041. **[mcp_gradio_client](https://github.com/justjoehere/mcp_gradio_client)** - ⭐ 67
   This is a proof of concept repo on how to create a gradio UI using the Model Context Protocol Client Python SDK.

2042. **[deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp)** - ⭐ 67
   A MCP provider Deepseek reasoning content to MCP-enabled AI Clients, like Claude Desktop. Supports access to Deepseek's CoT from the Deepseek API service or a local Ollama server.

2043. **[deepview-mcp](https://github.com/ai-1st/deepview-mcp)** - ⭐ 67
   DeepView MCP is a Model Context Protocol server that enables IDEs like Cursor and Windsurf to analyze large codebases using Gemini 2.5 Pro's extensive context window.

2044. **[roundtable](https://github.com/askbudi/roundtable)** - ⭐ 67
   Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface

2045. **[shinzo-ts](https://github.com/shinzo-labs/shinzo-ts)** - ⭐ 67
   TypeScript SDK for MCP server observability, built on OpenTelemetry. Gain insight into agent usage patterns, contextualize tool calls, and analyze server performance across platforms. Integrate with any OpenTelemetry ingest service including the Shinzo platform.

2046. **[nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)** - ⭐ 67
   MCP server that provides tools and resources to control and monitor robots using Nav2.

2047. **[QuickMCP](https://github.com/gunpal5/QuickMCP)** - ⭐ 67
   Effortlessly Build Model Context Protocol Servers with OpenAPI or Swagger or Google Discovery Specifications

2048. **[erpnext-mcp-server](https://github.com/rakeshgangwar/erpnext-mcp-server)** - ⭐ 67
   Connect AI assistants to your ERPNext instance via the Model Context Protocol (MCP) using the official Frappe API.

2049. **[mcp_newsnow](https://github.com/sligter/mcp_newsnow)** - ⭐ 67
   一个基于 Model Context Protocol (MCP) 的新闻聚合服务器，通过 Newsnow API 提供多平台热点新闻和趋势话题。

2050. **[ros2_mcp](https://github.com/wise-vision/ros2_mcp)** - ⭐ 67
   Advanced MCP Server ROS 2 bridging AI agents straight into robotics

2051. **[mcp-bear](https://github.com/jkawamoto/mcp-bear)** - ⭐ 67
   A MCP server for interacting with Bear note-taking software.

2052. **[CanvasMCPClient](https://github.com/n00bvn/CanvasMCPClient)** - ⭐ 67
   Canvas MCP Client is an open-source, self-hostable dashboard application built around an infinite, zoomable, and pannable canvas. It provides a unified interface for interacting with multiple MCP (Model Context Protocol) servers through a flexible, widget-based system.

2053. **[MySQL_MCP](https://github.com/guangxiangdebizi/MySQL_MCP)** - ⭐ 66
   这是一个功能强大且易用的MySQL数据库MCP（Model Context Protocol）服务器，让你的AI助手可以安全地进行完整的数据库操作，支持多数据库连接管理、增删改查、事务管理和智能回滚功能。

2054. **[optuna-mcp](https://github.com/optuna/optuna-mcp)** - ⭐ 66
   The Optuna MCP Server is a Model Context Protocol (MCP) server to interact with Optuna APIs.

2055. **[awesome-mcp-best-practices](https://github.com/lirantal/awesome-mcp-best-practices)** - ⭐ 66
   Build Awesome MCPs with Awesome Best Practices for MCP Servers and MCP Clients

2056. **[nautex](https://github.com/hmldns/nautex)** - ⭐ 66
   MCP server for guiding Coding Agents via end-to-end requirements to implementation plan pipeline

2057. **[crash-mcp](https://github.com/nikkoxgonzales/crash-mcp)** - ⭐ 66
   MCP server for structured and efficient reasoning with step validation, branching, and revisions.

2058. **[mcp-gopls](https://github.com/hloiseau/mcp-gopls)** - ⭐ 66
   Model Context Protocol (MCP) server for Go using gopls – LSP-powered analysis, tests, coverage, and tooling.

2059. **[community-servers](https://github.com/mcp-get/community-servers)** - ⭐ 66
   This repository contains a collection of community-maintained Model Context Protocol (MCP) servers. All servers are automatically listed on the MCP Get registry and can be viewed and installed via CLI

2060. **[tiny-mcp](https://github.com/wdndev/tiny-mcp)** - ⭐ 66
   Python 实现 MCP client / service

2061. **[flapi](https://github.com/DataZooDE/flapi)** - ⭐ 66
   API Framework heavily relying on the power of DuckDB and DuckDB extensions. Ready to build performant and cost-efficient APIs on top of BigQuery or Snowflake  for AI Agents and Data Apps

2062. **[deep-research-mcp-server](https://github.com/ssdeanx/deep-research-mcp-server)** - ⭐ 66
   MCP Deep Research Server using Gemini creating a Research AI Agent

2063. **[robot_MCP](https://github.com/IliaLarchenko/robot_MCP)** - ⭐ 66
   A simple MCP server for the SO-ARM100 control

2064. **[VibeShift](https://github.com/GroundNG/VibeShift)** - ⭐ 66
   [MCP Server] The Security Agent for AI assisted coding

2065. **[voice-mcp-agent](https://github.com/den-vasyliev/voice-mcp-agent)** - ⭐ 66
   A voice assistant application built with the LiveKit Agents framework, capable of using Model Context Protocol (MCP) tools to interact with external services

2066. **[medical-mcp](https://github.com/JamesANZ/medical-mcp)** - ⭐ 66
   An MCP server that provides comprehensive medical information by querying multiple authoritative medical APIs including FDA, WHO, PubMed, Google Scholar, and RxNorm

2067. **[mcp-tutorials](https://github.com/chenmingyong0423/mcp-tutorials)** - ⭐ 65
   Model Context Protocol(MCP) 中文教程讲解

2068. **[mcp4k](https://github.com/ondrsh/mcp4k)** - ⭐ 65
   Compiler-driven MCP framework for Kotlin Multiplatform

2069. **[svelte5-mcp](https://github.com/StudentOfJS/svelte5-mcp)** - ⭐ 65
   A specialized Model Context Protocol (MCP) server for Svelte 5 frontend development

2070. **[fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server)** - ⭐ 65
   Open-source FRED MCP Server (Federal Reserve Economic Data)

2071. **[mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer)** - ⭐ 65
   MCP server providing token-efficient access to OpenAPI/Swagger specs via MCP Resource Templates for client-side exploration.

2072. **[mcp-fhir](https://github.com/flexpa/mcp-fhir)** - ⭐ 65
   A Model Context Protocol implementation for FHIR

2073. **[amazon-mcp](https://github.com/Fewsats/amazon-mcp)** - ⭐ 65
   Amazon MCP server to search & buy products using the L402

2074. **[mcp-all-in-one](https://github.com/vtxf/mcp-all-in-one)** - ⭐ 65
   A powerful MCP (Model Context Protocol) service aggregator that combines multiple MCP services into a single unified MCP service with self-configuration capabilities.

2075. **[dramacraft](https://github.com/whatyun/dramacraft)** - ⭐ 65
   DramaCraft 是一个专业的短剧视频编辑 MCP (Model Context Protocol) 服务，集成国产中文大模型 API，实现剪映的智能自动化编辑功能。项目已完成从视频分析到草稿生成的完整解决方案

2076. **[fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server)** - ⭐ 65
   FHIR MCP Server for handling medical data standard.

2077. **[open-skills](https://github.com/besoeasy/open-skills)** - ⭐ 65
   Battle-tested skill library for AI agents. Save 98% of API costs with ready-to-use code for crypto, PDFs, search, web scraping & more. No trial-and-error, no expensive APIs.

2078. **[mcp-image](https://github.com/shinpr/mcp-image)** - ⭐ 65
   MCP server for AI image generation and editing with automatic prompt optimization and quality presets (fast/balanced/quality). Powered by Gemini (Nano Banana 2 & Pro).

2079. **[lsd-mcp](https://github.com/lsd-so/lsd-mcp)** - ⭐ 64
   LSD Model Context Protocol

2080. **[ollama-mcp-client](https://github.com/anjor/ollama-mcp-client)** - ⭐ 64

2081. **[mcp-config](https://github.com/marcusschiesser/mcp-config)** - ⭐ 64
   A CLI tool for easy installation of MCP servers and managing their configuration

2082. **[mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye)** - ⭐ 64
   A Model Context Protocol server that provides network asset information based on query conditions. This server allows LLMs to obtain network asset information and supports querying network asset information by zoomeye dork etc.

2083. **[pydantic-rpc](https://github.com/i2y/pydantic-rpc)** - ⭐ 64
   PydanticRPC is a Python library for rapidly exposing Pydantic models as gRPC, ConnectRPC, and MCP services without protobuf files.

2084. **[MCP4EDA](https://github.com/NellyW8/MCP4EDA)** - ⭐ 64
   This is the Github Repo for the paper: MCP4EDA: LLM-Powered Model Context Protocol RTL-to-GDSII Automation with Backend Aware Synthesis Optimization. MCP server for a collection of open-source EDA tools

2085. **[purple-mcp](https://github.com/Sentinel-One/purple-mcp)** - ⭐ 64
   Access SentinelOne's Purple AI and security services through the Model Context Protocol (MCP) - query alerts, vulnerabilities, misconfigurations, and inventory

2086. **[usolver](https://github.com/sdiehl/usolver)** - ⭐ 64
   A model context protocol server for solving combinatorial optimization problems with logical and numerical constraints.

2087. **[EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)** - ⭐ 64
   The first open-source Model Context Protocol server enabling AI assistants and applications to interact programmatically with EnergyPlus building energy simulation.

2088. **[Pare](https://github.com/Dave-London/Pare)** - ⭐ 64
   Dev tools, optimized for agents. Structured, token-efficient MCP servers for git, test runners, npm, Docker, and more.

2089. **[UnrealMotionGraphicsMCP](https://github.com/winyunq/UnrealMotionGraphicsMCP)** - ⭐ 64
   🚀 UE5-UMG-MCP: A deep-focused MCP for Unreal Engine UMG layout. Designed to maximize AI efficiency within limited context windows by prioritizing precision in UI structure, animations, and blueprint integration.

2090. **[xc-mcp](https://github.com/conorluddy/xc-mcp)** - ⭐ 64
   XCode CLI MCP: Convenience wrapper for Xcode CLI tools & iOS Simulator. Progressive disclosure of tool responses to reduce context usage.  Use --mini param for build-only with tiny context footprint.

2091. **[agent-security-scanner-mcp](https://github.com/sinewaveai/agent-security-scanner-mcp)** - ⭐ 64
   Security scanner MCP server for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vulnerability rules with AST & taint analysis, auto-fix.

2092. **[mcp-sdk](https://github.com/AntigmaLabs/mcp-sdk)** - ⭐ 63
   Minimalistic Rust Implementation Of Model Context Protocol from Anthropic

2093. **[nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server implementation that integrates with the Nutrient Document Web Service (DWS) Processor API, providing powerful PDF processing capabilities for AI assistants.

2094. **[chess-mcp](https://github.com/pab1it0/chess-mcp)** - ⭐ 63
   A Model Context Protocol server for Chess.com's Published Data API.  This provides access to Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.

2095. **[mcp-server](https://github.com/UI5/mcp-server)** - ⭐ 63
   The UI5 MCP server improves the developer experience when working with agentic AI and the UI5 framework.

2096. **[mcd-mcp-server](https://github.com/M-China/mcd-mcp-server)** - ⭐ 63
   McDonald's China MCP Server Integration Guide

2097. **[clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server)** - ⭐ 63
   A Model Context Protocol (MCP) server for Microsoft Clarity

2098. **[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp)** - ⭐ 63
   A Model Context Protocol server to run locally and connect to a Canvas LMS 

2099. **[ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)** - ⭐ 63
   Extend the Ollama API with dynamic AI tool integration from multiple MCP (Model Context Protocol) servers. Fully compatible, transparent, and developer-friendly, ideal for building powerful local LLM applications, AI agents, and custom chatbots

2100. **[mcp-miro](https://github.com/k-jarzyna/mcp-miro)** - ⭐ 62
   Miro integration for Model Context Protocol

2101. **[mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)** - ⭐ 62
   Cryptocurrency Market Data MCP Server

2102. **[mcp-durable-object-client](https://github.com/Dhravya/mcp-durable-object-client)** - ⭐ 62
   testing mcps

2103. **[mcp-server-okppt](https://github.com/NeekChaw/mcp-server-okppt)** - ⭐ 62
   这个项目是一个基于MCP (Model Context Protocol) 的服务器工具，名为 "MCP OKPPT Server"。它的核心功能是允许大型语言模型（如Claude、GPT等）通过生成SVG图像来间接设计和创建PowerPoint演示文稿。工具负责将这些SVG图像高质量地插入到PPTX幻灯片中，并保留其矢量特性，确保图像在PowerPoint中可缩放且清晰。

2104. **[xiaozhi-mcp-client](https://github.com/shadowcz007/xiaozhi-mcp-client)** - ⭐ 62
   可视化的配置和管理，给xiaozhi接入mcp

2105. **[data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp)** - ⭐ 62
   Advanced MCP server for seamless access to Israeli Government Open Data

2106. **[mcpr](https://github.com/devOpifex/mcpr)** - ⭐ 62
   Model Context Protocol server and client for R

2107. **[fli](https://github.com/punitarani/fli)** - ⭐ 62
   Google Flights MCP and Python Library

2108. **[vesta-mac-dist](https://github.com/scouzi1966/vesta-mac-dist)** - ⭐ 62
   Vesta macOS Distribution - Official releases and downloads.Vesta AI Chat Assistant for macOS - Built with SwiftUI and Apple Intelligence using Apple's on device model on MacOs Tahoe (MacOS 26). Now with side-by-side Qwen3-VL for vison

2109. **[zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server)** - ⭐ 62
   A Model Context Protocol server for Zendesk

2110. **[ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server)** - ⭐ 62
   A Model Context Protocol (MCP) server designed to integrate with the TickTick task management platform, enabling intelligent context-aware task operations and automation.

2111. **[MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP)** - ⭐ 62
   MeiGen-AI-Design-MCP — Turn Claude Code / OpenClaw into your local Lovart. Local ComfyUI, 1,400+ prompt library, multi-direction parallel generation.

2112. **[CodeMCP](https://github.com/SimplyLiz/CodeMCP)** - ⭐ 62
   Code intelligence for AI assistants - MCP server, CLI, and HTTP API with symbol navigation, impact analysis, and architecture mapping

2113. **[contentful-mcp](https://github.com/ivo-toby/contentful-mcp)** - ⭐ 61
   MCP (Model Context Protocol) server for the Contentful Management API

2114. **[kollektiv-mcp](https://github.com/alexander-zuev/kollektiv-mcp)** - ⭐ 61
   Kollektiv MCP enables you to chat with and query your own documents directly from IDEs and MCP clients. Private, secure, and integrated into your favorite code editor

2115. **[ollama-mcp-db](https://github.com/robdodson/ollama-mcp-db)** - ⭐ 61
   An interactive chat interface that combines Ollama's LLM capabilities with PostgreSQL database access through the Model Context Protocol (MCP).

2116. **[mcp-cn](https://github.com/mengjian-github/mcp-cn)** - ⭐ 61
   MCP Hub 中国是一个专注于 Model Context Protocol (MCP) 生态的开源平台。它致力于汇聚全球优质的 MCP 服务,提供一站式的解决方案,包括服务发现、接入指南和使用示例,并建立完善的中文生态,欢迎开发者参与贡献和完善平台功能。

2117. **[yamcp](https://github.com/hamidra/yamcp)** - ⭐ 61
   Organize your MCP servers in local workspaces, share them as Yet-Another-MCP through a single command

2118. **[identity-service](https://github.com/agntcy/identity-service)** - ⭐ 61
   AGNTCY Identity Service serves as the central hub for managing and verifying digital identities for your Agentic Services. 

2119. **[rember-mcp](https://github.com/rember/rember-mcp)** - ⭐ 61
   A Model Context Protocol (MCP) server for Rember.

2120. **[nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server)** - ⭐ 61
   nocodb mcp server

2121. **[mcp-clojure-sdk](https://github.com/unravel-team/mcp-clojure-sdk)** - ⭐ 61
   A Clojure SDK to create MCP servers (and eventually clients)

2122. **[MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server)** - ⭐ 61
   Model Context Protocol (MCP) Server to connect your AI with any MediaWiki

2123. **[bc-code-intelligence-mcp](https://github.com/JeremyVyska/bc-code-intelligence-mcp)** - ⭐ 61
   BC Code Intelligence MCP Server - Persona-driven workflow orchestration for Business Central development. Provides 16+ MCP tools, layered knowledge system, and intelligent BC pattern analysis through Model Context Protocol.

2124. **[zeromcp](https://github.com/mrexodia/zeromcp)** - ⭐ 61
   Zero-dependency MCP server implementation.

2125. **[mcp-server-security-standard](https://github.com/mcp-security-standard/mcp-server-security-standard)** - ⭐ 61
   MCP Server Security Standard (MSSS): an open, testable security control standard for certifying MCP servers, with levels, evidence requirements, and reporting schemas.

2126. **[devto-mcp](https://github.com/Arindam200/devto-mcp)** - ⭐ 60
   MCP Server of DevTo

2127. **[mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server)** - ⭐ 60
   mcp-difyworkflow-server is an mcp server Tools application that implements the query and invocation of Dify workflows, supporting the on-demand operation of multiple custom Dify workflows.

2128. **[autosteer](https://github.com/notch-ai/autosteer)** - ⭐ 60
   Desktop app for multi-workspace Claude Code management

2129. **[FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP)** - ⭐ 60
   FreeCAD plugin for automating model creation and control via Model Contro Protocol (MCP). Provides a MCP server,GUl panel, and client for running macros,managing documents, and adjusting views.

2130. **[mcp-servers](https://github.com/pulsemcp/mcp-servers)** - ⭐ 60
   MCP (Model Context Protocol) Servers authored and maintained by the PulseMCP team. We build reliable servers thoughtfully designed specifically for MCP Client-powered workflows.

2131. **[baml-agents](https://github.com/Elijas/baml-agents)** - ⭐ 60
   Building Agents with LLM structured generation (BAML), MCP Tools, and 12-Factor Agents principles

2132. **[joplin-mcp-server](https://github.com/dweigend/joplin-mcp-server)** - ⭐ 60
   A Model Context Protocol (MCP) Server for https://joplinapp.org/ that enables note access through the https://modelcontextprotocol.io. Perfect for integration with AI assistants like Claude.

2133. **[academia_mcp](https://github.com/IlyaGusev/academia_mcp)** - ⭐ 60
   Academia MCP server: Tools for automatic scientific research

2134. **[Alph](https://github.com/Aqualia/Alph)** - ⭐ 60
   Universal MCP Server Configuration Manager

2135. **[mcp-hub](https://github.com/lobstercare/mcp-hub)** - ⭐ 60
   A curated list of awesome Model Context Protocol (MCP) servers.

2136. **[mcp-server-echart](https://github.com/cnkanwei/mcp-server-echart)** - ⭐ 60
   基于 mcp-go 框架构建的 mcp 服务，它提供了一个能动态生成 ECharts 图表页面的工具。

2137. **[time-mcp](https://github.com/yokingma/time-mcp)** - ⭐ 60
   ⏰ Time MCP Server: Giving LLMs Time Awareness Capabilities

2138. **[bloodhound_mcp](https://github.com/mwnickerson/bloodhound_mcp)** - ⭐ 60
   A Model Context Protocol (MCP) server to converse with data in Bloodhound

2139. **[firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp)** - ⭐ 60
   Model Context Protocol server for Firefox DevTools - enables AI assistants to inspect and control Firefox browser through the Remote Debugging Protocol

2140. **[ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk)** - ⭐ 59
   OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library

2141. **[daipendency-mcp](https://github.com/daipendency/daipendency-mcp)** - ⭐ 59
   Model Context Protocol server for Daipendency

2142. **[smart-pet-with-mcp](https://github.com/shijianzhong/smart-pet-with-mcp)** - ⭐ 59
   一个桌宠形式的mcp client，可以对接任意mcp server,配合测试的mcp server 开源地址：https://github.com/shijianzhong/mcp-server-for-pc

2143. **[cline-mcp-memory-bank](https://github.com/dazeb/cline-mcp-memory-bank)** - ⭐ 59
   A memory system for Cline that tracks progress between conversations.

2144. **[shadcn-ui-mcp-server](https://github.com/ymadd/shadcn-ui-mcp-server)** - ⭐ 59
   MCP server for shadcn/ui component references

2145. **[nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server implementation exposes document processing capabilities through natural language, supporting both direct human interaction and AI agent tool calling.

2146. **[mobile-mcp](https://github.com/runablehq/mobile-mcp)** - ⭐ 59
   A Model Context Protocol (MCP) server that provides mobile automation capabilities.

2147. **[mcp_server_gdb](https://github.com/pansila/mcp_server_gdb)** - ⭐ 59
   MCP Server to expose the GDB debugging capabilities

2148. **[mcp](https://github.com/abap-ai/mcp)** - ⭐ 59
   ABAP MCP - Model Context Protocol - Server SDK

2149. **[quick-mcp-example](https://github.com/ALucek/quick-mcp-example)** - ⭐ 59
   Short and sweet example MCP server / client implementation for Tools, Resources and Prompts.

2150. **[mono-mcp](https://github.com/sin4ch/mono-mcp)** - ⭐ 59
   A comprehensive Model Context Protocol (MCP) server for Nigerian banking operations using the Mono Open Banking API.

2151. **[pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)** - ⭐ 59
   A Model Context Protocol (MCP) server enabling AI agents to intelligently search, retrieve, and analyze biomedical literature from PubMed via NCBI E-utilities. Includes a research agent scaffold. STDIO & HTTP

2152. **[blockbench-mcp-plugin](https://github.com/jasonjgardner/blockbench-mcp-plugin)** - ⭐ 59
   Adds MCP server to Blockbench

2153. **[mengram](https://github.com/alibaizhanov/mengram)** - ⭐ 59
   Human-like memory for AI agents — semantic, episodic & procedural. Experience-driven procedures that learn from failures. Free API, Python & JS SDKs, LangChain & CrewAI integrations.

2154. **[ashra-mcp](https://github.com/getrupt/ashra-mcp)** - ⭐ 58
   A Model Context Protocol server for Ashra

2155. **[create-mcp-app](https://github.com/boguan/create-mcp-app)** - ⭐ 58
   A CLI tool for quickly scaffolding Model Context Protocol (MCP) server applications with TypeScript support and modern development tooling

2156. **[mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom)** - ⭐ 58
   Axiom Model Context Protocol Server

2157. **[mcpserver](https://github.com/2234839/mcpserver)** - ⭐ 58
   为claude code+glm 添加上眼睛

2158. **[MCP-Dandan](https://github.com/82ch/MCP-Dandan)** - ⭐ 58
   MCP Security Solution for Agentic AI — real-time proxying, behavior analysis, and malicious tool detection

2159. **[job-searchoor](https://github.com/0xDAEF0F/job-searchoor)** - ⭐ 58
   A simple MCP server that delivers you jobs based on your needs

2160. **[mcp-think-tank](https://github.com/flight505/mcp-think-tank)** - ⭐ 58
   MCP Think Tank is a powerful Model Context Protocol (MCP) server designed to enhance the capabilities of AI assistants like Cursor and Claude. It provides a structured environment for enhanced reasoning, persistent memory, and responsible tool usage.

2161. **[scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)** - ⭐ 58
   ScapeGraph MCP Server

2162. **[freecad-mcp](https://github.com/contextform/freecad-mcp)** - ⭐ 58
   FreeCAD MCP - Open-source Model Context Protocol server for FreeCAD automation

2163. **[podman-mcp-server](https://github.com/manusa/podman-mcp-server)** - ⭐ 58
   Model Context Protocol (MCP) server for container runtimes (Podman and Docker)

2164. **[sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver)** - ⭐ 58
   Rust + WASM sublinear-time solver for asymmetric diagonally dominant systems. Exposes Neumann series, push, and hybrid random-walk algorithms with npm/npx CLI and Flow-Nexus HTTP streaming for swarm cost propagation and verification.

2165. **[stackoverflow-mcp](https://github.com/gscalzo/stackoverflow-mcp)** - ⭐ 58
   A Model Context Protocol server for querying Stack Overflow to help AI models find programming solutions

2166. **[mxcp](https://github.com/raw-labs/mxcp)** - ⭐ 58
   Model eXecution + Context Protocol: Enterprise-Grade Data-to-AI Infrastructure

2167. **[geoserver-mcp](https://github.com/mahdin75/geoserver-mcp)** - ⭐ 58
   A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API

2168. **[mcp-shell](https://github.com/sonirico/mcp-shell)** - ⭐ 58
   Give hands to AI. MCP server to run shell commands securely, auditably, and on demand.

2169. **[mcp-server-synology](https://github.com/atom2ueki/mcp-server-synology)** - ⭐ 58
   💾 Model Context Protocol (MCP) server for Synology NAS - Enables AI assistants (Claude, Cursor, Continue) to manage files, downloads, and system operations through secure API integration. Features Docker deployment, auto-authentication, and comprehensive file system tools.

2170. **[ask-user-questions-mcp](https://github.com/paulp-o/ask-user-questions-mcp)** - ⭐ 58
   Better 'AskUserQuestion' - A lightweight MCP server/OpenCode plugin/Agent Skills + CLI tool that allows your LLMs ask questions to you. Be the human in the human-in-the-loop!

2171. **[mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** - ⭐ 58
   Node.js/TypeScript MCP server for Atlassian Jira. Equips AI systems (LLMs) with tools to list/get projects, search/get issues (using JQL/ID), and view dev info (commits, PRs). Connects AI capabilities directly into Jira project management and issue tracking workflows.

2172. **[trpc-mcp-go](https://github.com/trpc-group/trpc-mcp-go)** - ⭐ 58
   Go implementation of the Model Context Protocol (MCP) with comprehensive Streamable HTTP, STDIO, and SSE support. 

2173. **[metis-router](https://github.com/metis-mantis/metis-router)** - ⭐ 57
   MCP router and Web Based MCP client

2174. **[Archive-Agent](https://github.com/shredEngineer/Archive-Agent)** - ⭐ 57
   Find your files with natural language and ask questions.

2175. **[adbfriend](https://github.com/mikepenz/adbfriend)** - ⭐ 57
   Android ADB CLI tool including integrated MCP Server with common adb actions used during development

2176. **[appium-mcp](https://github.com/Rahulec08/appium-mcp)** - ⭐ 57
   AI-powered mobile automation with Model Context Protocol (MCP) integration. Seamlessly control Android & iOS devices through Appium with intelligent visual element detection and recovery. Built for AI agents like Claude to perform complex mobile testing workflows.

2177. **[mcp-open-library](https://github.com/8enSmith/mcp-open-library)** - ⭐ 57
   A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

2178. **[mkp](https://github.com/StacklokLabs/mkp)** - ⭐ 57
   MKP is a Model Context Protocol (MCP) server for Kubernetes

2179. **[vscode-mcp](https://github.com/tjx666/vscode-mcp)** - ⭐ 57
   MCP server for Claude Code/VSCode/Cursor/Windsurf to use editor self functionality. ⚡ Get real-time LSP diagnostics, type information, and code navigation for AI coding agents without waiting for slow tsc/eslint checks.

2180. **[mcp-manager](https://github.com/MediaPublishing/mcp-manager)** - ⭐ 57
   A web-based GUI tool for managing Model Context Protocol (MCP) servers in Claude and Cursor

2181. **[umbraco-mcp](https://github.com/Matthew-Wise/umbraco-mcp)** - ⭐ 57
   A model context protocol  (MCP) server for Umbraco 

2182. **[mcp](https://github.com/twelvedata/mcp)** - ⭐ 57
   Twelve Data MCP (Model Context Protocol) Server provides seamless, real-time access to financial market data via WebSocket, enabling reliable streaming of price quotes, market metrics, and events directly into your applications.

2183. **[naver-search-mcp](https://github.com/isnow890/naver-search-mcp)** - ⭐ 57
   MCP server for Naver Search API integration. Provides comprehensive search capabilities across Naver services (web, news, blog, shopping, etc) and data trend analysis tools via DataLab API.

2184. **[mcp-gemini-search](https://github.com/arjunprabhulal/mcp-gemini-search)** - ⭐ 56
   Model Context Protocol (MCP) with Gemini 2.5 Pro. Convert conversational queries into flight searches using Gemini's function calling capabilities and MCP's flight search tools

2185. **[Intelli](https://github.com/intelligentnode/Intelli)** - ⭐ 56
   Build multi-model chatbots and agents from intent.

2186. **[mcp-thinking](https://github.com/mattzcarey/mcp-thinking)** - ⭐ 56
   thinking tool for claude desktop/mcp clients using Deepseek reasoner

2187. **[AllVoiceLab-MCP](https://github.com/allvoicelab/AllVoiceLab-MCP)** - ⭐ 56
   Official AllVoiceLab Model Context Protocol (MCP) server, supporting interaction with powerful text-to-speech and video translation APIs. 

2188. **[solana-mcp-server](https://github.com/openSVM/solana-mcp-server)** - ⭐ 56
   solana mcp sever to enable solana rpc methods

2189. **[mcp-batchit](https://github.com/ryanjoachim/mcp-batchit)** - ⭐ 56
   🚀 MCP aggregator for batching multiple tool calls into a single request. Reduces overhead, saves tokens, and simplifies complex operations in AI agent workflows.

2190. **[chucknorris](https://github.com/pollinations/chucknorris)** - ⭐ 56
   ⚡ C̷h̷u̷c̷k̷N̷o̷r̷r̷i̷s̷ MCP server: Helping LLMs break limits. Provides enhancement prompts inspired by elder-plinius' L1B3RT4S

2191. **[anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server)** - ⭐ 56
   A Model Context Protocol (MCP) server that provides comprehensive access to LinkedIn data and functionalities using the Anysite API, enabling not only data retrieval but also robust management of user accounts.

2192. **[DecompilerServer](https://github.com/pardeike/DecompilerServer)** - ⭐ 56
   A powerful MCP (Model Context Protocol) server for decompiling and analyzing .NET assemblies, with specialized support for Unity's Assembly-CSharp.dll files. DecompilerServer provides comprehensive decompilation, search, and code analysis capabilities through a rich set of tools and APIs.

2193. **[web2mcp](https://github.com/neelsomani/web2mcp)** - ⭐ 56
   Generate an MCP for any web app

2194. **[mcp-ssh](https://github.com/shuakami/mcp-ssh)** - ⭐ 56
   🔐 SSH MCP Tool - AI-powered SSH management through MCP protocol | 基于MCP协议的SSH工具，为AI提供SSH远程操作能力

2195. **[teams-mcp](https://github.com/floriscornel/teams-mcp)** - ⭐ 56
   MCP server providing comprehensive Microsoft Teams and Graph API access for AI assistants including messaging, search, and user management.

2196. **[agenticmail](https://github.com/agenticmail/agenticmail)** - ⭐ 56
   Email & SMS infrastructure for AI agents — send and receive real email and text messages programmatically

2197. **[mcp-bridge-api](https://github.com/INQUIRELAB/mcp-bridge-api)** - ⭐ 55
   MCP Bridge is a lightweight, fast, and LLM-agnostic proxy for connecting to multiple Model Context Protocol (MCP) servers through a unified REST API. It enables secure tool execution across diverse environments like mobile, web, and edge devices. Designed for flexibility, scalability, and easy integration with any LLM backend.

2198. **[astro-mcp](https://github.com/morinokami/astro-mcp)** - ⭐ 55
   MCP server to support Astro project development

2199. **[mcp-server-kibana](https://github.com/TocharianOU/mcp-server-kibana)** - ⭐ 55
   MCP server for Kibana, Access search and manage Kibana in MCP Client.

2200. **[attio-mcp-server](https://github.com/kesslerio/attio-mcp-server)** - ⭐ 55
   Attio Model Context Protocol (MCP) server implementation

2201. **[mcp-secrets-plugin](https://github.com/amirshk/mcp-secrets-plugin)** - ⭐ 55
   Secure credential management for MCP servers leveraging system-native keychain storage across macOS, Windows, and Linux platforms

2202. **[puremd-mcp](https://github.com/puremd/puremd-mcp)** - ⭐ 55
   Unblock, scrape, and search tools for MCP clients

2203. **[trellis_blender](https://github.com/FishWoWater/trellis_blender)** - ⭐ 55
   Blender plugin for TRELLIS and TRELLIS.2 (3D AIGC Model, Text-to-3D, Image-to-3D)

2204. **[cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin)** - ⭐ 55
   MCP (Model Context Protocol) server plugin for CAP NodeJS

2205. **[powhttp-mcp](https://github.com/usestring/powhttp-mcp)** - ⭐ 55
   MCP server enabling agents to debug HTTP requests better (using powhttp)

2206. **[mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)** - ⭐ 55
   Write notes to Flomo

2207. **[p4mcp-server](https://github.com/perforce/p4mcp-server)** - ⭐ 55
   [Community Supported] Perforce P4MCP Server is a Model Context Protocol (MCP) server that integrates with the Perforce P4 version control system.

2208. **[hulunote](https://github.com/hulunote/hulunote)** - ⭐ 55
   An open-source outliner note-taking application with bidirectional linking.

2209. **[MCP_Atom_of_Thoughts](https://github.com/kbsooo/MCP_Atom_of_Thoughts)** - ⭐ 55
   Atom of Thoughts (AoT) MCP is a server that decomposes complex problems into independent atomic units of thought, using the dependencies between these units to deliver more robust reasoning and validated insights.

2210. **[python](https://github.com/mcp-auth/python)** - ⭐ 55
   🔐 Plug-and-play auth for Python MCP servers.

2211. **[godoctor](https://github.com/danicat/godoctor)** - ⭐ 55
   A Model Context Protocol server for Go developers

2212. **[vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp)** - ⭐ 55
   This project is a Model Context Protocol (MCP) server for interacting with the VRChat API.

2213. **[mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager)** - ⭐ 55
   MCP SSH Server: 37 tools for remote SSH management | Claude Code & OpenAI Codex | DevOps automation, backups, database operations, health monitoring

2214. **[rust-analyzer-mcp](https://github.com/zeenix/rust-analyzer-mcp)** - ⭐ 55
   A Model Context Protocol (MCP) server that provides integration with rust-analyzer

2215. **[nasdaq-data-link-mcp](https://github.com/stefanoamorelli/nasdaq-data-link-mcp)** - ⭐ 54
   A Nasdaq Data Link MCP (Model Context Protocol) Server

2216. **[openai-mcp-client](https://github.com/ResoluteError/openai-mcp-client)** - ⭐ 54
   A rudimentary implementation of Anthropic's Model Context Protocol with OpenAIs Model

2217. **[mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** - ⭐ 54
   A MCP (Model Context Protocol) server that provides get, send Gmails without local credential or token setup.

2218. **[minibridge](https://github.com/acuvity/minibridge)** - ⭐ 54
   Make your MCP servers secure and production ready

2219. **[mssql_mcp_server](https://github.com/JexinSam/mssql_mcp_server)** - ⭐ 54
   A Model Context Protocol (MCP) server facilitating secure interactions with MSSQL databases.

2220. **[temporal-mcp](https://github.com/Mocksi/temporal-mcp)** - ⭐ 54
   Empowering AI with Workflow Orchestration

2221. **[mcp-server-azure-ai-agents](https://github.com/farzad528/mcp-server-azure-ai-agents)** - ⭐ 54
   Model Context Protocol Servers for Azure AI Search

2222. **[ibkr-mcp-server](https://github.com/seriallazer/ibkr-mcp-server)** - ⭐ 54
   MCP Server for IBKR Client

2223. **[mcp-duckdb-memory-server](https://github.com/IzumiSy/mcp-duckdb-memory-server)** - ⭐ 54
   MCP Memory Server with DuckDB backend

2224. **[sympy-mcp](https://github.com/sdiehl/sympy-mcp)** - ⭐ 54
   A MCP server for symbolic manipulation of mathematical expressions

2225. **[swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui)** - ⭐ 54
   MCP server that can execute commands such as keyboard input and mouse movement on macOS

2226. **[mcp-docs-service](https://github.com/alekspetrov/mcp-docs-service)** - ⭐ 54
   MCP Documentation Management Service - A Model Context Protocol implementation for documentation management

2227. **[cosmotop](https://github.com/bjia56/cosmotop)** - ⭐ 54
   Multiplatform system monitoring tool using Cosmopolitan Libc

2228. **[mcp-gearbox](https://github.com/rohitsoni007/mcp-gearbox)** - ⭐ 54
   A modern desktop application for managing Model Context Protocol (MCP) servers across multiple AI agents

2229. **[talkito](https://github.com/robdmac/talkito)** - ⭐ 54
   TalkiTo lets developers interact with AI systems through speech across multiple channels (terminal, API, phone). It can be used as both a command-line tool and a Python library.

2230. **[ocaml-mcp](https://github.com/tmattio/ocaml-mcp)** - ⭐ 54
   OCaml implementation of the Model Context Protocol (MCP)

2231. **[tuisic](https://github.com/Dark-Kernel/tuisic)** - ⭐ 54
   First of its kind, A simple TUI online music streaming application written in c++ with easy vim motions, now with support for Model Context Protocol (MCP)

2232. **[rag-app-on-aws](https://github.com/genieincodebottle/rag-app-on-aws)** - ⭐ 54
   Build and deploy a full-stack RAG app on AWS with Terraform, using free tier Gemini Pro, real-time web search using Remote MCP server and Streamlit UI with token based authentication.

2233. **[mcp-things3](https://github.com/drjforrest/mcp-things3)** - ⭐ 54
   A Model Context Protocol for reading todos and writing todos and projects in the macOS app Things3 using a combination of Applescript and x-call URLs.

2234. **[Navidrome-MCP](https://github.com/Blakeem/Navidrome-MCP)** - ⭐ 54
   Analyze listening patterns, create custom playlists, discover missing albums, discover similar artists, discover radio stations, and validate radio streams using natural language.

2235. **[mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)** - ⭐ 54
   Excel MCP Server & CLI - 23 tools, 214 operations for AI-powered Excel automation via COM API

2236. **[mcp-openai](https://github.com/S1M0N38/mcp-openai)** - ⭐ 53
   🔗 MCP Client with OpenAI compatible API

2237. **[NoLLMChat](https://github.com/zrg-team/NoLLMChat)** - ⭐ 53
   Not-Only LLM Chat. An AI application that enhances creativity and user experience beyond just LLM chat. Noted: Seems it beta version of there is issue with DB please clear site Data in debug 

2238. **[gomcp](https://github.com/llmcontext/gomcp)** - ⭐ 53
   Unofficial Golang SDK for Anthropic Model Context Protocol

2239. **[awesome-remote-mcp-servers](https://github.com/sylviangth/awesome-remote-mcp-servers)** - ⭐ 53
   A curated list of Hosted & Managed Model Context Protocol (MCP) Servers accessible via a simple URL endpoint.

2240. **[client](https://github.com/php-mcp/client)** - ⭐ 53
   Core PHP implementation for the Model Context Protocol (MCP) Client

2241. **[user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp)** - ⭐ 53
   Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.

2242. **[claude-code-emacs](https://github.com/yuya373/claude-code-emacs)** - ⭐ 53
   This package provides seamless integration with Claude Code, allowing you to run AI-powered coding sessions directly in your Emacs environment.

2243. **[mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server)** - ⭐ 53
   MCP Swagger Server 将任何符合 OpenAPI/Swagger 规范的 REST API 转换为 Model Context Protocol (MCP) 格式，让 AI 助手能够理解和调用您的 API。

2244. **[Multi-Agent-System-A2A-ADK-MCP](https://github.com/RubensZimbres/Multi-Agent-System-A2A-ADK-MCP)** - ⭐ 53
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2245. **[godot-mcp](https://github.com/bradypp/godot-mcp)** - ⭐ 53
   A Model Context Protocol (MCP) server for interacting with the Godot game engine.

2246. **[cortex-scout](https://github.com/cortex-works/cortex-scout)** - ⭐ 53
   An advanced web extraction and meta-search engine for AI agents. It features native parallel searching, Human-in-the-Loop (HITL) authentication fallback, and LLM-optimized data synthesis for deep web research.

2247. **[deploystack](https://github.com/deploystackio/deploystack)** - ⭐ 53
   Open source MCP hosting - deploy MCP servers to HTTP endpoints for n8n, Dify, Voiceflow, and any MCP client.

2248. **[skrills](https://github.com/athola/skrills)** - ⭐ 53
   Coordinate skills between Codex, Copilot, and Claude Code. Validates, analyzes, and syncs skills, subagents, commands, and configuration between multiple CLIs.

2249. **[ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp)** - ⭐ 53
   An ntfy MCP server for sending/fetching ntfy notifications to self-hosted or ANY ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

2250. **[MegaMemory](https://github.com/0xK3vin/MegaMemory)** - ⭐ 53
   Persistent project knowledge graph for coding agents. MCP server with semantic search, in-process embeddings, and web explorer.

2251. **[mcp-cpp](https://github.com/Neumann-Labs/mcp-cpp)** - ⭐ 52
   A C++ SDK for the Model Context Protocol (MCP). The SDK will provide a framework for creating MCP servers and clients in C++.

2252. **[mcp-app-demo](https://github.com/pomerium/mcp-app-demo)** - ⭐ 52
   Demo application showcasing how to build and secure MCP servers and clients with Pomerium using contextual access policies.

2253. **[adx-mcp-server](https://github.com/pab1it0/adx-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server that enables AI assistants to query and analyze Azure Data Explorer databases through standardized interfaces.

2254. **[A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP)** - ⭐ 52
   Multi-Agent Systems with Google's Agent Development Kit + A2A + MCP

2255. **[context-optimizer-mcp-server](https://github.com/malaksedarous/context-optimizer-mcp-server)** - ⭐ 52
   A Model Context Protocol (MCP) server that provides context optimization tools for AI coding assistants including GitHub Copilot, Cursor AI, Claude Desktop, and other MCP-compatible assistants enabling them to extract targeted information rather than processing large terminal outputs and files wasting their context.

2256. **[adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course)** - ⭐ 52
   This project demonstrates a multi-agent system using Google's Agent Development Kit (ADK), Agent2Agent (A2A) and Model Context Protocol (MCP).  that integrates Notion for information retrieval and ElevenLabs for text-to-speech conversion.

2257. **[scheduler-mcp](https://github.com/PhialsBasement/scheduler-mcp)** - ⭐ 52
   MCP Scheduler is a task automation server that lets you schedule shell commands, API calls, AI tasks, and desktop notifications using cron expressions. Built with Model Context Protocol for seamless integration with Claude Desktop and other AI assistants.

2258. **[Memory-Plus](https://github.com/Yuchen20/Memory-Plus)** - ⭐ 52
   🧠 𝑴𝒆𝒎𝒐𝒓𝒚-𝑷𝒍𝒖𝒔 is a lightweight, local RAG memory store for MCP agents. Easily record, retrieve, update, delete, and visualize persistent "memories" across sessions—perfect for developers working with multiple AI coders (like Windsurf, Cursor, or Copilot) or anyone who wants their AI to actually remember them.

2259. **[supermcp](https://github.com/dhanababum/supermcp)** - ⭐ 52
   🚀 SuperMCP - Create multiple isolated MCP servers using a single connector. Build powerful Model Context Protocol integrations for databases (PostgreSQL, MSSQL) with FastAPI backend, React dashboard, and token-based auth. Perfect for multi-tenant apps and AI assistants.

2260. **[gdal-mcp](https://github.com/JordanGunn/gdal-mcp)** - ⭐ 52
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2261. **[mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2262. **[baba_is_eval](https://github.com/lennart-finke/baba_is_eval)** - ⭐ 52
   Claude  et al. play the brilliant puzzle title "Baba is You"

2263. **[us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)** - ⭐ 52
   The U.S. Census Bureau Data API MCP connects AI Assistants with official Census Bureau statistics.

2264. **[youtube-mcp-server](https://github.com/mourad-ghafiri/youtube-mcp-server)** - ⭐ 52
   A powerful Model Context Protocol (MCP) server for YouTube video transcription and metadata extraction.

2265. **[mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs)** - ⭐ 52
   The implementation of Model Context Protocol (MCP) server for VictoriaLogs.

2266. **[mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor)** - ⭐ 52
   MCP (Model Context Protocol) server that enables AI assistants to interact with Storybook design systems. Extract component HTML, analyze styles, and help with design system adoption and refactoring.

2267. **[langfuse-mcp](https://github.com/avivsinai/langfuse-mcp)** - ⭐ 52
   A Model Context Protocol (MCP) server for Langfuse, enabling AI agents to query Langfuse trace data for enhanced debugging and observability

2268. **[mcp-dock](https://github.com/OldJii/mcp-dock)** - ⭐ 52
   A cross-platform MCP Server manager for Cursor, Claude, Windsurf, Zed & TRAE. Features one-click installation, multi-client sync, and a curated registry of Official & Smithery servers.

2269. **[hyperterse](https://github.com/hyperterse/hyperterse)** - ⭐ 52
   The MCP framework. Connect your data to your agents.

2270. **[mcp-mermaid-validator](https://github.com/rtuin/mcp-mermaid-validator)** - ⭐ 51
   A Model Context Protocol server that validates and renders Mermaid diagrams.

2271. **[gomcp](https://github.com/localrivet/gomcp)** - ⭐ 51
   gomcp provides a Go implementation of the Model Context Protocol (MCP), enabling communication between language models/agents and external tools or resources via a standardized protocol.

2272. **[qu3-app](https://github.com/qu3ai/qu3-app)** - ⭐ 51
   Quantum-proof MCP Server and Client Interactions

2273. **[mcp-client](https://github.com/rakesh-eltropy/mcp-client)** - ⭐ 51

2274. **[go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql)** - ⭐ 51
   Zero burden, ready-to-use Model Context Protocol (MCP) server for interacting with MySQL and automation. No Node.js or Python environment needed.

2275. **[mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit)** - ⭐ 51
   A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.

2276. **[gdal-mcp](https://github.com/Wayfinder-Foundry/gdal-mcp)** - ⭐ 51
   Model Context Protocol server that packages GDAL-style geospatial workflows through Python-native libraries (Rasterio, GeoPandas, PyProj, etc.) to give AI agents catalog discovery, metadata intelligence, and raster/vector processing with built-in reasoning guidance and reference resources.

2277. **[whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp)** - ⭐ 51
   MCP Server for whois lookups.

2278. **[tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp)** - ⭐ 51
   A Model Context Protocol (MCP) server for Tripadvisor Content API.  This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search for travel destinations and experiences.

2279. **[pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** - ⭐ 51
   PagerDuty's official local MCP (Model Context Protocol) server which provides tools to interact with your PagerDuty account directly from your MCP-enabled client.

2280. **[mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server)** - ⭐ 51
   MCP server connecting AI assistants with Jira & Confluence for smart project management.

2281. **[kroger-mcp](https://github.com/CupOfOwls/kroger-mcp)** - ⭐ 51
   A FastMCP server that provides AI assistants like Claude with access to Kroger's grocery shopping functionality through the Model Context Protocol (MCP). This server enables AI assistants to find stores, search products, manage shopping carts, and access Kroger's comprehensive grocery data via the kroger-api python library.

2282. **[mcp-kubernetes](https://github.com/Azure/mcp-kubernetes)** - ⭐ 51
   A Model Context Protocol (MCP) server that enables AI assistants to interact with Kubernetes clusters. It serves as a bridge between AI tools (like Claude, Cursor, and GitHub Copilot) and Kubernetes

2283. **[ShadowCrawl](https://github.com/DevsHero/ShadowCrawl)** - ⭐ 51
   🥷 The FREE, Sovereign alternative to Firecrawl & Tavily. Pure Rust Stealth Scraper + Built-in God-Tier Meta-Search for AI Agents. Bypass Cloudflare & DataDome via HITL. Zero-bloat, ultra-clean LLM data. 99.99% Success Rate. 🦀

2284. **[rs-utcp](https://github.com/universal-tool-calling-protocol/rs-utcp)** - ⭐ 51
   Official Rust implementation of the UTCP

2285. **[Skills-ContextManager](https://github.com/One-Man-Company/Skills-ContextManager)** - ⭐ 51
   A self-hosted web application for managing AI skills, workflows, and contexts with full MCP (Model Context Protocol) integration. Organize, manage, and dynamically load specialized knowledge bases into any AI Agent just by toggling your Skills On/Off in simple local hosted WEB UI.

2286. **[hmr](https://github.com/promplate/hmr)** - ⭐ 51
   Real hot-module reload for Python—side effects handled reactively. https://py3.online/hmr

2287. **[gemini-cloud-assist-mcp](https://github.com/GoogleCloudPlatform/gemini-cloud-assist-mcp)** - ⭐ 51
   An MCP Server for Gemini Cloud Assist; provides tools to assist with your tasks on GCP

2288. **[clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server)** - ⭐ 51
   MCP server for the ClinicalTrials.gov v2 API. Allow LLMs to search trials, retrieve study details, compare studies, analyze trends, and match patients to eligible trials.

2289. **[sugar](https://github.com/roboticforce/sugar)** - ⭐ 51
   🍰 Sugar - The autonomous layer for AI coding agents

2290. **[Perigon.CLI](https://github.com/AterDev/Perigon.CLI)** - ⭐ 50
   This is a tool that helps you quickly build backend services based on Asp.Net Core and EF Core. It provides command line, WebUI and IDE MCP support. In a well-designed project architecture that has been put into practice, code generation and LLM technology are used to reduce various template codes and greatly improve development efficiency!

2291. **[AgentDNS-Node](https://github.com/jsjfai/AgentDNS-Node)** - ⭐ 50
   AgentDNS·Node makes it easy to manage and scale multiple MCP (Model Context Protocol) servers by organizing them into flexible Streamable HTTP (SSE) endpoints—supporting access to all servers, individual servers, or logical server groups.

2292. **[mcp-guard](https://github.com/General-Analysis/mcp-guard)** - ⭐ 50
   MCP Guard secures your MCP client from prompt injection attacks and more.

2293. **[ScreenPilot](https://github.com/Mtehabsim/ScreenPilot)** - ⭐ 50
   Tool that allows the AI to control your device in the same way you do, enabling automation for everything!

2294. **[mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal)** - ⭐ 50
   TS based companion MCP server for the Drupal MCP module that works with the STDIO transport.

2295. **[create-mcp](https://github.com/zueai/create-mcp)** - ⭐ 50
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

2296. **[mcpo_docker_use](https://github.com/flyfox666/mcpo_docker_use)** - ⭐ 50
   An example Docker image for mcpo（with npm,curl,nodejs,uv Pre-Built;Pre-Built MCP:amap;baidumap;server-brave-search; tavily;fetch）, a tool that exposes MCP (Model Context Protocol) servers as OpenAPI-compatible HTTP endpoints for OpenWebUI.

2297. **[AI-Cursor-Scraping-Assistant](https://github.com/TheWebScrapingClub/AI-Cursor-Scraping-Assistant)** - ⭐ 50
   A powerful tool that leverages Cursor AI and MCP (Model Context Protocol) to easily generate web scrapers for various types of websites.

2298. **[mcp-oauth-gateway](https://github.com/atrawog/mcp-oauth-gateway)** - ⭐ 50
   An OAuth 2.1 Authorization Server that adds authentication to any MCP (Model Context Protocol) server without code modification.

2299. **[mcp-server](https://github.com/inkdropapp/mcp-server)** - ⭐ 50
   Inkdrop Model Context Protocol Server

2300. **[model-context-protocol-rb](https://github.com/dickdavis/model-context-protocol-rb)** - ⭐ 50
   An implementation of the Model Context Protocol in Ruby.

2301. **[hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp)** - ⭐ 50
   A Model Context Protocol server for integrating HackMD's note-taking platform with AI assistants.

2302. **[semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server)** - ⭐ 50
   🔍 This project implements a Model Context Protocol (MCP) server for interacting with the Semantic Scholar API. It provides tools for searching papers, retrieving paper and author details, and fetching citations and references.

2303. **[mcp](https://github.com/getAlby/mcp)** - ⭐ 50
   Connect a bitcoin lightning wallet to your LLM using Nostr Wallet Connect and Model Context Protocol

2304. **[matlab-mcp-server](https://github.com/subspace-lab/matlab-mcp-server)** - ⭐ 50
   Matlab MCP Server in python

2305. **[mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)** - ⭐ 50
   Node.js/TypeScript MCP server for Atlassian Confluence. Provides tools enabling AI systems (LLMs) to list/get spaces & pages (content formatted as Markdown) and search via CQL. Connects AI seamlessly to Confluence knowledge bases using the standard MCP interface.

2306. **[activitywatch-mcp-server](https://github.com/8bitgentleman/activitywatch-mcp-server)** - ⭐ 50
   Model Context Protocol server for ActivityWatch time tracking data

2307. **[gimp-mcp](https://github.com/maorcc/gimp-mcp)** - ⭐ 50
   GIMP MCP server

2308. **[pasal](https://github.com/ilhamfp/pasal)** - ⭐ 50
   The first open, AI-native Indonesian legal platform. MCP server + web app giving Claude grounded access Indonesian laws.

2309. **[n8n-workflow-builder-mcp](https://github.com/ifmelate/n8n-workflow-builder-mcp)** - ⭐ 49
   MCP server that allow LLM in agent mode builds n8n workflows for you

2310. **[rulego-server](https://github.com/rulego/rulego-server)** - ⭐ 49
   A lightweight dependency-free workflow automation platform. Supports iPaaS, stream computing, MCP, and AI capabilities. 

2311. **[oatpp-mcp](https://github.com/oatpp/oatpp-mcp)** - ⭐ 49
   Anthropic’s Model Context Protocol implementation for Oat++

2312. **[linux-do-mcp](https://github.com/Pleasurecruise/linux-do-mcp)** - ⭐ 49
   A MCP Server For LINUX DO community

2313. **[Koppla](https://github.com/ruudmens/Koppla)** - ⭐ 49
   A Model-Context-Protocol (MCP) Server for Active Directory

2314. **[agent-os](https://github.com/imran-siddique/agent-os)** - ⭐ 49
   A Safety-First Kernel for Autonomous AI Agents - POSIX-inspired primitives with 0% policy violation guarantee

2315. **[1xn-vmcp](https://github.com/1xn-labs/1xn-vmcp)** - ⭐ 49
   vMCP - Virtual Model Context Protocol

2316. **[cinema4d-mcp](https://github.com/ttiimmaacc/cinema4d-mcp)** - ⭐ 49
   Cinema 4D plugin integrating Claude AI for prompt-driven 3D modeling, scene creation, and manipulation.

2317. **[mealie-mcp-server](https://github.com/rldiao/mealie-mcp-server)** - ⭐ 49
   MCP server that exposes Mealie APIs to MCP clients such as Claude Desktop

2318. **[image-gen-mcp](https://github.com/lansespirit/image-gen-mcp)** - ⭐ 49
   An MCP server that integrates with gpt-image-1 & Gemini imagen4 model for text-to-image generation services

2319. **[mcp](https://github.com/goplus/mcp)** - ⭐ 49
   A XGo implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.

2320. **[crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp)** - ⭐ 49
   Crawlbase MCP Server connects AI agents and LLMs with real-time web data. It powers Claude, Cursor, and Windsurf integrations with battle-tested web scraping, JavaScript rendering, and anti-bot protection enabling structured, live data inside your AI workflows.

2321. **[mcp-amadeus](https://github.com/donghyun-chae/mcp-amadeus)** - ⭐ 49
   Amadeus MCP(Model Context Protocol) Server

2322. **[ai-humanizer-mcp-server](https://github.com/Text2Go/ai-humanizer-mcp-server)** - ⭐ 49
   A powerful Model Context Protocol (MCP) server that helps refine AI-generated content to sound more natural and human-like. Built with advanced AI detection and text enhancement capabilities.

2323. **[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)** - ⭐ 49
   A Model Context Protocol (MCP) server that provides conversational interface for the exploration and analysis of RDF (Turtle) based Knowledge Graph in Local File mode or SPARQL Endpoint mode.

2324. **[mcp-tts](https://github.com/blacktop/mcp-tts)** - ⭐ 49
   MCP Server for Text to Speech

2325. **[sample-agentic-ai-web](https://github.com/aws-samples/sample-agentic-ai-web)** - ⭐ 49
   This project demonstrates how to use AWS Bedrock with Anthropic Claude and Amazon Nova models to create a web automation assistant with tool use, human-in-the-loop interaction, and vision capabilities.

2326. **[crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server)** - ⭐ 49
   🕷️ A lightweight Model Context Protocol (MCP) server that exposes Crawl4AI web scraping and crawling capabilities as tools for AI agents.  Similar to Firecrawl's API but self-hosted and free. Perfect for integrating web scraping into your AI workflows with OpenAI Agents SDK, Cursor, Claude Code, and other MCP-compatible tools.

2327. **[mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify)** - ⭐ 49
   Send system notification when Agent task is done.

2328. **[MayaMCP](https://github.com/PatrickPalmer/MayaMCP)** - ⭐ 49
   Model Context Protocol (MCP) server implementation for Autodesk Maya

2329. **[caldav-mcp](https://github.com/dominik1001/caldav-mcp)** - ⭐ 48
   A CalDAV client using Model Context Protocol (MCP) to expose calendar operations as tools for AI assistants.

2330. **[auto-MCP-client](https://github.com/Chen-speculation/auto-MCP-client)** - ⭐ 48
   A Go library implementation of the Model Controller Protocol (MCP). This library allows developers to easily parse MCP service configurations, generate corresponding MCP clients, and integrate them as callable tools within LLM agent systems. Focuses on providing reusable Go packages for building MCP-enabled applications.

2331. **[mcp-client-demo](https://github.com/KelvinQiu802/mcp-client-demo)** - ⭐ 48

2332. **[vchart-mcp-server](https://github.com/VisActor/vchart-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for the @visactor/vchart that enables AI assistants to generate interactive charts and visualizations.

2333. **[mcp-server-chart-minio](https://github.com/zaizaizhao/mcp-server-chart-minio)** - ⭐ 48
   mcp-server-chart私有化部署方案

2334. **[mcp-gitee](https://github.com/oschina/mcp-gitee)** - ⭐ 48
   mcp-gitee is a Model Context Protocol (MCP) server implementation for Gitee. It provides a set of tools that interact with Gitee's API, allowing AI assistants to manage repository, issues, pull requests, etc.

2335. **[lakevision](https://github.com/lakevision-project/lakevision)** - ⭐ 48
   Lakevision is a tool which provides insights into your Apache Iceberg based Data Lakehouse.

2336. **[calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server that provides Claude with advanced mathematical calculation capabilities

2337. **[mcp-dap-server](https://github.com/go-delve/mcp-dap-server)** - ⭐ 48
   MCP server to communicate with DAP servers allowing AI Agents the ability to debug live programs.

2338. **[mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers)** - ⭐ 48
   🔒 Reference MCP servers that demo how authentication works with the current Model Context Protocol spec.

2339. **[buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server)** - ⭐ 48
   Official MCP Server for Buildkite.

2340. **[shotgrid-mcp-server](https://github.com/loonghao/shotgrid-mcp-server)** - ⭐ 48
   A Model Context Protocol (MCP) server for Autodesk ShotGrid/Flow Production Tracking (FPT) with comprehensive CRUD operations and data management capabilities.

2341. **[APIWeaver](https://github.com/GongRzhe/APIWeaver)** - ⭐ 48
   A FastMCP server that dynamically creates MCP (Model Context Protocol) servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.

2342. **[vikunja-mcp](https://github.com/democratize-technology/vikunja-mcp)** - ⭐ 48
   Model Context Protocol server for Vikunja task management. Enables AI assistants to interact with Vikunja instances via MCP.

2343. **[mcp-metabase-server](https://github.com/easecloudio/mcp-metabase-server)** - ⭐ 48
   A comprehensive MCP server for Metabase with 70+ tools.

2344. **[globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server)** - ⭐ 48
   Remote MCP server that gives LLMs access to run network commands

2345. **[mcp_demo](https://github.com/Ming-jiayou/mcp_demo)** - ⭐ 47
   A simple example of building an MCP client using C#.

2346. **[kuon](https://github.com/lissettecarlr/kuon)** - ⭐ 47
   久远：一个开发中的大模型语音助手，当前关注易用性，简单上手，支持对话选择性记忆和Model Context Protocol (MCP)服务。 KUON:A large language model-based voice assistant under development, currently focused on ease of use and simple onboarding. It supports selective memory in conversations and the Model Context Protocol (MCP) service.

2347. **[claude-mcp-setup](https://github.com/patruff/claude-mcp-setup)** - ⭐ 47
   Easy setup script for Anthropic Claude Model Context Protocol (MCP) servers on Windows

2348. **[spec-coding-mcp](https://github.com/feiyun0112/spec-coding-mcp)** - ⭐ 47
   Transform feature ideas into production-ready code through systematic Spec-Driven Development 通过系统化的**规格驱动开发**，将功能想法转化为可投入生产的代码

2349. **[codex-mcp-go](https://github.com/w31r4/codex-mcp-go)** - ⭐ 47
   codex-mcp-go is a Go-based MCP (Model Context Protocol) server that serves as a bridge for Codex CLI, enabling various AI coding assistants (such as Claude Code, Roo Code, KiloCode, etc.) to seamlessly collaborate with Codex.

2350. **[mcp](https://github.com/40ants/mcp)** - ⭐ 47
   40ANTS-MCP is a framework for building Model Context Protocol servers in Common Lisp

2351. **[mcp-youtube](https://github.com/adhikasp/mcp-youtube)** - ⭐ 47
   Model Context Protocol to fetch youtube transcript

2352. **[Aspire.MCP.Sample](https://github.com/elbruno/Aspire.MCP.Sample)** - ⭐ 47
   Sample MCP Server and MCP client with Aspire

2353. **[pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp)** - ⭐ 47
   This is a Model Context Protocol (MCP) server implemented in Go, providing a tool to analyze Go pprof performance profiles.

2354. **[gnome-mcp-server](https://github.com/bilelmoussaoui/gnome-mcp-server)** - ⭐ 47
   Grant the AI octopus access to a portion of your desktop

2355. **[dremio-mcp](https://github.com/dremio/dremio-mcp)** - ⭐ 47
   Dremio MCP server

2356. **[advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** - ⭐ 47
   An advanced MCP server for Home Assistant. 🔋 Batteries included.

2357. **[Reversecore_MCP](https://github.com/sjkim1127/Reversecore_MCP)** - ⭐ 47
   A security-first MCP server empowering AI agents to orchestrate Ghidra, Radare2, and YARA for automated reverse engineering.

2358. **[bookstack-mcp-server](https://github.com/pnocera/bookstack-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) server providing full access to BookStack's knowledge management capabilities

2359. **[ns-mcp-server](https://github.com/r-huijts/ns-mcp-server)** - ⭐ 47
   A Model Context Protocol (MCP) server that provides access to NS (Dutch Railways) travel information through Claude AI. This server enables Claude to fetch real-time train travel information and disruptions using the official Dutch NS API.

2360. **[mcp-filter](https://github.com/pro-vi/mcp-filter)** - ⭐ 47
   A proxy MCP (Model Context Protocol) server that filters the upstream tool surface to just the tools you need.

2361. **[codex-specialized-subagents](https://github.com/leonardsellem/codex-specialized-subagents)** - ⭐ 47
   MCP server that lets Codex delegate to isolated codex exec sub-agents, selecting repo+global skills automatically

2362. **[meme-mcp](https://github.com/haltakov/meme-mcp)** - ⭐ 47
   A simple Model Context Protocol (MCP) server for generating memes using the ImgFlip API

2363. **[langchaingo-mcp-adapter](https://github.com/i2y/langchaingo-mcp-adapter)** - ⭐ 47
   A Go adapter that bridges LangChain Go tools with Model Context Protocol (MCP) servers.

2364. **[mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema)** - ⭐ 47
   OpenAPI Schema Model Context Protocol Server

2365. **[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw)** - ⭐ 47
   Curated awesome list for OpenClaw (formerly Moltbot/Clawdbot): skills, plugins, memory systems, MCP tools, deployment stacks, ecosystem platforms, and developer tooling.

2366. **[mcp-ssh](https://github.com/AiondaDotCom/mcp-ssh)** - ⭐ 47
   A Model Context Protocol (MCP) server for managing and controlling SSH connections.

2367. **[langchain-mcp-client](https://github.com/guinacio/langchain-mcp-client)** - ⭐ 47
   This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and interacting with them using different LLM providers (OpenAI, Anthropic, Google, Ollama).

2368. **[Claude-Deep-Research](https://github.com/mcherukara/Claude-Deep-Research)** - ⭐ 47
   An MCP (Model Context Protocol) server that enables comprehensive research capabilities for Claude

2369. **[lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp)** - ⭐ 47
   A Model Context Protocol (MCP) server implementation for LunchMoney, providing programmatic access to personal finance management through LunchMoney's API.

2370. **[MDB-MCP](https://github.com/smadi0x86/MDB-MCP)** - ⭐ 47
   Multi Debugger MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2371. **[mcp-zen](https://github.com/199-mcp/mcp-zen)** - ⭐ 47
   Enhanced Zen MCP Server with 'zen' default tool and improvements

2372. **[eliza-plugin-mcp](https://github.com/fleek-platform/eliza-plugin-mcp)** - ⭐ 46
   ElizaOS plugin allowing agents to connect to MCP servers

2373. **[Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for interacting with Home Assistant. This server provides tools to control and monitor your Home Assistant devices through MCP-enabled applications.

2374. **[mcp-lite-dev](https://github.com/datawhalechina/mcp-lite-dev)** - ⭐ 46
   共学《MCP极简开发》项目代码

2375. **[shadowgit-mcp](https://github.com/blade47/shadowgit-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server that provides AI assistants with secure, read-only access to your ShadowGit repositories. This enables powerful debugging and code analysis capabilities by giving AI access to your project's fine-grained git history.

2376. **[steel-mcp-server](https://github.com/steel-dev/steel-mcp-server)** - ⭐ 46
   MCP Server for interacting with a Steel web browser

2377. **[tiger-slack](https://github.com/timescale/tiger-slack)** - ⭐ 46
   Real-time Slack ingest and MCP server to power your agentic Slack bots

2378. **[modular-mcp](https://github.com/d-kimuson/modular-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multiple MCP servers by grouping them and loading tool schemas on-demand.

2379. **[abaqus-mcp-server](https://github.com/jianzhichun/abaqus-mcp-server)** - ⭐ 46
   An MCP (Model Context Protocol) server designed to interact with an already running Abaqus/CAE Graphical User Interface (GUI). It allows for the execution of Python scripts within the Abaqus environment and retrieval of messages from the Abaqus message log/area, all through MCP tools.

2380. **[esa-mcp-server](https://github.com/esaio/esa-mcp-server)** - ⭐ 46
   esa.io の公式 MCP(Model Context Protocol)サーバー(STDIO Transport版)

2381. **[mcp-starter-template](https://github.com/StevenStavrakis/mcp-starter-template)** - ⭐ 46
   An opinionated starter template for making Model Context Protocol (MCP) servers

2382. **[flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server)** - ⭐ 46
   Model Context Protocol server for Flight Tracking

2383. **[davinci-resolve-mcp](https://github.com/apvlv/davinci-resolve-mcp)** - ⭐ 46
   A Model Context Protocol (MCP) server for interacting with DaVinci Resolve and Fusion

2384. **[mcp-toolbox-sdk-go](https://github.com/googleapis/mcp-toolbox-sdk-go)** - ⭐ 46
   Go SDK for interacting with the MCP Toolbox for Databases.

2385. **[mcp-mail](https://github.com/shuakami/mcp-mail)** - ⭐ 46
   📧 MCP Mail Tool - AI-powered email management tool | 基于 MCP 的智能邮件管理工具

2386. **[mcpcat-python-sdk](https://github.com/MCPCat/mcpcat-python-sdk)** - ⭐ 46
   MCPcat is an analytics platform for MCP server owners 🐱.

2387. **[thoughtbox](https://github.com/Kastalien-Research/thoughtbox)** - ⭐ 46
   Thoughtbox is a Git-inspired workspace for Agent Teams.

2388. **[metabase-mcp](https://github.com/jerichosequitin/metabase-mcp)** - ⭐ 46
   A high-performance Model Context Protocol server for AI integration with Metabase analytics platforms. Features response optimization, robust error handling, and comprehensive data access tools. Featured on Claude.

2389. **[luma-mcp](https://github.com/JochenYang/luma-mcp)** - ⭐ 46
   Multi-Model Visual Understanding MCP Server, GLM-4.6V, DeepSeek-OCR (free), and Qwen3-VL-Flash. Provide visual processing capabilities for AI coding models that do not support image understanding.多模型视觉理解MCP服务器，GLM-4.6V、DeepSeek-OCR（免费）和Qwen3-VL-Flash等。为不支持图片理解的 AI 编码模型提供视觉处理能力。

2390. **[ai-software-architect](https://github.com/codenamev/ai-software-architect)** - ⭐ 46
   AI-powered architecture documentation framework with ADRs, reviews, and pragmatic mode. Now available as Claude Code Plugin for easiest installation.

2391. **[youtrack-mcp](https://github.com/devstroop/youtrack-mcp)** - ⭐ 46
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2392. **[aivectormemory](https://github.com/Edlineas/aivectormemory)** - ⭐ 46
   aivectormemory 是一款基于 Model Context Protocol (MCP) 开发的轻量级内存管理工具。它专门为 Claude、OpenCode、Cursor 和 主流IDE 编程工具设计，通过向量数据库技术解决 AI 在不同对话会话中「健忘」的问题。aivectormemory: A lightweight MCP Server enabling persistent, cross-session memory for AI-powered IDEs via vector search.

2393. **[mcp-sdk](https://github.com/symfony/mcp-sdk)** - ⭐ 45
   Model Context Protocol SDK for Client and Server applications in PHP

2394. **[mcp-made-simple](https://github.com/chongdashu/mcp-made-simple)** - ⭐ 45
   Model Context Protocol (MCP) Made Simple - Code for the tutorial series - focusing on practical ways to understand and use MCP

2395. **[Serper-search-mcp](https://github.com/NightTrek/Serper-search-mcp)** - ⭐ 45
   Un-official Serper Google search server for Cline and other MCP clients

2396. **[excalidraw-mcp](https://github.com/i-tozer/excalidraw-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server for Excalidraw - Work in Progress

2397. **[marinade-finance-mcp-server](https://github.com/lorine93s/marinade-finance-mcp-server)** - ⭐ 45
   Marinade Finance MCP Server is an MCP server specifically designed for the Marinade Finance.

2398. **[vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation. This project enables developers to ask questions about the Vercel AI SDK and receive accurate, contextualized responses based on the official documentation.

2399. **[awesome-mcp-security](https://github.com/AIM-Intelligence/awesome-mcp-security)** - ⭐ 45
   Security Threats related with MCP (Model Context Protocol), MCP Servers and more

2400. **[dataproduct-mcp](https://github.com/entropy-data/dataproduct-mcp)** - ⭐ 45
   A Model Context Protocol (MCP) server for discovering data products and requesting access in Data Mesh Manager, and executing queries on the data platform to access business data.

2401. **[lisply-mcp](https://github.com/gornskew/lisply-mcp)** - ⭐ 45
   Model Context Protocol (MCP) server to manage and talk to compliant "Lisply" lisp-speaking backend services

2402. **[js](https://github.com/mcp-auth/js)** - ⭐ 45
   🔐 Plug-and-play auth for Node.js MCP servers.

2403. **[mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)** - ⭐ 45
   Real-time stock API with Python, MCP server example, yfinance stock analysis dashboard

2404. **[inAI-wiki](https://github.com/inai-sandy/inAI-wiki)** - ⭐ 45
   🌍 The open-source Wikipedia of AI — 2M+ apps, agents, LLMs & datasets. Updated daily with tools, tutorials & news.

2405. **[world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)** - ⭐ 45
   An implementation of the Model Context Protocol for the World Bank open data API

2406. **[fossil-mcp](https://github.com/yfedoseev/fossil-mcp)** - ⭐ 45
   The code quality toolkit for the agentic AI era. Find dead code, clones, and scaffolding across 15 languages. MCP server + CLI.

2407. **[mcp_server_filesystem](https://github.com/MarcusJellinghaus/mcp_server_filesystem)** - ⭐ 45
   MCP File System Server: A secure Model Context Protocol server that provides file operations for AI assistants. Enables Claude and other assistants to safely read, write, and list files in a designated project directory with robust path validation and security controls.

2408. **[codebadger](https://github.com/Lekssays/codebadger)** - ⭐ 45
   A containerized Model Context Protocol (MCP) server providing static code analysis using Joern's Code Property Graph (CPG) with support for Java, C/C++, JavaScript, Python, Go, Kotlin, C#, Ghidra, Jimple, PHP, Ruby, and Swift.

2409. **[mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server)** - ⭐ 45
   Implementation of Model Context Protocol server for Mailgun APIs

2410. **[altium-mcp](https://github.com/coffeenmusic/altium-mcp)** - ⭐ 45
   Altium Model Context Protocol server and Altium API script

2411. **[ainovelprompter](https://github.com/danielsobrado/ainovelprompter)** - ⭐ 45
   Create the prompts you need to write your Novel using AI

2412. **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** - ⭐ 45
   MCP server that enables AI agents to perform comprehensive web audits using Google Lighthouse with 13+ tools for performance, accessibility, SEO, and security analysis.

2413. **[RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)** - ⭐ 45
   Deep Research & Competitor Analysis MCP for Claude & Cursor. No API Keys. Features: Web Search, Social Media (Reddit/HN), Trends & OCR.

2414. **[gno](https://github.com/gmickel/gno)** - ⭐ 44
   Local AI-powered document search and editing with first-in-class hybrid retrieval, LLM answers, WebUI, REST API and MCP support for AI clients.

2415. **[moondream-mcp](https://github.com/ColeMurray/moondream-mcp)** - ⭐ 44
   Moondream MCP Server in Python

2416. **[vue-mcp-next](https://github.com/tuskermanshu/vue-mcp-next)** - ⭐ 44
   Vue MCP Next bridges AI agents with Vue.js applications, enabling real-time component state inspection and   manipulation through the Model Context Protocol. Built for AI-assisted development workflows

2417. **[spring-ai-mcp-client](https://github.com/ogulcanarbc/spring-ai-mcp-client)** - ⭐ 44
   mcp client application that utilizes spring ai. it integrates with mcp protocol-supported servers to enable ai-powered chat interactions.

2418. **[Claude-Project-Coordinator](https://github.com/M-Pineapple/Claude-Project-Coordinator)** - ⭐ 44
   Claude Project Coordinator is a Swift-powered MCP (Model Context Protocol) server designed to streamline multi-project Xcode development. It lets you track project status, auto-detect frameworks, search code patterns, and maintain a structured development knowledge base — all locally, with Claude Desktop as your assistant.

2419. **[rhinoMcpServer](https://github.com/always-tinkering/rhinoMcpServer)** - ⭐ 44
   RhinoMCP connects Rhino to Claude AI through the Model Context Protocol (MCP), enabling AI-assisted 3D modeling and architectural design.

2420. **[mcp-typescribe](https://github.com/yWorks/mcp-typescribe)** - ⭐ 44
   An MCP server implementation enabling LLMs to work with new APIs and frameworks

2421. **[code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp)** - ⭐ 44
   MCP server for generating beautiful code screenshots directly from Claude

2422. **[scaled-mcp](https://github.com/Traego/scaled-mcp)** - ⭐ 44
   ScaledMCP is a horizontally scalabled MCP and A2A Server. You know, for AI.

2423. **[contentful-mcp-server](https://github.com/contentful/contentful-mcp-server)** - ⭐ 44
   MCP (Model Context Protocol) server for the Contentful Management API

2424. **[mcp-container-ts](https://github.com/Azure-Samples/mcp-container-ts)** - ⭐ 44
   This is a quick start guide that provides the basic building blocks to set up a remote Model Context Protocol (MCP) server using Azure Container Apps. The MCP server is built using Node.js and TypeScript, and it can be used to run various tools and services in a serverless environment.

2425. **[python-notebook-mcp](https://github.com/UsamaK98/python-notebook-mcp)** - ⭐ 44
   Lightweight Python Notebook MCP - Enable AI assistants to create, edit, and view Jupyter notebooks via Model Context Protocol

2426. **[dynamic-fastmcp](https://github.com/ragieai/dynamic-fastmcp)** - ⭐ 44
   Dynamic FastMCP extends the Model Context Protocol Python server with context-aware tools that adapt their behavior and descriptions based on user, tenant, and request context.

2427. **[mcp-agents-hub](https://github.com/mcp-agents-ai/mcp-agents-hub)** - ⭐ 44
   The open-source ecosystem for building, discovering, and deploying Model Context Protocol servers and clients.

2428. **[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** - ⭐ 44
   🔍Model Context Protocol (MCP) server for Apache Airflow API integration. Provides comprehensive tools for managing Airflow clusters including service operations, configuration management, status monitoring, and request tracking.

2429. **[wechat-mcp](https://github.com/JettChenT/wechat-mcp)** - ⭐ 44
   Model Context Protocol for WeChat

2430. **[devcontext](https://github.com/aiurda/devcontext)** - ⭐ 44
   DevContext is a cutting-edge Model Context Protocol (MCP) server designed to provide developers with continuous, project-centric context awareness. Unlike traditional context systems, DevContext continuously learns from and adapts to your development patterns and delivers highly relevant context providing a deeper understanding of your codebase.

2431. **[smythos-studio](https://github.com/SmythOS/smythos-studio)** - ⭐ 44
   SmythOS Studio: Open-Source Visual AI Agent Builder and deployable runtime stack from SmythOS. Start with an intuitive drag-and-drop workspace, extend with custom code, and deploy your agents anywhere — local, cloud, or edge — with full governance and control.

2432. **[discourse-mcp](https://github.com/discourse/discourse-mcp)** - ⭐ 44
   MCP client for Discourse sites

2433. **[chrome-debug-mcp](https://github.com/robertheadley/chrome-debug-mcp)** - ⭐ 44
   An MCP server to allow you to debug webpages using LLMs

2434. **[mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger)** - ⭐ 44
   A Model Context Protocol server for interacting with Ledger CLI, a powerful double-entry accounting system. This server enables Large Language Models to query and analyze financial data through a standardized interface, making it easy for AI assistants to help with financial reporting, budget analysis, and accounting tasks.

2435. **[beemcp](https://github.com/OkGoDoIt/beemcp)** - ⭐ 44
   BeeMCP: an unofficial Model Context Protocol (MCP) server that connects your Bee wearable lifelogger to AI via the Model Context Protocol

2436. **[kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server)** - ⭐ 44
   A Model Context Protocol (MCP) server for Apache Kafka implemented in Go, leveraging franz-go and mcp-go.

2437. **[mcp-codestyle-server](https://github.com/itxaiohanglover/mcp-codestyle-server)** - ⭐ 44
   MCP Codestyle Server 是一个基于 Spring AI 实现的 Model Context Protocol (MCP) 服务器，为 IDE 和 AI 代理提供代码模板搜索和检索工具。该服务从本地缓存查找模板，并在缺失时自动从远程仓库下载元数据和文件进行修复。

2438. **[sharepoint-mcp](https://github.com/DEmodoriGatsuO/sharepoint-mcp)** - ⭐ 44
   SharePoint MCP (Model Context Protocol) - A SharePoint connector for LLM applications. Access SharePoint documents and lists through Microsoft Graph API.

2439. **[osm-mcp](https://github.com/wiseman/osm-mcp)** - ⭐ 44
   Model Context Protocol server for OpenStreetMap data

2440. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** - ⭐ 44
   A Model Context Protocol (MCP) server for OpenSCAD 3D modeling and rendering

2441. **[imap-mcp](https://github.com/non-dirty/imap-mcp)** - ⭐ 44
   IMAP Model Context Protocol server for interactive email processing

2442. **[kanban-mcp](https://github.com/bradrisse/kanban-mcp)** - ⭐ 44
   MCP Kanban is a specialized middleware designed to facilitate interaction between Large Language Models (LLMs) and Planka, a Kanban board application. It serves as an intermediary layer that provides LLMs with a simplified and enhanced API to interact with Planka's task management system.

2443. **[reaper-reapy-mcp](https://github.com/wegitor/reaper-reapy-mcp)** - ⭐ 44
   Reaper and MCP or AI integration A Python application for controlling REAPER Digital Audio Workstation (DAW) using the MCP(Model context protocol).

2444. **[generic-mcp-client-chat](https://github.com/rom1504/generic-mcp-client-chat)** - ⭐ 43
   Generic MCP Client to use any MCP tool in a chat

2445. **[thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp)** - ⭐ 43
   This MCP server integrates ThingsPanel IoT platform with AI models like Claude, GPT, and others that support the Model Context Protocol. 

2446. **[MCPP.Net](https://github.com/xuzeyu91/MCPP.Net)** - ⭐ 43
   Model Context Protocol Platform，统一管理你的MCP服务

2447. **[mcp-playground](https://github.com/Elkhn/mcp-playground)** - ⭐ 43
   A Streamlit-based chat app for LLMs with plug-and-play tool support via Model Context Protocol (MCP), powered by LangChain, LangGraph, and Docker.

2448. **[LLaMa-MCP-Streamlit](https://github.com/Nikunj2003/LLaMa-MCP-Streamlit)** - ⭐ 43
   AI assistant built with Streamlit, NVIDIA NIM (LLaMa 3.3:70B) / Ollama, and Model Control Protocol (MCP).

2449. **[pdf-mcp](https://github.com/saury1120/pdf-mcp)** - ⭐ 43
   一个强大的 PDF 处理 MCP（Model Context Protocol）服务，提供全面的 PDF 文档分析功能

2450. **[mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi)** - ⭐ 43
   A Model Context Protocol server implementation for Kagi's API

2451. **[any2markdown](https://github.com/WW-AI-Lab/any2markdown)** - ⭐ 43
   一个高性能的文档转换服务器，同时支持 Model Context Protocol (MCP) 和 RESTful API 接口。将 PDF、Word 和 Excel 文档转换为 Markdown 格式，具备图片提取、页眉页脚移除和批量处理等高级功能

2452. **[mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema)** - ⭐ 43
   GraphQL Schema Model Context Protocol Server

2453. **[openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that provides JSON-RPC functionality through OpenRPC.

2454. **[mcp-openmsx](https://github.com/nataliapc/mcp-openmsx)** - ⭐ 43
   A Model Context Protocol (MCP) server for automating openMSX emulator instances. This server provides comprehensive tools for MSX software development, testing, and automation through standardized MCP protocols.

2455. **[mcp-rquest](https://github.com/xxxbrian/mcp-rquest)** - ⭐ 43
   A MCP server providing realistic browser-like HTTP request capabilities with accurate TLS/JA3/JA4 fingerprints for bypassing anti-bot measures. It also supports converting PDF and HTML documents to Markdown for easier processing by LLMs.

2456. **[MCPApp](https://github.com/tanaikech/MCPApp)** - ⭐ 43
   This text introduces the Model Context Protocol (MCP) for AI interaction, exploring Google Apps Script (GAS) as a server option. It shows feasibility with a sample but notes the lack of a GAS SDK, aiming to encourage understanding and development.

2457. **[salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server)** - ⭐ 43
   Model Context Protocol server for Salesforce REST API integration

2458. **[cli](https://github.com/syrin-labs/cli)** - ⭐ 43
   Runtime intelligence system that makes MCP servers debuggable, testable, and safe to run in production.

2459. **[agentic-developer-mcp](https://github.com/teabranch/agentic-developer-mcp)** - ⭐ 43
   An MCP server that scales development into controllable agentic, recursive flows, and build a feature from bottom-up

2460. **[prism-mcp-rs](https://github.com/prismworks-ai/prism-mcp-rs)** - ⭐ 43
   Enterprise-grade Rust implementation of Anthropic's MCP protocol

2461. **[nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server that enables AI assistants to perform network scanning operations using NMAP

2462. **[mcp-ai-memory](https://github.com/scanadi/mcp-ai-memory)** - ⭐ 43
   A production-ready Model Context Protocol (MCP) server for semantic memory management

2463. **[adeu](https://github.com/dealfluence/adeu)** - ⭐ 43
   Agentic DOCX Redlining Engine. Enables LLMs to read Word documents and inject native Track Changes (w:ins, w:del) and Comments without breaking formatting. Includes Model Context Protocol (MCP) Server.

2464. **[mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb)** - ⭐ 43
   This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implements core database operations and allows seamless integration with ArangoDB through MCP tools. You can use it wih Claude app and also extension for VSCode that works with mcp like Cline!

2465. **[fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp)** - ⭐ 43
   A high-performance Model Context Protocol (MCP) server that provides secure filesystem access for Claude and other AI assistants.

2466. **[yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp)** - ⭐ 43
   Yandex Tracker MCP Server with OAuth2 support

2467. **[gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server)** - ⭐ 43
   A Model Context Protocol (MCP) server to enable AI tools to interact with Gradle projects programmatically.

2468. **[pentestMCP](https://github.com/ramkansal/pentestMCP)** - ⭐ 43
   pentestMCP: AI-Powered Penetration Testing via MCP, an MCP designed for penetration testers.

2469. **[Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)** - ⭐ 43
   Control Fusion 360 with any AI through Model Context Protocol (MCP)

2470. **[taskMaster-todoist-mcp](https://github.com/mingolladaniele/taskMaster-todoist-mcp)** - ⭐ 42
   A lightweight Model Context Protocol (MCP) server that enables natural language interaction with your Todoist tasks directly from your IDE. Built with simplicity and maintainability in mind.

2471. **[solana-dev-mcp](https://github.com/solana-foundation/solana-dev-mcp)** - ⭐ 42
   Solana Model Context Protocol (MCP) Demo

2472. **[awesome-mcp-servers](https://github.com/mctrinh/awesome-mcp-servers)** - ⭐ 42
   A curated list of excellent Model Context Protocol (MCP) servers.

2473. **[mobile-dev-mcp-server](https://github.com/jsuarezruiz/mobile-dev-mcp-server)** - ⭐ 42
   This is a MCP designed to manage and interact with mobile devices and simulators.

2474. **[repl-mcp](https://github.com/simm-is/repl-mcp)** - ⭐ 42
   Model Context Protocol Clojure support including REPL integration with development tools.

2475. **[mcp-logic](https://github.com/angrysky56/mcp-logic)** - ⭐ 42
   Fully functional AI Logic Calculator utilizing Prover9/Mace4 via Python based Model Context Protocol (MCP-Server)- tool for Windows Claude App etc

2476. **[zed-mcp-server-sequential-thinking](https://github.com/LoamStudios/zed-mcp-server-sequential-thinking)** - ⭐ 42
   A sequential thinking MCP server extension for Zed

2477. **[mcp-zenml](https://github.com/zenml-io/mcp-zenml)** - ⭐ 42
   MCP server to connect an MCP client (Cursor, Claude Desktop etc) with your ZenML MLOps and LLMOps pipelines

2478. **[illustrator-mcp-server](https://github.com/spencerhhubert/illustrator-mcp-server)** - ⭐ 42
   mcp server to run scripts on adobe illustrator

2479. **[org-mcp](https://github.com/laurynas-biveinis/org-mcp)** - ⭐ 42
   Emacs Org-mode integration with Model Context Protocol (MCP) for AI-assisted task management

2480. **[mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner)** - ⭐ 42
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core.

2481. **[mcp-server-ios-simulator](https://github.com/atom2ueki/mcp-server-ios-simulator)** - ⭐ 42
   Model Context Protocol (MCP) implementation for iOS simulators

2482. **[whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp)** - ⭐ 42
   WhatsApp Unofficial MCP Server

2483. **[flutter-skill](https://github.com/ai-dashboad/flutter-skill)** - ⭐ 42
   AI-powered E2E testing for 10 platforms. 253 MCP tools. Zero config. Works with Claude, Cursor, Windsurf, Copilot. Test Flutter, React Native, iOS, Android, Web, Electron, Tauri, KMP, .NET MAUI — all from natural language.

2484. **[linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp)** - ⭐ 42
   MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.

2485. **[mcp-server-js](https://github.com/yepcode/mcp-server-js)** - ⭐ 41
   MCP server that exposes YepCode processes as callable tools for AI platforms. Securely connect AI assistants to your YepCode workflows, APIs, and automations.

2486. **[dynamic-shell-server](https://github.com/codelion/dynamic-shell-server)** - ⭐ 41
   Dynamic Shell Command MCP Server

2487. **[zig-mcp-server](https://github.com/openSVM/zig-mcp-server)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides Zig language tooling, code analysis, and documentation access. This server enhances AI capabilities with Zig-specific functionality including code optimization, compute unit estimation, code generation, and best practices recommendations.

2488. **[mcp](https://github.com/Azure-Samples/mcp)** - ⭐ 41
   Links to samples, tools, and resources for building and integrating Model Context Protocol (MCP) servers on Azure using multiple languages

2489. **[dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)** - ⭐ 41
   A Model Context Protocol server for Dify

2490. **[ZMCPTools](https://github.com/ZachHandley/ZMCPTools)** - ⭐ 41
   A custom TypeScript MCP Server intended to be used with Claude Code

2491. **[locallama-mcp](https://github.com/Heratiki/locallama-mcp)** - ⭐ 41
   An MCP Server that works with Roo Code/Cline.Bot/Claude Desktop to optimize costs by intelligently routing coding tasks between local LLMs free APIs and paid APIs.

2492. **[seekcode](https://github.com/seekrays/seekcode)** - ⭐ 41
   A clean and efficient code snippet and clipboard management tool designed for developers

2493. **[binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server)** - ⭐ 41
   Unofficial tools and server implementation for Binance's Model Context Protocol (MCP). Designed to support developers building crypto trading  AI Agents.

2494. **[openrouter-deep-research-mcp](https://github.com/wheattoast11/openrouter-deep-research-mcp)** - ⭐ 41
   A multi-agent research MCP server + mini client adapter - orchestrates a net of async agents or streaming swarm to conduct ensemble consensus-backed research. Each task builds its own indexed pglite database on the fly in web assembly. Includes semantic + hybrid search, SQL execution, semaphores, prompts/resources and more

2495. **[beanquery-mcp](https://github.com/vanto/beanquery-mcp)** - ⭐ 41
   Beancount MCP Server is an experimental implementation that utilizes the Model Context Protocol (MCP) to enable AI assistants to query and analyze Beancount ledger files using Beancount Query Language (BQL) and the beanquery tool.

2496. **[embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** - ⭐ 41
   A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more

2497. **[nvim-mcp](https://github.com/linw1995/nvim-mcp)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides seamless integration with Neovim instances, enabling AI assistants to interact with your editor through connections and access diagnostic information via structured resources.

2498. **[platform-context-exporter](https://github.com/alkoleft/platform-context-exporter)** - ⭐ 41
   Инструмент для выгрузки синтаксис помощника в файлы

2499. **[ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides vision capabilities to analyze image and video

2500. **[polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp)** - ⭐ 41
   a mcp server for polymarket

2501. **[instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** - ⭐ 41
   📢 Instagram MCP Server – A powerful Model Context Protocol (MCP) server for tracking Instagram engagement, generating leads, and analyzing audience feedback.

2502. **[MCPToolBenchPP](https://github.com/mcp-tool-bench/MCPToolBenchPP)** - ⭐ 41
   MCPToolBench++ MCP Model Context Protocol Tool Use Benchmark on AI Agent and Model Tool Use Ability

2503. **[Readwise-Reader-MCP](https://github.com/edricgsh/Readwise-Reader-MCP)** - ⭐ 41
   A Model Context Protocol (MCP) server for the Readwise Reader API, built with TypeScript and the official Claude SDK.

2504. **[linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** - ⭐ 41
   A powerful Model Context Protocol server for LinkedIn API integration

2505. **[svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp)** - ⭐ 41
   Model Context Protocol server for SVGMaker - AI-powered SVG generation and editing. Seamlessly integrate SVG creation into AI workflows.

2506. **[mcp_weather_server](https://github.com/isdaniel/mcp_weather_server)** - ⭐ 41
   A Model Context Protocol (MCP) server that provides weather information using the Open-Meteo API.

2507. **[mcp-obsidian](https://github.com/fazer-ai/mcp-obsidian)** - ⭐ 41
   MCP server for Obsidian (TypeScript + Bun)

2508. **[xhs-mcp](https://github.com/Algovate/xhs-mcp)** - ⭐ 41
   用于小红书（xiaohongshu.com）的 Model Context Protocol（MCP）服务器与 CLI 工具，支持登录、发布、搜索、推荐等自动化能力

2509. **[unreal-mcp](https://github.com/runeape-sats/unreal-mcp)** - ⭐ 41
   Unreal Engine MCP server for Claude Desktop (early alpha preview)

2510. **[adal-cli](https://github.com/SylphAI-Inc/adal-cli)** - ⭐ 41
   The self-evolving coding agent that learns from your entire team and codebase. Less syncing. Less waiting. Deliver at the speed of thought.

2511. **[mcpshim](https://github.com/mcpshim/mcpshim)** - ⭐ 41
   Turn remote MCP servers into local command workflows.

2512. **[mcp-server](https://github.com/profullstack/mcp-server)** - ⭐ 40
   A generic, modular server for implementing the Model Context Protocol (MCP). 

2513. **[mcp_rails_template](https://github.com/seuros/mcp_rails_template)** - ⭐ 40
   A minimal Rails API template for creating MCP (Model Context Protocol) servers with robust tool execution capabilities and examples.

2514. **[agentic-mcp-client](https://github.com/peakmojo/agentic-mcp-client)** - ⭐ 40
   A standalone agent runner that executes tasks using MCP (Model Context Protocol) tools via Anthropic Claude, AWS BedRock and OpenAI APIs. It enables AI agents to run autonomously in cloud environments and interact with various systems securely.

2515. **[browser-use-mcp-client](https://github.com/Linzo99/browser-use-mcp-client)** - ⭐ 40
   A MCP client for browser-use

2516. **[mcp-shell](https://github.com/hdresearch/mcp-shell)** - ⭐ 40
   Execute a secure shell in Claude Desktop using the Model Context Protocol.

2517. **[bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** - ⭐ 40
   Bluesky MCP (Model Context Protocol) Server

2518. **[just-mcp](https://github.com/toolprint/just-mcp)** - ⭐ 40
   Share the same project justfile tasks with your AI Coding Agent.

2519. **[scraps](https://github.com/boykush/scraps)** - ⭐ 40
   Scraps is a portable CLI knowledge hub for managing interconnected Markdown documentation with Wiki-link notation.

2520. **[Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP)** - ⭐ 40
   A Model Context Protocol (MCP) server that provides LLMs with real-time access to scientific papers from arXiv and OpenAlex.

2521. **[algorand-mcp](https://github.com/GoPlausible/algorand-mcp)** - ⭐ 40
   Algorand Local Model Context Protocol (Server & Client)

2522. **[mcp-panther](https://github.com/panther-labs/mcp-panther)** - ⭐ 40
   Write detections, investigate alerts, and query logs from your favorite AI agents

2523. **[dev-to-mcp](https://github.com/nickytonline/dev-to-mcp)** - ⭐ 40
   A remote Model Context Protocol (MCP) server for interacting with the dev.to public API without requiring authentication.

2524. **[mcp-pyautogui-server](https://github.com/hetaoBackend/mcp-pyautogui-server)** - ⭐ 40
   A MCP (Model Context Protocol) server that provides automated GUI testing and control capabilities through PyAutoGUI.

2525. **[linkedin-mcp-server](https://github.com/Dishant27/linkedin-mcp-server)** - ⭐ 40
   Model Context Protocol (MCP) server for LinkedIn API integration

2526. **[TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer)** - ⭐ 40
   台灣證交所OpenAPI 的 MCP Server

2527. **[shodan-mcp-server](https://github.com/Cyreslab-AI/shodan-mcp-server)** - ⭐ 40
   A Model Context Protocol server that provides access to Shodan API functionality

2528. **[neurondb](https://github.com/neurondb/neurondb)** - ⭐ 40
   PostgreSQL extension for vector search, embeddings, and ML, plus NeuronAgent runtime and NeuronMCP server.

2529. **[forgejo-mcp](https://github.com/raohwork/forgejo-mcp)** - ⭐ 40
   A MCP server that enables you to manage Gitea/Forgejo repositories through AI assistants

2530. **[pdf-rag-mcp-server](https://github.com/hyson666/pdf-rag-mcp-server)** - ⭐ 40
   PDF RAG server for cursor.

2531. **[anki-mcp](https://github.com/nietus/anki-mcp)** - ⭐ 39
   MCP server for anki

2532. **[dotcom.chat](https://github.com/kamath/dotcom.chat)** - ⭐ 39
   A simple NextJS MCP client with sensible keybindings

2533. **[MCPollinations](https://github.com/pinkpixel-dev/MCPollinations)** - ⭐ 39
   A Model Context Protocol (MCP) server that enables AI assistants to generate images, text, and audio through the Pollinations APIs. Supports customizable parameters, image saving, and multiple model options.

2534. **[mcp_code_analyzer](https://github.com/emiryasar/mcp_code_analyzer)** - ⭐ 39
   A Model Context Protocol (MCP) server implementation for comprehensive code analysis. This tool integrates with Claude Desktop to provide code analysis capabilities through natural language interactions.

2535. **[mmcp](https://github.com/koki-develop/mmcp)** - ⭐ 39
   🛠️ Manage your MCP (Model Context Protocol) server definitions in one place and apply them to supported agents.

2536. **[mcp-desktop](https://github.com/http4k/mcp-desktop)** - ⭐ 39
   http4k MCP Desktop Client

2537. **[mcp-client-server-host-demo](https://github.com/danwritecode/mcp-client-server-host-demo)** - ⭐ 39
   A quick pokemon demo to showcase MCP server, client, and host

2538. **[mcp](https://github.com/kyopark2014/mcp)** - ⭐ 39
   It shows how to use model-context-protocol. 

2539. **[mssql-mcp](https://github.com/daobataotie/mssql-mcp)** - ⭐ 39
   mssql mcp server

2540. **[mcp_ctl](https://github.com/runablehq/mcp_ctl)** - ⭐ 39
   A package manager to manage all your mcp servers across platforms

2541. **[mcp-android-server-python](https://github.com/nim444/mcp-android-server-python)** - ⭐ 39
   MCP Android agent - This project provides an *MCP (Model Context Protocol)* server for automating Android devices using uiautomator2. It's designed to be easily plugged into AI agents like GitHub Copilot Chat, Claude, or Open Interpreter to control Android devices through natural language.

2542. **[nia](https://github.com/nozomio-labs/nia)** - ⭐ 39
   Nia is a context-augmentation layer for agents, primarily designed for coding agents. It provides them with an up-to-date knowledge base and improves their performance by 27%.

2543. **[vscode-agent-todos](https://github.com/digitarald/vscode-agent-todos)** - ⭐ 39
   Gives VS Code agent mode planning superpowers with dynamic todo lists

2544. **[pbixray-mcp-server](https://github.com/jonaolden/pbixray-mcp-server)** - ⭐ 39
   MCP server to give llms such as Claude, GitHub Copilot etc full PowerBI model context (from input .pbix) through tools based on PBIXRay python package.

2545. **[ContextPods](https://github.com/conorluddy/ContextPods)** - ⭐ 39
   Model Context Protocol management suite/factory. An MCP that can generate and manage other local MCPs in multiple languages. Uses the official SDKs for code gen.

2546. **[open-ghl-mcp](https://github.com/basicmachines-co/open-ghl-mcp)** - ⭐ 39
   An open source Model Context Protocol server for GoHighLevel API v2 with OAuth

2547. **[search-scrape](https://github.com/DevsHero/search-scrape)** - ⭐ 39
   Self-hosted Stealth Scraping & Federated Search for AI Agents. A 100% private, free alternative to Firecrawl, Jina Reader, and Tavily. Featuring Universal Anti-bot Bypass + Semantic Research Memory, Copy-Paste setup

2548. **[agent-mcp-gateway](https://github.com/roddutra/agent-mcp-gateway)** - ⭐ 39
   Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

2549. **[RedBook-Search-Comment-MCP](https://github.com/chenningling/RedBook-Search-Comment-MCP)** - ⭐ 39
   这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

2550. **[steampipe-mcp](https://github.com/turbot/steampipe-mcp)** - ⭐ 39
   Enable AI assistants to explore and query your Steampipe data!

2551. **[storybook-mcp](https://github.com/mcpland/storybook-mcp)** - ⭐ 39
   A MCP server for Storybook.

2552. **[webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server)** - ⭐ 39
    A Model Context Protocol (MCP) server implementation that integrates with WebScraping.AI for web data extraction capabilities.

2553. **[gatekit](https://github.com/gatekit-ai/gatekit)** - ⭐ 39
   A hackable Model Context Protocol (MCP) gateway

2554. **[mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides comprehensive access to MLB statistics and baseball data through a FastMCP-based interface.

2555. **[mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp)** - ⭐ 39

2556. **[How-To-Create-MCP-Server](https://github.com/nisalgunawardhana/How-To-Create-MCP-Server)** - ⭐ 39
   This guide will help you set up a basic MCP (Model Context Protocol) server in .NET, configure it in VS Code, and interact with it using Copilot Chat.

2557. **[mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode)** - ⭐ 39
   A Model Context Protocol (MCP) server for LeetCode that provides access to problems, user data, and contest information through GraphQL

2558. **[RiMCP_hybrid](https://github.com/h7lu/RiMCP_hybrid)** - ⭐ 39
   Rimworld Coding RAG MCP server

2559. **[google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp)** - ⭐ 39
   A Model Context Protocol (MCP) server that provides secure integration with Google Drive, Docs, Sheets, Slides and Calendar. It allows Claude Desktop and other MCP clients to manage files in Google Drive through a standardized interface.

2560. **[McpDotNet.Extensions.SemanticKernel](https://github.com/StefH/McpDotNet.Extensions.SemanticKernel)** - ⭐ 39
   Microsoft SemanticKernel integration for the Model Context Protocol (MCP). Enables seamless use of MCP tools as AI functions.

2561. **[claude-additional-models-mcp](https://github.com/Arkya-AI/claude-additional-models-mcp)** - ⭐ 39
   Reduce Claude Desktop consumption by 10x - Integrate Google's Gemini or Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

2562. **[openzim-mcp](https://github.com/cameronrye/openzim-mcp)** - ⭐ 39
   OpenZIM MCP is a modern, secure, and high-performance MCP (Model Context Protocol) server that enables AI models to access and search ZIM format knowledge bases offline.

2563. **[apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp)** - ⭐ 39
   Apple Books MCP Server

2564. **[mcp-tasks](https://github.com/flesler/mcp-tasks)** - ⭐ 39
   A comprehensive and efficient MCP server for task management with multi-format support (Markdown, JSON, YAML)

2565. **[music-composer-webmcp](https://github.com/Leanmcp-Community/music-composer-webmcp)** - ⭐ 39
   This WebMCP Music Composer project is a functional demonstration of the WebMCP Protocol, illustrating how AI agents can interact with local browser contexts (tools) to achieve complex workflows autonomously.

2566. **[mcp-crypto-price](https://github.com/truss44/mcp-crypto-price)** - ⭐ 38
   A Model Context Protocol (MCP) server that provides real-time cryptocurrency analysis via CoinCap's API. Enables Claude and other MCP clients to fetch crypto prices, analyze market trends, and track historical data.

2567. **[mcp-sitecore-server](https://github.com/Antonytm/mcp-sitecore-server)** - ⭐ 38
   Model Context Protocol server for Sitecore

2568. **[middy-mcp](https://github.com/fredericbarthelet/middy-mcp)** - ⭐ 38
   Middy middleware for Model Context Protocol server hosting on AWS Lambda

2569. **[mcp-center](https://github.com/nautilus-ops/mcp-center)** - ⭐ 38
   A centralized platform for managing and connecting MCP servers. MCP Center provides a high-performance proxy service that enables seamless communication between MCP clients and multiple MCP servers.

2570. **[okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** - ⭐ 38
   The Okta MCP Server is a groundbreaking tool built by the team at Fctr that enables AI models to interact directly with your Okta environment using the Model Context Protocol (MCP). Built specifically for IAM engineers, security teams, and Okta administrators, it implements the MCP specification to help work with Okta enitities

2571. **[grafana-mcp-analyzer](https://github.com/SailingCoder/grafana-mcp-analyzer)** - ⭐ 38
   让AI助手直接分析你的Grafana监控数据 - A Model Context Protocol server for Grafana data analysis

2572. **[prompt-decorators](https://github.com/synaptiai/prompt-decorators)** - ⭐ 38
   A standardized framework for enhancing how LLMs process and respond to prompts through composable decorators, featuring an official open standard specification and Python reference implementation with MCP server integration.

2573. **[DeepCo](https://github.com/succlz123/DeepCo)** - ⭐ 38
   A Chat Client for LLMs, written in Compose Multiplatform.

2574. **[vancouver](https://github.com/jameslong/vancouver)** - ⭐ 38
   Simple MCP server library for Elixir.

2575. **[cdk_pywrapper](https://github.com/sebotic/cdk_pywrapper)** - ⭐ 38
   A Python wrapper for the Chemistry Development Kit (CDK)

2576. **[mocxykit](https://github.com/shunseven/mocxykit)** - ⭐ 38
   This is an Frontend development service middleware that can be used with webpack and vite. Its main function is to visualize the configuration, manage http(s)-proxy, and mock data.

2577. **[comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server)** - ⭐ 38
   A server using FastMCP framework to generate images based on prompts via a remote Comfy server.

2578. **[mcpmc](https://github.com/gerred/mcpmc)** - ⭐ 38
   Model Context Protocol Minecraft Server

2579. **[autoteam](https://github.com/diazoxide/autoteam)** - ⭐ 38
   Orchestrate AI agents with YAML-driven workflows via universal Model Context Protocol (MCP)

2580. **[tomtom-mcp](https://github.com/tomtom-international/tomtom-mcp)** - ⭐ 38
   A Model Context Protocol (MCP) server providing TomTom's location services, search, routing, and traffic data to AI agents.

2581. **[mcp-konnect](https://github.com/Kong/mcp-konnect)** - ⭐ 38
   A Model Context Protocol (MCP) server for interacting with Kong Konnect APIs, allowing AI assistants to query and analyze Kong Gateway configurations, traffic, and analytics.

2582. **[nuclei-mcp](https://github.com/addcontent/nuclei-mcp)** - ⭐ 38
   An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables context-aware vulnerability scanning by intelligently providing models and context to the scanning engine, allowing for more efficient and targeted template execution

2583. **[kitwork](https://github.com/kitwork/kitwork)** - ⭐ 38
   Automate kit workflows effortlessly with a lightweight, high-performance, fast, and flexible engine for cloud or self-hosted environments.

2584. **[nostr-mcp](https://github.com/AbdelStark/nostr-mcp)** - ⭐ 38
   A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.

2585. **[octomind](https://github.com/Muvon/octomind)** - ⭐ 38
   Highly configurable autonomous efficient-first agentic AI framework for CLI

2586. **[reactbits-mcp-server](https://github.com/ceorkm/reactbits-mcp-server)** - ⭐ 38
   MCP server providing access to 135+ animated React components from ReactBits.dev (9.2/10 test score)

2587. **[mcp-gitlab-server](https://github.com/yoda-digital/mcp-gitlab-server)** - ⭐ 38
   Enhanced MCP server for GitLab: group projects listing and activity tracking

2588. **[context-awesome](https://github.com/bh-rat/context-awesome)** - ⭐ 38
   awesome-lists now available as MCP server for you agent.

2589. **[powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp)** - ⭐ 38
   Open Source Model Context Protocol server for PowerPoint automation on Windows via pywin32

2590. **[mcp-flight-search](https://github.com/arjunprabhulal/mcp-flight-search)** - ⭐ 38
   MCP Server implementation for the Model Context Protocol (MCP) enabling AI tool usage - Realtime Flight Search 

2591. **[mcp-front](https://github.com/stainless-api/mcp-front)** - ⭐ 38
   Auth proxy for Model Context Protocol servers - adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, Gemini

2592. **[evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server)** - ⭐ 38
   Evernote MCP server - allows LLMs that support MCP (like Claude Desktop) to query your notes in Evernote

2593. **[MCP-Server-Creator](https://github.com/GongRzhe/MCP-Server-Creator)** - ⭐ 38
   A powerful Model Context Protocol (MCP) server that creates other MCP servers! This meta-server provides tools for dynamically generating FastMCP server configurations and Python code.

2594. **[solscan-mcp](https://github.com/wowinter13/solscan-mcp)** - ⭐ 38
   An MCP server for querying Solana transactions using natural language with Solscan API

2595. **[Web-Algebra](https://github.com/AtomGraph/Web-Algebra)** - ⭐ 38
   Suite of generic Linked Data/SPARQL as well as LinkedDataHub-specific MCP tools

2596. **[keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)** - ⭐ 38
   MCP server implementation for Keycloak user management. Enables AI-powered administration of Keycloak users and realms through the Model Context Protocol (MCP). Seamlessly integrates with Claude Desktop and other MCP clients for automated user operations.

2597. **[metabase-mcp](https://github.com/hluaguo/metabase-mcp)** - ⭐ 38
   Metabase MCP server provides integration with the Metabase API, enabling LLM with MCP capabilites to directly interact with your analytics data, this server acts as a bridge between your analytics platform and conversational AI.

2598. **[React-Native-MCP](https://github.com/MrNitro360/React-Native-MCP)** - ⭐ 38
   A Model Context Protocol (MCP) server providing comprehensive guidance and best practices for React Native development based on official React Native documentation.

2599. **[MCP-Microsoft-Office](https://github.com/Aanerud/MCP-Microsoft-Office)** - ⭐ 38
   an local MCP server you can run on your env, connecting you to Microsoft Graph, and the complete M365 eco system.

2600. **[a11y-mcp](https://github.com/priyankark/a11y-mcp)** - ⭐ 38
   An MCP (Model Context Protocol) server for performing accessibility audits on webpages using axe-core. Use the results in an agentic loop with your favorite AI assistants (Amp/Cline/Cursor/GH Copilot) and let them fix a11y issues for you!

2601. **[mcp-appstore](https://github.com/appreply-co/mcp-appstore)** - ⭐ 38
   This is an MCP server that provides tools to LLMs for searching and analyzing apps from both Google Play Store and Apple App Store – perfect for ASO.

2602. **[trivy-mcp](https://github.com/aquasecurity/trivy-mcp)** - ⭐ 37
   Trivy plugin for starting an MCP server

2603. **[codebase-mcp](https://github.com/danyQe/codebase-mcp)** - ⭐ 37
   Open-source AI development assistant via Model Context Protocol (MCP). Turn Claude or any LLM into your personal coding assistant. Privacy-first with local semantic search, AI-assisted editing, persistent memory, and quality-checked code generation. Built for Python & React. Free alternative to paid AI coding tools.

2604. **[mcp-summarization-functions](https://github.com/Braffolk/mcp-summarization-functions)** - ⭐ 37
   Provides summarised output from various actions that could otherwise eat up tokens and cause crashes for AI agents 

2605. **[mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl)** - ⭐ 37
   MCP server tailored to connecting web crawler data and archives

2606. **[gemini-superclaude-mcp-server](https://github.com/Dianel555/gemini-superclaude-mcp-server)** - ⭐ 37
   A **complete rewrite** of the original SuperClaude MCP server with intelligent command routing, dynamic persona switching, and real MCP server orchestration for Gemini CLI.Th

2607. **[HAL](https://github.com/DeanWard/HAL)** - ⭐ 37
   HAL (HTTP API Layer) is a Model Context Protocol (MCP) server that provides HTTP API capabilities to Large Language Models.

2608. **[mcp-client-example](https://github.com/artemnovichkov/mcp-client-example)** - ⭐ 37
   Learn how to implement MCP client with SwiftUI and Anthropic API

2609. **[offeryn](https://github.com/avahowell/offeryn)** - ⭐ 37
   Build tools for LLMs in Rust using Model Context Protocol

2610. **[youtrack-mcp](https://github.com/itsalfredakku/youtrack-mcp)** - ⭐ 37
   An MCP (Model Context Protocol) server that provides YouTrack REST API access to AI agents

2611. **[matlab-mcp](https://github.com/Tsuchijo/matlab-mcp)** - ⭐ 37
   Model Context Protocol server to let LLMs write and execute matlab scripts 

2612. **[openai-mcp](https://github.com/arthurcolle/openai-mcp)** - ⭐ 37
   OpenAI Code Assistant Model Context Protocol (MCP) Server

2613. **[dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp)** - ⭐ 37
   DexPaprika MCP server allows access real-time and historical data on crypto tokens, DEX trading activity, and liquidity across multiple blockchains. It enables natural language queries for exploring market trends, token performance, and DeFi analytics through a standardized interface.

2614. **[Mcp.Net](https://github.com/SamFold/Mcp.Net)** - ⭐ 37
   A fully featured C# implementation of Anthropic's Model Context Protocol (MCP)

2615. **[GDB-MCP](https://github.com/smadi0x86/GDB-MCP)** - ⭐ 37
   An MCP server that enables LLMs to interact with GDB and LLDB for binary debugging and analysis.

2616. **[mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr)** - ⭐ 37
   Model Context Protocol (MCP) Server for Mistral OCR API

2617. **[mcp-anywhere](https://github.com/locomotive-agency/mcp-anywhere)** - ⭐ 37
   A unified gateway for Model Context Protocol (MCP) servers that lets you discover, configure, and access MCP tools from any GitHub repository through a single endpoint.

2618. **[nestjs-starter](https://github.com/hmake98/nestjs-starter)** - ⭐ 37
   Production-ready NestJS boilerplate with JWT auth, PostgreSQL/Prisma, AWS S3/SES, Bull/Redis queues, Docker/K8s support, and MCP integration for AI capabilities

2619. **[bonnard-cli](https://github.com/meal-inc/bonnard-cli)** - ⭐ 37
   Ultra-fast to deploy agentic-first mcp-ready semantic layer. Let your data be like water.

2620. **[mcp-wikidata](https://github.com/zzaebok/mcp-wikidata)** - ⭐ 37
   A server implementation for Wikidata API using the Model Context Protocol (MCP).

2621. **[claude-mcp](https://github.com/cnych/claude-mcp)** - ⭐ 37
   Claude Unified Model Context Interaction Protocol

2622. **[reaper-mcp](https://github.com/itsuzef/reaper-mcp)** - ⭐ 37
   A comprehensive Model Context Protocol (MCP) server that enables AI agents to create fully mixed and mastered tracks in REAPER with both MIDI and audio capabilities.

2623. **[ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp)** - ⭐ 37
   Headless IDA Pro binary analysis via Model Context Protocol

2624. **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** - ⭐ 37
   A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema discovery, and advanced search across people, companies, tasks, and notes.

2625. **[memcord](https://github.com/ukkit/memcord)** - ⭐ 37
   🧠 Privacy-first MCP server for AI memory management. Save, search & organize chat history with intelligent  summarization.

2626. **[agentic-commerce-protocol-demo](https://github.com/locus-technologies/agentic-commerce-protocol-demo)** - ⭐ 37
   Reference implementation of OpenAI's Agentic Commerce Protocol (ACP)

2627. **[shadcn-svelte-mcp](https://github.com/Michael-Obele/shadcn-svelte-mcp)** - ⭐ 37
   Mastra MCP server and tooling for the shadcn-svelte component docs and developer utilities.

2628. **[mcp-go](https://github.com/riza-io/mcp-go)** - ⭐ 36
   Build Model Context Protocol (MCP) servers in Go

2629. **[baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server)** - ⭐ 36
   特定のWeb APIに関するBaselineの状況を提供するModel Context Protocolサーバー

2630. **[example-mcp-server](https://github.com/kirill-markin/example-mcp-server)** - ⭐ 36
   A ready-to-use MCP (Model Context Protocol) server template for extending Cursor IDE with custom tools. Deploy your own server to Heroku with one click, create custom commands, and enhance your Cursor IDE experience. Perfect for developers who want to add their own tools and commands to Cursor IDE without complex setup.

2631. **[mcp-governance-sdk](https://github.com/ithena-one/mcp-governance-sdk)** - ⭐ 36
   Enterprise Governance Layer (Identity, RBAC, Credentials, Auditing, Logging, Tracing) for the Model Context Protocol SDK

2632. **[OmniMind](https://github.com/Techiral/OmniMind)** - ⭐ 36
   OmniMind: An open-source Python library for effortless MCP (Model Context Protocol) integration, AI Agents, AI workflows, and AI Automations. Plug & Play AI Tools for MCP Servers and Clients, powered by Google Gemini.

2633. **[flutter-mcp-ai-chat](https://github.com/leehack/flutter-mcp-ai-chat)** - ⭐ 36
   Demonstrate how to implement MCP Client in Flutter application with AI.

2634. **[FastDomainCheck-MCP-Server](https://github.com/bingal/FastDomainCheck-MCP-Server)** - ⭐ 36
   A Model Context Protocol for checking domain name registration status in bulk.

2635. **[mcp-debug](https://github.com/giantswarm/mcp-debug)** - ⭐ 36

2636. **[code-mcp](https://github.com/54yyyu/code-mcp)** - ⭐ 36
   Code-MCP: Connect Claude AI to your development environment through the Model Context Protocol (MCP), enabling terminal commands and file operations through the AI interface.

2637. **[MCPNotes](https://github.com/9Ninety/MCPNotes)** - ⭐ 36
   A simple note-taking MCP server for recording and managing notes with AI models.

2638. **[mcp-gateway](https://github.com/theognis1002/mcp-gateway)** - ⭐ 36
   Model Context Protocol (MCP) Gateway & Registry - Central hub for managing tools, resources, and prompts for MCP-compatible LLMs. Translates REST APIs into MCP, builds virtual MCP servers with security and observability, and bridges multiple transports (stdio, SSE, streamable HTTP).

2639. **[mcp-server-antv](https://github.com/antvis/mcp-server-antv)** - ⭐ 36
   🧑🏻‍💻 MCP Server for @antvis visualization development, which provides documentation context and examples for visualization developers.

2640. **[FastAPI-BitNet](https://github.com/grctest/FastAPI-BitNet)** - ⭐ 36
   Running Microsoft's BitNet inference framework via FastAPI, Uvicorn and Docker.

2641. **[storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server)** - ⭐ 36
   A modular, extensible MCP Server for managing Storyblok spaces, stories, components, assets, workflows, and more via the Model Context Protocol (MCP).

2642. **[mcp-google-cse](https://github.com/Richard-Weiss/mcp-google-cse)** - ⭐ 36
   A Model Context Protocol server that provides search capabilities using a Google CSE (custom search engine).

2643. **[coin_api_mcp](https://github.com/longmans/coin_api_mcp)** - ⭐ 36
   A Model Context Protocol server that provides access to CoinMarketCap's cryptocurrency data. This server enables AI-powered applications to retrieve cryptocurrency listings, quotes, and detailed information about various coins.

2644. **[mcp-crew-ai](https://github.com/adam-paterson/mcp-crew-ai)** - ⭐ 36
   MCP Crew AI Server is a lightweight Python-based server designed to run, manage and create CrewAI workflows.

2645. **[Handler](https://github.com/alDuncanson/Handler)** - ⭐ 36
   A2A Protocol client and developer toolkit.

2646. **[mcp-security-inspector](https://github.com/purpleroc/mcp-security-inspector)** - ⭐ 36
   一个用于检测Model Context Protocol (MCP)安全性的Chrome扩展工具。

2647. **[mcp-bundle](https://github.com/symfony/mcp-bundle)** - ⭐ 36
   Symfony integration bundle for Model Context Protocol (via official mcp/sdk)

2648. **[mcp-zero](https://github.com/zeromicro/mcp-zero)** - ⭐ 36
   Model Context Protocol (MCP) server for go-zero framework - Generate APIs, RPC services, and models with AI assistance.

2649. **[mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server)** - ⭐ 36
   Model Context Protocol (MCP) server for Databricks that empowers AI agents to autonomously interact with Unity Catalog metadata. Enables data discovery, lineage analysis, and intelligent SQL execution. Agents explore catalogs/schemas/tables, understand relationships, discover notebooks/jobs, and execute queries - greatly reducing ad-hoc query time.

2650. **[kirby-mcp](https://github.com/bnomei/kirby-mcp)** - ⭐ 36
   CLI-first MCP server for composer-based Kirby CMS projects — inspect blueprints/templates/plugins, interact with a real Kirby runtime, and use a bundled Kirby knowledge base.

2651. **[ai-workshop](https://github.com/dotnet-presentations/ai-workshop)** - ⭐ 36
   Building GenAI Apps in C#: AI Templates, GitHub Models, Azure OpenAI & More

2652. **[salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server)** - ⭐ 36
   A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients.

2653. **[google-workspace-mcp](https://github.com/dguido/google-workspace-mcp)** - ⭐ 36
   MCP server for Google Drive, Docs, Sheets, Slides, Calendar, Gmail, and Contacts

2654. **[keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server)** - ⭐ 36
   An MCP server for Keycloak,  designed to work with Keycloak for identity and access management, covering, Users, Realms, Clients, Roles, Groups, IDPs, Authentication. Searching keycloak discourse, Native builds available.

2655. **[jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)** - ⭐ 36
   A Model Context Protocol (MCP) server that integrates with Jina AI Search Foundation APIs.

2656. **[mcp-server](https://github.com/Aayush9029/mcp-server)** - ⭐ 36
   MCP SERVER

2657. **[MCPDocSearch](https://github.com/alizdavoodi/MCPDocSearch)** - ⭐ 36
   This project provides a toolset to crawl websites wikis, tool/library documentions and generate Markdown documentation, and make that documentation searchable via a Model Context Protocol (MCP) server, designed for integration with tools like Cursor.

2658. **[tasker-mcp](https://github.com/dceluis/tasker-mcp)** - ⭐ 36
   An MCP server for Android's Tasker automation app.

2659. **[mcp-sandbox](https://github.com/JohanLi233/mcp-sandbox)** - ⭐ 36
   Python sandboxes for llms

2660. **[awesome-mcp-personas](https://github.com/toolprint/awesome-mcp-personas)** - ⭐ 36
   A curated collection of persona-based mcp server & tool groupings.

2661. **[mcp-server](https://github.com/VapiAI/mcp-server)** - ⭐ 36
   Vapi MCP Server

2662. **[workflowy](https://github.com/mholzen/workflowy)** - ⭐ 36
   Powerful CLI and MCP server for WorkFlowy: reports, search/replace, backup support, and AI integration (Claude, LLMs)

2663. **[pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server)** - ⭐ 36
   pfSense MCP Server enables security administrators to manage their pfSense firewalls using natural language through AI assistants like Claude Desktop. Simply ask "Show me blocked IPs" or "Run a PCI compliance check" instead of navigating complex interfaces. Supports REST/XML-RPC/SSH connections, and includes built-in complian

2664. **[apple-mail-mcp](https://github.com/patrickfreyer/apple-mail-mcp)** - ⭐ 36
   MCP server giving AI assistants full access to Apple Mail - read, search, compose, organize & analyze emails via natural language

2665. **[octave-mcp](https://github.com/elevanaltd/octave-mcp)** - ⭐ 36
   OCTAVE protocol - structured AI communication with 3-20x token reduction. MCP server with lenient-to-canonical pipeline and schema validation.

2666. **[processhacker-mcp](https://github.com/illegal-instruction-co/processhacker-mcp)** - ⭐ 36
   your ai debugger, vibe hacking tool

2667. **[mcp-file-context-server](https://github.com/bsmi021/mcp-file-context-server)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides file system context to Large Language Models (LLMs). This server enables LLMs to read, search, and analyze code files with advanced caching and real-time file watching capabilities.

2668. **[mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server)** - ⭐ 35
   This project provides a dedicated MCP (Model Context Protocol) server that wraps the @google/genai SDK. It exposes Google's Gemini model capabilities as standard MCP tools, allowing other LLMs (like Cline) or MCP-compatible systems to leverage Gemini's features as a backend workhorse.

2669. **[esa-mcp-server](https://github.com/d-kimuson/esa-mcp-server)** - ⭐ 35
   esa の Model Context Protocol サーバー実装

2670. **[mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client)** - ⭐ 35
   LangChain.js client for Model Context Protocol.

2671. **[mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)** - ⭐ 35
   中国传统黄历 MCP 服务 | Chinese Traditional Almanac MCP Service

2672. **[mcp](https://github.com/screenshotone/mcp)** - ⭐ 35
   A simple implementation of an MCP server for the ScreenshotOne API

2673. **[atlas-docs-mcp](https://github.com/CartographAI/atlas-docs-mcp)** - ⭐ 35
   Provide LLMs hosted, clean markdown documentation of libraries and frameworks

2674. **[tinyagent](https://github.com/askbudi/tinyagent)** - ⭐ 35
   Tiny Agent: Production-Ready LLM Agent SDK for Every Developer

2675. **[MCPSwiftWrapper](https://github.com/jamesrochabrun/MCPSwiftWrapper)** - ⭐ 35
   A light wrapper around mcp-swift-sdk for easy usage of MCP clients in Swift

2676. **[yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server)** - ⭐ 35
   A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance to get comprehensive stock market data, news, financials, and more

2677. **[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides Nostr capabilities to AI agents

2678. **[mcp-zap-server](https://github.com/dtkmn/mcp-zap-server)** - ⭐ 35
   A Spring Boot application exposing OWASP ZAP as an MCP (Model Context Protocol) server. It lets any MCP‑compatible AI agent (e.g., Claude Desktop, Cursor) orchestrate ZAP actions—spider, active scan, import OpenAPI specs, and generate reports.

2679. **[mcp-server-text-editor](https://github.com/bhouston/mcp-server-text-editor)** - ⭐ 35
   An open source implementation of the Claude built-in text editor tool

2680. **[mcp-starter](https://github.com/instructa/mcp-starter)** - ⭐ 35
   A super simple Starter to build your own MCP Server

2681. **[mcp-client-cli](https://github.com/thedotmack/mcp-client-cli)** - ⭐ 35
   Command-line interface for any Model Context Protocol (MCP) server.

2682. **[mcp-toolkit](https://github.com/metosin/mcp-toolkit)** - ⭐ 35
   a lib to build MCP clients and MCP servers in Clojure(script)

2683. **[gopls-mcp](https://github.com/xieyuschen/gopls-mcp)** - ⭐ 35
   The essential MCP server for Go language development: Exposing compiler-grade semantics to AI Agents and LLM for deterministic code analysis and minimal context pollution.

2684. **[mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability)** - ⭐ 35
   A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.

2685. **[mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent)** - ⭐ 35
   A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities. This agent enables Claude to interact with web content, manipulate DOM elements, execute JavaScript, and perform API requests.

2686. **[SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server)** - ⭐ 35
   SUMO-MCP 是一个连接大语言模型 (LLM) 与 Eclipse SUMO 交通仿真的中间件。通过 Model Context Protocol (MCP)，它允许 AI 智能体（如 Claude, Cursor, TRAE等）直接调用 SUMO 的核心功能，实现从OpenStreetMap 数据获取、路网生成、需求建模到仿真运行与信号优化的全流程自动化。

2687. **[mcp-nats](https://github.com/sinadarbouy/mcp-nats)** - ⭐ 35
   A Model Context Protocol (MCP) server for NATS messaging system integration

2688. **[RoslynMCP](https://github.com/carquiza/RoslynMCP)** - ⭐ 35
   A Model Context Protocol (MCP) server that provides C# code analysis capabilities using Microsoft Roslyn

2689. **[authenticator_mcp](https://github.com/firstorderai/authenticator_mcp)** - ⭐ 35
   A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.

2690. **[roampal-core](https://github.com/roampal-ai/roampal-core)** - ⭐ 35
   Outcome-based memory for Claude Code and OpenCode

2691. **[copilot-security-instructions](https://github.com/Robotti-io/copilot-security-instructions)** - ⭐ 35
   ✨ A customizable copilot-instructions.md ruleset & prompts to guide GitHub Copilot toward secure coding defaults in Java, Node.js, C# and Python. Blocks risky patterns, teaches safe habits.

2692. **[SageFs](https://github.com/WillEhrendreich/SageFs)** - ⭐ 35
   Sage Mode for F# development — REPL with solution or project loading, Live Testing for FREE, Hot Reload, and session management.

2693. **[daisyui-mcp](https://github.com/birdseyevue/daisyui-mcp)** - ⭐ 35
   🌼 A token-friendly local MCP server for DaisyUI component documentation using their public llms.txt.

2694. **[best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers)** - ⭐ 35
   🏆  A ranked list of MCP servers. Updated weekly.

2695. **[macOS-Notification-MCP](https://github.com/devizor/macOS-Notification-MCP)** - ⭐ 34
   macOS Notification MCP enables AI assistants to trigger native macOS sounds, visual notifications, and text-to-speech. Built for Claude and other AI models using the Model Context Protocol.

2696. **[mcp-client-auth](https://github.com/dzhng/mcp-client-auth)** - ⭐ 34
   A TypeScript library providing OAuth2 authentication utilities for Model Context Protocol (MCP) clients. This library simplifies the process of adding OAuth authentication to MCP client implementations.

2697. **[chat-nextjs-mcp-client](https://github.com/shricodev/chat-nextjs-mcp-client)** - ⭐ 34
   ⚡ Chat MCP Client for Remote hosted MCP Servers (with Composio) and locally hosted MCP servers. 📡

2698. **[mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal)** - ⭐ 34
   Model Context Protocol Server for Apache OpenDAL™

2699. **[meta-prompt-mcp-server](https://github.com/tisu19021997/meta-prompt-mcp-server)** - ⭐ 34
   Turn any MCP Client into a "multi-agent" system (via prompting)

2700. **[aio-mcp](https://github.com/athapong/aio-mcp)** - ⭐ 34
   🚀 All-in-one MCP server with AI search, RAG, and multi-service integrations (GitLab/Jira/Confluence/YouTube) for AI-enhanced development workflows. Folk from https://github.com/nguyenvanduocit/all-in-one-model-context-protocol

2701. **[llm-tools-mcp](https://github.com/VirtusLab/llm-tools-mcp)** - ⭐ 34
   Connect to MCP servers right from your shell. Plugin for simonw/llm.

2702. **[godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server)** - ⭐ 34
   A mcp server provide infomation from pkg.go.dev. For all golang programmers

2703. **[DBJavaGenix](https://github.com/ZhaoXingPeng/DBJavaGenix)** - ⭐ 34
   智能数据库代码生成工具基于MCP架构，支持MySQL等多种数据库，自动生成Entity、DAO、Service及Controller等完整分层代码，大幅提升开发效率。依托MCP协议，具备强大扩展与集成能力，可智能推断表关系与业务语义。集成Mustache、MapStruct和Lombok，实现跨语言生成、高效映射和代码简化，并提供依赖自动管理，保障项目稳定。

2704. **[mcp-prompt-server-go](https://github.com/smallnest/mcp-prompt-server-go)** - ⭐ 34
   一个提供优秀prompt的Model Context Protocol (MCP)的服务器，用于根据用户任务需求提供预设的prompt模板，帮助Cline/Cursor/Windsurf...更高效地执行各种任务。服务器将预设的prompt作为工具(tools)返回，以便在Cursor和Windsurf等编辑器中更好地和使用。提供tool和prompt两种形式

2705. **[chessagineweb](https://github.com/jalpp/chessagineweb)** - ⭐ 34
   The most underrated FOSS chess interface that combines AI agents and chess engines into one unified platform. 

2706. **[prometheus_mcp_server](https://github.com/CaesarYangs/prometheus_mcp_server)** - ⭐ 34
   A Model Context Protocol (MCP) server enabling LLMs to query, analyze, and interact with Prometheus databases through predefined routes.

2707. **[codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server)** - ⭐ 34
   An MCP Server to utilize Codelogic's rich software dependency data in your AI programming assistant.

2708. **[any-script-mcp](https://github.com/izumin5210/any-script-mcp)** - ⭐ 34
   An MCP server that exposes arbitrary CLI tools and shell scripts as MCP Tools

2709. **[modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)** - ⭐ 34
   Modao Proto MCP is a standalone MCP (Model Context Protocol) service designed to connect Modao Proto design tools with AI models.

2710. **[claude-code-mcp](https://github.com/KunihiroS/claude-code-mcp)** - ⭐ 34
   MCP Server connects with claude code local command.

2711. **[mcp-scala](https://github.com/windymelt/mcp-scala)** - ⭐ 34
   Model Context Protocol server written in Scala

2712. **[mcp-registry](https://github.com/ARadRareness/mcp-registry)** - ⭐ 34
   A central registry and HTTP interface for coordinating Model Context Protocol (MCP) servers.

2713. **[iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server)** - ⭐ 34
   Apache IoTDB MCP Server

2714. **[1mcp](https://github.com/buremba/1mcp)** - ⭐ 34
   Let your agent write code and execute code directly in the browser with WASM

2715. **[kanban-mcp](https://github.com/eyalzh/kanban-mcp)** - ⭐ 34
   MCP server providing kanban-based task management memory for complex multi-session workflows with AI agents

2716. **[awesome-devops-mcp](https://github.com/agenticdevops/awesome-devops-mcp)** - ⭐ 34
   List of Awesome MCP Servers and Clients for building Agentic Devops 

2717. **[sunnysideFigma-Context-MCP](https://github.com/tercumantanumut/sunnysideFigma-Context-MCP)** - ⭐ 34
   A comprehensive Model Context Protocol (MCP) server that bridges Figma designs with AI development workflows. It provides 30 specialized tools for extracting pixel-perfect code, assets, and component structures directly from Figma designs.

2718. **[filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** - ⭐ 34
   A Model Context Protocol (MCP) server for platform-agnostic file capabilities, including advanced search/replace and directory tree traversal

2719. **[vulnerablemcp](https://github.com/vineethsai/vulnerablemcp)** - ⭐ 34
   A comprehensive database of Model Context Protocol vulnerabilities, security research, and exploits

2720. **[adb-mcp](https://github.com/srmorete/adb-mcp)** - ⭐ 34
   An MCP (Model Context Protocol) server for interacting with Android devices through ADB in TypeScript.

2721. **[Learn-Model-Context-Protocol-with-Python](https://github.com/PacktPublishing/Learn-Model-Context-Protocol-with-Python)** - ⭐ 34
   Learn Model Context Protocol with Python, published by Packt

2722. **[elysia-mcp](https://github.com/kerlos/elysia-mcp)** - ⭐ 34
   ElysiaJS plugin for Model Context Protocol with HTTP transport

2723. **[diy-tools-mcp](https://github.com/hesreallyhim/diy-tools-mcp)** - ⭐ 34
   An MCP server that allows users to dynamically add custom tools/functions at runtime

2724. **[mcp-sync](https://github.com/ztripez/mcp-sync)** - ⭐ 34
   Sync MCP (Model Context Protocol) configurations across AI tools

2725. **[pushover-mcp](https://github.com/AshikNesin/pushover-mcp)** - ⭐ 34
   A MCP implementation for sending notifications via Pushover

2726. **[foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)** - ⭐ 34
   An MCP (Model Context Protocol) server that bridges Foundry VTT data with Claude Desktop, enabling users to chat with their game world data using their own Claude subscription.

2727. **[arifOS](https://github.com/ariffazil/arifOS)** - ⭐ 34
   ArifOS — AAA MCP-governed constitutional kernel for AI agents.

2728. **[Outlook_Calendar_MCP](https://github.com/merajmehrabi/Outlook_Calendar_MCP)** - ⭐ 34
   A Model Context Protocol (MCP) server that allows Claude to access and manage your local Microsfot Outlook calendar (Windows only).

2729. **[mcp_server](https://github.com/peppemas/mcp_server)** - ⭐ 34
   A C++ implementation of a Model Context Protocol Server with a pluggable module architecture.

2730. **[MCP-Scanner](https://github.com/knostic/MCP-Scanner)** - ⭐ 34
   Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol (MCP) servers and AI infrastructure tools over HTTP & SSE.

2731. **[fal-mcp-server](https://github.com/raveenb/fal-mcp-server)** - ⭐ 34
   MCP server for Fal.ai - Generate images, videos, music and audio with Claude

2732. **[mcp-tool-filter](https://github.com/Portkey-AI/mcp-tool-filter)** - ⭐ 34
   Ultra-fast semantic tool filtering for MCP (Model Context Protocol) servers using embedding similarity. Reduce your tool context from 1000+ tools down to the most relevant 10-20 tools in under 10ms.

2733. **[mcp-server-lib.el](https://github.com/laurynas-biveinis/mcp-server-lib.el)** - ⭐ 34
   Emacs Lisp implementation of the Model Context Protocol

2734. **[capacities-mcp](https://github.com/jem-computer/capacities-mcp)** - ⭐ 34
   Capacities×MCP

2735. **[mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced)** - ⭐ 34
   Enhanced MCP server for SearXNG: category-aware web-search, web-scraping, and date/time retrieval.

2736. **[peta-core](https://github.com/dunialabs/peta-core)** - ⭐ 34
   Peta core: The Control Plane for MCP — secure vault, managed runtime, audit trail, and policy-based approvals.

2737. **[UnrealMCPBridge](https://github.com/appleweed/UnrealMCPBridge)** - ⭐ 34
   An Unreal Engine plugin that implements an MCP server allowing MCP clients to access the UE Editor Python API.

2738. **[awesome-blockchain-mcps](https://github.com/royyannick/awesome-blockchain-mcps)** - ⭐ 33
   🔗 A curated list of Blockchain & Crypto Model Context Protocol (MCP) servers. Enabling AI Agents to interact with the Blockchain, Web3, DeFi, on-chain data, on-chain actions, etc.  🚀

2739. **[adk-python-mcp-client](https://github.com/arjunprabhulal/adk-python-mcp-client)** - ⭐ 33
   Demo of ADK (Agent Development Kit) as an MCP (Model Context Protocol) client for flight search capabilities.

2740. **[mcp-google-calendar](https://github.com/markelaugust74/mcp-google-calendar)** - ⭐ 33
   A Model Context Protocol (MCP) server implementation for Google Calendar integration. Create and manage calendar events directly through Claude or other AI assistants.

2741. **[McpToolkit](https://github.com/nuskey8/McpToolkit)** - ⭐ 33
   Lightweight, fast, NativeAOT compatible MCP (Model Context Protocol) framework for .NET

2742. **[mcp-api-gateway](https://github.com/rflpazini/mcp-api-gateway)** - ⭐ 33
   A universal MCP (Model Context Protocol) server to integrate any API with Claude Desktop using only Docker configurations.

2743. **[DMCPServer](https://github.com/Daniel09Fernandes/DMCPServer)** - ⭐ 33
   Dinos MCP Server, make your code, on MCP Action and execute by AI

2744. **[mcp-veo2](https://github.com/mario-andreschak/mcp-veo2)** - ⭐ 33
   MCP for Video- or Image-Generation with Google VEO2

2745. **[kaggle-mcp](https://github.com/arrismo/kaggle-mcp)** - ⭐ 33
   MCP server for Kaggle

2746. **[mcp-launcher](https://github.com/moeru-ai/mcp-launcher)** - ⭐ 33
   🐳🧩 Easy to use MCP builder & launcher for all possible MCP servers, just like Ollama for models!

2747. **[mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)** - ⭐ 33
   A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning R1 mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API.

2748. **[wezterm-mcp](https://github.com/hiraishikentaro/wezterm-mcp)** - ⭐ 33
   About A Model Context Protocol server that executes commands in the current WezTerm session

2749. **[PixVerse-MCP](https://github.com/PixVerseAI/PixVerse-MCP)** - ⭐ 33
   Official PixVerse Model Context Protocol (MCP) server that enables interaction with powerful AI video generation APIs.

2750. **[keynote-mcp](https://github.com/easychen/keynote-mcp)** - ⭐ 33
   A Model Context Protocol (MCP) server that enables AI assistants to control Keynote presentations through AppleScript automation.

2751. **[mcp-server](https://github.com/membranehq/mcp-server)** - ⭐ 33
   MCP Server for Membrane

2752. **[devduck](https://github.com/cagataycali/devduck)** - ⭐ 33
   Minimalist AI agent that fixes itself when things break.

2753. **[fastmcp-threatintel](https://github.com/4R9UN/fastmcp-threatintel)** - ⭐ 33
   AI-Powered Threat Intelligence MCP tool

2754. **[mcp-wasm](https://github.com/beekmarks/mcp-wasm)** - ⭐ 33
   A proof-of-concept implementation of a Model Context Protocol (MCP) server that runs in WebAssembly (WASM) within a web browser. This project demonstrates the integration of MCP tools and resources in a browser environment.

2755. **[dap_mcp](https://github.com/KashunCheng/dap_mcp)** - ⭐ 33
   Model Context Protocol (MCP) server that interacts with a Debugger

2756. **[midi-mcp-server](https://github.com/tubone24/midi-mcp-server)** - ⭐ 33
   MIDI MCP Server is a Model Context Protocol (MCP) server that enables AI models to generate MIDI files from text-based music data. This tool allows for programmatic creation of musical compositions through a standardized interface.

2757. **[bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp)** - ⭐ 33
   MCP Server for the Bitrise API, enabling app management, build operations, artifact management and more.

2758. **[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** - ⭐ 33
   A simple MCP server that grabs prediction market data from polymarket, PredictIt, & Kalshi. 

2759. **[lets-learn-mcp-java](https://github.com/microsoft/lets-learn-mcp-java)** - ⭐ 33
   Learn how to build Java-based MCP Servers and Clients with LangChain4J and Quarkus

2760. **[apisix-mcp](https://github.com/api7/apisix-mcp)** - ⭐ 33
   APISIX Model Context Protocol (MCP) server is used to bridge large language models (LLMs) with the APISIX Admin API.

2761. **[mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit)** - ⭐ 33
   一个强大的 MCP (Model Context Protocol) 服务器，提20个实用工具，覆盖代码质量、开发效率、项目管理、生成skills文档全流程。

2762. **[mcp-tools](https://github.com/clerk/mcp-tools)** - ⭐ 33
   Tools for building modern & secure MCP integrations across the client and server side

2763. **[metals-standalone-client](https://github.com/jpablo/metals-standalone-client)** - ⭐ 33
   Minimal Metals stand alone client that allows running the metals mcp server

2764. **[matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server)** - ⭐ 33
   MCP Server for a Matrix home server integration; chat, manage rooms, etc.

2765. **[mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)** - ⭐ 33
   基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

2766. **[notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure)** - ⭐ 33
   Secure NotebookLM MCP Server - Query Google NotebookLM from Claude/AI agents with 14 security hardening layers

2767. **[sharedcontext](https://github.com/Eversmile12/sharedcontext)** - ⭐ 33
   MCP server that gives AI coding assistants persistent cross-client memory. Facts and conversations stored in SQLite, encrypted with AES-256-GCM, synced to Arweave. No server, no account, recoverable with a 12-word phrase.

2768. **[mie](https://github.com/kraklabs/mie)** - ⭐ 33
   Persistent memory graph for AI agents. Facts, decisions, entities, and relationships that survive across sessions, tools, and providers. MCP server — works with Claude, Cursor, ChatGPT, and any MCP client.

2769. **[postman-mcp](https://github.com/SalehKhatri/postman-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with the Postman API. This package enables AI assistants and applications to interact with Postman workspaces, collections, requests, environments, and folders programmatically.

2770. **[zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server seamlessly connecting AI Agents and AI coding tools with Zilliz Cloud  https://zilliz.com/

2771. **[azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension)** - ⭐ 32
   Model Context Protocol extension for Azure Functions.

2772. **[laravel-mcp-client](https://github.com/scriptoshi/laravel-mcp-client)** - ⭐ 32

2773. **[crawl-mcp](https://github.com/wutongci/crawl-mcp)** - ⭐ 32
   完整的微信文章抓取MCP服务器 - 基于Model Context Protocol (MCP)的智能网页抓取工具，专为Cursor IDE和AI工具设计。

2774. **[fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** - ⭐ 32
   Yahoo Fantasy Football MCP server for Claude Desktop - Advanced lineup optimization, draft assistance, and league management. Built using Claude Code.

2775. **[openbim-mcp](https://github.com/helenkwok/openbim-mcp)** - ⭐ 32
   Model Context Protocol (MCP) server for openBIM

2776. **[mcpc](https://github.com/OlaHulleberg/mcpc)** - ⭐ 32
   An extension to MCP (Model-Context-Protocol) that enables two-way asynchronous communication between LLMs and tools through the already existing MCP transport - no additional transport layer needed.

2777. **[n8n-mcp](https://github.com/vredrick/n8n-mcp)** - ⭐ 32
   n8n MCP Server - Documentation and tools for n8n nodes via Model Context Protocol with SSE support

2778. **[mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks)** - ⭐ 32
   This Model Context Protocol (MCP) server provides a bridge between LLMs and Google Tasks, allowing you to manage your task lists and tasks directly through Claude.

2779. **[Direwolf](https://github.com/Framebuffers/Direwolf)** - ⭐ 32
   Distributed Data Processing Pipeline for MCP.

2780. **[imagegen-mcp](https://github.com/spartanz51/imagegen-mcp)** - ⭐ 32
   MCP server for OpenAI Image Generation & Editing — text-to-image, image-to-image (with mask), no extra plugins.

2781. **[PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server)** - ⭐ 32
   A comprehensive Model Context Protocol (MCP) server for accessing the PubChem chemical database. This server provides access to over 110 million chemical compounds with extensive molecular properties, bioassay data, and chemical informatics tools.

2782. **[ptt_mcp_server](https://github.com/PyPtt/ptt_mcp_server)** - ⭐ 32
   The best PTT MCP server

2783. **[azure-container-apps-ai-mcp](https://github.com/Azure-Samples/azure-container-apps-ai-mcp)** - ⭐ 32
   This project showcases how to use the MCP protocol with Azure OpenAI. It provides a simple example to interact with OpenAI's API seamlessly via an MCP server and client.

2784. **[hana-mcp-server](https://github.com/HatriGt/hana-mcp-server)** - ⭐ 32
   Model Context Server Protocol for your HANA DB

2785. **[MCPCorpus](https://github.com/Snakinya/MCPCorpus)** - ⭐ 32
   MCPCorpus is a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, containing ~14K MCP servers and 300 MCP clients with 20+ normalized metadata attributes.

2786. **[mcp-server-fuzzer](https://github.com/Agent-Hellboy/mcp-server-fuzzer)** - ⭐ 32
   A generic mcp server fuzzer

2787. **[mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)** - ⭐ 32
   Provide different cloud products  MCP Server tools to  help developers  manage cloud resources  with AI-agent

2788. **[univer-mcp](https://github.com/dream-num/univer-mcp)** - ⭐ 32
   AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

2789. **[MCP-Server-Starter](https://github.com/TheSethRose/MCP-Server-Starter)** - ⭐ 32
   A Model Context Protocol server starter template

2790. **[searxng-mcp](https://github.com/tisDDM/searxng-mcp)** - ⭐ 32
   A Model Context Protocol (MCP) server that enables AI assistants to perform web searches using SearXNG, a privacy-respecting metasearch engine.

2791. **[native-devtools-mcp](https://github.com/sh3ll3x3c/native-devtools-mcp)** - ⭐ 32
   MCP server for native app testing — screenshot, OCR, click, type, find_text, template matching. macOS, Windows & Android. Works with Claude, Cursor, and any MCP client.

2792. **[mcp-for-security-python](https://github.com/f1tz/mcp-for-security-python)** - ⭐ 32
   一个为主流渗透测试工具打造的MCP服务器集合。 | A collection of Model Context Protocol servers for popular security tools like SQLMap, FFUF, NMAP, Masscan and more. Integrate security testing and penetration testing into AI workflows.

2793. **[mcp-java-sdk-examples](https://github.com/thought2code/mcp-java-sdk-examples)** - ⭐ 32
   A collection of MCP server examples developed by various Java SDKs

2794. **[mcp](https://github.com/fastly/mcp)** - ⭐ 32
   Model Context Protocol (MCP) server for AI-powered Fastly CDN management.

2795. **[mcp-server](https://github.com/blockscout/mcp-server)** - ⭐ 32
   Wraps Blockscout APIs and exposes blockchain data by Model Context Protocol

2796. **[openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** - ⭐ 32
   A Model Context Protocol (MCP) server that provides seamless integration with OpenProject API v3.

2797. **[simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)** - ⭐ 32
   A beginner-friendly MCP server template featuring a PostgreSQL connector with clean, easy-to-understand code. Perfect for developers new to Model Context Protocol who want to experiment and create their own AI tool connectors with minimal setup.

2798. **[winremote-mcp](https://github.com/dddabtc/winremote-mcp)** - ⭐ 32
   Windows Remote MCP Server — 40+ tools for desktop automation, process management, file operations via FastMCP

2799. **[omega-memory](https://github.com/omega-memory/omega-memory)** - ⭐ 31
   Persistent memory for AI coding agents

2800. **[seatunnel-mcp](https://github.com/ocean-zhc/seatunnel-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) server for Apache Seatunnel.  This provides access to your Apache Seatunnel RESTful API V2 instance and the surrounding ecosystem.

2801. **[mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides hourly and daily weather forecasts using the AccuWeather API.

2802. **[Smart-Thinking](https://github.com/Leghis/Smart-Thinking)** - ⭐ 31
   Smart-Thinking is a Model Context Protocol (MCP) server that delivers graph-based, multi-step reasoning without relying on external AI APIs. Everything happens locally: similarity search, heuristic-based scoring, verification tracking, memory, and visualization all run in a deterministic pipeline designed for transparency and reproducibility.

2803. **[AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server)** - ⭐ 31
   A comprehensive Model Context Protocol (MCP) server that provides access to the AlphaFold Protein Structure Database through a rich set of tools and resources for protein structure prediction analysis.

2804. **[PRD-MCP-Server](https://github.com/Saml1211/PRD-MCP-Server)** - ⭐ 31
   Flagship Model Context Protocol server for generating Product Requirement Documents (PRDs) from codebase context.

2805. **[dev-kit](https://github.com/nguyenvanduocit/dev-kit)** - ⭐ 31
   [Model Context Protocol] Dev Kit - anything a developer need for him day to day works

2806. **[postmancer](https://github.com/hijaz/postmancer)** - ⭐ 31
   An experimental MCP server Rest Client intended to be a replacement of tools postman & insomnia

2807. **[chatwork-mcp-server](https://github.com/chatwork/chatwork-mcp-server)** - ⭐ 31
   ChatworkをAIから操作するためのMCP(Model Context Protocol)サーバー

2808. **[zerodha-mcp](https://github.com/mtwn105/zerodha-mcp)** - ⭐ 31
   Zerodha MCP Server & Client - AI Agent (w/Agno & w/Google ADK)

2809. **[jlcpcb-parts-mcp](https://github.com/nvsofts/jlcpcb-parts-mcp)** - ⭐ 31
   JLCPCB PCBA向けの、部品探しを補助するためのMCPサーバー

2810. **[unplugin-mcp](https://github.com/situ2001/unplugin-mcp)** - ⭐ 31
   A unified plugin for developers integrating MCP servers into modern JavaScript build tools, including Webpack, Rollup, Vite, and more.

2811. **[ez-mcp](https://github.com/intellectronica/ez-mcp)** - ⭐ 31
   The easiest path to getting an MCP server going

2812. **[ESP32MCPServer](https://github.com/navado/ESP32MCPServer)** - ⭐ 31
   Allow AI models connect to ESP32 exposed interfaces. AI generated MCP server for ESP32. 

2813. **[AskUserQuestionPlus](https://github.com/JoJoJotarou/AskUserQuestionPlus)** - ⭐ 31
   A MCP server (Streamable HTTP) for asking user questions via a web interface, inspired by the Claude Code AskUserQuestion Tool.

2814. **[maven-mcp-server](https://github.com/Bigsy/maven-mcp-server)** - ⭐ 31
   An MCP (Model Context Protocol) server that provides tools for checking Maven dependency versions.

2815. **[mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** - ⭐ 31
   A minimal Model Context Protocol 🖥️ server/client🧑‍💻with Azure OpenAI and 🌐 web browser control via Playwright.

2816. **[mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news)** - ⭐ 31
   This MCP server acts as a bridge between the official Hacker News API and AI-powered tools that support the Model Context Protocol, such as Claude and Cursor.

2817. **[pan-mcp-relay](https://github.com/PaloAltoNetworks/pan-mcp-relay)** - ⭐ 31
   Palo Alto Networks AI Runtime Security Model Context Protocol (MCP) Relay Server

2818. **[mcp-appium-gestures](https://github.com/AppiumTestDistribution/mcp-appium-gestures)** - ⭐ 31
   This is a Model Context Protocol (MCP) server providing resources and tools for Appium mobile gestures using Actions API..

2819. **[EU_AI_ACT_MCP](https://github.com/SonnyLabs/EU_AI_ACT_MCP)** - ⭐ 31
   EU AI Act MCP (Model Context Protocol) that connects to your AI agents, helping you to comply with the EU AI Act.

2820. **[paraview_mcp](https://github.com/llnl/paraview_mcp)** - ⭐ 31
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

2821. **[chabeau](https://github.com/permacommons/chabeau)** - ⭐ 31
   OpenAI-API compatible terminal chatbot and MCP client in Rust

2822. **[asterisk-mcp-server](https://github.com/winfunc/asterisk-mcp-server)** - ⭐ 31
   Asterisk Model Context Protocol (MCP) server.

2823. **[Amazing-Marvin-MCP](https://github.com/bgheneti/Amazing-Marvin-MCP)** - ⭐ 31
   Model Context Provider for Amazing Marvin productivity app - Access your tasks, projects, and categories in AI assistants

2824. **[phonepi-mcp](https://github.com/priyankark/phonepi-mcp)** - ⭐ 31
   PhonePi MCP enables seamless integration between desktop AI tools and your smartphone, providing 23+ direct actions including SMS messaging, phone calls, contact management, snippet creation and search, clipboard sharing, notifications, battery status checks, and remote device controls.

2825. **[mcp-bash](https://github.com/patrickomatik/mcp-bash)** - ⭐ 31
   A simple model context protocol (MCP) server that allows Claude Desktop or other MCP aware clients to run Bash commands on your local machine.

2826. **[File-Organizer-MCP](https://github.com/kridaydave/File-Organizer-MCP)** - ⭐ 31
   This MCP server will organize your files using connections to MCP using clients like Claude, Cursor and Gemini Cli

2827. **[email-mcp](https://github.com/TimeCyber/email-mcp)** - ⭐ 31
   一个让AI轻松接管邮箱的MCP服务，基于 Model Context Protocol (MCP) 构建，支持在 MCP-X,Claude Desktop 等 MCP 客户端中使用。

2828. **[browser-use-rs](https://github.com/BB-fat/browser-use-rs)** - ⭐ 31
   A Rust library for browser automation via Chrome DevTools Protocol with built-in AI integration through Model Context Protocol (MCP)

2829. **[cml-mcp](https://github.com/xorrkaz/cml-mcp)** - ⭐ 31
   A Model Context Protocol (MCP) Server for Cisco Modeling Labs (CML)

2830. **[WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)** - ⭐ 31
   [Self-hosted] A Model Context Protocol (MCP) server implementation that provides a web search capability over stdio transport. This server integrates with a WebSearch Crawler API to retrieve search results.

2831. **[myBrAIn](https://github.com/lilium360/myBrAIn)** - ⭐ 31
   myBrAIn is an MCP (Model Context Protocol) server designed to provide persistent and contextual memory to language models (like Google Antigravity). It acts as a "second brain" for your development environment, allowing the AI to remember project rules, architectural decisions, and technical insights across different chat sessions

2832. **[omop_mcp](https://github.com/OHNLP/omop_mcp)** - ⭐ 31
   Model Context Protocol (MCP) server for mapping clinical terminology to Observational Medical Outcomes Partnership (OMOP) concepts using Large Language Models

2833. **[puppeteer-mcp-claude](https://github.com/jaenster/puppeteer-mcp-claude)** - ⭐ 31
   A Model Context Protocol (MCP) server that provides Claude Code with comprehensive browser automation capabilities through Puppeteer

2834. **[xmind-generator-mcp](https://github.com/BangyiZhang/xmind-generator-mcp)** - ⭐ 31
   An MCP (Model Context Protocol) server for generating Xmind mind maps. This server allows LLMs to create structured mind maps through the MCP protocol.

2835. **[notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp)** - ⭐ 31
   MCP server for NotebookLM - Let your AI agents (Claude Code, Codex) research documentation directly with grounded, citation-backed answers from Gemini. Persistent auth, library management, cross-client sharing. Zero hallucinations, just your knowledge base.

2836. **[machinepal](https://github.com/skalenetwork/machinepal)** - ⭐ 30
   The Cloud-Native MCP and X402 Gateway to Run and Monetize your AI Agents and Services, as well as optimize your AI costs

2837. **[mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)** - ⭐ 30
   Model Context Protocol服务器，用于抓取微博用户信息、动态和搜索功能

2838. **[clap-mcp](https://github.com/gakonst/clap-mcp)** - ⭐ 30
   A Rust framework that bridges clap command-line applications with the Model Context Protocol (MCP)

2839. **[demo-mcp-server-client-implementation](https://github.com/mschwarzmueller/demo-mcp-server-client-implementation)** - ⭐ 30
   A demo implementation of a MCP server (consuming a dummy API) and basic client.

2840. **[mcp-ollama](https://github.com/emgeee/mcp-ollama)** - ⭐ 30
   Query model running with Ollama from within Claude Desktop or other MCP clients

2841. **[mcp-client](https://github.com/edanyal/mcp-client)** - ⭐ 30
   Typescript mcp client library.

2842. **[mcp-inception](https://github.com/tanevanwifferen/mcp-inception)** - ⭐ 30
   Call another MCP client from your MCP client. Offload context windows, delegate tasks, split between models

2843. **[mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops)** - ⭐ 30
   Model Context Protocol server for Cyclops

2844. **[carrot-ai-pm](https://github.com/talvinder/carrot-ai-pm)** - ⭐ 30
   Carrot auto-writes specs and catches AI code drift. MCP server for Cursor that AST-validates every commit.

2845. **[runjs](https://github.com/CharlieDigital/runjs)** - ⭐ 30
   The only MCP server you need: let your LLM generate and safely execute JavaScript -- including fetch API calls, JSONPath ETL, built-in resiliencey, and secrets management

2846. **[airflow-mcp-server](https://github.com/abhishekbhakat/airflow-mcp-server)** - ⭐ 30
   MCP Server for Apache Airflow

2847. **[kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp)** - ⭐ 30
   A comprehensive Message Control Protocol (MCP) server for Kafka Schema Registry.

2848. **[itential-mcp](https://github.com/itential/itential-mcp)** - ⭐ 30
   🔌 Itential Platform MCP Server

2849. **[ros-mcp](https://github.com/Yutarop/ros-mcp)** - ⭐ 30
   MCP server for ROS to control robots via topics, services, and actions.

2850. **[rod-mcp](https://github.com/go-rod/rod-mcp)** - ⭐ 30
   Model Context Protocol Server of Rod

2851. **[chrome-extension-bridge-mcp](https://github.com/Oanakiaja/chrome-extension-bridge-mcp)** - ⭐ 30
   A chrome extension bridge that allows you to connect to a mcp server to use global window object.

2852. **[protonmail-mcp](https://github.com/amotivv/protonmail-mcp)** - ⭐ 30
   This MCP server provides email sending functionality using Protonmail's SMTP service. It allows both Claude Desktop and Cline VSCode extension to send emails on your behalf using your Protonmail credentials.

2853. **[turbovault](https://github.com/Epistates/turbovault)** - ⭐ 30
   MCP server that transforms your Obsidian vault into an intelligent knowledge system

2854. **[postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server)** - ⭐ 30
   MCP (Model Context Protocol) Server for postgres Database

2855. **[minimax_search](https://github.com/MiniMax-AI/minimax_search)** - ⭐ 30
   MiniMax Search is an MCP (Model Context Protocol) server that provides web search and browsing capabilities.

2856. **[browserai-mcp](https://github.com/brightdata/browserai-mcp)** - ⭐ 30
   A powerful Model Context Protocol (MCP) server that provides an access to serverless browser for AI agents and apps

2857. **[mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host)** - ⭐ 30
   A Mattermost integration that connects to Model Context Protocol (MCP) servers, leveraging a LangGraph-based Agent.

2858. **[cca-mcp-configurator](https://github.com/doggy8088/cca-mcp-configurator)** - ⭐ 30
   一個簡單易用的網頁工具，用於管理 GitHub Copilot 的 MCP (Model Context Protocol) 設定

2859. **[actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp)** - ⭐ 30
   A dual-perspective thinking analysis server based on Model Context Protocol (MCP), providing comprehensive performance evaluation through Actor-Critic methodology.

2860. **[levante](https://github.com/levante-hub/levante)** - ⭐ 30
   Levante - Personal, Secure, Free, Local AI, MCP Client

2861. **[mcp-stata](https://github.com/tmonk/mcp-stata)** - ⭐ 30
    A lightweight Model Context Protocol (MCP) server for Stata. Execute commands, inspect data, retrieve stored results (r()/e()), and view graphs in your chat interface. Built for economists who want to integrate LLM assistance into their Stata workflow. 

2862. **[pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server)** - ⭐ 30
   PubNub MCP Model Context Protocol Server for use in Cursor, Windsurf, Claude Desktop, Claude Code and OpenAI Codex and more!

2863. **[forgejo-mcp](https://github.com/goern/forgejo-mcp)** - ⭐ 30
   MIRROR ONLY!! This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API.

2864. **[ddg_search](https://github.com/OEvortex/ddg_search)** - ⭐ 30
   A powerful Model Context Protocol (MCP) server for web search and URL content extraction using DuckDuckGo.

2865. **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** - ⭐ 30
   A Model Context Protocol (MCP) server that integrates Volatility 3 memory forensics framework with Claude

2866. **[mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index)** - ⭐ 30
   17 MCP query tools for codebase navigation — functions, classes, imports, dependency graphs, change impact. Zero dependencies. 87% token reduction.

2867. **[AI-Tracker](https://github.com/twwch/AI-Tracker)** - ⭐ 29
   本仓库旨在整理关于大语言模型（LLM）底层逻辑、**上下文工程 (Context Engineering)** 以及 **Model Context Protocol (MCP)** 协议的核心学习资源与实战路径。

2868. **[mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai)** - ⭐ 29
   MCP (Model Context Protocol) server for Dumpling AI

2869. **[mcp-badges](https://github.com/mcpx-dev/mcp-badges)** - ⭐ 29
   Get your projects MCP (Model Context Protocol)  badges

2870. **[mcp-attr](https://github.com/frozenlib/mcp-attr)** - ⭐ 29
   A library for declaratively building Model Context Protocol servers.

2871. **[rails-pg-extras-mcp](https://github.com/pawurb/rails-pg-extras-mcp)** - ⭐ 29
   MCP (Model Context Protocol) LLM interface for rails-pg-extras gem

2872. **[luke-desktop](https://github.com/DrJonBrock/luke-desktop)** - ⭐ 29
   A modern desktop client for Claude AI with MCP server support, built with Tauri, React, and TypeScript.

2873. **[NetContextServer](https://github.com/willibrandon/NetContextServer)** - ⭐ 29
   A .NET implementation of the Model Context Protocol enabling AI assistants to explore and understand .NET codebases.

2874. **[openai-mcp-agent-dotnet](https://github.com/Azure-Samples/openai-mcp-agent-dotnet)** - ⭐ 29
   Sample to create an AI Agent using OpenAI models with any MCP server running on Azure Container Apps

2875. **[dockashell](https://github.com/anzax/dockashell)** - ⭐ 29
   DockaShell is an MCP server that gives AI agents isolated Docker containers to work in. MCP tools for shell access, file operations, and full audit trail.

2876. **[biothings-mcp](https://github.com/longevity-genie/biothings-mcp)** - ⭐ 29
   MCP (Model Context Protocol) server for biothings

2877. **[telegram-mcp-server](https://github.com/kfastov/telegram-mcp-server)** - ⭐ 29
   MCP server implementation for Telegram

2878. **[agent-pm](https://github.com/gannonh/agent-pm)** - ⭐ 29
   MCP server for the planning and execution of AI-assisted development projects.

2879. **[mcp-notify](https://github.com/aahl/mcp-notify)** - ⭐ 29
   💬  MCP Server for notify to Weixin, Telegram, Bark, Lark, 飞书, 钉钉

2880. **[rdkit-mcp-server](https://github.com/tandemai-inc/rdkit-mcp-server)** - ⭐ 29
   MCP server that enables language models to interact with RDKit through natural language

2881. **[robinhood-mcp-server](https://github.com/rohitsingh-iitd/robinhood-mcp-server)** - ⭐ 29
   The Robinhood MCP Server provides a comprehensive interface to the Robinhood Crypto API. This server handles authentication, account management, market data retrieval, and trading operations through both REST API and WebSocket interfaces.

2882. **[alibabacloud-dms-mcp-server](https://github.com/aliyun/alibabacloud-dms-mcp-server)** - ⭐ 29
   A universal multi-cloud data MCP Server supporting over 40 types of data source connections, providing secure, unified data access in a single platform. Supports full range of Alibaba Cloud services and Mainstream databases/data warehouses.

2883. **[tgcli](https://github.com/kfastov/tgcli)** - ⭐ 29
   Telegram user console client and archiver

2884. **[framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for creating and managing Framer plugins with web3 capabilities

2885. **[workflows-mcp-server](https://github.com/cyanheads/workflows-mcp-server)** - ⭐ 29
   Model Context Protocol server that enables AI agents to discover, create, and execute complex, multi-step workflows defined in simple YAML files. Allow your AI agents to better organize their tool usage and provide a more structured way to handle complex multi-step tasks.

2886. **[kaggle-mcp](https://github.com/54yyyu/kaggle-mcp)** - ⭐ 29
   Kaggle-MCP: Connect Claude AI to the Kaggle API through the Model Context Protocol (MCP), enabling competition, dataset, and kernel operations through the AI interface.

2887. **[excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)** - ⭐ 29
   A Model Context Protocol (MCP) server for reading Excel files with automatic chunking and pagination support. Built with SheetJS and TypeScript.

2888. **[TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server)** - ⭐ 29
   A comprehensive Model Context Protocol (MCP) server for market sizing analysis, TAM/SAM calculations, and industry research. Built with TypeScript, Express.js, and following the MCP  specification.

2889. **[freepik-mcp](https://github.com/freepik-company/freepik-mcp)** - ⭐ 29
   The Freepik enables popular agent Model Context Protocol (MCP) to integrate with Freepik APIs through function calling.

2890. **[bear-notes-mcp](https://github.com/bejaminjones/bear-notes-mcp)** - ⭐ 29
   MCP server for Bear app - Full Read + Write AI-powered note management with Claude Desktop

2891. **[mcpmcp-server](https://github.com/glenngillen/mcpmcp-server)** - ⭐ 29
   Discover, setup, and integrate MCP servers with your favorite clients. Unlock the full potential of AI in your daily workflow.

2892. **[notion-mcp](https://github.com/Badhansen/notion-mcp)** - ⭐ 29
   A simple Model Context Protocol (MCP) server that integrates with Notion's API to manage my personal todo list.

2893. **[powerplatform-mcp](https://github.com/michsob/powerplatform-mcp)** - ⭐ 29
   PowerPlatform Model Context Protocol server

2894. **[deno-mcp-template](https://github.com/phughesmcr/deno-mcp-template)** - ⭐ 29
   A template repo for writing and publishing local, remote, DXT, and binary MCP servers using Deno.

2895. **[enhanced-mcp-memory](https://github.com/cbunting99/enhanced-mcp-memory)** - ⭐ 29
   An enhanced MCP (Model Context Protocol) server for intelligent memory and task management, designed for AI assistants and development workflows. Features semantic search, automatic task extraction, knowledge graphs, and comprehensive project management.

2896. **[codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit)** - ⭐ 29
   Model Context Protocol server for CODESYS automation platform

2897. **[omnifocus-mcp-enhanced](https://github.com/jqlts1/omnifocus-mcp-enhanced)** - ⭐ 29
   Enhanced Model Context Protocol (MCP) server for OmniFocus with complete subtask support, perspective views (Inbox/Flagged/Forecast/Tags), ultimate   task filtering, and direct access to custom perspectives. Seamlessly integrate OmniFocus with Claude AI for intelligent task management.

2898. **[mcp-etherscan-server](https://github.com/crazyrabbitLTC/mcp-etherscan-server)** - ⭐ 29
   An MCP (Model Context Protocol) server that provides Ethereum blockchain data tools via Etherscan's API. Features include checking ETH balances, viewing transaction history, tracking ERC20 transfers, fetching contract ABIs, monitoring gas prices, and resolving ENS names.

2899. **[mcp-ollama-agent](https://github.com/ausboss/mcp-ollama-agent)** - ⭐ 29
   A TypeScript example showcasing the integration of Ollama with the Model Context Protocol (MCP) servers. This project provides an interactive command-line interface for an AI agent that can utilize the tools from multiple MCP Servers..

2900. **[mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm)** - ⭐ 29
   MCP server for Klever blockchain smart contract development

2901. **[seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** - ⭐ 29
   TypeScript Model Context Protocol (MCP) server for SEO Insights. Provides SEO tools for backlinks, keyword research, and traffic analysis. Includes CLI support and extensible structure for connecting AI systems (LLMs) to SEO APIs

2902. **[MCPSecBench](https://github.com/AIS2Lab/MCPSecBench)** - ⭐ 29
   MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols

2903. **[FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer)** - ⭐ 29
   FalkorDB-MCPServer is an MCP (Model Context Protocol) server that connects LLMs to FalkorDB

2904. **[mcp_autogen_sse_stdio](https://github.com/SaM-92/mcp_autogen_sse_stdio)** - ⭐ 29
   This repository demonstrates how to use AutoGen to integrate local and remote MCP (Model Context Protocol) servers. It showcases a local math tool (math_server.py) using Stdio and a remote Apify tool (RAG Web Browser Actor) via SSE for tasks like arithmetic and web browsing.

2905. **[bgg-mcp](https://github.com/kkjdaniel/bgg-mcp)** - ⭐ 29
   BGG MCP provides access to BoardGameGeek and a variety of board game related data through the Model Context Protocol. Enabling retrieval and filtering of board game data, user collections, and profiles.

2906. **[sketchfab-mcp-server](https://github.com/gregkop/sketchfab-mcp-server)** - ⭐ 28
   This is an MCP (Model Context Protocol) Server for discovering and downloading 3D models 

2907. **[mcp-testing-framework](https://github.com/L-Qun/mcp-testing-framework)** - ⭐ 28
   Testing framework for Model Context Protocol (MCP)

2908. **[laravel-mcp-sdk](https://github.com/mohamedahmed01/laravel-mcp-sdk)** - ⭐ 28
   Laravel Based Implementation for Model Context Protocol

2909. **[mcp-websocket](https://github.com/virajsharma2000/mcp-websocket)** - ⭐ 28
   This server implements an MCP (Model Context Protocol) server with WebSocket enhancements for real-time data updates.

2910. **[nchan-mcp-transport](https://github.com/ConechoAI/nchan-mcp-transport)** - ⭐ 28
   The best way to deploy mcp server. A high-performance WebSocket/SSE transport layer & gateway for Anthropic's MCP (Model Context Protocol) — powered by Nginx, Nchan, and FastAPI.

2911. **[vsc-mcp](https://github.com/thomasgazzoni/vsc-mcp)** - ⭐ 28
   This project provides tools that expose Language Server Protocol (LSP) functionality as MCP (Model Context Protocol) tools

2912. **[YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop)** - ⭐ 28
   An MCP (Model Context Protocol) tool that provides stock market data and trading capabilities using the yfinance library, specifically adapted for Claude Desktop.

2913. **[openapi-mcp-generator](https://github.com/abutbul/openapi-mcp-generator)** - ⭐ 28
   A Python tool that automatically converts OpenAPI(Swagger, ETAPI) compatible specifications into fully functional Model Context Protocol (MCP) servers. Generates Docker-ready implementations with support for SSE/IO communication protocols, authentication, and comprehensive error handling. https://pypi.org/project/openapi-mcp-generator/

2914. **[claude-code-mcp](https://github.com/zebbern/claude-code-mcp)** - ⭐ 28
   Model Context Protocol (MCP) servers with Claude Code. These tools dramatically enhance Claude Code's capabilities, allowing it to interact with your filesystem, web browsers, and more.

2915. **[taskflow-mcp](https://github.com/pinkpixel-dev/taskflow-mcp)** - ⭐ 28
   A task management Model Context Protocol (MCP) server that helps AI assistants break down user requests into manageable tasks with subtasks, dependencies, and notes. Enforces a structured workflow with user approval steps.

2916. **[gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp)** - ⭐ 28
   Professional Gemini API integration for Claude and all MCP-compatible hosts with intelligent model selection and advanced file handling | Smithery.ai verified

2917. **[gaia-x](https://github.com/YFGaia/gaia-x)** - ⭐ 28
   Gaia-X 基于AI新范式的下一代企业级AI应用平台。Gaia-X旨在实现类人脑的、针对企业办公业务场景的AI化赋能，包括一系列新颖而稳定的企业级AI功能，包括不限于：企业级管理功能、MCP Server支持（且支持将企业内部系统API转换为MCP Server提供服务）、支持自然语言驱动的RPA（大模型操作电脑）、划词分析和悬浮球等。

2918. **[tempo-mcp-server](https://github.com/ivelin-web/tempo-mcp-server)** - ⭐ 28
   MCP server for managing Tempo worklogs in Jira

2919. **[mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff)** - ⭐ 28
   ESPN Fantasy API with LLMs!

2920. **[Healthcare-MCP](https://github.com/innovaccer/Healthcare-MCP)** - ⭐ 28
   Specification and documentation for the Healthcare Model Context Protocol. This builds on top of the base Model Context Protocol

2921. **[touchdesigner-mcp-server](https://github.com/bottobot/touchdesigner-mcp-server)** - ⭐ 28
   TouchDesigner Documentation MCP Server v2.6.1 - FIXED Python API tools! Features 629 operators + 14 tutorials + 69 Python API classes with working get_python_api & search_python_api tools. Zero-configuration setup for VS Code/Codium.

2922. **[src-to-kb](https://github.com/vezlo/src-to-kb)** - ⭐ 28
   Convert source code to LLM ready knowledge base

2923. **[MCP-BOE](https://github.com/ComputingVictor/MCP-BOE)** - ⭐ 28
   MCP server para el BOE 🇪🇸 — Acceso a legislación consolidada, sumarios diarios y tablas oficiales del Boletín Oficial del Estado mediante Model Context Protocol y API REST.

2924. **[whistle-mcp](https://github.com/7gugu/whistle-mcp)** - ⭐ 28
   A Whistle proxy management tool based on Model Context Protocol that allows AI assistants to directly control local Whistle proxy servers, simplifying network debugging, API testing, and proxy rule configuration through natural language interaction.

2925. **[mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)** - ⭐ 28
   A Model Context Protocol (MCP) server for Caiyun (ColorfulClouds) Weather.

2926. **[mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy)** - ⭐ 28
   a web logging proxy for MCP client-server communication

2927. **[mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack)** - ⭐ 28
   Model Context Protocol to bridge in Substack writings to Claude.

2928. **[zillow-mcp-server](https://github.com/sap156/zillow-mcp-server)** - ⭐ 28
   Zillow MCP Server for real estate data access via the Model Context Protocol

2929. **[ai-foundry-agents-samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)** - ⭐ 28
   Azure AI Foundry - Agents related sample code

2930. **[mcp-proxy](https://github.com/stephenlacy/mcp-proxy)** - ⭐ 28
   Fast rust MCP proxy between stdio and SSE

2931. **[laravel-mcp-companion](https://github.com/brianirish/laravel-mcp-companion)** - ⭐ 28
   A Laravel developer's MCP companion. Get the absolute best advice, recommendations, and up-to-date documentation for the entire Laravel ecosystem.

2932. **[google-search-console-mcp-server](https://github.com/Shin-sibainu/google-search-console-mcp-server)** - ⭐ 28
   Model Context Protocol server for Google Search Console API - integrate with Claude Code and Claude Desktop

2933. **[MCPServer](https://github.com/rhennigan/MCPServer)** - ⭐ 28
   Implements a model context protocol server using Wolfram Language

2934. **[nettune](https://github.com/jtsang4/nettune)** - ⭐ 28
   A network diagnostics and TCP optimization tool with MCP (Model Context Protocol) integration for AI-assisted configuration.

2935. **[alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server)** - ⭐ 28
   A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open API through a standardized interface. This implementation is based on the Aliyun Open API and enables AI agents to perform cloud resources operations seamlessly.

2936. **[mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy)** - ⭐ 28
   An implementation of Giphy integration with Model Context Protocol

2937. **[MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP)** - ⭐ 28
   Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered search and vision analysis APIs optimized for code development workflows

2938. **[drawio-mcp-server](https://github.com/simonkurtz-MSFT/drawio-mcp-server)** - ⭐ 28
   A Model Context Protocol (MCP) server for programmatic diagram generation using Draw.io (Diagrams.net). This server generates Draw.io XML directly — no browser extension or Draw.io instance required.

2939. **[MCPbundler](https://github.com/eugenepyvovarov/MCPbundler)** - ⭐ 28

2940. **[izan.io](https://github.com/ekingunoncu/izan.io)** - ⭐ 28
   Turn Any Browser Action & Data Extraction into an AI Tool in 60 Seconds

2941. **[gtm-mcp-server](https://github.com/paolobietolini/gtm-mcp-server)** - ⭐ 28
   An MCP server for Google Tag Manager. Connect it to your LLM, authenticate once, and start managing GTM through natural language.

2942. **[Unity-AI-Animation](https://github.com/IvanMurzak/Unity-AI-Animation)** - ⭐ 28
   AI-powered tools for Unity animation workflow. Create and modify AnimationClips and AnimatorControllers directly through natural language commands.

2943. **[mssqlclient-mcp-server](https://github.com/aadversteeg/mssqlclient-mcp-server)** - ⭐ 28
   A Microsoft SQL Server client implementing the Model Context Protocol (MCP). This server provides SQL query capabilities through a simple MCP interface.

2944. **[Memgpt-MCP-Server](https://github.com/Vic563/Memgpt-MCP-Server)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides persistent memory and multi-model LLM support.

2945. **[aws-mcp](https://github.com/lokeswaran-aj/aws-mcp)** - ⭐ 27
   An MCP(Model Context Protocol) Server for AWS services

2946. **[mcpc](https://github.com/apify/mcpc)** - ⭐ 27
   Universal command-line client for the Model Context Protocol (MCP)

2947. **[VercelGenUI_MCP](https://github.com/JamesSloan/VercelGenUI_MCP)** - ⭐ 27
   Proof of concept chat AI combining the Model Context Protocol (MCP) with Vercel's AI SDK UI

2948. **[mcp](https://github.com/supadata-ai/mcp)** - ⭐ 27
   Official Supadata MCP Server - Adds powerful video & web scraping to Cursor, Claude and any other LLM clients.

2949. **[google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)** - ⭐ 27
   A Model Context Protocol server for Google Workspace integration (Gmail and Calendar)

2950. **[mcp-web-browser](https://github.com/random-robbie/mcp-web-browser)** - ⭐ 27
   An advanced web browsing server for the Model Context Protocol (MCP) powered by Playwright, enabling headless browser interactions through a flexible, secure API.

2951. **[directus-mcp-server](https://github.com/rijkvanzanten/directus-mcp-server)** - ⭐ 27
   Model Context Protocol server for Directus

2952. **[Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server)** - ⭐ 27
   PRIMS is a lightweight, open-source Model Context Protocol (MCP) server that lets LLM agents safely execute arbitrary Python code in a secure, throw-away sandbox.

2953. **[nimbletools-core](https://github.com/NimbleBrainInc/nimbletools-core)** - ⭐ 27
   NimbleTools is an open-source MCP runtime. Infrastructure for the agentic web.

2954. **[mcp-stytch-consumer-todo-list](https://github.com/stytchauth/mcp-stytch-consumer-todo-list)** - ⭐ 27
   Workers + Stytch TODO App MCP Server

2955. **[mindbridge-mcp](https://github.com/pinkpixel-dev/mindbridge-mcp)** - ⭐ 27
   MindBridge is an AI orchestration MCP server that lets any app talk to any LLM — OpenAI, Anthropic, DeepSeek, Ollama, and more — through a single unified API. Route queries, compare models, get second opinions, and build smarter multi-LLM workflows.

2956. **[php-mcp](https://github.com/dtyq/php-mcp)** - ⭐ 27
   A complete PHP implementation of the Model Context Protocol (MCP) with server and client support, STDIO and HTTP transports, and framework integration

2957. **[FerrumMCP](https://github.com/Eth3rnit3/FerrumMCP)** - ⭐ 27
   A Model Context Protocol (MCP) server that provides web automation capabilities through Ferrum, with optional BotBrowser integration for advanced anti-detection features. This enables AI agents to interact with web pages seamlessly.

2958. **[vision-one-mcp-server](https://github.com/trendmicro/vision-one-mcp-server)** - ⭐ 27
   The Trend Vision One Model Context Protocol (MCP) Server enables natural language interaction between your favourite AI tooling and the Trend Vision One web APIs.  This allows users to harness the power of Large Language Models (LLM) to interpret and respond to security events.

2959. **[brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server)** - ⭐ 27
   A MCP (Model Context Protocol) server for agent-driven research on Brazilian law using official sources

2960. **[review-flow](https://github.com/DGouron/review-flow)** - ⭐ 27
   Automated AI code reviews powered — webhook-driven, real-time dashboard, MCP integration, smart queue with deduplication, multi-agent audits, and iterative follow-up reviews for GitLab MRs and GitHub PRs

2961. **[pulse-editor](https://github.com/ClayPulse/pulse-editor)** - ⭐ 27
   Vibe code on any device, and scale your apps with visual workflows. Pulse Editor is a modular, cross-platform, AI-powered productivity platform with federated app collaboration and extensible workflows. 

2962. **[mcp-config-manager](https://github.com/holstein13/mcp-config-manager)** - ⭐ 27
   Manage MCP server configs across Claude, Gemini & other AI systems. Interactive CLI for server enable/disable, preset management & config sync.

2963. **[Wwise-MCP](https://github.com/BilkentAudio/Wwise-MCP)** - ⭐ 27
   Wwise-MCP is a Model Context Protocol server that allows LLMs to interact with the Wwise Authoring application. It exposes tools from a custom python waapi function library to MCP clients.

2964. **[jdwp-mcp](https://github.com/navicore/jdwp-mcp)** - ⭐ 27
   Java debugging for LLMs via JDWP and Model Context Protocol

2965. **[mcp-local-dev](https://github.com/txbm/mcp-local-dev)** - ⭐ 27
   Let LLMs manage your local dev environments

2966. **[kernel-mcp-server](https://github.com/kernel/kernel-mcp-server)** - ⭐ 27
   Open-source MCP server for secure, low-latency cloud-browser automation on Kernel.

2967. **[cheat-engine-server-python](https://github.com/bethington/cheat-engine-server-python)** - ⭐ 27
   MCP Cheat Engine Server — provides safe, structured read-only access to memory analysis and debugging functionality through the Model Context Protocol (MCP). For developers, security researchers, and game modders.

2968. **[RevitMCP](https://github.com/oakplank/RevitMCP)** - ⭐ 27
   model context protocol for Autodesk Revit

2969. **[metabase-mcp-server](https://github.com/hyeongjun-dev/metabase-mcp-server)** - ⭐ 27
   A Model Context Protocol server that integrates AI assistants with Metabase analytics platform

2970. **[camofox-mcp](https://github.com/redf0x1/camofox-mcp)** - ⭐ 27
   Anti-detection browser MCP server for AI agents — navigate, interact, and automate the web without getting blocked

2971. **[godot-mcp](https://github.com/HaD0Yun/godot-mcp)** - ⭐ 27
   GoPeak — The most comprehensive MCP server for Godot Engine. 95+ tools: scene management, GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, CC0 asset library. npx gopeak

2972. **[mcp-structured-thinking](https://github.com/Promptly-Technologies-LLC/mcp-structured-thinking)** - ⭐ 26
   A TypeScript Model Context Protocol (MCP) server to allow LLMs to programmatically construct mind maps to explore an idea space, with enforced "metacognitive" self-reflection

2973. **[mcp-frontend-testing](https://github.com/StudentOfJS/mcp-frontend-testing)** - ⭐ 26
   Frontend testing tools for Model Context Protocol

2974. **[do-remote-mcp-server-template](https://github.com/do-community/do-remote-mcp-server-template)** - ⭐ 26
   A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution

2975. **[pptx-xlsx-mcp](https://github.com/jenstangen1/pptx-xlsx-mcp)** - ⭐ 26
   Antrophics Model context protocol to edit powerpoint files

2976. **[minds-mcp](https://github.com/mindsdb/minds-mcp)** - ⭐ 26
   An MCP (Model Context Protocol) server for Minds, allowing LLMs to interact with the Minds SDK through a standardized interface.

2977. **[mcp-client-x](https://github.com/RGGH/mcp-client-x)** - ⭐ 26
   Python MCP client + server example

2978. **[mcp-gateway](https://github.com/lucky-aeon/mcp-gateway)** - ⭐ 26
   The MCP gateway is a reverse proxy server that forwards requests from clients to the MCP server or uses all MCP servers under the gateway through a unified portal.

2979. **[langchain-mcp-tools-py](https://github.com/hideya/langchain-mcp-tools-py)** - ⭐ 26
   MCP to LangChain Tools Conversion Utility / Python

2980. **[MalwareBazaar_MCP](https://github.com/mytechnotalent/MalwareBazaar_MCP)** - ⭐ 26
   An AI-driven MCP server that autonomously interfaces with Malware Bazaar, delivering real-time threat intel and sample metadata for authorized cybersecurity research workflows.

2981. **[ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server written in Python for natural language interaction with the TON blockchain 💎

2982. **[nebulagraph-mcp-server](https://github.com/nebula-contrib/nebulagraph-mcp-server)** - ⭐ 26
   Model Context Protocol Server for NebulaGraph 3.x

2983. **[taiwan-holiday-mcp](https://github.com/lis186/taiwan-holiday-mcp)** - ⭐ 26
   一個基於 Model Context Protocol (MCP) 的台灣假期查詢伺服器，為 AI 工具提供準確的台灣國定假日資訊。

2984. **[MCP-Developer-SubAgent](https://github.com/gensecaihq/MCP-Developer-SubAgent)** - ⭐ 26
    A specialized framework for Model Context Protocol (MCP) development featuring 8   Claude Code sub-agents, security hooks, and production-ready FastMCP server   templates. Provides immediate MCP development assistance through markdown-driven   agents with optional programmatic SDK .

2985. **[mcp-auth](https://github.com/famma-ai/mcp-auth)** - ⭐ 26
   MCP Auth via Reverse Proxy 

2986. **[mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver)** - ⭐ 26
   Simple MCP to give Claude ability to check current time as well as know when holidays are, what is the time distance between dates etc.

2987. **[turn-based-game-mcp](https://github.com/github-samples/turn-based-game-mcp)** - ⭐ 26
   A turn-based games app built with Next.js and TypeScript that features Tic-Tac-Toe and Rock Paper Scissors games with AI opponents powered by the Model Context Protocol (MCP), offering three difficulty levels.

2988. **[semrush-mcp](https://github.com/mrkooblu/semrush-mcp)** - ⭐ 26
   A Model Context Protocol (MCP) server implementation that provides tools for accessing Semrush API data.

2989. **[chatbot_Shopify](https://github.com/Mobeen-Dev/chatbot_Shopify)** - ⭐ 26
   Agentic Shopify Chatbot with MCP integration, embedded directly into Shopify via a Theme Extension

2990. **[symfony-mcp-server](https://github.com/klapaudius/symfony-mcp-server)** - ⭐ 26
   A Symfony package designed for building secure servers based on the Model Context Protocol, utilizing Server-Sent Events (SSE) and/or StreamableHTTP for real-time communication. It offers a scalable tool system tailored for enterprise-grade applications.

2991. **[greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server)** - ⭐ 26
   A Model Context Protocol (MCP) server for GreptimeDB

2992. **[clay-mcp](https://github.com/clay-inc/clay-mcp)** - ⭐ 26
   A simple Model Context Protocol (MCP) server for Clay.

2993. **[mcp-server-starter-ts](https://github.com/alexanderop/mcp-server-starter-ts)** - ⭐ 26
   A minimal TypeScript starter template for building Model Context Protocol (MCP) servers.

2994. **[arch-mcp](https://github.com/nihalxkumar/arch-mcp)** - ⭐ 26
   Arch Linux MCP (Model Context Protocol)

2995. **[wiki-js-mcp](https://github.com/talosdeus/wiki-js-mcp)** - ⭐ 26
   Model Context Protocol (MCP) server for Wiki.js with hierarchical documentation & Docker setup

2996. **[relace-mcp](https://github.com/possible055/relace-mcp)** - ⭐ 26
   Unofficial Relace MCP client with AI features. Personal project; not affiliated with or endorsed by Relace

2997. **[Unity-AI-ProBuilder](https://github.com/IvanMurzak/Unity-AI-ProBuilder)** - ⭐ 26
   AI-powered 3D modeling tools for Unity ProBuilder. Enables AI assistants to create and manipulate editable meshes through natural language commands. Create primitive shapes, extrude faces, bevel edges, apply materials, merge objects, and perform advanced mesh operations like bridging and subdivision.

2998. **[unplugin-devpilot](https://github.com/zcf0508/unplugin-devpilot)** - ⭐ 26
   A universal plugin framework for development tools that enables seamless browser-server communication and MCP (Model Context Protocol) integration with AI/LLM systems.

2999. **[php-mcp-sdk](https://github.com/dalehurley/php-mcp-sdk)** - ⭐ 26
   PHP implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.  ✨ Features  🚀 Complete MCP Protocol Support - Full implementation of the MCP specification 🔧 Type-Safe - Leverages PHP 8.1+ type system with enums, union types, and strict typing ⚡ Async First

3000. **[mcp-ffmpeg-helper](https://github.com/sworddut/mcp-ffmpeg-helper)** - ⭐ 26
   一个基于 Model Context Protocol (MCP) 的 FFmpeg 辅助工具，提供视频处理功能。

3001. **[mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify)** - ⭐ 26
   An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).

3002. **[fast-mcp-telegram](https://github.com/leshchenko1979/fast-mcp-telegram)** - ⭐ 26
   Telegram MCP Server and HTTP-MTProto bridge | Multi-user auth, intelligent search, file sending, web setup | Docker & PyPI ready

3003. **[batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate)** - ⭐ 26
   Model Context Protocol (MCP) server for BatchData.io property and address APIs - Real estate data integration for Claude and other AI assistants

3004. **[congressMCP](https://github.com/amurshak/congressMCP)** - ⭐ 26
   An MCP server allowing AI agents and MCP clients to interface with the Congress.gov API

3005. **[mcp_xpp](https://github.com/ccampora/mcp_xpp)** - ⭐ 26
   Experimental MCP server for Dynamics 365 F&O X++ development. Provides object creation, modification, and codebase navigation through the Model Context Protocol. Includes VS2022 service integration for D365 object handling.

3006. **[mcp-chain-of-draft-server](https://github.com/bsmi021/mcp-chain-of-draft-server)** - ⭐ 25
   Chain of Draft Server is a powerful AI-driven tool that helps developers make better decisions through systematic, iterative refinement of thoughts and designs. It integrates seamlessly with popular AI agents and provides a structured approach to reasoning, API design, architecture decisions, code reviews, and implementation planning.

3007. **[alpaca-mcp-server](https://github.com/tedlikeskix/alpaca-mcp-server)** - ⭐ 25
   Model Context Protocol (MCP) server for Alpaca trading API

3008. **[gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server)** - ⭐ 25
   Official Model Context Protocol server for Gyazo

3009. **[mcp-php](https://github.com/garyblankenship/mcp-php)** - ⭐ 25
   model context protocol or mcp for php laravel

3010. **[mcp-media-processor](https://github.com/maoxiaoke/mcp-media-processor)** - ⭐ 25
   A Node.js server implementing Model Context Protocol (MCP) for media processing operations, providing powerful video and image manipulation capabilities.

3011. **[mcp-webdriveragent](https://github.com/AppiumTestDistribution/mcp-webdriveragent)** - ⭐ 25
   This is a Model Context Protocol (MCP) server that provides tools for building and signing WebDriverAgent for iOS.

3012. **[mcp-manager](https://github.com/nstebbins/mcp-manager)** - ⭐ 25
   CLI tool for managing Model Context Protocol (MCP) servers in one place & using them across them different clients

3013. **[mcp-server-semgrep](https://github.com/VetCoders/mcp-server-semgrep)** - ⭐ 25
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3014. **[deep-research-mcp](https://github.com/pinkpixel-dev/deep-research-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) compliant server designed for comprehensive web research. It uses Tavily's Search and Crawl APIs to gather detailed information on a given topic, then structures this data in a format perfect for LLMs to create high-quality markdown documents.

3015. **[puzzlebox](https://github.com/cliffhall/puzzlebox)** - ⭐ 25
   An MCP server that hosts finite state machines as dynamic resources that multiple clients can subscribe to and be updated when their state changes.

3016. **[Tiny-OAI-MCP-Agent](https://github.com/jalr4ever/Tiny-OAI-MCP-Agent)** - ⭐ 25
   A MCP protocol agent that operates a SQLite using natural language by OpenAI-Compatible LLM.

3017. **[slack-mcp-server](https://github.com/AVIMBU/slack-mcp-server)** - ⭐ 25
   A Model Context Protocol Server for Interacting with Slack

3018. **[systemprompt-mcp-notion](https://github.com/Ejb503/systemprompt-mcp-notion)** - ⭐ 25
   This an Model Context Protocol (MCP) server that integrates Notion into your AI workflows. This server enables seamless access to Notion through MCP, allowing AI agents to interact with pages, databases, and comments.

3019. **[mcp_rss](https://github.com/buhe/mcp_rss)** - ⭐ 25
   MCP RSS is a Model Context Protocol (MCP) server for interacting with RSS feeds.

3020. **[agent-hub-mcp](https://github.com/gilbarbara/agent-hub-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server that enables communication and coordination between multiple AI agents

3021. **[meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp)** - ⭐ 25
   Model Context Protocol server for AI assistants to create meeting bots, search transcripts, and manage meeting recordings.

3022. **[mcp_streamable_http](https://github.com/theailanguage/mcp_streamable_http)** - ⭐ 25
   Educational repo for MCP streamable HTTP servers and clients

3023. **[ccmcp](https://github.com/gsong/ccmcp)** - ⭐ 25
   A CLI tool that intelligently discovers, validates, and selects MCP (Model Context Protocol) server configurations for Claude Code.

3024. **[awesome-mcp-lists](https://github.com/collabnix/awesome-mcp-lists)** - ⭐ 25
   A Curated List of MCP Servers, Clients and Toolkits

3025. **[mcp-slicer](https://github.com/zhaoyouj/mcp-slicer)** - ⭐ 25
   A Model Context Protocol server for 3D Slicer integration

3026. **[nestjs-mcp](https://github.com/bamada/nestjs-mcp)** - ⭐ 25
   NestJS module for seamless Model Context Protocol (MCP) server integration using decorators.

3027. **[apifox-mcp](https://github.com/iwen-conf/apifox-mcp)** - ⭐ 25
   Apifox MCP 服务器 - 让 Claude 等 AI 助手通过自然语言管理你的 Apifox 项目，轻松创建、更新和审计 API 接口

3028. **[lucide-icons-mcp](https://github.com/SeeYangZhi/lucide-icons-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server exposing Lucide icons as resources and tools for LLMs and agentic applications. Built with Bun and the MCP TypeScript SDK.

3029. **[github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp)** - ⭐ 25
   Model Context Protocol server for Github Repo // Reading Github Repo

3030. **[aistudio-mcp-server](https://github.com/eternnoir/aistudio-mcp-server)** - ⭐ 25
   Google AI Studio MCP Server - Powerful Gemini API integration for Model Context Protocol with multi-modal file processing, PDF-to-Markdown conversion, image analysis,   and audio transcription capabilities. Supports all Gemini 2.5 models with comprehensive file format support.

3031. **[mcp-annotated-java-sdk](https://github.com/thought2code/mcp-annotated-java-sdk)** - ⭐ 25
   Annotation-driven MCP dev 🚀 No Spring, Zero Boilerplate, Pure Java

3032. **[PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP)** - ⭐ 25
   The universal MCP server for Claude Code and other MCP-compatible clients. One installation gives AI access to 10,000+ PowerShell modules and any CLI tool. You and AI collaborate in the same console with full transparency. Supports Windows, Linux, and macOS.

3033. **[openai-copilot](https://github.com/feiskyer/openai-copilot)** - ⭐ 25
   Your life Copilot powered by LLM models (CLI interface for LLM models with MCP tools).

3034. **[MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity)** - ⭐ 25
   MCP Server + Plugin for Unity Editor and Unity game. The Plugin allows to connect to MCP clients like Claude Desktop or others.

3035. **[mcp-desktop-automation](https://github.com/tanob/mcp-desktop-automation)** - ⭐ 25
   A Model Context Protocol server that provides desktop automation capabilities using RobotJS and screenshot capabilities

3036. **[deep-research](https://github.com/ssdeanx/deep-research)** - ⭐ 25
   The Deep Research Assistant is meticulously crafted on Mastra's modular, scalable architecture, designed for intelligent orchestration and seamless human-AI interaction. It's built to tackle complex research challenges autonomously.

3037. **[kratos-mcp](https://github.com/ceorkm/kratos-mcp)** - ⭐ 25
   🏛️ Memory System for AI Coding Tools - Never explain your codebase again. MCP server with perfect project isolation, 95.8% context accuracy, and the Four Pillars Framework.

3038. **[json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server)** - ⭐ 25
   Message Communication Protocol server for json2video API integration

3039. **[fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server)** - ⭐ 25
   A model context protocol (MCP) server for Autodesk Fusion that provides resources and tools from ADSK to an AI client such as Claude or Cursor.

3040. **[ebay-mcp](https://github.com/YosefHayim/ebay-mcp)** - ⭐ 25
   Open source local MCP server providing AI assistants with comprehensive access to eBay's Sell APIs. Includes 325 tools for inventory management, order fulfillment, marketing campaigns, analytics, developer tools, and more.

3041. **[mcp-playground](https://github.com/zanetworker/mcp-playground)** - ⭐ 25
   Simple MCP Client for remote MCP Servers 🌐

3042. **[silverbullet-mcp](https://github.com/Ahmad-A0/silverbullet-mcp)** - ⭐ 25
   A Model Context Protocol (MCP) server to interact with your SilverBullet notes and data.

3043. **[opnsense-mcp-server](https://github.com/Pixelworlds/opnsense-mcp-server)** - ⭐ 25
   Modular MCP server for OPNsense firewall management - 88 tools providing access to 2000+ methods through AI assistants

3044. **[help-scout-mcp-server](https://github.com/drewburchfield/help-scout-mcp-server)** - ⭐ 25
   MCP server for Help Scout - search conversations, threads, and inboxes with AI agents

3045. **[prometheus-mcp](https://github.com/idanfishman/prometheus-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation that provides AI agents with programmatic access to Prometheus metrics via a unified interface.

3046. **[GenomeMCP](https://github.com/Eldergenix/GenomeMCP)** - ⭐ 24
   An AI-driven genomic intelligence system delivering structured ClinVar interpretation and high-precision exon, intron, and gene queries using the Model Context Protocol (MCP).

3047. **[Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop](https://github.com/gloveboxes/Unlock-your-agents-potential-with-Model-Context-Protocol-PostgreSQL-Workshop)** - ⭐ 24

3048. **[opnsense-mcp-server](https://github.com/floriangrousset/opnsense-mcp-server)** - ⭐ 24
   A Model Context Protocol (MCP) server implementation for managing OPNsense firewalls. This server allows Claude and other MCP-compatible clients to interact with all features exposed by the OPNsense API.

3049. **[n8n-AI-agent-DVM-MCP-client](https://github.com/r0d8lsh0p/n8n-AI-agent-DVM-MCP-client)** - ⭐ 24
   An AI agent built in n8n which can find and use Model Context Protocol (MCP) Server Tools served as Data Vending Machines (DVM) over the Nostr network.

3050. **[mcp-server-semgrep](https://github.com/Szowesgad/mcp-server-semgrep)** - ⭐ 24
   MCP Server Semgrep is a [Model Context Protocol](https://modelcontextprotocol.io) compliant server that integrates the powerful Semgrep static analysis tool with AI assistants like Anthropic Claude. It enables advanced code analysis, security vulnerability detection, and code quality improvements directly through a conversational interface.

3051. **[python-sequential-thinking-mcp](https://github.com/XD3an/python-sequential-thinking-mcp)** - ⭐ 24
   A Python implementation of the Sequential Thinking MCP server using the official Model Context Protocol (MCP) Python SDK. This server facilitates a detailed, step-by-step thinking process for problem-solving and analysis.

3052. **[MCP](https://github.com/EduBase/MCP)** - ⭐ 24
   The EduBase MCP server enables Claude and other LLMs to interact with EduBase's comprehensive e-learning platform through the Model Context Protocol (MCP).

3053. **[mcp-task-manager-server](https://github.com/bsmi021/mcp-task-manager-server)** - ⭐ 24
   A local Model Context Protocol (MCP) server providing backend tools for client-driven project and task management using a SQLite database.

3054. **[DeepResearchMCP](https://github.com/ameeralns/DeepResearchMCP)** - ⭐ 24
   Deep Research MCP is an intelligent research assistant built on the Model Context Protocol (MCP) that performs comprehensive, multi-step research on any topic.

3055. **[mcp-template-dotnet](https://github.com/NikiforovAll/mcp-template-dotnet)** - ⭐ 24
   This repository contains a template for creating a Model Context Protocol (MCP) applications in .NET.

3056. **[Awesome-MCP](https://github.com/Albertchamberlain/Awesome-MCP)** - ⭐ 24
   Awesome-MCP Servers & Clients & Funny things

3057. **[calendar-mcp](https://github.com/deciduus/calendar-mcp)** - ⭐ 24
   This project implements a Python-based MCP (Model Context Protocol) server that acts as an interface between Large Language Models (LLMs) and the Google Calendar API. It enables LLMs to perform calendar operations via natural language requests.

3058. **[readwise-vector-db](https://github.com/leonardsellem/readwise-vector-db)** - ⭐ 24
   Turn your Readwise library into a blazing-fast, self-hosted semantic search engine – complete with nightly syncs, vector search API, Prometheus metrics, and a streaming MCP server for LLM clients.

3059. **[cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server)** - ⭐ 24
   An MCP server enabling CFBD API queries within Claude Desktop.

3060. **[mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock)** - ⭐ 24
   Model Context Procotol(MCP) server for using Amazon Bedrock Nova Canvas to generate images

3061. **[k6-mcp-server](https://github.com/QAInsights/k6-mcp-server)** - ⭐ 24
   k6 MCP server

3062. **[bzm-mcp](https://github.com/Blazemeter/bzm-mcp)** - ⭐ 24
   Official BlazeMeter MCP Server for AI-driven performance testing

3063. **[mcp-client-agent](https://github.com/shane-kercheval/mcp-client-agent)** - ⭐ 24
   CLI that uses DSPy to interact with MCP servers.

3064. **[roo-logger](https://github.com/annenpolka/roo-logger)** - ⭐ 24
   An MCP server for logging activity in Roo Code/Cline.

3065. **[identity-spec](https://github.com/agntcy/identity-spec)** - ⭐ 24
   AGNTCY Identity allows to onboard, create and verify identities for Agents, Model Context Protocol (MCP) Servers and Multi-Agent Systems (MASs).

3066. **[cursor-db-mcp](https://github.com/jbdamask/cursor-db-mcp)** - ⭐ 24
   Model Context Protocol server for querying Cursor chat history

3067. **[d365fo-client](https://github.com/mafzaal/d365fo-client)** - ⭐ 24
   A comprehensive Python client library and MCP server for Microsoft Dynamics 365 Finance & Operations (D365 F&O) that provides easy access to OData endpoints, metadata operations, label management, and AI assistant integration.

3068. **[lua-resty-mcp](https://github.com/ufownl/lua-resty-mcp)** - ⭐ 24
   Model Context Protocol SDK implemented in Lua for OpenResty

3069. **[solana-mcp](https://github.com/tony-42069/solana-mcp)** - ⭐ 24
   A comprehensive Solana MCP (Model Context Protocol) server for analyzing memecoins, tracking trends, and providing AI-powered insights using cultural analysis and on-chain data.

3070. **[aj-mcp](https://github.com/lightweight-component/aj-mcp)** - ⭐ 24
   Simple MCP SDK in Java

3071. **[skill-mcp](https://github.com/fkesheh/skill-mcp)** - ⭐ 24
   LLM-managed skills platform using MCP - create, edit, and execute skills programmatically in Claude, Cursor, and any MCP-compatible client without manual file uploads.

3072. **[codingbuddy](https://github.com/JeremyDev87/codingbuddy)** - ⭐ 24
   Codingbuddy orchestrates 29 specialized AI agents to deliver code quality comparable to a team of human experts through a PLAN → ACT → EVAL workflow.

3073. **[jsonv-ts](https://github.com/dswbx/jsonv-ts)** - ⭐ 24
   JSON Schema builder and validator for TypeScript with static type inference, Hono middleware for OpenAPI generation and validation, and MCP server/client implementation. Lightweight, dependency-free, and built on Web Standards.

3074. **[mcp-mesh](https://github.com/dhyansraj/mcp-mesh)** - ⭐ 24
   Enterprise-grade distributed AI agent framework | Develop → Deploy → Observe | K8s-native | Dynamic DI | Auto-failover | Multi-LLM | Python + Java + TypeScript

3075. **[holoviz-mcp](https://github.com/MarcSkovMadsen/holoviz-mcp)** - ⭐ 24
   ✨A MCP server that provides intelligent access to the HoloViz ecosystem for humans and AIs.

3076. **[mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator)** - ⭐ 24
   Model Context Protocol Server for aggregating RSS feeds in Claude Desktop

3077. **[agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp)** - ⭐ 24
   A Model Context Protocol (MCP) server that integrates with X using the @elizaOS `agent-twitter-client` package, allowing AI models to interact with Twitter without direct API access.

3078. **[server-sharepoint](https://github.com/Zerg00s/server-sharepoint)** - ⭐ 24
   This is a MCP server for Claude Desktop that allows you to interact with SharePoint Online using the SharePoint REST API. It is designed to be used with the [Claude Desktop](https://claude.ai/download) app, but could be used by other MCP clients as well.

3079. **[Excel-MCP-Server-Master](https://github.com/guillehr2/Excel-MCP-Server-Master)** - ⭐ 24
   Excel MCP Server - Manipulate Excel files without Microsoft Excel. Model Context Protocol for XLSX, XLSM with Claude AI integration

3080. **[Model-Context-Protocol](https://github.com/Coding-Crashkurse/Model-Context-Protocol)** - ⭐ 23

3081. **[jigsawstack-mcp-server](https://github.com/JigsawStack/jigsawstack-mcp-server)** - ⭐ 23
   Model Context Protocol Server that allows AI models to interact with JigsawStack models!

3082. **[cortex](https://github.com/FreePeak/cortex)** - ⭐ 23
   A declarative platform for building Model Context Protocol (MCP) servers in Golang—exposing tools, resources & prompts in a clean, structured way

3083. **[paraview_mcp](https://github.com/LLNL/paraview_mcp)** - ⭐ 23
   ParaView-MCP integrates multimodal LLMs with ParaView via Model Context Protocol, enabling natural language control of scientific visualizations. The agent observes the viewport for visual feedback, making complex visualization tool accessible to all users while providing intelligent automation for experts.

3084. **[lineshopping-api-mcp](https://github.com/woraphol-j/lineshopping-api-mcp)** - ⭐ 23
   Model Context Protocol (MCP) server for the LINE SHOPPING API. Enables AI agents and tools to manage products, inventory, orders, and settlements on LINE SHOPPING via auto-generated MCP tools from the official OpenAPI spec.

3085. **[home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) integration that enables AI assistants to search for and control Home Assistant devices through natural language commands in Cursor.

3086. **[mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** - ⭐ 23
   Model Context Protocol Server for Accessing twitter

3087. **[strava-mcp](https://github.com/kw510/strava-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server with Strava OAuth integration, built on Cloudflare Workers. Enables secure authentication and tool access for MCP clients like Claude and Cursor through Strava login. Perfect for developers looking to integrate Strava authentication with AI tools.

3088. **[mcp-community](https://github.com/Mirascope/mcp-community)** - ⭐ 23
   Easily run, deploy, and connect to MCP servers

3089. **[aisdk-mcp-bridge](https://github.com/vrknetha/aisdk-mcp-bridge)** - ⭐ 23
   Bridge package enabling seamless integration between Model Context Protocol (MCP) servers and AI SDK tools. Supports multiple server types, real-time communication, and TypeScript.

3090. **[nlweb-net](https://github.com/nlweb-ai/nlweb-net)** - ⭐ 23
   The official .NET 9 implementation of the NLWeb protocol for building natural language web interfaces with support for List, Summarize, and Generate query modes, plus Model Context Protocol (MCP) integration for AI clients.

3091. **[mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)** - ⭐ 23
   A personal assistant AI agent built with the Model Context Protocol (MCP)

3092. **[microsoft_fabric_mcp](https://github.com/Augustab/microsoft_fabric_mcp)** - ⭐ 23
   MCP server wrapping around the Fabric Rest API

3093. **[lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server)** - ⭐ 23
   A MCP(Model Context Protocol) server that accesses to Lightdash

3094. **[balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp)** - ⭐ 23
   An MCP Server implementation that integrates the Balldontlie API, to provide information about players, teams and games for the NBA, NFL and MLB

3095. **[slack-mcp-client](https://github.com/csonigo/slack-mcp-client)** - ⭐ 23
   An MCP client for slack in Typescript

3096. **[fastify-mcp-server](https://github.com/flaviodelgrosso/fastify-mcp-server)** - ⭐ 23
   Fastify plugin to easily spin up Model Context Protocol (MCP) HTTP servers

3097. **[codemesh](https://github.com/kiliman/codemesh)** - ⭐ 23
   The Self-Improving MCP Server - Agents write code to orchestrate multiple MCP servers with intelligent TypeScript execution and auto-augmentation

3098. **[azure-diagram-mcp](https://github.com/dminkovski/azure-diagram-mcp)** - ⭐ 23
   MCP server that turns natural-language prompts into Microsoft Azure architecture diagrams (PNG) using Python Diagrams + Graphviz.

3099. **[MCP-123](https://github.com/Tylersuard/MCP-123)** - ⭐ 23
   The easiest possible implementation of an MCP server and client.  Set up a server or a client in 2 lines of code.

3100. **[cf-mcp-client](https://github.com/cpage-pivotal/cf-mcp-client)** - ⭐ 23
   Tanzu Platform Chat

3101. **[fastify-mcp](https://github.com/haroldadmin/fastify-mcp)** - ⭐ 23
   A Fastify plugin to run Model Context Protocol (MCP) servers

3102. **[datawrapper-mcp](https://github.com/palewire/datawrapper-mcp)** - ⭐ 23
   A Model Context Protocol (MCP) server for creating Datawrapper charts using AI assistants.

3103. **[codebase-context](https://github.com/PatrickSys/codebase-context)** - ⭐ 23
   Local-first Second brain for AI agents working on your codebase -  detects your team coding conventions and patterns, brings in persistent memory, code-generation checks, and hybrid search with evidence scoring. Exposed through CLI and MCP server.

3104. **[google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** - ⭐ 23
   Google Search Console MCP Server for Claude, Cursor, Windsurf and other MCP Clients

3105. **[NiFiMCP](https://github.com/ms82119/NiFiMCP)** - ⭐ 23
   An MCP Server and client for communicating with Nifi (v1.28)

3106. **[autotask-mcp](https://github.com/asachs01/autotask-mcp)** - ⭐ 23
   MCP server for Kaseya Autotask PSA — 39 tools for companies, tickets, projects, time entries, and more

3107. **[Claude-Code-MCP-Manager](https://github.com/qdhenry/Claude-Code-MCP-Manager)** - ⭐ 23
    A comprehensive tool to manage Model Context Protocol (MCP) configurations for Claude code

3108. **[zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** - ⭐ 23
   MCP server to expose local zotero repository to MCP clients 

3109. **[rlm-claude](https://github.com/EncrEor/rlm-claude)** - ⭐ 23
   Recursive Language Models for Claude Code - Infinite memory solution inspired by MIT CSAIL paper

3110. **[brainstorm-mcp](https://github.com/spranab/brainstorm-mcp)** - ⭐ 23
   MCP server for multi-round AI brainstorming debates between multiple models (GPT, DeepSeek, Groq, Ollama, etc.)

3111. **[context-harness](https://github.com/parallax-labs/context-harness)** - ⭐ 23
   Local-first context ingestion and retrieval for AI tools. SQLite + embeddings + MCP server for Cursor & Claude.

3112. **[nobitex-mcp-server](https://github.com/xmannii/nobitex-mcp-server)** - ⭐ 22
   a Model Context Protocol (MCP) server that provides access to cryptocurrency market data from the Nobitex API.

3113. **[mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)** - ⭐ 22
   Model Context Protocol server to access oracle database

3114. **[higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server)** - ⭐ 22
   A Model Context Protocol (MCP) server implementation that enables comprehensive configuration and management of Higress.

3115. **[Elysia-mcp](https://github.com/keithagroves/Elysia-mcp)** - ⭐ 22
   Model Context Protocol (MCP) Server for Bun and Elysia

3116. **[mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio)** - ⭐ 22
   A Model Context Protocol server for Flux image generation, providing tools for image generation, manipulation, and control

3117. **[DANP-Engine](https://github.com/DANP-LABS/DANP-Engine)** - ⭐ 22
   A trusted AI Model Context Protocol (MCP) runtime for secure, decentralized AI tools and services.

3118. **[mcp-sse-authenticated-cloud-run](https://github.com/the-freetech-company/mcp-sse-authenticated-cloud-run)** - ⭐ 22
   Host an Model Context Protocol SSE deployment on Cloud Run, Authenticating with IAM.

3119. **[MobSF-MCP](https://github.com/il-il1/MobSF-MCP)** - ⭐ 22
   a Node.js-based Model Context Protocol implementation for MobSF

3120. **[async-mcp](https://github.com/v3g42/async-mcp)** - ⭐ 22
   A minimalistic async Rust implementation of the Model Context Protocol (MCP).

3121. **[mcpagentai](https://github.com/mcpagents-ai/mcpagentai)** - ⭐ 22
   Python SDK designed to simplify interactions with MCP (Model Context Protocol) servers. It provides an easy-to-use interface for connecting to MCP servers, reading resources, and calling tools

3122. **[p5js-ai-editor](https://github.com/adilmoujahid/p5js-ai-editor)** - ⭐ 22
   A modern, web-based IDE for creating and editing p5.js sketches with AI assistance and Model Context Protocol (MCP) integration for Claude Desktop.

3123. **[printify-mcp](https://github.com/TSavo/printify-mcp)** - ⭐ 22
   A Model Context Protocol (MCP) server for integrating AI assistants with Printify's print-on-demand platform

3124. **[supabase-mcp-client](https://github.com/tambo-ai/supabase-mcp-client)** - ⭐ 22
   Supabase MCP client react app with Tambo

3125. **[biznagafest-mcp](https://github.com/0GiS0/biznagafest-mcp)** - ⭐ 22
   MCP Servers en Málaga con salero

3126. **[langchain-mcp-tools-ts](https://github.com/hideya/langchain-mcp-tools-ts)** - ⭐ 22
   MCP to LangChain Tools Conversion Utility / TypeScript

3127. **[dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp)** - ⭐ 22
   MCP (model context protocol) server for interacting with dbt Docs

3128. **[metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp)** - ⭐ 22
   Met Museum MCP integration to discover the art collection at The Metropolitan Museum of Art in New York

3129. **[nix-mcp-servers](https://github.com/ismail-kattakath/nix-mcp-servers)** - ⭐ 22
   A nix flake for configuring Model Context Protocol (MCP) servers across supported AI assistant clients

3130. **[ib-mcp-cache-server](https://github.com/ibproduct/ib-mcp-cache-server)** - ⭐ 22
   Memory Cache Server for use with supported MCP API Clients.

3131. **[your-money-left-the-chat](https://github.com/Rayato159/your-money-left-the-chat)** - ⭐ 22
   A Rust + MCP powered financial tracker that knows exactly where your money ghosted you.

3132. **[turbomcpstudio](https://github.com/Epistates/turbomcpstudio)** - ⭐ 22
   A native desktop application for developing, testing, and debugging Model Context Protocol servers.

3133. **[mcp-cmd](https://github.com/developit/mcp-cmd)** - ⭐ 22
   CLI for calling successive MCP Server tools

3134. **[mcp-framework](https://github.com/koki7o/mcp-framework)** - ⭐ 22
   Rust MCP framework for building AI agents

3135. **[GUI-MCP](https://github.com/PhialsBasement/GUI-MCP)** - ⭐ 22
   A Blueprint-style visual node editor for creating FastMCP servers. Build MCP tools, resources, and prompts by connecting nodes - no coding required.

3136. **[mcp-wireshark](https://github.com/khuynh22/mcp-wireshark)** - ⭐ 22
   An MCP server that integrates Wireshark/tshark with AI tools and IDEs. Capture live traffic, parse .pcap files, apply display filters, follow streams, and export JSON - all via Claude Desktop, VS Code, or CLI. Cross‑platform, typed, tested, and pip‑installable.

3137. **[mcpc](https://github.com/micl2e2/mcpc)** - ⭐ 22
   Cross-platform C SDK for Model Context Protocol (MCP), in modern🚀 C23.

3138. **[mcpls](https://github.com/bug-ops/mcpls)** - ⭐ 22
   Universal MCP to LSP bridge - expose Language Server Protocol capabilities as MCP tools for AI agents

3139. **[suse-ai-up](https://github.com/SUSE/suse-ai-up)** - ⭐ 22
   A comprehensive platform for managing and proxying Model Context Protocol (MCP) servers, providing scalable AI service orchestration across multiple microservices.

3140. **[ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite)** - ⭐ 22
   MCP server for video/audio processing via FFmpeg - convert, compress, trim, extract audio, add subtitles

3141. **[awesome-mcp](https://github.com/MCPHubCloud/awesome-mcp)** - ⭐ 22
   A collection of mcp servers/client/sdks

3142. **[MCP_A2A](https://github.com/regismesquita/MCP_A2A)** - ⭐ 21
   A2A MCP Server is a lightweight Python bridge that lets Claude Desktop or any MCP client talk to A2A agents. It provides three tools: register servers, list agents, and call an agent, enabling quick integration of A2A-compatible agents with zero boilerplate for rapid prototyping.

3143. **[grumpydev-mcp](https://github.com/sinedied/grumpydev-mcp)** - ⭐ 21
   Let the grumpy senior dev review your code with this MCP server

3144. **[bridge-mcp](https://github.com/codingjam/bridge-mcp)** - ⭐ 21
   Open Source MCP gateway and proxy for Model Context Protocol (MCP) servers with enterprise authentication and service discovery

3145. **[mcpsharepoint](https://github.com/BrianCusack/mcpsharepoint)** - ⭐ 21
   Model Context Protocol server that provides access to Organisational SharePoint.

3146. **[command-executor-mcp-server](https://github.com/Sunwood-ai-labs/command-executor-mcp-server)** - ⭐ 21
   Model Context Protocol Server for Safely Executing Pre-approved Commands

3147. **[emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server)** - ⭐ 21
   A Model Context Protocol (MCP) server implementation that provides EMQX MQTT broker interaction.

3148. **[mcp-sentry](https://github.com/MCP-100/mcp-sentry)** - ⭐ 21
   A Model Context Protocol server for retrieving and analyzing issues from Sentry.io

3149. **[mcp-korean-spell](https://github.com/winterjung/mcp-korean-spell)** - ⭐ 21
   MCP(Model Context Protocol) server designed for Korean spell checking

3150. **[DocsRay](https://github.com/MIMICLab/DocsRay)** - ⭐ 21
   Lightweight PDF Q&A tool powered by RAG (Retrieval-Augmented Generation) with MCP (Model Context Protocol) Support.

3151. **[MCPRules](https://github.com/bartwisch/MCPRules)** - ⭐ 21
   A powerful Model Context Protocol (MCP) server that manages and serves programming guidelines and rules. This server integrates with development tools to provide consistent coding standards across projects.

3152. **[code-context-mcp](https://github.com/fkesheh/code-context-mcp)** - ⭐ 21
   A Model Context Protocol (MCP) server for providing code context from git repositories

3153. **[mcp-knowledge-base](https://github.com/hjlee94/mcp-knowledge-base)** - ⭐ 21
   MCP agent/client/server implementation for private knowledge base

3154. **[plux](https://github.com/milisp/plux)** - ⭐ 21
   💡AI finder/explorer. One click @files via a visual filetree and save insights in a notepad. build with Tauri

3155. **[mcp-deepseek-demo](https://github.com/Ulanxx/mcp-deepseek-demo)** - ⭐ 21
   deepseek 结合 mcp 场景，最小用例，包括 client and server

3156. **[room-mcp](https://github.com/agree-able/room-mcp)** - ⭐ 21
   Allow MCP clients like claude-desktop to use rooms to coordinate with other agents

3157. **[mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server)** - ⭐ 21
   An MCP server that provides server-to-client notifications for file changes that the client subscribes to

3158. **[hs-mcp](https://github.com/buecking/hs-mcp)** - ⭐ 21
   Haskell server/client for MCP (Model Context Protocol)

3159. **[perplexity-mcp-server](https://github.com/cyanheads/perplexity-mcp-server)** - ⭐ 21
   A Perplexity API MCP server that unlocks Perplexity's search-augmented AI capabilities for LLM agents. Features robust error handling, secure input validation, and transparent reasoning with the showThinking parameter.

3160. **[mcp-ai-agent](https://github.com/fkesheh/mcp-ai-agent)** - ⭐ 21
   A TypeScript library that enables AI agents to leverage MCP (Model Context Protocol) servers for enhanced capabilities. This library integrates with the AI SDK to provide a seamless way to connect to MCP servers and use their tools in AI-powered applications.

3161. **[aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp)** - ⭐ 21
   MCP server to integrate AWS S3 and LLM

3162. **[mcp-server-memos-py](https://github.com/RyoJerryYu/mcp-server-memos-py)** - ⭐ 21
   A Python package enabling LLM models to interact with the Memos server via the MCP interface for searching, creating, retrieving, and managing memos.

3163. **[golemcore-bot](https://github.com/alexk-dev/golemcore-bot)** - ⭐ 21
   AI agent framework for Java — skill-based architecture with MCP support, tool calling, RAG, and Telegram integration. Built on Spring Boot and  LangChain4j

3164. **[qdrant-mcp-server](https://github.com/mhalder/qdrant-mcp-server)** - ⭐ 21
   MCP server for semantic search using local Qdrant vector database and OpenAI embeddings

3165. **[raybridge](https://github.com/jlokos/raybridge)** - ⭐ 21
   MCP server that bridges Raycast extensions to any MCP-compatible client

3166. **[mcp-prompt-optimizer](https://github.com/Bubobot-Team/mcp-prompt-optimizer)** - ⭐ 21
   Advanced MCP server providing cutting-edge prompt optimization tools with research-backed strategies

3167. **[html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp)** - ⭐ 21
   MCP server for converting HTML to Markdown using Turndown.js. Fetch web pages and convert them to clean, formatted Markdown.

3168. **[Air-Quality-Trends-Analysis-Project](https://github.com/dyneth02/Air-Quality-Trends-Analysis-Project)** - ⭐ 21
   Full-stack air quality analytics platform built with FastAPI, React, and MySQL. Aggregates multi-source PM2.5/PM10 data, performs multi-city comparison and time-series forecasting (SARIMAX), and integrates an LLM-based planning agent with tiered access, secure APIs, and PDF reporting.

3169. **[guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks](https://github.com/aws-solutions-library-samples/guidance-for-scalable-model-inference-and-agentic-ai-on-amazon-eks)** - ⭐ 21
   Comprehensive, scalable ML inference architecture using Amazon EKS, leveraging Graviton processors for cost-effective CPU-based inference and GPU instances for accelerated inference. Guidance provides a complete end-to-end platform for deploying LLMs with agentic AI capabilities, including RAG and MCP

3170. **[local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp)** - ⭐ 21
   Local FAISS vector store as an MCP server – drop-in local RAG for Claude / Copilot / Agents.

3171. **[heuristic-mcp](https://github.com/softerist/heuristic-mcp)** - ⭐ 21
   Enhanced MCP server for semantic code search with call-graph proximity, recency ranking, and find-similar-code. Built for AI coding assistants.

3172. **[mcp-diagnostics-extension](https://github.com/newbpydev/mcp-diagnostics-extension)** - ⭐ 20
   VS Code extension that exposes diagnostic problems via Model Context Protocol (MCP) for AI agents and tools

3173. **[mcp-server-runner](https://github.com/yonaka15/mcp-server-runner)** - ⭐ 20
   A WebSocket server implementation for running Model Context Protocol (MCP) servers. This application enables MCP servers to be accessed via WebSocket connections, facilitating integration with web applications and other network-enabled clients.

3174. **[easymcp](https://github.com/promptmesh/easymcp)** - ⭐ 20
   A high performance MCP client sdk for python

3175. **[PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides access to the Protein Data Bank (PDB) - the worldwide repository of information about the 3D structures of proteins, nucleic acids, and complex assemblies.

3176. **[mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer)** - ⭐ 20
   MCP (Model Context Protocol) server - free usdc transfer powered by Coinbase CDP

3177. **[mcp-file-operations-server](https://github.com/bsmi021/mcp-file-operations-server)** - ⭐ 20
   A Model Context Protocol (MCP) server that provides enhanced file operation capabilities with streaming, patching, and change tracking support.

3178. **[cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp)** - ⭐ 20
   MCP Server for Cucumber Studio

3179. **[knowledgebase-mcp](https://github.com/biocontext-ai/knowledgebase-mcp)** - ⭐ 20
   BioContextAI Knowledgebase MCP server for biomedical agentic AI 

3180. **[registry](https://github.com/biocontext-ai/registry)** - ⭐ 20
   The BioContextAI Registry for biomedical MCP servers

3181. **[jenkins-mcp-enterprise](https://github.com/Jordan-Jarvis/jenkins-mcp-enterprise)** - ⭐ 20
   The most advanced Jenkins MCP server available - Enterprise debugging, multi-instance management, AI-powered failure analysis, vector search, and configurable diagnostics for complex CI/CD pipelines.

3182. **[UCAI](https://github.com/nirholas/UCAI)** - ⭐ 20
   Universal Contract AI Interface (UCAI) 🔗 ABI to MCP | The open standard for connecting AI agents to blockchain. MCP server generator for smart contracts. Claude + Uniswap, Aave, ERC20, NFTs, DeFi. Python CLI, Web3 integration, transaction simulation. Polygon, Arbitrum, Base, Ethereum EVM chains. Claude, GPT, LLM tooling, Solidity, OpenAI.

3183. **[agent-mcp](https://github.com/grupa-ai/agent-mcp)** - ⭐ 20
   MCPAgent for Grupa.AI Multi-agent Collaboration Network (MACNET) with Model Context Protocol (MCP) capabilities baked in

3184. **[lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp)** - ⭐ 20
   MCP server for structured problem-solving using the Lotus Sutra's wisdom framework. Beautiful visualizations, multiple thinking approaches, compatible with various MCP clients (e.g., Claude Desktop, Cursor, Cherry Studio).

3185. **[flutter-ai-labs](https://github.com/theshivamlko/flutter-ai-labs)** - ⭐ 20
   A curated collection of LLM-powered Flutter apps built using RAG, AI Agents, Multi-Agent Systems, MCP, and Voice Agents.

3186. **[MCP-Mastery-with-Claude-and-Langchain](https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain)** - ⭐ 20
   Build MCP servers & clients with Python, Streamlit, ChromaDB, LangChain, LangGraph agents, and Ollama integrations

3187. **[mcp-link](https://github.com/AuraFriday/mcp-link)** - ⭐ 20
   Let AI agents like ChatGPT & Claude use real-world local/remote tools you approve via browser extension + optional MCP server

3188. **[Zammad-MCP](https://github.com/basher83/Zammad-MCP)** - ⭐ 20
   A Model Context Protocol (MCP) server for Zammad integration, enabling AI assistants to interact with tickets, users, and organizations.

3189. **[janee](https://github.com/rsdouglas/janee)** - ⭐ 20
   Secrets management for AI agents via MCP • @janeesecure

3190. **[mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper)** - ⭐ 20
   The Decodo MCP server which enables MCP clients to interface with services.

3191. **[rollbar-mcp-server](https://github.com/rollbar/rollbar-mcp-server)** - ⭐ 20
   Pre-release - Model Context Protocol server for Rollbar

3192. **[claude-vigil-mcp](https://github.com/Vvkmnn/claude-vigil-mcp)** - ⭐ 19
   🏺 An MCP server for checkpointing and file recovery in Claude Code

3193. **[gemini-mcp-client](https://github.com/angrysky56/gemini-mcp-client)** - ⭐ 19
   A MCP (Model Context Protocol) client that uses Google Gemini AI models for intelligent tool usage and conversation handling.  Tested working nicely with Claude Desktop as an MCP Server currently. Based on untested AI gen code by a non-coder use at own risk.

3194. **[starbase](https://github.com/metorial/starbase)** - ⭐ 19
   Connect, explore, and test any MCP server with AI models 🤖 ⚡

3195. **[mcp](https://github.com/EmilLindfors/mcp)** - ⭐ 19
    A crate for making MCP (Model Context Protocol) compatible programs with rust

3196. **[mcp-frontend](https://github.com/shaharia-lab/mcp-frontend)** - ⭐ 19
   Frontend for MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3197. **[mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb)** - ⭐ 19
   An mcp server that provides read-only access to MariaDB.

3198. **[mcp-server](https://github.com/paperinvest/mcp-server)** - ⭐ 19
   Official MCP server for Paper's trading platform - enables AI assistants to interact with Paper's API

3199. **[linux-command-mcp](https://github.com/xkiranj/linux-command-mcp)** - ⭐ 19
   MCP server and client for running Linux commands

3200. **[mcp-server-client-demo](https://github.com/S1LV3RJ1NX/mcp-server-client-demo)** - ⭐ 19
   Streamable HTTP based MCP server and Client demo with auto registry, Dockerfile setup and env. 

3201. **[openapi2mcptools](https://github.com/2013xile/openapi2mcptools)** - ⭐ 19
   OpenAPI specifications => MCP (Model Context Protocol) tools

3202. **[ai-cli](https://github.com/manusa/ai-cli)** - ⭐ 19
   ai-cli lets you go from zero to AI-powered in seconds in a safe, automated and tailored way.

3203. **[typescript-mcp-client](https://github.com/CodelyTV/typescript-mcp-client)** - ⭐ 19

3204. **[eraser-io-mcp-server](https://github.com/buck-0x/eraser-io-mcp-server)** - ⭐ 19
   A Python MCP (Model Context Protocol) server and CLI tool to render diagrams using the Eraser API.

3205. **[context-lens](https://github.com/cornelcroi/context-lens)** - ⭐ 19
   Semantic search knowledge base for MCP-enabled AI assistants. Index local files or GitHub repos, query with natural language. Built on LanceDB vector storage. Works with Claude Desktop, Cursor, and other MCP clients.

3206. **[termlink](https://github.com/chu2bard/termlink)** - ⭐ 19
   MCP server for shell and terminal operations

3207. **[Augmented-Nature-UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server providing advanced access to the UniProt protein database. 

3208. **[ACP-MCP-Server](https://github.com/GongRzhe/ACP-MCP-Server)** - ⭐ 19
   A bridge server that connects Agent Communication Protocol (ACP) agents with Model Context Protocol (MCP) clients, enabling seamless integration between ACP-based AI agents and MCP-compatible tools like Claude Desktop.

3209. **[it-tools-mcp](https://github.com/wrenchpilot/it-tools-mcp)** - ⭐ 19
   A comprehensive Model Context Protocol (MCP) server that provides access to over 100 IT tools and utilities commonly used by developers, system administrators, and IT professionals. Inspired by https://github.com/CorentinTh/it-tools

3210. **[Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server)** - ⭐ 19
   MCP server addon for Blender - Control Blender via AI agents through 51 powerful tools. Made to be used with PolyMCP for intelligent tool orchestration. Features thread-safe execution, auto-dependency installation, and complete 3D workflow automation.

3211. **[codeprism](https://github.com/rustic-ai/codeprism)** - ⭐ 19
   An experimental, 100% AI-generated, high-performance code intelligence server providing AI assistants with a graph-based understanding of codebases.

3212. **[google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp)** - ⭐ 19
   An MCP server for Google Scholar written in TypeScript with Streamable HTTP

3213. **[mcpbi](https://github.com/jonaolden/mcpbi)** - ⭐ 19
   PowerBI MCP server to give LLM clients (Claude, GH Copilot,etc) context from locally running PowerBI Desktop instances.

3214. **[mcp](https://github.com/yandex-cloud/mcp)** - ⭐ 19
   Yandex Cloud MCP Servers

3215. **[mirroir-mcp](https://github.com/jfarcand/mirroir-mcp)** - ⭐ 19
   MCP server for controlling a real iPhone via macOS iPhone Mirroring...and any MacOs app. Screenshot, tap, swipe, type — from any MCP client.

3216. **[mcp](https://github.com/zuplo/mcp)** - ⭐ 18
   A fetch API based TypeScript SDK for MCP

3217. **[eleven.shopping](https://github.com/elevenlabs/eleven.shopping)** - ⭐ 18
   ElevenLabs Agent with Storefront MCP UI Server & MCP UI client

3218. **[openpyxl-mcp-server](https://github.com/jonemo/openpyxl-mcp-server)** - ⭐ 18
   A thin wrapper around the OpenPyXl Python library that exposes some of its features as Model Context Protocol (MCP) server. This allows Claude and other MCP clients to fetch data from Excel files.

3219. **[sufetch](https://github.com/productdevbook/sufetch)** - ⭐ 18
   Type-safe OpenAPI clients with MCP server for AI-driven API exploration

3220. **[SimpleMcp.Demo](https://github.com/hassanhabib/SimpleMcp.Demo)** - ⭐ 18
   Simplest Possible Demo for Building MCP Server & Client

3221. **[mcp-copilot](https://github.com/tshu-w/mcp-copilot)** - ⭐ 18
   A meta MCP server that seamlessly scales LLMs to 1000+ MCP servers through automatic routing.

3222. **[mcp-libsql](https://github.com/Xexr/mcp-libsql)** - ⭐ 18
   Secure MCP server for libSQL databases with comprehensive tools, connection pooling, and transaction support. Built with TypeScript for Claude Desktop, Claude Code, Cursor, and other MCP clients.

3223. **[gpt2099.nu](https://github.com/cablehead/gpt2099.nu)** - ⭐ 18
   a Nushell cross.stream extension to interact with LLMs and MCP servers

3224. **[Devmind-MCP](https://github.com/JochenYang/Devmind-MCP)** - ⭐ 18
   DevMind MCP provides **persistent memory capabilities** for AI assistants through the Model Context Protocol (MCP). It enables AI to remember context across conversations, automatically track development activities, and retrieve relevant information intelligently.

3225. **[seedream-image-mcp](https://github.com/wearzdk/seedream-image-mcp)** - ⭐ 18
   🚀 PixelMCP | 为你的 Cursor、Claude Code 等集成AI绘画能力，让AI生成的页面不再单调！

3226. **[mcp-chat-studio](https://github.com/JoeCastrom/mcp-chat-studio)** - ⭐ 18
   A powerful MCP testing tool with multi-provider LLM support (Ollama, OpenAI, Claude, Gemini). Test, debug, and develop MCP servers with a modern UI.

3227. **[mcp-agent](https://github.com/joshuaalpuerto/mcp-agent)** - ⭐ 18
   Lightweight, focused utilities to manage connections and execute MCP tools with minimal integration effort. Use it to directly call tools or build simple agents within your current architecture.

3228. **[mcpx](https://github.com/AIGC-Hackers/mcpx)** - ⭐ 18
   Token-efficient MCP client: TypeScript schemas instead of JSON, LLM-friendly syntax, batch calls, TOON output. Built for Claude/GPT automations.

3229. **[mcp-server-microsoft-paint](https://github.com/ghuntley/mcp-server-microsoft-paint)** - ⭐ 18

3230. **[mcp-chain-of-draft-prompt-tool](https://github.com/brendancopley/mcp-chain-of-draft-prompt-tool)** - ⭐ 18
   MCP prompt tool applying Chain-of-Draft (CoD) reasoning - BYOLLM

3231. **[mcp-oauth-proxy](https://github.com/obot-platform/mcp-oauth-proxy)** - ⭐ 18
   Oauth 2.1 proxy server that can autheticate client and proxy requests to mcp server

3232. **[mcp-yfinance](https://github.com/9nate-drake/mcp-yfinance)** - ⭐ 18
   MCP Server for fething yfinance financial data into Claude Desktop

3233. **[gh-mcp](https://github.com/shuymn/gh-mcp)** - ⭐ 18
   A GitHub CLI extension that seamlessly runs the github-mcp-server using your existing gh authentication. Eliminates manual PAT setup by automatically retrieving GitHub credentials and launching the MCP server with proper authentication.

3234. **[toolkit-mcp-server](https://github.com/cyanheads/toolkit-mcp-server)** - ⭐ 18
   A Model Context Protocol server providing LLM Agents with system utilities and tools, including IP geolocation, network diagnostics, system monitoring, cryptographic operations, and QR code generation.

3235. **[hasmcp-ce](https://github.com/hasmcp/hasmcp-ce)** - ⭐ 18
   HasMCP Community Edition

3236. **[model-context-protocol-survey](https://github.com/asinghcsu/model-context-protocol-survey)** - ⭐ 18
   Model Context Protocol (MCP)

3237. **[MCP-Development-with-Rust](https://github.com/RustSandbox/MCP-Development-with-Rust)** - ⭐ 18
   This comprehensive learning resource provides two complete tutorials for mastering Model Context Protocol (MCP) development with Rust. From beginner-friendly introductions to production-ready enterprise applications, these tutorials guide you through every aspect of building robust MCP servers.

3238. **[mcp-server-amazon](https://github.com/rigwild/mcp-server-amazon)** - ⭐ 18
   🛍📦 Unofficial Amazon Model Context Protocol Server (MCP) - Search products and purchase directly from Claude AI! ✨

3239. **[unity-editor-mcp](https://github.com/ozankasikci/unity-editor-mcp)** - ⭐ 18
   An MCP server and client for LLMs to interact with Unity Projects

3240. **[emceepee](https://github.com/eastlondoner/emceepee)** - ⭐ 18
   MCP server to dynamically connect to other MCP servers & exposes the entire MCP protocol via tool calls. Ideal for testing MCPs during development or accessing MCP Server features from clients that do not support notifications, resource templates, prompts or elicitations.

3241. **[short-url](https://github.com/fengzhongsen/short-url)** - ⭐ 18
   简单易用的短链接生成工具，完全开源、免费、无需登录，可私有化部署，链接永久有效！

3242. **[MCP-Agent](https://github.com/CursorTouch/MCP-Agent)** - ⭐ 18
   Connect to any MCP servers using agents

3243. **[github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp)** - ⭐ 18
   GitHub Repos Manager MCP Server that enables your MCP client (e.g., Claude Desktop, Roo Code, etc.) to interact with GitHub repositories using your GitHub personal access token.

3244. **[substack-mcp](https://github.com/marcomoauro/substack-mcp)** - ⭐ 18
   A Model Context Protocol (MCP) Server for Substack enabling LLM clients to interact with Substack's API for automations like creating posts, managing drafts, and more.

3245. **[universal-crypto-mcp](https://github.com/nirholas/universal-crypto-mcp)** - ⭐ 18
   Universal MCP server for AI agents to interact with any* blockchain via natural language and plugins. Supports swaps, bridges, gas, staking, lending, and more across Ethereum, Arbitrum, Base, Polygon, BSC, and testnets. 

3246. **[titanmind-whatsapp-mcp](https://github.com/TitanmindAGI/titanmind-whatsapp-mcp)** - ⭐ 18
   A WhatsApp marketing and messaging tool MCP (Model Control Protocol) service using Titanmind. Handles free-form messages (24hr window) and template workflows automatically

3247. **[local-skills-mcp](https://github.com/kdpa-llc/local-skills-mcp)** - ⭐ 18
   Universal MCP server enabling any LLM or AI agent to utilize expert skills from your local filesystem. Reduces context consumption through lazy loading. Works with Claude, Cline, and any MCP-compatible client.

3248. **[IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server)** - ⭐ 18
   MCP server for Industrial IoT, SCADA and PLC systems. Unifies MQTT sensors, Modbus devices and industrial equipment into a single AI-orchestrable API. Features real-time monitoring, alarms, time-series storage and actuator control.

3249. **[smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server)** - ⭐ 17
   Local version of Smartlead MCP for quick download and deployment to MCP compatible clients or n8n.

3250. **[mcp-http-client-example](https://github.com/slavashvets/mcp-http-client-example)** - ⭐ 17
   Simple example client demonstrating how to connect to MCP servers over HTTP (SSE)

3251. **[jiki](https://github.com/teilomillet/jiki)** - ⭐ 17

3252. **[askit](https://github.com/johnrobinsn/askit)** - ⭐ 17
   LLM Function Calling Library and CLI with Support for MCP Servers

3253. **[youtube-mcp-server](https://github.com/0GiS0/youtube-mcp-server)** - ⭐ 17
   Cómo crear MCP Servers y usarlos con GitHub Copilot Chat 🚀💻🤖

3254. **[cmcp](https://github.com/RussellLuo/cmcp)** - ⭐ 17
   A command-line utility for interacting with MCP servers.

3255. **[GUARDRAIL](https://github.com/nshkrdotcom/GUARDRAIL)** - ⭐ 17
   GUARDRAIL - MCP Security - Gateway for Unified Access, Resource Delegation, and Risk-Attenuating Information Limits

3256. **[mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus)** - ⭐ 17
   MCP server for interacting with Prometheus

3257. **[mcp-koii](https://github.com/benjaminr/mcp-koii)** - ⭐ 17
   MCP Server for Teenage Engineering EP-133 KO-II

3258. **[context-engineering](https://github.com/timothywarner-org/context-engineering)** - ⭐ 17
   🧠 Stop building AI that forgets. Master MCP (Model Context Protocol) with production-ready semantic memory, hybrid RAG, and the WARNERCO Schematica teaching app. FastMCP + LangGraph + Vector/Graph stores. Your AI assistant's long-term memory starts here.

3259. **[daiv](https://github.com/srtab/daiv)** - ⭐ 17
   Async SWE agents seamlessly integrated on your git platform to automate code issues implementation, reviews, and pipeline repairs.

3260. **[docmole](https://github.com/Vigtu/docmole)** - ⭐ 17
   Dig through any documentation with AI - MCP server for Claude, Cursor, and other AI assistants

3261. **[unity-mcp](https://github.com/wondeks/unity-mcp)** - ⭐ 17
   A Unity MCP server that allows MCP clients like Claude Desktop or Cursor to perform Unity Editor actions.

3262. **[Agentic-MCP-Skill](https://github.com/cablate/Agentic-MCP-Skill)** - ⭐ 17
   Agentic-MCP, Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage. Use MCP without pre-install & wasting full-loading

3263. **[mcp-chatbot](https://github.com/mctrinh/mcp-chatbot)** - ⭐ 17
   MCP Chatbot powered by Anthropic Claude. Delivering on‐demand literature search and summarisation for academics and engineers

3264. **[autowpmcp](https://github.com/Njengah/autowpmcp)** - ⭐ 17
   AutoWP MCP (Model Context Protocol) server connects Claude to WordPress site and allows users to ask Claude to write blog posts and automatically publish them to WordPress sites.

3265. **[arxiv-mcp-server](https://github.com/anuj0456/arxiv-mcp-server)** - ⭐ 17
   MCP server for arXiv.org - Search, analyze, and export academic papers with AI assistants. Features advanced paper discovery, citation analysis, trend tracking, and multi-format exports.

3266. **[rpc-nodes-mcp](https://github.com/chainstacklabs/rpc-nodes-mcp)** - ⭐ 17
   Minimal, fast, and extensible MCP server for interactions with JSON-RPC blockchain nodes

3267. **[teamcity-mcp](https://github.com/Daghis/teamcity-mcp)** - ⭐ 17
   Model Context Protocol (MCP) server for JetBrains TeamCity: control builds, tests, agents and configs from AI coding assistants.

3268. **[toolhive-catalog](https://github.com/stacklok/toolhive-catalog)** - ⭐ 17
   ToolHive's registry catalog of MCP servers

3269. **[mcp-server-codegraph](https://github.com/CartographAI/mcp-server-codegraph)** - ⭐ 17
   MCP server for graph representation of a codebase

3270. **[leanmcp-sdk](https://github.com/LeanMCP/leanmcp-sdk)** - ⭐ 17
   Production-ready TypeScript SDK for MCP servers: auth, multi-tenant, observability. Build enterprise AI agents fast.

3271. **[pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server)** - ⭐ 17
   *Featured on Claude!* MCP server for accessing near real-time health data from Yale's PopHIVE platform, as well as additional HHS/CDC data

3272. **[ChatSpatial](https://github.com/cafferychen777/ChatSpatial)** - ⭐ 17
   🧬 Analyze spatial transcriptomics data through natural language conversation. Stop writing code, start having conversations with your data. MCP server for Claude Code and Codex.

3273. **[skill-to-mcp](https://github.com/biocontext-ai/skill-to-mcp)** - ⭐ 17
   Convert AI Skills (Claude Skills format) to MCP server resources - Part of BioContextAI

3274. **[MCPHammer](https://github.com/praetorian-inc/MCPHammer)** - ⭐ 17
   MCP security testing framework for evaluating Model Context Protocol server vulnerabilities

3275. **[gumroad-mcp](https://github.com/rmarescu/gumroad-mcp)** - ⭐ 17
   A Model Context Protocol (MCP) server implementation for Gumroad API

3276. **[awesome-dxt-mcp](https://github.com/MCPStar/awesome-dxt-mcp)** - ⭐ 17
   🚀 A curated list of awesome Desktop Extensions (DXT) and MCP servers for Claude Desktop. Discover, share, and contribute to the growing ecosystem of AI-powered local tools and automations.

3277. **[archmcp](https://github.com/dejo1307/archmcp)** - ⭐ 17
   archmcp - MCP Architectural Snapshot Server and Knowledge Graph

3278. **[unity-api-mcp](https://github.com/Codeturion/unity-api-mcp)** - ⭐ 17
   Instant, accurate Unity API lookups instead of expensive source file reads, saving your agent tokens, context, and hallucinations

3279. **[muxi](https://github.com/ranaroussi/muxi)** - ⭐ 16
   An extensible AI agents framework

3280. **[mcp-email-client](https://github.com/gamalan/mcp-email-client)** - ⭐ 16
   Email Client as MCP Server. Feature: multiple configuration, more than just gmail

3281. **[oneshot](https://github.com/Destiner/oneshot)** - ⭐ 16
   Anthropic MCP client for macOS

3282. **[CereBro](https://github.com/rob1997/CereBro)** - ⭐ 16
   A model-agnostic MCP Client-Server for .Net and Unity

3283. **[lite-mcp-client](https://github.com/sligter/lite-mcp-client)** - ⭐ 16
   Lite-MCP-Client是一个基于命令行的轻量级MCP客户端工具

3284. **[EasyMCP](https://github.com/mshojaei77/EasyMCP)** - ⭐ 16
   A beginner-friendly client for the MCP (Model Context Protocol). Connect to SSE, NPX, and UV servers, and integrate with OpenAI for dynamic tool interactions. Perfect for exploring server connections and chat enhancements.

3285. **[mcp-installer](https://github.com/joobisb/mcp-installer)** - ⭐ 16
   Simplifies the installation and management of MCP (Model Context Protocol) servers across different AI clients.

3286. **[appvector-mcp](https://github.com/Multivariate-AI-Inc/appvector-mcp)** - ⭐ 16
   This MCP server provides programmatic access to AppVector's powerful APIs, enabling you to integrate ASO insights directly into your development and marketing workflows through any MCP Client

3287. **[protocols-io-mcp-server](https://github.com/hqn21/protocols-io-mcp-server)** - ⭐ 16
   An MCP server that enables MCP clients like Claude Desktop to interact with data from protocols.io.

3288. **[mcp-progressive-agentskill](https://github.com/cablate/mcp-progressive-agentskill)** - ⭐ 16
   AgentSkill - Progressive MCP client with three-layer lazy loading. Validates AgentSkills.io pattern for efficient token usage.

3289. **[create-mcp](https://github.com/fefergrgrgrg/create-mcp)** - ⭐ 16
   CLI to set up and deploy MCP Servers to Cloudflare Workers in seconds. Just write TypeScript functions to make Cursor MCP tools.

3290. **[videocapture-mcp](https://github.com/13rac1/videocapture-mcp)** - ⭐ 16
   Model Context Protocol (MCP) server to capture images from an OpenCV-compatible webcam or video source

3291. **[aica](https://github.com/dotneet/aica)** - ⭐ 16
   aica(AI Code Analyzer) reviews your code using AI. Supports CLI and GitHub Actions.

3292. **[go-mcp](https://github.com/dstotijn/go-mcp)** - ⭐ 16
   Go library for implementing the Model Context Protocol (MCP).

3293. **[sveltekit-mcp-starter](https://github.com/axel-rock/sveltekit-mcp-starter)** - ⭐ 16

3294. **[mcp-gateway](https://github.com/unrelated-ai/mcp-gateway)** - ⭐ 16
   Transform any HTTP endpoint into an MCP server. Aggregate multiple MCP servers, manage configuration profiles, and serve them through a unified gateway with multi-tenant isolation.

3295. **[qmt-mcp-server](https://github.com/jm12138/qmt-mcp-server)** - ⭐ 16
   基于 QMT 平台股票行情的 MCP 服务器，用于提供股票市场数据下载和查询的功能。

3296. **[mlb-mcp](https://github.com/etweisberg/mlb-mcp)** - ⭐ 16
   MCP server for advanced baseball analytics (statcast, fangraphs, baseball reference, mlb stats API) with client demo 

3297. **[grok-faf-mcp](https://github.com/Wolfe-Jam/grok-faf-mcp)** - ⭐ 16
   First MCP server for Grok | FAST⚡️AF • URL-based AI context • Vercel-deployed

3298. **[hass-mcp-server](https://github.com/ganhammar/hass-mcp-server)** - ⭐ 16
   A Home Assistant Custom Component that provides an MCP (Model Context Protocol) server using HTTP transport, allowing AI assistants like Claude to interact with your Home Assistant instance over HTTP

3299. **[agentidentityprotocol](https://github.com/openagentidentityprotocol/agentidentityprotocol)** - ⭐ 16
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3300. **[mcp-jest](https://github.com/josharsh/mcp-jest)** - ⭐ 16
   Automated testing for Model Context Protocol servers. Ship MCP Servers with confidence.

3301. **[rigour](https://github.com/rigour-labs/rigour)** - ⭐ 16
   Local-first quality gate + fix-loop controller for AI coding agents (CLI + MCP).

3302. **[hoot](https://github.com/Portkey-AI/hoot)** - ⭐ 16
   MCP Testing Tool — Like Postman, but for the Model Context Protocol.

3303. **[mcp-client-and-proxy](https://github.com/appsecco/mcp-client-and-proxy)** - ⭐ 15
   A universal MCP client with proxying feature to interact with MCP Servers which support STDIO transport.

3304. **[mcp_client](https://github.com/app-appplayer/mcp_client)** - ⭐ 15

3305. **[MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer)** - ⭐ 15
   An MCP server to read MCP logs to debug directly inside the client

3306. **[mistr-agent](https://github.com/itisaevalex/mistr-agent)** - ⭐ 15
   A MCP client that enables Mistral AI models to autonomously execute complex tasks across web and local environments through standardized agentic capabilities.

3307. **[mcp-server](https://github.com/HarperFast/mcp-server)** - ⭐ 15
   An MCP server providing an interface for MCP clients to access data within Harper.

3308. **[mcp-this](https://github.com/shane-kercheval/mcp-this)** - ⭐ 15
   mcp-this lets you turn any command-line tool into an MCP tool and create structured prompt templates that any MCP Client (e.g. Claude Desktop) can use. er for any command

3309. **[django-firebase-mcp](https://github.com/raghavdasila/django-firebase-mcp)** - ⭐ 15
   A production-ready Django app implementing Firebase Model Context Protocol (MCP) server with 14 Firebase tools for AI agents. Features standalone agent, HTTP/stdio transport, LangChain integration, and complete Firebase service coverage (Auth, Firestore, Storage).

3310. **[claude-server](https://github.com/davidteren/claude-server)** - ⭐ 15
   Claude Server is an MCP implementation that enhances Claude's capabilities by providing sophisticated context management across sessions, enabling persistent knowledge organization through hierarchical project contexts and continuous conversation threads stored in a well-structured ~/.claude directory.

3311. **[pinmeto-location-mcp](https://github.com/PinMeTo/pinmeto-location-mcp)** - ⭐ 15
   PinMeTo MCP server that enables users with authorized credentials to unlock their data 

3312. **[npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server)** - ⭐ 15
   MCP server for searching npm packages

3313. **[mcp-server-python-template](https://github.com/sontallive/mcp-server-python-template)** - ⭐ 15
   This template provides a streamlined foundation for building Model Context Protocol (MCP) servers in Python. It's designed to make AI-assisted development of MCP tools easier and more efficient.

3314. **[mcp-graphql-forge](https://github.com/toolprint/mcp-graphql-forge)** - ⭐ 15
   MCP that can proxy any GraphQL API and expose graphql operations as mcp tools.

3315. **[mcp-tui](https://github.com/msabramo/mcp-tui)** - ⭐ 15
   MCP host app w/ textual user interface, in Python

3316. **[mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog)** - ⭐ 15
   Unity Catalog AI Model Context Protocol Server

3317. **[claude-mcp-scheduler](https://github.com/tonybentley/claude-mcp-scheduler)** - ⭐ 15
   Use Claude API to prompt remote agents on a cron interval but use local MCPs to handle tool calls for context

3318. **[Frontapp-MCP](https://github.com/zqushair/Frontapp-MCP)** - ⭐ 15
   MCP server and client for Frontapp

3319. **[vite-plugin-mcp-client-tools](https://github.com/atesgoral/vite-plugin-mcp-client-tools)** - ⭐ 15
   Pluggable Vite MCP plugin that brings client-side tools to your existing Vite setup

3320. **[mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates)** - ⭐ 15
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs.

3321. **[mcp-client-for-weather-example](https://github.com/a-persimmons/mcp-client-for-weather-example)** - ⭐ 15
   一个MCP客户端实践：实现LLM调用天气MCP服务端查询天气的快速示例

3322. **[predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp)** - ⭐ 15
   AI-Powered Predictive Maintenance & Fault Diagnosis through Model Context Protocol. An open-source framework for integrating Large Language Models with predictive maintenance and fault diagnosis workflows.

3323. **[signal-mcp-client](https://github.com/piebro/signal-mcp-client)** - ⭐ 15
   An MCP client that uses signal for sending and receiving messages.

3324. **[mcp-turso-cloud](https://github.com/spences10/mcp-turso-cloud)** - ⭐ 15
   🗂️ A Model Context Protocol (MCP) server that provides integration with Turso databases for LLMs. This server implements a two-level authentication system to handle both organization-level and database-level operations, making it easy to manage and query Turso databases directly from LLMs.

3325. **[lyra-tool-discovery](https://github.com/nirholas/lyra-tool-discovery)** - ⭐ 15
   AI powered automation toolkit which acts as an agent that discovers MCP servers for you. Point it at GitHub/npm/configure your own discovery, let GPT or Claude analyze the API or MCP or any tool, get ready-to-ship plugin configs. Zero manual work.

3326. **[uk-case-law-mcp-server](https://github.com/georgejeffers/uk-case-law-mcp-server)** - ⭐ 15
   MCP server for UK case law using The National Archives API. Enables LLMs to search, retrieve, and cite UK legal judgments.

3327. **[mcp-web-client](https://github.com/hemanth/mcp-web-client)** - ⭐ 15
   A web-based client for connecting to MCP servers with OAuth support

3328. **[mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)** - ⭐ 15
   Model Context Protocol (MCP) server exposes tools to read multiple document types including DOCX, PDF, Excel, and TXT. This has been tested on Trae Desktop.

3329. **[cursor-feedback-extension](https://github.com/jianger666/cursor-feedback-extension)** - ⭐ 15
   Save your Cursor monthly quota! Unlimited AI interactions in one conversation via MCP feedback loop.

3330. **[the-academy](https://github.com/im-knots/the-academy)** - ⭐ 15
   A Socratic dialogue engine for AI agents. 

3331. **[scopus-mcp](https://github.com/qwe4559999/scopus-mcp)** - ⭐ 15
   A Model Context Protocol (MCP) server for Elsevier Scopus. Allows AI assistants like Claude to search academic papers, retrieve abstracts, and analyze author profiles directly.

3332. **[penpot-mcp-server](https://github.com/zcube/penpot-mcp-server)** - ⭐ 15
   MCP server for Penpot - Connect AI assistants to Penpot design platform via Model Context Protocol

3333. **[hop](https://github.com/danmartuszewski/hop)** - ⭐ 15
   Fast, elegant SSH connection manager with a TUI dashboard and MCP server

3334. **[stitch-mcp-auto](https://github.com/GreenSheep01201/stitch-mcp-auto)** - ⭐ 15
   Automated installer for Stitch MCP - The easiest way to set up your Universal MCP server for Google Stitch.

3335. **[mcp](https://github.com/local-falcon/mcp)** - ⭐ 15
   MCP server for Local Falcon's local SEO and AI visibility platform: geo-grid rank tracking, campaign management, and competitor analysis via Model Context Protocol

3336. **[claude-praetorian-mcp](https://github.com/Vvkmnn/claude-praetorian-mcp)** - ⭐ 14
   ⚜️ An MCP server for context compaction and recycling in Claude Code

3337. **[chatgpt-app-typescript-template](https://github.com/pomerium/chatgpt-app-typescript-template)** - ⭐ 14
   ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

3338. **[systemprompt-mcp-core](https://github.com/Ejb503/systemprompt-mcp-core)** - ⭐ 14
   The core MCP extension for Systemprompt MCP multimodal client

3339. **[Open-MCP-Client](https://github.com/GongRzhe/Open-MCP-Client)** - ⭐ 14
   ChatMCP is a powerful command-line chat interface that connects to multiple LLM providers (OpenAI, Anthropic, Groq, etc.) and extends their capabilities with tools using the Model Context Protocol (MCP).

3340. **[llm-sse-mcp-demo-2025](https://github.com/nlinhvu/llm-sse-mcp-demo-2025)** - ⭐ 14
   This project demonstrates the integration between LLM clients and MCP (Model Context Protocol) servers using Server-Sent Events (SSE) for real-time communication.

3341. **[mcp-bundler](https://github.com/wrtnlabs/mcp-bundler)** - ⭐ 14
   Is the MCP configuration too complicated? You can easily share your own simplified setup!

3342. **[ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server)** - ⭐ 14
   An MCP (Model Context Protocol) server designed to interact with the ntfy push notification service. It enables LLMs and AI agents to send notifications to your devices with extensive customization options.

3343. **[mcpterm](https://github.com/dwrtz/mcpterm)** - ⭐ 14
   An MCP tool server that provides stateful, TUI-compatible terminal sessions.

3344. **[work-memory-mcp](https://github.com/moontmsai/work-memory-mcp)** - ⭐ 14
   Never lose context again - persistent memory management system for AI-powered workflows across multiple tools

3345. **[mcp-ipfs](https://github.com/alexbakers/mcp-ipfs)** - ⭐ 14
   🪐 MCP IPFS Server 

3346. **[deep-research](https://github.com/troyhantech/deep-research)** - ⭐ 14
   A minimalist deep research framework for any OpenAI API compatible LLMs. 

3347. **[hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp)** - ⭐ 14
   Hive Intelligence Crypto MCP | The Ultimate Cryptocurrency MCP for AI Assistants - Unified access to crypto, DeFi, and Web3 analytics 

3348. **[google-mcp](https://github.com/vakharwalad23/google-mcp)** - ⭐ 14
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3349. **[ultrathink](https://github.com/husniadil/ultrathink)** - ⭐ 14
   MCP server for sequential thinking and complex problem-solving. Built iteratively using itself. Features confidence scoring,   assumption tracking, and multi-session support.

3350. **[mcp-server-subagent](https://github.com/dvcrn/mcp-server-subagent)** - ⭐ 14
   MCP for letting agents delegate tasks to sub-agents (Claude Code, Aider, Q)

3351. **[mcp-server-gemini-pro](https://github.com/gurveeer/mcp-server-gemini-pro)** - ⭐ 14
   A state-of-the-art Model Context Protocol (MCP) server that provides seamless integration with Google's Gemini AI models. This server enables Claude Desktop and other MCP-compatible clients to leverage the full power of Gemini's advanced AI capabilities.

3352. **[opentargets-mcp](https://github.com/nickzren/opentargets-mcp)** - ⭐ 14
   MCP server for Open Targets Data

3353. **[MCP-Platform](https://github.com/Data-Everything/MCP-Platform)** - ⭐ 14
   A flexible platform that provides Docker & Kubernetes backends, a lightweight CLI (mcpt), and client utilities for seamless MCP integration. Spin up servers from templates, route requests through a single endpoint with load balancing, and support both deployed (HTTP) and local (stdio) transports — all with sensible defaults and YAML-based configs

3354. **[mcp-server](https://github.com/configcat/mcp-server)** - ⭐ 14
   Official ConfigCat Model Context Protocol (MCP) Server 

3355. **[mcp-config-editor](https://github.com/kaichen/mcp-config-editor)** - ⭐ 14
   A simple GUI for managing MCP servers, for easy toggle mcp servers.

3356. **[deep-directory-tree-mcp](https://github.com/andredezzy/deep-directory-tree-mcp)** - ⭐ 14
   Powerful Model Context Protocol (MCP) implementation for visualizing directory structures with real-time updates, configurable depth, and smart exclusions for efficient project navigation

3357. **[mcpdog](https://github.com/kinhunt/mcpdog)** - ⭐ 14
   🐕 Universal MCP Server Manager - Configure once, manage multiple MCP servers through a single interface. Perfect for Claude   Desktop, Claude Code, Cursor, Gemini CLI & AI assistants. Web dashboard, auto-detection, unified proxy layer.

3358. **[mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian)** - ⭐ 14
   simple mcp server for interacting with local obsidian notes

3359. **[local-mcp-gateway](https://github.com/DXHeroes/local-mcp-gateway)** - ⭐ 14
   Aggregate multiple MCP servers into a single endpoint with web UI, OAuth 2.1, and profile-based tool management

3360. **[mcp-client-compatibility](https://github.com/tadata-org/mcp-client-compatibility)** - ⭐ 14

3361. **[django-mcp](https://github.com/hyperb1iss/django-mcp)** - ⭐ 14
    Connect Django apps to AI assistants with Model Context Protocol. Simple decorators expose models, admin functions, and custom tools to Claude and other AI assistants.

3362. **[mcp.zig](https://github.com/muhammad-fiaz/mcp.zig)** - ⭐ 14
   A comprehensive Model Context Protocol (MCP) library for Zig — bringing MCP support to the Zig ecosystem.

3363. **[davinci-mcp-professional](https://github.com/Positronikal/davinci-mcp-professional)** - ⭐ 14
   An enterprise-grade MCP server that exposes the full functionality of DaVinci Resolve and DaVinci Resolve Studio (through version 20) to either Claude Desktop or Cursor MCP clients. Fully configured and tested as a Claude Desktop Extension making installation as easy as clicking a button. Supports both Windows and Macintosh.

3364. **[programmatic-tool-calling-ai-sdk](https://github.com/cameronking4/programmatic-tool-calling-ai-sdk)** - ⭐ 14
   ⚡ Cut LLM inference costs 80% with Programmatic Tool Calling. Instead of N tool call round-trips, generate JavaScript to orchestrate tools in Vercel Sandbox. Supports Anthropic, OpenAI, 100+ models via AI Gateway. Novel MCP Bridge for external service integration.

3365. **[mcp-kling](https://github.com/199-mcp/mcp-kling)** - ⭐ 14
   🎬 The FIRST MCP server for Kling AI video generation! Generate stunning AI videos directly from Claude.

3366. **[companies-house-mcp](https://github.com/stefanoamorelli/companies-house-mcp)** - ⭐ 14
   🇬🇧🏦 MCP server for UK Companies House API - Search companies, retrieve detailed information, filing history, officers, and charges data through the Model Context Protocol

3367. **[mcp-time](https://github.com/TheoBrigitte/mcp-time)** - ⭐ 14
   MCP (Model Context Protocol) server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities

3368. **[dx-toolkit](https://github.com/youdotcom-oss/dx-toolkit)** - ⭐ 14
   Open-source toolkit enabling developers to integrate You.com's AI capabilities into their workflows

3369. **[Convert-Markdown-PDF-MCP](https://github.com/seanivore/Convert-Markdown-PDF-MCP)** - ⭐ 14
   Markdown To PDF Conversion MCP

3370. **[awesome-finance-mcp](https://github.com/BlockRunAI/awesome-finance-mcp)** - ⭐ 14
   A curated list of MCP servers for AI finance agents

3371. **[mcpskills-cli](https://github.com/dhanababum/mcpskills-cli)** - ⭐ 14
   Generate Agent Skills from MCP server tools. Connects via Streamable HTTP, discovers tools, and outputs a skill with schema docs and a call script in the language of your choice.

3372. **[gemini-webapi-mcp](https://github.com/AndyShaman/gemini-webapi-mcp)** - ⭐ 14
   MCP server for Google Gemini — free image generation, editing & chat via browser cookies. No API keys needed.

3373. **[clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server)** - ⭐ 14
   ClickUp MCP Server - Integrate ClickUp project management with AI through Model Context Protocol

3374. **[ironcurtain](https://github.com/provos/ironcurtain)** - ⭐ 14
   A secure* runtime for autonomous AI agents. Policy from plain-English constitutions. (*https://ironcurtain.dev)

3375. **[outlook-mcp](https://github.com/XenoXilus/outlook-mcp)** - ⭐ 13
   MCP server for Microsoft Office 365 Outlook – email, calendar & SharePoint integration for Claude, ChatGPT, and AI assistants via Microsoft Graph API

3376. **[spring-ai-mcp-deepseek](https://github.com/firefly0512/spring-ai-mcp-deepseek)** - ⭐ 13
   使用 Spring AI 整合 MCP 服务，包括 MCP server 和 deepseek client

3377. **[llamacppMCPClientDemo](https://github.com/brucepro/llamacppMCPClientDemo)** - ⭐ 13
   standalone react MCP client using SSE

3378. **[sample-multi-tenant-saas-mcp-server](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)** - ⭐ 13
   Multi-Tenant remote MCP server with Amazon Cognito and remote client with Amazon Bedrock hosted on AWS

3379. **[mcp-chat-client](https://github.com/Ceeon/mcp-chat-client)** - ⭐ 13
   基于高德地图MCP服务的聊天客户端

3380. **[mcp-client-laravel](https://github.com/RedberryProducts/mcp-client-laravel)** - ⭐ 13
   Laravel-native client for Model Context Protocol (MCP) servers. Built by Redberry (Diamond-tier Laravel partner). Used by LarAgent and other frameworks to enable AI agent functionality.

3381. **[mcp-perplexity-server](https://github.com/PoliTwit1984/mcp-perplexity-server)** - ⭐ 13
   A Model Context Protocol (MCP) server for intelligent code analysis and debugging using Perplexity AI’s API, seamlessly integrated with the Claude desktop client.

3382. **[mcp-more](https://github.com/toosean/mcp-more)** - ⭐ 13
   A modern desktop application for managing Model Context Protocol (MCP) servers.

3383. **[MCP-Manager-GUI](https://github.com/gabrielbacha/MCP-Manager-GUI)** - ⭐ 13
   MCP Toggle is a simple GUI tool to help you manage MCP servers across clients seamlessly.

3384. **[easy-mcp-use](https://github.com/dforel/easy-mcp-use)** - ⭐ 13
   Easy-MCP-Use is the open source TypeScript library to connect any LLM to any MCP server and build custom agents that have tool access, without using closed source or application clients.

3385. **[mcphawk](https://github.com/tech4242/mcphawk)** - ⭐ 13
   MCPHawk is a new Logging & Monitoring solution for Model Context Protocol (MCP) traffic, providing deep visibility into MCP client-server interactions. It started off as a mix between Wireshark and mcpinspector, purpose-built for the MCP ecosystem, and is now slowly turning into something more.

3386. **[mcp-test-client](https://github.com/crazyrabbitLTC/mcp-test-client)** - ⭐ 13
   MCP Test Client is a TypeScript testing utility for Model Context Protocol (MCP) servers.

3387. **[mongo-mcp](https://github.com/1RB/mongo-mcp)** - ⭐ 13
   MCP server that provide tools to LLMs such as claude in cursor to interact with MongoDB

3388. **[memory-mcp-server](https://github.com/hpkv-io/memory-mcp-server)** - ⭐ 13
   A MCP (Model Context Protocol) server providing long-term memory for LLMs

3389. **[mcp-web-search-tool](https://github.com/gabrimatic/mcp-web-search-tool)** - ⭐ 13
   A MCP server providing real-time web search capabilities to any AI model.

3390. **[jadx-mcp-server](https://github.com/Qtty/jadx-mcp-server)** - ⭐ 13
   A Pure-Java MCP Server for JaDX Android Reverse Engineering Tool

3391. **[mcp-client-langchain-ts](https://github.com/hideya/mcp-client-langchain-ts)** - ⭐ 13
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / TypeScript

3392. **[prompt-engineer-mcp-server](https://github.com/hireshBrem/prompt-engineer-mcp-server)** - ⭐ 13
   Write 10x better prompts using Prompt Engineer MCP server.

3393. **[mcp-windows-automation](https://github.com/mukul975/mcp-windows-automation)** - ⭐ 13
   🚀 AI-Powered Windows Automation Server using Model Context Protocol (MCP) | Control Windows apps, automate tasks, and manage systems through natural language commands with Claude, ChatGPT & other AI assistants | 80+ automation tools

3394. **[google-mcp-remote](https://github.com/vakharwalad23/google-mcp-remote)** - ⭐ 13
   Collection of Google-native tools (e.g., Gmail, Calendar) for the MCP

3395. **[mcp_review_code_tool](https://github.com/wenkil/mcp_review_code_tool)** - ⭐ 13
   A code review tool based on Model Context Protocol (MCP) that leverages OpenAI's capabilities for intelligent code analysis and review. | 基于模型上下文协议(MCP)的代码审查工具，利用OpenAI的能力进行智能代码分析和审查。

3396. **[sherpa](https://github.com/CartographAI/sherpa)** - ⭐ 13
   Chat with any codebase with MCP servers in a single command

3397. **[capture-mcp-server](https://github.com/blencorp/capture-mcp-server)** - ⭐ 13
   AI-native Model Context Protocol (MCP) server that integrates SAM.gov, USASpending.gov, and Tango APIs to capture and analyze federal procurement and spending data through natural language queries. Responses include both human-readable text and structured JSON so MCP-compatible clients can consume the data programmatically.

3398. **[mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player)** - ⭐ 13
   MCP server to manage Spotify from MCP clients

3399. **[codepilot](https://github.com/rohittcodes/codepilot)** - ⭐ 13
   A multi-agent CLI tool powered by Swarms-rs and Composio

3400. **[openwebui-mcp-setup](https://github.com/sonzentherevolution/openwebui-mcp-setup)** - ⭐ 13
    Universal MCPO/MCP bridge for Open Web UI with AI-powered configuration. Automated setup generation, Docker support, beginner-friendly. Any AI assistant can instantly convert MCP configs to   working Open Web UI integrations.

3401. **[mcp-meme-sticky](https://github.com/nkapila6/mcp-meme-sticky)** - ⭐ 13
   Create AI generated memes using MCP Meme Sticky. Can converted generated memes into stickers for Telegram or WhatsApp (WA coming soon).  ✨ no APIs required ✨.

3402. **[mcp-safe-run](https://github.com/ithena-one/mcp-safe-run)** - ⭐ 13
   Tired of hardcoding secrets like API keys in your MCP client configuration (e.g., mcp.json, claude_desktop_config.json)? mcp-secure-launcher lets you run your existing MCP servers securely without modifying them.

3403. **[gsd-task-manager](https://github.com/vscarpenter/gsd-task-manager)** - ⭐ 13
   Stop juggling, start finishing. GSD Task Manager makes it easy to sort your to-dos into what’s urgent and what’s important, so you can finally get stuff done without burning out. It’s simple, visual, and works entirely offline.

3404. **[AgentStack](https://github.com/ssdeanx/AgentStack)** - ⭐ 13
   AgentStack is a production-grade multi-agent framework built on Mastra, delivering 50+ enterprise tools, 25+ specialized agents, and A2A/MCP orchestration for scalable AI systems. Focuses on financial intelligence, RAG pipelines, observability, and secure governance.

3405. **[devtap](https://github.com/killme2008/devtap)** - ⭐ 13
   Bridge build/dev process output to AI coding sessions via MCP — supports Claude Code, Codex, OpenCode, Gemini CLI, and aider

3406. **[sarvam-mcp-server](https://github.com/Shobhit-Nagpal/sarvam-mcp-server)** - ⭐ 13
   talk to sarvam APIs directly, without code.

3407. **[signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server)** - ⭐ 13
   Connect your Signoz Instance with Cursor, Claude Desktop or any other MCP Compatible Client

3408. **[vmware-esxi-mcp](https://github.com/uldyssian-sh/vmware-esxi-mcp)** - ⭐ 13
   Professional Model Context Protocol (MCP) server for VMware ESXi hypervisor management. Enterprise-ready solution with secure interfaces for ESXi operations, VM lifecycle management, and infrastructure monitoring.

3409. **[automagik-tools](https://github.com/namastexlabs/automagik-tools)** - ⭐ 13
   From API to AI in 30 Seconds - Transform any API into an intelligent MCP agent that learns, adapts, and speaks human

3410. **[vector_mcp](https://github.com/sergiobayona/vector_mcp)** - ⭐ 13
   A server implementation for the Model Context Protocol (MCP) in Ruby.

3411. **[RAG-MCP](https://github.com/cr21/RAG-MCP)** - ⭐ 13
   Simple RAG implementation from scratch using MCP, focusing on Perception, Memory, Decision and Action

3412. **[slack-mcp-server](https://github.com/jtalk22/slack-mcp-server)** - ⭐ 13
   Session-based Slack MCP server for local and hosted runtimes.

3413. **[pentest-mcp-server](https://github.com/LayeSec006/pentest-mcp-server)** - ⭐ 13
   MCP server for penetration testing

3414. **[pentesting-cyber-mcp](https://github.com/hackersatyamrastogi/pentesting-cyber-mcp)** - ⭐ 13
   🔐 50+ MCP Security Servers for AI-Powered Pentesting | Integrate Nmap, Burp Suite, Nuclei, Shodan, BloodHound, Semgrep, Trivy | Model Context Protocol for Cybersecurity

3415. **[taiga-ui-mcp](https://github.com/taiga-family/taiga-ui-mcp)** - ⭐ 13
   Taiga UI MCP server providing documentation search and scaffolding tools.

3416. **[owl-mcp](https://github.com/ai4curation/owl-mcp)** - ⭐ 13
   MCP server for OWL applications

3417. **[XcodeMCPWrapper](https://github.com/SoundBlaster/XcodeMCPWrapper)** - ⭐ 13
   MCP that makes Xcode 26.3's MCP compatible with Cursor and other strict MCP-spec-compliant clients

3418. **[opencode-browser](https://github.com/michaljach/opencode-browser)** - ⭐ 13
   Browser automation plugin for OpenCode AI editor - Control Chrome/Edge with AI, automate web testing, scraping & form filling via MCP integration

3419. **[SchemaPin](https://github.com/ThirdKeyAI/SchemaPin)** - ⭐ 13
   The SchemaPin protocol for cryptographically signing and verifying AI agent tool schemas to prevent supply-chain attacks.

3420. **[mcp-delphi](https://github.com/flydev-fr/mcp-delphi)** - ⭐ 13
   Delphi and Lazarus/FPC MCP server: build/clean pascal projects via MCP tools.

3421. **[shodan-mcp](https://github.com/Vorota-ai/shodan-mcp)** - ⭐ 13
   Shodan MCP server for Claude, Cursor & VS Code. 20 tools for passive reconnaissance, CVE/CPE intelligence, DNS analysis, and device search. 4 tools work free without an API key. OSINT and vulnerability research from your IDE.

3422. **[mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce)** - ⭐ 13
   🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object.

3423. **[mcp-server-weather-js](https://github.com/hideya/mcp-server-weather-js)** - ⭐ 13
   Simple Weather MCP Server Example

3424. **[inspector](https://github.com/mcp-use/inspector)** - ⭐ 13
   Modern MCP Inspector for remote mcp servers with support for Apps SDK

3425. **[Unity-AI-ParticleSystem](https://github.com/IvanMurzak/Unity-AI-ParticleSystem)** - ⭐ 13
   AI-powered tools for Unity Particle System. Create and modify Particle System directly through natural language commands.

3426. **[temple-bridge](https://github.com/templetwo/temple-bridge)** - ⭐ 12
   The Sovereign Stack: MCP server binding local AI capabilities with governance protocols. 100% local operation with memory, conscience, and recursive observation.

3427. **[llama-nexus](https://github.com/LlamaEdge/llama-nexus)** - ⭐ 12
   A gateway service designed to manage and orchestrate OpenAI-compatible API servers with MCP support.

3428. **[st_rag_mcp](https://github.com/digital-duck/st_rag_mcp)** - ⭐ 12
   MCP streamlit client with RAG support for tool search

3429. **[n8n-coolify-mcp-tools](https://github.com/wrediam/n8n-coolify-mcp-tools)** - ⭐ 12
   This workflow leverages the Community n8n MCP Client and my new Coolify MCP Server to interact with your Coolify infrastructure using MCP (Model Context Protocol). 

3430. **[mcp-server-manager](https://github.com/infinitimeless/mcp-server-manager)** - ⭐ 12
   A tool to create, build, and manage MCP servers for use with Claude and other MCP clients

3431. **[MCP-Client-Server-for-agents](https://github.com/qmatteoq/MCP-Client-Server-for-agents)** - ⭐ 12
   This project demonstrates a Model Context Protocol (MCP) server and client implementation in .NET

3432. **[xcf](https://github.com/CodeFreezeAI/xcf)** - ⭐ 12
   Xcode MCP Server xcf is a 100% Swift based allowing you to integrate Xcode with your favorite AI IDE or MCP Client

3433. **[CursorMCPMonitor](https://github.com/willibrandon/CursorMCPMonitor)** - ⭐ 12
   Real-time monitoring tool for Model Context Protocol (MCP) interactions in Cursor AI editor. Track, analyze, and debug AI context exchanges between LLM clients and servers. Supports log rotation, pattern matching, and color-coded event visualization.

3434. **[Tinvo](https://github.com/imxcstar/Tinvo)** - ⭐ 12
   LLM AI Client based on Blazor. (openai, chatgpt, llama, ollama, onnx, deepseekr1...)

3435. **[gemma-mcp](https://github.com/monatis/gemma-mcp)** - ⭐ 12
   MCP Client for Gemma-3

3436. **[muster](https://github.com/giantswarm/muster)** - ⭐ 12
   MCP tool management and workflow proxy

3437. **[proxy-base-agent](https://github.com/TheProxyCompany/proxy-base-agent)** - ⭐ 12
   A stateful agent with 100% reliable tool use. Build custom agents on any LLM with guaranteed state consistency.

3438. **[create-mcp-server-kit](https://github.com/Epi-1120/create-mcp-server-kit)** - ⭐ 12
   Scaffold a production-ready Model Context Protocol (MCP) server in seconds.

3439. **[memory-visualizer](https://github.com/mjherich/memory-visualizer)** - ⭐ 12
   Interactive visualizer for Anthropic's Memory MCP knowledge graphs. Instantly explore, debug, and analyze entities, relations, and observations from memory.json files in the Model Context Protocol.

3440. **[MIST](https://github.com/CLoaKY233/MIST)** - ⭐ 12
   MCP server empowering AI assistants with real-world capabilities: Gmail, Calendar, Tasks, Git integration, and note management. Bridges AI assistants to external services through standardized protocol with secure authentication.

3441. **[llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator)** - ⭐ 12
   The ultimate AI-powered generator for llms.txt and llms-full.txt files. 

3442. **[ckan-mcp-server](https://github.com/ondics/ckan-mcp-server)** - ⭐ 12
   A Model Context Protocol (MCP) server for the CKAN API that enables browsing and managing CKAN data portals through MCP-compatible clients.

3443. **[claude_autoapprove](https://github.com/PyneSys/claude_autoapprove)** - ⭐ 12
   Autoapprove support for claude

3444. **[ia-na-pratica](https://github.com/Code4Delphi/ia-na-pratica)** - ⭐ 12
   IA na Prática: LLM, RAG, MCP, Agents, Function Calling, Multimodal, TTS/STT e mais

3445. **[PackageFlow](https://github.com/runkids/PackageFlow)** - ⭐ 12
   A visual DevOps hub for npm scripts, Git, workflows, and deploy — controllable by AI via MCP.

3446. **[ggMCP4VSCode](https://github.com/n2ns/ggMCP4VSCode)** - ⭐ 12
   Google Gemini Model Context Protocol (MCP) Client for VS Code. Connect AI assistants to local context & tools.

3447. **[SQL_MCP_Server](https://github.com/pawankumar94/SQL_MCP_Server)** - ⭐ 12
   SQLGenius is an AI-powered SQL assistant that converts natural language to SQL queries using Vertex AI's Gemini Pro. Built with MCP and Streamlit, it provides an intuitive interface for BigQuery data exploration with real-time visualization and schema management.

3448. **[nestjs-mcp](https://github.com/orbit-codes/nestjs-mcp)** - ⭐ 12
   An opinionated MCP module for NestJS

3449. **[snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server)** - ⭐ 12
   MCP Server for connecting to Snowflake with read-only questions

3450. **[mcp-server-kintone](https://github.com/macrat/mcp-server-kintone)** - ⭐ 12
   MCP server for kintone

3451. **[mcp-server-webscan](https://github.com/bsmi021/mcp-server-webscan)** - ⭐ 12
   A Model Context Protocol (MCP) server for web content scanning and analysis. This server provides tools for fetching, analyzing, and extracting information from web pages.

3452. **[swift-context-protocol](https://github.com/1amageek/swift-context-protocol)** - ⭐ 12
   swift-context-protocol is a Swift-based implementation of the Model Context Protocol (MCP) for AI contexts. It leverages Swift’s distributed actor model to enable type-safe, asynchronous remote invocation of tools, resources, and prompts.

3453. **[agent-identity-protocol](https://github.com/ArangoGutierrez/agent-identity-protocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3454. **[md2confluence-mcp](https://github.com/Gyeom/md2confluence-mcp)** - ⭐ 12
   MCP server to upload Markdown to Confluence. Auto-converts Mermaid diagrams, code blocks, images, and tables.

3455. **[puppeteer-mcp-server](https://github.com/sultannaufal/puppeteer-mcp-server)** - ⭐ 12
   Self-hosted Puppeteer MCP server with remote SSE access, API key authentication, and Docker deployment. Complete tool suite for browser automation via Model Context Protocol.

3456. **[_b00t_](https://github.com/elasticdotventures/_b00t_)** - ⭐ 12
   🥾 _b00t_:  brians dotfiles aka state of the art agentic tooling & context initialization

3457. **[jenkins-mcp-server](https://github.com/AshwiniGhuge3012/jenkins-mcp-server)** - ⭐ 12
   An MCP server for interacting with a Jenkins server. Allows you to trigger jobs, check build statuses, and manage your Jenkins instance through MCP.

3458. **[openagentidentityprotocol](https://github.com/openagentidentityprotocol/openagentidentityprotocol)** - ⭐ 12
   Agent Identity Protocol - Zero-trust security layer for AI agents. Policy enforcement proxy for MCP with Human-in-the-Loop approval, DLP scanning, and audit logging.

3459. **[subcog](https://github.com/zircote/subcog)** - ⭐ 12
   Persistent memory system for AI coding assistants. Captures decisions, learnings, and context from coding sessions. Features hybrid search (semantic + BM25), MCP server integration, SQLite persistence with knowledge graph, and proactive memory surfacing. Written in Rust.

3460. **[osmmcp](https://github.com/NERVsystems/osmmcp)** - ⭐ 12
   OpenStreetMap MCP server providing precision geospatial tools for LLMs via Model Context Protocol. Features geocoding, routing, nearby places, neighborhood analysis, EV charging stations, and more.

3461. **[garmin-connect-mcp](https://github.com/eddmann/garmin-connect-mcp)** - ⭐ 12
   MCP server enabling LLMs to interact with Garmin Connect - activities, health metrics, sleep data, and training analysis

3462. **[dav-mcp](https://github.com/PhilflowIO/dav-mcp)** - ⭐ 12
   Transform AI agents into orchestrating assistants managing calendars, contacts, and tasks

3463. **[mcp-add](https://github.com/paoloricciuti/mcp-add)** - ⭐ 12
   Universal cli to add an MCP server to a variety of clients

3464. **[mcp-client-gen](https://github.com/kriasoft/mcp-client-gen)** - ⭐ 12
   Turn any MCP server into a type-safe TypeScript SDK in seconds - with    OAuth 2.1 and multi-provider support

3465. **[cv-resume-builder-mcp](https://github.com/eyaab/cv-resume-builder-mcp)** - ⭐ 12
   AI-powered CV and resume builder using Model Context Protocol. Automatically sync your achievements from Jira, Credly, LinkedIn, and git. Keep your CV always up-to-date.

3466. **[agent-board](https://github.com/quentintou/agent-board)** - ⭐ 12
   Open-source multi-agent task board for OpenClaw. Kanban + DAG dependencies + MCP server + auto-retry + audit trail. Built for autonomous AI agent teams.

3467. **[mcp-ecosystem](https://github.com/SynkraAI/mcp-ecosystem)** - ⭐ 12
   MCP Ecosystem: Docker MCP Toolkit, IDE Configs & Presets for AIOS

3468. **[github-to-mcp](https://github.com/nirholas/github-to-mcp)** - ⭐ 12
   Convert GitHub repositories to MCP servers automatically. Extract tools from OpenAPI, GraphQL & REST APIs for Claude Desktop, Cursor, Windsurf, Cline & VS Code. AI-powered code generation creates type-safe TypeScript/Python MCP servers. Zero config setup - just paste a repo URL. Built for AI assistants & LLM tool integration.

3469. **[awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** - ⭐ 12
   Awesome list of MCP servers for interacting with hardware and the physical world.

3470. **[minimal-godot-mcp](https://github.com/ryanmazzolini/minimal-godot-mcp)** - ⭐ 12
   Lightweight MCP server bridging Godot LSP to MCP clients for GDScript validation

3471. **[istek](https://github.com/istekapp/istek)** - ⭐ 12
   The API client built for AI agents. HTTP, GraphQL, gRPC, WebSocket, MQTT + MCP."

3472. **[MCPGateway](https://github.com/abdullah1854/MCPGateway)** - ⭐ 12
   Open-source MCP server — progressive tool discovery, code execution, intelligent routing & token optimization across 50+ tools

3473. **[phabricator-mcp](https://github.com/freelancer/phabricator-mcp)** - ⭐ 12
   MCP server for Phabricator

3474. **[domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp)** - ⭐ 12
   Zero-config domain availability MCP for Claude & ChatGPT. AI suggestions, premium/auction detection via GoDaddy, RDAP/WHOIS fallback. Stdio + HTTP.

3475. **[fcpxml-mcp-server](https://github.com/DareDev256/fcpxml-mcp-server)** - ⭐ 12
   🎬 The first AI-powered MCP server for Final Cut Pro XML. Control your edits with natural language.

3476. **[porkbun-mcp-server](https://github.com/miraclebakelaser/porkbun-mcp-server)** - ⭐ 11
   MCP server implementation for managing domains, DNS, and SSL via the Porkbun API.

3477. **[context-kit](https://github.com/eyalzh/context-kit)** - ⭐ 11
   A CLI tool and MCP client, used to create spec files for AI coding agents with context baked in

3478. **[mcp_client_rust](https://github.com/darinkishore/mcp_client_rust)** - ⭐ 11

3479. **[mcp-client](https://github.com/EuclideanAI/mcp-client)** - ⭐ 11
   A custom Model Context Protocol (MCP) Client interface with integrated LLM agent chat capabilities built with Next.js and the Vercel AI SDK

3480. **[MCP_Client](https://github.com/andrewdeng318/MCP_Client)** - ⭐ 11

3481. **[trebuchet](https://github.com/fuzzball-muck/trebuchet)** - ⭐ 11
   A MUD/MUCK/MUSH chat client with MCP/GUI support.

3482. **[systemprompt-mcp-gmail](https://github.com/Ejb503/systemprompt-mcp-gmail)** - ⭐ 11
   A specialized Model Context Protocol (MCP) server that enables you to search, read, delete and send emails from your Gmail account, leveraging an AI Agent to help with each operation.  Optimized for Systemprompt MCP Voice client.

3483. **[mcp-client-app](https://github.com/RegiByte/mcp-client-app)** - ⭐ 11
   A mcp client chat application built for learning purposes

3484. **[mcp-browser-automation](https://github.com/hrmeetsingh/mcp-browser-automation)** - ⭐ 11
   Model Context Protocol based AI Agent that runs a browser from Claude desktop

3485. **[simple-nodejs-mcp-client](https://github.com/sawa-zen/simple-nodejs-mcp-client)** - ⭐ 11
   This is a study repository for implementing a Model Context Protocol (MCP) client. It features a simple interactive MCP client implemented in Node.js.

3486. **[langchain-mcp-tools-ts-usage](https://github.com/hideya/langchain-mcp-tools-ts-usage)** - ⭐ 11
   MCP Tools Usage From LangChain ReAct Agent / Example in TypeScript

3487. **[mcp-chat-widget](https://github.com/aimdoc-ai/mcp-chat-widget)** - ⭐ 11
   Configure, host and embed MCP-enabled chat widgets for your website or product. Lightweight and extensible Chatbase clone to remotely configure and embed your agents anywhere.

3488. **[oauth-callback](https://github.com/kriasoft/oauth-callback)** - ⭐ 11
   Lightweight OAuth 2.0 authorization code capture for CLI tools & desktop   apps. Works with Node.js, Deno, Bun. MCP SDK ready.

3489. **[semantictool](https://github.com/promptmesh/semantictool)** - ⭐ 11
   tool management service for performing vector tool calling at scale.

3490. **[mcpconnect](https://github.com/rocket-connect/mcpconnect)** - ⭐ 11
   Inspect and debug Model Context Protocol servers directly in your browser.

3491. **[locust-mcp-server](https://github.com/QAInsights/locust-mcp-server)** - ⭐ 11
   A Model Context Protocol (MCP) server implementation for running Locust load tests. This server enables seamless integration of Locust load testing capabilities with AI-powered development environments.

3492. **[scorable-mcp](https://github.com/root-signals/scorable-mcp)** - ⭐ 11
   MCP for Scorable Evaluation Platform

3493. **[mcp-boilerplate](https://github.com/iamsrikanthnani/mcp-boilerplate)** - ⭐ 11
   A powerful, production-ready MCP server implementing the Model Context Protocol with robust SSE transport, built-in tools, and comprehensive error handling. Seamlessly connect AI models to data sources with enterprise-grade stability and performance.

3494. **[emcp](https://github.com/joeymeere/emcp)** - ⭐ 11
   A framework for building simple MCP servers with custom middleware

3495. **[local-history-mcp](https://github.com/xxczaki/local-history-mcp)** - ⭐ 11
   MCP server for accessing VS Code/Cursor's Local History

3496. **[openalgo-mcp](https://github.com/marketcalls/openalgo-mcp)** - ⭐ 11
   Documentation

3497. **[polaris](https://github.com/octu0/polaris)** - ⭐ 11
   Distributed AI Agent Framework

3498. **[mcp-server-zotero-dev](https://github.com/introfini/mcp-server-zotero-dev)** - ⭐ 11
   Give your AI assistant superpowers for Zotero plugin development. 25 tools for screenshots, DOM inspection, JavaScript execution, build integration, and debugging via Model Context Protocol.

3499. **[glm5-mcp](https://github.com/Arkya-AI/glm5-mcp)** - ⭐ 11
   Reduce Claude Desktop consumption by 10x - Integrate Z.ai's GLM-5 (744B params) with Claude via MCP for intelligent task delegation

3500. **[french-tax-mcp](https://github.com/cornelcroi/french-tax-mcp)** - ⭐ 11
   MCP server for French tax calculations and information - enables AI assistants to provide accurate French tax guidance

3501. **[springboot-ai-mcp-example](https://github.com/duongminhhieu/springboot-ai-mcp-example)** - ⭐ 11
   Example Spring AI Model Context Protocol (MCP)

3502. **[mcp-space](https://github.com/tharuneshwar-s/mcp-space)** - ⭐ 11
   MCP Space is a no-code platform for building and deploying AI tools using the Model Context Protocol (MCP). Create powerful AI agents through an intuitive chat interface without writing code, then deploy with one click to Cloudflare Workers. Combines a Next.js frontend with Google ADK backend for a seamless AI development experience.

3503. **[druid-mcp-server](https://github.com/iunera/druid-mcp-server)** - ⭐ 11
   A comprehensive Model Context Protocol (MCP) server for Apache Druid that provides extensive tools, resources, and AI-assisted prompts for managing and analyzing Druid clusters. Built with Spring Boot and Spring AI, this server enables seamless integration between AI assistants and Apache Druid through standardized MCP protocol.

3504. **[obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** - ⭐ 11
   MCP server for Obsidian vault management - enables Claude and other AI assistants to read, write, search, and organize your notes

3505. **[trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp)** - ⭐ 11
   TrainingPeaks MCP server for Claude Desktop. No API approval needed - works with any account. Query workouts, CTL/ATL/TSB fitness data, power PRs via natural language.

3506. **[mcp-client-langchain-py](https://github.com/hideya/mcp-client-langchain-py)** - ⭐ 11
   Simple MCP Client CLI Implementation Using LangChain ReAct Agent / Python

3507. **[stata-workbench](https://github.com/tmonk/stata-workbench)** - ⭐ 11
   A VS Code compatible extension (Cursor, Windsurf, Antigravity etc.) that allows Stata code to be run directly from the editor. Enables AI agents to directly interact with Stata. Powered by mcp-stata, https://github.com/tmonk/mcp-stata.

3508. **[ProxmoxMCP-advance](https://github.com/Markermav/ProxmoxMCP-advance)** - ⭐ 11
   ProxmoxMCP (advance): MCP for Proxmox integration in Claude, Goose, Cline, any client.

3509. **[mcp-interactive-terminal](https://github.com/amol21p/mcp-interactive-terminal)** - ⭐ 11
   MCP server that gives AI agents (Claude Code, Cursor, Windsurf) real interactive terminal sessions — REPLs, SSH, databases, Docker, and any interactive CLI with clean output and smart completion detection

3510. **[mcpkit](https://github.com/cybertheory/mcpkit)** - ⭐ 11
   Easy to use Official MCP Registry Client UI. npx @cybertheory/mcpkit

3511. **[better-notion-mcp](https://github.com/n24q02m/better-notion-mcp)** - ⭐ 11
   Markdown-first MCP server for Notion API - composite tools optimized for AI agents

3512. **[kiro-powers](https://github.com/praveenc/kiro-powers)** - ⭐ 11
   Repository of custom kiro powers. https://kiro.dev/docs/powers/

3513. **[MicrosoftGraph_Transcript_MCP](https://github.com/ITSpecialist111/MicrosoftGraph_Transcript_MCP)** - ⭐ 11
   A remote **Model Context Protocol (MCP)** server that retrieves Microsoft Teams meeting transcripts via the Microsoft Graph API, using delegated **OAuth 2.0 On-Behalf-Of (OBO)** authentication.  Designed for integration with **Microsoft Copilot Studio** (via the MCP Wizard), though any MCP-compatible client can connect.

3514. **[robotmcp_client](https://github.com/robotmcp/robotmcp_client)** - ⭐ 11
   Connect AI models like Claude & GPT with robots using MCP and ROS.

3515. **[cie](https://github.com/kraklabs/cie)** - ⭐ 11
   Code Intelligence Engine — indexes your codebase and gives AI assistants deep understanding via MCP (semantic search, call graphs, 20+ tools)

3516. **[webfetch-mcp](https://github.com/manooll/webfetch-mcp)** - ⭐ 11
   Live Web Access for Your Local AI — Tunable Search & Clean Content Extraction

3517. **[LSP4J-MCP](https://github.com/stephanj/LSP4J-MCP)** - ⭐ 11
   A Java MCP (Model Context Protocol) server that wraps JDTLS (Eclipse JDT Language Server) using LSP4J to provide Java IDE features to AI assistants like Claude.

3518. **[mcp-wikipedia](https://github.com/algonacci/mcp-wikipedia)** - ⭐ 10
   MCP server to give client the ability to access Wikipedia pages

3519. **[taskboard](https://github.com/tcarac/taskboard)** - ⭐ 10
   Local project management with Kanban UI, CLI, and MCP server for AI assistants. SQLite-backed, single binary, installable via Homebrew.

3520. **[claude-context-local](https://github.com/MikeO-AI/claude-context-local)** - ⭐ 10
   🔒 Privacy-first MCP server for Claude using PostgreSQL + Ollama. Local alternative to cloud-based code context with full data sovereignty. No API keys, no external calls, 100% local.

3521. **[langchain-mcp-client](https://github.com/datalayer/langchain-mcp-client)** - ⭐ 10
   🦜🔗 LangChain Model Context Protocol (MCP) Client

3522. **[mcp_client_openai](https://github.com/liangpn/mcp_client_openai)** - ⭐ 10
   适配Openai SDK构建MCP Client

3523. **[mcp-serverman](https://github.com/benhaotang/mcp-serverman)** - ⭐ 10
   a cli/mcp server tool for managing mcp server json config file with version control, profiles and multi-client support

3524. **[py-mcp-sse](https://github.com/jayliangdl/py-mcp-sse)** - ⭐ 10
   MCP Client 与 MCP Server基于SSE方式的样例实现（Python版本）

3525. **[AIFoundry-MCPConnector-FabricGraphQL](https://github.com/LazaUK/AIFoundry-MCPConnector-FabricGraphQL)** - ⭐ 10
   MCP Client and Server apps to demo integration of Azure OpenAI-based AI agent with a Data Warehouse, exposed through GraphQL in Microsoft Fabric.

3526. **[kanboard-mcp](https://github.com/ChristianJStarr/kanboard-mcp)** - ⭐ 10
   Transform your Kanboard.org into an AI-powered project management powerhouse! This plugin enables complete control over Kanboard through the Model Context Protocol (MCP), allowing AI assistants like Cursor, Claude, and other MCP clients to manage your projects through natural language commands.

3527. **[emotion_ai](https://github.com/angrysky56/emotion_ai)** - ⭐ 10
   The Aura Emotion AI system has chroma with a local embedding model, memvid qr code mp4 infinite memory, brainwave and neurochemical simulations, sociobiological reasoning, autonomous subsystem processing with a Gemini flash model so the main model is less taxed, is a MCP client with adaptive tool learning and MCP server. 

3528. **[mcp-express-adapter](https://github.com/Moe03/mcp-express-adapter)** - ⭐ 10
   Run multiple MCP clients on a NodeJS Express server (adapter/middleware)

3529. **[mcp-trace](https://github.com/zabirauf/mcp-trace)** - ⭐ 10
   A TUI to probe the calls between MCP client and server

3530. **[mcp-server-blog](https://github.com/portal-labs-infrastructure/mcp-server-blog)** - ⭐ 10
   Example of a MCP implementation using TypeScript and OAuth.

3531. **[unity-mcp-template](https://github.com/dunward/unity-mcp-template)** - ⭐ 10
   Simple template project for controlling Unity via MCP

3532. **[mcp-agent-proxy](https://github.com/mashh-lab/mcp-agent-proxy)** - ⭐ 10
   An MCP server that exposes local and remote agents across different servers as MCP tools.

3533. **[amazon-seller-mcp](https://github.com/enginterzi/amazon-seller-mcp)** - ⭐ 10
   Transform Your Amazon Business with AI - The first Model Context Protocol (MCP) client that seamlessly connects Claude and other AI agents to Amazon's Selling Partner API, enabling intelligent automation of your entire seller workflow from inventory management to listing optimization.

3534. **[auto-mcp-client](https://github.com/down-to-earth1994/auto-mcp-client)** - ⭐ 10
   基于Spring AI 封装了 mcp-client 服务，目的使web网页智能体也能通过 stdio 和 HTTP SSE（Server-Sent Events） 与 MCP Server 进行交互。项目实现了自动化的连接管理机制，包括自动初始化连接、健康检查、超时关闭以及链接复用等功能

3535. **[mcp-kit](https://github.com/shaharia-lab/mcp-kit)** - ⭐ 10
   MCP (Model Context Protocol) Kit for Go - A Complete MCP solutions for ready to use

3536. **[CodeCompass](https://github.com/alvinveroy/CodeCompass)** - ⭐ 10
   CodeCompass: AI-powered Vibe Coding with MCP. Connects Git repositories to AI assistants like Claude, using Ollama for privacy or OpenAI for cloud. Integrates with VSCode, Cursor, and more.

3537. **[mode-manager-mcp](https://github.com/NiclasOlofsson/mode-manager-mcp)** - ⭐ 10
   MCP Memory Agent Server - A VS Code chatmode and instruction manager with library integration

3538. **[mcp-reporter](https://github.com/cyanheads/mcp-reporter)** - ⭐ 10
   mcp-reporter is a streamlined utility that generates comprehensive capability reports for Model Context Protocol servers, empowering developers to easily understand available functionality across their MCP servers ecosystem for both documentation and integration into other tools.

3539. **[mcp-starter-template-ts](https://github.com/onamfc/mcp-starter-template-ts)** - ⭐ 10
   TypeScript starter template for building Model Context Protocol (MCP) servers, designed to help developers create secure and robust AI-agent-compatible services.

3540. **[prometheus-protocol](https://github.com/prometheus-protocol/prometheus-protocol)** - ⭐ 10
   The trust layer for the open agentic web—giving AI agents a passport, a bank account, and a trusted marketplace to securely interact with the world.

3541. **[rec-us-mcp-server](https://github.com/elizabethsiegle/rec-us-mcp-server)** - ⭐ 10
   Book a San Francisco tennis court via MCP server w/ auth

3542. **[mcp-demo](https://github.com/sshh12/mcp-demo)** - ⭐ 10
   URL MCP is a proof of concept stateless MCP server builder that allows users to build MCP servers without writing or hosting code. It's intended for protocol and security experimentation rather than for building real world MCP integrations.

3543. **[AgentX-mcp-servers](https://github.com/AgentX-ai/AgentX-mcp-servers)** - ⭐ 10
   List of open sourced MCP servers. MIT license. Managed by AgentX with love.

3544. **[mcp-tradovate](https://github.com/0xjmp/mcp-tradovate)** - ⭐ 10
   MCP server for the Tradovate platform

3545. **[mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews)** - ⭐ 10
   An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).

3546. **[glasses-mcp](https://github.com/gourraguis/glasses-mcp)** - ⭐ 10
   Glasses MCP is a simple MCP server that lets your AI agent see and capture the web 👓

3547. **[ObsidianMCPServer](https://github.com/otaviocc/ObsidianMCPServer)** - ⭐ 10
   A Model Context Protocol (MCP) server that enables AI assistants to interact with your Obsidian vault 

3548. **[mcp-sys-bridge](https://github.com/leynier/mcp-sys-bridge)** - ⭐ 10
   An implementation of the Model Context Protocol (MCP), acting as a simple bridge to native OS functionalities like clipboard management and URL handling.

3549. **[sec-edgar-agentkit](https://github.com/stefanoamorelli/sec-edgar-agentkit)** - ⭐ 10
   AI agent toolkit for accessing and analyzing SEC EDGAR filing data. Build intelligent agents with LangChain, MCP-use, Gradio, Dify, and smolagents to analyze financial statements, insider trading, and company filings.

3550. **[context-engineering-mcp](https://github.com/bralca/context-engineering-mcp)** - ⭐ 10
   Context Engineering is a MCP server that gives AI agents perfect understanding of your codebase. Eliminates context loss, reduces token usage, and generates comprehensive feature plans in minutes. Compatible with Cursor, Claude Code, and VS Code.

3551. **[nautobot_mcp](https://github.com/kvncampos/nautobot_mcp)** - ⭐ 10
   Nautobot Model Context Protocol (MCP) Server - Contains STDIO and HTTP Deployments with Embedding Search and RAG.

3552. **[mcp-sqlite-server](https://github.com/prayanks/mcp-sqlite-server)** - ⭐ 10
   These are MCP server implementations for accessing a SQLite database in your MCP client. There is both a SDIO and a SSE implementation.

3553. **[langgraph-mcp-dataanalysis](https://github.com/gongwon-nayeon/langgraph-mcp-dataanalysis)** - ⭐ 10
   DataAnalysis Agent using LangGraph & MCP server and client

3554. **[claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp)** - ⭐ 10
   Anthropic-approved MCP Server | Persistent AI Context | IANA-registered .faf format

3555. **[mcp-go](https://github.com/XiaoConstantine/mcp-go)** - ⭐ 10
   Golang impl of mcp protocol

3556. **[mcpet](https://github.com/shreyaskarnik/mcpet)** - ⭐ 10
   This is a TypeScript-based Model Context Protocol (MCP) server that implements a virtual pet simulation system. It demonstrates core MCP concepts by providing tools for pet care and interaction.

3557. **[miniflux-mcp](https://github.com/tssujt/miniflux-mcp)** - ⭐ 10
   A Model Context Protocol (MCP) server for interacting with Miniflux RSS reader.

3558. **[mcp-spring-ai-mcp-client](https://github.com/chaozai0304/mcp-spring-ai-mcp-client)** - ⭐ 10
   使用java实现mcp client了解底层的调用机制，demo示例

3559. **[mcp-optimizer](https://github.com/StacklokLabs/mcp-optimizer)** - ⭐ 10
   MCP server that acts as an intelligent intermediary between AI clients and multiple MCP servers

3560. **[awesome-mcp](https://github.com/timunbasah3/awesome-mcp)** - ⭐ 10
   🚀 Discover and explore a curated list of MCP servers, tools, and resources for AI assistants, enhancing your development and productivity.

3561. **[biomed-agent](https://github.com/nickzren/biomed-agent)** - ⭐ 10
   Connecting AI agent to biomedical data

3562. **[Simple_MCP_Client](https://github.com/Avento/Simple_MCP_Client)** - ⭐ 10
   Simple MCP Client for OpenAI/Deepseek R1/V3

3563. **[KunAvatar](https://github.com/KunLabAI/KunAvatar)** - ⭐ 10
   基于ollama推理框架本地部署的Agent应用，实现MCP工具调用，短长期记忆等功能。||  A locally deployed agent application built on the Ollama, featuring MCP tool integration along with both short-term and long-term memory support.

3564. **[awesome-mcp](https://github.com/gauravfs-14/awesome-mcp)** - ⭐ 10
   A carefully curated collection of high-quality tools, libraries, research papers, projects, and tutorials centered around Model Context Protocol (MCP) — a novel paradigm designed to enable modular, adaptive coordination between large language models (LLMs) and external tools or data contexts.

3565. **[mcp-for-woocommerce](https://github.com/iOSDevSK/mcp-for-woocommerce)** - ⭐ 10
   WooCommerce MCP Server — WordPress community plugin implementing the Model Context Protocol (MCP) for WooCommerce. Supports STDIO and HTTP streamable transport, with optional JWT authentication. Based on Automattic’s official WordPress MCP.  This plugin is not affiliated with Automattic.

3566. **[openapi-mcp-swagger](https://github.com/salacoste/openapi-mcp-swagger)** - ⭐ 10
   Solve AI context window limits for API docs | Convert any Swagger/OpenAPI to searchable MCP server | AI-powered endpoint discovery & code generation | Works with Cursor, Claude, VS Code

3567. **[mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig)** - ⭐ 10
   A local MCP server that breaks on demand. Test your client against auth failures, disappearing tools, flaky responses, and token expiry, all from a web UI.

3568. **[extract-llms-docs](https://github.com/nirholas/extract-llms-docs)** - ⭐ 10
   Extract documentation for AI agents from any site with llms.txt support. Features MCP server, REST API, batch processing, and multiple export formats.

3569. **[notification-mcp](https://github.com/pinkpixel-dev/notification-mcp)** - ⭐ 10
   A Model Context Protocol server that allows AI agents to play a notification sound via a tool when a task is completed.

3570. **[kroki-mcp](https://github.com/utain/kroki-mcp)** - ⭐ 10
   Kroki-MCP is a Go-based Model Context Protocol tool that converts textual diagram definitions (PlantUML, Mermaid, and more) into images via a Kroki backend. Designed for simplicity and flexibility, it supports both local and remote Kroki servers, offers configurable settings, and outputs multiple formats – making it ideal for developers building AI

3571. **[plumcp](https://github.com/plumce/plumcp)** - ⭐ 10
   Clojure/ClojureScript library for making MCP server and client

3572. **[swift-mcp](https://github.com/DePasqualeOrg/swift-mcp)** - ⭐ 10
   Full-featured Swift SDK for Model Context Protocol servers and clients

3573. **[mcp-coroot](https://github.com/jamesbrink/mcp-coroot)** - ⭐ 10
   MCP server for Coroot observability platform - integrate monitoring, troubleshooting, and configuration tools with AI agents

3574. **[adonis-mcp](https://github.com/7nohe/adonis-mcp)** - ⭐ 10
   An AdonisJS package for building remote MCP servers

3575. **[arxiv-mcp-server](https://github.com/1Dark134/arxiv-mcp-server)** - ⭐ 10
   arXiv MCP Server Client 🐙 enables AI assistants to search, retrieve, analyze, and summarize arXiv papers with features like author/category browsing, trends, and citation insights.

3576. **[webmcp-sh](https://github.com/WebMCP-org/webmcp-sh)** - ⭐ 10
   A modern web-based Model Context Protocol (MCP) playground for testing and developing MCP servers and clients

3577. **[genkit-mcp-client-blender](https://github.com/xprilion/genkit-mcp-client-blender)** - ⭐ 10
   An MCP Client for interfacing with the Blender MCP Server built with Firebase Genkit and Gemini

3578. **[docdex](https://github.com/bekirdag/docdex)** - ⭐ 10
   A document index with MCP, http and client support. https://docdex.org/ 

3579. **[esp32-mcpserver](https://github.com/solnera/esp32-mcpserver)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server framework for ESP32. Seamlessly connect embedded devices to LLMs.

3580. **[asap-protocol](https://github.com/adriannoes/asap-protocol)** - ⭐ 10
   The production-ready standard for async agent orchestration. Stateful and MCP-compliant communication for distributed AI workflows.

3581. **[youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server)** - ⭐ 10
   A comprehensive Model Context Protocol (MCP) server providing real-time YouTube Data API access for AI assistants. Features 14 functions including intelligent content evaluation with technology freshness scoring for knowledge base curation.

3582. **[gtm-mcp](https://github.com/pouyanafisi/gtm-mcp)** - ⭐ 10
   MCP server for Google Tag Manager: read tags/triggers/variables, publish containers, and audit changes via Claude/Gemini.

3583. **[msty-admin-mcp](https://github.com/M-Pineapple/msty-admin-mcp)** - ⭐ 10
   AI-powered administration for Msty Studio Desktop. 24 MCP tools for database insights, config sync, local model orchestration, and Claude handoff workflows.

3584. **[FocusRelayMCP](https://github.com/deverman/FocusRelayMCP)** - ⭐ 10
   Talk to your OmniFocus tasks. An MCP server that lets AI assistants query your tasks, projects, and tags using natural language—no more clicking through endless lists.

3585. **[Azure-Foundry-Webinar](https://github.com/ShivamGoyal03/Azure-Foundry-Webinar)** - ⭐ 10
   This repository is the official companion for the Azure AI Foundry Agent Service Webinar Series. It provides hands-on code samples, modular use cases, and practical guides for building, deploying, and scaling AI agents on Azure.

3586. **[Cognio](https://github.com/0xReLogic/Cognio)** - ⭐ 10
   Persistent semantic memory server for MCP - Give your AI long-term memory that survives across conversations. Lightweight Python server with SQLite storage and semantic search.

3587. **[bookmark-manager-mcp](https://github.com/infinitepi-io/bookmark-manager-mcp)** - ⭐ 10
   A lightweight Model Context Protocol (MCP) server that provides persistent bookmark management for Claude and other MCP-compatible clients. Features categorized storage, resource discovery, and seamless integration with your AI workflow.

3588. **[bruno-mcp](https://github.com/macarthy/bruno-mcp)** - ⭐ 10
   🚀 MCP server for generating Bruno API testing files programmatically. Create collections, environments, requests, and test scripts using AI clients like Claude Desktop.

3589. **[systemprompt-template](https://github.com/systempromptio/systemprompt-template)** - ⭐ 10
   Production AI agent mesh in 3 commands. MCP servers, playbooks, and multi-agent orchestration built on systemprompt-core.

3590. **[chromadb-remote-mcp](https://github.com/meloncafe/chromadb-remote-mcp)** - ⭐ 10
   Remote MCP server for ChromaDB

3591. **[guildbridge](https://github.com/dend/guildbridge)** - ⭐ 10
   🏰 Remotely hosted MCP server for Discord

3592. **[cheatengine-mcp-bridge](https://github.com/beamstar/cheatengine-mcp-bridge)** - ⭐ 10
   🔗 Connect AI to Cheat Engine for fast memory analysis, enabling quick mods and audits without the tedious manual work.

3593. **[toolhive-cloud-ui](https://github.com/stacklok/toolhive-cloud-ui)** - ⭐ 10
   ToolHive Cloud UI surfaces MCP servers running in your infrastructure, highlighting metadata, tool capabilities, and copy-ready endpoints for fast AI agent integrations.

3594. **[Rube](https://github.com/dorucioclea/Rube)** - ⭐ 10
   Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

3595. **[keycloak-mcp](https://github.com/HaithamOumerzoug/keycloak-mcp)** - ⭐ 10
   MCP server that integrates with Keycloak, allowing you to manage Keycloak users and realms through a standardized protocol. It uses the official Keycloak Admin Client to interact with Keycloak's API.

3596. **[photon](https://github.com/portel-dev/photon)** - ⭐ 10
   Build MCP servers from single TypeScript files. One file becomes an MCP server, CLI tool, and web UI — automatically.

3597. **[x402-deploy](https://github.com/nirholas/x402-deploy)** - ⭐ 10
   Turn any API or MCP server into a paid service with x402 

### MCP Clients

*MCP client applications that connect to MCP servers*

1. **[chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)** - ⭐ 41,555
   CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

2. **[bytebot](https://github.com/bytebot-ai/bytebot)** - ⭐ 10,477
   Bytebot is a self-hosted AI desktop agent that automates computer tasks through natural language commands, operating within a containerized Linux desktop environment.

3. **[valuecell](https://github.com/ValueCell-ai/valuecell)** - ⭐ 9,304
   ValueCell is a community-driven, multi-agent platform for financial applications.

4. **[deepchat](https://github.com/ThinkInAIXYZ/deepchat)** - ⭐ 5,528
   🐬DeepChat - A smart assistant that connects powerful AI to your personal world

5. **[ruoyi-ai](https://github.com/ageerle/ruoyi-ai)** - ⭐ 4,828
   RuoYi AI 是一个全栈式 AI 开发平台，旨在帮助开发者快速构建和部署个性化的 AI 应用。

6. **[koog](https://github.com/JetBrains/koog)** - ⭐ 3,757
   Koog is the official Kotlin framework for building predictable, fault-tolerant and enterprise-ready AI agents across all platforms – from backend services to Android and iOS, JVM, and even in-browser environments. Koog is based on our AI products expertise and provides proven solutions for complex LLM and AI problems

7. **[shippie](https://github.com/mattzcarey/shippie)** - ⭐ 2,335
   extendable code review and QA agent 🚢

8. **[open-mcp-client](https://github.com/CopilotKit/open-mcp-client)** - ⭐ 1,641

9. **[supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp)** - ⭐ 1,617
   Your memories are in ChatGPT... But nowhere else. Universal Memory MCP makes your memories available to every single LLM. No logins or paywall. One command to set it up.

10. **[openinference](https://github.com/Arize-ai/openinference)** - ⭐ 869
   OpenTelemetry Instrumentation for AI Observability

11. **[VectorCode](https://github.com/Davidyz/VectorCode)** - ⭐ 809
   A code repository indexing tool to supercharge your LLM experience.

12. **[HyperChat](https://github.com/BigSweetPotatoStudio/HyperChat)** - ⭐ 712
   HyperChat is a Chat client that strives for openness, utilizing APIs from various LLMs to achieve the best Chat experience, as well as implementing productivity tools through the MCP protocol.

13. **[nono](https://github.com/always-further/nono)** - ⭐ 625
   Secure, kernel-enforced sandbox CLI and SDKs for AI agents. Capability-based isolation with secure key management, atomic rollback, cryptographic immutable audit chain of provenance. Run your agents in a zero-trust environment.

14. **[GalwayBus](https://github.com/joreilly/GalwayBus)** - ⭐ 580
   Galway Bus Kotlin Multiplatform project using Jetpack Compose and SwiftUI 

15. **[comunica](https://github.com/comunica/comunica)** - ⭐ 547
   📬 A knowledge graph querying framework for JavaScript

16. **[fleur](https://github.com/fleuristes/fleur)** - ⭐ 532
   The easiest way to discover and install MCPs

17. **[a2a-x402](https://github.com/google-agentic-commerce/a2a-x402)** - ⭐ 459
   The A2A x402 Extension brings cryptocurrency payments to the Agent-to-Agent (A2A) protocol, enabling agents to monetize their services through on-chain payments. This extension revives the spirit of HTTP 402 "Payment Required" for the decentralized agent ecosystem.

18. **[self-dify](https://github.com/datawhalechina/self-dify)** - ⭐ 343
   本教程将全面指导你如何快速搭建自己的AI应用环境，从Docker桌面版的安装与配置开始，到本地部署Dify并自定义AI助手功能，让你轻松实现“猜病例”、“甜蜜哄人”、“新生入学指南”、“小红书读书卡片”与“面试宝典”等多种特色AI应用。并教会你从基础智能体到使用工作流，再到知识库、DeepResearch、数据库、MCP、复杂任务编排等高阶任务，由浅到深的学习掌握基于dify的大模型应用开发。

19. **[mcp-toolbox-sdk-python](https://github.com/googleapis/mcp-toolbox-sdk-python)** - ⭐ 162
   Python SDK for interacting with the MCP Toolbox for Databases. 

20. **[web-hacker](https://github.com/VectorlyApp/web-hacker)** - ⭐ 153
   Reverse engineer web apps

21. **[terminal-ai](https://github.com/dwmkerr/terminal-ai)** - ⭐ 152
   Unopinionated AI for the Shell. A lightweight AI CLI for scripts, pipelines, and automation, with a universal client for MCP, A2A, and other AI protocols. .

22. **[ai](https://github.com/WordPress/ai)** - ⭐ 143
   Demonstrate and deliver AI features by combining all AI Building Blocks into a unified WordPress experience.

23. **[airbyte-agent-connectors](https://github.com/airbytehq/airbyte-agent-connectors)** - ⭐ 107
   🐙 Drop-in tools that give AI agents reliable, permission-aware access to external systems.

24. **[FlowUpdater](https://github.com/FlowArg/FlowUpdater)** - ⭐ 98
   The free and open source solution to update Minecraft.

25. **[ai-microcore](https://github.com/Nayjest/ai-microcore)** - ⭐ 95
   A handy lib for smooth interaction with large language models (LLMs) and crafting AI apps.

26. **[mcp-manager](https://github.com/petiky/mcp-manager)** - ⭐ 95
   This is a visual client tool used to manage MCP (Model Context Protocol). With this tool, you can easily manage and operate the MCP environment without manually performing complex command-line operations.

27. **[hm_editor](https://github.com/huimeicloud/hm_editor)** - ⭐ 78
   一款轻量级、可扩展的、跨平台的、专为医疗信息化设计的电子病历编辑器内核，为EMR（电子病历系统）提供专业的结构化病历编辑与AI接入解决方案。

28. **[mcp-toolbox-sdk-js](https://github.com/googleapis/mcp-toolbox-sdk-js)** - ⭐ 65
   Javascript SDK for interacting with the MCP Toolbox for Databases.

29. **[researcher_agent](https://github.com/lgesuellip/researcher_agent)** - ⭐ 63
   An application built on the Model Context Protocol (MCP) that transforms any website into highly relevant content based on your queries. The app seamlessly integrates with platforms like X, Slack, and among others.

30. **[MCPE-Client-Sources](https://github.com/Turkeii/MCPE-Client-Sources)** - ⭐ 54

31. **[revit-mcp-commandset](https://github.com/revit-mcp/revit-mcp-commandset)** - ⭐ 47
   🔄 Revit-MCP Client | Core implementation of the Revit-MCP protocol that connects LLMs with Revit. Includes essential CRUD commands for Revit elements enabling AI-driven BIM automation.

32. **[deepsecure](https://github.com/DeepTrail/deepsecure)** - ⭐ 44
   Effortlessly secure your AI agents and AI-powered workflows — from prototype to production. Get easy-to-use identity, credential, and access management built for fast-moving AI developers.

33. **[mcp-client-python-example](https://github.com/alejandro-ao/mcp-client-python-example)** - ⭐ 38

34. **[askimo](https://github.com/haiphucnguyen/askimo)** - ⭐ 33
   AI Native App Client App with Built-in Knowledge Base & Multi-Provider Support (OpenAI, Gemini, Ollama,  ...)

35. **[flowllm](https://github.com/FlowLLM-AI/flowllm)** - ⭐ 32
   FlowLLM: Simplifying LLM-based HTTP/MCP Service Development

36. **[mcp-web-client](https://github.com/jinruoxinchen/mcp-web-client)** - ⭐ 28
   MCP Web Client project

37. **[mcpx4j](https://github.com/dylibso/mcpx4j)** - ⭐ 27
   Java client library for https://mcp.run - call portable and secure tools for your AI Agents and Apps

38. **[axonflow](https://github.com/getaxonflow/axonflow)** - ⭐ 26
   AxonFlow — Source-available AI control plane for production LLM systems

39. **[mcpx-py](https://github.com/dylibso/mcpx-py)** - ⭐ 25
   Python client library for https://mcp.run - call portable & secure tools for your AI Agents and Apps

40. **[mcp-client](https://github.com/liuwenzhoa/mcp-client)** - ⭐ 23

41. **[awesome-netsuite-ai](https://github.com/michoelchaikin/awesome-netsuite-ai)** - ⭐ 22
   A curated list of awesome NetSuite AI resources, tools, articles, and community contributions focused on the NetSuite AI Connector Service and MCP (Model Context Protocol) integration.

42. **[luma-api-mcp](https://github.com/lumalabs/luma-api-mcp)** - ⭐ 20
   Powered by Ray (video) and Photon (image) models by Luma AI

43. **[desktop4mistral](https://github.com/hathibelagal-dev/desktop4mistral)** - ⭐ 18
   A desktop client with MCP support for Mistral LLMs

44. **[fast-mcp-client](https://github.com/aswincandra/fast-mcp-client)** - ⭐ 11
   MCP Client Implemented to FastAPI

45. **[pic-standard](https://github.com/madeinplutofabio/pic-standard)** - ⭐ 11
   The industry standard for Provenance & Intent Contracts (PIC) in Agentic AI. Bridging the Causal Gap in autonomous systems.

46. **[novelcrafter-mcp](https://github.com/deadshot465/novelcrafter-mcp)** - ⭐ 10
   An experimental desktop client for using Claude Desktop's MCP with Novelcrafter codices.

47. **[chatbot-spring-ai-mcp-telegram-client](https://github.com/mohamedYoussfi/chatbot-spring-ai-mcp-telegram-client)** - ⭐ 10

### Tools & Libraries

*Development tools and libraries for working with MCP*

1. **[n8n](https://github.com/n8n-io/n8n)** - ⭐ 176,613
   Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

2. **[kong](https://github.com/Kong/kong)** - ⭐ 42,841
   🦍 The API and AI Gateway

3. **[FastGPT](https://github.com/labring/FastGPT)** - ⭐ 27,195
   FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

4. **[kratos](https://github.com/go-kratos/kratos)** - ⭐ 25,476
   Your ultimate Go microservices framework for the cloud-native era.

5. **[excelize](https://github.com/qax-os/excelize)** - ⭐ 20,340
   Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

6. **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** - ⭐ 18,141
   Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

7. **[plate](https://github.com/udecode/plate)** - ⭐ 15,964
   Rich-text editor with AI, MCP, and shadcn/ui

8. **[LangBot](https://github.com/langbot-app/LangBot)** - ⭐ 14,244
   Production-grade platform for building IM bots / 生产级即时通信机器人开发平台. Bots for QQ / QQ频道 / Discord / LINE / WeChat(微信, 企业微信)/ Telegram / 飞书 / 钉钉 / Slack e.g. Integrated with ChatGPT(GPT), DeepSeek, Dify, n8n, Langflow, Coze, Claude, Google Gemini, Nano Banana, Kimi, PPIO, Ollama, MiniMax, SiliconFlow, Qwen, Moonshot, MCP etc. LLM & Agent & RAG

9. **[Fay](https://github.com/xszyou/Fay)** - ⭐ 12,179
   fay是一个帮助数字人（2.5d、3d、移动、pc、网页）或大语言模型（openai兼容、deepseek）连通业务系统的mcp框架。

10. **[ui](https://github.com/creativetimofficial/ui)** - ⭐ 11,723
   Open-source components, blocks, and AI agents designed to speed up your workflow. Import them seamlessly into your favorite tools through Registry and MCPs.

11. **[note-gen](https://github.com/codexu/note-gen)** - ⭐ 10,953
   A cross-platform Markdown AI note-taking software.

12. **[langchain4j](https://github.com/langchain4j/langchain4j)** - ⭐ 10,851
   LangChain4j is an open-source Java library that simplifies the integration of LLMs into Java applications through a unified API, providing access to popular LLMs and vector databases. It makes implementing RAG, tool calling (including support for MCP), and agents easy. LangChain4j integrates seamlessly with various enterprise Java frameworks.

13. **[astron-agent](https://github.com/iflytek/astron-agent)** - ⭐ 9,504
   Enterprise-grade, commercial-friendly agentic workflow platform for building next-generation SuperAgents.

14. **[OpenMetadata](https://github.com/open-metadata/OpenMetadata)** - ⭐ 8,774
   OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration.

15. **[53AIHub](https://github.com/53AI/53AIHub)** - ⭐ 8,479
   53AI Hub is an open-source AI portal, which enables you to quickly build a operational-level AI portal to launch and operate AI agents, prompts, and AI tools. It supports seamless integration with development platforms like Coze, Dify, FastGPT, RAGFlow.

16. **[Upsonic](https://github.com/Upsonic/Upsonic)** - ⭐ 7,797
   Agent Framework For Fintech and Banks

17. **[lamda](https://github.com/firerpa/lamda)** - ⭐ 7,630
    The most powerful Android RPA agent framework, next generation of mobile automation robots.

18. **[adk-go](https://github.com/google/adk-go)** - ⭐ 7,029
   An open-source, code-first Go toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

19. **[Viper](https://github.com/FunnyWolf/Viper)** - ⭐ 4,973
   Adversary simulation and Red teaming platform with AI

20. **[magic](https://github.com/dtyq/magic)** - ⭐ 4,469
   Super Magic. The first open-source all-in-one AI productivity platform (Generalist AI Agent + Workflow Engine + IM + Online collaborative office system)

21. **[Yuxi-Know](https://github.com/xerrors/Yuxi-Know)** - ⭐ 4,387
   结合LightRAG 知识库的知识图谱智能体平台。 An agent platform that integrates a LightRAG knowledge base and knowledge graphs. Build with LangChain v1 + Vue + FastAPI, support DeepAgents、MinerU PDF、Neo4j 、MCP.

22. **[ENScan_GO](https://github.com/wgpsec/ENScan_GO)** - ⭐ 4,223
   一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入

23. **[ag2](https://github.com/ag2ai/ag2)** - ⭐ 4,197
   AG2 (formerly AutoGen): The Open-Source AgentOS. Join us at: https://discord.gg/sNGSwQME3x

24. **[nexent](https://github.com/ModelEngine-Group/nexent)** - ⭐ 4,057
   Nexent is a zero-code platform for auto-generating agents — no orchestration, no complex drag-and-drop required. Nexent also offers powerful capabilities for agent running control, data processing and MCP tools.

25. **[kubefwd](https://github.com/txn2/kubefwd)** - ⭐ 4,051
   Bulk port forwarding Kubernetes services for local development.

26. **[manifest](https://github.com/mnfst/manifest)** - ⭐ 3,309
   A shadcn/ui library for building ChatGPT Apps and MCP Apps

27. **[semantic-router](https://github.com/vllm-project/semantic-router)** - ⭐ 3,240
   System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge

28. **[Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)** - ⭐ 2,800
   Multi-modal Generative Media Skills for AI Agents (Claude Code, Cursor, Gemini CLI). High-quality image, video, and audio generation powered by muapi.ai.

29. **[solon](https://github.com/opensolon/solon)** - ⭐ 2,708
   🔥 Java enterprise application development framework for full scenario: Restrained, Efficient, Open, Ecologicalll!!! 700% higher concurrency 50% memory savings Startup is 10 times faster. Packing 90% smaller; Compatible with java8 ~ java25; Supports LTS. (Replaceable spring)

30. **[ultracite](https://github.com/haydenbleasel/ultracite)** - ⭐ 2,707
   A highly opinionated, zero-configuration linter and formatter.

31. **[harbor](https://github.com/av/harbor)** - ⭐ 2,470
   One command brings a complete pre-wired LLM stack with hundreds of services to explore.

32. **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** - ⭐ 1,903
   ✨ Agentic chat experience in your terminal. Build applications using natural language.

33. **[generative-ai](https://github.com/genieincodebottle/generative-ai)** - ⭐ 1,792
   Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation.

34. **[MinecraftDev](https://github.com/minecraft-dev/MinecraftDev)** - ⭐ 1,716
   Plugin for IntelliJ IDEA that gives special support for Minecraft modding projects.

35. **[d2mcpp](https://github.com/mcpp-community/d2mcpp)** - ⭐ 1,556
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

36. **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** - ⭐ 1,488
   MultiAgentPPT 是一个集成了 A2A（Agent2Agent）+ MCP（Model Context Protocol）+ ADK（Agent Development Kit） 架构的智能化演示文稿生成系统，支持通过多智能体协作和流式并发机制

37. **[mcpelauncher-manifest](https://github.com/minecraft-linux/mcpelauncher-manifest)** - ⭐ 1,455
   The main repository for the Linux and Mac OS Bedrock edition Minecraft launcher.

38. **[mcpp-standard](https://github.com/Sunrisepeak/mcpp-standard)** - ⭐ 1,372
   D2X | Modern C++ Core Language Features - "A C++ tutorial project focused on practical"

39. **[paperdebugger](https://github.com/PaperDebugger/paperdebugger)** - ⭐ 1,341
   A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing

40. **[NagaAgent](https://github.com/Xxiii8322766509/NagaAgent)** - ⭐ 1,325
   A simple yet powerful agent framework for personal assistants, designed to enable intelligent interaction, multi-agent collaboration, and seamless tool integration.

41. **[awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists)** - ⭐ 1,292
   A curated collection of top-tier penetration testing tools and productivity utilities across multiple domains. Join us to explore, contribute, and enhance your hacking toolkit!

42. **[BuildingAI](https://github.com/BidingCC/BuildingAI)** - ⭐ 1,229
   BuildingAI is an enterprise-grade open-source intelligent agent platform designed for AI developers, AI entrepreneurs, and forward-thinking organizations. Through a visual configuration interface (Do It Yourself), you can build native enterprise AI applications without code. The platform offers native capabilities such as intelligent agents, MCP...

43. **[langchain4j-aideepin](https://github.com/moyangzhan/langchain4j-aideepin)** - ⭐ 1,169
   基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

44. **[AWorld](https://github.com/inclusionAI/AWorld)** - ⭐ 1,134
   Build, evaluate and train General Multi-Agent Assistance with ease

45. **[any-agent](https://github.com/mozilla-ai/any-agent)** - ⭐ 1,107
   A single interface to use and evaluate different agent frameworks 

46. **[Gearboy](https://github.com/drhelius/Gearboy)** - ⭐ 1,082
   Game Boy / Gameboy Color emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

47. **[AIPex](https://github.com/AIPexStudio/AIPex)** - ⭐ 1,077
   AIPex: AI browser automation assistant, no migration and privacy first. Alternative to Manus Browser Operator、 Claude Chrome and Agent Browser

48. **[chunkhound](https://github.com/chunkhound/chunkhound)** - ⭐ 1,065
   Local first codebase intelligence

49. **[open-trading-api](https://github.com/koreainvestment/open-trading-api)** - ⭐ 1,059
   Korea Investment & Securities Open API Github

50. **[zen](https://github.com/sheshbabu/zen)** - ⭐ 1,052
   Selfhosted notes app. Single golang binary, notes stored as markdown within SQLite, full-text search, very low resource usage

51. **[openops](https://github.com/openops-cloud/openops)** - ⭐ 994
   The batteries-included, No-Code FinOps automation platform, with the AI you trust.

52. **[arduino-mcp2515](https://github.com/autowp/arduino-mcp2515)** - ⭐ 967
   Arduino MCP2515 CAN interface library

53. **[rulesync](https://github.com/dyoshikawa/rulesync)** - ⭐ 830
   A Utility CLI for AI Coding Agents

54. **[voicemode](https://github.com/mbailey/voicemode)** - ⭐ 793
   Natural voice conversations with Claude Code

55. **[claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)** - ⭐ 773
   A Claude MCP tool to interact with the ChatGPT desktop app on macOS

56. **[aderyn](https://github.com/Cyfrin/aderyn)** - ⭐ 733
   Solidity Static Analyzer that easily integrates into your editor

57. **[bytechef](https://github.com/bytechefhq/bytechef)** - ⭐ 732
   Open-source, AI-native, low-code platform for API orchestration, workflow automation, and AI agent integration across internal systems and SaaS products.

58. **[MCPELauncher](https://github.com/zhuowei/MCPELauncher)** - ⭐ 730
   Source code for BlockLauncher, a launcher that patches Minecraft for Android

59. **[JiwuChat](https://github.com/KiWi233333/JiwuChat)** - ⭐ 699
   JiwuChat 🍂 : 轻量级跨平台IM聊天应用，集成AI机器人( DeepSeek/Gemini/Kimi... )、音视频通话及AI购物。支持多端消息同步，自定义主题，高效便捷  🍒

60. **[Sentient](https://github.com/existence-master/Sentient)** - ⭐ 675
   A personal AI assistant for everyone

61. **[infio-copilot](https://github.com/infiolab/infio-copilot)** - ⭐ 645
   A Cursor-inspired AI assistant for Obsidian that offers smart autocomplete and interactive chat with your selected notes

62. **[WHartTest](https://github.com/MGdaasLab/WHartTest)** - ⭐ 642
   WHartTest 是基于 Django REST Framework 与现代大模型技术打造的 AI 驱动测试自动化平台。平台聚合自然语言理解、知识库检索与嵌入搜索能力，结合 LangChain 与 MCP（Model Context Protocol） 工具调用，实现从需求到可执行测试用例的自动化生成与管理，帮助测试团队提升效率与覆盖率。

63. **[chatlog_alpha](https://github.com/teest114514/chatlog_alpha)** - ⭐ 622
   原 [chatlog]项目（一个微信数据库读取及提供mcp服务开源软件）的二次开发，会尽可能同步最新开源解密源码

64. **[IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP)** - ⭐ 607
   Say goodbye to the complex, verbose, and laggy interaction mode of IDA Pro MCP

65. **[LightAgent](https://github.com/wanxingai/LightAgent)** - ⭐ 606
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

66. **[cloudsword](https://github.com/wgpsec/cloudsword)** - ⭐ 596
   一款帮助云租户发现和测试云上风险、增强云上防护能力的综合性开源工具

67. **[ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill)** - ⭐ 541
   An IOS Simulator Skill for ClaudeCode. Use it to optimise Claude's ability to build, run and interact with your apps, without using up any of the available token/context budget.

68. **[tool-ui](https://github.com/assistant-ui/tool-ui)** - ⭐ 538
   UI components for AI interfaces

69. **[marmot](https://github.com/marmotdata/marmot)** - ⭐ 524
   Marmot helps teams discover, understand, and leverage their data with powerful search and lineage visualisation tools. It's designed to make data accessible for everyone.

70. **[auto-commenter](https://github.com/rokpiy/auto-commenter)** - ⭐ 512
   A Claude skill that automatically posts personalized, authentic comments in your target communities.

71. **[ai-code-helper](https://github.com/liyupi/ai-code-helper)** - ⭐ 485
   2025 年 AI 编程助手实战项目（作者：程序员鱼皮），基于 Spring Boot 3.5 + Java 21 + LangChain4j + AI 构建智能编程学习与求职辅导机器人，覆盖 AI 大模型接入、LangChain4j 核心特性、流式对话、Prompt 工程、RAG 检索增强、向量数据库、Tool Calling 工具调用、MCP 模型上下文协议、Web 爬虫、安全防护、Vue.js 前端开发、SSE 服务端推送等企业级 AI 应用开发技术。帮助开发者掌握 AI 时代必备技能，熟悉 LangChain 框架，提升编程学习效率和求职竞争力，成为企业需要的 AI 全栈开发人才。

72. **[AIWriteX](https://github.com/iniwap/AIWriteX)** - ⭐ 465
   AIWriteX是基于CrewAI、AIForge的新一代智能内容创作平台，从微信公众号自动化工具起步，正在重新定义AI辅助内容创作的边界，融合"AI+创意+搜索+借鉴"四重能力，多种超绝玩法，内容创作充满无限可能。

73. **[browser-operator-core](https://github.com/BrowserOperator/browser-operator-core)** - ⭐ 459
   Browser Operator - The AI browser with built in Multi-Agent platform! Open source alternative to ChatGPT Atlas, Perplexity Comet, Dia and Microsoft CoPilot Edge Browser

74. **[LightAgent](https://github.com/wxai-space/LightAgent)** - ⭐ 430
   LightAgent: Lightweight AI agent framework with memory, tools & tree-of-thought. Supports multi-agent collaboration, self-learning, and major LLMs (OpenAI/DeepSeek/Qwen). Open-source with MCP/SSE protocol integration.

75. **[mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)** - ⭐ 413
   这是一个为大模型提供 A 股数据的的 MCP(Model Content Protocol) 服务。

76. **[groundhog](https://github.com/ghuntley/groundhog)** - ⭐ 393
   Groundhog's primary purpose is to teach people how Cursor and all these other coding agents work under the hood. If you understand how these coding assistants work from first principles, then you can drive these tools harder (or perhaps make your own!).

77. **[mcpi](https://github.com/martinohanlon/mcpi)** - ⭐ 389
   Minecraft: Pi Edition API Python Library

78. **[bridle](https://github.com/neiii/bridle)** - ⭐ 389
   TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

79. **[volcano-agent-sdk](https://github.com/Kong/volcano-agent-sdk)** - ⭐ 387
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

80. **[volcano-sdk](https://github.com/Kong/volcano-sdk)** - ⭐ 386
   🌋 Build AI agents that seamlessly combine LLM reasoning with real-world actions via MCP tools — in just a few lines of TypeScript.

81. **[azan-mcp](https://github.com/ahmedeltaher/azan-mcp)** - ⭐ 382
   Azan + Prayer Time + MCP + AI Agents + Islamic + Salah + A lightweight MCP library to calculate prayer times and trigger Azan with a single tool call. If you’re building an AI agent or prayer application, there’s no need to deal with astronomical calculations, timezones, or edge cases again.

82. **[ChattyPlay-Agent](https://github.com/P1kaj1uu/ChattyPlay-Agent)** - ⭐ 381
   本项目基于React+TypeScript+Hono实现，实现Google、Github授权登录，已接入OpenAI SDK、MCP服务和Agent相关大模型，扩展实时黄金和K线图，获取Hugging Face论文，以及文生图服务(无需再代理和APIKey)，同时支持腾讯视频、爱奇艺、优酷、芒果TV、哔哩哔哩、网易云音乐等平台会员视频破解可在线解析、动漫漫画畅享阅读和论文降重（适配PC端、移动端）

83. **[Adafruit-MCP23017-Arduino-Library](https://github.com/adafruit/Adafruit-MCP23017-Arduino-Library)** - ⭐ 376
   Arduino Library for Adafruit MCP23017

84. **[pokemon-chat](https://github.com/skygazer42/pokemon-chat)** - ⭐ 368
   基于 LightRAG、LangGraph、MCP、RagFlow、微调LLMs宝可梦主题的智能聊天助手

85. **[graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)** - ⭐ 364
   Python toolkit for building graph-enhanced GenAI applications

86. **[pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents)** - ⭐ 360
   Python Deep Agent framework built on top of Pydantic-AI, designed to help you quickly build production-grade autonomous AI agents with planning, filesystem operations, subagent delegation, skills, and structured outputs—in just 10 lines of code.

87. **[UE5-MCP](https://github.com/VedantRGosavi/UE5-MCP)** - ⭐ 348
   MCP for Unreal Engine 5

88. **[exograph](https://github.com/exograph/exograph)** - ⭐ 343
   Build production-ready backends in minutes

89. **[MCprep](https://github.com/Moo-Ack-Productions/MCprep)** - ⭐ 342
   Blender python addon to increase workflow for creating minecraft renders and animations

90. **[depyler](https://github.com/paiml/depyler)** - ⭐ 335
   Compiles Python to Rust, helping transition off of Python to Energy Efficient and Safe Rust Code

91. **[eechat](https://github.com/Lucassssss/eechat)** - ⭐ 335
   🚀 Powerful Local AI Chat Application - Mcp, Secure, Efficient, Personalized 本地化部署的大模型客户端

92. **[CookHero](https://github.com/Decade-qiu/CookHero)** - ⭐ 335
   CookHero是一个基于 LLM + RAG + Agent + 多模态的智能饮食与烹饪管理平台，支持智能菜谱查询、个性化饮食计划、AI 饮食记录、营养分析、Web 搜索增强，以及可扩展的 ReAct Agent / Subagent 工具体系，帮助厨房新手轻松成为“烹饪英雄”。

93. **[Gearsystem](https://github.com/drhelius/Gearsystem)** - ⭐ 324
   Sega Master System / Game Gear / SG-1000 emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

94. **[MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController)** - ⭐ 319
   Drop-in panel control for iOS with blurring background and screen-edge activation gestures.

95. **[news-agents](https://github.com/eugeneyan/news-agents)** - ⭐ 312
   📰 Building News Agents to Summarize News with MCP, Q, and tmux

96. **[awesome-slash](https://github.com/avifenesh/awesome-slash)** - ⭐ 312
   AI writes code. This automates everything else. 9 plugins · 39 agents · 24 skills · for Claude Code, OpenCode, Codex.

97. **[napi](https://github.com/nanoapi-io/napi)** - ⭐ 296
   Software architecture tooling for the AI age

98. **[building-an-agentic-system](https://github.com/gerred/building-an-agentic-system)** - ⭐ 290
   An in-depth book and reference on building agentic systems like Claude Code

99. **[ai4eh](https://github.com/ethiack/ai4eh)** - ⭐ 275
   AI for Ethical Hacking - Workshop

100. **[MCPDict](https://github.com/MaigoAkisame/MCPDict)** - ⭐ 259
   Android App: 漢字古今中外讀音查詢

101. **[oreilly-ai-agents](https://github.com/sinanuozdemir/oreilly-ai-agents)** - ⭐ 254
   An introduction to the world of AI Agents

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

107. **[Minecraft-Deobfuscator3000](https://github.com/SimplyProgrammer/Minecraft-Deobfuscator3000)** - ⭐ 235
   Powerful and universal deobfuscator for Minecraft mods and java decompiler!

108. **[MCPU](https://github.com/cpldcpu/MCPU)** - ⭐ 233
   MCPU - A Minimal 8Bit CPU in a 32 Macrocell CPLD

109. **[stock-scanner-mcp](https://github.com/wbsu2003/stock-scanner-mcp)** - ⭐ 231
   这是一个基于 FastAPI-MCP 的股票分析服务，旨在通过 MCP 工具函数接口提供股票相关的综合数据和分析能力，包括价格、评分、技术报告和 AI 分析。

110. **[mcpfp](https://github.com/MauritsWilke/mcpfp)** - ⭐ 221
   A website to generate Minecraft profile pictures

111. **[AuditLuma](https://github.com/Vistaminc/AuditLuma)** - ⭐ 217
   AuditLuma是一个AI+智能体代码审计系统，它利用多个AI代理和先进的技术，包括多代理合作协议（MCP）和Self-RAG（检索增强生成），为代码库提供全面的安全分析，目前已经支持ollama部署的本地大模型

112. **[McPicker-iOS](https://github.com/kmcgill88/McPicker-iOS)** - ⭐ 215
   McPicker is a customizable, closure driven UIPickerView drop-in solution with animations that is rotation ready.

113. **[Toucan](https://github.com/TheAgentArk/Toucan)** - ⭐ 215
   Official repo of Toucan: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

114. **[langchain_data_agent](https://github.com/eosho/langchain_data_agent)** - ⭐ 215
   NL2SQL - Ask questions in plain English, get SQL queries and results. Powered by LangGraph.

115. **[mcpat](https://github.com/HewlettPackard/mcpat)** - ⭐ 209
   An integrated power, area, and timing modeling framework for multicore and manycore architectures

116. **[weam](https://github.com/weam-ai/weam)** - ⭐ 206
   Web app for teams of 20+ members. In-built connections to major LLMs via API. Share chats, prompts, and agents in team or private folders. Modern, fully responsive stack (Next.js, Node.js). Deploy your own vibe-coded AI apps, agents, or workflows—or use ready-made solutions from the library.

117. **[BaseLayer](https://github.com/zwgnr/BaseLayer)** - ⭐ 201
   Re-usable multi part components built on React Aria and TailwindCSS. 

118. **[MCP-919](https://github.com/Marcelektro/MCP-919)** - ⭐ 190
   Fully working & decompiled MCP for Minecraft 1.8.9 

119. **[MCPScan](https://github.com/antgroup/MCPScan)** - ⭐ 189

120. **[cupcake](https://github.com/eqtylab/cupcake)** - ⭐ 187
   A native policy enforcement layer for AI coding agents. Built on OPA/Rego.

121. **[mangaba_ai](https://github.com/Mangaba-ai/mangaba_ai)** - ⭐ 184
   Repositório minimalista para criação de agentes de IA inteligentes e versáteis com protocolos A2A (Agent-to-Agent) e MCP (Model Context Protocol).

122. **[agentic-ai-systems](https://github.com/ThibautMelen/agentic-ai-systems)** - ⭐ 179
   🐔 Agentic systems explained with chickens. Workflows, agents & orchestration made simple. Mermaid diagrams included

123. **[Weave](https://github.com/liaotxcn/Weave)** - ⭐ 178
   A highly efficient, secure, and stable application development platform with excellent performance, easy scalability, and deep integration of AI capabilities such as LLM, AI Chat, RAG, and Agents.高效、安全、稳定的服务研发平台，具备良好性能，同时易扩展，深度集成LLM、AIChat、RAG、Agent等AI能力

124. **[bluebox-sdk](https://github.com/VectorlyApp/bluebox-sdk)** - ⭐ 169
   Reverse engineer web apps

125. **[x-mcp](https://github.com/xpzouying/x-mcp)** - ⭐ 169
   小红书创作中心

126. **[codecompanion-history.nvim](https://github.com/ravitemer/codecompanion-history.nvim)** - ⭐ 166
   A history management extension for codecompanion AI chat plugin that enables saving, browsing and restoring chat sessions.

127. **[ZenOps](https://github.com/opsre/ZenOps)** - ⭐ 155
   🧘 通过钉钉、飞书、企微智能机器人用自然语言查询运维资源的工具。

128. **[rocketship](https://github.com/rocketship-ai/rocketship)** - ⭐ 140
   A QA testing framework for your coding agent.

129. **[mcp-audit](https://github.com/apisec-inc/mcp-audit)** - ⭐ 140
   See what your AI agents can access. Scan MCP configs for exposed secrets, shadow APIs, and AI models. Generate AI-BOMs for compliance.

130. **[toon-java](https://github.com/toon-format/toon-java)** - ⭐ 139
   ☕ Community-driven Java implementation of TOON

131. **[mcp-toolkit](https://github.com/charIesding/mcp-toolkit)** - ⭐ 137
   utilities for mcp

132. **[awesome-ai-repositories](https://github.com/altengineer/awesome-ai-repositories)** - ⭐ 126
   A curated list of open source repositories for AI Engineers

133. **[Z.ai2api](https://github.com/hmjz100/Z.ai2api)** - ⭐ 126
   将 Z.ai Chat 代理为 OpenAI/Anthropic Compatible 格式，支持多模型列表映射、免令牌、智能处理思考链、图片上传等功能；Z.ai ZtoApi z2api ZaitoApi zai X-Signature 签名 GLM 4.5 v 4.6

134. **[claude-ipc-mcp](https://github.com/jdez427/claude-ipc-mcp)** - ⭐ 125
   AI-to-AI communication protocol for Claude, Gemini, and other AI assistants

135. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/sdivyanshu90/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 117
   5-Day Gen AI Intensive Course with Google

136. **[AgentNexus](https://github.com/wozhenbang2004/AgentNexus)** - ⭐ 113
   Multi-Agent,MCP,RAG,SpringAI1.0.0,RE-ACT

137. **[STAMP](https://github.com/KatherLab/STAMP)** - ⭐ 113
   Solid Tumor Associative Modeling in Pathology

138. **[Gearcoleco](https://github.com/drhelius/Gearcoleco)** - ⭐ 109
   ColecoVision emulator and debugger for macOS, Windows, Linux, BSD and RetroArch.

139. **[AgentFly](https://github.com/Agent-One-Lab/AgentFly)** - ⭐ 109
   Scalable and extensible reinforcement learning for LM agents.

140. **[protocol-launcher](https://github.com/zhensherlock/protocol-launcher)** - ⭐ 109
   One-click launch URL generator for protocol-based apps

141. **[5-Day-AI-Agents-Intensive-Course-with-Google](https://github.com/anxiong2025/5-Day-AI-Agents-Intensive-Course-with-Google)** - ⭐ 107
   谷歌5天AI Agents强化课程

142. **[kalouk-mcp](https://github.com/fabianabarca/kalouk-mcp)** - ⭐ 106
   Servidor de contexto de Kalouk para agentes de inteligencia artificial.

143. **[mcp-in-action](https://github.com/huangjia2019/mcp-in-action)** - ⭐ 104
   极客时间MCP新课已经上线！超2000同学一起开启MCP学习之旅！

144. **[Squirrel](https://github.com/hakoniwaa/Squirrel)** - ⭐ 92
   ai memory for coding

145. **[coplay-unity-plugin](https://github.com/CoplayDev/coplay-unity-plugin)** - ⭐ 90
   Unity plugin for Coplay

146. **[Complementarity.jl](https://github.com/chkwon/Complementarity.jl)** - ⭐ 79
   provides a modeling interface for mixed complementarity problems (MCP) and math programs with equilibrium problems (MPEC) via JuMP 

147. **[smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system)** - ⭐ 78
   构建一个基于大模型的智能客服系统，可提供静态知识问答(静态数据)、动态知识问答（数据库），业务办理（api调用）等功能，同时系统具有自我学习能力。定期的反思可让系统变得更强大。

148. **[TensorBlock-Studio](https://github.com/TensorBlock/TensorBlock-Studio)** - ⭐ 75
   A lightweight, open, and extensible multi-LLM interaction studio.

149. **[nvim-gemini-companion](https://github.com/gutsavgupta/nvim-gemini-companion)** - ⭐ 75
   A Neovim plugin to integrate Gemini CLI well (+ Qwen-code now)

150. **[onemcp-hub](https://github.com/ipenywis/onemcp-hub)** - ⭐ 73
   OneMCP feature requests, bugs and improvements 

151. **[lycoris](https://github.com/solaoi/lycoris)** - ⭐ 73
   Real-time speech recognition & AI-powered note-taking app for macOS with offline/online modes, multilingual transcription, and Japanese translation support.

152. **[quarkus-workshop-langchain4j](https://github.com/quarkusio/quarkus-workshop-langchain4j)** - ⭐ 73
   Quarkus Langchain4J Workshop

153. **[tiktok-mcp](https://github.com/yap-audio/tiktok-mcp)** - ⭐ 66
   A Model Context Protocol service for TikTok video discovery and metadata extraction.

154. **[claude-code-buddy](https://github.com/PCIRCLE-AI/claude-code-buddy)** - ⭐ 64
   MeMesh Plugin — Searchable project memory plugin for Claude Code.

155. **[seekchat](https://github.com/seekrays/seekchat)** - ⭐ 62
   ✨ A Sleek and Powerful AI Desktop Assistant that supports MCP integration✨

156. **[Roomey_AI_Voice_Agent](https://github.com/augmentedstartups/Roomey_AI_Voice_Agent)** - ⭐ 61
   Roomey is a multi-purpose Voice Agent designed to run your personal and business life.

157. **[Grapheteria](https://github.com/beubax/Grapheteria)** - ⭐ 60
   Grapheteria: A structured framework bringing uniformity to agent orchestration!

158. **[OneCite](https://github.com/HzaCode/OneCite)** - ⭐ 56
   📚 An intelligent toolkit to automatically parse, complete, and format academic references.

159. **[chm-converter](https://github.com/DTDucas/chm-converter)** - ⭐ 51
   chm to markdown and vectorDB

160. **[houdini-mcp](https://github.com/capoom/houdini-mcp)** - ⭐ 50
   Houdini integration through the Model Context Protocol

161. **[mcp-java8-sdk](https://github.com/krrr/mcp-java8-sdk)** - ⭐ 46
   Backported Model Context Protocol SDK for Java 8

162. **[asya](https://github.com/deliveryhero/asya)** - ⭐ 40
   🎭 Actors on Kubernetes for scalable Gen AI

163. **[ummon](https://github.com/Nayshins/ummon)** - ⭐ 37
   The semantic layer for software engineering: Connect   code to meaning, build on understanding

164. **[prompt-pro](https://github.com/timothywarner-org/prompt-pro)** - ⭐ 35
   Master AI prompting for business innovation. O'Reilly Live Learning course by Tim Warner covering ChatGPT, Claude, Copilot, and enterprise prompt engineering with MCP implementation.

165. **[xiaozhi-MCPTools](https://github.com/ZhongZiTongXue/xiaozhi-MCPTools)** - ⭐ 35
   一个图形化界面的小智MCP服务连接器，包含多种工具！ 自动部署服务，方便小白给小智Ai添加MCP工具

166. **[Wireshark_mcp](https://github.com/jayimu/Wireshark_mcp)** - ⭐ 34
   Wireshark MCP 是一个基于 Model Context Protocol (MCP) 的服务器，允许 AI 助手通过 tshark 命令行工具进行交互。该工具提供了丰富的网络数据分析功能，支持实时抓包和离线分析。

167. **[advanced-reason-mcp](https://github.com/Kuon-dev/advanced-reason-mcp)** - ⭐ 33
   Enhanced version of "Sequential Thinking" MCP

168. **[zentrun](https://github.com/andrewsky-labs/zentrun)** - ⭐ 32
   Prompt-driven automation platform - Transform natural language into executable workflows

169. **[awesome-mcp-list](https://github.com/notedit/awesome-mcp-list)** - ⭐ 28
   Awesome Model Context Protocol Service List

170. **[shebe](https://github.com/shebe-oss/shebe)** - ⭐ 28
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

171. **[adk-mcp-gemma3](https://github.com/arjunprabhulal/adk-mcp-gemma3)** - ⭐ 27
   Build AI Agent using Google ADK , MCP and Gemma 3 model

172. **[shebe](https://github.com/rhobimd-oss/shebe)** - ⭐ 26
   Fast BM25 full-text search for code repositories with MCP integration for AI coding agents.

173. **[hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298](https://github.com/LinkedInLearning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a-6055298)** - ⭐ 26
   this repo is for linkedin learning course: Hands-On AI: Building AI Agents with Model Context Protocol (MCP) and Agent2Agent (A2A)

174. **[codai](https://github.com/codai-agent/codai)** - ⭐ 24
   Codai is an AI programming tool that boosts coding efficiency and empowers non-programmers. Its future plans include introducing a local database, enabling customization, and building a versatile AI terminal. It aims to popularize AI programming and lead the AI Programming+ era.

175. **[minime-mcp](https://github.com/manujbawa/minime-mcp)** - ⭐ 21
   Universal infinite memory layer for Developer AI assistants. One shared brain across Claude, Cursor, Windsurf & more. 100% local, built on MCP standard. Stop re-explaining context

176. **[cursor-like-pro](https://github.com/gifflet/cursor-like-pro)** - ⭐ 17
   Cursor IDE like Pro

177. **[MCPStack](https://github.com/MCP-Pipeline/MCPStack)** - ⭐ 16
   Stack & Orchestrate MCP Tools — The Scikit-Learn-Pipeline Way , For LLMs

178. **[mcp-labs](https://github.com/thangchung/mcp-labs)** - ⭐ 16
   All things about MCP experiments.⭐️ Star to support our work!

179. **[QCX](https://github.com/QueueLab/QCX)** - ⭐ 16
   Language to Maps

180. **[n8n-operator](https://github.com/jakub-k-slys/n8n-operator)** - ⭐ 15
   Kubernetes Operator for N8n, a fair-code workflow automation platform with native AI capabilities.

181. **[ai-agents](https://github.com/rjmurillo/ai-agents)** - ⭐ 14
   Multi-agent system for software development

182. **[ai-tools](https://github.com/elsejj/ai-tools)** - ⭐ 14
   ai-tools  call your llm based tools through shortcut (ctrl-q) in any application

183. **[feather_wand_agent](https://github.com/QAInsights/feather_wand_agent)** - ⭐ 13
   Feather Wand Agent is a comprehensive AI-powered toolkit for performance testing and monitoring. It integrates multiple industry-standard performance testing tools (JMeter, k6, Gatling, and Locust) into a single, unified interface, allowing users to execute and analyze performance tests through natural language interactions.

184. **[mkinf-run](https://github.com/mkinf-io/mkinf-run)** - ⭐ 13
   mkinf run API

185. **[velocity](https://github.com/OptimiLabs/velocity)** - ⭐ 13
   Local-first workspace for Claude Code, Codex CLI, and Gemini CLI with sessions, analytics, workflows, and tools

186. **[mcp-tools](https://github.com/shaharia-lab/mcp-tools)** - ⭐ 11
   Tools for MCP (Model Context Protocol) written in Go

187. **[Unity-AI-Tools-Template](https://github.com/IvanMurzak/Unity-AI-Tools-Template)** - ⭐ 11
   Unity MCP Tool template project

### Examples

*Example projects demonstrating MCP usage*

1. **[YC-Killer](https://github.com/sahibzada-allahyar/YC-Killer)** - ⭐ 2,660
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

2. **[AI-Agents-Library](https://github.com/sahibzada-allahyar/AI-Agents-Library)** - ⭐ 2,610
   A library of enterprise-grade AI agents designed to democratize artificial intelligence and provide free, open-source alternatives to overvalued Y Combinator startups. If you are excited about democratizing AI access & AI agents, please star ⭐️ this repository and use the link in the readme to join our open source AI research team.

3. **[claude-mcp-examples](https://github.com/charIesding/claude-mcp-examples)** - ⭐ 151
   examples of claude with mcp integration

4. **[End-to-End-Agentic-Ai-Automation-Lab](https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab)** - ⭐ 50
   This repository contains hands-on projects, code examples, and deployment workflows. Explore multi-agent systems, LangChain, LangGraph, AutoGen, CrewAI, RAG, MCP, automation with n8n, and scalable agent deployment using Docker, AWS, and BentoML.

5. **[claude-mcp](https://github.com/thinkbigcd/claude-mcp)** - ⭐ 11
   claude and mcp integration examples and tutorials

### Documentation

*Documentation, tutorials, and learning resources*

1. **[ai-guide](https://github.com/liyupi/ai-guide)** - ⭐ 8,105
   程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享大模型选择指南（DeepSeek / GPT / Gemini / Claude）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（RAG / MCP / A2A）、AI 编程教程、AI 工具用法（Cursor / Claude Code / OpenClaw / TRAE / Lovable / Agent Skills）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档版本，已升级为鱼皮 AI 导航网站

2. **[modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)** - ⭐ 7,316
   Specification and documentation for the Model Context Protocol

3. **[jar-analyzer](https://github.com/jar-analyzer/jar-analyzer)** - ⭐ 1,931
   Jar Analyzer - 一个 JAR 包 GUI 分析工具，方法调用关系搜索，方法调用链 DFS 算法分析，模拟 JVM 的污点分析验证 DFS 结果，字符串搜索，Java Web 组件入口分析，CFG 程序分析，JVM 栈帧分析，自定义表达式搜索，紧跟 AI 技术发展，支持 MCP 调用，支持 n8n 工作流，文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

4. **[LLM-Agents-Ecosystem-Handbook](https://github.com/oxbshw/LLM-Agents-Ecosystem-Handbook)** - ⭐ 494
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

10. **[Q4_learning](https://github.com/DanielHashmi/Q4_learning)** - ⭐ 14
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

